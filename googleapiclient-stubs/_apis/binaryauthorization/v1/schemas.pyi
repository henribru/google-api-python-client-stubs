import typing

import typing_extensions

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    description: str
    expression: str
    title: str

class Attestor(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    userOwnedGrafeasNote: UserOwnedGrafeasNote
    updateTime: str

class Policy(typing_extensions.TypedDict, total=False):
    name: str
    admissionWhitelistPatterns: typing.List[AdmissionWhitelistPattern]
    globalPolicyEvaluationMode: typing_extensions.Literal[
        "GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED", "ENABLE", "DISABLE"
    ]
    defaultAdmissionRule: AdmissionRule
    updateTime: str
    clusterAdmissionRules: typing.Dict[str, typing.Any]
    description: str

class ListAttestorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    attestors: typing.List[Attestor]

class Empty(typing_extensions.TypedDict, total=False): ...

class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class AdmissionWhitelistPattern(typing_extensions.TypedDict, total=False):
    namePattern: str

class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

class PkixPublicKey(typing_extensions.TypedDict, total=False):
    publicKeyPem: str
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

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ValidateAttestationOccurrenceResponse(typing_extensions.TypedDict, total=False):
    denialReason: str
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "VERIFIED", "ATTESTATION_NOT_VERIFIABLE"
    ]

class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    serializedPayload: str
    signatures: typing.List[Signature]
    jwts: typing.List[Jwt]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: IamPolicy

class IamPolicy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    bindingId: str
    condition: Expr
    members: typing.List[str]

class AttestorPublicKey(typing_extensions.TypedDict, total=False):
    comment: str
    id: str
    pkixPublicKey: PkixPublicKey
    asciiArmoredPgpPublicKey: str

class UserOwnedGrafeasNote(typing_extensions.TypedDict, total=False):
    noteReference: str
    delegationServiceAccountEmail: str
    publicKeys: typing.List[AttestorPublicKey]

class ValidateAttestationOccurrenceRequest(typing_extensions.TypedDict, total=False):
    occurrenceNote: str
    attestation: AttestationOccurrence
    occurrenceResourceUri: str

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
