import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListTracesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    traces: _list[Trace]

@typing.type_check_only
class Trace(typing_extensions.TypedDict, total=False):
    projectId: str
    spans: _list[TraceSpan]
    traceId: str

@typing.type_check_only
class TraceSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    kind: typing_extensions.Literal["SPAN_KIND_UNSPECIFIED", "RPC_SERVER", "RPC_CLIENT"]
    labels: dict[str, typing.Any]
    name: str
    parentSpanId: str
    spanId: str
    startTime: str

@typing.type_check_only
class Traces(typing_extensions.TypedDict, total=False):
    traces: _list[Trace]
