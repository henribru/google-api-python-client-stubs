import typing

_list = list

@typing.type_check_only
class CancelPortabilityArchiveRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelPortabilityArchiveResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckAccessTypeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckAccessTypeResponse(typing.TypedDict, total=False):
    oneTimeResources: _list[str]
    timeBasedResources: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class InitiatePortabilityArchiveRequest(typing.TypedDict, total=False):
    endTime: str
    resources: _list[str]
    startTime: str

@typing.type_check_only
class InitiatePortabilityArchiveResponse(typing.TypedDict, total=False):
    accessType: typing.Literal[
        "ACCESS_TYPE_UNSPECIFIED", "ACCESS_TYPE_ONE_TIME", "ACCESS_TYPE_TIME_BASED"
    ]
    archiveJobId: str

@typing.type_check_only
class PortabilityArchiveState(typing.TypedDict, total=False):
    exportTime: str
    name: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "IN_PROGRESS", "COMPLETE", "FAILED", "CANCELLED"
    ]
    urls: _list[str]

@typing.type_check_only
class ResetAuthorizationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetryPortabilityArchiveRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetryPortabilityArchiveResponse(typing.TypedDict, total=False):
    archiveJobId: str
