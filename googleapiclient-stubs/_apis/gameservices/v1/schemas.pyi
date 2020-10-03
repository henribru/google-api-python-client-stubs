import typing

import typing_extensions

class ListGameServerDeploymentsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    gameServerDeployments: typing.List[GameServerDeployment]
    nextPageToken: str

class TargetState(typing_extensions.TypedDict, total=False):
    details: typing.List[TargetDetails]

class PreviewGameServerDeploymentRolloutResponse(
    typing_extensions.TypedDict, total=False
):
    etag: str
    unavailable: typing.List[str]
    targetState: TargetState

class LabelSelector(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class GameServerConfigOverride(typing_extensions.TypedDict, total=False):
    realmsSelector: RealmSelector
    configVersion: str

class SpecSource(typing_extensions.TypedDict, total=False):
    name: str
    gameServerConfigName: str

class PreviewCreateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class PreviewUpdateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GameServerCluster(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    etag: str
    updateTime: str
    description: str
    connectionInfo: GameServerClusterConnectionInfo
    name: str
    createTime: str

class ListGameServerConfigsResponse(typing_extensions.TypedDict, total=False):
    gameServerConfigs: typing.List[GameServerConfig]
    unreachable: typing.List[str]
    nextPageToken: str

class GameServerConfig(typing_extensions.TypedDict, total=False):
    name: str
    updateTime: str
    createTime: str
    fleetConfigs: typing.List[FleetConfig]
    labels: typing.Dict[str, typing.Any]
    description: str
    scalingConfigs: typing.List[ScalingConfig]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class GameServerClusterConnectionInfo(typing_extensions.TypedDict, total=False):
    gkeClusterReference: GkeClusterReference
    namespace: str

class PreviewDeleteGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class FetchDeploymentStateResponse(typing_extensions.TypedDict, total=False):
    clusterState: typing.List[DeployedClusterState]
    unavailable: typing.List[str]

class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: CloudAuditOptions
    dataAccess: DataAccessOptions
    counter: CounterOptions

class ScalingConfig(typing_extensions.TypedDict, total=False):
    schedules: typing.List[Schedule]
    name: str
    selectors: typing.List[LabelSelector]
    fleetAutoscalerSpec: str

class Schedule(typing_extensions.TypedDict, total=False):
    cronJobDuration: str
    cronSpec: str
    endTime: str
    startTime: str

class TargetFleet(typing_extensions.TypedDict, total=False):
    specSource: SpecSource
    name: str

class GkeClusterReference(typing_extensions.TypedDict, total=False):
    cluster: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    createTime: str
    requestedCancellation: bool
    apiVersion: str
    operationStatus: typing.Dict[str, typing.Any]
    unreachable: typing.List[str]
    statusMessage: str
    target: str
    verb: str

class TargetFleetDetails(typing_extensions.TypedDict, total=False):
    autoscaler: TargetFleetAutoscaler
    fleet: TargetFleet

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Location(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str

class FetchDeploymentStateRequest(typing_extensions.TypedDict, total=False): ...

class PreviewRealmUpdateResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class Realm(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    labels: typing.Dict[str, typing.Any]
    etag: str
    updateTime: str
    createTime: str
    timeZone: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    bindingId: str
    condition: Expr
    members: typing.List[str]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class DeployedFleet(typing_extensions.TypedDict, total=False):
    status: DeployedFleetStatus
    specSource: SpecSource
    fleetSpec: str
    fleet: str

class DataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_MODE_UNSPECIFIED", "LOG_FAIL_CLOSED"]

class GameServerDeployment(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    description: str
    etag: str
    updateTime: str
    createTime: str

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "PERMISSION_TYPE_UNSPECIFIED",
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
    ]

class RealmSelector(typing_extensions.TypedDict, total=False):
    realms: typing.List[str]

class DeployedFleetStatus(typing_extensions.TypedDict, total=False):
    allocatedReplicas: str
    readyReplicas: str
    reservedReplicas: str
    replicas: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    error: Status

class Empty(typing_extensions.TypedDict, total=False): ...

class ListGameServerClustersResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    nextPageToken: str
    gameServerClusters: typing.List[GameServerCluster]

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    exemptedMembers: typing.List[str]
    auditLogConfigs: typing.List[AuditLogConfig]

class ListRealmsResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    realms: typing.List[Realm]
    nextPageToken: str

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int
    etag: str
    rules: typing.List[Rule]
    iamOwned: bool

class DeployedClusterState(typing_extensions.TypedDict, total=False):
    cluster: str
    fleetDetails: typing.List[DeployedFleetDetails]

class GameServerDeploymentRollout(typing_extensions.TypedDict, total=False):
    name: str
    defaultGameServerConfig: str
    updateTime: str
    etag: str
    gameServerConfigOverrides: typing.List[GameServerConfigOverride]
    createTime: str

class TargetFleetAutoscaler(typing_extensions.TypedDict, total=False):
    name: str
    specSource: SpecSource

class DeployedFleetAutoscaler(typing_extensions.TypedDict, total=False):
    specSource: SpecSource
    fleetAutoscalerSpec: str
    autoscaler: str

class FleetConfig(typing_extensions.TypedDict, total=False):
    fleetSpec: str
    name: str

class CustomField(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class Condition(typing_extensions.TypedDict, total=False):
    svc: str
    sys: typing_extensions.Literal["NO_ATTR", "REGION", "SERVICE", "NAME", "IP"]
    values: typing.List[str]
    iam: typing_extensions.Literal[
        "NO_ATTR",
        "AUTHORITY",
        "ATTRIBUTION",
        "SECURITY_REALM",
        "APPROVER",
        "JUSTIFICATION_TYPE",
        "CREDENTIALS_TYPE",
        "CREDS_ASSERTION",
    ]
    op: typing_extensions.Literal[
        "NO_OP", "EQUALS", "NOT_EQUALS", "IN", "NOT_IN", "DISCHARGED"
    ]

class TargetDetails(typing_extensions.TypedDict, total=False):
    fleetDetails: typing.List[TargetFleetDetails]
    gameServerDeploymentName: str
    gameServerClusterName: str

class CloudAuditOptions(typing_extensions.TypedDict, total=False):
    logName: typing_extensions.Literal[
        "UNSPECIFIED_LOG_NAME", "ADMIN_ACTIVITY", "DATA_ACCESS"
    ]
    authorizationLoggingOptions: AuthorizationLoggingOptions

class OperationStatus(typing_extensions.TypedDict, total=False):
    errorMessage: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "INTERNAL_ERROR",
        "PERMISSION_DENIED",
        "CLUSTER_CONNECTION",
    ]
    done: bool

class DeployedFleetDetails(typing_extensions.TypedDict, total=False):
    deployedFleet: DeployedFleet
    deployedAutoscaler: DeployedFleetAutoscaler

class CounterOptions(typing_extensions.TypedDict, total=False):
    metric: str
    customFields: typing.List[CustomField]
    field: str

Rule = typing_extensions.TypedDict(
    "Rule",
    {
        "logConfig": typing.List[LogConfig],
        "conditions": typing.List[Condition],
        "permissions": typing.List[str],
        "action": typing_extensions.Literal[
            "NO_ACTION", "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG"
        ],
        "in": typing.List[str],
        "description": str,
        "notIn": typing.List[str],
    },
    total=False,
)
