import typing

import typing_extensions

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    etag: str
    version: int
    bindings: typing.List[Binding]

class EncryptResponse(typing_extensions.TypedDict, total=False):
    ciphertextCrc32c: str
    verifiedAdditionalAuthenticatedDataCrc32c: bool
    ciphertext: str
    name: str
    verifiedPlaintextCrc32c: bool

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class EncryptRequest(typing_extensions.TypedDict, total=False):
    additionalAuthenticatedDataCrc32c: str
    additionalAuthenticatedData: str
    plaintext: str
    plaintextCrc32c: str

class ListCryptoKeysResponse(typing_extensions.TypedDict, total=False):
    cryptoKeys: typing.List[CryptoKey]
    nextPageToken: str
    totalSize: int

class ImportJob(typing_extensions.TypedDict, total=False):
    name: str
    expireEventTime: str
    state: typing_extensions.Literal[
        "IMPORT_JOB_STATE_UNSPECIFIED", "PENDING_GENERATION", "ACTIVE", "EXPIRED"
    ]
    attestation: KeyOperationAttestation
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL"
    ]
    publicKey: WrappingPublicKey
    generateTime: str
    createTime: str
    importMethod: typing_extensions.Literal[
        "IMPORT_METHOD_UNSPECIFIED",
        "RSA_OAEP_3072_SHA1_AES_256",
        "RSA_OAEP_4096_SHA1_AES_256",
    ]
    expireTime: str

class CryptoKeyVersion(typing_extensions.TypedDict, total=False):
    generateTime: str
    attestation: KeyOperationAttestation
    importFailureReason: str
    createTime: str
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL"
    ]
    importTime: str
    destroyEventTime: str
    destroyTime: str
    name: str
    externalProtectionLevelOptions: ExternalProtectionLevelOptions
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
    importJob: str
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
        "RSA_DECRYPT_OAEP_2048_SHA256",
        "RSA_DECRYPT_OAEP_3072_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA512",
        "EC_SIGN_P256_SHA256",
        "EC_SIGN_P384_SHA384",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    title: str
    location: str

class PublicKey(typing_extensions.TypedDict, total=False):
    name: str
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
        "RSA_DECRYPT_OAEP_2048_SHA256",
        "RSA_DECRYPT_OAEP_3072_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA512",
        "EC_SIGN_P256_SHA256",
        "EC_SIGN_P384_SHA384",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    pemCrc32c: str
    pem: str

class ExternalProtectionLevelOptions(typing_extensions.TypedDict, total=False):
    externalKeyUri: str

class RestoreCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False): ...

class CryptoKey(typing_extensions.TypedDict, total=False):
    rotationPeriod: str
    labels: typing.Dict[str, typing.Any]
    versionTemplate: CryptoKeyVersionTemplate
    nextRotationTime: str
    primary: CryptoKeyVersion
    name: str
    createTime: str
    purpose: typing_extensions.Literal[
        "CRYPTO_KEY_PURPOSE_UNSPECIFIED",
        "ENCRYPT_DECRYPT",
        "ASYMMETRIC_SIGN",
        "ASYMMETRIC_DECRYPT",
    ]

class KeyRing(typing_extensions.TypedDict, total=False):
    name: str
    createTime: str

class AsymmetricDecryptRequest(typing_extensions.TypedDict, total=False):
    ciphertextCrc32c: str
    ciphertext: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class CertificateChains(typing_extensions.TypedDict, total=False):
    caviumCerts: typing.List[str]
    googleCardCerts: typing.List[str]
    googlePartitionCerts: typing.List[str]

class DecryptRequest(typing_extensions.TypedDict, total=False):
    ciphertext: str
    ciphertextCrc32c: str
    additionalAuthenticatedData: str
    additionalAuthenticatedDataCrc32c: str

class ListCryptoKeyVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    cryptoKeyVersions: typing.List[CryptoKeyVersion]

class UpdateCryptoKeyPrimaryVersionRequest(typing_extensions.TypedDict, total=False):
    cryptoKeyVersionId: str

class AsymmetricSignRequest(typing_extensions.TypedDict, total=False):
    digestCrc32c: str
    digest: Digest

class WrappingPublicKey(typing_extensions.TypedDict, total=False):
    pem: str

class LocationMetadata(typing_extensions.TypedDict, total=False):
    hsmAvailable: bool
    ekmAvailable: bool

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    bindingId: str
    members: typing.List[str]
    role: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class ListKeyRingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    keyRings: typing.List[KeyRing]
    totalSize: int

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AsymmetricSignResponse(typing_extensions.TypedDict, total=False):
    signature: str
    name: str
    verifiedDigestCrc32c: bool
    signatureCrc32c: str

class Digest(typing_extensions.TypedDict, total=False):
    sha512: str
    sha384: str
    sha256: str

class DecryptResponse(typing_extensions.TypedDict, total=False):
    plaintextCrc32c: str
    plaintext: str

class AsymmetricDecryptResponse(typing_extensions.TypedDict, total=False):
    verifiedCiphertextCrc32c: bool
    plaintext: str
    plaintextCrc32c: str

class KeyOperationAttestation(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "ATTESTATION_FORMAT_UNSPECIFIED", "CAVIUM_V1_COMPRESSED", "CAVIUM_V2_COMPRESSED"
    ]
    content: str
    certChains: CertificateChains

class CryptoKeyVersionTemplate(typing_extensions.TypedDict, total=False):
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
        "RSA_DECRYPT_OAEP_2048_SHA256",
        "RSA_DECRYPT_OAEP_3072_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA512",
        "EC_SIGN_P256_SHA256",
        "EC_SIGN_P384_SHA384",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    protectionLevel: typing_extensions.Literal[
        "PROTECTION_LEVEL_UNSPECIFIED", "SOFTWARE", "HSM", "EXTERNAL"
    ]

class ListImportJobsResponse(typing_extensions.TypedDict, total=False):
    totalSize: int
    importJobs: typing.List[ImportJob]
    nextPageToken: str

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ImportCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False):
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
        "RSA_DECRYPT_OAEP_2048_SHA256",
        "RSA_DECRYPT_OAEP_3072_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA256",
        "RSA_DECRYPT_OAEP_4096_SHA512",
        "EC_SIGN_P256_SHA256",
        "EC_SIGN_P384_SHA384",
        "EXTERNAL_SYMMETRIC_ENCRYPTION",
    ]
    rsaAesWrappedKey: str
    importJob: str

class DestroyCryptoKeyVersionRequest(typing_extensions.TypedDict, total=False): ...
