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
 * This example updates an ad unit on a publisher ad client.
 * To get ad clients, see GetAllAdClientsForPublisher.php.
 * To get ad units, see GetAllAdUnitsForPublisher.php.
 *
 * Tags: accounts.adunits.patch
 */
class UpdateAdUnitOnPublisher {
  /**
   * Updates an ad unit on a publisher ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $accountId string the ID for the publisher account to be used.
   * @param $adClientId string the ID for the ad client to be used.
   * @param $adUnitId string the ID of the ad unit to be updated.
   * @return Google_Service_AdSenseHost_AdUnit the updated ad unit.
   */
  public static function run($service, $accountId, $adClientId, $adUnitId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Updating ad unit %s\n", $adUnitId);
    print $separator;

    $adUnit = new Google_Service_AdSenseHost_AdUnit();
    $contentAdsSettings =
        new Google_Service_AdSenseHost_AdUnitContentAdsSettings();
    $customStyle = new Google_Service_AdSenseHost_AdStyle();
    $colors = new Google_Service_AdSenseHost_AdStyleColors();
    $colors->setText('ff0000');
    $customStyle->setColors($colors);
    $adUnit->setCustomStyle($customStyle);

    $result = $service->accounts_adunits->patch($accountId, $adClientId,
        $adUnitId, $adUnit);

    printf("Ad unit with ID \"%s\" was updated with text color \"%s\"\n",
        $result->getId(), $result->getCustomStyle()->getColors()->getText());

    print "\n";

    return $result;
  }
}
