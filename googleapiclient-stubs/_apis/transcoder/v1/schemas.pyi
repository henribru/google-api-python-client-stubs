import typing

_list = list

@typing.type_check_only
class AdBreak(typing.TypedDict, total=False):
    startTimeOffset: str

@typing.type_check_only
class Aes128Encryption(typing.TypedDict, total=False): ...

@typing.type_check_only
class Animation(typing.TypedDict, total=False):
    animationEnd: AnimationEnd
    animationFade: AnimationFade
    animationStatic: AnimationStatic

@typing.type_check_only
class AnimationEnd(typing.TypedDict, total=False):
    startTimeOffset: str

@typing.type_check_only
class AnimationFade(typing.TypedDict, total=False):
    endTimeOffset: str
    fadeType: typing.Literal["FADE_TYPE_UNSPECIFIED", "FADE_IN", "FADE_OUT"]
    startTimeOffset: str
    xy: NormalizedCoordinate

@typing.type_check_only
class AnimationStatic(typing.TypedDict, total=False):
    startTimeOffset: str
    xy: NormalizedCoordinate

@typing.type_check_only
class Audio(typing.TypedDict, total=False):
    highBoost: bool
    lowBoost: bool
    lufs: float

@typing.type_check_only
class AudioMapping(typing.TypedDict, total=False):
    atomKey: str
    gainDb: float
    inputChannel: int
    inputKey: str
    inputTrack: int
    outputChannel: int

@typing.type_check_only
class AudioStream(typing.TypedDict, total=False):
    bitrateBps: int
    channelCount: int
    channelLayout: _list[str]
    codec: str
    displayName: str
    languageCode: str
    mapping: _list[AudioMapping]
    sampleRateHertz: int

@typing.type_check_only
class BwdifConfig(typing.TypedDict, total=False):
    deinterlaceAllFrames: bool
    mode: str
    parity: str

@typing.type_check_only
class Clearkey(typing.TypedDict, total=False): ...

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    brightness: float
    contrast: float
    saturation: float

@typing.type_check_only
class Crop(typing.TypedDict, total=False):
    bottomPixels: int
    leftPixels: int
    rightPixels: int
    topPixels: int

@typing.type_check_only
class DashConfig(typing.TypedDict, total=False):
    segmentReferenceScheme: typing.Literal[
        "SEGMENT_REFERENCE_SCHEME_UNSPECIFIED",
        "SEGMENT_LIST",
        "SEGMENT_TEMPLATE_NUMBER",
    ]

@typing.type_check_only
class Deblock(typing.TypedDict, total=False):
    enabled: bool
    strength: float

@typing.type_check_only
class Deinterlace(typing.TypedDict, total=False):
    bwdif: BwdifConfig
    yadif: YadifConfig

@typing.type_check_only
class Denoise(typing.TypedDict, total=False):
    strength: float
    tune: str

@typing.type_check_only
class DrmSystems(typing.TypedDict, total=False):
    clearkey: Clearkey
    fairplay: Fairplay
    playready: Playready
    widevine: Widevine

@typing.type_check_only
class EditAtom(typing.TypedDict, total=False):
    endTimeOffset: str
    inputs: _list[str]
    key: str
    startTimeOffset: str

@typing.type_check_only
class ElementaryStream(typing.TypedDict, total=False):
    audioStream: AudioStream
    key: str
    textStream: TextStream
    videoStream: VideoStream

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Encryption(typing.TypedDict, total=False):
    aes128: Aes128Encryption
    drmSystems: DrmSystems
    id: str
    mpegCenc: MpegCommonEncryption
    sampleAes: SampleAesEncryption
    secretManagerKeySource: SecretManagerSource

@typing.type_check_only
class Fairplay(typing.TypedDict, total=False): ...

@typing.type_check_only
class Fmp4Config(typing.TypedDict, total=False):
    codecTag: str

@typing.type_check_only
class H264CodecSettings(typing.TypedDict, total=False):
    allowOpenGop: bool
    aqStrength: float
    bFrameCount: int
    bPyramid: bool
    bitrateBps: int
    crfLevel: int
    enableTwoPass: bool
    entropyCoder: str
    frameRate: float
    frameRateConversionStrategy: typing.Literal[
        "FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED", "DOWNSAMPLE", "DROP_DUPLICATE"
    ]
    gopDuration: str
    gopFrameCount: int
    heightPixels: int
    hlg: H264ColorFormatHLG
    pixelFormat: str
    preset: str
    profile: str
    rateControlMode: str
    sdr: H264ColorFormatSDR
    tune: str
    vbvFullnessBits: int
    vbvSizeBits: int
    widthPixels: int

@typing.type_check_only
class H264ColorFormatHLG(typing.TypedDict, total=False): ...

@typing.type_check_only
class H264ColorFormatSDR(typing.TypedDict, total=False): ...

@typing.type_check_only
class H265CodecSettings(typing.TypedDict, total=False):
    allowOpenGop: bool
    aqStrength: float
    bFrameCount: int
    bPyramid: bool
    bitrateBps: int
    crfLevel: int
    enableTwoPass: bool
    frameRate: float
    frameRateConversionStrategy: typing.Literal[
        "FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED", "DOWNSAMPLE", "DROP_DUPLICATE"
    ]
    gopDuration: str
    gopFrameCount: int
    hdr10: H265ColorFormatHDR10
    heightPixels: int
    hlg: H265ColorFormatHLG
    pixelFormat: str
    preset: str
    profile: str
    rateControlMode: str
    sdr: H265ColorFormatSDR
    tune: str
    vbvFullnessBits: int
    vbvSizeBits: int
    widthPixels: int

