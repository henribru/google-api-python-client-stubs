import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class PhotoId(typing_extensions.TypedDict, total=False):
    id: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class BatchDeletePhotosResponse(typing_extensions.TypedDict, total=False):
    status: typing.List[Status]

class BatchUpdatePhotosRequest(typing_extensions.TypedDict, total=False):
    updatePhotoRequests: typing.List[UpdatePhotoRequest]

class PhotoResponse(typing_extensions.TypedDict, total=False):
    status: Status
    photo: Photo

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    name: str
    response: typing.Dict[str, typing.Any]

class Photo(typing_extensions.TypedDict, total=False):
    shareLink: str
    photoId: PhotoId
    connections: typing.List[Connection]
    places: typing.List[Place]
    uploadReference: UploadRef
    thumbnailUrl: str
    transferStatus: typing_extensions.Literal[
        "TRANSFER_STATUS_UNKNOWN",
        "NEVER_TRANSFERRED",
        "PENDING",
        "COMPLETED",
        "REJECTED",
        "EXPIRED",
        "CANCELLED",
        "RECEIVED_VIA_TRANSFER",
    ]
    viewCount: str
    mapsPublishStatus: typing_extensions.Literal[
        "UNSPECIFIED_MAPS_PUBLISH_STATUS", "PUBLISHED", "REJECTED_UNKNOWN"
    ]
    captureTime: str
    pose: Pose
    downloadUrl: str

class Place(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    placeId: str

class Pose(typing_extensions.TypedDict, total=False):
    roll: float
    heading: float
    latLngPair: LatLng
    altitude: float
    pitch: float
    level: Level
    accuracyMeters: float

class BatchUpdatePhotosResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[PhotoResponse]

class BatchGetPhotosResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[PhotoResponse]

class LatLng(typing_extensions.TypedDict, total=False):
    longitude: float
    latitude: float

class ListPhotosResponse(typing_extensions.TypedDict, total=False):
    photos: typing.List[Photo]
    nextPageToken: str

class BatchDeletePhotosRequest(typing_extensions.TypedDict, total=False):
    photoIds: typing.List[str]

class Level(typing_extensions.TypedDict, total=False):
    name: str
    number: float

class Connection(typing_extensions.TypedDict, total=False):
    target: PhotoId

class UploadRef(typing_extensions.TypedDict, total=False):
    uploadUrl: str

class UpdatePhotoRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    photo: Photo
