import typing

_list = list

@typing.type_check_only
class CreateOrUpdateTagsRequest(typing.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class CreateOrUpdateTagsResponse(typing.TypedDict, total=False):
    tags: _list[Tag]

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    booleanValue: bool
    int64Value: str
    key: str
    stringValue: str
    timeValue: str

@typing.type_check_only
class VerifyTokenRequest(typing.TypedDict, total=False):
    persona: str

@typing.type_check_only
class VerifyTokenResponse(typing.TypedDict, total=False): ...
