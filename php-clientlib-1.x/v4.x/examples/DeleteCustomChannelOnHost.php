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
 * This example deletes a custom channel on a host ad client.
 * To get ad clients, see GetAllAdClientsForHost.php.
 * To get custom channels, see GetAllCustomChannelsForHost.php.
 *
 * Tags: customchannels.delete
 */
class DeleteCustomChannelOnHost {
  /**
   * Deletes a custom channel on a host ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $adClientId string the ID for the ad client to be used.
   * @param $customChannelId string the ID of the custom channel to be deleted.
   */
  public static function run($service, $adClientId, $customChannelId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Deleting custom channel %s\n", $customChannelId);
    print $separator;

    $result = $service->customchannels->delete($adClientId, $customChannelId);

    printf("Custom channel with ID \"%s\" was deleted.\n", $result->getId());

    print "\n";
  }
}