@typing.type_check_only
class H265ColorFormatHDR10(typing.TypedDict, total=False): ...

@typing.type_check_only
class H265ColorFormatHLG(typing.TypedDict, total=False): ...

@typing.type_check_only
class H265ColorFormatSDR(typing.TypedDict, total=False): ...

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    alpha: float
    resolution: NormalizedCoordinate
    uri: str

@typing.type_check_only
class Input(typing.TypedDict, total=False):
    attributes: InputAttributes
    key: str
    preprocessingConfig: PreprocessingConfig
    uri: str

@typing.type_check_only
class InputAttributes(typing.TypedDict, total=False):
    trackDefinitions: _list[TrackDefinition]

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    batchModePriority: int
    config: JobConfig
    createTime: str
    endTime: str
    error: Status
    fillContentGaps: bool
    inputUri: str
    labels: dict[str, typing.Any]
    mode: typing.Literal[
        "PROCESSING_MODE_UNSPECIFIED",
        "PROCESSING_MODE_INTERACTIVE",
        "PROCESSING_MODE_BATCH",
    ]
    name: str
    optimization: typing.Literal[
        "OPTIMIZATION_STRATEGY_UNSPECIFIED", "AUTODETECT", "DISABLED"
    ]
    outputUri: str
    startTime: str
    state: typing.Literal[
        "PROCESSING_STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]
    templateId: str
    ttlAfterCompletionDays: int

@typing.type_check_only
class JobConfig(typing.TypedDict, total=False):
    adBreaks: _list[AdBreak]
    editList: _list[EditAtom]
    elementaryStreams: _list[ElementaryStream]
    encryptions: _list[Encryption]
    inputs: _list[Input]
    manifests: _list[Manifest]
    muxStreams: _list[MuxStream]
    output: Output
    overlays: _list[Overlay]
    pubsubDestination: PubsubDestination
    spriteSheets: _list[SpriteSheet]

@typing.type_check_only
class JobTemplate(typing.TypedDict, total=False):
    config: JobConfig
    labels: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ListJobTemplatesResponse(typing.TypedDict, total=False):
    jobTemplates: _list[JobTemplate]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class Manifest(typing.TypedDict, total=False):
    dash: DashConfig
    fileName: str
    muxStreams: _list[str]
    type: typing.Literal["MANIFEST_TYPE_UNSPECIFIED", "HLS", "DASH"]

@typing.type_check_only
class MpegCommonEncryption(typing.TypedDict, total=False):
    scheme: str

@typing.type_check_only
class MuxStream(typing.TypedDict, total=False):
    container: str
    elementaryStreams: _list[str]
    encryptionId: str
    fileName: str
    fmp4: Fmp4Config
    key: str
    segmentSettings: SegmentSettings

@typing.type_check_only
class NormalizedCoordinate(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class Output(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Overlay(typing.TypedDict, total=False):
    animations: _list[Animation]
    image: Image

@typing.type_check_only
class Pad(typing.TypedDict, total=False):
    bottomPixels: int
    leftPixels: int
    rightPixels: int
    topPixels: int

@typing.type_check_only
class Playready(typing.TypedDict, total=False): ...

@typing.type_check_only
class PreprocessingConfig(typing.TypedDict, total=False):
    audio: Audio
    color: Color
    crop: Crop
    deblock: Deblock
    deinterlace: Deinterlace
    denoise: Denoise
    pad: Pad

@typing.type_check_only
class PubsubDestination(typing.TypedDict, total=False):
    topic: str

@typing.type_check_only
class SampleAesEncryption(typing.TypedDict, total=False): ...

@typing.type_check_only
class SecretManagerSource(typing.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class SegmentSettings(typing.TypedDict, total=False):
    individualSegments: bool
    segmentDuration: str

@typing.type_check_only
class SpriteSheet(typing.TypedDict, total=False):
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
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TextMapping(typing.TypedDict, total=False):
    atomKey: str
    inputKey: str
    inputTrack: int

@typing.type_check_only
class TextStream(typing.TypedDict, total=False):
    codec: str
    displayName: str
    languageCode: str
    mapping: _list[TextMapping]

@typing.type_check_only
class TrackDefinition(typing.TypedDict, total=False):
    detectLanguages: bool
    detectedLanguages: _list[str]
    inputTrack: int
    languages: _list[str]

@typing.type_check_only
class VideoStream(typing.TypedDict, total=False):
    h264: H264CodecSettings
    h265: H265CodecSettings
    vp9: Vp9CodecSettings

@typing.type_check_only
class Vp9CodecSettings(typing.TypedDict, total=False):
    bitrateBps: int
    crfLevel: int
    frameRate: float
    frameRateConversionStrategy: typing.Literal[
        "FRAME_RATE_CONVERSION_STRATEGY_UNSPECIFIED", "DOWNSAMPLE", "DROP_DUPLICATE"
    ]
    gopDuration: str
    gopFrameCount: int
    heightPixels: int
    hlg: Vp9ColorFormatHLG
    pixelFormat: str
    profile: str
    rateControlMode: str
    sdr: Vp9ColorFormatSDR
    widthPixels: int

@typing.type_check_only
class Vp9ColorFormatHLG(typing.TypedDict, total=False): ...

@typing.type_check_only
class Vp9ColorFormatSDR(typing.TypedDict, total=False): ...

@typing.type_check_only
class Widevine(typing.TypedDict, total=False): ...

@typing.type_check_only
class YadifConfig(typing.TypedDict, total=False):
    deinterlaceAllFrames: bool
    disableSpatialInterlacing: bool
    mode: str
    parity: str
