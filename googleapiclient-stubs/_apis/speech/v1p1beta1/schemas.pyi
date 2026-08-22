import typing

_list = list

@typing.type_check_only
class ABNFGrammar(typing.TypedDict, total=False):
    abnfStrings: _list[str]

@typing.type_check_only
class ClassItem(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class CreateCustomClassRequest(typing.TypedDict, total=False):
    customClass: CustomClass
    customClassId: str

@typing.type_check_only
class CreatePhraseSetRequest(typing.TypedDict, total=False):
    phraseSet: PhraseSet
    phraseSetId: str

@typing.type_check_only
class CustomClass(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    customClassId: str
    deleteTime: str
    displayName: str
    etag: str
    expireTime: str
    items: _list[ClassItem]
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    reconciling: bool
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    uid: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Entry(typing.TypedDict, total=False):
    caseSensitive: bool
    replace: str
    search: str

@typing.type_check_only
class ListCustomClassesResponse(typing.TypedDict, total=False):
    customClasses: _list[CustomClass]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPhraseSetResponse(typing.TypedDict, total=False):
    nextPageToken: str
    phraseSets: _list[PhraseSet]

@typing.type_check_only
class LongRunningRecognizeMetadata(typing.TypedDict, total=False):
    lastUpdateTime: str
    outputConfig: TranscriptOutputConfig
    progressPercent: int
    startTime: str
    uri: str

@typing.type_check_only
class LongRunningRecognizeRequest(typing.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig
    outputConfig: TranscriptOutputConfig

@typing.type_check_only
class LongRunningRecognizeResponse(typing.TypedDict, total=False):
    outputConfig: TranscriptOutputConfig
    outputError: Status
    requestId: str
    results: _list[SpeechRecognitionResult]
    speechAdaptationInfo: SpeechAdaptationInfo
    totalBilledTime: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Phrase(typing.TypedDict, total=False):
    boost: float
    value: str

@typing.type_check_only
class PhraseSet(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    boost: float
    deleteTime: str
    displayName: str
    etag: str
    expireTime: str
    kmsKeyName: str
    kmsKeyVersionName: str
    name: str
    phrases: _list[Phrase]
    reconciling: bool
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETED"]
    uid: str

@typing.type_check_only
class RecognitionAudio(typing.TypedDict, total=False):
    content: str
    uri: str

@typing.type_check_only
class RecognitionConfig(typing.TypedDict, total=False):
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
    encoding: typing.Literal[
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
        "ALAW",
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
class RecognitionMetadata(typing.TypedDict, total=False):
    audioTopic: str
    industryNaicsCodeOfAudio: int
    interactionType: typing.Literal[
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
    microphoneDistance: typing.Literal[
        "MICROPHONE_DISTANCE_UNSPECIFIED", "NEARFIELD", "MIDFIELD", "FARFIELD"
    ]
    obfuscatedId: str
    originalMediaType: typing.Literal[
        "ORIGINAL_MEDIA_TYPE_UNSPECIFIED", "AUDIO", "VIDEO"
    ]
    originalMimeType: str
    recordingDeviceName: str
    recordingDeviceType: typing.Literal[
        "RECORDING_DEVICE_TYPE_UNSPECIFIED",
        "SMARTPHONE",
        "PC",
        "PHONE_LINE",
        "VEHICLE",
        "OTHER_OUTDOOR_DEVICE",
        "OTHER_INDOOR_DEVICE",
    ]

@typing.type_check_only
class RecognizeRequest(typing.TypedDict, total=False):
    audio: RecognitionAudio
    config: RecognitionConfig

@typing.type_check_only
class RecognizeResponse(typing.TypedDict, total=False):
    requestId: str
    results: _list[SpeechRecognitionResult]
    speechAdaptationInfo: SpeechAdaptationInfo
    totalBilledTime: str
    usingLegacyModels: bool

@typing.type_check_only
class SpeakerDiarizationConfig(typing.TypedDict, total=False):
    enableSpeakerDiarization: bool
    maxSpeakerCount: int
    minSpeakerCount: int
    speakerTag: int

@typing.type_check_only
class SpeechAdaptation(typing.TypedDict, total=False):
    abnfGrammar: ABNFGrammar
    customClasses: _list[CustomClass]
    phraseSetReferences: _list[str]
    phraseSets: _list[PhraseSet]

@typing.type_check_only
class SpeechAdaptationInfo(typing.TypedDict, total=False):
    adaptationTimeout: bool
    timeoutMessage: str

@typing.type_check_only
class SpeechContext(typing.TypedDict, total=False):
    boost: float
    phrases: _list[str]

@typing.type_check_only
class SpeechRecognitionAlternative(typing.TypedDict, total=False):
    confidence: float
    transcript: str
    words: _list[WordInfo]

@typing.type_check_only
class SpeechRecognitionResult(typing.TypedDict, total=False):
    alternatives: _list[SpeechRecognitionAlternative]
    channelTag: int
    languageCode: str
    resultEndTime: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TranscriptNormalization(typing.TypedDict, total=False):
    entries: _list[Entry]

@typing.type_check_only
class TranscriptOutputConfig(typing.TypedDict, total=False):
    gcsUri: str

@typing.type_check_only
class WordInfo(typing.TypedDict, total=False):
    confidence: float
    endTime: str
    speakerLabel: str
    speakerTag: int
    startTime: str
    word: str
