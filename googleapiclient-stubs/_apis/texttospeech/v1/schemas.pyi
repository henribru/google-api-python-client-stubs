import typing

import typing_extensions

class Voice(typing_extensions.TypedDict, total=False):
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
    languageCodes: typing.List[str]
    naturalSampleRateHertz: int

class VoiceSelectionParams(typing_extensions.TypedDict, total=False):
    languageCode: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
    name: str

class SynthesizeSpeechResponse(typing_extensions.TypedDict, total=False):
    audioContent: str

class AudioConfig(typing_extensions.TypedDict, total=False):
    effectsProfileId: typing.List[str]
    pitch: float
    speakingRate: float
    sampleRateHertz: int
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MP3", "OGG_OPUS"
    ]
    volumeGainDb: float

class SynthesizeSpeechRequest(typing_extensions.TypedDict, total=False):
    voice: VoiceSelectionParams
    input: SynthesisInput
    audioConfig: AudioConfig

class ListVoicesResponse(typing_extensions.TypedDict, total=False):
    voices: typing.List[Voice]

class SynthesisInput(typing_extensions.TypedDict, total=False):
    text: str
    ssml: str
