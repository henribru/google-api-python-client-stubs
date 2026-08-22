import typing

_list = list

@typing.type_check_only
class AddFirebaseRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Bucket(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DefaultBucket(typing.TypedDict, total=False):
    bucket: Bucket
    location: str
    name: str
    storageClass: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListBucketsResponse(typing.TypedDict, total=False):
    buckets: _list[Bucket]
    nextPageToken: str

@typing.type_check_only
class RemoveFirebaseRequest(typing.TypedDict, total=False): ...
