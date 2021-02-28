import typing

import typing_extensions
@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    id: str
    name: str
    names: typing.List[str]

@typing.type_check_only
class Attestation(typing_extensions.TypedDict, total=False):
    pgpSignedAttestation: PgpSignedAttestation

@typing.type_check_only
class AttestationAuthority(typing_extensions.TypedDict, total=False):
    hint: AttestationAuthorityHint

@typing.type_check_only
class AttestationAuthorityHint(typing_extensions.TypedDict, total=False):
    humanReadableName: str

@typing.type_check_only
class Basis(typing_extensions.TypedDict, total=False):
    fingerprint: Fingerprint
    resourceUrl: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class BuildDetails(typing_extensions.TypedDict, total=False):
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
    finishTime: str
    id: str
    logsBucket: str
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
class BuildType(typing_extensions.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

@typing.type_check_only
class Command(typing_extensions.TypedDict, total=False):
    args: typing.List[str]
    dir: str
    env: typing.List[str]
    id: str
    name: str
    waitFor: typing.List[str]

@typing.type_check_only
class CreateOperationRequest(typing_extensions.TypedDict, total=False):
    operation: Operation
    operationId: str

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
    cpe: str
    operation: Operation

@typing.type_check_only
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
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GetVulnzOccurrencesSummaryResponse(typing_extensions.TypedDict, total=False):
    counts: typing.List[SeverityCount]

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1AliasContext(
    typing_extensions.TypedDict, total=False
):
    kind: typing_extensions.Literal["KIND_UNSPECIFIED", "FIXED", "MOVABLE", "OTHER"]
    name: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1CloudRepoSourceContext(
    typing_extensions.TypedDict, total=False
):
    aliasContext: GoogleDevtoolsContaineranalysisV1alpha1AliasContext
    repoId: GoogleDevtoolsContaineranalysisV1alpha1RepoId
    revisionId: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1GerritSourceContext(
    typing_extensions.TypedDict, total=False
):
    aliasContext: GoogleDevtoolsContaineranalysisV1alpha1AliasContext
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1GitSourceContext(
    typing_extensions.TypedDict, total=False
):
    revisionId: str
    url: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1ProjectRepoId(
    typing_extensions.TypedDict, total=False
):
    projectId: str
    repoName: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1RepoId(
    typing_extensions.TypedDict, total=False
):
    projectRepoId: GoogleDevtoolsContaineranalysisV1alpha1ProjectRepoId
    uid: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1SourceContext(
    typing_extensions.TypedDict, total=False
):
    cloudRepo: GoogleDevtoolsContaineranalysisV1alpha1CloudRepoSourceContext
    gerrit: GoogleDevtoolsContaineranalysisV1alpha1GerritSourceContext
    git: GoogleDevtoolsContaineranalysisV1alpha1GitSourceContext
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256"]
    value: str

@typing.type_check_only
class Installation(typing_extensions.TypedDict, total=False):
    location: typing.List[Location]
    name: str

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
    attestationAuthority: AttestationAuthority
    baseImage: Basis
    buildType: BuildType
    createTime: str
    deployable: Deployable
    discovery: Discovery
    expirationTime: str
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
    longDescription: str
    name: str
    package: Package
    relatedUrl: typing.List[RelatedUrl]
    shortDescription: str
    updateTime: str
    upgrade: UpgradeNote
    vulnerabilityType: VulnerabilityType

@typing.type_check_only
class Occurrence(typing_extensions.TypedDict, total=False):
    attestation: Attestation
    buildDetails: BuildDetails
    createTime: str
    deployment: Deployment
    derivedImage: Derived
    discovered: Discovered
    installation: Installation
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
    name: str
    noteName: str
    remediation: str
    resource: Resource
    resourceUrl: str
    updateTime: str
    upgrade: UpgradeOccurrence
    vulnerabilityDetails: VulnerabilityDetails

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
class RelatedUrl(typing_extensions.TypedDict, total=False):
    label: str
    url: str

@typing.type_check_only
class RepoSource(typing_extensions.TypedDict, total=False):
    branchName: str
    commitSha: str
    projectId: str
    repoName: str
    tagName: str

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
class SeverityCount(typing_extensions.TypedDict, total=False):
    count: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    additionalContexts: typing.List[
        GoogleDevtoolsContaineranalysisV1alpha1SourceContext
    ]
    artifactStorageSource: StorageSource
    context: GoogleDevtoolsContaineranalysisV1alpha1SourceContext
    fileHashes: typing.Dict[str, typing.Any]
    repoSource: RepoSource
    storageSource: StorageSource

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class UpdateOperationRequest(typing_extensions.TypedDict, total=False):
    operation: Operation
    updateMask: str

@typing.type_check_only
class UpgradeDistribution(typing_extensions.TypedDict, total=False):
    classification: str
    cpeUri: str
    cve: typing.List[str]
    severity: str

@typing.type_check_only
class UpgradeNote(typing_extensions.TypedDict, total=False):
    distributions: typing.List[UpgradeDistribution]
    package: str
    version: Version

@typing.type_check_only
class UpgradeOccurrence(typing_extensions.TypedDict, total=False):
    distribution: UpgradeDistribution
    package: str
    parsedVersion: Version

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    epoch: int
    inclusive: bool
    kind: typing_extensions.Literal["NORMAL", "MINIMUM", "MAXIMUM"]
    name: str
    revision: str

@typing.type_check_only
class VulnerabilityDetails(typing_extensions.TypedDict, total=False):
    cvssScore: float
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    packageIssue: typing.List[PackageIssue]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    type: str

@typing.type_check_only
class VulnerabilityLocation(typing_extensions.TypedDict, total=False):
    cpeUri: str
    package: str
    version: Version

@typing.type_check_only
class VulnerabilityType(typing_extensions.TypedDict, total=False):
    cvssScore: float
    details: typing.List[Detail]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
