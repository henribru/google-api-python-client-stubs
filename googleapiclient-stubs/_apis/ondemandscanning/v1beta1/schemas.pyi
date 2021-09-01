import typing

import typing_extensions

@typing.type_check_only
class AliasContext(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class AnalyzePackagesMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesMetadataV1(typing_extensions.TypedDict, total=False):
    createTime: str
    resourceUri: str

@typing.type_check_only
class AnalyzePackagesRequest(typing_extensions.TypedDict, total=False):
    packages: typing.List[PackageData]
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
    names: typing.List[str]

@typing.type_check_only
class AttestationOccurrence(typing_extensions.TypedDict, total=False):
    jwts: typing.List[Jwt]
    serializedPayload: str
    signatures: typing.List[Signature]

@typing.type_check_only
class BuildOccurrence(typing_extensions.TypedDict, total=False):
    intotoProvenance: InTotoProvenance
    provenance: BuildProvenance
    provenanceBytes: str

@typing.type_check_only
class BuildProvenance(typing_extensions.TypedDict, total=False):
    buildOptions: typing.Dict[str, typing.Any]
    builderVersion: str
    builtArtifacts: typing.List[Artifact]
    commands: typing.List[Command]
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
    args: typing.List[str]
    dir: str
    env: typing.List[str]
    id: str
    name: str
    waitFor: typing.List[str]

@typing.type_check_only
class Completeness(typing_extensions.TypedDict, total=False):
    arguments: bool
    environment: bool
    materials: bool

@typing.type_check_only
class ComplianceOccurrence(typing_extensions.TypedDict, total=False):
    nonComplianceReason: str
    nonCompliantFiles: typing.List[NonCompliantFile]

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
    resourceUri: typing.List[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class DiscoveryOccurrence(typing_extensions.TypedDict, total=False):
    analysisStatus: typing_extensions.Literal[
        "ANALYSIS_STATUS_UNSPECIFIED",
        "PENDING",
        "SCANNING",
        "FINISHED_SUCCESS",
        "FINISHED_FAILED",
        "FINISHED_UNSUPPORTED",
    ]
    analysisStatusError: Status
    continuousAnalysis: typing_extensions.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    cpe: str
    lastScanTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Envelope(typing_extensions.TypedDict, total=False):
    payload: str
    payloadType: str
    signatures: typing.List[EnvelopeSignature]

@typing.type_check_only
class EnvelopeSignature(typing_extensions.TypedDict, total=False):
    keyid: str
    sig: str

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

@typing.type_check_only
class Fingerprint(typing_extensions.TypedDict, total=False):
    v1Name: str
    v2Blob: typing.List[str]
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
    layerInfo: typing.List[Layer]

@typing.type_check_only
class InTotoProvenance(typing_extensions.TypedDict, total=False):
    builderConfig: BuilderConfig
    materials: typing.List[str]
    metadata: Metadata
    recipe: Recipe

@typing.type_check_only
class InTotoStatement(typing_extensions.TypedDict, total=False):
    predicateType: str
    provenance: InTotoProvenance
    subject: typing.List[Subject]
    type: str

@typing.type_check_only
class Jwt(typing_extensions.TypedDict, total=False):
    compactJwt: str

@typing.type_check_only
class Layer(typing_extensions.TypedDict, total=False):
    arguments: str
    directive: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListVulnerabilitiesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: typing.List[Occurrence]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

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
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class PackageData(typing_extensions.TypedDict, total=False):
    cpeUri: str
    os: str
    osVersion: str
    package: str
    packageType: typing_extensions.Literal[
        "PACKAGE_TYPE_UNSPECIFIED", "OS", "MAVEN", "GO", "GO_STDLIB"
    ]
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
    fixAvailable: bool
    fixedCpeUri: str
    fixedPackage: str
    fixedVersion: Version
    packageType: str

@typing.type_check_only
class PackageOccurrence(typing_extensions.TypedDict, total=False):
    location: typing.List[Location]
    name: str

@typing.type_check_only
class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class Recipe(typing_extensions.TypedDict, total=False):
    arguments: typing.List[typing.Dict[str, typing.Any]]
    definedInMaterial: str
    entryPoint: str
    environment: typing.List[typing.Dict[str, typing.Any]]
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
class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    additionalContexts: typing.List[SourceContext]
    artifactStorageSourceUri: str
    context: SourceContext
    fileHashes: typing.Dict[str, typing.Any]

@typing.type_check_only
class SourceContext(typing_extensions.TypedDict, total=False):
    cloudRepo: CloudRepoSourceContext
    gerrit: GerritSourceContext
    git: GitSourceContext
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subject(typing_extensions.TypedDict, total=False):
    digest: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class UpgradeDistribution(typing_extensions.TypedDict, total=False):
    classification: str
    cpeUri: str
    cve: typing.List[str]
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
class VulnerabilityOccurrence(typing_extensions.TypedDict, total=False):
    cvssScore: float
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fixAvailable: bool
    longDescription: str
    packageIssue: typing.List[PackageIssue]
    relatedUrls: typing.List[RelatedUrl]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str

@typing.type_check_only
class WindowsUpdate(typing_extensions.TypedDict, total=False):
    categories: typing.List[Category]
    description: str
    identity: Identity
    kbArticleIds: typing.List[str]
    lastPublishedTimestamp: str
    supportUrl: str
    title: str
