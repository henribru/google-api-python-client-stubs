import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class LicenseAssignment(typing.TypedDict, total=False):
    etags: str
    kind: str
    productId: str
    productName: str
    selfLink: str
    skuId: str
    skuName: str
    userId: str

@typing.type_check_only
class LicenseAssignmentInsert(typing.TypedDict, total=False):
    userId: str

@typing.type_check_only
class LicenseAssignmentList(typing.TypedDict, total=False):
    etag: str
    items: _list[LicenseAssignment]
    kind: str
    nextPageToken: str
