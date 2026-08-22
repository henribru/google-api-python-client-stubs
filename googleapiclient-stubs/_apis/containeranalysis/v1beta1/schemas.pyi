import typing

_list = list

@typing.type_check_only
class AISkillAnalysisNote(typing.TypedDict, total=False): ...

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
class Artifact(typing.TypedDict, total=False):
    checksum: str
    id: str
    names: _list[str]

@typing.type_check_only
class ArtifactHashes(typing.TypedDict, total=False):
    sha256: str

@typing.type_check_only
class ArtifactRule(typing.TypedDict, total=False):
    artifactRule: _list[str]

@typing.type_check_only
class Assessment(typing.TypedDict, total=False):
    cve: str
    impacts: _list[str]
    justification: Justification
    longDescription: str
    relatedUris: _list[RelatedUrl]
    remediations: _list[Remediation]
    shortDescription: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "AFFECTED", "NOT_AFFECTED", "FIXED", "UNDER_INVESTIGATION"
    ]
    vulnerabilityId: str

@typing.type_check_only
class Attestation(typing.TypedDict, total=False):
    genericSignedAttestation: GenericSignedAttestation
    pgpSignedAttestation: PgpSignedAttestation

@typing.type_check_only
class Authority(typing.TypedDict, total=False):
    hint: Hint

@typing.type_check_only
class Basis(typing.TypedDict, total=False):
    fingerprint: Fingerprint
    resourceUrl: str

@typing.type_check_only
class BatchCreateNotesRequest(typing.TypedDict, total=False):
    notes: dict[str, typing.Any]

@typing.type_check_only
class BatchCreateNotesResponse(typing.TypedDict, total=False):
    notes: _list[Note]

@typing.type_check_only
class BatchCreateOccurrencesRequest(typing.TypedDict, total=False):
    occurrences: _list[Occurrence]

@typing.type_check_only
class BatchCreateOccurrencesResponse(typing.TypedDict, total=False):
    occurrences: _list[Occurrence]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Build(typing.TypedDict, total=False):
    builderVersion: str
    signature: BuildSignature

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
class BuildSignature(typing.TypedDict, total=False):
    keyId: str
    keyType: typing.Literal["KEY_TYPE_UNSPECIFIED", "PGP_ASCII_ARMORED", "PKIX_PEM"]
    publicKey: str
    signature: str

