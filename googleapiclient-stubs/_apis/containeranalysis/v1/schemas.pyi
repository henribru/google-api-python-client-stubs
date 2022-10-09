import typing

import typing_extensions

_list = list

@typing.type_check_only
class AliasContext(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class AnalysisCompleted(typing_extensions.TypedDict, total=False):
    analysisType: _list[str]

@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    id: str
    names: _list[str]

@typing.type_check_only
class AttestationNote(typing_extensions.TypedDict, total=False):
    hint: Hint

@typing.type_check_only
class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    jwts: _list[Jwt]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class BatchCreateNotesRequest(typing_extensions.TypedDict, total=False):
    notes: dict[str, typing.Any]

@typing.type_check_only
class BatchCreateNotesResponse(typing_extensions.TypedDict, total=False):
    notes: _list[Note]

@typing.type_check_only
class BatchCreateOccurrencesRequest(typing_extensions.TypedDict, total=False):
    occurrences: _list[Occurrence]

@typing.type_check_only
class BatchCreateOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: _list[Occurrence]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BuildNote(typing_extensions.TypedDict, total=False):
    builderVersion: str

@typing.type_check_only
class BuildOccurrence(typing_extensions.TypedDict, total=False):
    intotoProvenance: InTotoProvenance
    intotoStatement: InTotoStatement
    provenance: BuildProvenance
    provenanceBytes: str

@typing.type_check_only
class BuildProvenance(typing_extensions.TypedDict, total=False):
    buildOptions: dict[str, typing.Any]
    builderVersion: str
    builtArtifacts: _list[Artifact]
    commands: _list[Command]
    createTime: str
    creator: str
    endTime: str
    id: str
    logsUri: str
    projectId: str
    sourceProvenance: Source
    startTime: str
    triggerId: str

@typing.type_check_only
class BuilderConfig(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class CVSS(typing_extensions.TypedDict, total=False):
    attackComplexity: typing_extensions.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    authentication: typing_extensions.Literal[
        "AUTHENTICATION_UNSPECIFIED",
        "AUTHENTICATION_MULTIPLE",
        "AUTHENTICATION_SINGLE",
        "AUTHENTICATION_NONE",
    ]
    availabilityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    exploitabilityScore: float
    impactScore: float
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing_extensions.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"
    ]
    userInteraction: typing_extensions.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class CVSSv3(typing_extensions.TypedDict, total=False):
    attackComplexity: typing_extensions.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    exploitabilityScore: float
    impactScore: float
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing_extensions.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"
    ]
    userInteraction: typing_extensions.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

@typing.type_check_only
class Category(typing_extensions.TypedDict, total=False):
    categoryId: str
    name: str

@typing.type_check_only
class CisBenchmark(typing_extensions.TypedDict, total=False):
    profileLevel: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class CloudRepoSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    repoId: RepoId
    revisionId: str

@typing.type_check_only
class Command(typing_extensions.TypedDict, total=False):
    args: _list[str]
    dir: str
    env: _list[str]
    id: str
    name: str
    waitFor: _list[str]

@typing.type_check_only
class Completeness(typing_extensions.TypedDict, total=False):
    arguments: bool
    environment: bool
    materials: bool

@typing.type_check_only
class ComplianceNote(typing_extensions.TypedDict, total=False):
    cisBenchmark: CisBenchmark
    description: str
    rationale: str
    remediation: str
    scanInstructions: str
    title: str
    version: _list[ComplianceVersion]

@typing.type_check_only
class ComplianceOccurrence(typing_extensions.TypedDict, total=False):
    nonComplianceReason: str
    nonCompliantFiles: _list[NonCompliantFile]

