import typing

import typing_extensions
@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    progressPercent: int
    startTime: str
    uri: str

@typing.type_check_only
class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    confidence: float
    transcript: str
    words: typing.List[WordInfo]

@typing.type_check_only
class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    alternatives: typing.List[SpeechRecognitionAlternative]
    channelTag: int
    languageCode: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    endOffset: str
    speakerTag: int
    startOffset: str
    word: str
