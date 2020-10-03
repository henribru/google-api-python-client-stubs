import typing

import typing_extensions

class PreviewCreateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    targetState: TargetState
    etag: str

class Condition(typing_extensions.TypedDict, total=False):
    sys: typing_extensions.Literal["NO_ATTR", "REGION", "SERVICE", "NAME", "IP"]
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
    svc: str
    values: typing.List[str]

class CloudAuditOptions(typing_extensions.TypedDict, total=False):
    logName: typing_extensions.Literal[
        "UNSPECIFIED_LOG_NAME", "ADMIN_ACTIVITY", "DATA_ACCESS"
    ]
    authorizationLoggingOptions: AuthorizationLoggingOptions

class GameServerCluster(typing_extensions.TypedDict, total=False):
    createTime: str
    etag: str
    updateTime: str
    description: str
    name: str
    labels: typing.Dict[str, typing.Any]
    connectionInfo: GameServerClusterConnectionInfo

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TargetState(typing_extensions.TypedDict, total=False):
    details: typing.List[TargetDetails]

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    members: typing.List[str]
    condition: Expr
    role: str

class CustomField(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    title: str
    expression: str

class DeployedFleet(typing_extensions.TypedDict, total=False):
    status: DeployedFleetStatus
    specSource: SpecSource
    fleet: str
    fleetSpec: str

class LabelSelector(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

class DeployedFleetAutoscaler(typing_extensions.TypedDict, total=False):
    fleetAutoscalerSpec: str
    autoscaler: str
    specSource: SpecSource

class TargetFleetDetails(typing_extensions.TypedDict, total=False):
    fleet: TargetFleet
    autoscaler: TargetFleetAutoscaler

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DeployedClusterState(typing_extensions.TypedDict, total=False):
    cluster: str
    fleetDetails: typing.List[DeployedFleetDetails]

class PreviewDeleteGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class DataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_MODE_UNSPECIFIED", "LOG_FAIL_CLOSED"]

class TargetFleet(typing_extensions.TypedDict, total=False):
    name: str
    specSource: SpecSource

class RealmSelector(typing_extensions.TypedDict, total=False):
    realms: typing.List[str]

class CounterOptions(typing_extensions.TypedDict, total=False):
    field: str
    customFields: typing.List[CustomField]
    metric: str

class Empty(typing_extensions.TypedDict, total=False): ...

class ListGameServerConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: typing.List[str]
    gameServerConfigs: typing.List[GameServerConfig]

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "PERMISSION_TYPE_UNSPECIFIED",
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
    ]

class GameServerClusterConnectionInfo(typing_extensions.TypedDict, total=False):
    namespace: str
    gkeClusterReference: GkeClusterReference

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    locationId: str

class PreviewUpdateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    targetState: TargetState
    etag: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status

class SpecSource(typing_extensions.TypedDict, total=False):
    gameServerConfigName: str
    name: str

class Policy(typing_extensions.TypedDict, total=False):
    iamOwned: bool
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    rules: typing.List[Rule]
    etag: str
    version: int

class DeployedFleetStatus(typing_extensions.TypedDict, total=False):
    reservedReplicas: str
    allocatedReplicas: str
    readyReplicas: str
    replicas: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class DeployedFleetDetails(typing_extensions.TypedDict, total=False):
    deployedFleet: DeployedFleet
    deployedAutoscaler: DeployedFleetAutoscaler

class ScalingConfig(typing_extensions.TypedDict, total=False):
    fleetAutoscalerSpec: str
    schedules: typing.List[Schedule]
    selectors: typing.List[LabelSelector]
    name: str

class TargetDetails(typing_extensions.TypedDict, total=False):
    gameServerDeploymentName: str
    gameServerClusterName: str
    fleetDetails: typing.List[TargetFleetDetails]

class PreviewGameServerDeploymentRolloutResponse(
    typing_extensions.TypedDict, total=False
):
    unavailable: typing.List[str]
    etag: str
    targetState: TargetState

class GameServerConfig(typing_extensions.TypedDict, total=False):
    updateTime: str
    createTime: str
    name: str
    fleetConfigs: typing.List[FleetConfig]
    scalingConfigs: typing.List[ScalingConfig]
    labels: typing.Dict[str, typing.Any]
    description: str

class GameServerDeploymentRollout(typing_extensions.TypedDict, total=False):
    gameServerConfigOverrides: typing.List[GameServerConfigOverride]
    defaultGameServerConfig: str
    createTime: str
    etag: str
    updateTime: str
    name: str

class ListRealmsResponse(typing_extensions.TypedDict, total=False):
    realms: typing.List[Realm]
    unreachable: typing.List[str]
    nextPageToken: str

class GameServerDeployment(typing_extensions.TypedDict, total=False):
    updateTime: str
    labels: typing.Dict[str, typing.Any]
    name: str
    description: str
    etag: str
    createTime: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class FleetConfig(typing_extensions.TypedDict, total=False):
    name: str
    fleetSpec: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Realm(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    description: str
    timeZone: str
    updateTime: str
    name: str
    etag: str
    createTime: str

class PreviewRealmUpdateResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class OperationStatus(typing_extensions.TypedDict, total=False):
    done: bool
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "INTERNAL_ERROR",
        "PERMISSION_DENIED",
        "CLUSTER_CONNECTION",
    ]
    errorMessage: str

class ListGameServerDeploymentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: typing.List[str]
    gameServerDeployments: typing.List[GameServerDeployment]

class GkeClusterReference(typing_extensions.TypedDict, total=False):
    cluster: str

class Schedule(typing_extensions.TypedDict, total=False):
    cronJobDuration: str
    cronSpec: str
    endTime: str
    startTime: str

class FetchDeploymentStateRequest(typing_extensions.TypedDict, total=False): ...

class ListGameServerClustersResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    gameServerClusters: typing.List[GameServerCluster]
    nextPageToken: str

Rule = typing_extensions.TypedDict(
    "Rule",
    {
        "description": str,
        "in": typing.List[str],
        "permissions": typing.List[str],
        "conditions": typing.List[Condition],
        "action": typing_extensions.Literal[
            "NO_ACTION", "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG"
        ],
        "logConfig": typing.List[LogConfig],
        "notIn": typing.List[str],
    },
    total=False,
)

class OperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    verb: str
    apiVersion: str
    endTime: str
    operationStatus: typing.Dict[str, typing.Any]
    requestedCancellation: bool
    target: str
    statusMessage: str
    unreachable: typing.List[str]

class FetchDeploymentStateResponse(typing_extensions.TypedDict, total=False):
    clusterState: typing.List[DeployedClusterState]
    unavailable: typing.List[str]

class TargetFleetAutoscaler(typing_extensions.TypedDict, total=False):
    specSource: SpecSource
    name: str

class LogConfig(typing_extensions.TypedDict, total=False):
    counter: CounterOptions
    dataAccess: DataAccessOptions
    cloudAudit: CloudAuditOptions

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]
    exemptedMembers: typing.List[str]

class GameServerConfigOverride(typing_extensions.TypedDict, total=False):
    configVersion: str
    realmsSelector: RealmSelector
