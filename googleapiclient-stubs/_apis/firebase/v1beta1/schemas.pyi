import typing

import typing_extensions
@typing.type_check_only
class AddFirebaseRequest(typing_extensions.TypedDict, total=False):
    locationId: str
    regionCode: str
    timeZone: str

@typing.type_check_only
class AddGoogleAnalyticsRequest(typing_extensions.TypedDict, total=False):
    analyticsAccountId: str
    analyticsPropertyId: str

@typing.type_check_only
class AdminSdkConfig(typing_extensions.TypedDict, total=False):
    databaseURL: str
    locationId: str
    projectId: str
    storageBucket: str

@typing.type_check_only
class AnalyticsDetails(typing_extensions.TypedDict, total=False):
    analyticsProperty: AnalyticsProperty
    streamMappings: typing.List[StreamMapping]

@typing.type_check_only
class AnalyticsProperty(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class AndroidApp(typing_extensions.TypedDict, total=False):
    appId: str
    displayName: str
    name: str
    packageName: str
    projectId: str

@typing.type_check_only
class AndroidAppConfig(typing_extensions.TypedDict, total=False):
    configFileContents: str
    configFilename: str

@typing.type_check_only
class DefaultResources(typing_extensions.TypedDict, total=False):
    hostingSite: str
    locationId: str
    realtimeDatabaseInstance: str
    storageBucket: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FinalizeDefaultLocationRequest(typing_extensions.TypedDict, total=False):
    locationId: str

@typing.type_check_only
class FirebaseAppInfo(typing_extensions.TypedDict, total=False):
    appId: str
    displayName: str
    name: str
    namespace: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID", "WEB"]

@typing.type_check_only
class FirebaseProject(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    projectId: str
    projectNumber: str
    resources: DefaultResources
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class IosApp(typing_extensions.TypedDict, total=False):
    appId: str
    appStoreId: str
    bundleId: str
    displayName: str
    name: str
    projectId: str

@typing.type_check_only
class IosAppConfig(typing_extensions.TypedDict, total=False):
    configFileContents: str
    configFilename: str

@typing.type_check_only
class ListAndroidAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[AndroidApp]
    nextPageToken: str

@typing.type_check_only
class ListAvailableLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListAvailableProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projectInfo: typing.List[ProjectInfo]

@typing.type_check_only
class ListFirebaseProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[FirebaseProject]

@typing.type_check_only
class ListIosAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[IosApp]
    nextPageToken: str

@typing.type_check_only
class ListShaCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: typing.List[ShaCertificate]

@typing.type_check_only
class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[WebApp]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    features: typing.List[str]
    locationId: str
    type: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED", "REGIONAL", "MULTI_REGIONAL"
    ]

@typing.type_check_only
class MessageSet(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class ProjectInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    locationId: str
    project: str

@typing.type_check_only
class RemoveAnalyticsRequest(typing_extensions.TypedDict, total=False):
    analyticsPropertyId: str

@typing.type_check_only
class SearchFirebaseAppsResponse(typing_extensions.TypedDict, total=False):
    apps: typing.List[FirebaseAppInfo]
    nextPageToken: str

@typing.type_check_only
class ShaCertificate(typing_extensions.TypedDict, total=False):
    certType: typing_extensions.Literal[
        "SHA_CERTIFICATE_TYPE_UNSPECIFIED", "SHA_1", "SHA_256"
    ]
    name: str
    shaHash: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusProto(typing_extensions.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: MessageSet
    space: str

@typing.type_check_only
class StreamMapping(typing_extensions.TypedDict, total=False):
    app: str
    measurementId: str
    streamId: str

@typing.type_check_only
class WebApp(typing_extensions.TypedDict, total=False):
    appId: str
    appUrls: typing.List[str]
    displayName: str
    name: str
    projectId: str
    webId: str

@typing.type_check_only
class WebAppConfig(typing_extensions.TypedDict, total=False):
    apiKey: str
    appId: str
    authDomain: str
    databaseURL: str
    locationId: str
    measurementId: str
    messagingSenderId: str
    projectId: str
    storageBucket: str
