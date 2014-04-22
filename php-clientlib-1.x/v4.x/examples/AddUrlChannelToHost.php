<?php
/*
 * Copyright 2014 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * This example adds a URL channel to a host ad client.
 * To get ad clients, see GetAllAdClientsForHost.php.
 *
 * Tags: urlchannels.insert
 */
class AddUrlChannelToHost {
  /**
   * Adds a URL channel to a host ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $adClientId string the ID for the ad client to be used.
   * @return Google_Service_AdSenseHost_UrlChannel the created URL channel.
   */
  public static function run($service, $adClientId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Adding URL channel to ad client %s\n", $adClientId);
    print $separator;

    $urlChannel = new Google_Service_AdSenseHost_UrlChannel();
    $urlChannel->setUrlPattern('www.example.com/' . getUniqueName());

    $result = $service->urlchannels->insert($adClientId, $urlChannel);

    printf("URL channel with id \"%s\" and URL pattern \"%s\" was created.\n",
        $result->getId(), $result->getUrlPattern());

    print "\n";

    return $result;
  }
}
