import typing

import typing_extensions

_list = list

@typing.type_check_only
class ClassItem(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class CreateCustomClassRequest(typing_extensions.TypedDict, total=False):
    customClass: CustomClass
    customClassId: str

@typing.type_check_only
class CreatePhraseSetRequest(typing_extensions.TypedDict, total=False):
    phraseSet: PhraseSet
    phraseSetId: str

@typing.type_check_only
class CustomClass(typing_extensions.TypedDict, total=False):
    customClassId: str
    items: _list[ClassItem]
    name: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entry(typing_extensions.TypedDict, total=False):
    caseSensitive: bool
    replace: str
    search: str

@typing.type_check_only
class ListCustomClassesResponse(typing_extensions.TypedDict, total=False):
    customClasses: _list[CustomClass]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPhraseSetResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    phraseSets: _list[PhraseSet]

@typing.type_check_only
class LongRunningRecognizeMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    outputConfig: TranscriptOutputConfig
    progressPercent: int
    startTime: str
    uri: str

@typing.type_check_only
class LongRunningRecognizeRequest(typing_extensions.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig
    outputConfig: TranscriptOutputConfig

@typing.type_check_only
class LongRunningRecognizeResponse(typing_extensions.TypedDict, total=False):
    outputConfig: TranscriptOutputConfig
    outputError: Status
    requestId: str
    results: _list[SpeechRecognitionResult]
    totalBilledTime: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Phrase(typing_extensions.TypedDict, total=False):
    boost: float
    value: str

@typing.type_check_only
class PhraseSet(typing_extensions.TypedDict, total=False):
    boost: float
    name: str
    phrases: _list[Phrase]

@typing.type_check_only
class RecognitionAudio(typing_extensions.TypedDict, total=False):
    content: str
    uri: str

@typing.type_check_only
class RecognitionConfig(typing_extensions.TypedDict, total=False):
    adaptation: SpeechAdaptation
    alternativeLanguageCodes: _list[str]
    audioChannelCount: int
    diarizationConfig: SpeakerDiarizationConfig
    diarizationSpeakerCount: int
    enableAutomaticPunctuation: bool
    enableSeparateRecognitionPerChannel: bool
    enableSpeakerDiarization: bool
    enableSpokenEmojis: bool
    enableSpokenPunctuation: bool
    enableWordConfidence: bool
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
        "MP3",
        "WEBM_OPUS",
    ]
    languageCode: str
    maxAlternatives: int
    metadata: RecognitionMetadata
    model: str
    profanityFilter: bool
    sampleRateHertz: int
    speechContexts: _list[SpeechContext]
    transcriptNormalization: TranscriptNormalization
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
    obfuscatedId: str
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
    requestId: str
    results: _list[SpeechRecognitionResult]
    totalBilledTime: str

@typing.type_check_only
class SpeakerDiarizationConfig(typing_extensions.TypedDict, total=False):
    enableSpeakerDiarization: bool
    maxSpeakerCount: int
    minSpeakerCount: int
    speakerTag: int

@typing.type_check_only
class SpeechAdaptation(typing_extensions.TypedDict, total=False):
    customClasses: _list[CustomClass]
    phraseSetReferences: _list[str]
    phraseSets: _list[PhraseSet]

@typing.type_check_only
class SpeechContext(typing_extensions.TypedDict, total=False):
    boost: float
    phrases: _list[str]

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
    resultEndTime: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TranscriptNormalization(typing_extensions.TypedDict, total=False):
    entries: _list[Entry]

@typing.type_check_only
class TranscriptOutputConfig(typing_extensions.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class WordInfo(typing_extensions.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerTag: int
    startTime: str
    word: str
