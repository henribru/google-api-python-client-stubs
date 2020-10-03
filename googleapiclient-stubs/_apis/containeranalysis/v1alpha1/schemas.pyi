import typing

import typing_extensions

class GoogleDevtoolsContaineranalysisV1alpha1GitSourceContext(
    typing_extensions.TypedDict, total=False
):
    url: str
    revisionId: str

class Command(typing_extensions.TypedDict, total=False):
    dir: str
    id: str
    env: typing.List[str]
    waitFor: typing.List[str]
    name: str
    args: typing.List[str]

class Distribution(typing_extensions.TypedDict, total=False):
    url: str
    cpeUri: str
    maintainer: str
    latestVersion: Version
    description: str
    architecture: typing_extensions.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]

class Installation(typing_extensions.TypedDict, total=False):
    name: str
    location: typing.List[Location]

class RepoSource(typing_extensions.TypedDict, total=False):
    repoName: str
    tagName: str
    commitSha: str
    branchName: str
    projectId: str

class Deployment(typing_extensions.TypedDict, total=False):
    address: str
    resourceUri: typing.List[str]
    config: str
    deployTime: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    userEmail: str
    undeployTime: str

class StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    etag: str
    bindings: typing.List[Binding]

class GoogleDevtoolsContaineranalysisV1alpha1RepoId(
    typing_extensions.TypedDict, total=False
):
    uid: str
    projectRepoId: GoogleDevtoolsContaineranalysisV1alpha1ProjectRepoId

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Attestation(typing_extensions.TypedDict, total=False):
    pgpSignedAttestation: PgpSignedAttestation

class RelatedUrl(typing_extensions.TypedDict, total=False):
    url: str
    label: str

class BuildType(typing_extensions.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

class Location(typing_extensions.TypedDict, total=False):
    path: str
    version: Version
    cpeUri: str

class ListNoteOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]
    nextPageToken: str

class SeverityCount(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    count: str

class UpgradeNote(typing_extensions.TypedDict, total=False):
    package: str
    version: Version
    distributions: typing.List[UpgradeDistribution]

class GoogleDevtoolsContaineranalysisV1alpha1SourceContext(
    typing_extensions.TypedDict, total=False
):
    cloudRepo: GoogleDevtoolsContaineranalysisV1alpha1CloudRepoSourceContext
    gerrit: GoogleDevtoolsContaineranalysisV1alpha1GerritSourceContext
    labels: typing.Dict[str, typing.Any]
    git: GoogleDevtoolsContaineranalysisV1alpha1GitSourceContext

class BuildDetails(typing_extensions.TypedDict, total=False):
    provenanceBytes: str
    provenance: BuildProvenance

class GoogleDevtoolsContaineranalysisV1alpha1ProjectRepoId(
    typing_extensions.TypedDict, total=False
):
    repoName: str
    projectId: str

class UpgradeDistribution(typing_extensions.TypedDict, total=False):
    classification: str
    severity: str
    cve: typing.List[str]
    cpeUri: str

class GoogleDevtoolsContaineranalysisV1alpha1GerritSourceContext(
    typing_extensions.TypedDict, total=False
):
    gerritProject: str
    revisionId: str
    aliasContext: GoogleDevtoolsContaineranalysisV1alpha1AliasContext
    hostUri: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListOccurrencesResponse(typing_extensions.TypedDict, total=False):
    occurrences: typing.List[Occurrence]
    nextPageToken: str

class BuildSignature(typing_extensions.TypedDict, total=False):
    keyType: typing_extensions.Literal[
        "KEY_TYPE_UNSPECIFIED", "PGP_ASCII_ARMORED", "PKIX_PEM"
    ]
    keyId: str
    publicKey: str
    signature: str

class Discovery(typing_extensions.TypedDict, total=False):
    analysisKind: typing_extensions.Literal[
        "KIND_UNSPECIFIED",
        "PACKAGE_VULNERABILITY",
        "BUILD_DETAILS",
        "IMAGE_BASIS",
        "PACKAGE_MANAGER",
        "DEPLOYABLE",
        "DISCOVERY",
        "ATTESTATION_AUTHORITY",
        "UPGRADE",
    ]

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class PackageIssue(typing_extensions.TypedDict, total=False):
    severityName: str
    affectedLocation: VulnerabilityLocation
    fixedLocation: VulnerabilityLocation

class UpgradeOccurrence(typing_extensions.TypedDict, total=False):
    distribution: UpgradeDistribution
    package: str
    parsedVersion: Version

class Artifact(typing_extensions.TypedDict, total=False):
    name: str
    id: str
    checksum: str
    names: typing.List[str]

class Layer(typing_extensions.TypedDict, total=False):
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
    arguments: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Source(typing_extensions.TypedDict, total=False):
    context: GoogleDevtoolsContaineranalysisV1alpha1SourceContext
    fileHashes: typing.Dict[str, typing.Any]
    artifactStorageSource: StorageSource
    additionalContexts: typing.List[
        GoogleDevtoolsContaineranalysisV1alpha1SourceContext
    ]
    repoSource: RepoSource
    storageSource: StorageSource

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: typing.List[str]
    role: str

class Occurrence(typing_extensions.TypedDict, total=False):
    deployment: Deployment
    buildDetails: BuildDetails
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED",
        "PACKAGE_VULNERABILITY",
        "BUILD_DETAILS",
        "IMAGE_BASIS",
        "PACKAGE_MANAGER",
        "DEPLOYABLE",
        "DISCOVERY",
        "ATTESTATION_AUTHORITY",
        "UPGRADE",
    ]
    updateTime: str
    attestation: Attestation
    installation: Installation
    upgrade: UpgradeOccurrence
    derivedImage: Derived
    createTime: str
    remediation: str
    resource: Resource
    noteName: str
    name: str
    resourceUrl: str
    discovered: Discovered
    vulnerabilityDetails: VulnerabilityDetails

