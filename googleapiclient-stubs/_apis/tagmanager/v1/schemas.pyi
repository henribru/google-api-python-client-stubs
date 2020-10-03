import typing

import typing_extensions

class Folder(typing_extensions.TypedDict, total=False):
    fingerprint: str
    accountId: str
    folderId: str
    name: str
    containerId: str

class Parameter(typing.Dict[str, typing.Any]): ...

class ListAccountUsersResponse(typing_extensions.TypedDict, total=False):
    userAccess: typing.List[UserAccess]

class ListContainerVersionsResponse(typing_extensions.TypedDict, total=False):
    containerVersion: typing.List[ContainerVersion]
    containerVersionHeader: typing.List[ContainerVersionHeader]

class ListContainersResponse(typing_extensions.TypedDict, total=False):
    containers: typing.List[Container]

class TeardownTag(typing_extensions.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[Account]

class SetupTag(typing_extensions.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

class ContainerVersionHeader(typing_extensions.TypedDict, total=False):
    containerVersionId: str
    numTriggers: str
    containerId: str
    numTags: str
    numMacros: str
    name: str
    accountId: str
    deleted: bool
    numRules: str
    numVariables: str

class Account(typing_extensions.TypedDict, total=False):
    accountId: str
    fingerprint: str
    shareData: bool
    name: str

class Trigger(typing_extensions.TypedDict, total=False):
    triggerId: str
    containerId: str
    continuousTimeMinMilliseconds: Parameter
    totalTimeMinMilliseconds: Parameter
    filter: typing.List[Condition]
    autoEventFilter: typing.List[Condition]
    intervalSeconds: Parameter
    visibilitySelector: Parameter
    fingerprint: str
    horizontalScrollPercentageList: Parameter
    checkValidation: Parameter
    waitForTags: Parameter
    accountId: str
    name: str
    parameter: typing.List[Parameter]
    eventName: Parameter
    maxTimerLengthSeconds: Parameter
    parentFolderId: str
    customEventFilter: typing.List[Condition]
    type: typing_extensions.Literal[
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
    interval: Parameter
    waitForTagsTimeout: Parameter
    verticalScrollPercentageList: Parameter
    visiblePercentageMax: Parameter
    selector: Parameter
    uniqueTriggerId: Parameter
    limit: Parameter
    visiblePercentageMin: Parameter

class AccountAccess(typing_extensions.TypedDict, total=False):
    permission: typing.List[str]

class PublishContainerVersionResponse(typing_extensions.TypedDict, total=False):
    containerVersion: ContainerVersion
    compilerError: bool

class Tag(typing_extensions.TypedDict, total=False):
    firingRuleId: typing.List[str]
    teardownTag: typing.List[TeardownTag]
    priority: Parameter
    type: str
    containerId: str
    scheduleEndMs: str
    tagFiringOption: typing_extensions.Literal[
        "unlimited", "oncePerEvent", "oncePerLoad"
    ]
    parentFolderId: str
    tagId: str
    liveOnly: bool
    setupTag: typing.List[SetupTag]
    blockingTriggerId: typing.List[str]
    blockingRuleId: typing.List[str]
    fingerprint: str
    firingTriggerId: typing.List[str]
    parameter: typing.List[Parameter]
    accountId: str
    notes: str
    name: str
    scheduleStartMs: str
    paused: bool

class Macro(typing_extensions.TypedDict, total=False):
    accountId: str
    macroId: str
    enablingRuleId: typing.List[str]
    fingerprint: str
    scheduleStartMs: str
    containerId: str
    type: str
    notes: str
    name: str
    scheduleEndMs: str
    parentFolderId: str
    parameter: typing.List[Parameter]
    disablingRuleId: typing.List[str]

class FolderEntities(typing_extensions.TypedDict, total=False):
    tag: typing.List[Tag]
    trigger: typing.List[Trigger]
    variable: typing.List[Variable]

class ListTagsResponse(typing_extensions.TypedDict, total=False):
    tags: typing.List[Tag]

class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    triggers: typing.List[Trigger]

class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]

class ContainerVersion(typing.Dict[str, typing.Any]): ...
class Rule(typing.Dict[str, typing.Any]): ...
class Condition(typing.Dict[str, typing.Any]): ...

class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: typing.List[Folder]

class Container(typing_extensions.TypedDict, total=False):
    enabledBuiltInVariable: typing.List[str]
    timeZoneId: str
    timeZoneCountryId: str
    notes: str
    usageContext: typing.List[str]
    accountId: str
    publicId: str
    name: str
    domainName: typing.List[str]
    containerId: str
    fingerprint: str

class Environment(typing_extensions.TypedDict, total=False):
    authorizationCode: str
    fingerprint: str
    url: str
    type: typing_extensions.Literal["user", "live", "latest", "draft"]
    containerId: str
    containerVersionId: str
    accountId: str
    authorizationTimestampMs: str
    environmentId: str
    description: str
    enableDebug: bool
    name: str

class CreateContainerVersionRequestVersionOptions(
    typing_extensions.TypedDict, total=False
):
    quickPreview: bool
    notes: str
    name: str

class UserAccess(typing_extensions.TypedDict, total=False):
    accountAccess: AccountAccess
    containerAccess: typing.List[ContainerAccess]
    permissionId: str
    accountId: str
    emailAddress: str

class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    variables: typing.List[Variable]

class ContainerAccess(typing_extensions.TypedDict, total=False):
    permission: typing.List[str]
    containerId: str

class CreateContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

class Variable(typing.Dict[str, typing.Any]): ...
