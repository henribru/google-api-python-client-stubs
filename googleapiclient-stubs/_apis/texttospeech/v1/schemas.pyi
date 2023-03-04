import typing

import typing_extensions

_list = list

@typing.type_check_only
class AudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MP3", "OGG_OPUS", "MULAW", "ALAW"
    ]
    effectsProfileId: _list[str]
    pitch: float
    sampleRateHertz: int
    speakingRate: float
    volumeGainDb: float

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CustomVoiceParams(typing_extensions.TypedDict, total=False):
    model: str
    reportedUsage: typing_extensions.Literal[
        "REPORTED_USAGE_UNSPECIFIED", "REALTIME", "OFFLINE"
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudTexttospeechV1SynthesizeLongAudioMetadata(
    typing_extensions.TypedDict, total=False
):
    progressPercentage: float
    startTime: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListVoicesResponse(typing_extensions.TypedDict, total=False):
    voices: _list[Voice]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SynthesisInput(typing_extensions.TypedDict, total=False):
    ssml: str
    text: str

@typing.type_check_only
class SynthesizeLongAudioMetadata(typing_extensions.TypedDict, total=False):
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
    audioConfig: AudioConfig
    input: SynthesisInput
    voice: VoiceSelectionParams

@typing.type_check_only
class SynthesizeSpeechResponse(typing_extensions.TypedDict, total=False):
    audioContent: str

@typing.type_check_only
class Voice(typing_extensions.TypedDict, total=False):
    languageCodes: _list[str]
    name: str
    naturalSampleRateHertz: int
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]

@typing.type_check_only
class VoiceSelectionParams(typing_extensions.TypedDict, total=False):
    customVoice: CustomVoiceParams
    languageCode: str
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
