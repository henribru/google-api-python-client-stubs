import typing

import typing_extensions

_list = list

@typing.type_check_only
class Item(typing_extensions.TypedDict, total=False):
    crxVersion: str
    id: str
    itemError: _list[ItemError]
    kind: str
    publicKey: str
    uploadState: str

@typing.type_check_only
class Item2(typing_extensions.TypedDict, total=False):
    item_id: str
    kind: str
    status: _list[str]
    statusDetail: _list[str]

@typing.type_check_only
class ItemError(typing_extensions.TypedDict, total=False):
    error_code: str
    error_detail: str

@typing.type_check_only
class PublishRequest(typing_extensions.TypedDict, total=False):
    deployPercentage: int
    reviewExemption: bool
    target: str
