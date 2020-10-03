import typing

import typing_extensions

class CVSSv3(typing_extensions.TypedDict, total=False):
    impactScore: float
    availabilityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    integrityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    scope: typing_extensions.Literal[
        "SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"
    ]
    attackVector: typing_extensions.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    baseScore: float
    userInteraction: typing_extensions.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]
    confidentialityImpact: typing_extensions.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing_extensions.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    attackComplexity: typing_extensions.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    exploitabilityScore: float

class Package(typing_extensions.TypedDict, total=False):
    distribution: typing.List[Distribution]
    name: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class SourceContext(typing_extensions.TypedDict, total=False):
    git: GitSourceContext
    gerrit: GerritSourceContext
    labels: typing.Dict[str, typing.Any]
    cloudRepo: CloudRepoSourceContext

class RepoId(typing_extensions.TypedDict, total=False):
    projectRepoId: ProjectRepoId
    uid: str

class GoogleDevtoolsContaineranalysisV1alpha1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str

class Hint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

class GrafeasV1beta1VulnerabilityDetails(typing_extensions.TypedDict, total=False):
    relatedUrls: typing.List[RelatedUrl]
    longDescription: str
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    cvssScore: float
    type: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    packageIssue: typing.List[PackageIssue]
    shortDescription: str

class ByProducts(typing_extensions.TypedDict, total=False):
    customValues: typing.Dict[str, typing.Any]

class Details(typing_extensions.TypedDict, total=False):
    attestation: Attestation

class Resource(typing_extensions.TypedDict, total=False):
    contentHash: Hash
    name: str
    uri: str

class GrafeasV1beta1IntotoArtifact(typing_extensions.TypedDict, total=False):
    resourceUri: str
    hashes: ArtifactHashes

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    names: typing.List[str]
    id: str

class PgpSignedAttestation(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]
    signature: str
    pgpKeyId: str

class Discovered(typing_extensions.TypedDict, total=False):
    analysisStatus: typing_extensions.Literal[
        "ANALYSIS_STATUS_UNSPECIFIED",
        "PENDING",
        "SCANNING",
        "FINISHED_SUCCESS",
        "FINISHED_FAILED",
        "FINISHED_UNSUPPORTED",
    ]
    continuousAnalysis: typing_extensions.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    analysisStatusError: Status
    lastAnalysisTime: str

class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    scanConfigs: typing.List[ScanConfig]
    nextPageToken: str

class PackageIssue(typing_extensions.TypedDict, total=False):
    severityName: str
    fixedLocation: VulnerabilityLocation
    affectedLocation: VulnerabilityLocation

class VulnerabilityOccurrencesSummary(typing_extensions.TypedDict, total=False):
    counts: typing.List[FixableTotalByDigest]

class Deployment(typing_extensions.TypedDict, total=False):
    address: str
    config: str
    undeployTime: str
    resourceUri: typing.List[str]
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    userEmail: str
    deployTime: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]

class GitSourceContext(typing_extensions.TypedDict, total=False):
    url: str
    revisionId: str

class BatchCreateNotesRequest(typing_extensions.TypedDict, total=False):
    notes: typing.Dict[str, typing.Any]

class BuildProvenance(typing_extensions.TypedDict, total=False):
    buildOptions: typing.Dict[str, typing.Any]
    triggerId: str
    createTime: str
    endTime: str
    startTime: str
    commands: typing.List[Command]
    builtArtifacts: typing.List[Artifact]
    creator: str
    logsUri: str
    sourceProvenance: Source
    builderVersion: str
    projectId: str
    id: str

class Attestation(typing_extensions.TypedDict, total=False):
    pgpSignedAttestation: PgpSignedAttestation
    genericSignedAttestation: GenericSignedAttestation

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

class Detail(typing_extensions.TypedDict, total=False):
    packageType: str
    severityName: str
    minAffectedVersion: Version
    cpeUri: str
    sourceUpdateTime: str
    maxAffectedVersion: Version
    fixedLocation: VulnerabilityLocation
    isObsolete: bool
    description: str
    package: str

class Derived(typing_extensions.TypedDict, total=False):
    fingerprint: Fingerprint
    baseResourceUrl: str
    layerInfo: typing.List[Layer]
    distance: int

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    bindingId: str
    role: str

class VulnerabilityLocation(typing_extensions.TypedDict, total=False):
    version: Version
    package: str
    cpeUri: str

class Environment(typing_extensions.TypedDict, total=False):
    customValues: typing.Dict[str, typing.Any]

class WindowsDetail(typing_extensions.TypedDict, total=False):
    name: str
    description: str
    fixingKbs: typing.List[KnowledgeBase]
    cpeUri: str

class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: typing.List[Note]

class BatchCreateOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]

class Occurrence(typing_extensions.TypedDict, total=False):
    noteName: str
    createTime: str
    resource: Resource
    vulnerability: GrafeasV1beta1VulnerabilityDetails
    intoto: GrafeasV1beta1IntotoDetails
    name: str
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
    discovered: GrafeasV1beta1DiscoveryDetails
    installation: GrafeasV1beta1PackageDetails
    derivedImage: GrafeasV1beta1ImageDetails
    deployment: GrafeasV1beta1DeploymentDetails
    remediation: str
    build: GrafeasV1beta1BuildDetails
    updateTime: str
    attestation: Details

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

class CloudRepoSourceContext(typing_extensions.TypedDict, total=False):
    repoId: RepoId
    aliasContext: AliasContext
    revisionId: str

class Link(typing_extensions.TypedDict, total=False):
    environment: Environment
    materials: typing.List[GrafeasV1beta1IntotoArtifact]
    command: typing.List[str]
    byproducts: ByProducts
    products: typing.List[GrafeasV1beta1IntotoArtifact]

