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
class LongRunningRecognizeRequest(typing_extensions.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig

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
class RecognitionAudio(typing_extensions.TypedDict, total=False):
    content: str
    uri: str

@typing.type_check_only
class RecognitionConfig(typing_extensions.TypedDict, total=False):
    audioChannelCount: int
    diarizationConfig: SpeakerDiarizationConfig
    enableAutomaticPunctuation: bool
    enableSeparateRecognitionPerChannel: bool
    enableWordTimeOffsets: bool
    encoding: typing_extensions.Literal[
        "ENCODING_UNSPECIFIED",
        "LINEAR16",
        "FLAC",
        "MULAW",
        "AMR",
        "AMR_WB",
        "OGG_OPUS",
        "SPEEX_WITH_HEADER_BYTE",
    ]
    languageCode: str
    maxAlternatives: int
    metadata: RecognitionMetadata
    model: str
    profanityFilter: bool
    sampleRateHertz: int
    speechContexts: typing.List[SpeechContext]
    useEnhanced: bool

@typing.type_check_only
class RecognitionMetadata(typing_extensions.TypedDict, total=False):
    audioTopic: str
    industryNaicsCodeOfAudio: int
    interactionType: typing_extensions.Literal[
        "INTERACTION_TYPE_UNSPECIFIED",
        "DISCUSSION",
        "PRESENTATION",
        "PHONE_CALL",
        "VOICEMAIL",
        "PROFESSIONALLY_PRODUCED",
        "VOICE_SEARCH",
        "VOICE_COMMAND",
        "DICTATION",
    ]
    microphoneDistance: typing_extensions.Literal[
        "MICROPHONE_DISTANCE_UNSPECIFIED", "NEARFIELD", "MIDFIELD", "FARFIELD"
    ]
    originalMediaType: typing_extensions.Literal[
        "ORIGINAL_MEDIA_TYPE_UNSPECIFIED", "AUDIO", "VIDEO"
    ]
    originalMimeType: str
    recordingDeviceName: str
    recordingDeviceType: typing_extensions.Literal[
        "RECORDING_DEVICE_TYPE_UNSPECIFIED",
        "SMARTPHONE",
        "PC",
        "PHONE_LINE",
        "VEHICLE",
        "OTHER_OUTDOOR_DEVICE",
        "OTHER_INDOOR_DEVICE",
    ]

@typing.type_check_only
class RecognizeRequest(typing_extensions.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig

@typing.type_check_only
class RecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

@typing.type_check_only
class SpeakerDiarizationConfig(typing_extensions.TypedDict, total=False):
    enableSpeakerDiarization: bool
    maxSpeakerCount: int
    minSpeakerCount: int
    speakerTag: int

@typing.type_check_only
class SpeechContext(typing_extensions.TypedDict, total=False):
    phrases: typing.List[str]

@typing.type_check_only
class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    confidence: float
    transcript: str
    words: typing.List[WordInfo]

@typing.type_check_only
class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    alternatives: typing.List[SpeechRecognitionAlternative]
    channelTag: int

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class WordInfo(typing_extensions.TypedDict, total=False):
    endTime: str
    speakerTag: int
    startTime: str
    word: str
