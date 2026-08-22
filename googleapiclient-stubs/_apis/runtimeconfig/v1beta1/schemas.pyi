import typing

_list = list

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Cardinality(typing.TypedDict, total=False):
    number: int
    path: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EndCondition(typing.TypedDict, total=False):
    cardinality: Cardinality

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListConfigsResponse(typing.TypedDict, total=False):
    configs: _list[RuntimeConfig]
    nextPageToken: str

@typing.type_check_only
class ListVariablesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    variables: _list[Variable]

@typing.type_check_only
class ListWaitersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    waiters: _list[Waiter]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RuntimeConfig(typing.TypedDict, total=False):
    description: str
    name: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Variable(typing.TypedDict, total=False):
    name: str
    state: typing.Literal["VARIABLE_STATE_UNSPECIFIED", "UPDATED", "DELETED"]
    text: str
    updateTime: str
    value: str

@typing.type_check_only
class Waiter(typing.TypedDict, total=False):
    createTime: str
    done: bool
    error: Status
    failure: EndCondition
    name: str
    success: EndCondition
    timeout: str

@typing.type_check_only
class WatchVariableRequest(typing.TypedDict, total=False):
    newerThan: str
