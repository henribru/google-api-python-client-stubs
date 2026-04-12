import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdvancedVoiceOptions(typing_extensions.TypedDict, total=False):
    enableTextnorm: bool
    lowLatencyJourneySynthesis: bool
    relaxSafetyFilters: bool
    safetySettings: SafetySettings

@typing.type_check_only
class AudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "LINEAR16",
        "MP3",
        "MP3_64_KBPS",
        "OGG_OPUS",
        "MULAW",
        "ALAW",
        "PCM",
        "M4A",
    ]
    effectsProfileId: _list[str]
    pitch: float
    sampleRateHertz: int
    speakingRate: float
    volumeGainDb: float

@typing.type_check_only
class CustomPronunciationParams(typing_extensions.TypedDict, total=False):
    phoneticEncoding: typing_extensions.Literal[
        "PHONETIC_ENCODING_UNSPECIFIED",
        "PHONETIC_ENCODING_IPA",
        "PHONETIC_ENCODING_X_SAMPA",
        "PHONETIC_ENCODING_JAPANESE_YOMIGANA",
        "PHONETIC_ENCODING_PINYIN",
    ]
    phrase: str
    pronunciation: str

@typing.type_check_only
class CustomPronunciations(typing_extensions.TypedDict, total=False):
    pronunciations: _list[CustomPronunciationParams]

@typing.type_check_only
class CustomVoiceParams(typing_extensions.TypedDict, total=False):
    model: str
    reportedUsage: typing_extensions.Literal[
        "REPORTED_USAGE_UNSPECIFIED", "REALTIME", "OFFLINE"
    ]

@typing.type_check_only
class GoogleCloudTexttospeechV1beta1SynthesizeLongAudioMetadata(
    typing_extensions.TypedDict, total=False
):
    lastUpdateTime: str
    progressPercentage: float
    startTime: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListVoicesResponse(typing_extensions.TypedDict, total=False):
    voices: _list[Voice]

@typing.type_check_only
class MultiSpeakerMarkup(typing_extensions.TypedDict, total=False):
    turns: _list[Turn]

@typing.type_check_only
class MultiSpeakerVoiceConfig(typing_extensions.TypedDict, total=False):
    speakerVoiceConfigs: _list[MultispeakerPrebuiltVoice]

@typing.type_check_only
class MultispeakerPrebuiltVoice(typing_extensions.TypedDict, total=False):
    speakerAlias: str
    speakerId: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class SafetySetting(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "HARM_CATEGORY_UNSPECIFIED",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_DANGEROUS_CONTENT",
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    ]
    threshold: typing_extensions.Literal[
        "HARM_BLOCK_THRESHOLD_UNSPECIFIED",
        "BLOCK_LOW_AND_ABOVE",
        "BLOCK_MEDIUM_AND_ABOVE",
        "BLOCK_ONLY_HIGH",
        "BLOCK_NONE",
        "OFF",
    ]

@typing.type_check_only
class SafetySettings(typing_extensions.TypedDict, total=False):
    settings: _list[SafetySetting]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SynthesisInput(typing_extensions.TypedDict, total=False):
    customPronunciations: CustomPronunciations
    markup: str
    multiSpeakerMarkup: MultiSpeakerMarkup
    prompt: str
    ssml: str
    text: str

@typing.type_check_only
class SynthesizeLongAudioMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    progressPercentage: float
    startTime: str

@typing.type_check_only
class SynthesizeLongAudioRequest(typing_extensions.TypedDict, total=False):
    audioConfig: AudioConfig
    input: SynthesisInput
    outputGcsUri: str
    voice: VoiceSelectionParams

@typing.type_check_only
class SynthesizeSpeechRequest(typing_extensions.TypedDict, total=False):
    advancedVoiceOptions: AdvancedVoiceOptions
    audioConfig: AudioConfig
    enableTimePointing: _list[
        typing_extensions.Literal["TIMEPOINT_TYPE_UNSPECIFIED", "SSML_MARK"]
    ]
    input: SynthesisInput
    voice: VoiceSelectionParams

@typing.type_check_only
class SynthesizeSpeechResponse(typing_extensions.TypedDict, total=False):
    audioConfig: AudioConfig
    audioContent: str
    timepoints: _list[Timepoint]

@typing.type_check_only
class Timepoint(typing_extensions.TypedDict, total=False):
    markName: str
    timeSeconds: float

@typing.type_check_only
class Turn(typing_extensions.TypedDict, total=False):
    speaker: str
    text: str

@typing.type_check_only
class Voice(typing_extensions.TypedDict, total=False):
    languageCodes: _list[str]
    name: str
    naturalSampleRateHertz: int
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]

@typing.type_check_only
class VoiceCloneParams(typing_extensions.TypedDict, total=False):
    voiceCloningKey: str

@typing.type_check_only
class VoiceSelectionParams(typing_extensions.TypedDict, total=False):
    customVoice: CustomVoiceParams
    languageCode: str
    modelName: str
    multiSpeakerVoiceConfig: MultiSpeakerVoiceConfig
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
    voiceClone: VoiceCloneParams
