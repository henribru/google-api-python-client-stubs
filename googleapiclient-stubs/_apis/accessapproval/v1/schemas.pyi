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
    notificationPubsubTopic: str
    preferNoBroadApprovalRequests: bool
    preferredRequestExpirationDays: int
    requestScopeMaxWidthPreference: typing_extensions.Literal[
        "REQUEST_SCOPE_MAX_WIDTH_PREFERENCE_UNSPECIFIED",
        "ORGANIZATION",
        "FOLDER",
        "PROJECT",
    ]
    requireCustomerVisibleJustification: bool

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
        "CLOUD_INITIATED_ACCESS",
    ]

@typing.type_check_only
class ApprovalRequest(typing_extensions.TypedDict, total=False):
    approve: ApproveDecision
    dismiss: DismissDecision
    name: str
    requestTime: str
    requestedAugmentedInfo: AugmentedInfo
    requestedDuration: str
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
class AugmentedInfo(typing_extensions.TypedDict, total=False):
    command: str

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
    googleKeyAlgorithm: typing_extensions.Literal[
        "CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED",
        "GOOGLE_SYMMETRIC_ENCRYPTION",
        "AES_128_GCM",
        "AES_256_GCM",
        "AES_128_CBC",
        "AES_256_CBC",
        "AES_128_CTR",
        "AES_256_CTR",
        "RSA_SIGN_PSS_2048_SHA256",
        "RSA_SIGN_PSS_3072_SHA256",
        "RSA_SIGN_PSS_4096_SHA256",
        "RSA_SIGN_PSS_4096_SHA512",
        "RSA_SIGN_PKCS1_2048_SHA256",
        "RSA_SIGN_PKCS1_3072_SHA256",
        "RSA_SIGN_PKCS1_4096_SHA256",
        "RSA_SIGN_PKCS1_4096_SHA512",
        "RSA_SIGN_RAW_PKCS1_2048",
        "RSA_SIGN_RAW_PKCS1_3072",
        "RSA_SIGN_RAW_PKCS1_4096",
        "RSA_DECRYPT_OAEP_2048_SHA256",
        "RSA_DECRYPT_OAEP_3072_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA512",
        "RSA_DECRYPT_OAEP_2048_SHA1",
        "RSA_DECRYPT_OAEP_3072_SHA1",
        "RSA_DECRYPT_OAEP_4096_SHA1",
        "EC_SIGN_P256_SHA256",
        "EC_SIGN_P384_SHA384",
        "EC_SIGN_SECP256K1_SHA256",
        "EC_SIGN_ED25519",
        "HMAC_SHA256",
        "HMAC_SHA1",
        "HMAC_SHA384",
        "HMAC_SHA512",
        "HMAC_SHA224",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    googlePublicKeyPem: str
    serializedApprovalRequest: str
    signature: str
