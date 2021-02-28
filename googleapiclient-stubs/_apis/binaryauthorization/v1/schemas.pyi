import typing

import typing_extensions
@typing.type_check_only
class AdmissionRule(typing_extensions.TypedDict, total=False):
    enforcementMode: typing_extensions.Literal[
        "ENFORCEMENT_MODE_UNSPECIFIED",
        "ENFORCED_BLOCK_AND_AUDIT_LOG",
        "DRYRUN_AUDIT_LOG_ONLY",
    ]
    evaluationMode: typing_extensions.Literal[
        "EVALUATION_MODE_UNSPECIFIED",
        "ALWAYS_ALLOW",
        "REQUIRE_ATTESTATION",
        "ALWAYS_DENY",
    ]
    requireAttestationsBy: typing.List[str]

@typing.type_check_only
class AdmissionWhitelistPattern(typing_extensions.TypedDict, total=False):
    namePattern: str

@typing.type_check_only
class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    jwts: typing.List[Jwt]
    serializedPayload: str
    signatures: typing.List[Signature]

@typing.type_check_only
class Attestor(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    updateTime: str
    userOwnedGrafeasNote: UserOwnedGrafeasNote

@typing.type_check_only
class AttestorPublicKey(typing_extensions.TypedDict, total=False):
    asciiArmoredPgpPublicKey: str
    comment: str
    id: str
    pkixPublicKey: PkixPublicKey

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class IamPolicy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class ListAttestorsResponse(typing_extensions.TypedDict, total=False):
    attestors: typing.List[Attestor]
    nextPageToken: str

@typing.type_check_only
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

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    admissionWhitelistPatterns: typing.List[AdmissionWhitelistPattern]
    clusterAdmissionRules: typing.Dict[str, typing.Any]
    defaultAdmissionRule: AdmissionRule
    description: str
    globalPolicyEvaluationMode: typing_extensions.Literal[
        "GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED", "ENABLE", "DISABLE"
    ]
    istioServiceIdentityAdmissionRules: typing.Dict[str, typing.Any]
    kubernetesNamespaceAdmissionRules: typing.Dict[str, typing.Any]
    kubernetesServiceAccountAdmissionRules: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: IamPolicy

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class UserOwnedGrafeasNote(typing_extensions.TypedDict, total=False):
    delegationServiceAccountEmail: str
    noteReference: str
    publicKeys: typing.List[AttestorPublicKey]

@typing.type_check_only
class ValidateAttestationOccurrenceRequest(typing_extensions.TypedDict, total=False):
    attestation: AttestationOccurrence
    occurrenceNote: str
    occurrenceResourceUri: str

@typing.type_check_only
class ValidateAttestationOccurrenceResponse(typing_extensions.TypedDict, total=False):
    denialReason: str
    result: typing_extensions.Literal[
        "RESULT_UNSPECIFIED", "VERIFIED", "ATTESTATION_NOT_VERIFIABLE"
    ]
