import typing

import typing_extensions

class LicenseAssignment(typing_extensions.TypedDict, total=False):
    productId: str
    kind: str
    productName: str
    skuId: str
    userId: str
    etags: str
    skuName: str
    selfLink: str

class LicenseAssignmentList(typing_extensions.TypedDict, total=False):
    items: typing.List[LicenseAssignment]
    nextPageToken: str
    kind: str
    etag: str

class LicenseAssignmentInsert(typing_extensions.TypedDict, total=False):
    userId: str
