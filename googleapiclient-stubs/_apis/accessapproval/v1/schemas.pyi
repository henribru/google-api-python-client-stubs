import typing

import typing_extensions

class DismissApprovalRequestMessage(typing_extensions.TypedDict, total=False): ...

class ApprovalRequest(typing_extensions.TypedDict, total=False):
    requestedReason: AccessReason
    requestedExpiration: str
    approve: ApproveDecision
    requestedResourceName: str
    name: str
    requestedResourceProperties: ResourceProperties
    dismiss: DismissDecision
    requestTime: str
    requestedLocations: AccessLocations

class EnrolledService(typing_extensions.TypedDict, total=False):
    enrollmentLevel: typing_extensions.Literal[
        "ENROLLMENT_LEVEL_UNSPECIFIED", "BLOCK_ALL"
    ]
    cloudProduct: str

class ResourceProperties(typing_extensions.TypedDict, total=False):
    excludesDescendants: bool

class ListApprovalRequestsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    approvalRequests: typing.List[ApprovalRequest]

class DismissDecision(typing_extensions.TypedDict, total=False):
    dismissTime: str
    implicit: bool

class ApproveApprovalRequestMessage(typing_extensions.TypedDict, total=False):
    expireTime: str

class ApproveDecision(typing_extensions.TypedDict, total=False):
    approveTime: str
    expireTime: str

class AccessLocations(typing_extensions.TypedDict, total=False):
    principalPhysicalLocationCountry: str
    principalOfficeCountry: str

class AccessReason(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CUSTOMER_INITIATED_SUPPORT",
        "GOOGLE_INITIATED_SERVICE",
        "GOOGLE_INITIATED_REVIEW",
    ]
    detail: str

class AccessApprovalSettings(typing_extensions.TypedDict, total=False):
    name: str
    enrolledAncestor: bool
    enrolledServices: typing.List[EnrolledService]
    notificationEmails: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...
