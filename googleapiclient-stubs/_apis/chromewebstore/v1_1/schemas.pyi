import typing

_list = list

@typing.type_check_only
class Item(typing.TypedDict, total=False):
    crxVersion: str
    id: str
    itemError: _list[ItemError]
    kind: str
    publicKey: str
    uploadState: str

@typing.type_check_only
class Item2(typing.TypedDict, total=False):
    item_id: str
    kind: str
    status: _list[str]
    statusDetail: _list[str]

@typing.type_check_only
class ItemError(typing.TypedDict, total=False):
    error_code: str
    error_detail: str

@typing.type_check_only
class PublishRequest(typing.TypedDict, total=False):
    deployPercentage: int
    reviewExemption: bool
    target: str
