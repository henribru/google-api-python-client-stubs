import typing

import typing_extensions
@typing.type_check_only
class AccessApprovalSettings(typing_extensions.TypedDict, total=False):
    enrolledAncestor: bool
    enrolledServices: typing.List[EnrolledService]
    name: str
    notificationEmails: typing.List[str]

@typing.type_check_only
class AccessLocations(typing_extensions.TypedDict, total=False):
    principalOfficeCountry: str
    principalPhysicalLocationCountry: str

@typing.type_check_only
class AccessReason(typing_extensions.TypedDict, total=False):
    detail: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CUSTOMER_INITIATED_SUPPORT",
        "GOOGLE_INITIATED_SERVICE",
        "GOOGLE_INITIATED_REVIEW",
    ]

@typing.type_check_only
class ApprovalRequest(typing_extensions.TypedDict, total=False):
    approve: ApproveDecision
    dismiss: DismissDecision
    name: str
    requestTime: str
    requestedExpiration: str
    requestedLocations: AccessLocations
    requestedReason: AccessReason
    requestedResourceName: str
    requestedResourceProperties: ResourceProperties

@typing.type_check_only
class ApproveApprovalRequestMessage(typing_extensions.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class ApproveDecision(typing_extensions.TypedDict, total=False):
    approveTime: str
    expireTime: str

@typing.type_check_only
class DismissApprovalRequestMessage(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DismissDecision(typing_extensions.TypedDict, total=False):
    dismissTime: str
    implicit: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrolledService(typing_extensions.TypedDict, total=False):
    cloudProduct: str
    enrollmentLevel: typing_extensions.Literal[
        "ENROLLMENT_LEVEL_UNSPECIFIED", "BLOCK_ALL"
    ]

@typing.type_check_only
class ListApprovalRequestsResponse(typing_extensions.TypedDict, total=False):
    approvalRequests: typing.List[ApprovalRequest]
    nextPageToken: str

@typing.type_check_only
class ResourceProperties(typing_extensions.TypedDict, total=False):
    excludesDescendants: bool
