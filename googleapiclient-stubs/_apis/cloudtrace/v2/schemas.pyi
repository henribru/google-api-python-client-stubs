import typing

import typing_extensions

class StackFrame(typing_extensions.TypedDict, total=False):
    functionName: TruncatableString
    sourceVersion: TruncatableString
    fileName: TruncatableString
    loadModule: Module
    columnNumber: str
    originalFunctionName: TruncatableString
    lineNumber: str

class Link(typing_extensions.TypedDict, total=False):
    spanId: str
    traceId: str
    attributes: Attributes
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "CHILD_LINKED_SPAN", "PARENT_LINKED_SPAN"
    ]

class TimeEvents(typing_extensions.TypedDict, total=False):
    droppedAnnotationsCount: int
    timeEvent: typing.List[TimeEvent]
    droppedMessageEventsCount: int

class MessageEvent(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SENT", "RECEIVED"]
    compressedSizeBytes: str
    uncompressedSizeBytes: str
    id: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Links(typing_extensions.TypedDict, total=False):
    droppedLinksCount: int
    link: typing.List[Link]

class Span(typing_extensions.TypedDict, total=False):
    stackTrace: StackTrace
    sameProcessAsParentSpan: bool
    timeEvents: TimeEvents
    endTime: str
    links: Links
    parentSpanId: str
    childSpanCount: int
    spanId: str
    attributes: Attributes
    name: str
    spanKind: typing_extensions.Literal[
        "SPAN_KIND_UNSPECIFIED", "INTERNAL", "SERVER", "CLIENT", "PRODUCER", "CONSUMER"
    ]
    startTime: str
    displayName: TruncatableString
    status: Status

class TimeEvent(typing_extensions.TypedDict, total=False):
    time: str
    annotation: Annotation
    messageEvent: MessageEvent

class Annotation(typing_extensions.TypedDict, total=False):
    description: TruncatableString
    attributes: Attributes

class TruncatableString(typing_extensions.TypedDict, total=False):
    value: str
    truncatedByteCount: int

class StackTrace(typing_extensions.TypedDict, total=False):
    stackTraceHashId: str
    stackFrames: StackFrames

class StackFrames(typing_extensions.TypedDict, total=False):
    frame: typing.List[StackFrame]
    droppedFramesCount: int

class BatchWriteSpansRequest(typing_extensions.TypedDict, total=False):
    spans: typing.List[Span]

class AttributeValue(typing_extensions.TypedDict, total=False):
    stringValue: TruncatableString
    boolValue: bool
    intValue: str

class Attributes(typing_extensions.TypedDict, total=False):
    attributeMap: typing.Dict[str, typing.Any]
    droppedAttributesCount: int

class Empty(typing_extensions.TypedDict, total=False): ...

class Module(typing_extensions.TypedDict, total=False):
    buildId: TruncatableString
    module: TruncatableString
