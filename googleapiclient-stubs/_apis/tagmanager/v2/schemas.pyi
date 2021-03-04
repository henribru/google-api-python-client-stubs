import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountId: str
    fingerprint: str
    name: str
    path: str
    shareData: bool
    tagManagerUrl: str

@typing.type_check_only
class AccountAccess(typing_extensions.TypedDict, total=False):
    permission: typing_extensions.Literal[
        "accountPermissionUnspecified", "noAccess", "user", "admin"
    ]

@typing.type_check_only
class BuiltInVariable(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    name: str
    path: str
    type: typing_extensions.Literal[
        "builtInVariableTypeUnspecified",
        "pageUrl",
        "pageHostname",
        "pagePath",
        "referrer",
        "event",
        "clickElement",
        "clickClasses",
        "clickId",
        "clickTarget",
        "clickUrl",
        "clickText",
        "firstPartyServingUrl",
        "formElement",
        "formClasses",
        "formId",
        "formTarget",
        "formUrl",
        "formText",
        "errorMessage",
        "errorUrl",
        "errorLine",
        "newHistoryUrl",
        "oldHistoryUrl",
        "newHistoryFragment",
        "oldHistoryFragment",
        "newHistoryState",
        "oldHistoryState",
        "historySource",
        "containerVersion",
        "debugMode",
        "randomNumber",
        "containerId",
        "appId",
        "appName",
        "appVersionCode",
        "appVersionName",
        "language",
        "osVersion",
        "platform",
        "sdkVersion",
        "deviceName",
        "resolution",
        "advertiserId",
        "advertisingTrackingEnabled",
        "htmlId",
        "environmentName",
        "ampBrowserLanguage",
        "ampCanonicalPath",
        "ampCanonicalUrl",
        "ampCanonicalHost",
        "ampReferrer",
        "ampTitle",
        "ampClientId",
        "ampClientTimezone",
        "ampClientTimestamp",
        "ampClientScreenWidth",
        "ampClientScreenHeight",
        "ampClientScrollX",
        "ampClientScrollY",
        "ampClientMaxScrollX",
        "ampClientMaxScrollY",
        "ampTotalEngagedTime",
        "ampPageViewId",
        "ampPageLoadTime",
        "ampPageDownloadTime",
        "ampGtmEvent",
        "eventName",
        "firebaseEventParameterCampaign",
        "firebaseEventParameterCampaignAclid",
        "firebaseEventParameterCampaignAnid",
        "firebaseEventParameterCampaignClickTimestamp",
        "firebaseEventParameterCampaignContent",
        "firebaseEventParameterCampaignCp1",
        "firebaseEventParameterCampaignGclid",
        "firebaseEventParameterCampaignSource",
        "firebaseEventParameterCampaignTerm",
        "firebaseEventParameterCurrency",
        "firebaseEventParameterDynamicLinkAcceptTime",
        "firebaseEventParameterDynamicLinkLinkid",
        "firebaseEventParameterNotificationMessageDeviceTime",
        "firebaseEventParameterNotificationMessageId",
        "firebaseEventParameterNotificationMessageName",
        "firebaseEventParameterNotificationMessageTime",
        "firebaseEventParameterNotificationTopic",
        "firebaseEventParameterPreviousAppVersion",
        "firebaseEventParameterPreviousOsVersion",
        "firebaseEventParameterPrice",
        "firebaseEventParameterProductId",
        "firebaseEventParameterQuantity",
        "firebaseEventParameterValue",
        "videoProvider",
        "videoUrl",
        "videoTitle",
        "videoDuration",
        "videoPercent",
        "videoVisible",
        "videoStatus",
        "videoCurrentTime",
        "scrollDepthThreshold",
        "scrollDepthUnits",
        "scrollDepthDirection",
        "elementVisibilityRatio",
        "elementVisibilityTime",
        "elementVisibilityFirstTime",
        "elementVisibilityRecentTime",
        "requestPath",
        "requestMethod",
        "clientName",
        "queryString",
    ]
    workspaceId: str

@typing.type_check_only
class Client(typing_extensions.TypedDict, total=False):
    accountId: str
    clientId: str
    containerId: str
    fingerprint: str
    name: str
    notes: str
    parameter: typing.List[Parameter]
    parentFolderId: str
    path: str
    priority: int
    tagManagerUrl: str
    type: str
    workspaceId: str

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    parameter: typing.List[Parameter]
    type: typing_extensions.Literal[
        "conditionTypeUnspecified",
        "equals",
        "contains",
        "startsWith",
        "endsWith",
        "matchRegex",
        "greater",
        "greaterOrEquals",
        "less",
        "lessOrEquals",
        "cssSelector",
        "urlMatches",
    ]

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    domainName: typing.List[str]
    fingerprint: str
    name: str
    notes: str
    path: str
    publicId: str
    tagManagerUrl: str
    usageContext: typing.List[str]

@typing.type_check_only
class ContainerAccess(typing_extensions.TypedDict, total=False):
    containerId: str
    permission: typing_extensions.Literal[
        "containerPermissionUnspecified",
        "noAccess",
        "read",
        "edit",
        "approve",
        "publish",
    ]

@typing.type_check_only
class ContainerVersion(typing_extensions.TypedDict, total=False):
    accountId: str
    builtInVariable: typing.List[BuiltInVariable]
    client: typing.List[Client]
    container: Container
    containerId: str
    containerVersionId: str
    customTemplate: typing.List[CustomTemplate]
    deleted: bool
    description: str
    fingerprint: str
    folder: typing.List[Folder]
    name: str
    path: str
    tag: typing.List[Tag]
    tagManagerUrl: str
    trigger: typing.List[Trigger]
    variable: typing.List[Variable]
    zone: typing.List[Zone]

@typing.type_check_only
class ContainerVersionHeader(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    containerVersionId: str
    deleted: bool
    name: str
    numClients: str
    numCustomTemplates: str
    numMacros: str
    numRules: str
    numTags: str
    numTriggers: str
    numVariables: str
    numZones: str
    path: str

@typing.type_check_only
class CreateBuiltInVariableResponse(typing_extensions.TypedDict, total=False):
    builtInVariable: typing.List[BuiltInVariable]

@typing.type_check_only
class CreateContainerVersionRequestVersionOptions(
    typing_extensions.TypedDict, total=False
):
    name: str
    notes: str

@typing.type_check_only
class CreateContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion
    newWorkspacePath: str
    syncStatus: SyncStatus

@typing.type_check_only
class CustomTemplate(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    galleryReference: GalleryReference
    name: str
    path: str
    tagManagerUrl: str
    templateData: str
    templateId: str
    workspaceId: str

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    changeStatus: typing_extensions.Literal[
        "changeStatusUnspecified", "none", "added", "deleted", "updated"
    ]
    client: Client
    folder: Folder
    tag: Tag
    trigger: Trigger
    variable: Variable

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
    accountId: str
    authorizationCode: str
    authorizationTimestamp: str
    containerId: str
    containerVersionId: str
    description: str
    enableDebug: bool
    environmentId: str
    fingerprint: str
    name: str
    path: str
    tagManagerUrl: str
    type: typing_extensions.Literal["user", "live", "latest", "workspace"]
    url: str
    workspaceId: str

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    folderId: str
    name: str
    notes: str
    path: str
    tagManagerUrl: str
    workspaceId: str

@typing.type_check_only
class FolderEntities(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tag: typing.List[Tag]
    trigger: typing.List[Trigger]
    variable: typing.List[Variable]

@typing.type_check_only
class GalleryReference(typing_extensions.TypedDict, total=False):
    host: str
    isModified: bool
    owner: str
    repository: str
    signature: str
    version: str

@typing.type_check_only
class GetWorkspaceStatusResponse(typing_extensions.TypedDict, total=False):
    mergeConflict: typing.List[MergeConflict]
    workspaceChange: typing.List[Entity]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    account: typing.List[Account]
    nextPageToken: str

@typing.type_check_only
class ListContainerVersionsResponse(typing_extensions.TypedDict, total=False):
    containerVersionHeader: typing.List[ContainerVersionHeader]
    nextPageToken: str

@typing.type_check_only
class ListContainersResponse(typing_extensions.TypedDict, total=False):
    container: typing.List[Container]
    nextPageToken: str

@typing.type_check_only
class ListEnabledBuiltInVariablesResponse(typing_extensions.TypedDict, total=False):
    builtInVariable: typing.List[BuiltInVariable]
    nextPageToken: str

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environment: typing.List[Environment]
    nextPageToken: str

@typing.type_check_only
class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folder: typing.List[Folder]
    nextPageToken: str

@typing.type_check_only
class ListTagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tag: typing.List[Tag]

@typing.type_check_only
class ListTemplatesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    template: typing.List[CustomTemplate]

@typing.type_check_only
class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    trigger: typing.List[Trigger]

@typing.type_check_only
class ListUserPermissionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userPermission: typing.List[UserPermission]

@typing.type_check_only
class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    variable: typing.List[Variable]

@typing.type_check_only
class ListWorkspacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workspace: typing.List[Workspace]

@typing.type_check_only
class ListZonesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    zone: typing.List[Zone]

@typing.type_check_only
class MergeConflict(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Parameter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class PublishContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class QuickPreviewResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion
    syncStatus: SyncStatus

@typing.type_check_only
class RevertBuiltInVariableResponse(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RevertFolderResponse(typing_extensions.TypedDict, total=False):
    folder: Folder

@typing.type_check_only
class RevertTagResponse(typing_extensions.TypedDict, total=False):
    tag: Tag

@typing.type_check_only
class RevertTemplateResponse(typing_extensions.TypedDict, total=False):
    template: CustomTemplate

@typing.type_check_only
class RevertTriggerResponse(typing_extensions.TypedDict, total=False):
    trigger: Trigger

@typing.type_check_only
class RevertVariableResponse(typing_extensions.TypedDict, total=False):
    variable: Variable

@typing.type_check_only
class RevertZoneResponse(typing_extensions.TypedDict, total=False):
    zone: Zone

@typing.type_check_only
class SetupTag(typing_extensions.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

@typing.type_check_only
class SyncStatus(typing_extensions.TypedDict, total=False):
    mergeConflict: bool
    syncError: bool

@typing.type_check_only
class SyncWorkspaceResponse(typing_extensions.TypedDict, total=False):
    mergeConflict: typing.List[MergeConflict]
    syncStatus: SyncStatus

@typing.type_check_only
class Tag(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TeardownTag(typing_extensions.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

@typing.type_check_only
class Trigger(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class UserPermission(typing_extensions.TypedDict, total=False):
    accountAccess: AccountAccess
    accountId: str
    containerAccess: typing.List[ContainerAccess]
    emailAddress: str
    path: str

@typing.type_check_only
class Variable(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class VariableFormatValue(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Workspace(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    description: str
    fingerprint: str
    name: str
    path: str
    tagManagerUrl: str
    workspaceId: str

@typing.type_check_only
class Zone(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ZoneBoundary(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ZoneChildContainer(typing_extensions.TypedDict, total=False):
    nickname: str
    publicId: str

@typing.type_check_only
class ZoneTypeRestriction(typing_extensions.TypedDict, total=False):
    enable: bool
    whitelistedTypeId: typing.List[str]
