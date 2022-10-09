import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessApprovalServiceAccount(typing_extensions.TypedDict, total=False):
    accountEmail: str
    name: str

@typing.type_check_only
class AccessApprovalSettings(typing_extensions.TypedDict, total=False):
    activeKeyVersion: str
    ancestorHasActiveKeyVersion: bool
    enrolledAncestor: bool
    enrolledServices: _list[EnrolledService]
    invalidKeyVersion: bool
    name: str
    notificationEmails: _list[str]

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
        "THIRD_PARTY_DATA_REQUEST",
        "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
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
    autoApproved: bool
    expireTime: str
    invalidateTime: str
    signatureInfo: SignatureInfo

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
class InvalidateApprovalRequestMessage(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListApprovalRequestsResponse(typing_extensions.TypedDict, total=False):
    approvalRequests: _list[ApprovalRequest]
    nextPageToken: str

@typing.type_check_only
class ResourceProperties(typing_extensions.TypedDict, total=False):
    excludesDescendants: bool

@typing.type_check_only
class SignatureInfo(typing_extensions.TypedDict, total=False):
    customerKmsKeyVersion: str
    googlePublicKeyPem: str
    signature: str
