import typing

import typing_extensions

_list = list

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
    requireAttestationsBy: _list[str]

@typing.type_check_only
class AdmissionWhitelistPattern(typing_extensions.TypedDict, total=False):
    namePattern: str

@typing.type_check_only
class AllowlistResult(typing_extensions.TypedDict, total=False):
    matchedPattern: str

@typing.type_check_only
class AttestationAuthenticator(typing_extensions.TypedDict, total=False):
    displayName: str
    pkixPublicKeySet: PkixPublicKeySet

@typing.type_check_only
class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    jwts: _list[Jwt]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class AttestationSource(typing_extensions.TypedDict, total=False):
    containerAnalysisAttestationProjects: _list[str]

@typing.type_check_only
class Attestor(typing_extensions.TypedDict, total=False):
    description: str
    etag: str
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
    members: _list[str]
    role: str

@typing.type_check_only
class Check(typing_extensions.TypedDict, total=False):
    alwaysDeny: bool
    displayName: str
    imageAllowlist: ImageAllowlist
    imageFreshnessCheck: ImageFreshnessCheck
    sigstoreSignatureCheck: SigstoreSignatureCheck
    simpleSigningAttestationCheck: SimpleSigningAttestationCheck
    slsaCheck: SlsaCheck
    trustedDirectoryCheck: TrustedDirectoryCheck
    vulnerabilityCheck: VulnerabilityCheck

@typing.type_check_only
class CheckResult(typing_extensions.TypedDict, total=False):
    allowlistResult: AllowlistResult
    displayName: str
    evaluationResult: EvaluationResult
    explanation: str
    index: str
    type: str

@typing.type_check_only
class CheckResults(typing_extensions.TypedDict, total=False):
    results: _list[CheckResult]

@typing.type_check_only
class CheckSet(typing_extensions.TypedDict, total=False):
    checks: _list[Check]
    displayName: str
    imageAllowlist: ImageAllowlist
    scope: Scope

@typing.type_check_only
class CheckSetResult(typing_extensions.TypedDict, total=False):
    allowlistResult: AllowlistResult
    checkResults: CheckResults
    displayName: str
    explanation: str
    index: str
    scope: Scope

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EvaluateGkePolicyRequest(typing_extensions.TypedDict, total=False):
    resource: dict[str, typing.Any]

