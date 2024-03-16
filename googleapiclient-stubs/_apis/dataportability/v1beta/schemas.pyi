import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InitiatePortabilityArchiveRequest(typing_extensions.TypedDict, total=False):
    resources: _list[str]

@typing.type_check_only
class InitiatePortabilityArchiveResponse(typing_extensions.TypedDict, total=False):
    archiveJobId: str

@typing.type_check_only
class PortabilityArchiveState(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETE", "FAILED", "CANCELLED"
    ]
    urls: _list[str]

@typing.type_check_only
class ResetAuthorizationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryPortabilityArchiveRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryPortabilityArchiveResponse(typing_extensions.TypedDict, total=False):
    archiveJobId: str
