import typing

_list = list

@typing.type_check_only
class AccessApprovalServiceAccount(typing.TypedDict, total=False):
    accountEmail: str
    name: str

@typing.type_check_only
class AccessApprovalSettings(typing.TypedDict, total=False):
    activeKeyVersion: str
    ancestorHasActiveKeyVersion: bool
    ancestorsEnrolledServices: _list[EnrolledService]
    approvalPolicy: CustomerApprovalApprovalPolicy
    effectiveApprovalPolicy: CustomerApprovalApprovalPolicy
    enrolledAncestor: bool
    enrolledServices: _list[EnrolledService]
    invalidKeyVersion: bool
    name: str
    notificationEmails: _list[str]
    notificationPubsubTopic: str
    preferNoBroadApprovalRequests: bool
    preferredRequestExpirationDays: int
    requestScopeMaxWidthPreference: typing.Literal[
        "REQUEST_SCOPE_MAX_WIDTH_PREFERENCE_UNSPECIFIED",
        "ORGANIZATION",
        "FOLDER",
        "PROJECT",
    ]
    requireCustomerVisibleJustification: bool

@typing.type_check_only
class AccessLocations(typing.TypedDict, total=False):
    principalOfficeCountry: str
    principalPhysicalLocationCountry: str

@typing.type_check_only
class AccessReason(typing.TypedDict, total=False):
    detail: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "CUSTOMER_INITIATED_SUPPORT",
        "GOOGLE_INITIATED_SERVICE",
        "GOOGLE_INITIATED_REVIEW",
        "THIRD_PARTY_DATA_REQUEST",
        "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
        "CLOUD_INITIATED_ACCESS",
    ]

@typing.type_check_only
class ApprovalRequest(typing.TypedDict, total=False):
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
class ApproveApprovalRequestMessage(typing.TypedDict, total=False):
    expireTime: str

@typing.type_check_only
class ApproveDecision(typing.TypedDict, total=False):
    approveTime: str
    autoApproved: bool
    expireTime: str
    invalidateTime: str
    policyApproved: bool
    signatureInfo: SignatureInfo

@typing.type_check_only
class AugmentedInfo(typing.TypedDict, total=False):
    command: str

@typing.type_check_only
class CustomerApprovalApprovalPolicy(typing.TypedDict, total=False):
    justificationBasedApprovalPolicy: typing.Literal[
        "JUSTIFICATION_BASED_APPROVAL_POLICY_UNSPECIFIED",
        "JUSTIFICATION_BASED_APPROVAL_ENABLED_ALL",
        "JUSTIFICATION_BASED_APPROVAL_ENABLED_EXTERNAL_JUSTIFICATIONS",
        "JUSTIFICATION_BASED_APPROVAL_NOT_ENABLED",
        "JUSTIFICATION_BASED_APPROVAL_INHERITED",
    ]

@typing.type_check_only
class DismissApprovalRequestMessage(typing.TypedDict, total=False): ...

@typing.type_check_only
class DismissDecision(typing.TypedDict, total=False):
    dismissTime: str
    implicit: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnrolledService(typing.TypedDict, total=False):
    cloudProduct: str
    enrollmentLevel: typing.Literal["ENROLLMENT_LEVEL_UNSPECIFIED", "BLOCK_ALL"]

@typing.type_check_only
class InvalidateApprovalRequestMessage(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListApprovalRequestsResponse(typing.TypedDict, total=False):
    approvalRequests: _list[ApprovalRequest]
    nextPageToken: str

@typing.type_check_only
class ResourceProperties(typing.TypedDict, total=False):
    excludesDescendants: bool

@typing.type_check_only
class SignatureInfo(typing.TypedDict, total=False):
    customerKmsKeyVersion: str
    googleKeyAlgorithm: typing.Literal[
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
        "ML_KEM_768",
        "ML_KEM_1024",
        "KEM_XWING",
        "PQ_SIGN_ML_DSA_44",
        "PQ_SIGN_ML_DSA_65",
        "PQ_SIGN_ML_DSA_87",
        "PQ_SIGN_SLH_DSA_SHA2_128S",
        "PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256",
        "PQ_SIGN_ML_DSA_44_EXTERNAL_MU",
        "PQ_SIGN_ML_DSA_65_EXTERNAL_MU",
        "PQ_SIGN_ML_DSA_87_EXTERNAL_MU",
        "KEM_ECDH_P256",
        "KEM_ECDH_P384",
        "AES_256_KWP",
    ]
    googlePublicKeyPem: str
    serializedApprovalRequest: str
    signature: str
