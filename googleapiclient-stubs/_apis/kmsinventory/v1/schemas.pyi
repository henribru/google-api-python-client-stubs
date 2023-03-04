import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudKmsInventoryV1ListCryptoKeysResponse(
    typing_extensions.TypedDict, total=False
):
    cryptoKeys: _list[GoogleCloudKmsV1CryptoKey]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudKmsInventoryV1ProtectedResource(
    typing_extensions.TypedDict, total=False
):
    cloudProduct: str
    createTime: str
    cryptoKeyVersion: str
    cryptoKeyVersions: _list[str]
    labels: dict[str, typing.Any]
    location: str
    name: str
    project: str
    projectId: str
    resourceType: str

@typing.type_check_only
class GoogleCloudKmsInventoryV1ProtectedResourcesSummary(
    typing_extensions.TypedDict, total=False
):
    cloudProducts: dict[str, typing.Any]
    locations: dict[str, typing.Any]
    name: str
    projectCount: int
    resourceCount: str
    resourceTypes: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    protectedResources: _list[GoogleCloudKmsInventoryV1ProtectedResource]

@typing.type_check_only
class GoogleCloudKmsV1CryptoKey(typing_extensions.TypedDict, total=False):
    createTime: str
    cryptoKeyBackend: str
    destroyScheduledDuration: str
    importOnly: bool
    labels: dict[str, typing.Any]
    name: str
    nextRotationTime: str
    primary: GoogleCloudKmsV1CryptoKeyVersion
    purpose: typing_extensions.Literal[
        "CRYPTO_KEY_PURPOSE_UNSPECIFIED",
        "ENCRYPT_DECRYPT",
        "ASYMMETRIC_SIGN",
        "ASYMMETRIC_DECRYPT",
        "MAC",
    ]
    rotationPeriod: str
    versionTemplate: GoogleCloudKmsV1CryptoKeyVersionTemplate

@typing.type_check_only
class GoogleCloudKmsV1CryptoKeyVersion(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
        "CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED",
        "GOOGLE_SYMMETRIC_ENCRYPTION",
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
        "HMAC_SHA256",
        "HMAC_SHA1",
        "HMAC_SHA384",
        "HMAC_SHA512",
        "HMAC_SHA224",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    attestation: GoogleCloudKmsV1KeyOperationAttestation
    createTime: str
    destroyEventTime: str
    destroyTime: str
    externalProtectionLevelOptions: GoogleCloudKmsV1ExternalProtectionLevelOptions
    generateTime: str
    importFailureReason: str
    importJob: str
    importTime: str
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    reimportEligible: bool
    state: typing_extensions.Literal[
        "CRYPTO_KEY_VERSION_STATE_UNSPECIFIED",
        "PENDING_GENERATION",
        "ENABLED",
        "DISABLED",
        "DESTROYED",
        "DESTROY_SCHEDULED",
        "PENDING_IMPORT",
        "IMPORT_FAILED",
    ]

@typing.type_check_only
class GoogleCloudKmsV1CryptoKeyVersionTemplate(
    typing_extensions.TypedDict, total=False
):
    algorithm: typing_extensions.Literal[
        "CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED",
        "GOOGLE_SYMMETRIC_ENCRYPTION",
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
        "HMAC_SHA256",
        "HMAC_SHA1",
        "HMAC_SHA384",
        "HMAC_SHA512",
        "HMAC_SHA224",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]

@typing.type_check_only
class GoogleCloudKmsV1ExternalProtectionLevelOptions(
    typing_extensions.TypedDict, total=False
):
    ekmConnectionKeyPath: str
    externalKeyUri: str

@typing.type_check_only
class GoogleCloudKmsV1KeyOperationAttestation(typing_extensions.TypedDict, total=False):
    certChains: GoogleCloudKmsV1KeyOperationAttestationCertificateChains
    content: str
    format: typing_extensions.Literal[
        "ATTESTATION_FORMAT_UNSPECIFIED", "CAVIUM_V1_COMPRESSED", "CAVIUM_V2_COMPRESSED"
    ]

@typing.type_check_only
class GoogleCloudKmsV1KeyOperationAttestationCertificateChains(
    typing_extensions.TypedDict, total=False
):
    caviumCerts: _list[str]
    googleCardCerts: _list[str]
    googlePartitionCerts: _list[str]
