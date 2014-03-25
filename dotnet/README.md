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
* Make sure that the _Build Action_ for client_secrets.json is "Content" and _Copy to Output Directory_ is "Copy if newer"
* Build and execute
