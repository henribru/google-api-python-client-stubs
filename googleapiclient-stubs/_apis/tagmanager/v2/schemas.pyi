import typing

import typing_extensions

class CreateBuiltInVariableResponse(typing_extensions.TypedDict, total=False):
    builtInVariable: typing.List[BuiltInVariable]

class ListZonesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    zone: typing.List[Zone]

class PublishContainerVersionResponse(typing_extensions.TypedDict, total=False):
    containerVersion: ContainerVersion
    compilerError: bool

class ZoneChildContainer(typing_extensions.TypedDict, total=False):
    publicId: str
    nickname: str

class Zone(typing.Dict[str, typing.Any]): ...

class UserPermission(typing_extensions.TypedDict, total=False):
    accountId: str
    path: str
    containerAccess: typing.List[ContainerAccess]
    emailAddress: str
    accountAccess: AccountAccess

class Environment(typing_extensions.TypedDict, total=False):
    url: str
    tagManagerUrl: str
    authorizationTimestamp: str
    accountId: str
    description: str
    containerId: str
    environmentId: str
    path: str
    workspaceId: str
    type: typing_extensions.Literal["user", "live", "latest", "workspace"]
    containerVersionId: str
    name: str
    fingerprint: str
    authorizationCode: str
    enableDebug: bool

class Entity(typing_extensions.TypedDict, total=False):
    variable: Variable
    trigger: Trigger
    tag: Tag
    changeStatus: typing_extensions.Literal[
        "changeStatusUnspecified", "none", "added", "deleted", "updated"
    ]
    folder: Folder

class ListTagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tag: typing.List[Tag]

class RevertTemplateResponse(typing_extensions.TypedDict, total=False):
    template: CustomTemplate

class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    folder: typing.List[Folder]

class QuickPreviewResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    syncStatus: SyncStatus
    containerVersion: ContainerVersion

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

class Folder(typing_extensions.TypedDict, total=False):
    folderId: str
    notes: str
    tagManagerUrl: str
    workspaceId: str
    accountId: str
    fingerprint: str
    containerId: str
    path: str
    name: str

class ListTemplatesResponse(typing_extensions.TypedDict, total=False):
    template: typing.List[CustomTemplate]
    nextPageToken: str

class CustomTemplate(typing_extensions.TypedDict, total=False):
    path: str
    tagManagerUrl: str
    galleryReference: GalleryReference
    templateId: str
    workspaceId: str
    fingerprint: str
    templateData: str
    accountId: str
    containerId: str
    name: str

class Account(typing_extensions.TypedDict, total=False):
    fingerprint: str
    shareData: bool
    accountId: str
    name: str
    path: str
    tagManagerUrl: str

class VariableFormatValue(typing_extensions.TypedDict, total=False):
    convertFalseToValue: Parameter
    caseConversionType: typing_extensions.Literal["none", "lowercase", "uppercase"]
    convertUndefinedToValue: Parameter
    convertTrueToValue: Parameter
    convertNullToValue: Parameter

class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    environment: typing.List[Environment]

class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    account: typing.List[Account]
    nextPageToken: str

class Tag(typing.Dict[str, typing.Any]): ...

class MergeConflict(typing_extensions.TypedDict, total=False):
    entityInBaseVersion: Entity
    entityInWorkspace: Entity

class GalleryReference(typing_extensions.TypedDict, total=False):
    isModified: bool
    version: str
    signature: str
    owner: str
    repository: str
    host: str

class CreateContainerVersionRequestVersionOptions(
    typing_extensions.TypedDict, total=False
):
    notes: str
    name: str

class GetWorkspaceStatusResponse(typing_extensions.TypedDict, total=False):
    mergeConflict: typing.List[MergeConflict]
    workspaceChange: typing.List[Entity]

class RevertVariableResponse(typing_extensions.TypedDict, total=False):
    variable: Variable

class ListContainersResponse(typing_extensions.TypedDict, total=False):
    container: typing.List[Container]
    nextPageToken: str

class SyncStatus(typing_extensions.TypedDict, total=False):
    syncError: bool
    mergeConflict: bool

class RevertZoneResponse(typing_extensions.TypedDict, total=False):
    zone: Zone

class ListContainerVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    containerVersionHeader: typing.List[ContainerVersionHeader]

class FolderEntities(typing_extensions.TypedDict, total=False):
    variable: typing.List[Variable]
    trigger: typing.List[Trigger]
    nextPageToken: str
    tag: typing.List[Tag]

class Variable(typing.Dict[str, typing.Any]): ...

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

class ContainerVersion(typing.Dict[str, typing.Any]): ...

class RevertTagResponse(typing_extensions.TypedDict, total=False):
    tag: Tag

class ListWorkspacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workspace: typing.List[Workspace]

class CreateContainerVersionResponse(typing_extensions.TypedDict, total=False):
    newWorkspacePath: str
    compilerError: bool
    syncStatus: SyncStatus
    containerVersion: ContainerVersion

class AccountAccess(typing_extensions.TypedDict, total=False):
    permission: typing_extensions.Literal[
        "accountPermissionUnspecified", "noAccess", "user", "admin"
    ]

class BuiltInVariable(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
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
    path: str
    name: str

class SyncWorkspaceResponse(typing_extensions.TypedDict, total=False):
    syncStatus: SyncStatus
    mergeConflict: typing.List[MergeConflict]

class RevertBuiltInVariableResponse(typing_extensions.TypedDict, total=False):
    enabled: bool

class Trigger(typing.Dict[str, typing.Any]): ...
class Client(typing.Dict[str, typing.Any]): ...
class Parameter(typing.Dict[str, typing.Any]): ...

class ContainerVersionHeader(typing_extensions.TypedDict, total=False):
    name: str
    containerId: str
    numCustomTemplates: str
    numTags: str
    numVariables: str
    path: str
    numTriggers: str
    numMacros: str
    containerVersionId: str
    numRules: str
    numZones: str
    accountId: str
    deleted: bool

class ListUserPermissionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userPermission: typing.List[UserPermission]

class ZoneBoundary(typing.Dict[str, typing.Any]): ...

class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    trigger: typing.List[Trigger]
    nextPageToken: str

class ZoneTypeRestriction(typing_extensions.TypedDict, total=False):
    whitelistedTypeId: typing.List[str]
    enable: bool

class RevertTriggerResponse(typing_extensions.TypedDict, total=False):
    trigger: Trigger

class ListEnabledBuiltInVariablesResponse(typing_extensions.TypedDict, total=False):
    builtInVariable: typing.List[BuiltInVariable]
    nextPageToken: str

class TeardownTag(typing_extensions.TypedDict, total=False):
    tagName: str
    stopTeardownOnFailure: bool

class RevertFolderResponse(typing_extensions.TypedDict, total=False):
    folder: Folder

class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    variable: typing.List[Variable]

class SetupTag(typing_extensions.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

class Workspace(typing_extensions.TypedDict, total=False):
    tagManagerUrl: str
    accountId: str
    containerId: str
    name: str
    path: str
    description: str
    workspaceId: str
    fingerprint: str

class Container(typing_extensions.TypedDict, total=False):
    notes: str
    name: str
    path: str
    tagManagerUrl: str
    usageContext: typing.List[str]
    containerId: str
    publicId: str
    domainName: typing.List[str]
    fingerprint: str
    accountId: str