@typing.type_check_only
class ComplianceVersion(typing_extensions.TypedDict, total=False):
    benchmarkDocument: str
    cpeUri: str
    version: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig(
    typing_extensions.TypedDict, total=False
):
    approvalRequired: bool

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult(
    typing_extensions.TypedDict, total=False
):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing_extensions.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Artifacts(
    typing_extensions.TypedDict, total=False
):
    images: _list[str]
    objects: ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects(
    typing_extensions.TypedDict, total=False
):
    location: str
    paths: _list[str]
    timing: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Build(
    typing_extensions.TypedDict, total=False
):
    approval: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApproval
    artifacts: ContaineranalysisGoogleDevtoolsCloudbuildV1Artifacts
    availableSecrets: ContaineranalysisGoogleDevtoolsCloudbuildV1Secrets
    buildTriggerId: str
    createTime: str
    failureInfo: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfo
    finishTime: str
    id: str
    images: _list[str]
    logUrl: str
    logsBucket: str
    name: str
    options: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptions
    projectId: str
    queueTtl: str
    results: ContaineranalysisGoogleDevtoolsCloudbuildV1Results
    secrets: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Secret]
    serviceAccount: str
    source: ContaineranalysisGoogleDevtoolsCloudbuildV1Source
    sourceProvenance: ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenance
    startTime: str
    status: typing_extensions.Literal[
        "STATUS_UNKNOWN",
        "PENDING",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]
    statusDetail: str
    steps: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStep]
    substitutions: dict[str, typing.Any]
    tags: _list[str]
    timeout: str
    timing: dict[str, typing.Any]
    warnings: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarning]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApproval(
    typing_extensions.TypedDict, total=False
):
    config: ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig
    result: ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfo(
    typing_extensions.TypedDict, total=False
):
    detail: str
    type: typing_extensions.Literal[
        "FAILURE_TYPE_UNSPECIFIED",
        "PUSH_FAILED",
        "PUSH_IMAGE_NOT_FOUND",
        "PUSH_NOT_AUTHORIZED",
        "LOGGING_FAILURE",
        "USER_BUILD_STEP",
        "FETCH_SOURCE_FAILED",
    ]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptions(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: str
    dynamicSubstitutions: bool
    env: _list[str]
    logStreamingOption: typing_extensions.Literal[
        "STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"
    ]
    logging: typing_extensions.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]
    machineType: typing_extensions.Literal[
        "UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"
    ]
    pool: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption
    requestedVerifyOption: typing_extensions.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[str]
    substitutionOption: typing_extensions.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Volume]
    workerPool: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption(
    typing_extensions.TypedDict, total=False
):
    name: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStep(
    typing_extensions.TypedDict, total=False
):
    allowExitCodes: _list[int]
    allowFailure: bool
    args: _list[str]
    dir: str
    entrypoint: str
    env: _list[str]
    exitCode: int
    id: str
    name: str
    pullTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    script: str
    secretEnv: _list[str]
    status: typing_extensions.Literal[
        "STATUS_UNKNOWN",
        "PENDING",
        "QUEUED",
        "WORKING",
        "SUCCESS",
        "FAILURE",
        "INTERNAL_ERROR",
        "TIMEOUT",
        "CANCELLED",
        "EXPIRED",
    ]
    timeout: str
    timing: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    volumes: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Volume]
    waitFor: _list[str]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarning(
    typing_extensions.TypedDict, total=False
):
    priority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"
    ]
    text: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage(
    typing_extensions.TypedDict, total=False
):
    digest: str
    name: str
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes(
    typing_extensions.TypedDict, total=False
):
    fileHash: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Hash]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Hash(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["NONE", "SHA256", "MD5"]
    value: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecret(
    typing_extensions.TypedDict, total=False
):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource(
    typing_extensions.TypedDict, total=False
):
    branchName: str
    commitSha: str
    dir: str
    invertRegex: bool
    projectId: str
    repoName: str
    substitutions: dict[str, typing.Any]
    tagName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Results(
    typing_extensions.TypedDict, total=False
):
    artifactManifest: str
    artifactTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    images: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage]
    numArtifacts: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Secret(
    typing_extensions.TypedDict, total=False
):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecret(
    typing_extensions.TypedDict, total=False
):
    env: str
    versionName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Secrets(
    typing_extensions.TypedDict, total=False
):
    inline: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecret]
    secretManager: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecret]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Source(
    typing_extensions.TypedDict, total=False
):
    repoSource: ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource
    storageSource: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource
    storageSourceManifest: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenance(
    typing_extensions.TypedDict, total=False
):
    fileHashes: dict[str, typing.Any]
    resolvedRepoSource: ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource
    resolvedStorageSource: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource
    resolvedStorageSourceManifest: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource(
    typing_extensions.TypedDict, total=False
):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest(
    typing_extensions.TypedDict, total=False
):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Volume(
    typing_extensions.TypedDict, total=False
):
    name: str
    path: str

