import typing

import typing_extensions

_list = list

@typing.type_check_only
class AsymmetricDecryptRequest(typing_extensions.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str

@typing.type_check_only
class AsymmetricDecryptResponse(typing_extensions.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    verifiedCiphertextCrc32c: bool

@typing.type_check_only
class AsymmetricSignRequest(typing_extensions.TypedDict, total=False):
    data: str
    dataCrc32c: str
    digest: Digest
    digestCrc32c: str

@typing.type_check_only
class AsymmetricSignResponse(typing_extensions.TypedDict, total=False):
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    signature: str
    signatureCrc32c: str
    verifiedDataCrc32c: bool
    verifiedDigestCrc32c: bool

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AutokeyConfig(typing_extensions.TypedDict, total=False):
    etag: str
    keyProject: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "KEY_PROJECT_DELETED", "UNINITIALIZED"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Certificate(typing_extensions.TypedDict, total=False):
    issuer: str
    notAfterTime: str
    notBeforeTime: str
    parsed: bool
    rawDer: str
    serialNumber: str
    sha256Fingerprint: str
    subject: str
    subjectAlternativeDnsNames: _list[str]

@typing.type_check_only
class CertificateChains(typing_extensions.TypedDict, total=False):
    caviumCerts: _list[str]
    googleCardCerts: _list[str]
    googlePartitionCerts: _list[str]

@typing.type_check_only
class ChecksummedData(typing_extensions.TypedDict, total=False):
    crc32cChecksum: str
    data: str

@typing.type_check_only
class CryptoKey(typing_extensions.TypedDict, total=False):
    createTime: str
    cryptoKeyBackend: str
    destroyScheduledDuration: str
    importOnly: bool
    keyAccessJustificationsPolicy: KeyAccessJustificationsPolicy
    labels: dict[str, typing.Any]
    name: str
    nextRotationTime: str
    primary: CryptoKeyVersion
    purpose: typing_extensions.Literal[
        "CRYPTO_KEY_PURPOSE_UNSPECIFIED",
        "ENCRYPT_DECRYPT",
        "ASYMMETRIC_SIGN",
        "ASYMMETRIC_DECRYPT",
        "RAW_ENCRYPT_DECRYPT",
        "MAC",
    ]
    rotationPeriod: str
    versionTemplate: CryptoKeyVersionTemplate

@typing.type_check_only
class CryptoKeyVersion(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
        "PQ_SIGN_ML_DSA_65",
        "PQ_SIGN_SLH_DSA_SHA2_128S",
        "PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256",
    ]
    attestation: KeyOperationAttestation
    createTime: str
    destroyEventTime: str
    destroyTime: str
    externalDestructionFailureReason: str
    externalProtectionLevelOptions: ExternalProtectionLevelOptions
    generateTime: str
    generationFailureReason: str
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
        "GENERATION_FAILED",
        "PENDING_EXTERNAL_DESTRUCTION",
        "EXTERNAL_DESTRUCTION_FAILED",
    ]

@typing.type_check_only
class CryptoKeyVersionTemplate(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
        "PQ_SIGN_ML_DSA_65",
        "PQ_SIGN_SLH_DSA_SHA2_128S",
        "PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256",
    ]
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]

