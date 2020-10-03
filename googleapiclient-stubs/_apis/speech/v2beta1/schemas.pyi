import typing

import typing_extensions

class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    startTime: str
    uri: str
    progressPercent: int

class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    speakerTag: int
    startOffset: str
    endOffset: str
    word: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    confidence: float
    transcript: str
    words: typing.List[WordInfo]

class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    channelTag: int
    languageCode: str
    alternatives: typing.List[SpeechRecognitionAlternative]
