import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddFirebaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirebaseStorageControlplaneV1alphaMigrateLocationDestructivelyMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    lastUpdateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "CREATING_TEMP_BUCKET",
        "TRANSFERRING_TO_TEMP",
        "DELETING_SOURCE_BUCKET",
        "CREATING_DESTINATION_BUCKET",
        "TRANSFERRING_TO_DESTINATION",
        "DELETING_TEMP_BUCKET",
        "SUCCEEDED",
        "FAILED",
        "ROLLING_BACK",
        "ROLLED_BACK",
    ]

@typing.type_check_only
class GoogleFirebaseStorageControlplaneV1betaMigrateLocationDestructivelyMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    lastUpdateTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "CREATING_TEMP_BUCKET",
        "TRANSFERRING_TO_TEMP",
        "DELETING_SOURCE_BUCKET",
        "CREATING_DESTINATION_BUCKET",
        "TRANSFERRING_TO_DESTINATION",
        "DELETING_TEMP_BUCKET",
        "SUCCEEDED",
        "FAILED",
        "ROLLING_BACK",
        "ROLLED_BACK",
    ]

@typing.type_check_only
class ListBucketsResponse(typing_extensions.TypedDict, total=False):
    buckets: _list[Bucket]
    nextPageToken: str

@typing.type_check_only
class RemoveFirebaseRequest(typing_extensions.TypedDict, total=False): ...
