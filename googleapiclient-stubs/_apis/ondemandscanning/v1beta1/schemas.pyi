import typing

_list = list

@typing.type_check_only
class AISkillAnalysisOccurrence(typing.TypedDict, total=False):
    findings: _list[Finding]
    maxSeverity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH"]
    perScannerVerdict: PerScannerVerdict
    skillName: str

@typing.type_check_only
class AliasContext(typing.TypedDict, total=False):
    kind: typing.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class AnalysisCompleted(typing.TypedDict, total=False):
    analysisType: _list[str]

@typing.type_check_only
class AnalyzePackagesMetadata(typing.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesMetadataV1(typing.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesRequest(typing.TypedDict, total=False):
    packages: _list[PackageData]
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesResponse(typing.TypedDict, total=False):
    scan: str

@typing.type_check_only
class AnalyzePackagesResponseV1(typing.TypedDict, total=False):
    scan: str

@typing.type_check_only
class Artifact(typing.TypedDict, total=False):
    checksum: str
    id: str
    names: _list[str]

@typing.type_check_only
class AttestationOccurrence(typing.TypedDict, total=False):
    jwts: _list[Jwt]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class BaseImage(typing.TypedDict, total=False):
    layerCount: int
    name: str
    registry: str
    repository: str

@typing.type_check_only
class BinarySourceInfo(typing.TypedDict, total=False):
    binaryVersion: PackageVersion
    sourceVersion: PackageVersion

@typing.type_check_only
class BuildDefinition(typing.TypedDict, total=False):
    buildType: str
    externalParameters: dict[str, typing.Any]
    internalParameters: dict[str, typing.Any]
    resolvedDependencies: _list[ResourceDescriptor]

@typing.type_check_only
class BuildMetadata(typing.TypedDict, total=False):
    finishedOn: str
    invocationId: str
    startedOn: str

@typing.type_check_only
class BuildOccurrence(typing.TypedDict, total=False):
    inTotoSlsaProvenanceV1: InTotoSlsaProvenanceV1
    intotoProvenance: InTotoProvenance
    intotoStatement: InTotoStatement
    provenance: BuildProvenance
    provenanceBytes: str

@typing.type_check_only
class BuildProvenance(typing.TypedDict, total=False):
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
class BuilderConfig(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class CISAKnownExploitedVulnerabilities(typing.TypedDict, total=False):
    knownRansomwareCampaignUse: str

@typing.type_check_only
class CVSS(typing.TypedDict, total=False):
    attackComplexity: typing.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
        "ATTACK_COMPLEXITY_MEDIUM",
    ]
    attackRequirements: typing.Literal[
        "ATTACK_REQUIREMENTS_UNSPECIFIED",
        "ATTACK_REQUIREMENTS_NONE",
        "ATTACK_REQUIREMENTS_PRESENT",
    ]
    attackVector: typing.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    authentication: typing.Literal[
        "AUTHENTICATION_UNSPECIFIED",
        "AUTHENTICATION_MULTIPLE",
        "AUTHENTICATION_SINGLE",
        "AUTHENTICATION_NONE",
    ]
    availabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    baseScore: float
    confidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    exploitMaturity: typing.Literal[
        "EXPLOIT_MATURITY_UNSPECIFIED",
        "EXPLOIT_MATURITY_NOT_DEFINED",
        "EXPLOIT_MATURITY_ATTACKED",
        "EXPLOIT_MATURITY_POC",
        "EXPLOIT_MATURITY_UNREPORTED",
    ]
    exploitabilityScore: float
    impactScore: float
    integrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    privilegesRequired: typing.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing.Literal["SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"]
    subsequentSystemAvailabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    subsequentSystemConfidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    subsequentSystemIntegrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    userInteraction: typing.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
        "USER_INTERACTION_PASSIVE",
        "USER_INTERACTION_ACTIVE",
    ]
    vulnerableSystemAvailabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    vulnerableSystemConfidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    vulnerableSystemIntegrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    categoryId: str
    name: str

@typing.type_check_only
class CloudRepoSourceContext(typing.TypedDict, total=False):
    aliasContext: AliasContext
    repoId: RepoId
    revisionId: str

@typing.type_check_only
class Command(typing.TypedDict, total=False):
    args: _list[str]
    dir: str
    env: _list[str]
    id: str
    name: str
    waitFor: _list[str]

@typing.type_check_only
class Completeness(typing.TypedDict, total=False):
    arguments: bool
    environment: bool
    materials: bool

@typing.type_check_only
class ComplianceOccurrence(typing.TypedDict, total=False):
    nonComplianceReason: str
    nonCompliantFiles: _list[NonCompliantFile]
    version: ComplianceVersion

@typing.type_check_only
class ComplianceVersion(typing.TypedDict, total=False):
    benchmarkDocument: str
    cpeUri: str
    version: str

@typing.type_check_only
class DSSEAttestationOccurrence(typing.TypedDict, total=False):
    envelope: Envelope
    statement: InTotoStatement

@typing.type_check_only
class DeploymentOccurrence(typing.TypedDict, total=False):
    address: str
    config: str
    deployTime: str
    platform: typing.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    resourceUri: _list[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class DiscoveryOccurrence(typing.TypedDict, total=False):
    analysisCompleted: AnalysisCompleted
    analysisError: _list[Status]
    analysisStatus: typing.Literal[
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
    continuousAnalysis: typing.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    cpe: str
    files: _list[File]
    lastScanTime: str
    lastVulnerabilityUpdateTime: str
    sbomStatus: SBOMStatus

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Envelope(typing.TypedDict, total=False):
    payload: str
    payloadType: str
    signatures: _list[EnvelopeSignature]

@typing.type_check_only
class EnvelopeSignature(typing.TypedDict, total=False):
    keyid: str
    sig: str

@typing.type_check_only
class ExploitPredictionScoringSystem(typing.TypedDict, total=False):
    percentile: float
    score: float

@typing.type_check_only
class File(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    name: str

@typing.type_check_only
class FileHashes(typing.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class FileLocation(typing.TypedDict, total=False):
    filePath: str
    layerDetails: LayerDetails
    lineNumber: int

@typing.type_check_only
class Finding(typing.TypedDict, total=False):
    category: str
    details: str
    location: FindingLocation
    scanner: typing.Literal[
        "SCANNER_UNSPECIFIED", "STATIC", "LLM", "WS_POLICY", "GOOGLE_ANTIVIRUS"
    ]
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH"]

@typing.type_check_only
class FindingLocation(typing.TypedDict, total=False):
    filePath: str
    lineNumber: str

@typing.type_check_only
class Fingerprint(typing.TypedDict, total=False):
    v1Name: str
    v2Blob: _list[str]
    v2Name: str

@typing.type_check_only
class GerritSourceContext(typing.TypedDict, total=False):
    aliasContext: AliasContext
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GitSourceContext(typing.TypedDict, total=False):
    revisionId: str
    url: str

@typing.type_check_only
class GrafeasV1BaseImage(typing.TypedDict, total=False):
    layerCount: int
    name: str
    registry: str
    repository: str

@typing.type_check_only
class GrafeasV1FileLocation(typing.TypedDict, total=False):
    filePath: str
    layerDetails: GrafeasV1LayerDetails
    lineNumber: int

@typing.type_check_only
class GrafeasV1LayerDetails(typing.TypedDict, total=False):
    baseImages: _list[GrafeasV1BaseImage]
    chainId: str
    command: str
    diffId: str
    index: int

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaBuilder(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaCompleteness(typing.TypedDict, total=False):
    environment: bool
    materials: bool
    parameters: bool

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSource(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    entryPoint: str
    uri: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaInvocation(typing.TypedDict, total=False):
    configSource: GrafeasV1SlsaProvenanceZeroTwoSlsaConfigSource
    environment: dict[str, typing.Any]
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaMaterial(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class GrafeasV1SlsaProvenanceZeroTwoSlsaMetadata(typing.TypedDict, total=False):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: GrafeasV1SlsaProvenanceZeroTwoSlsaCompleteness
    reproducible: bool

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class Identity(typing.TypedDict, total=False):
    revision: int
    updateId: str

@typing.type_check_only
class ImageOccurrence(typing.TypedDict, total=False):
    baseResourceUrl: str
    distance: int
    fingerprint: Fingerprint
    layerInfo: _list[Layer]

@typing.type_check_only
class InTotoProvenance(typing.TypedDict, total=False):
    builderConfig: BuilderConfig
    materials: _list[str]
    metadata: Metadata
    recipe: Recipe

@typing.type_check_only
class InTotoSlsaProvenanceV1(typing.TypedDict, total=False):
    _type: str
    predicate: SlsaProvenanceV1
    predicateType: str
    subject: _list[Subject]

@typing.type_check_only
class InTotoStatement(typing.TypedDict, total=False):
    _type: str
    predicateType: str
    provenance: InTotoProvenance
    slsaProvenance: SlsaProvenance
    slsaProvenanceZeroTwo: SlsaProvenanceZeroTwo
    subject: _list[Subject]

@typing.type_check_only
class IngestionSource(typing.TypedDict, total=False):
    attachmentUri: str
    resourceUrl: str
    source: typing.Literal["SOURCE_UNSPECIFIED", "DOCKER_IMAGE", "SBOM_ATTACHMENT"]

@typing.type_check_only
class Justification(typing.TypedDict, total=False):
    details: str
    justificationType: typing.Literal[
        "JUSTIFICATION_TYPE_UNSPECIFIED",
        "COMPONENT_NOT_PRESENT",
        "VULNERABLE_CODE_NOT_PRESENT",
        "VULNERABLE_CODE_NOT_IN_EXECUTE_PATH",
        "VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY",
        "INLINE_MITIGATIONS_ALREADY_EXIST",
    ]

@typing.type_check_only
class Jwt(typing.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class LanguagePackageDependency(typing.TypedDict, total=False):
    package: str
    version: str

@typing.type_check_only
class Layer(typing.TypedDict, total=False):
    arguments: str
    directive: str

@typing.type_check_only
class LayerDetails(typing.TypedDict, total=False):
    baseImages: _list[BaseImage]
    chainId: str
    command: str
    diffId: str
    index: int

@typing.type_check_only
class License(typing.TypedDict, total=False):
    comments: str
    expression: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListVulnerabilitiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

@typing.type_check_only
class Maintainer(typing.TypedDict, total=False):
    email: str
    kind: str
    name: str
    url: str

@typing.type_check_only
class MaliciousContentLLMResult(typing.TypedDict, total=False):
    maxSeverity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH"]
    scanStatus: typing.Literal["SCAN_STATUS_UNSPECIFIED", "PERFORMED", "NOT_PERFORMED"]

@typing.type_check_only
class MaliciousContentStaticResult(typing.TypedDict, total=False):
    maxSeverity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH"]
    scanStatus: typing.Literal["SCAN_STATUS_UNSPECIFIED", "PERFORMED", "NOT_PERFORMED"]

@typing.type_check_only
class MalwareScanResult(typing.TypedDict, total=False):
    scanStatus: typing.Literal["SCAN_STATUS_UNSPECIFIED", "PERFORMED", "NOT_PERFORMED"]
    verdict: typing.Literal["VERDICT_UNSPECIFIED", "PASSED", "FAILED"]

@typing.type_check_only
class Material(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    uri: str

@typing.type_check_only
class Metadata(typing.TypedDict, total=False):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: Completeness
    reproducible: bool

@typing.type_check_only
class NonCompliantFile(typing.TypedDict, total=False):
    displayCommand: str
    path: str
    reason: str

@typing.type_check_only
class Occurrence(typing.TypedDict, total=False):
    advisoryPublishTime: str
    aiSkillAnalysis: AISkillAnalysisOccurrence
    attestation: AttestationOccurrence
    build: BuildOccurrence
    compliance: ComplianceOccurrence
    createTime: str
    deployment: DeploymentOccurrence
    discovery: DiscoveryOccurrence
    dsseAttestation: DSSEAttestationOccurrence
    envelope: Envelope
    image: ImageOccurrence
    kind: typing.Literal[
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
        "VULNERABILITY_ASSESSMENT",
        "SBOM_REFERENCE",
        "SECRET",
        "AI_SKILL_ANALYSIS",
    ]
    name: str
    noteName: str
    package: PackageOccurrence
    remediation: str
    resourceUri: str
    sbomReference: SBOMReferenceOccurrence
    secret: SecretOccurrence
    updateTime: str
    upgrade: UpgradeOccurrence
    vulnerability: VulnerabilityOccurrence

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PackageData(typing.TypedDict, total=False):
    architecture: str
    binarySourceInfo: _list[BinarySourceInfo]
    binaryVersion: PackageVersion
    cpeUri: str
    dependencyChain: _list[LanguagePackageDependency]
    fileLocation: _list[FileLocation]
    hashDigest: str
    ingestionSources: _list[IngestionSource]
    layerDetails: LayerDetails
    licenses: _list[str]
    maintainer: Maintainer
    os: str
    osVersion: str
    package: str
    packageType: typing.Literal[
        "PACKAGE_TYPE_UNSPECIFIED",
        "OS",
        "MAVEN",
        "GO",
        "GO_STDLIB",
        "PYPI",
        "NPM",
        "NUGET",
        "RUBYGEMS",
        "RUST",
        "COMPOSER",
        "SWIFT",
    ]
    patchedCve: _list[str]
    sourceVersion: PackageVersion
    unused: str
    version: str

@typing.type_check_only
class PackageIssue(typing.TypedDict, total=False):
    affectedCpeUri: str
    affectedPackage: str
    affectedVersion: Version
    effectiveSeverity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fileLocation: _list[GrafeasV1FileLocation]
    fixAvailable: bool
    fixedCpeUri: str
    fixedPackage: str
    fixedVersion: Version
    packageType: str

@typing.type_check_only
class PackageOccurrence(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    license: License
    location: _list[Location]
    name: str
    packageType: str
    version: Version

@typing.type_check_only
class PackageVersion(typing.TypedDict, total=False):
    licenses: _list[str]
    name: str
    version: str

@typing.type_check_only
class PerScannerVerdict(typing.TypedDict, total=False):
    maliciousContentLlmResult: MaliciousContentLLMResult
    maliciousContentStaticResult: MaliciousContentStaticResult
    malwareScan: MalwareScanResult
    workspacePolicy: WorkspacePolicyResult

@typing.type_check_only
class ProjectRepoId(typing.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class ProvenanceBuilder(typing.TypedDict, total=False):
    builderDependencies: _list[ResourceDescriptor]
    id: str
    version: dict[str, typing.Any]

@typing.type_check_only
class Recipe(typing.TypedDict, total=False):
    arguments: _list[dict[str, typing.Any]]
    definedInMaterial: str
    entryPoint: str
    environment: _list[dict[str, typing.Any]]
    type: str

@typing.type_check_only
class RelatedUrl(typing.TypedDict, total=False):
    label: str
    url: str

@typing.type_check_only
class Remediation(typing.TypedDict, total=False):
    details: str
    remediationType: typing.Literal[
        "REMEDIATION_TYPE_UNSPECIFIED",
        "MITIGATION",
        "NO_FIX_PLANNED",
        "NONE_AVAILABLE",
        "VENDOR_FIX",
        "WORKAROUND",
    ]
    remediationUri: RelatedUrl

@typing.type_check_only
class RepoId(typing.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class ResourceDescriptor(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    content: str
    digest: dict[str, typing.Any]
    downloadLocation: str
    mediaType: str
    name: str
    uri: str

@typing.type_check_only
class Risk(typing.TypedDict, total=False):
    cisaKev: CISAKnownExploitedVulnerabilities
    epss: ExploitPredictionScoringSystem

@typing.type_check_only
class RunDetails(typing.TypedDict, total=False):
    builder: ProvenanceBuilder
    byproducts: _list[ResourceDescriptor]
    metadata: BuildMetadata

@typing.type_check_only
class SBOMReferenceOccurrence(typing.TypedDict, total=False):
    payload: SbomReferenceIntotoPayload
    payloadType: str
    signatures: _list[EnvelopeSignature]

@typing.type_check_only
class SBOMStatus(typing.TypedDict, total=False):
    error: str
    sbomState: typing.Literal["SBOM_STATE_UNSPECIFIED", "PENDING", "COMPLETE"]

@typing.type_check_only
class SbomReferenceIntotoPayload(typing.TypedDict, total=False):
    _type: str
    predicate: SbomReferenceIntotoPredicate
    predicateType: str
    subject: _list[Subject]

@typing.type_check_only
class SbomReferenceIntotoPredicate(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    location: str
    mimeType: str
    referrerId: str

@typing.type_check_only
class SecretLocation(typing.TypedDict, total=False):
    fileLocation: GrafeasV1FileLocation

@typing.type_check_only
class SecretOccurrence(typing.TypedDict, total=False):
    kind: typing.Literal[
        "SECRET_KIND_UNSPECIFIED",
        "SECRET_KIND_UNKNOWN",
        "SECRET_KIND_GCP_SERVICE_ACCOUNT_KEY",
        "SECRET_KIND_GCP_API_KEY",
        "SECRET_KIND_GCP_OAUTH2_CLIENT_CREDENTIALS",
        "SECRET_KIND_GCP_OAUTH2_ACCESS_TOKEN",
        "SECRET_KIND_ANTHROPIC_ADMIN_API_KEY",
        "SECRET_KIND_ANTHROPIC_API_KEY",
        "SECRET_KIND_AZURE_ACCESS_TOKEN",
        "SECRET_KIND_AZURE_IDENTITY_TOKEN",
        "SECRET_KIND_DOCKER_HUB_PERSONAL_ACCESS_TOKEN",
        "SECRET_KIND_GITHUB_APP_REFRESH_TOKEN",
        "SECRET_KIND_GITHUB_APP_SERVER_TO_SERVER_TOKEN",
        "SECRET_KIND_GITHUB_APP_USER_TO_SERVER_TOKEN",
        "SECRET_KIND_GITHUB_CLASSIC_PERSONAL_ACCESS_TOKEN",
        "SECRET_KIND_GITHUB_FINE_GRAINED_PERSONAL_ACCESS_TOKEN",
        "SECRET_KIND_GITHUB_OAUTH_TOKEN",
        "SECRET_KIND_HUGGINGFACE_API_KEY",
        "SECRET_KIND_OPENAI_API_KEY",
        "SECRET_KIND_PERPLEXITY_API_KEY",
        "SECRET_KIND_STRIPE_SECRET_KEY",
        "SECRET_KIND_STRIPE_RESTRICTED_KEY",
        "SECRET_KIND_STRIPE_WEBHOOK_SECRET",
    ]
    locations: _list[SecretLocation]
    statuses: _list[SecretStatus]

@typing.type_check_only
class SecretStatus(typing.TypedDict, total=False):
    message: str
    status: typing.Literal["STATUS_UNSPECIFIED", "UNKNOWN", "VALID", "INVALID"]
    updateTime: str

@typing.type_check_only
class Signature(typing.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SlsaBuilder(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class SlsaCompleteness(typing.TypedDict, total=False):
    arguments: bool
    environment: bool
    materials: bool

@typing.type_check_only
class SlsaMetadata(typing.TypedDict, total=False):
    buildFinishedOn: str
    buildInvocationId: str
    buildStartedOn: str
    completeness: SlsaCompleteness
    reproducible: bool

@typing.type_check_only
class SlsaProvenance(typing.TypedDict, total=False):
    builder: SlsaBuilder
    materials: _list[Material]
    metadata: SlsaMetadata
    recipe: SlsaRecipe

@typing.type_check_only
class SlsaProvenanceV1(typing.TypedDict, total=False):
    buildDefinition: BuildDefinition
    runDetails: RunDetails

@typing.type_check_only
class SlsaProvenanceZeroTwo(typing.TypedDict, total=False):
    buildConfig: dict[str, typing.Any]
    buildType: str
    builder: GrafeasV1SlsaProvenanceZeroTwoSlsaBuilder
    invocation: GrafeasV1SlsaProvenanceZeroTwoSlsaInvocation
    materials: _list[GrafeasV1SlsaProvenanceZeroTwoSlsaMaterial]
    metadata: GrafeasV1SlsaProvenanceZeroTwoSlsaMetadata

@typing.type_check_only
class SlsaRecipe(typing.TypedDict, total=False):
    arguments: dict[str, typing.Any]
    definedInMaterial: str
    entryPoint: str
    environment: dict[str, typing.Any]
    type: str

@typing.type_check_only
class Source(typing.TypedDict, total=False):
    additionalContexts: _list[SourceContext]
    artifactStorageSourceUri: str
    context: SourceContext
    fileHashes: dict[str, typing.Any]

@typing.type_check_only
class SourceContext(typing.TypedDict, total=False):
    cloudRepo: CloudRepoSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext
    labels: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    name: str

@typing.type_check_only
class UpgradeDistribution(typing.TypedDict, total=False):
    classification: str
    cpeUri: str
    cve: _list[str]
    severity: str

@typing.type_check_only
class UpgradeOccurrence(typing.TypedDict, total=False):
    distribution: UpgradeDistribution
    package: str
    parsedVersion: Version
    windowsUpdate: WindowsUpdate

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    epoch: int
    fullName: str
    inclusive: bool
    kind: typing.Literal["VERSION_KIND_UNSPECIFIED", "NORMAL", "MINIMUM", "MAXIMUM"]
    name: str
    revision: str

@typing.type_check_only
class VexAssessment(typing.TypedDict, total=False):
    cve: str
    impacts: _list[str]
    justification: Justification
    noteName: str
    relatedUris: _list[RelatedUrl]
    remediations: _list[Remediation]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "AFFECTED", "NOT_AFFECTED", "FIXED", "UNDER_INVESTIGATION"
    ]
    vulnerabilityId: str

@typing.type_check_only
class VulnerabilityOccurrence(typing.TypedDict, total=False):
    cvssScore: float
    cvssV2: CVSS
    cvssV4: CVSS
    cvssVersion: typing.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3", "CVSS_VERSION_4"
    ]
    cvssv3: CVSS
    effectiveSeverity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    extraDetails: str
    fixAvailable: bool
    longDescription: str
    packageIssue: _list[PackageIssue]
    relatedUrls: _list[RelatedUrl]
    risk: Risk
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str
    vexAssessment: VexAssessment

@typing.type_check_only
class WindowsUpdate(typing.TypedDict, total=False):
    categories: _list[Category]
    description: str
    identity: Identity
    kbArticleIds: _list[str]
    lastPublishedTimestamp: str
    supportUrl: str
    title: str

@typing.type_check_only
class WorkspacePolicyResult(typing.TypedDict, total=False):
    scanStatus: typing.Literal["SCAN_STATUS_UNSPECIFIED", "PERFORMED", "NOT_PERFORMED"]
    verdict: typing.Literal["VERDICT_UNSPECIFIED", "PASSED", "FAILED"]
