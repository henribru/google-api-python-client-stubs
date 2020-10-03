import typing

import typing_extensions

class StreamMapping(typing_extensions.TypedDict, total=False):
    streamId: str
    measurementId: str
    app: str

class ShaCertificate(typing_extensions.TypedDict, total=False):
    certType: typing_extensions.Literal[
        "SHA_CERTIFICATE_TYPE_UNSPECIFIED", "SHA_1", "SHA_256"
    ]
    shaHash: str
    name: str

class DefaultResources(typing_extensions.TypedDict, total=False):
    locationId: str
    realtimeDatabaseInstance: str
    hostingSite: str
    storageBucket: str

class IosAppConfig(typing_extensions.TypedDict, total=False):
    configFilename: str
    configFileContents: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status

class WebAppConfig(typing_extensions.TypedDict, total=False):
    projectId: str
    locationId: str
    messagingSenderId: str
    databaseURL: str
    authDomain: str
    measurementId: str
    apiKey: str
    storageBucket: str
    appId: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class SearchFirebaseAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[FirebaseAppInfo]
    nextPageToken: str

class ListShaCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[ShaCertificate]

class MessageSet(typing_extensions.TypedDict, total=False): ...

class Location(typing_extensions.TypedDict, total=False):
    features: typing.List[str]
    type: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED", "REGIONAL", "MULTI_REGIONAL"
    ]
    locationId: str

class ListAvailableProjectsResponse(typing_extensions.TypedDict, total=False):
    projectInfo: typing.List[ProjectInfo]
    nextPageToken: str

class StatusProto(typing_extensions.TypedDict, total=False):
    space: str
    message: str
    messageSet: MessageSet
    code: int
    canonicalCode: int

class AndroidAppConfig(typing_extensions.TypedDict, total=False):
    configFilename: str
    configFileContents: str

class AnalyticsProperty(typing_extensions.TypedDict, total=False):
    id: str
    displayName: str

class AddFirebaseRequest(typing_extensions.TypedDict, total=False):
    timeZone: str
    regionCode: str
    locationId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class FinalizeDefaultLocationRequest(typing_extensions.TypedDict, total=False):
    locationId: str

class AddGoogleAnalyticsRequest(typing_extensions.TypedDict, total=False):
    analyticsAccountId: str
    analyticsPropertyId: str

class ListIosAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[IosApp]
    nextPageToken: str

class RemoveAnalyticsRequest(typing_extensions.TypedDict, total=False):
    analyticsPropertyId: str

class ListAndroidAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[AndroidApp]
    nextPageToken: str

class AndroidApp(typing_extensions.TypedDict, total=False):
    packageName: str
    appId: str
    projectId: str
    name: str
    displayName: str

class FirebaseAppInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    appId: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID", "WEB"]
    namespace: str
    name: str

class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[WebApp]
    nextPageToken: str

class ListFirebaseProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[FirebaseProject]

class FirebaseProject(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    projectNumber: str
    displayName: str
    projectId: str
    name: str
    resources: DefaultResources

class ProjectInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    locationId: str
    project: str

class ListAvailableLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class IosApp(typing_extensions.TypedDict, total=False):
    appStoreId: str
    bundleId: str
    name: str
    appId: str
    displayName: str
    projectId: str

class AdminSdkConfig(typing_extensions.TypedDict, total=False):
    databaseURL: str
    locationId: str
    storageBucket: str
    projectId: str

class AnalyticsDetails(typing_extensions.TypedDict, total=False):
    streamMappings: typing.List[StreamMapping]
    analyticsProperty: AnalyticsProperty

class WebApp(typing_extensions.TypedDict, total=False):
    appId: str
    webId: str
    appUrls: typing.List[str]
    name: str
    projectId: str
    displayName: str
