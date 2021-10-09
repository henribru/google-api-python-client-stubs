import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LicenseAssignment(typing_extensions.TypedDict, total=False):
    etags: str
    kind: str
    productId: str
    productName: str
    selfLink: str
    skuId: str
    skuName: str
    userId: str

@typing.type_check_only
class LicenseAssignmentInsert(typing_extensions.TypedDict, total=False):
    userId: str

@typing.type_check_only
class LicenseAssignmentList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[LicenseAssignment]
    kind: str
    nextPageToken: str
