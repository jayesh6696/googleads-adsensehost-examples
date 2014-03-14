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

"""Auxiliary methods for starting and verifying association sessions."""

from blog.models import AssociationSession
import api_utils


def start_association(user):
    """Uses the API to start a new association session, and stores it."""
    service = api_utils.initialize_service()
    result = service.associationsessions().start(
      productCode='AFC',
      websiteUrl='www.examplehost.com/blog/%s' % user.name
    ).execute()

    session = AssociationSession(
      session_id=result['id'],
      user=user,
      redirect_url=result['redirectUrl'])

    session.save()
    return session


def verify_association(token):
    """Uses the API to verify an association session token."""
    service = api_utils.initialize_service()
    result = service.associationsessions().verify(token=token).execute()
    return result
