import typing

import typing_extensions

class IamPolicy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]

class ValidateAttestationOccurrenceRequest(typing_extensions.TypedDict, total=False):
    occurrenceResourceUri: str
    occurrenceNote: str
    attestation: AttestationOccurrence

class ListAttestorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    attestors: typing.List[Attestor]

class AdmissionRule(typing_extensions.TypedDict, total=False):
    evaluationMode: typing_extensions.Literal[
        "EVALUATION_MODE_UNSPECIFIED",
        "ALWAYS_ALLOW",
        "REQUIRE_ATTESTATION",
        "ALWAYS_DENY",
    ]
    enforcementMode: typing_extensions.Literal[
        "ENFORCEMENT_MODE_UNSPECIFIED",
        "ENFORCED_BLOCK_AND_AUDIT_LOG",
        "DRYRUN_AUDIT_LOG_ONLY",
    ]
    requireAttestationsBy: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    title: str
    description: str
    location: str

class Empty(typing_extensions.TypedDict, total=False): ...

class PkixPublicKey(typing_extensions.TypedDict, total=False):
    signatureAlgorithm: typing_extensions.Literal[
        "SIGNATURE_ALGORITHM_UNSPECIFIED",
        "RSA_PSS_2048_SHA256",
        "RSA_PSS_3072_SHA256",
        "RSA_PSS_4096_SHA256",
        "RSA_PSS_4096_SHA512",
        "RSA_SIGN_PKCS1_2048_SHA256",
        "RSA_SIGN_PKCS1_3072_SHA256",
        "RSA_SIGN_PKCS1_4096_SHA256",
        "RSA_SIGN_PKCS1_4096_SHA512",
        "ECDSA_P256_SHA256",
        "EC_SIGN_P256_SHA256",
        "ECDSA_P384_SHA384",
        "EC_SIGN_P384_SHA384",
        "ECDSA_P521_SHA512",
        "EC_SIGN_P521_SHA512",
    ]
    publicKeyPem: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    signatures: typing.List[Signature]
    serializedPayload: str
    jwts: typing.List[Jwt]

class AttestorPublicKey(typing_extensions.TypedDict, total=False):
    id: str
    asciiArmoredPgpPublicKey: str
    pkixPublicKey: PkixPublicKey
    comment: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: IamPolicy

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str
    bindingId: str

class Policy(typing_extensions.TypedDict, total=False):
    clusterAdmissionRules: typing.Dict[str, typing.Any]
    description: str
    name: str
    admissionWhitelistPatterns: typing.List[AdmissionWhitelistPattern]
    defaultAdmissionRule: AdmissionRule
    updateTime: str
    globalPolicyEvaluationMode: typing_extensions.Literal[
        "GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED", "ENABLE", "DISABLE"
    ]

class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

class ValidateAttestationOccurrenceResponse(typing_extensions.TypedDict, total=False):
    denialReason: str
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "VERIFIED", "ATTESTATION_NOT_VERIFIABLE"
    ]

class AdmissionWhitelistPattern(typing_extensions.TypedDict, total=False):
    namePattern: str

class UserOwnedDrydockNote(typing_extensions.TypedDict, total=False):
    publicKeys: typing.List[AttestorPublicKey]
    noteReference: str
    delegationServiceAccountEmail: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Attestor(typing_extensions.TypedDict, total=False):
    description: str
    updateTime: str
    name: str
    userOwnedDrydockNote: UserOwnedDrydockNote

class Signature(typing_extensions.TypedDict, total=False):
    signature: str
    publicKeyId: str
