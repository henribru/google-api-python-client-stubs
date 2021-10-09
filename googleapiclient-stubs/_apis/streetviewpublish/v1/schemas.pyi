import typing

import typing_extensions

_list = list

@typing.type_check_only
class BatchDeletePhotosRequest(typing_extensions.TypedDict, total=False):
    photoIds: _list[str]

@typing.type_check_only
class BatchDeletePhotosResponse(typing_extensions.TypedDict, total=False):
    status: _list[Status]

@typing.type_check_only
class BatchGetPhotosResponse(typing_extensions.TypedDict, total=False):
    results: _list[PhotoResponse]

@typing.type_check_only
class BatchUpdatePhotosRequest(typing_extensions.TypedDict, total=False):
    updatePhotoRequests: _list[UpdatePhotoRequest]

@typing.type_check_only
class BatchUpdatePhotosResponse(typing_extensions.TypedDict, total=False):
    results: _list[PhotoResponse]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    target: PhotoId

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LatLng(typing_extensions.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class Level(typing_extensions.TypedDict, total=False):
    name: str
    number: float

@typing.type_check_only
class ListPhotosResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    photos: _list[Photo]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Photo(typing_extensions.TypedDict, total=False):
    captureTime: str
    connections: _list[Connection]
    downloadUrl: str
    mapsPublishStatus: typing_extensions.Literal[
        "UNSPECIFIED_MAPS_PUBLISH_STATUS", "PUBLISHED", "REJECTED_UNKNOWN"
    ]
    photoId: PhotoId
    places: _list[Place]
    pose: Pose
    shareLink: str
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
    uploadReference: UploadRef
    uploadTime: str
    viewCount: str

@typing.type_check_only
class PhotoId(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class PhotoResponse(typing_extensions.TypedDict, total=False):
    photo: Photo
    status: Status

@typing.type_check_only
class Place(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    placeId: str

@typing.type_check_only
class Pose(typing_extensions.TypedDict, total=False):
    accuracyMeters: float
    altitude: float
    heading: float
    latLngPair: LatLng
    level: Level
    pitch: float
    roll: float

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UpdatePhotoRequest(typing_extensions.TypedDict, total=False):
    photo: Photo
    updateMask: str

@typing.type_check_only
class UploadRef(typing_extensions.TypedDict, total=False):
    uploadUrl: str
