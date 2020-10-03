import typing

import typing_extensions

class SynthesisInput(typing_extensions.TypedDict, total=False):
    ssml: str
    text: str

class VoiceSelectionParams(typing_extensions.TypedDict, total=False):
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
    name: str
    languageCode: str

class Voice(typing_extensions.TypedDict, total=False):
    languageCodes: typing.List[str]
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
    name: str
    naturalSampleRateHertz: int

class AudioConfig(typing_extensions.TypedDict, total=False):
    sampleRateHertz: int
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED",
        "LINEAR16",
        "MP3",
        "MP3_64_KBPS",
        "OGG_OPUS",
        "MULAW",
    ]
    volumeGainDb: float
    effectsProfileId: typing.List[str]
    pitch: float
    speakingRate: float

class Timepoint(typing_extensions.TypedDict, total=False):
    markName: str
    timeSeconds: float

class SynthesizeSpeechRequest(typing_extensions.TypedDict, total=False):
    input: SynthesisInput
    enableTimePointing: typing.List[str]
    voice: VoiceSelectionParams
    audioConfig: AudioConfig

class ListVoicesResponse(typing_extensions.TypedDict, total=False):
    voices: typing.List[Voice]

class SynthesizeSpeechResponse(typing_extensions.TypedDict, total=False):
    audioConfig: AudioConfig
    timepoints: typing.List[Timepoint]
    audioContent: str
