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
class AnalyzePackagesMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesMetadataV1(typing_extensions.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesRequestV1(typing_extensions.TypedDict, total=False):
    includeOsvData: bool
    packages: _list[PackageData]
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesResponse(typing_extensions.TypedDict, total=False):
    scan: str

@typing.type_check_only
class AnalyzePackagesResponseV1(typing_extensions.TypedDict, total=False):
    scan: str

@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    id: str
    names: _list[str]

@typing.type_check_only
class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    jwts: _list[Jwt]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class BinarySourceInfo(typing_extensions.TypedDict, total=False):
    binaryVersion: PackageVersion
    sourceVersion: PackageVersion

@typing.type_check_only
class BuildDefinition(typing_extensions.TypedDict, total=False):
    buildType: str
    externalParameters: dict[str, typing.Any]
    internalParameters: dict[str, typing.Any]
    resolvedDependencies: _list[ResourceDescriptor]

@typing.type_check_only
class BuildMetadata(typing_extensions.TypedDict, total=False):
    finishedOn: str
    invocationId: str
    startedOn: str

@typing.type_check_only
class BuildOccurrence(typing_extensions.TypedDict, total=False):
    inTotoSlsaProvenanceV1: InTotoSlsaProvenanceV1
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
        "ATTACK_COMPLEXITY_MEDIUM",
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
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    baseScore: float
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
    ]
    exploitabilityScore: float
    impactScore: float
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED",
        "IMPACT_HIGH",
        "IMPACT_LOW",
        "IMPACT_NONE",
        "IMPACT_PARTIAL",
        "IMPACT_COMPLETE",
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
class ComplianceOccurrence(typing_extensions.TypedDict, total=False):
    nonComplianceReason: str
    nonCompliantFiles: _list[NonCompliantFile]
    version: ComplianceVersion

@typing.type_check_only
class ComplianceVersion(typing_extensions.TypedDict, total=False):
    benchmarkDocument: str
    cpeUri: str
    version: str

@typing.type_check_only
class DSSEAttestationOccurrence(typing_extensions.TypedDict, total=False):
    envelope: Envelope
    statement: InTotoStatement

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
    sbomStatus: SBOMStatus

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
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class FileLocation(typing_extensions.TypedDict, total=False):
    filePath: str

@typing.type_check_only
class Fingerprint(typing_extensions.TypedDict, total=False):
    v1Name: str
    v2Blob: _list[str]
    v2Name: str

@typing.type_check_only
class GerritSourceContext(typing_extensions.TypedDict, total=False):
    aliasContext: AliasContext
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GitSourceContext(typing_extensions.TypedDict, total=False):
    revisionId: str
    url: str

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
class Identity(typing_extensions.TypedDict, total=False):
    revision: int
    updateId: str

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
class InTotoSlsaProvenanceV1(typing_extensions.TypedDict, total=False):
    _type: str
    predicate: SlsaProvenanceV1
    predicateType: str
    subject: _list[Subject]

@typing.type_check_only
class InTotoStatement(typing_extensions.TypedDict, total=False):
    _type: str
    predicateType: str
    provenance: InTotoProvenance
    slsaProvenance: SlsaProvenance
    slsaProvenanceZeroTwo: SlsaProvenanceZeroTwo
    subject: _list[Subject]

@typing.type_check_only
class Justification(typing_extensions.TypedDict, total=False):
    details: str
    justificationType: typing_extensions.Literal[
        "JUSTIFICATION_TYPE_UNSPECIFIED",
        "COMPONENT_NOT_PRESENT",
        "VULNERABLE_CODE_NOT_PRESENT",
        "VULNERABLE_CODE_NOT_IN_EXECUTE_PATH",
        "VULNERABLE_CODE_CANNOT_BE_CONTROLLED_BY_ADVERSARY",
        "INLINE_MITIGATIONS_ALREADY_EXIST",
    ]

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class LanguagePackageDependency(typing_extensions.TypedDict, total=False):
    package: str
    version: str

@typing.type_check_only
class Layer(typing_extensions.TypedDict, total=False):
    arguments: str
    directive: str

