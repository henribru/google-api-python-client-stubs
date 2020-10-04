import typing

import typing_extensions
@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountId: str
    fingerprint: str
    name: str
    shareData: bool

@typing.type_check_only
class AccountAccess(typing_extensions.TypedDict, total=False):
    permission: typing.List[str]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    parameter: typing.List[Parameter]
    type: typing_extensions.Literal[
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
    enabledBuiltInVariable: typing.List[str]
    fingerprint: str
    name: str
    notes: str
    publicId: str
    timeZoneCountryId: str
    timeZoneId: str
    usageContext: typing.List[str]

@typing.type_check_only
class ContainerAccess(typing_extensions.TypedDict, total=False):
    containerId: str
    permission: typing.List[str]

@typing.type_check_only
class ContainerVersion(typing_extensions.TypedDict, total=False):
    accountId: str
    container: Container
    containerId: str
    containerVersionId: str
    deleted: bool
    fingerprint: str
    folder: typing.List[Folder]
    macro: typing.List[Macro]
    name: str
    notes: str
    rule: typing.List[Rule]
    tag: typing.List[Tag]
    trigger: typing.List[Trigger]
    variable: typing.List[Variable]

@typing.type_check_only
class ContainerVersionHeader(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    containerVersionId: str
    deleted: bool
    name: str
    numMacros: str
    numRules: str
    numTags: str
    numTriggers: str
    numVariables: str

@typing.type_check_only
class CreateContainerVersionRequestVersionOptions(
    typing_extensions.TypedDict, total=False
):
    name: str
    notes: str
    quickPreview: bool

@typing.type_check_only
class CreateContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class Environment(typing_extensions.TypedDict, total=False):
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
    type: typing_extensions.Literal["user", "live", "latest", "draft"]
    url: str

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    accountId: str
    containerId: str
    fingerprint: str
    folderId: str
    name: str

@typing.type_check_only
class FolderEntities(typing_extensions.TypedDict, total=False):
    tag: typing.List[Tag]
    trigger: typing.List[Trigger]
    variable: typing.List[Variable]

@typing.type_check_only
class ListAccountUsersResponse(typing_extensions.TypedDict, total=False):
    userAccess: typing.List[UserAccess]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[Account]

@typing.type_check_only
class ListContainerVersionsResponse(typing_extensions.TypedDict, total=False):
    containerVersion: typing.List[ContainerVersion]
    containerVersionHeader: typing.List[ContainerVersionHeader]

@typing.type_check_only
class ListContainersResponse(typing_extensions.TypedDict, total=False):
    containers: typing.List[Container]

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: typing.List[Environment]

@typing.type_check_only
class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: typing.List[Folder]

@typing.type_check_only
class ListTagsResponse(typing_extensions.TypedDict, total=False):
    tags: typing.List[Tag]

@typing.type_check_only
class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    triggers: typing.List[Trigger]

@typing.type_check_only
class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    variables: typing.List[Variable]

@typing.type_check_only
class Macro(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Parameter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class PublishContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class Rule(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class SetupTag(typing_extensions.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

@typing.type_check_only
class Tag(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TeardownTag(typing_extensions.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

@typing.type_check_only
class Trigger(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class UserAccess(typing_extensions.TypedDict, total=False):
    accountAccess: AccountAccess
    accountId: str
    containerAccess: typing.List[ContainerAccess]
    emailAddress: str
    permissionId: str

@typing.type_check_only
class Variable(typing.Dict[str, typing.Any]): ...
