import typing

import typing_extensions

class SpeechRecognitionAlternative(typing_extensions.TypedDict, total=False):
    words: typing.List[WordInfo]
    confidence: float
    transcript: str

class SpeechRecognitionResult(typing_extensions.TypedDict, total=False):
    channelTag: int
    languageCode: str
    alternatives: typing.List[SpeechRecognitionAlternative]

class LongRunningRecognizeRequest(typing_extensions.TypedDict, total=False):
    config: RecognitionConfig
    audio: RecognitionAudio

class SpeakerDiarizationConfig(typing_extensions.TypedDict, total=False):
    minSpeakerCount: int
    maxSpeakerCount: int
    speakerTag: int
    enableSpeakerDiarization: bool

class WordInfo(typing_extensions.TypedDict, total=False):
    word: str
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str

class RecognitionConfig(typing_extensions.TypedDict, total=False):
    diarizationConfig: SpeakerDiarizationConfig
    adaptation: SpeechAdaptation
    enableAutomaticPunctuation: bool
    useEnhanced: bool
    alternativeLanguageCodes: typing.List[str]
    encoding: typing_extensions.Literal[
        "ENCODING_UNSPECIFIED",
        "LINEAR16",
        "FLAC",
        "MULAW",
        "AMR",
        "AMR_WB",
        "OGG_OPUS",
        "SPEEX_WITH_HEADER_BYTE",
        "MP3",
        "WEBM_OPUS",
    ]
    metadata: RecognitionMetadata
    model: str
    languageCode: str
    enableSpeakerDiarization: bool
    enableWordConfidence: bool
    profanityFilter: bool
    enableWordTimeOffsets: bool
    maxAlternatives: int
    audioChannelCount: int
    diarizationSpeakerCount: int
    enableSeparateRecognitionPerChannel: bool
    speechContexts: typing.List[SpeechContext]
    sampleRateHertz: int

class Phrase(typing_extensions.TypedDict, total=False):
    value: str
    boost: float

class RecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

class SpeechAdaptation(typing_extensions.TypedDict, total=False):
    customClasses: typing.List[CustomClass]
    phraseSets: typing.List[PhraseSet]

class RecognitionAudio(typing_extensions.TypedDict, total=False):
    content: str
    uri: str

class PhraseSet(typing_extensions.TypedDict, total=False):
    phrases: typing.List[Phrase]
    name: str
    boost: float

class SpeechContext(typing_extensions.TypedDict, total=False):
    boost: float
    phrases: typing.List[str]

class ClassItem(typing_extensions.TypedDict, total=False):
    value: str

class RecognizeRequest(typing_extensions.TypedDict, total=False):
    config: RecognitionConfig
    audio: RecognitionAudio

class CustomClass(typing_extensions.TypedDict, total=False):
    customClassId: str
    name: str
    items: typing.List[ClassItem]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    startTime: str
    uri: str
    progressPercent: int

class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[SpeechRecognitionResult]

class RecognitionMetadata(typing_extensions.TypedDict, total=False):
    obfuscatedId: str
    recordingDeviceType: typing_extensions.Literal[
        "RECORDING_DEVICE_TYPE_UNSPECIFIED",
        "SMARTPHONE",
        "PC",
        "PHONE_LINE",
        "VEHICLE",
        "OTHER_OUTDOOR_DEVICE",
        "OTHER_INDOOR_DEVICE",
    ]
    industryNaicsCodeOfAudio: int
    originalMediaType: typing_extensions.Literal[
        "ORIGINAL_MEDIA_TYPE_UNSPECIFIED", "AUDIO", "VIDEO"
    ]
    audioTopic: str
    originalMimeType: str
    recordingDeviceName: str
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

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    name: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str
