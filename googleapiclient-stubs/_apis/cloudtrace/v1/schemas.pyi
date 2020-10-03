import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class ListTracesResponse(typing_extensions.TypedDict, total=False):
    traces: typing.List[Trace]
    nextPageToken: str

class Trace(typing_extensions.TypedDict, total=False):
    spans: typing.List[TraceSpan]
    traceId: str
    projectId: str

class Traces(typing_extensions.TypedDict, total=False):
    traces: typing.List[Trace]

class TraceSpan(typing_extensions.TypedDict, total=False):
    parentSpanId: str
    spanId: str
    endTime: str
    kind: typing_extensions.Literal["SPAN_KIND_UNSPECIFIED", "RPC_SERVER", "RPC_CLIENT"]
    name: str
    startTime: str
    labels: typing.Dict[str, typing.Any]
