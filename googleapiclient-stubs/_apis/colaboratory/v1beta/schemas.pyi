import typing

_list = list

@typing.type_check_only
class ConnectionInfo(typing.TypedDict, total=False):
    expireTime: str
    token: str
    url: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorInfo(typing.TypedDict, total=False):
    domain: str
    metadata: dict[str, typing.Any]
    reason: str

@typing.type_check_only
class Key(typing.TypedDict, total=False):
    accelerator: str
    shape: typing.Literal["SHAPE_UNSPECIFIED", "SHAPE_STANDARD", "SHAPE_HIGHMEM"]
    variant: typing.Literal[
        "VARIANT_UNSPECIFIED", "VARIANT_CPU", "VARIANT_GPU", "VARIANT_TPU"
    ]

@typing.type_check_only
class ListRuntimeSpecsResponse(typing.TypedDict, total=False):
    runtimeSpecs: _list[RuntimeSpec]

@typing.type_check_only
class ListRuntimesResponse(typing.TypedDict, total=False):
    runtimes: _list[Runtime]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Runtime(typing.TypedDict, total=False):
    connectionInfo: ConnectionInfo
    name: str
    runtimeSpec: Key
    version: str

@typing.type_check_only
class RuntimeSpec(typing.TypedDict, total=False):
    eligible: bool
    key: Key

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    name: str
    tier: typing.Literal[
        "SUBSCRIPTION_TIER_UNSPECIFIED",
        "SUBSCRIPTION_TIER_FREE",
        "SUBSCRIPTION_TIER_PRO",
        "SUBSCRIPTION_TIER_PRO_PLUS",
    ]
