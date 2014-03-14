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

"""Maps application URLs to views."""

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'blog.views',
    url(r'^/*$', 'index'),
    url(r'^blog/(?P<user_name>\w+)/$', 'userblog', name='userblog'),
    url(r'^blog/(?P<user_name>\w+)/admin/$', 'admin'),
    url(r'^blog/(?P<user_name>\w+)/admin/monetize/$', 'monetize'),
    url(r'^callback/$', 'callback')
)

urlpatterns += patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)
