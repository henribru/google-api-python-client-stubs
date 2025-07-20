import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelPortabilityArchiveRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelPortabilityArchiveResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckAccessTypeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckAccessTypeResponse(typing_extensions.TypedDict, total=False):
    oneTimeResources: _list[str]
    timeBasedResources: _list[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InitiatePortabilityArchiveRequest(typing_extensions.TypedDict, total=False):
    endTime: str
    resources: _list[str]
    startTime: str

@typing.type_check_only
class InitiatePortabilityArchiveResponse(typing_extensions.TypedDict, total=False):
    accessType: typing_extensions.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "ACCESS_TYPE_ONE_TIME", "ACCESS_TYPE_TIME_BASED"
    ]
    archiveJobId: str

@typing.type_check_only
class PortabilityArchiveState(typing_extensions.TypedDict, total=False):
    exportTime: str
    name: str
    startTime: str
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
