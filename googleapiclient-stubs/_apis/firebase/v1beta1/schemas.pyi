import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddFirebaseRequest(typing_extensions.TypedDict, total=False):
    locationId: str

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
    streamMappings: _list[StreamMapping]

@typing.type_check_only
class AnalyticsProperty(typing_extensions.TypedDict, total=False):
    analyticsAccountId: str
    displayName: str
    id: str

@typing.type_check_only
class AndroidApp(typing_extensions.TypedDict, total=False):
    apiKeyId: str
    appId: str
    displayName: str
    name: str
    packageName: str
    projectId: str
    sha1Hashes: _list[str]
    sha256Hashes: _list[str]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

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
    apiKeyId: str
    appId: str
    displayName: str
    name: str
    namespace: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID", "WEB"]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class FirebaseProject(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    projectId: str
    projectNumber: str
    resources: DefaultResources
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class IosApp(typing_extensions.TypedDict, total=False):
    apiKeyId: str
    appId: str
    appStoreId: str
    bundleId: str
    displayName: str
    name: str
    projectId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    teamId: str

@typing.type_check_only
class IosAppConfig(typing_extensions.TypedDict, total=False):
    configFileContents: str
    configFilename: str

@typing.type_check_only
class ListAndroidAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[AndroidApp]
    nextPageToken: str

@typing.type_check_only
class ListAvailableLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListAvailableProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projectInfo: _list[ProjectInfo]

@typing.type_check_only
class ListFirebaseProjectsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[FirebaseProject]

@typing.type_check_only
class ListIosAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[IosApp]
    nextPageToken: str

@typing.type_check_only
class ListShaCertificatesResponse(typing_extensions.TypedDict, total=False):
    certificates: _list[ShaCertificate]

@typing.type_check_only
class ListWebAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[WebApp]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    features: _list[str]
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
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class ProjectInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    locationId: str
    project: str

@typing.type_check_only
class RemoveAnalyticsRequest(typing_extensions.TypedDict, total=False):
    analyticsPropertyId: str

@typing.type_check_only
class RemoveAndroidAppRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    etag: str
    validateOnly: bool

@typing.type_check_only
class RemoveIosAppRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    etag: str
    validateOnly: bool

@typing.type_check_only
class RemoveWebAppRequest(typing_extensions.TypedDict, total=False):
    allowMissing: bool
    etag: str
    validateOnly: bool

@typing.type_check_only
class SearchFirebaseAppsResponse(typing_extensions.TypedDict, total=False):
    apps: _list[FirebaseAppInfo]
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
    details: _list[dict[str, typing.Any]]
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
class UndeleteAndroidAppRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class UndeleteIosAppRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class UndeleteWebAppRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class WebApp(typing_extensions.TypedDict, total=False):
    apiKeyId: str
    appId: str
    appUrls: _list[str]
    displayName: str
    name: str
    projectId: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
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