@typing.type_check_only
class DSSEAttestationNote(typing_extensions.TypedDict, total=False):
    hint: DSSEHint

@typing.type_check_only
class DSSEAttestationOccurrence(typing_extensions.TypedDict, total=False):
    envelope: Envelope
    statement: InTotoStatement

@typing.type_check_only
class DSSEHint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

@typing.type_check_only
class DeploymentNote(typing_extensions.TypedDict, total=False):
    resourceUri: _list[str]

@typing.type_check_only
class DeploymentOccurrence(typing_extensions.TypedDict, total=False):
    address: str
    config: str
    deployTime: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    resourceUri: _list[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class Detail(typing_extensions.TypedDict, total=False):
    affectedCpeUri: str
    affectedPackage: str
    affectedVersionEnd: Version
    affectedVersionStart: Version
    description: str
    fixedCpeUri: str
    fixedPackage: str
    fixedVersion: Version
    isObsolete: bool
    packageType: str
    severityName: str
    source: str
    sourceUpdateTime: str
    vendor: str

@typing.type_check_only
class Digest(typing_extensions.TypedDict, total=False):
    algo: str
    digestBytes: str

@typing.type_check_only
class DiscoveryNote(typing_extensions.TypedDict, total=False):
    analysisKind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "UPGRADE",
        "COMPLIANCE",
        "DSSE_ATTESTATION",
    ]

@typing.type_check_only
class DiscoveryOccurrence(typing_extensions.TypedDict, total=False):
    analysisCompleted: AnalysisCompleted
    analysisError: _list[Status]
    analysisStatus: typing_extensions.Literal[
        "ANALYSIS_STATUS_UNSPECIFIED",
        "PENDING",
        "SCANNING",
        "FINISHED_SUCCESS",
        "COMPLETE",
        "FINISHED_FAILED",
        "FINISHED_UNSUPPORTED",
    ]
    analysisStatusError: Status
    archiveTime: str
    continuousAnalysis: typing_extensions.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    cpe: str
    lastScanTime: str

