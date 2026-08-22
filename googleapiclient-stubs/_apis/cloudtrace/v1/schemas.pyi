import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListTracesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    traces: _list[Trace]

@typing.type_check_only
class Trace(typing.TypedDict, total=False):
    projectId: str
    spans: _list[TraceSpan]
    traceId: str

@typing.type_check_only
class TraceSpan(typing.TypedDict, total=False):
    endTime: str
    kind: typing.Literal["SPAN_KIND_UNSPECIFIED", "RPC_SERVER", "RPC_CLIENT"]
    labels: dict[str, typing.Any]
    name: str
    parentSpanId: str
    spanId: str
    startTime: str

@typing.type_check_only
class Traces(typing.TypedDict, total=False):
    traces: _list[Trace]
