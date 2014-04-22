# AdSense Host API sample for PHP

This sample runs a number of different requests against the AdSense Host API.

## Prerequisites

* PHP version 5.2.1 or greater
* The JSON PHP extension


## Installation

* Download and install the [PHP Client library for Google APIs](
    https://developers.google.com/api-client-library/php/start/installation)
* Copy the AdSense Host API sample for PHP to your server
* Change the include path in adsensehost-sample.php to your client library
  installation
* If you want to run the publisher examples too, change the PUB_ACCOUNT_ID
  constant in adsensehost-sample.php to an associated publisher account ID
* Modify client_secrets.json with your client ID, client secret and redirect URL
  (http://your/path/adsensehost-sample.php)
* Open the sample (http://your/path/adsensehost-sample.php) in your browser

This will start an authentication flow, redirect back to your server, and then
print data about your AdSense Host account, as well as create, update and delete
channels in it.

If you set the PUB_ACCOUNT_ID constant, it will also display data about the
publisher account and create, update and delete ad units in it.
