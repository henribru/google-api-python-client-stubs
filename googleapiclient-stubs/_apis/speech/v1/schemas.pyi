import typing

import typing_extensions

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class RecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    lastUpdateTime: str
    progressPercent: int
    uri: str

class RecognizeRequest(typing_extensions.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig

class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

class WordInfo(typing_extensions.TypedDict, total=False):
    endTime: str
    word: str
    speakerTag: int
    startTime: str

class LongRunningRecognizeRequest(typing_extensions.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig

class SpeakerDiarizationConfig(typing_extensions.TypedDict, total=False):
    minSpeakerCount: int
    maxSpeakerCount: int
    enableSpeakerDiarization: bool
    speakerTag: int

class RecognitionConfig(typing_extensions.TypedDict, total=False):
    profanityFilter: bool
    enableSeparateRecognitionPerChannel: bool
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
    useEnhanced: bool
    diarizationConfig: SpeakerDiarizationConfig
    audioChannelCount: int
    sampleRateHertz: int
    enableAutomaticPunctuation: bool
    enableWordTimeOffsets: bool
    metadata: RecognitionMetadata
    model: str
    languageCode: str
    speechContexts: typing.List[SpeechContext]
    maxAlternatives: int

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class SpeechContext(typing_extensions.TypedDict, total=False):
    phrases: typing.List[str]

class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    alternatives: typing.List[SpeechRecognitionAlternative]
    channelTag: int

class RecognitionAudio(typing_extensions.TypedDict, total=False):
    content: str
    uri: str

class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    transcript: str
    confidence: float
    words: typing.List[WordInfo]

class RecognitionMetadata(typing_extensions.TypedDict, total=False):
    audioTopic: str
    originalMediaType: typing_extensions.Literal[
        "ORIGINAL_MEDIA_TYPE_UNSPECIFIED", "AUDIO", "VIDEO"
    ]
    recordingDeviceName: str
    microphoneDistance: typing_extensions.Literal[
        "MICROPHONE_DISTANCE_UNSPECIFIED", "NEARFIELD", "MIDFIELD", "FARFIELD"
    ]
    originalMimeType: str
    industryNaicsCodeOfAudio: int
    recordingDeviceType: typing_extensions.Literal[
        "RECORDING_DEVICE_TYPE_UNSPECIFIED",
        "SMARTPHONE",
        "PC",
        "PHONE_LINE",
        "VEHICLE",
        "OTHER_OUTDOOR_DEVICE",
        "OTHER_INDOOR_DEVICE",
    ]
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

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
