import typing

_list = list

@typing.type_check_only
class AddFirebaseRequest(typing.TypedDict, total=False):
    locationId: str

@typing.type_check_only
class AddGoogleAnalyticsRequest(typing.TypedDict, total=False):
    analyticsAccountId: str
    analyticsPropertyId: str

@typing.type_check_only
class AdminSdkConfig(typing.TypedDict, total=False):
    databaseURL: str
    locationId: str
    projectId: str
    storageBucket: str

@typing.type_check_only
class AnalyticsDetails(typing.TypedDict, total=False):
    analyticsProperty: AnalyticsProperty
    streamMappings: _list[StreamMapping]

@typing.type_check_only
class AnalyticsProperty(typing.TypedDict, total=False):
    analyticsAccountId: str
    displayName: str
    id: str

@typing.type_check_only
class AndroidApp(typing.TypedDict, total=False):
    apiKeyId: str
    appId: str
    displayName: str
    etag: str
    expireTime: str
    name: str
    packageName: str
    projectId: str
    sha1Hashes: _list[str]
    sha256Hashes: _list[str]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class AndroidAppConfig(typing.TypedDict, total=False):
    configFileContents: str
    configFilename: str

@typing.type_check_only
class DefaultResources(typing.TypedDict, total=False):
    hostingSite: str
    locationId: str
    realtimeDatabaseInstance: str
    storageBucket: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FinalizeDefaultLocationRequest(typing.TypedDict, total=False):
    locationId: str

@typing.type_check_only
class FirebaseAppInfo(typing.TypedDict, total=False):
    apiKeyId: str
    appId: str
    displayName: str
    expireTime: str
    name: str
    namespace: str
    platform: typing.Literal["PLATFORM_UNSPECIFIED", "IOS", "ANDROID", "WEB"]
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class FirebaseProject(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    displayName: str
    etag: str
    name: str
    projectId: str
    projectNumber: str
    resources: DefaultResources
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]

@typing.type_check_only
class IosApp(typing.TypedDict, total=False):
    apiKeyId: str
    appId: str
    appStoreId: str
    bundleId: str
    displayName: str
    etag: str
    expireTime: str
    name: str
    projectId: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    teamId: str

@typing.type_check_only
class IosAppConfig(typing.TypedDict, total=False):
    configFileContents: str
    configFilename: str

@typing.type_check_only
class ListAndroidAppsResponse(typing.TypedDict, total=False):
    apps: _list[AndroidApp]
    nextPageToken: str

@typing.type_check_only
class ListAvailableLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListAvailableProjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    projectInfo: _list[ProjectInfo]

@typing.type_check_only
class ListFirebaseProjectsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[FirebaseProject]

@typing.type_check_only
class ListIosAppsResponse(typing.TypedDict, total=False):
    apps: _list[IosApp]
    nextPageToken: str

@typing.type_check_only
class ListShaCertificatesResponse(typing.TypedDict, total=False):
    certificates: _list[ShaCertificate]

@typing.type_check_only
class ListWebAppsResponse(typing.TypedDict, total=False):
    apps: _list[WebApp]
    nextPageToken: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    features: _list[
        typing.Literal[
            "LOCATION_FEATURE_UNSPECIFIED", "FIRESTORE", "DEFAULT_STORAGE", "FUNCTIONS"
        ]
    ]
    locationId: str
    type: typing.Literal["LOCATION_TYPE_UNSPECIFIED", "REGIONAL", "MULTI_REGIONAL"]

@typing.type_check_only
class MessageSet(typing.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class ProductMetadata(typing.TypedDict, total=False):
    warningMessages: _list[str]

@typing.type_check_only
class ProjectInfo(typing.TypedDict, total=False):
    displayName: str
    locationId: str
    project: str

@typing.type_check_only
class RemoveAnalyticsRequest(typing.TypedDict, total=False):
    analyticsPropertyId: str

@typing.type_check_only
class RemoveAndroidAppRequest(typing.TypedDict, total=False):
    allowMissing: bool
    etag: str
    immediate: bool
    validateOnly: bool

@typing.type_check_only
class RemoveIosAppRequest(typing.TypedDict, total=False):
    allowMissing: bool
    etag: str
    immediate: bool
    validateOnly: bool

@typing.type_check_only
class RemoveWebAppRequest(typing.TypedDict, total=False):
    allowMissing: bool
    etag: str
    immediate: bool
    validateOnly: bool

@typing.type_check_only
class SearchFirebaseAppsResponse(typing.TypedDict, total=False):
    apps: _list[FirebaseAppInfo]
    nextPageToken: str

@typing.type_check_only
class ShaCertificate(typing.TypedDict, total=False):
    certType: typing.Literal["SHA_CERTIFICATE_TYPE_UNSPECIFIED", "SHA_1", "SHA_256"]
    name: str
    shaHash: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StatusProto(typing.TypedDict, total=False):
    canonicalCode: int
    code: int
    message: str
    messageSet: MessageSet
    space: str

@typing.type_check_only
class StreamMapping(typing.TypedDict, total=False):
    app: str
    measurementId: str
    streamId: str

@typing.type_check_only
class UndeleteAndroidAppRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class UndeleteIosAppRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class UndeleteWebAppRequest(typing.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class WebApp(typing.TypedDict, total=False):
    apiKeyId: str
    appId: str
    appUrls: _list[str]
    displayName: str
    etag: str
    expireTime: str
    name: str
    projectId: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    webId: str

@typing.type_check_only
class WebAppConfig(typing.TypedDict, total=False):
    apiKey: str
    appId: str
    authDomain: str
    databaseURL: str
    locationId: str
    measurementId: str
    messagingSenderId: str
    projectId: str
    projectNumber: str
    realtimeDatabaseUrl: str
    recaptchaSiteKey: str
    storageBucket: str
    version: str
