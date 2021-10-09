import typing

import typing_extensions

_list = list

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    progressPercent: int
    startTime: str
    uri: str

@typing.type_check_only
class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    results: _list[SpeechRecognitionResult]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    confidence: float
    transcript: str
    words: _list[WordInfo]

@typing.type_check_only
class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    alternatives: _list[SpeechRecognitionAlternative]
    channelTag: int
    languageCode: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    endOffset: str
    speakerTag: int
    startOffset: str
    word: str