@typing.type_check_only
class Distribution(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    description: str
    latestVersion: Version
    maintainer: str
    url: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Envelope(typing_extensions.TypedDict, total=False):
    payload: str
    payloadType: str
    signatures: _list[EnvelopeSignature]

@typing.type_check_only
class EnvelopeSignature(typing_extensions.TypedDict, total=False):
    keyid: str
    sig: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class Fingerprint(typing_extensions.TypedDict, total=False):
    v1Name: str
    v2Blob: _list[str]
    v2Name: str

@typing.type_check_only
class FixableTotalByDigest(typing_extensions.TypedDict, total=False):
    fixableCount: str
    resourceUri: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    totalCount: str

@typing.type_check_only
class GerritSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GitSourceContext(typing_extensions.TypedDict, total=False):
    revisionId: str
    url: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str

@typing.type_check_only
class GrafeasV1FileLocation(typing_extensions.TypedDict, total=False):
    filePath: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaBuilder(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaCompleteness(
    typing_extensions.TypedDict, total=False
):
    environment: bool
    materials: bool
    parameters: bool

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSource(
    typing_extensions.TypedDict, total=False
):
    digest: dict[str, typing.Any]
    entryPoint: str
    uri: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaInvocation(
    typing_extensions.TypedDict, total=False
):
    configSource: GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSource
    environment: dict[str, typing.Any]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaMaterial(
    typing_extensions.TypedDict, total=False
):
    digest: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaMetadata(
    typing_extensions.TypedDict, total=False
):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: GrafeasV1SlsaProvenanceZeroTwoSlsaCompleteness
    reproducible: bool

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class Hint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

@typing.type_check_only
class Identity(typing_extensions.TypedDict, total=False):
    revision: int
    updateId: str

@typing.type_check_only
class ImageNote(typing_extensions.TypedDict, total=False):
    fingerprint: Fingerprint
    resourceUrl: str

@typing.type_check_only
class ImageOccurrence(typing_extensions.TypedDict, total=False):
    baseResourceUrl: str
    distance: int
    fingerprint: Fingerprint
    layerInfo: _list[Layer]

@typing.type_check_only
class InTotoProvenance(typing_extensions.TypedDict, total=False):
    builderConfig: BuilderConfig
    materials: _list[str]
    metadata: Metadata
    recipe: Recipe

@typing.type_check_only
class InTotoStatement(typing_extensions.TypedDict, total=False):
    _type: str
    predicateType: str
    provenance: InTotoProvenance
    slsaProvenance: SlsaProvenance
    slsaProvenanceZeroTwo: SlsaProvenanceZeroTwo
    subject: _list[Subject]

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class KnowledgeBase(typing_extensions.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class Layer(typing_extensions.TypedDict, total=False):
    arguments: str
    directive: str

@typing.type_check_only
class License(typing_extensions.TypedDict, total=False):
    comments: str
    expression: str

@typing.type_check_only
class ListNoteOccurrencesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]

@typing.type_check_only
class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: _list[Note]

@typing.type_check_only
class ListOccurrencesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

@typing.type_check_only
class Material(typing_extensions.TypedDict, total=False):
    digest: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: Completeness
    reproducible: bool

@typing.type_check_only
class NonCompliantFile(typing_extensions.TypedDict, total=False):
    displayCommand: str
    path: str
    reason: str

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    attestation: AttestationNote
    build: BuildNote
    compliance: ComplianceNote
    createTime: str
    deployment: DeploymentNote
    discovery: DiscoveryNote
    dsseAttestation: DSSEAttestationNote
    expirationTime: str
    image: ImageNote
    kind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "UPGRADE",
        "COMPLIANCE",
        "DSSE_ATTESTATION",
    ]
    longDescription: str
    name: str
    package: PackageNote
    relatedNoteNames: _list[str]
    relatedUrl: _list[RelatedUrl]
    shortDescription: str
    updateTime: str
    upgrade: UpgradeNote
    vulnerability: VulnerabilityNote

@typing.type_check_only
class Occurrence(typing_extensions.TypedDict, total=False):
    attestation: AttestationOccurrence
    build: BuildOccurrence
    compliance: ComplianceOccurrence
    createTime: str
    deployment: DeploymentOccurrence
    discovery: DiscoveryOccurrence
    dsseAttestation: DSSEAttestationOccurrence
    envelope: Envelope
    image: ImageOccurrence
    kind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "UPGRADE",
        "COMPLIANCE",
        "DSSE_ATTESTATION",
    ]
    name: str
    noteName: str
    package: PackageOccurrence
    remediation: str
    resourceUri: str
    updateTime: str
    upgrade: UpgradeOccurrence
    vulnerability: VulnerabilityOccurrence

@typing.type_check_only
class PackageIssue(typing_extensions.TypedDict, total=False):
    affectedCpeUri: str
    affectedPackage: str
    affectedVersion: Version
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fileLocation: _list[GrafeasV1FileLocation]
    fixAvailable: bool
    fixedCpeUri: str
    fixedPackage: str
    fixedVersion: Version
    packageType: str

