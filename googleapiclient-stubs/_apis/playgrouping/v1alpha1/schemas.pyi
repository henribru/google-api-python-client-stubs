import typing

import typing_extensions

_list = list

@typing.type_check_only
class CreateOrUpdateTagsRequest(typing_extensions.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class CreateOrUpdateTagsResponse(typing_extensions.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class Tag(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    int64Value: str
    key: str
    stringValue: str
    timeValue: str

@typing.type_check_only
class VerifyTokenRequest(typing_extensions.TypedDict, total=False):
    persona: str

@typing.type_check_only
class VerifyTokenResponse(typing_extensions.TypedDict, total=False): ...
