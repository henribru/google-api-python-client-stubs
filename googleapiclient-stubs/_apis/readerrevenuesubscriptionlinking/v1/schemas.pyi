import typing

_list = list

@typing.type_check_only
class DeleteReaderResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Entitlement(typing.TypedDict, total=False):
    detail: str
    expireTime: str
    productId: str
    subscriptionToken: str

@typing.type_check_only
class Reader(typing.TypedDict, total=False):
    createTime: str
    name: str
    originatingPublicationId: str
    ppid: str
    publicationId: str

@typing.type_check_only
class ReaderEntitlements(typing.TypedDict, total=False):
    entitlements: _list[Entitlement]
    name: str
