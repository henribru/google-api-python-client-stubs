import typing

import typing_extensions

@typing.type_check_only
class AddFirebaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    name: str
    reconciling: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListBucketsResponse(typing_extensions.TypedDict, total=False):
    buckets: typing.List[Bucket]
    nextPageToken: str

@typing.type_check_only
class RemoveFirebaseRequest(typing_extensions.TypedDict, total=False): ...
