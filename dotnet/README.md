# AdSense Host API dotnet samples

## Prerequisites
* Project with access to the AdSense Host API in http://console.developers.google.com
* Project client ID and client secret
* Visual Studio 2012 and NuGet package management

## Installation
* Use NuGet to install **Google.Apis.AdSenseHost.v4_1 Client Library**
* Add the existing .cs files and client_secrets.json from the sample folder
* Open the project properties and set the Startup object:
 * **AdSenseHostSample** for general inventory calls
 * **AssociationSessionSample** for calls related to the account association
* Modify client_secrets.json with your client ID and client secret
* Make sure client_secrets.json is copied to the Output Directory
* Build and execute
