import typing

_list = list

@typing.type_check_only
class ArchiveSource(typing.TypedDict, total=False):
    author: SourceUserMetadata
    description: str
    externalSignedUri: str
    rootDirectory: str
    userStorageUri: str

@typing.type_check_only
class Backend(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    appId: str
    automaticBaseImageUpdatesDisabled: bool
    codebase: Codebase
    createTime: str
    deleteTime: str
    displayName: str
    environment: str
    etag: str
    labels: dict[str, typing.Any]
    managedResources: _list[ManagedResource]
    mode: str
    name: str
    overrideEnv: _list[EnvironmentVariable]
    reconciling: bool
    requestLogsDisabled: bool
    runtime: BackendRuntime
    serviceAccount: str
    servingLocality: typing.Literal[
        "SERVING_LOCALITY_UNSPECIFIED", "REGIONAL_STRICT", "GLOBAL_ACCESS"
    ]
    uid: str
    updateTime: str
    uri: str

@typing.type_check_only
class BackendRuntime(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class Build(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    buildLogsUri: str
    config: Config
    createTime: str
    deleteTime: str
    displayName: str
    environment: str
    error: Status
    errorSource: typing.Literal["ERROR_SOURCE_UNSPECIFIED", "CLOUD_BUILD", "CLOUD_RUN"]
    errors: _list[Error]
    etag: str
    image: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    source: BuildSource
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "BUILDING",
        "BUILT",
        "DEPLOYING",
        "READY",
        "FAILED",
        "SKIPPED",
        "EXPIRED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class BuildSource(typing.TypedDict, total=False):
    archive: ArchiveSource
    codebase: CodebaseSource
    container: ContainerSource
    locallyBuilt: LocallyBuiltSource

@typing.type_check_only
class Codebase(typing.TypedDict, total=False):
    repository: str
    rootDirectory: str

@typing.type_check_only
class CodebaseSource(typing.TypedDict, total=False):
    author: UserMetadata
    branch: str
    commit: str
    commitMessage: str
    commitTime: str
    displayName: str
    hash: str
    repository: str
    uri: str

@typing.type_check_only
class Config(typing.TypedDict, total=False):
    effectiveEnv: _list[EnvironmentVariable]
    env: _list[EnvironmentVariable]
    runConfig: RunConfig

@typing.type_check_only
class ContainerSource(typing.TypedDict, total=False):
    image: str

@typing.type_check_only
class CustomDomainOperationMetadata(typing.TypedDict, total=False):
    certState: typing.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_NON_FAH",
        "HOST_CONFLICT",
        "HOST_WRONG_SHARD",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    liveMigrationSteps: _list[LiveMigrationStep]
    ownershipState: typing.Literal[
        "OWNERSHIP_STATE_UNSPECIFIED",
        "OWNERSHIP_MISSING",
        "OWNERSHIP_UNREACHABLE",
        "OWNERSHIP_MISMATCH",
        "OWNERSHIP_CONFLICT",
        "OWNERSHIP_PENDING",
        "OWNERSHIP_ACTIVE",
    ]
    quickSetupUpdates: _list[DnsUpdates]

@typing.type_check_only
class CustomDomainStatus(typing.TypedDict, total=False):
    certState: typing.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_NON_FAH",
        "HOST_CONFLICT",
        "HOST_WRONG_SHARD",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    ownershipState: typing.Literal[
        "OWNERSHIP_STATE_UNSPECIFIED",
        "OWNERSHIP_MISSING",
        "OWNERSHIP_UNREACHABLE",
        "OWNERSHIP_MISMATCH",
        "OWNERSHIP_CONFLICT",
        "OWNERSHIP_PENDING",
        "OWNERSHIP_ACTIVE",
    ]
    requiredDnsUpdates: _list[DnsUpdates]

@typing.type_check_only
class DnsRecord(typing.TypedDict, total=False):
    domainName: str
    rdata: str
    relevantState: _list[
        typing.Literal[
            "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
            "HOST_STATE",
            "OWNERSHIP_STATE",
            "CERT_STATE",
        ]
    ]
    requiredAction: typing.Literal["NONE", "ADD", "REMOVE"]
    type: typing.Literal["TYPE_UNSPECIFIED", "A", "CNAME", "TXT", "AAAA", "CAA"]

@typing.type_check_only
class DnsRecordSet(typing.TypedDict, total=False):
    checkError: Status
    domainName: str
    records: _list[DnsRecord]

@typing.type_check_only
class DnsUpdates(typing.TypedDict, total=False):
    checkTime: str
    desired: _list[DnsRecordSet]
    discovered: _list[DnsRecordSet]
    domainName: str

@typing.type_check_only
class Domain(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    customDomainStatus: CustomDomainStatus
    deleteTime: str
    disabled: bool
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    purgeTime: str
    reconciling: bool
    serve: ServingBehavior
    type: typing.Literal["TYPE_UNSPECIFIED", "DEFAULT", "CUSTOM"]
    uid: str
    updateTime: str

@typing.type_check_only
class DomainOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    customDomainOperationMetadata: CustomDomainOperationMetadata
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentVariable(typing.TypedDict, total=False):
    availability: _list[typing.Literal["AVAILABILITY_UNSPECIFIED", "BUILD", "RUNTIME"]]
    origin: typing.Literal[
        "ORIGIN_UNSPECIFIED",
        "BACKEND_OVERRIDES",
        "BUILD_CONFIG",
        "APPHOSTING_YAML",
        "FIREBASE_SYSTEM",
    ]
    originFileName: str
    secret: str
    value: str
    variable: str

@typing.type_check_only
class Error(typing.TypedDict, total=False):
    cloudResource: str
    error: Status
    errorSource: typing.Literal["ERROR_SOURCE_UNSPECIFIED", "CLOUD_BUILD", "CLOUD_RUN"]

@typing.type_check_only
class ListBackendsResponse(typing.TypedDict, total=False):
    backends: _list[Backend]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBuildsResponse(typing.TypedDict, total=False):
    builds: _list[Build]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDomainsResponse(typing.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListRolloutsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]
    unreachable: _list[str]

@typing.type_check_only
class ListSupportedRuntimesResponse(typing.TypedDict, total=False):
    supportedRuntimes: _list[SupportedRuntime]

@typing.type_check_only
class LiveMigrationStep(typing.TypedDict, total=False):
    dnsUpdates: _list[DnsUpdates]
    issues: _list[Status]
    relevantDomainStates: _list[
        typing.Literal[
            "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
            "HOST_STATE",
            "OWNERSHIP_STATE",
            "CERT_STATE",
        ]
    ]
    stepState: typing.Literal[
        "STEP_STATE_UNSPECIFIED",
        "PREPARING",
        "PENDING",
        "INCOMPLETE",
        "PROCESSING",
        "COMPLETE",
    ]

@typing.type_check_only
class LocallyBuiltSource(typing.TypedDict, total=False):
    description: str
    env: _list[EnvironmentVariable]
    rootDirectory: str
    runCommand: str
    runConfig: RunConfig
    userStorageUri: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagedResource(typing.TypedDict, total=False):
    runService: RunService

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Path(typing.TypedDict, total=False):
    pattern: str
    type: typing.Literal["PATTERN_TYPE_UNSPECIFIED", "RE2", "GLOB", "PREFIX"]

@typing.type_check_only
class Redirect(typing.TypedDict, total=False):
    status: str
    uri: str

@typing.type_check_only
class Rollout(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    build: str
    createTime: str
    deleteTime: str
    displayName: str
    error: Status
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PENDING_BUILD",
        "PROGRESSING",
        "PAUSED",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "SKIPPED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class RolloutPolicy(typing.TypedDict, total=False):
    codebaseBranch: str
    disabled: bool
    disabledTime: str
    ignoredPaths: _list[Path]
    requiredPaths: _list[Path]

@typing.type_check_only
class RunConfig(typing.TypedDict, total=False):
    concurrency: int
    cpu: float
    maxInstances: int
    memoryMib: int
    minInstances: int

@typing.type_check_only
class RunService(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class ServingBehavior(typing.TypedDict, total=False):
    redirect: Redirect

@typing.type_check_only
class SourceUserMetadata(typing.TypedDict, total=False):
    displayName: str
    email: str
    imageUri: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedRuntime(typing.TypedDict, total=False):
    automaticBaseImageUpdatesSupported: bool
    decommissionTime: str
    deprecateTime: str
    name: str
    runtimeId: str

@typing.type_check_only
class Traffic(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    current: TrafficSet
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    rolloutPolicy: RolloutPolicy
    target: TrafficSet
    uid: str
    updateTime: str

@typing.type_check_only
class TrafficSet(typing.TypedDict, total=False):
    splits: _list[TrafficSplit]

@typing.type_check_only
class TrafficSplit(typing.TypedDict, total=False):
    build: str
    percent: int

@typing.type_check_only
class UserMetadata(typing.TypedDict, total=False):
    displayName: str
    email: str
    imageUri: str
