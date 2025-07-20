import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActivateDataSegmentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DataSegment(typing_extensions.TypedDict, total=False):
    cpmFee: Money
    createTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    updateTime: str

@typing.type_check_only
class DeactivateDataSegmentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListDataSegmentsResponse(typing_extensions.TypedDict, total=False):
    dataSegments: _list[DataSegment]
    nextPageToken: str

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str
