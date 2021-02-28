import typing

import typing_extensions
@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    exemptedMembers: typing.List[str]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: typing_extensions.Literal[
        "PERMISSION_TYPE_UNSPECIFIED",
        "ADMIN_READ",
        "ADMIN_WRITE",
        "DATA_READ",
        "DATA_WRITE",
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudAuditOptions(typing_extensions.TypedDict, total=False):
    authorizationLoggingOptions: AuthorizationLoggingOptions
    logName: typing_extensions.Literal[
        "UNSPECIFIED_LOG_NAME", "ADMIN_ACTIVITY", "DATA_ACCESS"
    ]

@typing.type_check_only
class Condition(typing_extensions.TypedDict, total=False):
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
    sys: typing_extensions.Literal["NO_ATTR", "REGION", "SERVICE", "NAME", "IP"]
    values: typing.List[str]

@typing.type_check_only
class CounterOptions(typing_extensions.TypedDict, total=False):
    customFields: typing.List[CustomField]
    field: str
    metric: str

@typing.type_check_only
class CustomField(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class DataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: typing_extensions.Literal["LOG_MODE_UNSPECIFIED", "LOG_FAIL_CLOSED"]

@typing.type_check_only
class DeployedClusterState(typing_extensions.TypedDict, total=False):
    cluster: str
    fleetDetails: typing.List[DeployedFleetDetails]

@typing.type_check_only
class DeployedFleet(typing_extensions.TypedDict, total=False):
    fleet: str
    fleetSpec: str
    specSource: SpecSource
    status: DeployedFleetStatus

@typing.type_check_only
class DeployedFleetAutoscaler(typing_extensions.TypedDict, total=False):
    autoscaler: str
    fleetAutoscalerSpec: str
    specSource: SpecSource

@typing.type_check_only
class DeployedFleetDetails(typing_extensions.TypedDict, total=False):
    deployedAutoscaler: DeployedFleetAutoscaler
    deployedFleet: DeployedFleet

@typing.type_check_only
class DeployedFleetStatus(typing_extensions.TypedDict, total=False):
    allocatedReplicas: str
    readyReplicas: str
    replicas: str
    reservedReplicas: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FetchDeploymentStateRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchDeploymentStateResponse(typing_extensions.TypedDict, total=False):
    clusterState: typing.List[DeployedClusterState]
    unavailable: typing.List[str]

@typing.type_check_only
class FleetConfig(typing_extensions.TypedDict, total=False):
    fleetSpec: str
    name: str

@typing.type_check_only
class GameServerCluster(typing_extensions.TypedDict, total=False):
    allocationPriority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "P1", "P2", "P3", "P4"
    ]
    connectionInfo: GameServerClusterConnectionInfo
    createTime: str
    description: str
    etag: str
    labels: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GameServerClusterConnectionInfo(typing_extensions.TypedDict, total=False):
    gkeClusterReference: GkeClusterReference
    gkeHubClusterReference: GkeHubClusterReference
    namespace: str

@typing.type_check_only
class GameServerConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    fleetConfigs: typing.List[FleetConfig]
    labels: typing.Dict[str, typing.Any]
    name: str
    scalingConfigs: typing.List[ScalingConfig]
    updateTime: str

@typing.type_check_only
class GameServerConfigOverride(typing_extensions.TypedDict, total=False):
    configVersion: str
    realmsSelector: RealmSelector

@typing.type_check_only
class GameServerDeployment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GameServerDeploymentRollout(typing_extensions.TypedDict, total=False):
    createTime: str
    defaultGameServerConfig: str
    etag: str
    gameServerConfigOverrides: typing.List[GameServerConfigOverride]
    name: str
    updateTime: str

@typing.type_check_only
class GkeClusterReference(typing_extensions.TypedDict, total=False):
    cluster: str

@typing.type_check_only
class GkeHubClusterReference(typing_extensions.TypedDict, total=False):
    membership: str

@typing.type_check_only
class LabelSelector(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]

@typing.type_check_only
class ListGameServerClustersResponse(typing_extensions.TypedDict, total=False):
    gameServerClusters: typing.List[GameServerCluster]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListGameServerConfigsResponse(typing_extensions.TypedDict, total=False):
    gameServerConfigs: typing.List[GameServerConfig]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListGameServerDeploymentsResponse(typing_extensions.TypedDict, total=False):
    gameServerDeployments: typing.List[GameServerDeployment]
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListRealmsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    realms: typing.List[Realm]
    unreachable: typing.List[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: CloudAuditOptions
    counter: CounterOptions
    dataAccess: DataAccessOptions

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    operationStatus: typing.Dict[str, typing.Any]
    requestedCancellation: bool
    statusMessage: str
    target: str
    unreachable: typing.List[str]
    verb: str

@typing.type_check_only
class OperationStatus(typing_extensions.TypedDict, total=False):
    done: bool
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "INTERNAL_ERROR",
        "PERMISSION_DENIED",
        "CLUSTER_CONNECTION",
    ]
    errorMessage: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    iamOwned: bool
    rules: typing.List[Rule]
    version: int

@typing.type_check_only
class PreviewCreateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

@typing.type_check_only
class PreviewDeleteGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

@typing.type_check_only
class PreviewGameServerDeploymentRolloutResponse(
    typing_extensions.TypedDict, total=False
):
    etag: str
    targetState: TargetState
    unavailable: typing.List[str]

@typing.type_check_only
class PreviewRealmUpdateResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

@typing.type_check_only
class PreviewUpdateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    etag: str
    targetState: TargetState

@typing.type_check_only
class Realm(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    etag: str
    labels: typing.Dict[str, typing.Any]
    name: str
    timeZone: str
    updateTime: str

@typing.type_check_only
class RealmSelector(typing_extensions.TypedDict, total=False):
    realms: typing.List[str]

AlternativeRule = typing_extensions.TypedDict(
    "AlternativeRule",
    {
        "action": typing_extensions.Literal[
            "NO_ACTION", "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG"
        ],
        "conditions": typing.List[Condition],
        "description": str,
        "in": typing.List[str],
        "logConfig": typing.List[LogConfig],
        "notIn": typing.List[str],
        "permissions": typing.List[str],
    },
    total=False,
)
@typing.type_check_only
class Rule(AlternativeRule): ...

@typing.type_check_only
class ScalingConfig(typing_extensions.TypedDict, total=False):
    fleetAutoscalerSpec: str
    name: str
    schedules: typing.List[Schedule]
    selectors: typing.List[LabelSelector]

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    cronJobDuration: str
    cronSpec: str
    endTime: str
    startTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SpecSource(typing_extensions.TypedDict, total=False):
    gameServerConfigName: str
    name: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetDetails(typing_extensions.TypedDict, total=False):
    fleetDetails: typing.List[TargetFleetDetails]
    gameServerClusterName: str
    gameServerDeploymentName: str

@typing.type_check_only
class TargetFleet(typing_extensions.TypedDict, total=False):
    name: str
    specSource: SpecSource

@typing.type_check_only
class TargetFleetAutoscaler(typing_extensions.TypedDict, total=False):
    name: str
    specSource: SpecSource

@typing.type_check_only
class TargetFleetDetails(typing_extensions.TypedDict, total=False):
    autoscaler: TargetFleetAutoscaler
    fleet: TargetFleet

@typing.type_check_only
class TargetState(typing_extensions.TypedDict, total=False):
    details: typing.List[TargetDetails]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
