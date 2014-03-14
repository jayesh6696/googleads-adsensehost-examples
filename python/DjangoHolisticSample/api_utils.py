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

"""Auxiliary file for AdSense Host API usage.

Handles various tasks to do with authentication and initialization.
"""

__author__ = 'sgomes@google.com (Sergio Gomes)'

import os
import sys
from apiclient.discovery import build
import httplib2
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OOB_CALLBACK_URN
from oauth2client.file import Storage
from oauth2client.tools import run

# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = 'client_secrets.json'

# Helpful message to display in the browser if the CLIENT_SECRETS file
# is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the APIs Console <https://code.google.com/apis/console>.

""" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)

# Set up a Flow object to be used if we need to authenticate.
FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope='https://www.googleapis.com/auth/adsensehost',
    redirect_uri=OOB_CALLBACK_URN,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

# File which will store auth credentials, namely the access and refresh tokens.
FILE_NAME = 'adsensehost.dat'


def prepare_credentials():
    """Handles auth. Reuses credentialss if available or runs the auth flow."""

    # If the credentials don't exist or are invalid run through the native
    # client flow. The Storage object will ensure that if successful the good
    # Credentials will get written back to a file.
    storage = Storage(FILE_NAME)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = run(FLOW, storage)
    return credentials


def retrieve_service(http):
    """Retrieves an AdSense Host API service via the discovery service."""

    # Construct a service object via the discovery service.
    service = build("adsensehost", "v4.1", http=http)
    return service


def initialize_service():
    """Builds instance of service from discovery data and does auth."""

    # Create an httplib2.Http object to handle our HTTP requests.
    http = httplib2.Http()

    # Prepare credentials, and authorize HTTP object with them.
    credentials = prepare_credentials()
    http = credentials.authorize(http)

    # Retrieve service.
    return retrieve_service(http)


def main(argv):
    """Authenticate and construct service, to prepare credentials file."""
    print 'Running this file will generate new access tokens if necessary.'
    print 'Please delete %s if you want to clear any old ones.' % FILE_NAME
    print '---------------------------------------------------------------'
    raw_input('Press Enter to continue...')
    prepare_credentials()


if __name__ == '__main__':
    main(sys.argv)
