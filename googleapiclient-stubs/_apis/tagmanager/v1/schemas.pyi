import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    accountId: str
    fingerprint: str
    name: str
    shareData: bool

@typing.type_check_only
class AccountAccess(typing.TypedDict, total=False):
    permission: _list[
        typing.Literal["read", "edit", "publish", "delete", "manage", "editWorkspace"]
    ]

@typing.type_check_only
class Condition(typing.TypedDict, total=False):
    parameter: _list[Parameter]
    type: typing.Literal[
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
    enabledBuiltInVariable: _list[
        typing.Literal[
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
            "environmentName",
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
            "analyticsClientId",
            "analyticsSessionId",
            "analyticsSessionNumber",
        ]
    ]
    fingerprint: str
    name: str
    notes: str
    publicId: str
    timeZoneCountryId: str
    timeZoneId: str
    usageContext: _list[
        typing.Literal["web", "android", "ios", "androidSdk5", "iosSdk5", "amp"]
    ]

@typing.type_check_only
class ContainerAccess(typing.TypedDict, total=False):
    containerId: str
    permission: _list[
        typing.Literal["read", "edit", "publish", "delete", "manage", "editWorkspace"]
    ]

@typing.type_check_only
class ContainerVersion(typing.TypedDict, total=False):
    accountId: str
    container: Container
    containerId: str
    containerVersionId: str
    deleted: bool
    fingerprint: str
    folder: _list[Folder]
    name: str
    notes: str
    tag: _list[Tag]
    trigger: _list[Trigger]
    variable: _list[Variable]

@typing.type_check_only
class ContainerVersionHeader(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    containerVersionId: str
    deleted: bool
    name: str
    numTags: str
    numTriggers: str
    numVariables: str

@typing.type_check_only
class CreateContainerVersionRequestVersionOptions(typing.TypedDict, total=False):
    name: str
    notes: str
    quickPreview: bool

@typing.type_check_only
class CreateContainerVersionResponse(typing.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class Environment(typing.TypedDict, total=False):
    accountId: str
    authorizationCode: str
    authorizationTimestampMs: str
    containerId: str
    containerVersionId: str
    description: str
    enableDebug: bool
    environmentId: str
    fingerprint: str
    name: str
    type: typing.Literal["user", "live", "latest", "draft"]
    url: str

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    folderId: str
    name: str

@typing.type_check_only
class FolderEntities(typing.TypedDict, total=False):
    tag: _list[Tag]
    trigger: _list[Trigger]
    variable: _list[Variable]

@typing.type_check_only
class ListAccountUsersResponse(typing.TypedDict, total=False):
    userAccess: _list[UserAccess]

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]

@typing.type_check_only
class ListContainerVersionsResponse(typing.TypedDict, total=False):
    containerVersion: _list[ContainerVersion]
    containerVersionHeader: _list[ContainerVersionHeader]

@typing.type_check_only
class ListContainersResponse(typing.TypedDict, total=False):
    containers: _list[Container]

@typing.type_check_only
class ListEnvironmentsResponse(typing.TypedDict, total=False):
    environments: _list[Environment]

@typing.type_check_only
class ListFoldersResponse(typing.TypedDict, total=False):
    folders: _list[Folder]

@typing.type_check_only
class ListTagsResponse(typing.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class ListTriggersResponse(typing.TypedDict, total=False):
    triggers: _list[Trigger]

@typing.type_check_only
class ListVariablesResponse(typing.TypedDict, total=False):
    variables: _list[Variable]

@typing.type_check_only
class Parameter(typing.TypedDict, total=False):
    key: str
    list: _list[Parameter]
    map: _list[Parameter]
    type: typing.Literal[
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
class PublishContainerVersionResponse(typing.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class SetupTag(typing.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    accountId: str
    blockingTriggerId: _list[str]
    containerId: str
    fingerprint: str
    firingTriggerId: _list[str]
    liveOnly: bool
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    paused: bool
    priority: Parameter
    scheduleEndMs: str
    scheduleStartMs: str
    setupTag: _list[SetupTag]
    tagFiringOption: typing.Literal["unlimited", "oncePerEvent", "oncePerLoad"]
    tagId: str
    teardownTag: _list[TeardownTag]
    type: str

@typing.type_check_only
class TeardownTag(typing.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

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
    parameter: _list[Parameter]
    parentFolderId: str
    selector: Parameter
    totalTimeMinMilliseconds: Parameter
    triggerId: str
    type: typing.Literal[
        "pageview",
        "domReady",
        "windowLoaded",
        "customEvent",
        "triggerGroup",
        "always",
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

@typing.type_check_only
class UserAccess(typing.TypedDict, total=False):
    accountAccess: AccountAccess
    accountId: str
    containerAccess: _list[ContainerAccess]
    emailAddress: str
    permissionId: str

@typing.type_check_only
class Variable(typing.TypedDict, total=False):
    accountId: str
    containerId: str
    disablingTriggerId: _list[str]
    enablingTriggerId: _list[str]
    fingerprint: str
    name: str
    notes: str
    parameter: _list[Parameter]
    parentFolderId: str
    scheduleEndMs: str
    scheduleStartMs: str
    type: str
    variableId: str
