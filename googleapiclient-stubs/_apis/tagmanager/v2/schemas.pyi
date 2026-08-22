import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    accountId: str
    features: AccountFeatures
    fingerprint: str
    name: str
    path: str
    shareData: bool
    tagManagerUrl: str

@typing.type_check_only
class AccountAccess(typing.TypedDict, total=False):
    permission: typing.Literal[
        "accountPermissionUnspecified", "noAccess", "user", "admin"
    ]

@typing.type_check_only
class AccountFeatures(typing.TypedDict, total=False):
    supportMultipleContainers: bool
    supportUserPermissions: bool

@typing.type_check_only
class BuiltInVariable(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    name: str
    path: str
    type: typing.Literal[
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
        "serverPageLocationUrl",
        "serverPageLocationPath",
        "serverPageLocationHostname",
        "visitorRegion",
        "analyticsClientId",
        "analyticsSessionId",
        "analyticsSessionNumber",
    ]
    workspaceId: str

@typing.type_check_only
class BulkUpdateWorkspaceResponse(typing.TypedDict, total=False):
    changes: _list[Entity]

@typing.type_check_only
class Client(typing.TypedDict, total=False):
    accountId: str
    clientId: str
    containerId: str
    fingerprint: str
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    path: str
    priority: int
    tagManagerUrl: str
    type: str
    workspaceId: str

@typing.type_check_only
class Condition(typing.TypedDict, total=False):
    parameter: _list[Parameter]
    type: typing.Literal[
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
class Container(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    domainName: _list[str]
    features: ContainerFeatures
    fingerprint: str
    name: str
    notes: str
    path: str
    publicId: str
    tagIds: _list[str]
    tagManagerUrl: str
    taggingServerUrls: _list[str]
    usageContext: _list[
        typing.Literal[
            "usageContextUnspecified",
            "web",
            "android",
            "ios",
            "androidSdk5",
            "iosSdk5",
            "amp",
            "server",
        ]
    ]

@typing.type_check_only
class ContainerAccess(typing.TypedDict, total=False):
    containerId: str
    permission: typing.Literal[
        "containerPermissionUnspecified",
        "noAccess",
        "read",
        "edit",
        "approve",
        "publish",
    ]

@typing.type_check_only
class ContainerFeatures(typing.TypedDict, total=False):
    supportBuiltInVariables: bool
    supportClients: bool
    supportEnvironments: bool
    supportFolders: bool
    supportGtagConfigs: bool
    supportTags: bool
    supportTemplates: bool
    supportTransformations: bool
    supportTriggers: bool
    supportUserPermissions: bool
    supportVariables: bool
    supportVersions: bool
    supportWorkspaces: bool
    supportZones: bool

@typing.type_check_only
class ContainerVersion(typing.TypedDict, total=False):
    accountId: str
    builtInVariable: _list[BuiltInVariable]
    client: _list[Client]
    container: Container
    containerId: str
    containerVersionId: str
    customTemplate: _list[CustomTemplate]
    deleted: bool
    description: str
    fingerprint: str
    folder: _list[Folder]
    gtagConfig: _list[GtagConfig]
    name: str
    path: str
    tag: _list[Tag]
    tagManagerUrl: str
    transformation: _list[Transformation]
    trigger: _list[Trigger]
    variable: _list[Variable]
    zone: _list[Zone]

@typing.type_check_only
class ContainerVersionHeader(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    containerVersionId: str
    deleted: bool
    name: str
    numClients: str
    numCustomTemplates: str
    numGtagConfigs: str
    numTags: str
    numTransformations: str
    numTriggers: str
    numVariables: str
    numZones: str
    path: str

@typing.type_check_only
class CreateBuiltInVariableResponse(typing.TypedDict, total=False):
    builtInVariable: _list[BuiltInVariable]

@typing.type_check_only
class CreateContainerVersionRequestVersionOptions(typing.TypedDict, total=False):
    name: str
    notes: str

@typing.type_check_only
class CreateContainerVersionResponse(typing.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion
    newWorkspacePath: str
    syncStatus: SyncStatus

@typing.type_check_only
class CustomTemplate(typing.TypedDict, total=False):
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
class Destination(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    destinationId: str
    destinationLinkId: str
    fingerprint: str
    name: str
    path: str
    tagManagerUrl: str

@typing.type_check_only
class Entity(typing.TypedDict, total=False):
    builtInVariable: BuiltInVariable
    changeStatus: typing.Literal[
        "changeStatusUnspecified", "none", "added", "deleted", "updated"
    ]
    client: Client
    customTemplate: CustomTemplate
    folder: Folder
    gtagConfig: GtagConfig
    tag: Tag
    transformation: Transformation
    trigger: Trigger
    variable: Variable
    zone: Zone

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
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
    type: typing.Literal["user", "live", "latest", "workspace"]
    url: str
    workspaceId: str

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
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
class FolderEntities(typing.TypedDict, total=False):
    nextPageToken: str
    tag: _list[Tag]
    trigger: _list[Trigger]
    variable: _list[Variable]

@typing.type_check_only
class GalleryReference(typing.TypedDict, total=False):
    galleryTemplateId: str
    host: str
    isModified: bool
    owner: str
    repository: str
    signature: str
    templateDeveloperId: str
    version: str

@typing.type_check_only
class GetContainerSnippetResponse(typing.TypedDict, total=False):
    containerConfig: str
    snippet: str

@typing.type_check_only
class GetWorkspaceStatusResponse(typing.TypedDict, total=False):
    mergeConflict: _list[MergeConflict]
    workspaceChange: _list[Entity]

@typing.type_check_only
class GtagConfig(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    gtagConfigId: str
    parameter: _list[Parameter]
    path: str
    tagManagerUrl: str
    type: str
    workspaceId: str

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    account: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListClientsResponse(typing.TypedDict, total=False):
    client: _list[Client]
    nextPageToken: str

@typing.type_check_only
class ListContainerVersionsResponse(typing.TypedDict, total=False):
    containerVersionHeader: _list[ContainerVersionHeader]
    nextPageToken: str

@typing.type_check_only
class ListContainersResponse(typing.TypedDict, total=False):
    container: _list[Container]
    nextPageToken: str

@typing.type_check_only
class ListDestinationsResponse(typing.TypedDict, total=False):
    destination: _list[Destination]
    nextPageToken: str

@typing.type_check_only
class ListEnabledBuiltInVariablesResponse(typing.TypedDict, total=False):
    builtInVariable: _list[BuiltInVariable]
    nextPageToken: str

@typing.type_check_only
class ListEnvironmentsResponse(typing.TypedDict, total=False):
    environment: _list[Environment]
    nextPageToken: str

@typing.type_check_only
class ListFoldersResponse(typing.TypedDict, total=False):
    folder: _list[Folder]
    nextPageToken: str

@typing.type_check_only
class ListGtagConfigResponse(typing.TypedDict, total=False):
    gtagConfig: _list[GtagConfig]
    nextPageToken: str

@typing.type_check_only
class ListTagsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tag: _list[Tag]

@typing.type_check_only
class ListTemplatesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    template: _list[CustomTemplate]

@typing.type_check_only
class ListTransformationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    transformation: _list[Transformation]

@typing.type_check_only
class ListTriggersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    trigger: _list[Trigger]

@typing.type_check_only
class ListUserPermissionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userPermission: _list[UserPermission]

@typing.type_check_only
class ListVariablesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    variable: _list[Variable]

@typing.type_check_only
class ListWorkspacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workspace: _list[Workspace]

@typing.type_check_only
class ListZonesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    zone: _list[Zone]

@typing.type_check_only
class MergeConflict(typing.TypedDict, total=False):
    entityInBaseVersion: Entity
    entityInWorkspace: Entity

@typing.type_check_only
class Parameter(typing.TypedDict, total=False):
    isWeakReference: bool
    key: str
    list: _list[Parameter]
    map: _list[Parameter]
    type: typing.Literal[
        "typeUnspecified",
        "template",
        "integer",
        "boolean",
        "list",
        "map",
        "triggerReference",
        "tagReference",
    ]
    value: str

@typing.type_check_only
class ProposedChange(typing.TypedDict, total=False):
    changes: _list[Entity]

@typing.type_check_only
class PublishContainerVersionResponse(typing.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class QuickPreviewResponse(typing.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion
    syncStatus: SyncStatus

@typing.type_check_only
class RevertBuiltInVariableResponse(typing.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class RevertClientResponse(typing.TypedDict, total=False):
    client: Client

@typing.type_check_only
class RevertFolderResponse(typing.TypedDict, total=False):
    folder: Folder

@typing.type_check_only
class RevertTagResponse(typing.TypedDict, total=False):
    tag: Tag

@typing.type_check_only
class RevertTemplateResponse(typing.TypedDict, total=False):
    template: CustomTemplate

@typing.type_check_only
class RevertTransformationResponse(typing.TypedDict, total=False):
    transformation: Transformation

@typing.type_check_only
class RevertTriggerResponse(typing.TypedDict, total=False):
    trigger: Trigger

@typing.type_check_only
class RevertVariableResponse(typing.TypedDict, total=False):
    variable: Variable

@typing.type_check_only
class RevertZoneResponse(typing.TypedDict, total=False):
    zone: Zone

@typing.type_check_only
class SetupTag(typing.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

@typing.type_check_only
class SyncStatus(typing.TypedDict, total=False):
    mergeConflict: bool
    syncError: bool

@typing.type_check_only
class SyncWorkspaceResponse(typing.TypedDict, total=False):
    mergeConflict: _list[MergeConflict]
    syncStatus: SyncStatus

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    accountId: str
    blockingTriggerId: _list[str]
    consentSettings: TagConsentSetting
    containerId: str
    fingerprint: str
    firingTriggerId: _list[str]
    liveOnly: bool
    monitoringMetadata: Parameter
    monitoringMetadataTagNameKey: str
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    path: str
    paused: bool
    priority: Parameter
    scheduleEndMs: str
    scheduleStartMs: str
    setupTag: _list[SetupTag]
    tagFiringOption: typing.Literal[
        "tagFiringOptionUnspecified", "unlimited", "oncePerEvent", "oncePerLoad"
    ]
    tagId: str
    tagManagerUrl: str
    teardownTag: _list[TeardownTag]
    type: str
    workspaceId: str

@typing.type_check_only
class TagConsentSetting(typing.TypedDict, total=False):
    consentStatus: typing.Literal["notSet", "notNeeded", "needed"]
    consentType: Parameter

@typing.type_check_only
class TeardownTag(typing.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

@typing.type_check_only
class Transformation(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    path: str
    tagManagerUrl: str
    transformationId: str
    type: str
    workspaceId: str

@typing.type_check_only
class Trigger(typing.TypedDict, total=False):
    accountId: str
    autoEventFilter: _list[Condition]
    checkValidation: Parameter
    containerId: str
    continuousTimeMinMilliseconds: Parameter
    customEventFilter: _list[Condition]
    eventName: Parameter
    filter: _list[Condition]
    fingerprint: str
    horizontalScrollPercentageList: Parameter
    interval: Parameter
    intervalSeconds: Parameter
    limit: Parameter
    maxTimerLengthSeconds: Parameter
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    path: str
    selector: Parameter
    tagManagerUrl: str
    totalTimeMinMilliseconds: Parameter
    triggerId: str
    type: typing.Literal[
        "eventTypeUnspecified",
        "pageview",
        "domReady",
        "windowLoaded",
        "customEvent",
        "triggerGroup",
        "init",
        "consentInit",
        "serverPageview",
        "always",
        "firebaseAppException",
        "firebaseAppUpdate",
        "firebaseCampaign",
        "firebaseFirstOpen",
        "firebaseInAppPurchase",
        "firebaseNotificationDismiss",
        "firebaseNotificationForeground",
        "firebaseNotificationOpen",
        "firebaseNotificationReceive",
        "firebaseOsUpdate",
        "firebaseSessionStart",
        "firebaseUserEngagement",
        "formSubmission",
        "click",
        "linkClick",
        "jsError",
        "historyChange",
        "timer",
        "ampClick",
        "ampTimer",
        "ampScroll",
        "ampVisibility",
        "youTubeVideo",
        "scrollDepth",
        "elementVisibility",
    ]
    uniqueTriggerId: Parameter
    verticalScrollPercentageList: Parameter
    visibilitySelector: Parameter
    visiblePercentageMax: Parameter
    visiblePercentageMin: Parameter
    waitForTags: Parameter
    waitForTagsTimeout: Parameter
    workspaceId: str

@typing.type_check_only
class UserPermission(typing.TypedDict, total=False):
    accountAccess: AccountAccess
    accountId: str
    containerAccess: _list[ContainerAccess]
    emailAddress: str
    path: str

@typing.type_check_only
class Variable(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    disablingTriggerId: _list[str]
    enablingTriggerId: _list[str]
    fingerprint: str
    formatValue: VariableFormatValue
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    path: str
    scheduleEndMs: str
    scheduleStartMs: str
    tagManagerUrl: str
    type: str
    variableId: str
    workspaceId: str

@typing.type_check_only
class VariableFormatValue(typing.TypedDict, total=False):
    caseConversionType: typing.Literal["none", "lowercase", "uppercase"]
    convertFalseToValue: Parameter
    convertNullToValue: Parameter
    convertToBoolean: bool
    convertToNumber: typing.Literal[
        "decimalSeparatorTypeUnspecified", "period", "comma", "automatic"
    ]
    convertTrueToValue: Parameter
    convertUndefinedToValue: Parameter

@typing.type_check_only
class Workspace(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    description: str
    fingerprint: str
    name: str
    path: str
    tagManagerUrl: str
    workspaceId: str

@typing.type_check_only
class Zone(typing.TypedDict, total=False):
    accountId: str
    boundary: ZoneBoundary
    childContainer: _list[ZoneChildContainer]
    containerId: str
    fingerprint: str
    name: str
    notes: str
    path: str
    tagManagerUrl: str
    typeRestriction: ZoneTypeRestriction
    workspaceId: str
    zoneId: str

@typing.type_check_only
class ZoneBoundary(typing.TypedDict, total=False):
    condition: _list[Condition]
    customEvaluationTriggerId: _list[str]

@typing.type_check_only
class ZoneChildContainer(typing.TypedDict, total=False):
    nickname: str
    publicId: str

@typing.type_check_only
class ZoneTypeRestriction(typing.TypedDict, total=False):
    enable: bool
    whitelistedTypeId: _list[str]