@typing.type_check_only
class License(typing_extensions.TypedDict, total=False):
    comments: str
    expression: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListVulnerabilitiesResponseV1(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

@typing.type_check_only
class Maintainer(typing_extensions.TypedDict, total=False):
    email: str
    kind: str
    name: str
    url: str

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
        "VULNERABILITY_ASSESSMENT",
        "SBOM_REFERENCE",
    ]
    name: str
    noteName: str
    package: PackageOccurrence
    remediation: str
    resourceUri: str
    sbomReference: SBOMReferenceOccurrence
    updateTime: str
    upgrade: UpgradeOccurrence
    vulnerability: VulnerabilityOccurrence

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PackageData(typing_extensions.TypedDict, total=False):
    architecture: str
    binarySourceInfo: _list[BinarySourceInfo]
    binaryVersion: PackageVersion
    cpeUri: str
    dependencyChain: _list[LanguagePackageDependency]
    fileLocation: _list[FileLocation]
    hashDigest: str
    licenses: _list[str]
    maintainer: Maintainer
    os: str
    osVersion: str
    package: str
    packageType: typing_extensions.Literal[
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
class PackageOccurrence(typing_extensions.TypedDict, total=False):
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    license: License
    location: _list[Location]
    name: str
    packageType: str
    version: Version

@typing.type_check_only
class PackageVersion(typing_extensions.TypedDict, total=False):
    licenses: _list[str]
    name: str
    version: str

@typing.type_check_only
class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class ProvenanceBuilder(typing_extensions.TypedDict, total=False):
    builderDependencies: _list[ResourceDescriptor]
    id: str
    version: dict[str, typing.Any]

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
class Remediation(typing_extensions.TypedDict, total=False):
    details: str
    remediationType: typing_extensions.Literal[
        "REMEDIATION_TYPE_UNSPECIFIED",
        "MITIGATION",
        "NO_FIX_PLANNED",
        "NONE_AVAILABLE",
        "VENDOR_FIX",
        "WORKAROUND",
    ]
    remediationUri: RelatedUrl

@typing.type_check_only
class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class ResourceDescriptor(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    content: str
    digest: dict[str, typing.Any]
    downloadLocation: str
    mediaType: str
    name: str
    uri: str

@typing.type_check_only
class RunDetails(typing_extensions.TypedDict, total=False):
    builder: ProvenanceBuilder
    byproducts: _list[ResourceDescriptor]
    metadata: BuildMetadata

@typing.type_check_only
class SBOMReferenceOccurrence(typing_extensions.TypedDict, total=False):
    payload: SbomReferenceIntotoPayload
    payloadType: str
    signatures: _list[EnvelopeSignature]

@typing.type_check_only
class SBOMStatus(typing_extensions.TypedDict, total=False):
    error: str
    sbomState: typing_extensions.Literal[
        "SBOM_STATE_UNSPECIFIED", "PENDING", "COMPLETE"
    ]

@typing.type_check_only
class SbomReferenceIntotoPayload(typing_extensions.TypedDict, total=False):
    _type: str
    predicate: SbomReferenceIntotoPredicate
    predicateType: str
    subject: _list[Subject]

@typing.type_check_only
class SbomReferenceIntotoPredicate(typing_extensions.TypedDict, total=False):
    digest: dict[str, typing.Any]
    location: str
    mimeType: str
    referrerId: str

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
class SlsaProvenanceV1(typing_extensions.TypedDict, total=False):
    buildDefinition: BuildDefinition
    runDetails: RunDetails

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
class UpgradeDistribution(typing_extensions.TypedDict, total=False):
    classification: str
    cpeUri: str
    cve: _list[str]
    severity: str

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
class VexAssessment(typing_extensions.TypedDict, total=False):
    cve: str
    impacts: _list[str]
    justification: Justification
    noteName: str
    relatedUris: _list[RelatedUrl]
    remediations: _list[Remediation]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "AFFECTED", "NOT_AFFECTED", "FIXED", "UNDER_INVESTIGATION"
    ]
    vulnerabilityId: str

@typing.type_check_only
class VulnerabilityOccurrence(typing_extensions.TypedDict, total=False):
    cvssScore: float
    cvssV2: CVSS
    cvssVersion: typing_extensions.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3"
    ]
    cvssv3: CVSS
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    extraDetails: str
    fixAvailable: bool
    longDescription: str
    packageIssue: _list[PackageIssue]
    relatedUrls: _list[RelatedUrl]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str
    vexAssessment: VexAssessment

@typing.type_check_only
class WindowsUpdate(typing_extensions.TypedDict, total=False):
    categories: _list[Category]
    description: str
    identity: Identity
    kbArticleIds: _list[str]
    lastPublishedTimestamp: str
    supportUrl: str
    title: str
