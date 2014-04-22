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
 * This example adds a new ad unit to a publisher ad client.
 * To get ad clients, see GetAllAdClientsForPublisher.php.
 *
 * Tags: accounts.adunits.insert
 */
class AddAdUnitToPublisher {
  /**
   * Adds a new ad unit to a publisher ad client.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $accountId string the ID for the publisher account to be used.
   * @param $adClientId string the ID for the ad client to be used.
   * @return Google_Service_AdSenseHost_AdUnit the created ad unit.
   */
  public static function run($service, $accountId, $adClientId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Adding ad unit to ad client %s\n", $adClientId);
    print $separator;

    $adUnit = new Google_Service_AdSenseHost_AdUnit();
    $adUnit->setName('Ad Unit #' . getUniqueName());

    $contentAdsSettings =
        new Google_Service_AdSenseHost_AdUnitContentAdsSettings();
    $backupOption =
        new Google_Service_AdSenseHost_AdUnitContentAdsSettingsBackupOption();
    $backupOption->setType('COLOR');
    $backupOption->setColor('ffffff');
    $contentAdsSettings->setBackupOption($backupOption);
    $contentAdsSettings->setSize('SIZE_200_200');
    $contentAdsSettings->setType('TEXT');
    $adUnit->setContentAdsSettings($contentAdsSettings);

    $customStyle = new Google_Service_AdSenseHost_AdStyle();
    $colors = new Google_Service_AdSenseHost_AdStyleColors();
    $colors->setBackground('ffffff');
    $colors->setBorder('000000');
    $colors->setText('000000');
    $colors->setTitle('000000');
    $colors->setUrl('0000ff');
    $customStyle->setColors($colors);
    $customStyle->setCorners('SQUARE');
    $font = new Google_Service_AdSenseHost_AdStyleFont();
    $font->setFamily('ACCOUNT_DEFAULT_FAMILY');
    $font->setSize('ACCOUNT_DEFAULT_SIZE');
    $customStyle->setFont($font);
    $adUnit->setCustomStyle($customStyle);

    $result =
        $service->accounts_adunits->insert($accountId, $adClientId, $adUnit);

    printf(
        "Ad unit with ID \"%s\", type \"%s\", name \"%s\" and status \"%s\" " .
            "was created.\n",
        $result->getId(), $result->getContentAdsSettings()->getType(),
        $result->getName(), $result->getStatus());

    print "\n";

    return $result;
  }
}
