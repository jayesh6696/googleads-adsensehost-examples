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
 * This example gets the account data for a publisher from their ad client ID.
 *
 * Tags: accounts.list
 */
class GetAccountDataForExistingPublisher {
  /**
   * Gets the account data for a publisher from their ad client ID.
   *
   * @param $service Google_Service_AdSenseHost AdSenseHost service object on
   *     which to run the requests.
   * @param $adClientId string the publisher ad client ID for which to get
   *     account data.
   */
  public static function run($service, $adClientId) {
    $separator = str_repeat('=', 80) . "\n";
    print $separator;
    printf("Listing publisher account for \"%s\"\n", $adClientId);
    print $separator;

    $accounts = null;
    $result = $service->accounts->listAccounts(array($adClientId));
    if (!empty($result['items'])) {
      $accounts = $result['items'];
      foreach ($accounts as $account) {
        $format = "Account with ID \"%s\", name \"%s\" and status \"%s\" " .
            "was found.\n";
        printf($format, $account['id'], $account['name'], $account['status']);
      }
    } else {
      print "No accounts found.\n";
    }
    print "\n";
  }
}
