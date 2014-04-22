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
 * This example deletes a URL channel on a host ad client.
 * To get ad clients, see GetAllAdClientsForHost.php.
 * To get URL channels, see GetAllUrlChannelsForHost.php.
 *
 * Tags: urlchannels.delete
 */
class DeleteUrlChannelOnHost {
  /**
   * Deletes a URL channel on a host ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $adClientId string the ID for the ad client to be used.
   * @param $urlChannelId string the ID of the URL channel to be deleted.
   */
  public static function run($service, $adClientId, $urlChannelId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Deleting URL channel %s\n", $urlChannelId);
    print $separator;

    $result = $service->urlchannels->delete($adClientId, $urlChannelId);

    printf("URL channel with ID \"%s\" was deleted.\n", $result->getId());

    print "\n";
  }
}
