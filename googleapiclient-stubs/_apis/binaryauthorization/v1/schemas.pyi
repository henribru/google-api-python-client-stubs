import typing

_list = list

@typing.type_check_only
class AdmissionRule(typing.TypedDict, total=False):
    enforcementMode: typing.Literal[
        "ENFORCEMENT_MODE_UNSPECIFIED",
        "ENFORCED_BLOCK_AND_AUDIT_LOG",
        "DRYRUN_AUDIT_LOG_ONLY",
    ]
    evaluationMode: typing.Literal[
        "EVALUATION_MODE_UNSPECIFIED",
        "ALWAYS_ALLOW",
        "REQUIRE_ATTESTATION",
        "ALWAYS_DENY",
    ]
    requireAttestationsBy: _list[str]

@typing.type_check_only
class AdmissionWhitelistPattern(typing.TypedDict, total=False):
    namePattern: str

@typing.type_check_only
class AllowlistResult(typing.TypedDict, total=False):
    matchedPattern: str

@typing.type_check_only
class AttestationAuthenticator(typing.TypedDict, total=False):
    displayName: str
    pkixPublicKeySet: PkixPublicKeySet

@typing.type_check_only
class AttestationOccurrence(typing.TypedDict, total=False):
    jwts: _list[Jwt]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class AttestationSource(typing.TypedDict, total=False):
    containerAnalysisAttestationProjects: _list[str]

@typing.type_check_only
class Attestor(typing.TypedDict, total=False):
    description: str
    etag: str
    name: str
    updateTime: str
    userOwnedGrafeasNote: UserOwnedGrafeasNote

@typing.type_check_only
class AttestorPublicKey(typing.TypedDict, total=False):
    asciiArmoredPgpPublicKey: str
    comment: str
    id: str
    pkixPublicKey: PkixPublicKey

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Check(typing.TypedDict, total=False):
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
class CheckResult(typing.TypedDict, total=False):
    allowlistResult: AllowlistResult
    displayName: str
    evaluationResult: EvaluationResult
    explanation: str
    index: str
    type: str

@typing.type_check_only
class CheckResults(typing.TypedDict, total=False):
    results: _list[CheckResult]

@typing.type_check_only
class CheckSet(typing.TypedDict, total=False):
    checks: _list[Check]
    displayName: str
    imageAllowlist: ImageAllowlist
    scope: Scope

@typing.type_check_only
class CheckSetResult(typing.TypedDict, total=False):
    allowlistResult: AllowlistResult
    checkResults: CheckResults
    displayName: str
    explanation: str
    index: str
    scope: Scope

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EvaluateGkePolicyRequest(typing.TypedDict, total=False):
    resource: dict[str, typing.Any]

