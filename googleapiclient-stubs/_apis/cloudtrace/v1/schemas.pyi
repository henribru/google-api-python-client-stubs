import typing

import typing_extensions
@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListTracesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    traces: typing.List[Trace]

@typing.type_check_only
class Trace(typing_extensions.TypedDict, total=False):
    projectId: str
    spans: typing.List[TraceSpan]
    traceId: str

@typing.type_check_only
class TraceSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    kind: typing_extensions.Literal["SPAN_KIND_UNSPECIFIED", "RPC_SERVER", "RPC_CLIENT"]
    labels: typing.Dict[str, typing.Any]
    name: str
    parentSpanId: str
    spanId: str
    startTime: str

@typing.type_check_only
class Traces(typing_extensions.TypedDict, total=False):
    traces: typing.List[Trace]
