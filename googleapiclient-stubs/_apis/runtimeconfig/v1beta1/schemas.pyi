import typing

import typing_extensions

class ListWaitersResponse(typing_extensions.TypedDict, total=False):
    waiters: typing.List[Waiter]
    nextPageToken: str

class Waiter(typing_extensions.TypedDict, total=False):
    failure: EndCondition
    name: str
    error: Status
    done: bool
    timeout: str
    createTime: str
    success: EndCondition

class Cardinality(typing_extensions.TypedDict, total=False):
    path: str
    number: int

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class WatchVariableRequest(typing_extensions.TypedDict, total=False):
    newerThan: str

class Variable(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    updateTime: str
    state: typing_extensions.Literal["VARIABLE_STATE_UNSPECIFIED", "UPDATED", "DELETED"]
    text: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListConfigsResponse(typing_extensions.TypedDict, total=False):
    configs: typing.List[RuntimeConfig]
    nextPageToken: str

class ListVariablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    variables: typing.List[Variable]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    members: typing.List[str]
    condition: Expr
    role: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class EndCondition(typing_extensions.TypedDict, total=False):
    cardinality: Cardinality

class RuntimeConfig(typing_extensions.TypedDict, total=False):
    name: str
    description: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