@typing.type_check_only
class PackageNote(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    description: str
    digest: _list[Digest]
    distribution: _list[Distribution]
    license: License
    maintainer: str
    name: str
    packageType: str
    url: str
    version: Version

@typing.type_check_only
class PackageOccurrence(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    license: License
    location: _list[Location]
    name: str
    packageType: str
    version: Version

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class Recipe(typing_extensions.TypedDict, total=False):
    arguments: _list[dict[str, typing.Any]]
    definedInMaterial: str
    entryPoint: str
    environment: _list[dict[str, typing.Any]]
    type: str

@typing.type_check_only
class RelatedUrl(typing_extensions.TypedDict, total=False):
    label: str
    url: str

@typing.type_check_only
class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SlsaBuilder(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class SlsaCompleteness(typing_extensions.TypedDict, total=False):
    arguments: bool
    environment: bool
    materials: bool

@typing.type_check_only
class SlsaMetadata(typing_extensions.TypedDict, total=False):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: SlsaCompleteness
    reproducible: bool

@typing.type_check_only
class SlsaProvenance(typing_extensions.TypedDict, total=False):
    builder: SlsaBuilder
    materials: _list[Material]
    metadata: SlsaMetadata
    recipe: SlsaRecipe

@typing.type_check_only
class SlsaProvenanceZeroTwo(typing_extensions.TypedDict, total=False):
    buildConfig: dict[str, typing.Any]
    buildType: str
    builder: GrafeasV1SlsaProvenanceZeroTwoSlsaBuilder
    invocation: GrafeasV1SlsaProvenanceZeroTwoSlsaInvocation
    materials: _list[GrafeasV1SlsaProvenanceZeroTwoSlsaMaterial]
    metadata: GrafeasV1SlsaProvenanceZeroTwoSlsaMetadata

@typing.type_check_only
class SlsaRecipe(typing_extensions.TypedDict, total=False):
    arguments: dict[str, typing.Any]
    definedInMaterial: str
    entryPoint: str
    environment: dict[str, typing.Any]
    type: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    additionalContexts: _list[SourceContext]
    artifactStorageSourceUri: str
    context: SourceContext
    fileHashes: dict[str, typing.Any]

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    cloudRepo: CloudRepoSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext
    labels: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    digest: dict[str, typing.Any]
    name: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpgradeDistribution(typing_extensions.TypedDict, total=False):
    classification: str
    cpeUri: str
    cve: _list[str]
    severity: str

@typing.type_check_only
class UpgradeNote(typing_extensions.TypedDict, total=False):
    distributions: _list[UpgradeDistribution]
    package: str
    version: Version
    windowsUpdate: WindowsUpdate

@typing.type_check_only
class UpgradeOccurrence(typing_extensions.TypedDict, total=False):
    distribution: UpgradeDistribution
    package: str
    parsedVersion: Version
    windowsUpdate: WindowsUpdate

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    epoch: int
    fullName: str
    inclusive: bool
    kind: typing_extensions.Literal[
        "VERSION_KIND_UNSPECIFIED", "NORMAL", "MINIMUM", "MAXIMUM"
    ]
    name: str
    revision: str

@typing.type_check_only
class VulnerabilityNote(typing_extensions.TypedDict, total=False):
    cvssScore: float
    cvssV3: CVSSv3
    cvssVersion: typing_extensions.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3"
    ]
    details: _list[Detail]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    sourceUpdateTime: str
    windowsDetails: _list[WindowsDetail]

@typing.type_check_only
class VulnerabilityOccurrence(typing_extensions.TypedDict, total=False):
    cvssScore: float
    cvssVersion: typing_extensions.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3"
    ]
    cvssv3: CVSS
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fixAvailable: bool
    longDescription: str
    packageIssue: _list[PackageIssue]
    relatedUrls: _list[RelatedUrl]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str

@typing.type_check_only
class VulnerabilityOccurrencesSummary(typing_extensions.TypedDict, total=False):
    counts: _list[FixableTotalByDigest]

@typing.type_check_only
class WindowsDetail(typing_extensions.TypedDict, total=False):
    cpeUri: str
    description: str
    fixingKbs: _list[KnowledgeBase]
    name: str

@typing.type_check_only
class WindowsUpdate(typing_extensions.TypedDict, total=False):
    categories: _list[Category]
    description: str
    identity: Identity
    kbArticleIds: _list[str]
    lastPublishedTimestamp: str
    supportUrl: str
    title: str
