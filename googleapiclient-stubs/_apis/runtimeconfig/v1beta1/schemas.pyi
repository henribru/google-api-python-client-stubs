import typing

import typing_extensions

_list = list

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
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
    configs: _list[RuntimeConfig]
    nextPageToken: str

@typing.type_check_only
class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    variables: _list[Variable]

@typing.type_check_only
class ListWaitersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    waiters: _list[Waiter]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
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
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

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
