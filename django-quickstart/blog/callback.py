#!/usr/bin/env python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Handle the full callback process for signup.

Performs various tasks, such as verifying the received token, retrieving and
choosing ad clients, creating ad units, and generating ad code.
"""

__author__ = 'sgomes@google.com (Sergio Gomes)'

from django.shortcuts import get_object_or_404, redirect, render
from oauth2client.anyjson import simplejson
import association
import api_utils
from blog.models import AdUnit, AssociationSession, User

MAX_PAGE_SIZE = 50


def handle_callback(service, request):
    """Handle a callback request from the signup process."""
    token = request.GET.get('token', '')
    try:
        result = association.verify_association(token)
    except Exception, e:
        return handle_error(request, e)

    association_session = get_object_or_404(
        AssociationSession,
        session_id=result['id']
    )
    if association_session.user is not None and 'accountId' in result:
        user = association_session.user
        # Store the user's account ID in the database.
        user.pub_id = result['accountId']
        user.save()
        # Get the AFC ad client for this publisher.
        try:
            afc_ad_client = get_afc_ad_client(service, user)
        except Exception, e:
            return handle_error(request, e)

        if afc_ad_client is None:
            return render(
                request,
                "blog/error.html",
                {"e": ['AFC ad client not found, cannot create ad unit.']}
            )


        # Get all ad units for this publisher, in case we already created one.
        ad_units = AdUnit.objects.filter(user=user)
        if not ad_units:
            # Create a new ad unit for this publisher.
            try:
                ad_unit = create_ad_unit(service, user, afc_ad_client)
            except Exception, e:
                return handle_error(request, e)
            # Generate ad code for this publisher and save it.
            try:
                generated_ad_code = generate_ad_code(
                    service, ad_unit, afc_ad_client, user)
            except Exception, e:
                return handle_error(request, e)
            ad_unit.generated_ad_code = generated_ad_code
            ad_unit.save()

    return redirect('userblog', user_name=user.name)


def get_afc_ad_client(service, user):
    """Use the API to retrieve the AFC ad client for an account."""
    request = service.accounts().adclients().list(
        accountId=user.pub_id,
        maxResults=MAX_PAGE_SIZE)

    afc_ad_client = None

    while request is not None:
        result = request.execute()
        if 'items' in result:
            # We got some items, look for the AFC one
            ad_clients = result['items']
            for ad_client in ad_clients:
                if ad_client['productCode'] == 'AFC':
                    afc_ad_client = ad_client
                    break
            request = service.adclients().list_next(request, result)
        else:
            # No ad clients found
            break

    return afc_ad_client


def create_ad_unit(service, user, ad_client):
    """Use the API to create a new ad unit."""
    ad_unit = {
        'name': 'SampleHost top ad',
        'contentAdsSettings': {
            'backupOption': {
                'type': 'COLOR',
                'color': 'ffffff'
            },
            'size': 'SIZE_728_90',
            'type': 'TEXT'
        },
        'customStyle': {
            'colors': {
                'background': 'ffffff',
                'border': '000000',
                'text': '000000',
                'title': '000000',
                'url': '0000ff'
            },
            'corners': 'SQUARE',
            'font': {
                'family': 'ACCOUNT_DEFAULT_FAMILY',
                'size': 'ACCOUNT_DEFAULT_SIZE'
            }
        }
    }

    # Use API to create ad unit.
    result = service.accounts().adunits().insert(
        adClientId=ad_client['id'],
        accountId=user.pub_id,
        body=ad_unit).execute()

    # Create local ad unit object and save to database.
    ad_unit = AdUnit(
        user=user,
        adsense_unit_id=result['id'])

    ad_unit.save()

    return ad_unit


def generate_ad_code(service, ad_unit, afc_ad_client, user):
    """Use the API to generate the ad code for an existing ad unit."""
    result = service.accounts().adunits().getAdCode(
        adUnitId=ad_unit.adsense_unit_id,
        adClientId=afc_ad_client['id'],
        accountId=user.pub_id).execute()

    return result['adCode']


def handle_error(request, e):
    """Handles an API exception, preparing it for display to the user."""
    if (e.content):
        content_obj = simplejson.loads(e.content)
        if ('error' in content_obj and 'errors' in content_obj['error']):
            return render(
                request,
                "blog/error.html",
                {"e": [x['message'] for x in content_obj['error']['errors']]}
            )
        else:
            return render(
                request,
                "blog/error.html",
                {"e": [str(e)]}
            )
