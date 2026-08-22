import typing

_list = list

@typing.type_check_only
class BatchDeletePhotosRequest(typing.TypedDict, total=False):
    photoIds: _list[str]

@typing.type_check_only
class BatchDeletePhotosResponse(typing.TypedDict, total=False):
    status: _list[Status]

@typing.type_check_only
class BatchGetPhotosResponse(typing.TypedDict, total=False):
    results: _list[PhotoResponse]

@typing.type_check_only
class BatchUpdatePhotosRequest(typing.TypedDict, total=False):
    updatePhotoRequests: _list[UpdatePhotoRequest]

@typing.type_check_only
class BatchUpdatePhotosResponse(typing.TypedDict, total=False):
    results: _list[PhotoResponse]

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    target: PhotoId

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GpsDataGapFailureDetails(typing.TypedDict, total=False):
    gapDuration: str
    gapStartTime: str

@typing.type_check_only
class Imu(typing.TypedDict, total=False):
    accelMpsps: _list[Measurement3d]
    gyroRps: _list[Measurement3d]
    magUt: _list[Measurement3d]

@typing.type_check_only
class ImuDataGapFailureDetails(typing.TypedDict, total=False):
    gapDuration: str
    gapStartTime: str

@typing.type_check_only
class InsufficientGpsFailureDetails(typing.TypedDict, total=False):
    gpsPointsFound: int

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LatLngBounds(typing.TypedDict, total=False):
    northeast: LatLng
    southwest: LatLng

@typing.type_check_only
class Level(typing.TypedDict, total=False):
    name: str
    number: float

@typing.type_check_only
class ListPhotoSequencesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    photoSequences: _list[Operation]

@typing.type_check_only
class ListPhotosResponse(typing.TypedDict, total=False):
    nextPageToken: str
    photos: _list[Photo]

@typing.type_check_only
class Measurement3d(typing.TypedDict, total=False):
    captureTime: str
    x: float
    y: float
    z: float

@typing.type_check_only
class NoOverlapGpsFailureDetails(typing.TypedDict, total=False):
    gpsEndTime: str
    gpsStartTime: str
    videoEndTime: str
    videoStartTime: str

@typing.type_check_only
class NotOutdoorsFailureDetails(typing.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Photo(typing.TypedDict, total=False):
    captureTime: str
    connections: _list[Connection]
    downloadUrl: str
    mapsPublishStatus: typing.Literal[
        "UNSPECIFIED_MAPS_PUBLISH_STATUS", "PUBLISHED", "REJECTED_UNKNOWN"
    ]
    photoId: PhotoId
    places: _list[Place]
    pose: Pose
    shareLink: str
    thumbnailUrl: str
    transferStatus: typing.Literal[
        "TRANSFER_STATUS_UNKNOWN",
        "NEVER_TRANSFERRED",
        "PENDING",
        "COMPLETED",
        "REJECTED",
        "EXPIRED",
        "CANCELLED",
        "RECEIVED_VIA_TRANSFER",
    ]
    uploadReference: UploadRef
    uploadTime: str
    viewCount: str

@typing.type_check_only
class PhotoId(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class PhotoResponse(typing.TypedDict, total=False):
    photo: Photo
    status: Status

@typing.type_check_only
class PhotoSequence(typing.TypedDict, total=False):
    captureTimeOverride: str
    distanceMeters: float
    failureDetails: ProcessingFailureDetails
    failureReason: typing.Literal[
        "PROCESSING_FAILURE_REASON_UNSPECIFIED",
        "LOW_RESOLUTION",
        "DUPLICATE",
        "INSUFFICIENT_GPS",
        "NO_OVERLAP_GPS",
        "INVALID_GPS",
        "FAILED_TO_REFINE_POSITIONS",
        "TAKEDOWN",
        "CORRUPT_VIDEO",
        "INTERNAL",
        "INVALID_VIDEO_FORMAT",
        "INVALID_VIDEO_DIMENSIONS",
        "INVALID_CAPTURE_TIME",
        "GPS_DATA_GAP",
        "JUMPY_GPS",
        "INVALID_IMU",
        "INSUFFICIENT_IMU",
        "INSUFFICIENT_OVERLAP_TIME_SERIES",
        "IMU_DATA_GAP",
        "UNSUPPORTED_CAMERA",
        "NOT_OUTDOORS",
        "INSUFFICIENT_VIDEO_FRAMES",
        "INSUFFICIENT_MOVEMENT",
        "MAST_DOWN",
        "CAMERA_COVERED",
    ]
    filename: str
    gpsSource: typing.Literal["PHOTO_SEQUENCE", "CAMERA_MOTION_METADATA_TRACK"]
    id: str
    imu: Imu
    photos: _list[Photo]
    processingState: typing.Literal[
        "PROCESSING_STATE_UNSPECIFIED", "PENDING", "PROCESSING", "PROCESSED", "FAILED"
    ]
    rawGpsTimeline: _list[Pose]
    sequenceBounds: LatLngBounds
    uploadReference: UploadRef
    uploadTime: str
    viewCount: str

@typing.type_check_only
class Place(typing.TypedDict, total=False):
    languageCode: str
    name: str
    placeId: str

@typing.type_check_only
class Pose(typing.TypedDict, total=False):
    accuracyMeters: float
    altitude: float
    gpsRecordTimestampUnixEpoch: str
    heading: float
    latLngPair: LatLng
    level: Level
    pitch: float
    roll: float

@typing.type_check_only
class ProcessingFailureDetails(typing.TypedDict, total=False):
    gpsDataGapDetails: GpsDataGapFailureDetails
    imuDataGapDetails: ImuDataGapFailureDetails
    insufficientGpsDetails: InsufficientGpsFailureDetails
    noOverlapGpsDetails: NoOverlapGpsFailureDetails
    notOutdoorsDetails: NotOutdoorsFailureDetails

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UpdatePhotoRequest(typing.TypedDict, total=False):
    photo: Photo
    updateMask: str

@typing.type_check_only
class UploadRef(typing.TypedDict, total=False):
    uploadUrl: str
