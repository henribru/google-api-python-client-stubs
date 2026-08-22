import typing

_list = list

@typing.type_check_only
class AddQuorumMember(typing.TypedDict, total=False):
    twoFactorPublicKeyPem: str

@typing.type_check_only
class ApproveSingleTenantHsmInstanceProposalRequest(typing.TypedDict, total=False):
    quorumReply: QuorumReply
    requiredActionQuorumReply: RequiredActionQuorumReply

@typing.type_check_only
class ApproveSingleTenantHsmInstanceProposalResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class AsymmetricDecryptRequest(typing.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str

@typing.type_check_only
class AsymmetricDecryptResponse(typing.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    verifiedCiphertextCrc32c: bool

@typing.type_check_only
class AsymmetricSignRequest(typing.TypedDict, total=False):
    data: str
    dataCrc32c: str
    digest: Digest
    digestCrc32c: str

@typing.type_check_only
class AsymmetricSignResponse(typing.TypedDict, total=False):
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    signature: str
    signatureCrc32c: str
    verifiedDataCrc32c: bool
    verifiedDigestCrc32c: bool

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AutokeyConfig(typing.TypedDict, total=False):
    etag: str
    keyProject: str
    keyProjectResolutionMode: typing.Literal[
        "KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED",
        "DEDICATED_KEY_PROJECT",
        "RESOURCE_PROJECT",
        "DISABLED",
    ]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTIVE",
        "KEY_PROJECT_DELETED",
        "UNINITIALIZED",
        "KEY_PROJECT_PERMISSION_DENIED",
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Certificate(typing.TypedDict, total=False):
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
class CertificateChains(typing.TypedDict, total=False):
    caviumCerts: _list[str]
    googleCardCerts: _list[str]
    googlePartitionCerts: _list[str]

@typing.type_check_only
class Challenge(typing.TypedDict, total=False):
    challenge: str
    publicKeyPem: str

@typing.type_check_only
class ChallengeReply(typing.TypedDict, total=False):
    publicKeyPem: str
    signedChallenge: str

@typing.type_check_only
class ChecksummedData(typing.TypedDict, total=False):
    crc32cChecksum: str
    data: str

@typing.type_check_only
class CryptoKey(typing.TypedDict, total=False):
    createTime: str
    cryptoKeyBackend: str
    destroyScheduledDuration: str
    importOnly: bool
    keyAccessJustificationsPolicy: KeyAccessJustificationsPolicy
    labels: dict[str, typing.Any]
    name: str
    nextRotationTime: str
    primary: CryptoKeyVersion
    purpose: typing.Literal[
        "CRYPTO_KEY_PURPOSE_UNSPECIFIED",
        "ENCRYPT_DECRYPT",
        "ASYMMETRIC_SIGN",
        "ASYMMETRIC_DECRYPT",
        "RAW_ENCRYPT_DECRYPT",
        "MAC",
        "KEY_ENCAPSULATION",
        "AES_WRAPPING",
    ]
    rotationPeriod: str
    versionTemplate: CryptoKeyVersionTemplate

@typing.type_check_only
class CryptoKeyVersion(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
    attestation: KeyOperationAttestation
    createTime: str
    destroyEventTime: str
    destroyTime: str
    externalDestructionFailureReason: str
    externalProtectionLevelOptions: ExternalProtectionLevelOptions
    generateTime: str
    generationFailureReason: str
    hsmTrusted: bool
    importFailureReason: str
    importJob: str
    importTime: str
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    reimportEligible: bool
    state: typing.Literal[
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
    trustedWrappingEnabled: bool

@typing.type_check_only
class CryptoKeyVersionTemplate(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]

@typing.type_check_only
class DecapsulateRequest(typing.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str

@typing.type_check_only
class DecapsulateResponse(typing.TypedDict, total=False):
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    sharedSecret: str
    sharedSecretCrc32c: str
    verifiedCiphertextCrc32c: bool

@typing.type_check_only
class DecryptRequest(typing.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    ciphertext: str
    ciphertextCrc32c: str

@typing.type_check_only
class DecryptResponse(typing.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    usedPrimary: bool

@typing.type_check_only
class DeleteSingleTenantHsmInstance(typing.TypedDict, total=False): ...

@typing.type_check_only
class DestroyCryptoKeyVersionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Digest(typing.TypedDict, total=False):
    externalMu: str
    sha256: str
    sha384: str
    sha512: str

@typing.type_check_only
class DisableSingleTenantHsmInstance(typing.TypedDict, total=False): ...

@typing.type_check_only
class EkmConfig(typing.TypedDict, total=False):
    defaultEkmConnection: str
    name: str

@typing.type_check_only
class EkmConnection(typing.TypedDict, total=False):
    createTime: str
    cryptoSpacePath: str
    etag: str
    keyManagementMode: typing.Literal[
        "KEY_MANAGEMENT_MODE_UNSPECIFIED", "MANUAL", "CLOUD_KMS"
    ]
    name: str
    serviceResolvers: _list[ServiceResolver]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableSingleTenantHsmInstance(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptRequest(typing.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    plaintext: str
    plaintextCrc32c: str

@typing.type_check_only
class EncryptResponse(typing.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedPlaintextCrc32c: bool

@typing.type_check_only
class ExecuteSingleTenantHsmInstanceProposalRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportTrustedKeyWrappedCryptoKeyVersionResponse(typing.TypedDict, total=False):
    wrappedKey: str
    wrappedKeyCrc32c: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalProtectionLevelOptions(typing.TypedDict, total=False):
    ekmConnectionBackendOverride: str
    ekmConnectionKeyPath: str
    externalKeyUri: str

@typing.type_check_only
class GenerateRandomBytesRequest(typing.TypedDict, total=False):
    lengthBytes: int
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]

@typing.type_check_only
class GenerateRandomBytesResponse(typing.TypedDict, total=False):
    data: str
    dataCrc32c: str

@typing.type_check_only
class ImportCryptoKeyVersionRequest(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
    cryptoKeyVersion: str
    importJob: str
    rsaAesWrappedKey: str
    trustedWrappingEnabled: bool
    wrappedKey: str

@typing.type_check_only
class ImportJob(typing.TypedDict, total=False):
    attestation: KeyOperationAttestation
    createTime: str
    cryptoKeyBackend: str
    expireEventTime: str
    expireTime: str
    generateTime: str
    importMethod: typing.Literal[
        "IMPORT_METHOD_UNSPECIFIED",
        "RSA_OAEP_3072_SHA1_AES_256",
        "RSA_OAEP_4096_SHA1_AES_256",
        "RSA_OAEP_3072_SHA256_AES_256",
        "RSA_OAEP_4096_SHA256_AES_256",
        "RSA_OAEP_3072_SHA256",
        "RSA_OAEP_4096_SHA256",
        "HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM",
        "HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM",
        "HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM",
    ]
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    publicKey: WrappingPublicKey
    publicKeyFormat: typing.Literal[
        "PUBLIC_KEY_FORMAT_UNSPECIFIED", "PEM", "DER", "NIST_PQC", "XWING_RAW_BYTES"
    ]
    state: typing.Literal[
        "IMPORT_JOB_STATE_UNSPECIFIED", "PENDING_GENERATION", "ACTIVE", "EXPIRED"
    ]

@typing.type_check_only
class ImportTrustedKeyWrappedCryptoKeyVersionRequest(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
    cryptoKeyVersion: str
    importingKey: str
    wrappedKey: str

@typing.type_check_only
class KeyAccessJustificationsEnrollmentConfig(typing.TypedDict, total=False):
    auditLogging: bool
    policyEnforcement: bool

@typing.type_check_only
class KeyAccessJustificationsPolicy(typing.TypedDict, total=False):
    allowedAccessReasons: _list[
        typing.Literal[
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
class KeyAccessJustificationsPolicyConfig(typing.TypedDict, total=False):
    defaultKeyAccessJustificationPolicy: KeyAccessJustificationsPolicy
    defaultPolicyAvailable: bool
    name: str

@typing.type_check_only
class KeyHandle(typing.TypedDict, total=False):
    kmsKey: str
    name: str
    resourceTypeSelector: str

@typing.type_check_only
class KeyOperationAttestation(typing.TypedDict, total=False):
    certChains: CertificateChains
    content: str
    format: typing.Literal[
        "ATTESTATION_FORMAT_UNSPECIFIED", "CAVIUM_V1_COMPRESSED", "CAVIUM_V2_COMPRESSED"
    ]

@typing.type_check_only
class KeyRing(typing.TypedDict, total=False):
    createTime: str
    name: str

@typing.type_check_only
class ListCryptoKeyVersionsResponse(typing.TypedDict, total=False):
    cryptoKeyVersions: _list[CryptoKeyVersion]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListCryptoKeysResponse(typing.TypedDict, total=False):
    cryptoKeys: _list[CryptoKey]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListEkmConnectionsResponse(typing.TypedDict, total=False):
    ekmConnections: _list[EkmConnection]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListImportJobsResponse(typing.TypedDict, total=False):
    importJobs: _list[ImportJob]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListKeyHandlesResponse(typing.TypedDict, total=False):
    keyHandles: _list[KeyHandle]
    nextPageToken: str

@typing.type_check_only
class ListKeyRingsResponse(typing.TypedDict, total=False):
    keyRings: _list[KeyRing]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListRetiredResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    retiredResources: _list[RetiredResource]
    totalSize: str

@typing.type_check_only
class ListSingleTenantHsmInstanceProposalsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    singleTenantHsmInstanceProposals: _list[SingleTenantHsmInstanceProposal]
    totalSize: int

@typing.type_check_only
class ListSingleTenantHsmInstancesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    singleTenantHsmInstances: _list[SingleTenantHsmInstance]
    totalSize: int

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LocationMetadata(typing.TypedDict, total=False):
    ekmAvailable: bool
    hsmAvailable: bool
    hsmSingleTenantAvailable: bool

@typing.type_check_only
class MacSignRequest(typing.TypedDict, total=False):
    data: str
    dataCrc32c: str

@typing.type_check_only
class MacSignResponse(typing.TypedDict, total=False):
    mac: str
    macCrc32c: str
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    verifiedDataCrc32c: bool

@typing.type_check_only
class MacVerifyRequest(typing.TypedDict, total=False):
    data: str
    dataCrc32c: str
    mac: str
    macCrc32c: str

@typing.type_check_only
class MacVerifyResponse(typing.TypedDict, total=False):
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    success: bool
    verifiedDataCrc32c: bool
    verifiedMacCrc32c: bool
    verifiedSuccessIntegrity: bool

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKey(typing.TypedDict, total=False):
    algorithm: typing.Literal[
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
    name: str
    pem: str
    pemCrc32c: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    publicKey: ChecksummedData
    publicKeyFormat: typing.Literal[
        "PUBLIC_KEY_FORMAT_UNSPECIFIED", "PEM", "DER", "NIST_PQC", "XWING_RAW_BYTES"
    ]

@typing.type_check_only
class QuorumAuth(typing.TypedDict, total=False):
    requiredApproverCount: int
    totalApproverCount: int
    twoFactorPublicKeyPems: _list[str]

@typing.type_check_only
class QuorumParameters(typing.TypedDict, total=False):
    approvedTwoFactorPublicKeyPems: _list[str]
    challenges: _list[Challenge]
    requiredApproverCount: int

@typing.type_check_only
class QuorumReply(typing.TypedDict, total=False):
    challengeReplies: _list[ChallengeReply]

@typing.type_check_only
class RawDecryptRequest(typing.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    ciphertext: str
    ciphertextCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    tagLength: int

@typing.type_check_only
class RawDecryptResponse(typing.TypedDict, total=False):
    plaintext: str
    plaintextCrc32c: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedCiphertextCrc32c: bool
    verifiedInitializationVectorCrc32c: bool

@typing.type_check_only
class RawEncryptRequest(typing.TypedDict, total=False):
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    plaintext: str
    plaintextCrc32c: str

@typing.type_check_only
class RawEncryptResponse(typing.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str
    initializationVector: str
    initializationVectorCrc32c: str
    name: str
    protectionLevel: typing.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED",
        "SOFTWARE",
        "HSM",
        "EXTERNAL",
        "EXTERNAL_VPC",
        "HSM_SINGLE_TENANT",
    ]
    tagLength: int
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    verifiedInitializationVectorCrc32c: bool
    verifiedPlaintextCrc32c: bool

@typing.type_check_only
class RefreshSingleTenantHsmInstance(typing.TypedDict, total=False): ...

@typing.type_check_only
class RegisterTwoFactorAuthKeys(typing.TypedDict, total=False):
    requiredApproverCount: int
    twoFactorPublicKeyPems: _list[str]

@typing.type_check_only
class RemoveQuorumMember(typing.TypedDict, total=False):
    twoFactorPublicKeyPem: str

@typing.type_check_only
class RequiredActionQuorumParameters(typing.TypedDict, total=False):
    approvedTwoFactorPublicKeyPems: _list[str]
    quorumChallenges: _list[Challenge]
    requiredApproverCount: int
    requiredChallenges: _list[Challenge]

@typing.type_check_only
class RequiredActionQuorumReply(typing.TypedDict, total=False):
    quorumChallengeReplies: _list[ChallengeReply]
    requiredChallengeReplies: _list[ChallengeReply]

@typing.type_check_only
class RestoreCryptoKeyVersionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetiredResource(typing.TypedDict, total=False):
    deleteTime: str
    name: str
    originalResource: str
    resourceType: str

@typing.type_check_only
class ServiceResolver(typing.TypedDict, total=False):
    endpointFilter: str
    hostname: str
    serverCertificates: _list[Certificate]
    serviceDirectoryService: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class ShowEffectiveAutokeyConfigResponse(typing.TypedDict, total=False):
    keyProject: str
    keyProjectResolutionMode: typing.Literal[
        "KEY_PROJECT_RESOLUTION_MODE_UNSPECIFIED",
        "DEDICATED_KEY_PROJECT",
        "RESOURCE_PROJECT",
        "DISABLED",
    ]
    source: Source

@typing.type_check_only
class ShowEffectiveKeyAccessJustificationsEnrollmentConfigResponse(
    typing.TypedDict, total=False
):
    externalConfig: KeyAccessJustificationsEnrollmentConfig
    hardwareConfig: KeyAccessJustificationsEnrollmentConfig
    softwareConfig: KeyAccessJustificationsEnrollmentConfig

@typing.type_check_only
class ShowEffectiveKeyAccessJustificationsPolicyConfigResponse(
    typing.TypedDict, total=False
):
    effectiveKajPolicy: KeyAccessJustificationsPolicyConfig

@typing.type_check_only
class SingleTenantHsmInstance(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    disableTime: str
    keyPortabilityEnabled: bool
    name: str
    quorumAuth: QuorumAuth
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "PENDING_TWO_FACTOR_AUTH_REGISTRATION",
        "ACTIVE",
        "DISABLING",
        "DISABLED",
        "DELETING",
        "DELETED",
        "FAILED",
    ]
    unrefreshedDurationUntilDisable: str

@typing.type_check_only
class SingleTenantHsmInstanceProposal(typing.TypedDict, total=False):
    addQuorumMember: AddQuorumMember
    createTime: str
    deleteSingleTenantHsmInstance: DeleteSingleTenantHsmInstance
    deleteTime: str
    disableSingleTenantHsmInstance: DisableSingleTenantHsmInstance
    enableSingleTenantHsmInstance: EnableSingleTenantHsmInstance
    expireTime: str
    failureReason: str
    name: str
    purgeTime: str
    quorumParameters: QuorumParameters
    refreshSingleTenantHsmInstance: RefreshSingleTenantHsmInstance
    registerTwoFactorAuthKeys: RegisterTwoFactorAuthKeys
    removeQuorumMember: RemoveQuorumMember
    requiredActionQuorumParameters: RequiredActionQuorumParameters
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "PENDING",
        "APPROVED",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "DELETED",
    ]
    ttl: str
    upgradeKeyTrust: UpgradeKeyTrust

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpdateCryptoKeyPrimaryVersionRequest(typing.TypedDict, total=False):
    cryptoKeyVersionId: str

@typing.type_check_only
class UpgradeKeyTrust(typing.TypedDict, total=False):
    name: str
    twoFactorPublicKeyPem: str

@typing.type_check_only
class VerifyConnectivityResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class WrappingPublicKey(typing.TypedDict, total=False):
    data: str
    pem: str
