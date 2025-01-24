import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddFirebaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class DefaultBucket(typing_extensions.TypedDict, total=False):
    bucket: Bucket
    location: str
    name: str
    storageClass: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListBucketsResponse(typing_extensions.TypedDict, total=False):
    buckets: _list[Bucket]
    nextPageToken: str

@typing.type_check_only
class RemoveFirebaseRequest(typing_extensions.TypedDict, total=False): ...
