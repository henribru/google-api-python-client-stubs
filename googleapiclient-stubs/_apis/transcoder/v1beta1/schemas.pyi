import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdBreak(typing_extensions.TypedDict, total=False):
    startTimeOffset: str

@typing.type_check_only
class Aes128Encryption(typing_extensions.TypedDict, total=False):
    keyUri: str

@typing.type_check_only
class Animation(typing_extensions.TypedDict, total=False):
    animationEnd: AnimationEnd
    animationFade: AnimationFade
    animationStatic: AnimationStatic

@typing.type_check_only
class AnimationEnd(typing_extensions.TypedDict, total=False):
    startTimeOffset: str

@typing.type_check_only
class AnimationFade(typing_extensions.TypedDict, total=False):
    endTimeOffset: str
    fadeType: typing_extensions.Literal["FADE_TYPE_UNSPECIFIED", "FADE_IN", "FADE_OUT"]
    startTimeOffset: str
    xy: NormalizedCoordinate

@typing.type_check_only
class AnimationStatic(typing_extensions.TypedDict, total=False):
    startTimeOffset: str
    xy: NormalizedCoordinate

@typing.type_check_only
class Audio(typing_extensions.TypedDict, total=False):
    highBoost: bool
    lowBoost: bool
    lufs: float

@typing.type_check_only
class AudioAtom(typing_extensions.TypedDict, total=False):
    channels: _list[AudioChannel]
    key: str

@typing.type_check_only
class AudioChannel(typing_extensions.TypedDict, total=False):
    inputs: _list[AudioChannelInput]

@typing.type_check_only
class AudioChannelInput(typing_extensions.TypedDict, total=False):
    channel: int
    gainDb: float
    key: str
    track: int

@typing.type_check_only
class AudioStream(typing_extensions.TypedDict, total=False):
    bitrateBps: int
    channelCount: int
    channelLayout: _list[str]
    codec: str
    mapping: _list[AudioAtom]
    sampleRateHertz: int

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    brightness: float
    contrast: float
    saturation: float

@typing.type_check_only
class Crop(typing_extensions.TypedDict, total=False):
    bottomPixels: int
    leftPixels: int
    rightPixels: int
    topPixels: int

@typing.type_check_only
class Deblock(typing_extensions.TypedDict, total=False):
    enabled: bool
    strength: float

@typing.type_check_only
class Denoise(typing_extensions.TypedDict, total=False):
    strength: float
    tune: str

@typing.type_check_only
class EditAtom(typing_extensions.TypedDict, total=False):
    endTimeOffset: str
    inputs: _list[str]
    key: str
    startTimeOffset: str

@typing.type_check_only
class ElementaryStream(typing_extensions.TypedDict, total=False):
    audioStream: AudioStream
    key: str
    textStream: TextStream
    videoStream: VideoStream

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Encryption(typing_extensions.TypedDict, total=False):
    aes128: Aes128Encryption
    iv: str
    key: str
    mpegCenc: MpegCommonEncryption
    sampleAes: SampleAesEncryption

@typing.type_check_only
class FailureDetail(typing_extensions.TypedDict, total=False):
    description: str

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    alpha: float
    resolution: NormalizedCoordinate
    uri: str

@typing.type_check_only
class Input(typing_extensions.TypedDict, total=False):
    key: str
    preprocessingConfig: PreprocessingConfig
    uri: str

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    config: JobConfig
    createTime: str
    endTime: str
    failureDetails: _list[FailureDetail]
    failureReason: str
    inputUri: str
    name: str
    originUri: OriginUri
    outputUri: str
    priority: int
    progress: Progress
    startTime: str
    state: typing_extensions.Literal[
        "PROCESSING_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]
    templateId: str
    ttlAfterCompletionDays: int

@typing.type_check_only
class JobConfig(typing_extensions.TypedDict, total=False):
    adBreaks: _list[AdBreak]
    editList: _list[EditAtom]
    elementaryStreams: _list[ElementaryStream]
    inputs: _list[Input]
    manifests: _list[Manifest]
    muxStreams: _list[MuxStream]
    output: Output
    overlays: _list[Overlay]
    pubsubDestination: PubsubDestination
    spriteSheets: _list[SpriteSheet]

@typing.type_check_only
class JobTemplate(typing_extensions.TypedDict, total=False):
    config: JobConfig
    name: str

@typing.type_check_only
class ListJobTemplatesResponse(typing_extensions.TypedDict, total=False):
    jobTemplates: _list[JobTemplate]
    nextPageToken: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class Manifest(typing_extensions.TypedDict, total=False):
    fileName: str
    muxStreams: _list[str]
    type: typing_extensions.Literal["MANIFEST_TYPE_UNSPECIFIED", "HLS", "DASH"]

@typing.type_check_only
class MpegCommonEncryption(typing_extensions.TypedDict, total=False):
    keyId: str
    scheme: str

@typing.type_check_only
class MuxStream(typing_extensions.TypedDict, total=False):
    container: str
    elementaryStreams: _list[str]
    encryption: Encryption
    fileName: str
    key: str
    segmentSettings: SegmentSettings

@typing.type_check_only
class NormalizedCoordinate(typing_extensions.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class OriginUri(typing_extensions.TypedDict, total=False):
    dash: str
    hls: str

@typing.type_check_only
class Output(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Overlay(typing_extensions.TypedDict, total=False):
    animations: _list[Animation]
    image: Image

@typing.type_check_only
class Pad(typing_extensions.TypedDict, total=False):
    bottomPixels: int
    leftPixels: int
    rightPixels: int
    topPixels: int

@typing.type_check_only
class PreprocessingConfig(typing_extensions.TypedDict, total=False):
    audio: Audio
    color: Color
    crop: Crop
    deblock: Deblock
    denoise: Denoise
    pad: Pad

@typing.type_check_only
class Progress(typing_extensions.TypedDict, total=False):
    analyzed: float
    encoded: float
    notified: float
    uploaded: float

@typing.type_check_only
class PubsubDestination(typing_extensions.TypedDict, total=False):
    topic: str

@typing.type_check_only
class SampleAesEncryption(typing_extensions.TypedDict, total=False):
    keyUri: str

@typing.type_check_only
class SegmentSettings(typing_extensions.TypedDict, total=False):
    individualSegments: bool
    segmentDuration: str

@typing.type_check_only
class SpriteSheet(typing_extensions.TypedDict, total=False):
    columnCount: int
    endTimeOffset: str
    filePrefix: str
    format: str
    interval: str
    quality: int
    rowCount: int
    spriteHeightPixels: int
    spriteWidthPixels: int
    startTimeOffset: str
    totalCount: int

@typing.type_check_only
class TextAtom(typing_extensions.TypedDict, total=False):
    inputs: _list[TextInput]
    key: str

@typing.type_check_only
class TextInput(typing_extensions.TypedDict, total=False):
    key: str
    track: int

@typing.type_check_only
class TextStream(typing_extensions.TypedDict, total=False):
    codec: str
    languageCode: str
    mapping: _list[TextAtom]

@typing.type_check_only
class VideoStream(typing_extensions.TypedDict, total=False):
    allowOpenGop: bool
    aqStrength: float
    bFrameCount: int
    bPyramid: bool
    bitrateBps: int
    codec: str
    crfLevel: int
    enableTwoPass: bool
    entropyCoder: str
    frameRate: float
    gopDuration: str
    gopFrameCount: int
    heightPixels: int
    pixelFormat: str
    preset: str
    profile: str
    rateControlMode: str
    tune: str
    vbvFullnessBits: int
    vbvSizeBits: int
    widthPixels: int
