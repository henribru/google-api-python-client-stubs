import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountId: str
    fingerprint: str
    name: str
    shareData: bool

@typing.type_check_only
class AccountAccess(typing_extensions.TypedDict, total=False):
    permission: _list[str]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
    parameter: _list[Parameter]
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
    domainName: _list[str]
    enabledBuiltInVariable: _list[str]
    fingerprint: str
    name: str
    notes: str
    publicId: str
    timeZoneCountryId: str
    timeZoneId: str
    usageContext: _list[str]

@typing.type_check_only
class ContainerAccess(typing_extensions.TypedDict, total=False):
    containerId: str
    permission: _list[str]

@typing.type_check_only
class ContainerVersion(typing_extensions.TypedDict, total=False):
    accountId: str
    container: Container
    containerId: str
    containerVersionId: str
    deleted: bool
    fingerprint: str
    folder: _list[Folder]
    macro: _list[Macro]
    name: str
    notes: str
    rule: _list[Rule]
    tag: _list[Tag]
    trigger: _list[Trigger]
    variable: _list[Variable]

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
    tag: _list[Tag]
    trigger: _list[Trigger]
    variable: _list[Variable]

@typing.type_check_only
class ListAccountUsersResponse(typing_extensions.TypedDict, total=False):
    userAccess: _list[UserAccess]

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]

@typing.type_check_only
class ListContainerVersionsResponse(typing_extensions.TypedDict, total=False):
    containerVersion: _list[ContainerVersion]
    containerVersionHeader: _list[ContainerVersionHeader]

@typing.type_check_only
class ListContainersResponse(typing_extensions.TypedDict, total=False):
    containers: _list[Container]

@typing.type_check_only
class ListEnvironmentsResponse(typing_extensions.TypedDict, total=False):
    environments: _list[Environment]

@typing.type_check_only
class ListFoldersResponse(typing_extensions.TypedDict, total=False):
    folders: _list[Folder]

@typing.type_check_only
class ListTagsResponse(typing_extensions.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    triggers: _list[Trigger]

@typing.type_check_only
class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    variables: _list[Variable]

@typing.type_check_only
class Macro(dict[str, typing.Any]): ...

@typing.type_check_only
class Parameter(dict[str, typing.Any]): ...

@typing.type_check_only
class PublishContainerVersionResponse(typing_extensions.TypedDict, total=False):
    compilerError: bool
    containerVersion: ContainerVersion

@typing.type_check_only
class Rule(dict[str, typing.Any]): ...

@typing.type_check_only
class SetupTag(typing_extensions.TypedDict, total=False):
    stopOnSetupFailure: bool
    tagName: str

@typing.type_check_only
class Tag(dict[str, typing.Any]): ...

@typing.type_check_only
class TeardownTag(typing_extensions.TypedDict, total=False):
    stopTeardownOnFailure: bool
    tagName: str

@typing.type_check_only
class Trigger(dict[str, typing.Any]): ...

@typing.type_check_only
class UserAccess(typing_extensions.TypedDict, total=False):
    accountAccess: AccountAccess
    accountId: str
    containerAccess: _list[ContainerAccess]
    emailAddress: str
    permissionId: str

@typing.type_check_only
class Variable(dict[str, typing.Any]): ...