class GrafeasV1beta1DeploymentDetails(typing_extensions.TypedDict, total=False):
    deployment: Deployment

class GrafeasV1beta1BuildDetails(typing_extensions.TypedDict, total=False):
    provenanceBytes: str
    provenance: BuildProvenance

class Authority(typing_extensions.TypedDict, total=False):
    hint: Hint

class BuildSignature(typing_extensions.TypedDict, total=False):
    keyType: typing_extensions.Literal[
        "KEY_TYPE_UNSPECIFIED", "PGP_ASCII_ARMORED", "PKIX_PEM"
    ]
    publicKey: str
    keyId: str
    signature: str

class BatchCreateNotesResponse(typing_extensions.TypedDict, total=False):
    notes: typing.List[Note]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GrafeasV1beta1IntotoSignature(typing_extensions.TypedDict, total=False):
    keyid: str
    sig: str

class BatchCreateOccurrencesRequest(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]

class ProjectRepoId(typing_extensions.TypedDict, total=False):
    projectId: str
    repoName: str

class ArtifactRule(typing_extensions.TypedDict, total=False):
    artifactRule: typing.List[str]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Version(typing_extensions.TypedDict, total=False):
    revision: str
    name: str
    epoch: int
    kind: typing_extensions.Literal[
        "VERSION_KIND_UNSPECIFIED", "NORMAL", "MINIMUM", "MAXIMUM"
    ]

class Build(typing_extensions.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

class AliasContext(typing_extensions.TypedDict, total=False):
    name: str
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]

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

class ListNoteOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Installation(typing_extensions.TypedDict, total=False):
    name: str
    location: typing.List[Location]

class Location(typing_extensions.TypedDict, total=False):
    cpeUri: str
    version: Version
    path: str

class ArtifactHashes(typing_extensions.TypedDict, total=False):
    sha256: str

class KnowledgeBase(typing_extensions.TypedDict, total=False):
    name: str
    url: str

class ListOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]
    nextPageToken: str

class GrafeasV1beta1IntotoDetails(typing_extensions.TypedDict, total=False):
    signatures: typing.List[GrafeasV1beta1IntotoSignature]
    signed: Link

class Vulnerability(typing_extensions.TypedDict, total=False):
    windowsDetails: typing.List[WindowsDetail]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    details: typing.List[Detail]
    cvssV3: CVSSv3
    sourceUpdateTime: str
    cvssScore: float

class ScanConfig(typing_extensions.TypedDict, total=False):
    updateTime: str
    description: str
    createTime: str
    enabled: bool
    name: str

class Deployable(typing_extensions.TypedDict, total=False):
    resourceUri: typing.List[str]

class GrafeasV1beta1DiscoveryDetails(typing_extensions.TypedDict, total=False):
    discovered: Discovered

class GenericSignedAttestation(typing_extensions.TypedDict, total=False):
    serializedPayload: str
    signatures: typing.List[Signature]
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]

class Command(typing_extensions.TypedDict, total=False):
    env: typing.List[str]
    args: typing.List[str]
    waitFor: typing.List[str]
    name: str
    dir: str
    id: str

class InToto(typing_extensions.TypedDict, total=False):
    stepName: str
    threshold: str
    expectedCommand: typing.List[str]
    signingKeys: typing.List[SigningKey]
    expectedMaterials: typing.List[ArtifactRule]
    expectedProducts: typing.List[ArtifactRule]

class RelatedUrl(typing_extensions.TypedDict, total=False):
    label: str
    url: str

class GrafeasV1beta1ImageDetails(typing_extensions.TypedDict, total=False):
    derivedImage: Derived

class Distribution(typing_extensions.TypedDict, total=False):
    maintainer: str
    description: str
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    url: str
    latestVersion: Version

class Source(typing_extensions.TypedDict, total=False):
    fileHashes: typing.Dict[str, typing.Any]
    artifactStorageSourceUri: str
    additionalContexts: typing.List[SourceContext]
    context: SourceContext

class GrafeasV1beta1PackageDetails(typing_extensions.TypedDict, total=False):
    installation: Installation

class Basis(typing_extensions.TypedDict, total=False):
    resourceUrl: str
    fingerprint: Fingerprint

class Note(typing_extensions.TypedDict, total=False):
    build: Build
    discovery: Discovery
    createTime: str
    relatedUrl: typing.List[RelatedUrl]
    deployable: Deployable
    longDescription: str
    package: Package
    expirationTime: str
    vulnerability: Vulnerability
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
    updateTime: str
    intoto: InToto
    shortDescription: str
    baseImage: Basis
    name: str
    attestationAuthority: Authority
    relatedNoteNames: typing.List[str]

class FixableTotalByDigest(typing_extensions.TypedDict, total=False):
    totalCount: str
    fixableCount: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    resource: Resource

class SigningKey(typing_extensions.TypedDict, total=False):
    keyScheme: str
    keyId: str
    keyType: str
    publicKeyValue: str

class Fingerprint(typing_extensions.TypedDict, total=False):
    v2Name: str
    v2Blob: typing.List[str]
    v1Name: str

class GerritSourceContext(typing_extensions.TypedDict, total=False):
    gerritProject: str
    aliasContext: AliasContext
    hostUri: str
    revisionId: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Hash(typing_extensions.TypedDict, total=False):
    value: str
    type: typing_extensions.Literal["HASH_TYPE_UNSPECIFIED", "SHA256"]

class Signature(typing_extensions.TypedDict, total=False):
    signature: str
    publicKeyId: str
