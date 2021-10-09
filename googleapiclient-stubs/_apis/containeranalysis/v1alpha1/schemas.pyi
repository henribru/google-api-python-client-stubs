import typing

import typing_extensions

_list = list

@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    checksum: str
    id: str
    name: str
    names: _list[str]

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
    members: _list[str]
    role: str

@typing.type_check_only
class BuildDetails(typing_extensions.TypedDict, total=False):
    intotoProvenance: InTotoProvenance
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
class BuildStep(typing_extensions.TypedDict, total=False):
    args: _list[str]
    dir: str
    entrypoint: str
    env: _list[str]
    id: str
    name: str
    pullTiming: TimeSpan
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
    timing: TimeSpan
    volumes: _list[Volume]
    waitFor: _list[str]

@typing.type_check_only
class BuildType(typing_extensions.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

@typing.type_check_only
class BuilderConfig(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class CisBenchmark(typing_extensions.TypedDict, total=False):
    profileLevel: int
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

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
    cpeUri: str
    version: str

@typing.type_check_only
class CreateOperationRequest(typing_extensions.TypedDict, total=False):
    operation: Operation
    operationId: str

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
class Deployable(typing_extensions.TypedDict, total=False):
    resourceUri: _list[str]

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    address: str
    config: str
    deployTime: str
    platform: typing_extensions.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    resourceUri: _list[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class Derived(typing_extensions.TypedDict, total=False):
    baseResourceUrl: str
    distance: int
    fingerprint: Fingerprint
    layerInfo: _list[Layer]

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
    vendor: str

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
        "COMPLIANCE",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "DSSE_ATTESTATION",
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
class DocumentNote(typing_extensions.TypedDict, total=False):
    dataLicence: str
    spdxVersion: str

@typing.type_check_only
class DocumentOccurrence(typing_extensions.TypedDict, total=False):
    createTime: str
    creatorComment: str
    creators: _list[str]
    documentComment: str
    externalDocumentRefs: _list[str]
    id: str
    licenseListVersion: str
    namespace: str
    title: str

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
class ExternalRef(typing_extensions.TypedDict, total=False):
    category: typing_extensions.Literal[
        "CATEGORY_UNSPECIFIED", "SECURITY", "PACKAGE_MANAGER", "PERSISTENT_ID", "OTHER"
    ]
    comment: str
    locator: str
    type: str

@typing.type_check_only
class FileHashes(typing_extensions.TypedDict, total=False):
    fileHash: _list[Hash]

@typing.type_check_only
class FileNote(typing_extensions.TypedDict, total=False):
    checksum: _list[str]
    fileType: typing_extensions.Literal[
        "FILE_TYPE_UNSPECIFIED",
        "SOURCE",
        "BINARY",
        "ARCHIVE",
        "APPLICATION",
        "AUDIO",
        "IMAGE",
        "TEXT",
        "VIDEO",
        "DOCUMENTATION",
        "SPDX",
        "OTHER",
    ]
    title: str

@typing.type_check_only
class FileOccurrence(typing_extensions.TypedDict, total=False):
    attributions: _list[str]
    comment: str
    contributors: _list[str]
    copyright: str
    filesLicenseInfo: _list[str]
    id: str
    licenseComments: str
    licenseConcluded: str
    notice: str

@typing.type_check_only
class Fingerprint(typing_extensions.TypedDict, total=False):
    v1Name: str
    v2Blob: _list[str]
    v2Name: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GetVulnzOccurrencesSummaryResponse(typing_extensions.TypedDict, total=False):
    counts: _list[SeverityCount]

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
    labels: dict[str, typing.Any]

@typing.type_check_only
class Hash(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["NONE", "SHA256"]
    value: str

@typing.type_check_only
class InTotoProvenance(typing_extensions.TypedDict, total=False):
    builderConfig: BuilderConfig
    materials: _list[str]
    metadata: Metadata
    recipe: Recipe

@typing.type_check_only
class InTotoStatement(typing_extensions.TypedDict, total=False):
    predicateType: str
    provenance: InTotoProvenance
    subject: _list[Subject]
    type: str

@typing.type_check_only
class Installation(typing_extensions.TypedDict, total=False):
    location: _list[Location]
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
class ListScanConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scanConfigs: _list[ScanConfig]

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
class Note(typing_extensions.TypedDict, total=False):
    attestationAuthority: AttestationAuthority
    baseImage: Basis
    buildType: BuildType
    compliance: ComplianceNote
    createTime: str
    deployable: Deployable
    discovery: Discovery
    dsseAttestation: DSSEAttestationNote
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
        "COMPLIANCE",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "DSSE_ATTESTATION",
    ]
    longDescription: str
    name: str
    package: Package
    relatedUrl: _list[RelatedUrl]
    sbom: DocumentNote
    shortDescription: str
    spdxFile: FileNote
    spdxPackage: PackageNote
    spdxRelationship: RelationshipNote
    updateTime: str
    upgrade: UpgradeNote
    vulnerabilityType: VulnerabilityType

@typing.type_check_only
class Occurrence(typing_extensions.TypedDict, total=False):
    attestation: Attestation
    buildDetails: BuildDetails
    compliance: ComplianceOccurrence
    createTime: str
    deployment: Deployment
    derivedImage: Derived
    discovered: Discovered
    dsseAttestation: DSSEAttestationOccurrence
    envelope: Envelope
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
        "COMPLIANCE",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "DSSE_ATTESTATION",
    ]
    name: str
    noteName: str
    remediation: str
    resource: Resource
    resourceUrl: str
    sbom: DocumentOccurrence
    spdxFile: FileOccurrence
    spdxPackage: PackageOccurrence
    spdxRelationship: RelationshipOccurrence
    updateTime: str
    upgrade: UpgradeOccurrence
    vulnerabilityDetails: VulnerabilityDetails

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Package(typing_extensions.TypedDict, total=False):
    distribution: _list[Distribution]
    name: str

@typing.type_check_only
class PackageIssue(typing_extensions.TypedDict, total=False):
    affectedLocation: VulnerabilityLocation
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fixedLocation: VulnerabilityLocation
    packageType: str
    severityName: str

@typing.type_check_only
class PackageNote(typing_extensions.TypedDict, total=False):
    analyzed: bool
    attribution: str
    checksum: str
    copyright: str
    detailedDescription: str
    downloadLocation: str
    externalRefs: _list[ExternalRef]
    filesLicenseInfo: _list[str]
    homePage: str
    licenseDeclared: str
    originator: str
    summaryDescription: str
    supplier: str
    title: str
    verificationCode: str
    version: str

@typing.type_check_only
class PackageOccurrence(typing_extensions.TypedDict, total=False):
    comment: str
    filename: str
    id: str
    licenseComments: str
    licenseConcluded: str
    sourceInfo: str

@typing.type_check_only
class PgpSignedAttestation(typing_extensions.TypedDict, total=False):
    contentType: typing_extensions.Literal[
        "CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"
    ]
    pgpKeyId: str
    signature: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

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
class RelationshipNote(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RelationshipOccurrence(typing_extensions.TypedDict, total=False):
    comment: str
    source: str
    target: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "DESCRIBES",
        "DESCRIBED_BY",
        "CONTAINS",
        "CONTAINED_BY",
        "DEPENDS_ON",
        "DEPENDENCY_OF",
        "DEPENDENCY_MANIFEST_OF",
        "BUILD_DEPENDENCY_OF",
        "DEV_DEPENDENCY_OF",
        "OPTIONAL_DEPENDENCY_OF",
        "PROVIDED_DEPENDENCY_OF",
        "TEST_DEPENDENCY_OF",
        "RUNTIME_DEPENDENCY_OF",
        "EXAMPLE_OF",
        "GENERATES",
        "GENERATED_FROM",
        "ANCESTOR_OF",
        "DESCENDANT_OF",
        "VARIANT_OF",
        "DISTRIBUTION_ARTIFACT",
        "PATCH_FOR",
        "PATCH_APPLIED",
        "COPY_OF",
        "FILE_ADDED",
        "FILE_DELETED",
        "FILE_MODIFIED",
        "EXPANDED_FROM_ARCHIVE",
        "DYNAMIC_LINK",
        "STATIC_LINK",
        "DATA_FILE_OF",
        "TEST_CASE_OF",
        "BUILD_TOOL_OF",
        "DEV_TOOL_OF",
        "TEST_OF",
        "TEST_TOOL_OF",
        "DOCUMENTATION_OF",
        "OPTIONAL_COMPONENT_OF",
        "METAFILE_OF",
        "PACKAGE_OF",
        "AMENDS",
        "PREREQUISITE_FOR",
        "HAS_PREREQUISITE",
        "OTHER",
    ]

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
    additionalContexts: _list[GoogleDevtoolsContaineranalysisV1alpha1SourceContext]
    artifactStorageSource: StorageSource
    context: GoogleDevtoolsContaineranalysisV1alpha1SourceContext
    fileHashes: dict[str, typing.Any]
    repoSource: RepoSource
    storageSource: StorageSource

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageSource(typing_extensions.TypedDict, total=False):
    bucket: str
    generation: str
    object: str

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
class TimeSpan(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpdateOperationRequest(typing_extensions.TypedDict, total=False):
    operation: Operation
    updateMask: str

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
class Volume(typing_extensions.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class VulnerabilityDetails(typing_extensions.TypedDict, total=False):
    cvssScore: float
    effectiveSeverity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    packageIssue: _list[PackageIssue]
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
    details: _list[Detail]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