@typing.type_check_only
class EvaluateGkePolicyResponse(typing.TypedDict, total=False):
    results: _list[PodResult]
    verdict: typing.Literal[
        "VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class EvaluationResult(typing.TypedDict, total=False):
    verdict: typing.Literal[
        "CHECK_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GkePolicy(typing.TypedDict, total=False):
    checkSets: _list[CheckSet]
    imageAllowlist: ImageAllowlist

@typing.type_check_only
class IamPolicy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ImageAllowlist(typing.TypedDict, total=False):
    allowPattern: _list[str]

@typing.type_check_only
class ImageFreshnessCheck(typing.TypedDict, total=False):
    maxUploadAgeDays: int

@typing.type_check_only
class ImageResult(typing.TypedDict, total=False):
    allowlistResult: AllowlistResult
    checkSetResult: CheckSetResult
    explanation: str
    imageUri: str
    verdict: typing.Literal[
        "IMAGE_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Jwt(typing.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class ListAttestorsResponse(typing.TypedDict, total=False):
    attestors: _list[Attestor]
    nextPageToken: str

@typing.type_check_only
class ListPlatformPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    platformPolicies: _list[PlatformPolicy]

@typing.type_check_only
class PkixPublicKey(typing.TypedDict, total=False):
    keyId: str
    publicKeyPem: str
    signatureAlgorithm: typing.Literal[
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
        "ML_DSA_65",
    ]

@typing.type_check_only
class PkixPublicKeySet(typing.TypedDict, total=False):
    pkixPublicKeys: _list[PkixPublicKey]

@typing.type_check_only
class PlatformPolicy(typing.TypedDict, total=False):
    description: str
    etag: str
    gkePolicy: GkePolicy
    name: str
    updateTime: str

@typing.type_check_only
class PodResult(typing.TypedDict, total=False):
    imageResults: _list[ImageResult]
    kubernetesNamespace: str
    kubernetesServiceAccount: str
    podName: str
    verdict: typing.Literal[
        "POD_VERDICT_UNSPECIFIED", "CONFORMANT", "NON_CONFORMANT", "ERROR"
    ]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    admissionWhitelistPatterns: _list[AdmissionWhitelistPattern]
    clusterAdmissionRules: dict[str, typing.Any]
    defaultAdmissionRule: AdmissionRule
    description: str
    etag: str
    globalPolicyEvaluationMode: typing.Literal[
        "GLOBAL_POLICY_EVALUATION_MODE_UNSPECIFIED", "ENABLE", "DISABLE"
    ]
    istioServiceIdentityAdmissionRules: dict[str, typing.Any]
    kubernetesNamespaceAdmissionRules: dict[str, typing.Any]
    kubernetesServiceAccountAdmissionRules: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class Scope(typing.TypedDict, total=False):
    kubernetesNamespace: str
    kubernetesServiceAccount: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: IamPolicy

@typing.type_check_only
class Signature(typing.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SigstoreAuthority(typing.TypedDict, total=False):
    displayName: str
    publicKeySet: SigstorePublicKeySet

@typing.type_check_only
class SigstorePublicKey(typing.TypedDict, total=False):
    publicKeyPem: str

@typing.type_check_only
class SigstorePublicKeySet(typing.TypedDict, total=False):
    publicKeys: _list[SigstorePublicKey]

@typing.type_check_only
class SigstoreSignatureCheck(typing.TypedDict, total=False):
    sigstoreAuthorities: _list[SigstoreAuthority]

@typing.type_check_only
class SimpleSigningAttestationCheck(typing.TypedDict, total=False):
    attestationAuthenticators: _list[AttestationAuthenticator]
    containerAnalysisAttestationProjects: _list[str]

@typing.type_check_only
class SlsaCheck(typing.TypedDict, total=False):
    rules: _list[VerificationRule]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrustedDirectoryCheck(typing.TypedDict, total=False):
    trustedDirPatterns: _list[str]

@typing.type_check_only
class UserOwnedGrafeasNote(typing.TypedDict, total=False):
    delegationServiceAccountEmail: str
    noteReference: str
    publicKeys: _list[AttestorPublicKey]

@typing.type_check_only
class ValidateAttestationOccurrenceRequest(typing.TypedDict, total=False):
    attestation: AttestationOccurrence
    occurrenceNote: str
    occurrenceResourceUri: str

@typing.type_check_only
class ValidateAttestationOccurrenceResponse(typing.TypedDict, total=False):
    denialReason: str
    result: typing.Literal[
        "RESULT_UNSPECIFIED", "VERIFIED", "ATTESTATION_NOT_VERIFIABLE"
    ]

@typing.type_check_only
class VerificationRule(typing.TypedDict, total=False):
    attestationSource: AttestationSource
    configBasedBuildRequired: bool
    customConstraints: str
    trustedBuilder: typing.Literal["BUILDER_UNSPECIFIED", "GOOGLE_CLOUD_BUILD"]
    trustedSourceRepoPatterns: _list[str]

@typing.type_check_only
class VulnerabilityCheck(typing.TypedDict, total=False):
    allowedCves: _list[str]
    blockedCves: _list[str]
    containerAnalysisVulnerabilityProjects: _list[str]
    maximumFixableSeverity: typing.Literal[
        "MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED",
        "BLOCK_ALL",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "ALLOW_ALL",
    ]
    maximumUnfixableSeverity: typing.Literal[
        "MAXIMUM_ALLOWED_SEVERITY_UNSPECIFIED",
        "BLOCK_ALL",
        "MINIMAL",
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "ALLOW_ALL",
    ]