@typing.type_check_only
class EvaluateGkePolicyResponse(typing_extensions.TypedDict, total=False):
    results: _list[PodResult]
    verdict: typing_extensions.Literal[
        "VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class EvaluationResult(typing_extensions.TypedDict, total=False):
    verdict: typing_extensions.Literal[
        "CHECK_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GkePolicy(typing_extensions.TypedDict, total=False):
    checkSets: _list[CheckSet]
    imageAllowlist: ImageAllowlist

@typing.type_check_only
class IamPolicy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ImageAllowlist(typing_extensions.TypedDict, total=False):
    allowPattern: _list[str]

@typing.type_check_only
class ImageFreshnessCheck(typing_extensions.TypedDict, total=False):
    maxUploadAgeDays: int

@typing.type_check_only
class ImageResult(typing_extensions.TypedDict, total=False):
    allowlistResult: AllowlistResult
    checkSetResult: CheckSetResult
    explanation: str
    imageUri: str
    verdict: typing_extensions.Literal[
        "IMAGE_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class ListAttestorsResponse(typing_extensions.TypedDict, total=False):
    attestors: _list[Attestor]
    nextPageToken: str

@typing.type_check_only
class ListPlatformPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    platformPolicies: _list[PlatformPolicy]

@typing.type_check_only
class PkixPublicKey(typing_extensions.TypedDict, total=False):
    keyId: str
    publicKeyPem: str
    signatureAlgorithm: typing_extensions.Literal[
        "SIGNATURE_ALGORITHM_UNSPECIFIED",
        "RSA_PSS_2048_SHA256",
        "RSA_SIGN_PSS_2048_SHA256",
        "RSA_PSS_3072_SHA256",
        "RSA_SIGN_PSS_3072_SHA256",
        "RSA_PSS_4096_SHA256",
        "RSA_SIGN_PSS_4096_SHA256",
        "RSA_PSS_4096_SHA512",
        "RSA_SIGN_PSS_4096_SHA512",
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
class PkixPublicKeySet(typing_extensions.TypedDict, total=False):
    pkixPublicKeys: _list[PkixPublicKey]

@typing.type_check_only
class PlatformPolicy(typing_extensions.TypedDict, total=False):
    description: str
    etag: str
    gkePolicy: GkePolicy
    name: str
    updateTime: str

@typing.type_check_only
class PodResult(typing_extensions.TypedDict, total=False):
    imageResults: _list[ImageResult]
    kubernetesNamespace: str
    kubernetesServiceAccount: str
    podName: str
    verdict: typing_extensions.Literal[
        "POD_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    admissionWhitelistPatterns: _list[AdmissionWhitelistPattern]
    clusterAdmissionRules: dict[str, typing.Any]
    defaultAdmissionRule: AdmissionRule
    description: str
    etag: str
    globalPolicyEvaluationMode: typing_extensions.Literal[
        "GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED", "ENABLE", "DISABLE"
    ]
    istioServiceIdentityAdmissionRules: dict[str, typing.Any]
    kubernetesNamespaceAdmissionRules: dict[str, typing.Any]
    kubernetesServiceAccountAdmissionRules: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class Scope(typing_extensions.TypedDict, total=False):
    kubernetesNamespace: str
    kubernetesServiceAccount: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: IamPolicy

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SigstoreAuthority(typing_extensions.TypedDict, total=False):
    displayName: str
    publicKeySet: SigstorePublicKeySet

@typing.type_check_only
class SigstorePublicKey(typing_extensions.TypedDict, total=False):
    publicKeyPem: str

@typing.type_check_only
class SigstorePublicKeySet(typing_extensions.TypedDict, total=False):
    publicKeys: _list[SigstorePublicKey]

@typing.type_check_only
class SigstoreSignatureCheck(typing_extensions.TypedDict, total=False):
    sigstoreAuthorities: _list[SigstoreAuthority]

@typing.type_check_only
class SimpleSigningAttestationCheck(typing_extensions.TypedDict, total=False):
    attestationAuthenticators: _list[AttestationAuthenticator]
    containerAnalysisAttestationProjects: _list[str]

@typing.type_check_only
class SlsaCheck(typing_extensions.TypedDict, total=False):
    rules: _list[VerificationRule]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrustedDirectoryCheck(typing_extensions.TypedDict, total=False):
    trustedDirPatterns: _list[str]

@typing.type_check_only
class UserOwnedGrafeasNote(typing_extensions.TypedDict, total=False):
    delegationServiceAccountEmail: str
    noteReference: str
    publicKeys: _list[AttestorPublicKey]

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

@typing.type_check_only
class VerificationRule(typing_extensions.TypedDict, total=False):
    attestationSource: AttestationSource
    configBasedBuildRequired: bool
    trustedBuilder: typing_extensions.Literal[
        "BUILDER_UNSPECIFIED", "GOOGLE_CLOUD_BUILD"
    ]
    trustedSourceRepoPatterns: _list[str]

@typing.type_check_only
class VulnerabilityCheck(typing_extensions.TypedDict, total=False):
    allowedCves: _list[str]
    blockedCves: _list[str]
    containerAnalysisVulnerabilityProjects: _list[str]
    maximumFixableSeverity: typing_extensions.Literal[
        "MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED",
        "BLOCK_ALL",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "ALLOW_ALL",
    ]
    maximumUnfixableSeverity: typing_extensions.Literal[
        "MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED",
        "BLOCK_ALL",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "ALLOW_ALL",
    ]