@typing.type_check_only
class DecryptRequest(typing_extensions.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    ciphertext: str
    ciphertextCrc32c: str

@typing.type_check_only
class DecryptResponse(typing_extensions.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    usedPrimary: bool

@typing.type_check_only
class DestroyCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Digest(typing_extensions.TypedDict, total=False):
    sha256: str
    sha384: str
    sha512: str

@typing.type_check_only
class EkmConfig(typing_extensions.TypedDict, total=False):
    defaultEkmConnection: str
    name: str

@typing.type_check_only
class EkmConnection(typing_extensions.TypedDict, total=False):
    createTime: str
    cryptoSpacePath: str
    etag: str
    keyManagementMode: typing_extensions.Literal[
        "KEY_MANAGEMENT_MODE_UNSPECIFIED", "MANUAL", "CLOUD_KMS"
    ]
    name: str
    serviceResolvers: _list[ServiceResolver]

@typing.type_check_only
class EncryptRequest(typing_extensions.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    plaintext: str
    plaintextCrc32c: str

@typing.type_check_only
class EncryptResponse(typing_extensions.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedPlaintextCrc32c: bool

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalProtectionLevelOptions(typing_extensions.TypedDict, total=False):
    ekmConnectionKeyPath: str
    externalKeyUri: str

@typing.type_check_only
class GenerateRandomBytesRequest(typing_extensions.TypedDict, total=False):
    lengthBytes: int
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]

@typing.type_check_only
class GenerateRandomBytesResponse(typing_extensions.TypedDict, total=False):
    data: str
    dataCrc32c: str

@typing.type_check_only
class ImportCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
        "PQ_SIGN_ML_DSA_65",
        "PQ_SIGN_SLH_DSA_SHA2_128S",
        "PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256",
    ]
    cryptoKeyVersion: str
    importJob: str
    rsaAesWrappedKey: str
    wrappedKey: str

@typing.type_check_only
class ImportJob(typing_extensions.TypedDict, total=False):
    attestation: KeyOperationAttestation
    createTime: str
    expireEventTime: str
    expireTime: str
    generateTime: str
    importMethod: typing_extensions.Literal[
        "IMPORT_METHOD_UNSPECIFIED",
        "RSA_OAEP_3072_SHA1_AES_256",
        "RSA_OAEP_4096_SHA1_AES_256",
        "RSA_OAEP_3072_SHA256_AES_256",
        "RSA_OAEP_4096_SHA256_AES_256",
        "RSA_OAEP_3072_SHA256",
        "RSA_OAEP_4096_SHA256",
    ]
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    publicKey: WrappingPublicKey
    state: typing_extensions.Literal[
        "IMPORT_JOB_STATE_UNSPECIFIED", "PENDING_GENERATION", "ACTIVE", "EXPIRED"
    ]

@typing.type_check_only
class KeyAccessJustificationsEnrollmentConfig(typing_extensions.TypedDict, total=False):
    auditLogging: bool
    policyEnforcement: bool

@typing.type_check_only
class KeyAccessJustificationsPolicy(typing_extensions.TypedDict, total=False):
    allowedAccessReasons: _list[
        typing_extensions.Literal[
            "REASON_UNSPECIFIED",
            "CUSTOMER_INITIATED_SUPPORT",
            "GOOGLE_INITIATED_SERVICE",
            "THIRD_PARTY_DATA_REQUEST",
            "GOOGLE_INITIATED_REVIEW",
            "CUSTOMER_INITIATED_ACCESS",
            "GOOGLE_INITIATED_SYSTEM_OPERATION",
            "REASON_NOT_EXPECTED",
            "MODIFIED_CUSTOMER_INITIATED_ACCESS",
            "MODIFIED_GOOGLE_INITIATED_SYSTEM_OPERATION",
            "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
            "CUSTOMER_AUTHORIZED_WORKFLOW_SERVICING",
        ]
    ]

@typing.type_check_only
class KeyAccessJustificationsPolicyConfig(typing_extensions.TypedDict, total=False):
    defaultKeyAccessJustificationPolicy: KeyAccessJustificationsPolicy
    name: str

@typing.type_check_only
class KeyHandle(typing_extensions.TypedDict, total=False):
    kmsKey: str
    name: str
    resourceTypeSelector: str

@typing.type_check_only
class KeyOperationAttestation(typing_extensions.TypedDict, total=False):
    certChains: CertificateChains
    content: str
    format: typing_extensions.Literal[
        "ATTESTATION_FORMAT_UNSPECIFIED", "CAVIUM_V1_COMPRESSED", "CAVIUM_V2_COMPRESSED"
    ]

@typing.type_check_only
class KeyRing(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str

@typing.type_check_only
class ListCryptoKeyVersionsResponse(typing_extensions.TypedDict, total=False):
    cryptoKeyVersions: _list[CryptoKeyVersion]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListCryptoKeysResponse(typing_extensions.TypedDict, total=False):
    cryptoKeys: _list[CryptoKey]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListEkmConnectionsResponse(typing_extensions.TypedDict, total=False):
    ekmConnections: _list[EkmConnection]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListImportJobsResponse(typing_extensions.TypedDict, total=False):
    importJobs: _list[ImportJob]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListKeyHandlesResponse(typing_extensions.TypedDict, total=False):
    keyHandles: _list[KeyHandle]
    nextPageToken: str

@typing.type_check_only
class ListKeyRingsResponse(typing_extensions.TypedDict, total=False):
    keyRings: _list[KeyRing]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing_extensions.TypedDict, total=False):
    ekmAvailable: bool
    hsmAvailable: bool

@typing.type_check_only
class MacSignRequest(typing_extensions.TypedDict, total=False):
    data: str
    dataCrc32c: str

@typing.type_check_only
class MacSignResponse(typing_extensions.TypedDict, total=False):
    mac: str
    macCrc32c: str
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    verifiedDataCrc32c: bool

@typing.type_check_only
class MacVerifyRequest(typing_extensions.TypedDict, total=False):
    data: str
    dataCrc32c: str
    mac: str
    macCrc32c: str

@typing.type_check_only
class MacVerifyResponse(typing_extensions.TypedDict, total=False):
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    success: bool
    verifiedDataCrc32c: bool
    verifiedMacCrc32c: bool
    verifiedSuccessIntegrity: bool

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKey(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
        "PQ_SIGN_ML_DSA_65",
        "PQ_SIGN_SLH_DSA_SHA2_128S",
        "PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256",
    ]
    name: str
    pem: str
    pemCrc32c: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    publicKey: ChecksummedData
    publicKeyFormat: typing_extensions.Literal[
        "PUBLIC_KEY_FORMAT_UNSPECIFIED", "PEM", "NIST_PQC"
    ]

@typing.type_check_only
class RawDecryptRequest(typing_extensions.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    ciphertext: str
    ciphertextCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    tagLength: int

@typing.type_check_only
class RawDecryptResponse(typing_extensions.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedCiphertextCrc32c: bool
    verifiedInitializationVectorCrc32c: bool

@typing.type_check_only
class RawEncryptRequest(typing_extensions.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    plaintext: str
    plaintextCrc32c: str

@typing.type_check_only
class RawEncryptResponse(typing_extensions.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    name: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL", "EXTERNAL_VPC"
    ]
    tagLength: int
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedInitializationVectorCrc32c: bool
    verifiedPlaintextCrc32c: bool

@typing.type_check_only
class RestoreCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ServiceResolver(typing_extensions.TypedDict, total=False):
    endpointFilter: str
    hostname: str
    serverCertificates: _list[Certificate]
    serviceDirectoryService: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class ShowEffectiveAutokeyConfigResponse(typing_extensions.TypedDict, total=False):
    keyProject: str

@typing.type_check_only
class ShowEffectiveKeyAccessJustificationsEnrollmentConfigResponse(
    typing_extensions.TypedDict, total=False
):
    externalConfig: KeyAccessJustificationsEnrollmentConfig
    hardwareConfig: KeyAccessJustificationsEnrollmentConfig
    softwareConfig: KeyAccessJustificationsEnrollmentConfig

@typing.type_check_only
class ShowEffectiveKeyAccessJustificationsPolicyConfigResponse(
    typing_extensions.TypedDict, total=False
):
    effectiveKajPolicy: KeyAccessJustificationsPolicyConfig

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpdateCryptoKeyPrimaryVersionRequest(typing_extensions.TypedDict, total=False):
    cryptoKeyVersionId: str

@typing.type_check_only
class VerifyConnectivityResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class WrappingPublicKey(typing_extensions.TypedDict, total=False):
    pem: str
