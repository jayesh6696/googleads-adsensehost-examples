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

"""Defines the data models to be used in this application."""

from django.db import models


class User(models.Model):
    """Represents a user / publisher."""
    name = models.CharField(max_length=50)
    pub_id = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.name


class AdUnit(models.Model):
    """Represents an ad unit belonging to a user."""
    user = models.ForeignKey(User)
    adsense_unit_id = models.CharField(max_length=100)
    generated_ad_code = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.adsense_unit_id


class AssociationSession(models.Model):
    """Represents an open (or completed) association session for a user."""
    session_id = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    redirect_url = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.session_id
