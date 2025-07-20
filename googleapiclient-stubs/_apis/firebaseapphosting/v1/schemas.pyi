import typing

import typing_extensions

_list = list

@typing.type_check_only
class Backend(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    appId: str
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
    reconciling: bool
    serviceAccount: str
    servingLocality: typing_extensions.Literal[
        "SERVING_LOCALITY_UNSPECIFIED", "REGIONAL_STRICT", "GLOBAL_ACCESS"
    ]
    uid: str
    updateTime: str
    uri: str

@typing.type_check_only
class Build(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    buildLogsUri: str
    config: Config
    createTime: str
    deleteTime: str
    displayName: str
    environment: str
    errors: _list[Error]
    etag: str
    image: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    source: BuildSource
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "BUILDING", "BUILT", "DEPLOYING", "READY", "FAILED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class BuildSource(typing_extensions.TypedDict, total=False):
    codebase: CodebaseSource
    container: ContainerSource

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Codebase(typing_extensions.TypedDict, total=False):
    repository: str
    rootDirectory: str

@typing.type_check_only
class CodebaseSource(typing_extensions.TypedDict, total=False):
    author: UserMetadata
    branch: str
    commit: str
    commitMessage: str
    commitTime: str
    displayName: str
    hash: str
    uri: str

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    env: _list[EnvironmentVariable]
    runConfig: RunConfig

@typing.type_check_only
class ContainerSource(typing_extensions.TypedDict, total=False):
    image: str

@typing.type_check_only
class CustomDomainOperationMetadata(typing_extensions.TypedDict, total=False):
    certState: typing_extensions.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing_extensions.Literal[
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
    ownershipState: typing_extensions.Literal[
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
class CustomDomainStatus(typing_extensions.TypedDict, total=False):
    certState: typing_extensions.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing_extensions.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_NON_FAH",
        "HOST_CONFLICT",
        "HOST_WRONG_SHARD",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    ownershipState: typing_extensions.Literal[
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
class DnsRecord(typing_extensions.TypedDict, total=False):
    domainName: str
    rdata: str
    relevantState: _list[
        typing_extensions.Literal[
            "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
            "HOST_STATE",
            "OWNERSHIP_STATE",
            "CERT_STATE",
        ]
    ]
    requiredAction: typing_extensions.Literal["NONE", "ADD", "REMOVE"]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "A", "CNAME", "TXT", "AAAA", "CAA"
    ]

@typing.type_check_only
class DnsRecordSet(typing_extensions.TypedDict, total=False):
    checkError: Status
    domainName: str
    records: _list[DnsRecord]

@typing.type_check_only
class DnsUpdates(typing_extensions.TypedDict, total=False):
    checkTime: str
    desired: _list[DnsRecordSet]
    discovered: _list[DnsRecordSet]
    domainName: str

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    customDomainStatus: CustomDomainStatus
    deleteTime: str
    disabled: bool
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    reconciling: bool
    serve: ServingBehavior
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DEFAULT", "CUSTOM"]
    uid: str
    updateTime: str

@typing.type_check_only
class DomainOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    customDomainOperationMetadata: CustomDomainOperationMetadata
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnvironmentVariable(typing_extensions.TypedDict, total=False):
    availability: _list[
        typing_extensions.Literal["AVAILABILITY_UNSPECIFIED", "BUILD", "RUNTIME"]
    ]
    secret: str
    value: str
    variable: str

@typing.type_check_only
class Error(typing_extensions.TypedDict, total=False):
    cloudResource: str
    error: Status
    errorSource: typing_extensions.Literal[
        "ERROR_SOURCE_UNSPECIFIED", "CLOUD_BUILD", "CLOUD_RUN"
    ]

@typing.type_check_only
class ListBackendsResponse(typing_extensions.TypedDict, total=False):
    backends: _list[Backend]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListBuildsResponse(typing_extensions.TypedDict, total=False):
    builds: _list[Build]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListRolloutsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]
    unreachable: _list[str]

@typing.type_check_only
class LiveMigrationStep(typing_extensions.TypedDict, total=False):
    dnsUpdates: _list[DnsUpdates]
    issues: _list[Status]
    relevantDomainStates: _list[
        typing_extensions.Literal[
            "CUSTOM_DOMAIN_STATE_UNSPECIFIED",
            "HOST_STATE",
            "OWNERSHIP_STATE",
            "CERT_STATE",
        ]
    ]
    stepState: typing_extensions.Literal[
        "STEP_STATE_UNSPECIFIED",
        "PREPARING",
        "PENDING",
        "INCOMPLETE",
        "PROCESSING",
        "COMPLETE",
    ]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagedResource(typing_extensions.TypedDict, total=False):
    runService: RunService

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Redirect(typing_extensions.TypedDict, total=False):
    status: str
    uri: str

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "PENDING_BUILD",
        "PROGRESSING",
        "PAUSED",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class RolloutPolicy(typing_extensions.TypedDict, total=False):
    codebaseBranch: str
    disabled: bool
    disabledTime: str

@typing.type_check_only
class RunConfig(typing_extensions.TypedDict, total=False):
    concurrency: int
    cpu: float
    maxInstances: int
    memoryMib: int
    minInstances: int

@typing.type_check_only
class RunService(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class ServingBehavior(typing_extensions.TypedDict, total=False):
    redirect: Redirect

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Traffic(typing_extensions.TypedDict, total=False):
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
class TrafficSet(typing_extensions.TypedDict, total=False):
    splits: _list[TrafficSplit]

@typing.type_check_only
class TrafficSplit(typing_extensions.TypedDict, total=False):
    build: str
    percent: int

@typing.type_check_only
class UserMetadata(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str
    imageUri: str