@typing.type_check_only
class BuildStep(typing.TypedDict, total=False):
    allowExitCodes: _list[int]
    allowFailure: bool
    args: _list[str]
    automapSubstitutions: bool
    dir: str
    entrypoint: str
    env: _list[str]
    exitCode: int
    id: str
    name: str
    pullTiming: TimeSpan
    remoteConfig: str
    results: _list[StepResult]
    script: str
    secretEnv: _list[str]
    status: typing.Literal[
        "STATUS_UNKNOWN",
        "PENDING",
        "QUEUING",
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
class ByProducts(typing.TypedDict, total=False):
    customValues: dict[str, typing.Any]

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
class CVSSv3(typing.TypedDict, total=False):
    attackComplexity: typing.Literal[
        "ATTACK_COMPLEXITY_UNSPECIFIED",
        "ATTACK_COMPLEXITY_LOW",
        "ATTACK_COMPLEXITY_HIGH",
    ]
    attackVector: typing.Literal[
        "ATTACK_VECTOR_UNSPECIFIED",
        "ATTACK_VECTOR_NETWORK",
        "ATTACK_VECTOR_ADJACENT",
        "ATTACK_VECTOR_LOCAL",
        "ATTACK_VECTOR_PHYSICAL",
    ]
    availabilityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    baseScore: float
    confidentialityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    exploitabilityScore: float
    impactScore: float
    integrityImpact: typing.Literal[
        "IMPACT_UNSPECIFIED", "IMPACT_HIGH", "IMPACT_LOW", "IMPACT_NONE"
    ]
    privilegesRequired: typing.Literal[
        "PRIVILEGES_REQUIRED_UNSPECIFIED",
        "PRIVILEGES_REQUIRED_NONE",
        "PRIVILEGES_REQUIRED_LOW",
        "PRIVILEGES_REQUIRED_HIGH",
    ]
    scope: typing.Literal["SCOPE_UNSPECIFIED", "SCOPE_UNCHANGED", "SCOPE_CHANGED"]
    userInteraction: typing.Literal[
        "USER_INTERACTION_UNSPECIFIED",
        "USER_INTERACTION_NONE",
        "USER_INTERACTION_REQUIRED",
    ]

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
class ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig(
    typing.TypedDict, total=False
):
    approvalRequired: bool

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult(
    typing.TypedDict, total=False
):
    approvalTime: str
    approverAccount: str
    comment: str
    decision: typing.Literal["DECISION_UNSPECIFIED", "APPROVED", "REJECTED"]
    url: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Artifacts(
    typing.TypedDict, total=False
):
    genericArtifacts: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsGenericArtifact
    ]
    goModules: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsGoModule]
    images: _list[str]
    mavenArtifacts: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifact
    ]
    npmPackages: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackage]
    objects: ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects
    oci: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOci]
    pythonPackages: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackage
    ]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsArtifactObjects(
    typing.TypedDict, total=False
):
    location: str
    paths: _list[str]
    timing: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsGenericArtifact(
    typing.TypedDict, total=False
):
    folder: str
    registryPath: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsGoModule(
    typing.TypedDict, total=False
):
    modulePath: str
    moduleVersion: str
    repositoryLocation: str
    repositoryName: str
    repositoryProjectId: str
    sourcePath: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsMavenArtifact(
    typing.TypedDict, total=False
):
    artifactId: str
    deployFolder: str
    groupId: str
    path: str
    repository: str
    version: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsNpmPackage(
    typing.TypedDict, total=False
):
    packagePath: str
    repository: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsOci(
    typing.TypedDict, total=False
):
    file: str
    registryPath: str
    tags: _list[str]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ArtifactsPythonPackage(
    typing.TypedDict, total=False
):
    paths: _list[str]
    repository: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Build(typing.TypedDict, total=False):
    approval: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildApproval
    artifacts: ContaineranalysisGoogleDevtoolsCloudbuildV1Artifacts
    availableSecrets: ContaineranalysisGoogleDevtoolsCloudbuildV1Secrets
    buildTriggerId: str
    createTime: str
    dependencies: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Dependency]
    failureInfo: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfo
    finishTime: str
    gitConfig: ContaineranalysisGoogleDevtoolsCloudbuildV1GitConfig
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
    status: typing.Literal[
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
    typing.TypedDict, total=False
):
    config: ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalConfig
    result: ContaineranalysisGoogleDevtoolsCloudbuildV1ApprovalResult
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "APPROVED", "REJECTED", "CANCELLED"
    ]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildFailureInfo(
    typing.TypedDict, total=False
):
    detail: str
    type: typing.Literal[
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
    typing.TypedDict, total=False
):
    automapSubstitutions: bool
    defaultLogsBucketBehavior: typing.Literal[
        "DEFAULT_LOGS_BUCKET_BEHAVIOR_UNSPECIFIED",
        "REGIONAL_USER_OWNED_BUCKET",
        "LEGACY_BUCKET",
    ]
    diskSizeGb: str
    dynamicSubstitutions: bool
    enableStructuredLogging: bool
    env: _list[str]
    logStreamingOption: typing.Literal["STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"]
    logging: typing.Literal[
        "LOGGING_UNSPECIFIED",
        "LEGACY",
        "GCS_ONLY",
        "STACKDRIVER_ONLY",
        "CLOUD_LOGGING_ONLY",
        "NONE",
    ]
    machineType: typing.Literal[
        "UNSPECIFIED",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_32",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_32",
        "E2_MEDIUM",
        "E2_STANDARD_2",
    ]
    pool: ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption
    pubsubTopic: str
    requestedVerifyOption: typing.Literal["NOT_VERIFIED", "VERIFIED"]
    secretEnv: _list[str]
    sourceProvenanceHash: _list[
        typing.Literal[
            "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
        ]
    ]
    substitutionOption: typing.Literal["MUST_MATCH", "ALLOW_LOOSE"]
    volumes: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Volume]
    workerPool: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildOptionsPoolOption(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStep(
    typing.TypedDict, total=False
):
    allowExitCodes: _list[int]
    allowFailure: bool
    args: _list[str]
    automapSubstitutions: bool
    dir: str
    entrypoint: str
    env: _list[str]
    exitCode: int
    id: str
    name: str
    pullTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    results: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1StepResult]
    script: str
    secretEnv: _list[str]
    status: typing.Literal[
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
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildStepResults(
    typing.TypedDict, total=False
):
    results: dict[str, typing.Any]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuildWarning(
    typing.TypedDict, total=False
):
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "INFO", "WARNING", "ALERT"]
    text: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage(
    typing.TypedDict, total=False
):
    artifactRegistryPackage: str
    digest: str
    name: str
    ociMediaType: typing.Literal[
        "OCI_MEDIA_TYPE_UNSPECIFIED", "IMAGE_MANIFEST", "IMAGE_INDEX"
    ]
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1ConnectedRepository(
    typing.TypedDict, total=False
):
    dir: str
    repository: str
    revision: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Dependency(
    typing.TypedDict, total=False
):
    empty: bool
    genericArtifact: (
        ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGenericArtifactDependency
    )
    gitSource: ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGitSourceDependency

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGenericArtifactDependency(
    typing.TypedDict, total=False
):
    destPath: str
    resource: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGitSourceDependency(
    typing.TypedDict, total=False
):
    depth: str
    destPath: str
    recurseSubmodules: bool
    repository: ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGitSourceRepository
    revision: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1DependencyGitSourceRepository(
    typing.TypedDict, total=False
):
    developerConnect: str
    url: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1DeveloperConnectConfig(
    typing.TypedDict, total=False
):
    dir: str
    gitRepositoryLink: str
    revision: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes(
    typing.TypedDict, total=False
):
    fileHash: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1Hash]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1GitConfig(
    typing.TypedDict, total=False
):
    http: ContaineranalysisGoogleDevtoolsCloudbuildV1GitConfigHttpConfig

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1GitConfigHttpConfig(
    typing.TypedDict, total=False
):
    proxySecretVersionName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource(
    typing.TypedDict, total=False
):
    dir: str
    revision: str
    url: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Hash(typing.TypedDict, total=False):
    type: typing.Literal[
        "NONE", "SHA256", "MD5", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
    ]
    value: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecret(
    typing.TypedDict, total=False
):
    envMap: dict[str, typing.Any]
    kmsKeyName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource(
    typing.TypedDict, total=False
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
class ContaineranalysisGoogleDevtoolsCloudbuildV1Results(typing.TypedDict, total=False):
    artifactManifest: str
    artifactTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    buildStepImages: _list[str]
    buildStepOutputs: _list[str]
    buildStepResults: dict[str, typing.Any]
    genericArtifacts: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedGenericArtifact
    ]
    goModules: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedGoModule]
    images: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1BuiltImage]
    mavenArtifacts: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact
    ]
    npmPackages: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage]
    numArtifacts: str
    pythonPackages: _list[
        ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage
    ]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Secret(typing.TypedDict, total=False):
    kmsKeyName: str
    secretEnv: dict[str, typing.Any]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecret(
    typing.TypedDict, total=False
):
    env: str
    versionName: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Secrets(typing.TypedDict, total=False):
    inline: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1InlineSecret]
    secretManager: _list[ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecret]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Source(typing.TypedDict, total=False):
    connectedRepository: ContaineranalysisGoogleDevtoolsCloudbuildV1ConnectedRepository
    developerConnectConfig: (
        ContaineranalysisGoogleDevtoolsCloudbuildV1DeveloperConnectConfig
    )
    gitSource: ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource
    repoSource: ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource
    storageSource: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource
    storageSourceManifest: (
        ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest
    )

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1SourceProvenance(
    typing.TypedDict, total=False
):
    fileHashes: dict[str, typing.Any]
    resolvedConnectedRepository: (
        ContaineranalysisGoogleDevtoolsCloudbuildV1ConnectedRepository
    )
    resolvedGitSource: ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource
    resolvedRepoSource: ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource
    resolvedStorageSource: ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource
    resolvedStorageSourceManifest: (
        ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest
    )

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1StepResult(
    typing.TypedDict, total=False
):
    attestationContent: str
    attestationType: str
    name: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSource(
    typing.TypedDict, total=False
):
    bucket: str
    generation: str
    object: str
    sourceFetcher: typing.Literal["SOURCE_FETCHER_UNSPECIFIED", "GSUTIL", "GCS_FETCHER"]

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1StorageSourceManifest(
    typing.TypedDict, total=False
):
    bucket: str
    generation: str
    object: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan(
    typing.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedGenericArtifact(
    typing.TypedDict, total=False
):
    artifactFingerprint: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes
    artifactRegistryPackage: str
    fileHashes: dict[str, typing.Any]
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedGoModule(
    typing.TypedDict, total=False
):
    artifactRegistryPackage: str
    fileHashes: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedMavenArtifact(
    typing.TypedDict, total=False
):
    artifactRegistryPackage: str
    fileHashes: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedNpmPackage(
    typing.TypedDict, total=False
):
    artifactRegistryPackage: str
    fileHashes: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1UploadedPythonPackage(
    typing.TypedDict, total=False
):
    artifactRegistryPackage: str
    fileHashes: ContaineranalysisGoogleDevtoolsCloudbuildV1FileHashes
    pushTiming: ContaineranalysisGoogleDevtoolsCloudbuildV1TimeSpan
    uri: str

@typing.type_check_only
class ContaineranalysisGoogleDevtoolsCloudbuildV1Volume(typing.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class Deployable(typing.TypedDict, total=False):
    resourceUri: _list[str]

@typing.type_check_only
class Deployment(typing.TypedDict, total=False):
    address: str
    config: str
    deployTime: str
    platform: typing.Literal["PLATFORM_UNSPECIFIED", "GKE", "FLEX", "CUSTOM"]
    resourceUri: _list[str]
    undeployTime: str
    userEmail: str

@typing.type_check_only
class Derived(typing.TypedDict, total=False):
    baseResourceUrl: str
    distance: int
    fingerprint: Fingerprint
    layerInfo: _list[Layer]

@typing.type_check_only
class Detail(typing.TypedDict, total=False):
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
    vendor: str

@typing.type_check_only
class Details(typing.TypedDict, total=False):
    attestation: Attestation

@typing.type_check_only
class Digest(typing.TypedDict, total=False):
    algo: str
    digestBytes: str

@typing.type_check_only
class Discovered(typing.TypedDict, total=False):
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
    continuousAnalysis: typing.Literal[
        "CONTINUOUS_ANALYSIS_UNSPECIFIED", "ACTIVE", "INACTIVE"
    ]
    files: _list[File]
    lastAnalysisTime: str
    lastScanTime: str
    lastVulnerabilityUpdateTime: str
    sbomStatus: SBOMStatus

@typing.type_check_only
class Discovery(typing.TypedDict, total=False):
    analysisKind: typing.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "VULNERABILITY_ASSESSMENT",
        "SBOM_REFERENCE",
        "SECRET",
        "AI_SKILL_ANALYSIS",
    ]

@typing.type_check_only
class Distribution(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    description: str
    latestVersion: Version
    maintainer: str
    url: str

@typing.type_check_only
class DocumentNote(typing.TypedDict, total=False):
    dataLicence: str
    spdxVersion: str

@typing.type_check_only
class DocumentOccurrence(typing.TypedDict, total=False):
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
class Environment(typing.TypedDict, total=False):
    customValues: dict[str, typing.Any]

@typing.type_check_only
class ExportSBOMRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportSBOMResponse(typing.TypedDict, total=False):
    discoveryOccurrenceId: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExternalRef(typing.TypedDict, total=False):
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED", "SECURITY", "PACKAGE_MANAGER", "PERSISTENT_ID", "OTHER"
    ]
    comment: str
    locator: str
    type: str

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

@typing.type_check_only
class FileNote(typing.TypedDict, total=False):
    checksum: _list[str]
    fileType: typing.Literal[
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
class FileOccurrence(typing.TypedDict, total=False):
    attributions: _list[str]
    comment: str
    contributors: _list[str]
    copyright: str
    filesLicenseInfo: _list[str]
    id: str
    licenseConcluded: License
    notice: str

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
class FixableTotalByDigest(typing.TypedDict, total=False):
    fixableCount: str
    resource: Resource
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    totalCount: str

@typing.type_check_only
class GeneratePackagesSummaryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GenericSignedAttestation(typing.TypedDict, total=False):
    contentType: typing.Literal["CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"]
    serializedPayload: str
    signatures: _list[Signature]

@typing.type_check_only
class GerritSourceContext(typing.TypedDict, total=False):
    aliasContext: AliasContext
    gerritProject: str
    hostUri: str
    revisionId: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GitSourceContext(typing.TypedDict, total=False):
    revisionId: str
    url: str

@typing.type_check_only
class GoogleDevtoolsContaineranalysisV1alpha1OperationMetadata(
    typing.TypedDict, total=False
):
    createTime: str
    endTime: str

@typing.type_check_only
class GrafeasV1beta1BuildDetails(typing.TypedDict, total=False):
    inTotoSlsaProvenanceV1: InTotoSlsaProvenanceV1
    provenance: BuildProvenance
    provenanceBytes: str

@typing.type_check_only
class GrafeasV1beta1DeploymentDetails(typing.TypedDict, total=False):
    deployment: Deployment

@typing.type_check_only
class GrafeasV1beta1DiscoveryDetails(typing.TypedDict, total=False):
    discovered: Discovered

@typing.type_check_only
class GrafeasV1beta1ImageDetails(typing.TypedDict, total=False):
    derivedImage: Derived

@typing.type_check_only
class GrafeasV1beta1IntotoArtifact(typing.TypedDict, total=False):
    hashes: ArtifactHashes
    resourceUri: str

@typing.type_check_only
class GrafeasV1beta1IntotoDetails(typing.TypedDict, total=False):
    signatures: _list[GrafeasV1beta1IntotoSignature]
    signed: Link

@typing.type_check_only
class GrafeasV1beta1IntotoSignature(typing.TypedDict, total=False):
    keyid: str
    sig: str

@typing.type_check_only
class GrafeasV1beta1PackageDetails(typing.TypedDict, total=False):
    installation: Installation

@typing.type_check_only
class GrafeasV1beta1VulnerabilityDetails(typing.TypedDict, total=False):
    cvssScore: float
    cvssV2: CVSS
    cvssV3: CVSS
    cvssV4: CVSS
    cvssVersion: typing.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3", "CVSS_VERSION_4"
    ]
    effectiveSeverity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    extraDetails: str
    longDescription: str
    packageIssue: _list[PackageIssue]
    relatedUrls: _list[RelatedUrl]
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    shortDescription: str
    type: str
    vexAssessment: VexAssessment

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: typing.Literal[
        "HASH_TYPE_UNSPECIFIED", "SHA256", "GO_MODULE_H1", "SHA512", "DIRSUM_SHA256"
    ]
    value: str

@typing.type_check_only
class Hint(typing.TypedDict, total=False):
    humanReadableName: str

@typing.type_check_only
class InToto(typing.TypedDict, total=False):
    expectedCommand: _list[str]
    expectedMaterials: _list[ArtifactRule]
    expectedProducts: _list[ArtifactRule]
    signingKeys: _list[SigningKey]
    stepName: str
    threshold: str

@typing.type_check_only
class InTotoSlsaProvenanceV1(typing.TypedDict, total=False):
    _type: str
    predicate: SlsaProvenanceV1
    predicateType: str
    subject: _list[Subject]

@typing.type_check_only
class Installation(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
    cpeUri: str
    license: License
    location: _list[Location]
    name: str
    packageType: str
    version: Version

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
class KnowledgeBase(typing.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class Layer(typing.TypedDict, total=False):
    arguments: str
    directive: typing.Literal[
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
class License(typing.TypedDict, total=False):
    comments: str
    expression: str

@typing.type_check_only
class LicensesSummary(typing.TypedDict, total=False):
    count: str
    license: str

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    byproducts: ByProducts
    command: _list[str]
    environment: Environment
    materials: _list[GrafeasV1beta1IntotoArtifact]
    products: _list[GrafeasV1beta1IntotoArtifact]

@typing.type_check_only
class ListNoteOccurrencesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]

@typing.type_check_only
class ListNotesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    notes: _list[Note]
    unreachable: _list[str]

@typing.type_check_only
class ListOccurrencesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    occurrences: _list[Occurrence]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    cpeUri: str
    path: str
    version: Version

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
class Note(typing.TypedDict, total=False):
    aiSkillAnalysis: AISkillAnalysisNote
    attestationAuthority: Authority
    baseImage: Basis
    build: Build
    createTime: str
    deployable: Deployable
    discovery: Discovery
    expirationTime: str
    intoto: InToto
    kind: typing.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "VULNERABILITY_ASSESSMENT",
        "SBOM_REFERENCE",
        "SECRET",
        "AI_SKILL_ANALYSIS",
    ]
    longDescription: str
    name: str
    package: Package
    relatedNoteNames: _list[str]
    relatedUrl: _list[RelatedUrl]
    sbom: DocumentNote
    sbomReference: SBOMReferenceNote
    secret: SecretNote
    shortDescription: str
    spdxFile: FileNote
    spdxPackage: PackageInfoNote
    spdxRelationship: RelationshipNote
    updateTime: str
    vulnerability: Vulnerability
    vulnerabilityAssessment: VulnerabilityAssessmentNote

@typing.type_check_only
class Occurrence(typing.TypedDict, total=False):
    aiSkillAnalysis: AISkillAnalysisOccurrence
    attestation: Details
    build: GrafeasV1beta1BuildDetails
    createTime: str
    deployment: GrafeasV1beta1DeploymentDetails
    derivedImage: GrafeasV1beta1ImageDetails
    discovered: GrafeasV1beta1DiscoveryDetails
    envelope: Envelope
    installation: GrafeasV1beta1PackageDetails
    intoto: GrafeasV1beta1IntotoDetails
    kind: typing.Literal[
        "NOTE_KIND_UNSPECIFIED",
        "VULNERABILITY",
        "BUILD",
        "IMAGE",
        "PACKAGE",
        "DEPLOYMENT",
        "DISCOVERY",
        "ATTESTATION",
        "INTOTO",
        "SBOM",
        "SPDX_PACKAGE",
        "SPDX_FILE",
        "SPDX_RELATIONSHIP",
        "VULNERABILITY_ASSESSMENT",
        "SBOM_REFERENCE",
        "SECRET",
        "AI_SKILL_ANALYSIS",
    ]
    name: str
    noteName: str
    remediation: str
    resource: Resource
    sbom: DocumentOccurrence
    sbomReference: SBOMReferenceOccurrence
    secret: SecretOccurrence
    spdxFile: FileOccurrence
    spdxPackage: PackageInfoOccurrence
    spdxRelationship: RelationshipOccurrence
    updateTime: str
    vulnerability: GrafeasV1beta1VulnerabilityDetails

@typing.type_check_only
class Package(typing.TypedDict, total=False):
    architecture: typing.Literal["ARCHITECTURE_UNSPECIFIED", "X86", "X64"]
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
class PackageInfoNote(typing.TypedDict, total=False):
    analyzed: bool
    attribution: str
    checksum: str
    copyright: str
    detailedDescription: str
    downloadLocation: str
    externalRefs: _list[ExternalRef]
    filesLicenseInfo: _list[str]
    homePage: str
    licenseDeclared: License
    originator: str
    packageType: str
    summaryDescription: str
    supplier: str
    title: str
    verificationCode: str
    version: str

@typing.type_check_only
class PackageInfoOccurrence(typing.TypedDict, total=False):
    comment: str
    filename: str
    homePage: str
    id: str
    licenseConcluded: License
    packageType: str
    sourceInfo: str
    summaryDescription: str
    title: str
    version: str

@typing.type_check_only
class PackageIssue(typing.TypedDict, total=False):
    affectedLocation: VulnerabilityLocation
    effectiveSeverity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    fixedLocation: VulnerabilityLocation
    packageType: str
    severityName: str

@typing.type_check_only
class PackagesSummaryResponse(typing.TypedDict, total=False):
    licensesSummary: _list[LicensesSummary]
    resourceUrl: str

@typing.type_check_only
class PerScannerVerdict(typing.TypedDict, total=False):
    maliciousContentLlmResult: MaliciousContentLLMResult
    maliciousContentStaticResult: MaliciousContentStaticResult
    malwareScan: MalwareScanResult
    workspacePolicy: WorkspacePolicyResult

@typing.type_check_only
class PgpSignedAttestation(typing.TypedDict, total=False):
    contentType: typing.Literal["CONTENT_TYPE_UNSPECIFIED", "SIMPLE_SIGNING_JSON"]
    pgpKeyId: str
    signature: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Product(typing.TypedDict, total=False):
    genericUri: str
    id: str
    name: str

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
class Publisher(typing.TypedDict, total=False):
    issuingAuthority: str
    name: str
    publisherNamespace: str

@typing.type_check_only
class RelatedUrl(typing.TypedDict, total=False):
    label: str
    url: str

@typing.type_check_only
class RelationshipNote(typing.TypedDict, total=False):
    type: typing.Literal[
        "RELATIONSHIP_TYPE_UNSPECIFIED",
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
class RelationshipOccurrence(typing.TypedDict, total=False):
    comment: str
    source: str
    target: str
    type: typing.Literal[
        "RELATIONSHIP_TYPE_UNSPECIFIED",
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
class Resource(typing.TypedDict, total=False):
    contentHash: Hash
    name: str
    uri: str

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
class RunDetails(typing.TypedDict, total=False):
    builder: ProvenanceBuilder
    byproducts: _list[ResourceDescriptor]
    metadata: BuildMetadata

@typing.type_check_only
class SBOMReferenceNote(typing.TypedDict, total=False):
    format: str
    version: str

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
    fileLocation: FileLocation

@typing.type_check_only
class SecretNote(typing.TypedDict, total=False): ...

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
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Signature(typing.TypedDict, total=False):
    publicKeyId: str
    signature: str

@typing.type_check_only
class SigningKey(typing.TypedDict, total=False):
    keyId: str
    keyScheme: str
    keyType: str
    publicKeyValue: str

@typing.type_check_only
class SlsaProvenanceV1(typing.TypedDict, total=False):
    buildDefinition: BuildDefinition
    runDetails: RunDetails

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
class StepResult(typing.TypedDict, total=False):
    attestationContentName: str
    attestationType: str
    name: str

@typing.type_check_only
class Subject(typing.TypedDict, total=False):
    digest: dict[str, typing.Any]
    name: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeSpan(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    epoch: int
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
class Volume(typing.TypedDict, total=False):
    name: str
    path: str

@typing.type_check_only
class Vulnerability(typing.TypedDict, total=False):
    advisoryPublishTime: str
    cvssScore: float
    cvssV2: CVSS
    cvssV3: CVSSv3
    cvssV4: CVSS
    cvssVersion: typing.Literal[
        "CVSS_VERSION_UNSPECIFIED", "CVSS_VERSION_2", "CVSS_VERSION_3", "CVSS_VERSION_4"
    ]
    cwe: _list[str]
    details: _list[Detail]
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "MINIMAL", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    sourceUpdateTime: str
    windowsDetails: _list[WindowsDetail]

@typing.type_check_only
class VulnerabilityAssessmentNote(typing.TypedDict, total=False):
    assessment: Assessment
    languageCode: str
    longDescription: str
    product: Product
    publisher: Publisher
    shortDescription: str
    title: str

@typing.type_check_only
class VulnerabilityLocation(typing.TypedDict, total=False):
    cpeUri: str
    package: str
    version: Version

@typing.type_check_only
class VulnerabilityOccurrencesSummary(typing.TypedDict, total=False):
    counts: _list[FixableTotalByDigest]
    unreachable: _list[str]

@typing.type_check_only
class WindowsDetail(typing.TypedDict, total=False):
    cpeUri: str
    description: str
    fixingKbs: _list[KnowledgeBase]
    name: str

@typing.type_check_only
class WorkspacePolicyResult(typing.TypedDict, total=False):
    scanStatus: typing.Literal["SCAN_STATUS_UNSPECIFIED", "PERFORMED", "NOT_PERFORMED"]
    verdict: typing.Literal["VERDICT_UNSPECIFIED", "PASSED", "FAILED"]
