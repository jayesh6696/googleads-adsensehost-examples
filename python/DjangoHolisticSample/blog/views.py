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

"""Defines the views to be used in this application."""

from django.shortcuts import render_to_response, get_object_or_404, redirect
from blog.models import User, AdUnit
from blog.association import start_association
from blog.callback import handle_callback
import api_utils


def index(request):
    """Index view; lists all the available blogs."""
    latest_blogs = User.objects.order_by('name')[:5]
    return render_to_response('index.html', {'latest_blogs': latest_blogs})


def userblog(request, user_name):
    """Individual blog view, showing the blog entries."""
    user = get_object_or_404(User, name=user_name)
    return render_to_response('blog/userblog.html', {
        'user': user,
        'ad_units': AdUnit.objects.filter(user=user)
        }
    )


def admin(request, user_name):
    """Administration / configuration page for an individual blog."""
    user = get_object_or_404(User, name=user_name)
    return render_to_response('blog/admin.html', {'user': user})


def monetize(request, user_name):
    """Ephemeral view that handles the start of a new association."""
    user = get_object_or_404(User, name=user_name)
    association = start_association(user)
    return redirect(association.redirect_url)


def callback(request):
    """Ephemeral view that handles the callback at the end of signup."""
    service = api_utils.initialize_service()
    return handle_callback(service, request)
