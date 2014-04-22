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
 * This example adds a custom channel to a host ad client.
 * To get ad clients, see GetAllAdClientsForHost.php.
 *
 * Tags: customchannels.insert
 */
class AddCustomChannelToHost {
  /**
   * Adds a custom channel to a host ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $adClientId string the ID for the ad client to be used.
   * @return Google_Service_AdSenseHost_CustomChannel the created custom channel
   */
  public static function run($service, $adClientId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Adding custom channel to ad client %s\n", $adClientId);
    print $separator;

    $customChannel = new Google_Service_AdSenseHost_CustomChannel();
    $customChannel->setName('Sample Channel #' . getUniqueName());

    $result = $service->customchannels->insert($adClientId, $customChannel);

    printf(
        "Custom channel with ID \"%s\", code \"%s\" and name \"%s\" was " .
            "created.\n",
        $result->getId(), $result->getCode(), $result->getName());

    print "\n";

    return $result;
  }
}