class BuildProvenance(typing_extensions.TypedDict, total=False):
    logsBucket: str
    commands: typing.List[Command]
    createTime: str
    sourceProvenance: Source
    builderVersion: str
    triggerId: str
    startTime: str
    buildOptions: typing.Dict[str, typing.Any]
    creator: str
    finishTime: str
    projectId: str
    builtArtifacts: typing.List[Artifact]
    id: str

class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    scanConfigs: typing.List[ScanConfig]
    nextPageToken: str

class AttestationAuthority(typing_extensions.TypedDict, total=False):
    hint: AttestationAuthorityHint

class AttestationAuthorityHint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

class Fingerprint(typing_extensions.TypedDict, total=False):
    v2Name: str
    v2Blob: typing.List[str]
    v1Name: str

class VulnerabilityType(typing_extensions.TypedDict, total=False):
    details: typing.List[Detail]
    cvssScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

class Package(typing_extensions.TypedDict, total=False):
    name: str
    distribution: typing.List[Distribution]

class Hash(typing_extensions.TypedDict, total=False):
    value: str
    type: typing_extensions.Literal["NONE", "SHA256"]

class Deployable(typing_extensions.TypedDict, total=False):
    resourceUri: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]

class PgpSignedAttestation(typing_extensions.TypedDict, total=False):
    signature: str
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]
    pgpKeyId: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: typing.List[Hash]

class Derived(typing_extensions.TypedDict, total=False):
    baseResourceUrl: str
    fingerprint: Fingerprint
    layerInfo: typing.List[Layer]
    distance: int

class Note(typing_extensions.TypedDict, total=False):
    vulnerabilityType: VulnerabilityType
    package: Package
    discovery: Discovery
    longDescription: str
    deployable: Deployable
    relatedUrl: typing.List[RelatedUrl]
    baseImage: Basis
    updateTime: str
    name: str
    upgrade: UpgradeNote
    createTime: str
    shortDescription: str
    expirationTime: str
    buildType: BuildType
    attestationAuthority: AttestationAuthority
    kind: typing_extensions.Literal[
        "KIND_UNSPECIFIED",
        "PACKAGE_VULNERABILITY",
        "BUILD_DETAILS",
        "IMAGE_BASIS",
        "PACKAGE_MANAGER",
        "DEPLOYABLE",
        "DISCOVERY",
        "ATTESTATION_AUTHORITY",
        "UPGRADE",
    ]

class Version(typing_extensions.TypedDict, total=False):
    kind: typing_extensions.Literal["NORMAL", "MINIMUM", "MAXIMUM"]
    name: str
    revision: str
    epoch: int

class Resource(typing_extensions.TypedDict, total=False):
    name: str
    contentHash: Hash
    uri: str

class ScanConfig(typing_extensions.TypedDict, total=False):
    description: str
    updateTime: str
    createTime: str
    enabled: bool
    name: str

class Basis(typing_extensions.TypedDict, total=False):
    resourceUrl: str
    fingerprint: Fingerprint

class VulnerabilityDetails(typing_extensions.TypedDict, total=False):
    cvssScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    type: str
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    packageIssue: typing.List[PackageIssue]

class Discovered(typing_extensions.TypedDict, total=False):
    operation: Operation
    cpe: str
    analysisStatusError: Status
    continuousAnalysis: typing_extensions.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    analysisStatus: typing_extensions.Literal[
        "ANALYSIS_STATUS_UNSPECIFIED",
        "PENDING",
        "SCANNING",
        "FINISHED_SUCCESS",
        "FINISHED_FAILED",
        "FINISHED_UNSUPPORTED",
    ]

class GoogleDevtoolsContaineranalysisV1alpha1CloudRepoSourceContext(
    typing_extensions.TypedDict, total=False
):
    revisionId: str
    aliasContext: GoogleDevtoolsContaineranalysisV1alpha1AliasContext
    repoId: GoogleDevtoolsContaineranalysisV1alpha1RepoId

class Empty(typing_extensions.TypedDict, total=False): ...

class Detail(typing_extensions.TypedDict, total=False):
    minAffectedVersion: Version
    package: str
    description: str
    packageType: str
    maxAffectedVersion: Version
    fixedLocation: VulnerabilityLocation
    severityName: str
    cpeUri: str
    isObsolete: bool

class GoogleDevtoolsContaineranalysisV1alpha1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class VulnerabilityLocation(typing_extensions.TypedDict, total=False):
    cpeUri: str
    version: Version
    package: str

class ListNotesResponse(typing_extensions.TypedDict, total=False):
    notes: typing.List[Note]
    nextPageToken: str

class CreateOperationRequest(typing_extensions.TypedDict, total=False):
    operationId: str
    operation: Operation

class GoogleDevtoolsContaineranalysisV1alpha1AliasContext(
    typing_extensions.TypedDict, total=False
):
    name: str
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]

class UpdateOperationRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    operation: Operation

class GetVulnzOccurrencesSummaryResponse(typing_extensions.TypedDict, total=False):
    counts: typing.List[SeverityCount]
