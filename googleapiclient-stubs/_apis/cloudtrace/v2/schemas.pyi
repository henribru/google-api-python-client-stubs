import typing

import typing_extensions

_list = list

@typing.type_check_only
class Annotation(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    description: TruncatableString

@typing.type_check_only
class AttributeValue(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    stringValue: TruncatableString

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    attributeMap: dict[str, typing.Any]
    droppedAttributesCount: int

@typing.type_check_only
class BatchWriteSpansRequest(typing_extensions.TypedDict, total=False):
    spans: _list[Span]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    spanId: str
    traceId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "CHILD_LINKED_SPAN", "PARENT_LINKED_SPAN"
    ]

@typing.type_check_only
class Links(typing_extensions.TypedDict, total=False):
    droppedLinksCount: int
    link: _list[Link]

@typing.type_check_only
class MessageEvent(typing_extensions.TypedDict, total=False):
    compressedSizeBytes: str
    id: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SENT", "RECEIVED"]
    uncompressedSizeBytes: str

@typing.type_check_only
class Module(typing_extensions.TypedDict, total=False):
    buildId: TruncatableString
    module: TruncatableString

@typing.type_check_only
class Span(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    childSpanCount: int
    displayName: TruncatableString
    endTime: str
    links: Links
    name: str
    parentSpanId: str
    sameProcessAsParentSpan: bool
    spanId: str
    spanKind: typing_extensions.Literal[
        "SPAN_KIND_UNSPECIFIED", "INTERNAL", "SERVER", "CLIENT", "PRODUCER", "CONSUMER"
    ]
    stackTrace: StackTrace
    startTime: str
    status: Status
    timeEvents: TimeEvents

@typing.type_check_only
class StackFrame(typing_extensions.TypedDict, total=False):
    columnNumber: str
    fileName: TruncatableString
    functionName: TruncatableString
    lineNumber: str
    loadModule: Module
    originalFunctionName: TruncatableString
    sourceVersion: TruncatableString

@typing.type_check_only
class StackFrames(typing_extensions.TypedDict, total=False):
    droppedFramesCount: int
    frame: _list[StackFrame]

@typing.type_check_only
class StackTrace(typing_extensions.TypedDict, total=False):
    stackFrames: StackFrames
    stackTraceHashId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeEvent(typing_extensions.TypedDict, total=False):
    annotation: Annotation
    messageEvent: MessageEvent
    time: str

@typing.type_check_only
class TimeEvents(typing_extensions.TypedDict, total=False):
    droppedAnnotationsCount: int
    droppedMessageEventsCount: int
    timeEvent: _list[TimeEvent]

@typing.type_check_only
class TruncatableString(typing_extensions.TypedDict, total=False):
    truncatedByteCount: int
    value: str
