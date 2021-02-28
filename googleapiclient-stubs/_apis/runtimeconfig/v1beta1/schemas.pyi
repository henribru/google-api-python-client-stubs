import typing

import typing_extensions
@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Cardinality(typing_extensions.TypedDict, total=False):
    number: int
    path: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EndCondition(typing_extensions.TypedDict, total=False):
    cardinality: Cardinality

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListConfigsResponse(typing_extensions.TypedDict, total=False):
    configs: typing.List[RuntimeConfig]
    nextPageToken: str

@typing.type_check_only
class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    variables: typing.List[Variable]

@typing.type_check_only
class ListWaitersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    waiters: typing.List[Waiter]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    description: str
    name: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Variable(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal["VARIABLE_STATE_UNSPECIFIED", "UPDATED", "DELETED"]
    text: str
    updateTime: str
    value: str

@typing.type_check_only
class Waiter(typing_extensions.TypedDict, total=False):
    createTime: str
    done: bool
    error: Status
    failure: EndCondition
    name: str
    success: EndCondition
    timeout: str

@typing.type_check_only
class WatchVariableRequest(typing_extensions.TypedDict, total=False):
    newerThan: str
