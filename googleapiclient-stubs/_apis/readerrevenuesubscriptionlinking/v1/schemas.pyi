import typing

import typing_extensions

_list = list

@typing.type_check_only
class DeleteReaderResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing_extensions.TypedDict, total=False):
    detail: str
    expireTime: str
    productId: str
    subscriptionToken: str

@typing.type_check_only
class Reader(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str

@typing.type_check_only
class ReaderEntitlements(typing_extensions.TypedDict, total=False):
    entitlements: _list[Entitlement]
    name: str
