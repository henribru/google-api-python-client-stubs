import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    exemptedMembers: _list[str]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
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
    members: _list[str]
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
    values: _list[str]

@typing.type_check_only
class CounterOptions(typing_extensions.TypedDict, total=False):
    customFields: _list[CustomField]
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
    fleetDetails: _list[DeployedFleetDetails]

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
    clusterState: _list[DeployedClusterState]
    unavailable: _list[str]

@typing.type_check_only
class FleetConfig(typing_extensions.TypedDict, total=False):
    fleetSpec: str
    name: str

@typing.type_check_only
class GameServerCluster(typing_extensions.TypedDict, total=False):
    clusterState: KubernetesClusterState
    connectionInfo: GameServerClusterConnectionInfo
    createTime: str
    description: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GameServerClusterConnectionInfo(typing_extensions.TypedDict, total=False):
    gkeClusterReference: GkeClusterReference
    namespace: str

@typing.type_check_only
class GameServerConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    fleetConfigs: _list[FleetConfig]
    labels: dict[str, typing.Any]
    name: str
    scalingConfigs: _list[ScalingConfig]
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
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class GameServerDeploymentRollout(typing_extensions.TypedDict, total=False):
    createTime: str
    defaultGameServerConfig: str
    etag: str
    gameServerConfigOverrides: _list[GameServerConfigOverride]
    name: str
    updateTime: str

@typing.type_check_only
class GkeClusterReference(typing_extensions.TypedDict, total=False):
    cluster: str

@typing.type_check_only
class KubernetesClusterState(typing_extensions.TypedDict, total=False):
    agonesVersionInstalled: str
    agonesVersionTargeted: str
    installationState: typing_extensions.Literal[
        "INSTALLATION_STATE_UNSPECIFIED",
        "AGONES_KUBERNETES_VERSION_SUPPORTED",
        "AGONES_VERSION_UNSUPPORTED",
        "AGONES_KUBERNETES_VERSION_UNSUPPORTED",
        "AGONES_VERSION_UNRECOGNIZED",
        "KUBERNETES_VERSION_UNRECOGNIZED",
        "VERSION_VERIFICATION_FAILED",
        "AGONES_NOT_INSTALLED",
    ]
    kubernetesVersionInstalled: str
    provider: str
    versionInstalledErrorMessage: str

@typing.type_check_only
class LabelSelector(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]

@typing.type_check_only
class ListGameServerClustersResponse(typing_extensions.TypedDict, total=False):
    gameServerClusters: _list[GameServerCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGameServerConfigsResponse(typing_extensions.TypedDict, total=False):
    gameServerConfigs: _list[GameServerConfig]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListGameServerDeploymentsResponse(typing_extensions.TypedDict, total=False):
    gameServerDeployments: _list[GameServerDeployment]
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
class ListRealmsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    realms: _list[Realm]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
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
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    operationStatus: dict[str, typing.Any]
    requestedCancellation: bool
    statusMessage: str
    target: str
    unreachable: _list[str]
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
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    iamOwned: bool
    rules: _list[Rule]
    version: int

@typing.type_check_only
class PreviewCreateGameServerClusterResponse(typing_extensions.TypedDict, total=False):
    clusterState: KubernetesClusterState
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
    unavailable: _list[str]

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
    labels: dict[str, typing.Any]
    name: str
    timeZone: str
    updateTime: str

@typing.type_check_only
class RealmSelector(typing_extensions.TypedDict, total=False):
    realms: _list[str]

AlternativeRule = typing_extensions.TypedDict(
    "AlternativeRule",
    {
        "action": typing_extensions.Literal[
            "NO_ACTION", "ALLOW", "ALLOW_WITH_LOG", "DENY", "DENY_WITH_LOG", "LOG"
        ],
        "conditions": _list[Condition],
        "description": str,
        "in": _list[str],
        "logConfig": _list[LogConfig],
        "notIn": _list[str],
        "permissions": _list[str],
    },
    total=False,
)

@typing.type_check_only
class Rule(AlternativeRule): ...

@typing.type_check_only
class ScalingConfig(typing_extensions.TypedDict, total=False):
    fleetAutoscalerSpec: str
    name: str
    schedules: _list[Schedule]
    selectors: _list[LabelSelector]

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
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetDetails(typing_extensions.TypedDict, total=False):
    fleetDetails: _list[TargetFleetDetails]
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
    details: _list[TargetDetails]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
