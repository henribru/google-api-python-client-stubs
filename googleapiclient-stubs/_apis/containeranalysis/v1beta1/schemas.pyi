import typing

import typing_extensions
@typing.type_check_only
class AliasContext(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    id: str
    names: typing.List[str]

@typing.type_check_only
class ArtifactHashes(typing_extensions.TypedDict, total=False):
    sha256: str

@typing.type_check_only
class ArtifactRule(typing_extensions.TypedDict, total=False):
    artifactRule: typing.List[str]

@typing.type_check_only
class Attestation(typing_extensions.TypedDict, total=False):
    genericSignedAttestation: GenericSignedAttestation
    pgpSignedAttestation: PgpSignedAttestation

@typing.type_check_only
class Authority(typing_extensions.TypedDict, total=False):
    hint: Hint

@typing.type_check_only
class Basis(typing_extensions.TypedDict, total=False):
    fingerprint: Fingerprint
    resourceUrl: str

@typing.type_check_only
class BatchCreateNotesRequest(typing_extensions.TypedDict, total=False):
    notes: typing.Dict[str, typing.Any]

@typing.type_check_only
class BatchCreateNotesResponse(typing_extensions.TypedDict, total=False):
    notes: typing.List[Note]

@typing.type_check_only
class BatchCreateOccurrencesRequest(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]

@typing.type_check_only
class BatchCreateOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Build(typing_extensions.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

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
class BuildSignature(typing_extensions.TypedDict, total=False):
    keyId: str
    keyType: typing_extensions.Literal[
        "KEY_TYPE_UNSPECIFIED", "PGP_ASCII_ARMORED", "PKIX_PEM"
    ]
    publicKey: str
    signature: str

@typing.type_check_only
class ByProducts(typing_extensions.TypedDict, total=False):
    customValues: typing.Dict[str, typing.Any]

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
class Deployable(typing_extensions.TypedDict, total=False):
    resourceUri: typing.List[str]

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    address: str
    config: str
    deployTime: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    resourceUri: typing.List[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class Derived(typing_extensions.TypedDict, total=False):
    baseResourceUrl: str
    distance: int
    fingerprint: Fingerprint
    layerInfo: typing.List[Layer]

@typing.type_check_only
class Detail(typing_extensions.TypedDict, total=False):
    cpeUri: str
    description: str
    fixedLocation: VulnerabilityLocation
    isObsolete: bool
    maxAffectedVersion: Version
    minAffectedVersion: Version
    package: str
    packageType: str
    severityName: str
    source: str
    sourceUpdateTime: str

@typing.type_check_only
class Details(typing_extensions.TypedDict, total=False):
    attestation: Attestation

@typing.type_check_only
class Discovered(typing_extensions.TypedDict, total=False):
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
    lastAnalysisTime: str

@typing.type_check_only
class Discovery(typing_extensions.TypedDict, total=False):
    analysisKind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
    ]

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
class Environment(typing_extensions.TypedDict, total=False):
    customValues: typing.Dict[str, typing.Any]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

@typing.type_check_only
class Fingerprint(typing_extensions.TypedDict, total=False):
    v1Name: str
    v2Blob: typing.List[str]
    v2Name: str

@typing.type_check_only
class FixableTotalByDigest(typing_extensions.TypedDict, total=False):
    fixableCount: str
    resource: Resource
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    totalCount: str

@typing.type_check_only
class GenericSignedAttestation(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]
    serializedPayload: str
    signatures: typing.List[Signature]

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
class GrafeasV1beta1BuildDetails(typing_extensions.TypedDict, total=False):
    provenance: BuildProvenance
    provenanceBytes: str

@typing.type_check_only
class GrafeasV1beta1DeploymentDetails(typing_extensions.TypedDict, total=False):
    deployment: Deployment

@typing.type_check_only
class GrafeasV1beta1DiscoveryDetails(typing_extensions.TypedDict, total=False):
    discovered: Discovered

@typing.type_check_only
class GrafeasV1beta1ImageDetails(typing_extensions.TypedDict, total=False):
    derivedImage: Derived

@typing.type_check_only
class GrafeasV1beta1IntotoArtifact(typing_extensions.TypedDict, total=False):
    hashes: ArtifactHashes
    resourceUri: str

@typing.type_check_only
class GrafeasV1beta1IntotoDetails(typing_extensions.TypedDict, total=False):
    signatures: typing.List[GrafeasV1beta1IntotoSignature]
    signed: Link

@typing.type_check_only
class GrafeasV1beta1IntotoSignature(typing_extensions.TypedDict, total=False):
    keyid: str
    sig: str

@typing.type_check_only
class GrafeasV1beta1PackageDetails(typing_extensions.TypedDict, total=False):
    installation: Installation

@typing.type_check_only
class GrafeasV1beta1VulnerabilityDetails(typing_extensions.TypedDict, total=False):
    cvssScore: float
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    longDescription: str
    packageIssue: typing.List[PackageIssue]
    relatedUrls: typing.List[RelatedUrl]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["HASH_TYPE_UNSPECIFIED", "SHA256"]
    value: str

@typing.type_check_only
class Hint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

@typing.type_check_only
class InToto(typing_extensions.TypedDict, total=False):
    expectedCommand: typing.List[str]
    expectedMaterials: typing.List[ArtifactRule]
    expectedProducts: typing.List[ArtifactRule]
    signingKeys: typing.List[SigningKey]
    stepName: str
    threshold: str

@typing.type_check_only
class Installation(typing_extensions.TypedDict, total=False):
    location: typing.List[Location]
    name: str

@typing.type_check_only
class KnowledgeBase(typing_extensions.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class Layer(typing_extensions.TypedDict, total=False):
    arguments: str
    directive: typing_extensions.Literal[
        "DIRECTIVE_UNSPECIFIED",
        "MAINTAINER",
        "RUN",
        "CMD",
        "LABEL",
        "EXPOSE",
        "ENV",
        "ADD",
        "COPY",
        "ENTRYPOINT",
        "VOLUME",
        "USER",
        "WORKDIR",
        "ARG",
        "ONBUILD",
        "STOPSIGNAL",
        "HEALTHCHECK",
        "SHELL",
    ]

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    byproducts: ByProducts
    command: typing.List[str]
    environment: Environment
    materials: typing.List[GrafeasV1beta1IntotoArtifact]
    products: typing.List[GrafeasV1beta1IntotoArtifact]

@typing.type_check_only
class ListNoteOccurrencesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: typing.List[Occurrence]

@typing.type_check_only
class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: typing.List[Note]

@typing.type_check_only
class ListOccurrencesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    occurrences: typing.List[Occurrence]

@typing.type_check_only
class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanConfigs: typing.List[ScanConfig]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    attestationAuthority: Authority
    baseImage: Basis
    build: Build
    createTime: str
    deployable: Deployable
    discovery: Discovery
    expirationTime: str
    intoto: InToto
    kind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
    ]
    longDescription: str
    name: str
    package: Package
    relatedNoteNames: typing.List[str]
    relatedUrl: typing.List[RelatedUrl]
    shortDescription: str
    updateTime: str
    vulnerability: Vulnerability

@typing.type_check_only
class Occurrence(typing_extensions.TypedDict, total=False):
    attestation: Details
    build: GrafeasV1beta1BuildDetails
    createTime: str
    deployment: GrafeasV1beta1DeploymentDetails
    derivedImage: GrafeasV1beta1ImageDetails
    discovered: GrafeasV1beta1DiscoveryDetails
    installation: GrafeasV1beta1PackageDetails
    intoto: GrafeasV1beta1IntotoDetails
    kind: typing_extensions.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
    ]
    name: str
    noteName: str
    remediation: str
    resource: Resource
    updateTime: str
    vulnerability: GrafeasV1beta1VulnerabilityDetails

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    distribution: typing.List[Distribution]
    name: str

@typing.type_check_only
class PackageIssue(typing_extensions.TypedDict, total=False):
    affectedLocation: VulnerabilityLocation
    fixedLocation: VulnerabilityLocation
    severityName: str

@typing.type_check_only
class PgpSignedAttestation(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]
    pgpKeyId: str
    signature: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

@typing.type_check_only
class RelatedUrl(typing_extensions.TypedDict, total=False):
    label: str
    url: str

@typing.type_check_only
class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    contentHash: Hash
    name: str
    uri: str

@typing.type_check_only
class ScanConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    enabled: bool
    name: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SigningKey(typing_extensions.TypedDict, total=False):
    keyId: str
    keyScheme: str
    keyType: str
    publicKeyValue: str

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
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    epoch: int
    inclusive: bool
    kind: typing_extensions.Literal[
        "VERSION_KIND_UNSPECIFIED", "NORMAL", "MINIMUM", "MAXIMUM"
    ]
    name: str
    revision: str

@typing.type_check_only
class Vulnerability(typing_extensions.TypedDict, total=False):
    cvssScore: float
    cvssV3: CVSSv3
    details: typing.List[Detail]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    sourceUpdateTime: str
    windowsDetails: typing.List[WindowsDetail]

@typing.type_check_only
class VulnerabilityLocation(typing_extensions.TypedDict, total=False):
    cpeUri: str
    package: str
    version: Version

@typing.type_check_only
class VulnerabilityOccurrencesSummary(typing_extensions.TypedDict, total=False):
    counts: typing.List[FixableTotalByDigest]

@typing.type_check_only
class WindowsDetail(typing_extensions.TypedDict, total=False):
    cpeUri: str
    description: str
    fixingKbs: typing.List[KnowledgeBase]
    name: str
