import typing

import typing_extensions

_list = list

@typing.type_check_only
class Aggregate(typing_extensions.TypedDict, total=False):
    count: int
    group: str

@typing.type_check_only
class Blueprint(typing_extensions.TypedDict, total=False):
    engine: str
    package: str
    version: str

@typing.type_check_only
class Dependency(typing_extensions.TypedDict, total=False):
    alias: str
    unitKind: str

@typing.type_check_only
class Deprovision(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorBudget(typing_extensions.TypedDict, total=False):
    allowedCount: int
    allowedPercentage: int

@typing.type_check_only
class FromMapping(typing_extensions.TypedDict, total=False):
    dependency: str
    outputVariable: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]
    unreachable: _list[str]

@typing.type_check_only
class ListRolloutKindsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rolloutKinds: _list[RolloutKind]
    unreachable: _list[str]

@typing.type_check_only
class ListRolloutsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]
    unreachable: _list[str]

@typing.type_check_only
class ListSaasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    saas: _list[Saas]
    unreachable: _list[str]

@typing.type_check_only
class ListTenantsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tenants: _list[Tenant]
    unreachable: _list[str]

@typing.type_check_only
class ListUnitKindsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unitKinds: _list[UnitKind]
    unreachable: _list[str]

@typing.type_check_only
class ListUnitOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unitOperations: _list[UnitOperation]
    unreachable: _list[str]

@typing.type_check_only
class ListUnitsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    units: _list[Unit]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class MaintenanceSettings(typing_extensions.TypedDict, total=False):
    pinnedUntilTime: str

@typing.type_check_only
class Provision(typing_extensions.TypedDict, total=False):
    inputVariables: _list[UnitVariable]
    release: str

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    blueprint: Blueprint
    createTime: str
    etag: str
    inputVariableDefaults: _list[UnitVariable]
    inputVariables: _list[UnitVariable]
    labels: dict[str, typing.Any]
    name: str
    outputVariables: _list[UnitVariable]
    releaseRequirements: ReleaseRequirements
    uid: str
    unitKind: str
    updateTime: str

@typing.type_check_only
class ReleaseRequirements(typing_extensions.TypedDict, total=False):
    upgradeableFromReleases: _list[str]

@typing.type_check_only
class Rollout(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    control: RolloutControl
    createTime: str
    deleteTime: str
    effectiveUnitFilter: str
    endTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    parentRollout: str
    release: str
    rolloutKind: str
    rolloutOrchestrationStrategy: str
    rootRollout: str
    startTime: str
    state: typing_extensions.Literal[
        "ROLLOUT_STATE_UNSPECIFIED",
        "ROLLOUT_STATE_RUNNING",
        "ROLLOUT_STATE_PAUSED",
        "ROLLOUT_STATE_SUCCEEDED",
        "ROLLOUT_STATE_FAILED",
        "ROLLOUT_STATE_CANCELLED",
        "ROLLOUT_STATE_WAITING",
        "ROLLOUT_STATE_CANCELLING",
        "ROLLOUT_STATE_RESUMING",
        "ROLLOUT_STATE_PAUSING",
    ]
    stateMessage: str
    stateTransitionTime: str
    stats: RolloutStats
    uid: str
    unitFilter: str
    updateTime: str

@typing.type_check_only
class RolloutControl(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ROLLOUT_ACTION_UNSPECIFIED",
        "ROLLOUT_ACTION_RUN",
        "ROLLOUT_ACTION_PAUSE",
        "ROLLOUT_ACTION_CANCEL",
    ]
    runParams: RunRolloutActionParams

@typing.type_check_only
class RolloutKind(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    errorBudget: ErrorBudget
    etag: str
    labels: dict[str, typing.Any]
    maintenancePolicyEnforcement: typing_extensions.Literal[
        "MAINTENANCE_POLICY_ENFORCEMENT_UNSPECIFIED",
        "MAINTENANCE_POLICY_ENFORCEMENT_STRICT",
        "MAINTENANCE_POLICY_ENFORCEMENT_IGNORED",
        "MAINTENANCE_POLICY_ENFORCEMENT_SKIPPED",
    ]
    name: str
    rolloutOrchestrationStrategy: str
    uid: str
    unitFilter: str
    unitKind: str
    updateTime: str
    updateUnitKindStrategy: typing_extensions.Literal[
        "UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED",
        "UPDATE_UNIT_KIND_STRATEGY_ON_START",
        "UPDATE_UNIT_KIND_STRATEGY_NEVER",
    ]

@typing.type_check_only
class RolloutStats(typing_extensions.TypedDict, total=False):
    operationsByState: _list[Aggregate]

@typing.type_check_only
class RunRolloutActionParams(typing_extensions.TypedDict, total=False):
    retryFailedOperations: bool

@typing.type_check_only
class Saas(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    locations: _list[Location]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    startTime: str

@typing.type_check_only
class Tenant(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    consumerResource: str
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    saas: str
    uid: str
    updateTime: str

@typing.type_check_only
class ToMapping(typing_extensions.TypedDict, total=False):
    dependency: str
    ignoreForLookup: bool
    inputVariable: str

@typing.type_check_only
class Unit(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    conditions: _list[UnitCondition]
    createTime: str
    dependencies: _list[UnitDependency]
    dependents: _list[UnitDependency]
    etag: str
    inputVariables: _list[UnitVariable]
    labels: dict[str, typing.Any]
    maintenance: MaintenanceSettings
    managementMode: typing_extensions.Literal[
        "MANAGEMENT_MODE_UNSPECIFIED", "MANAGEMENT_MODE_USER", "MANAGEMENT_MODE_SYSTEM"
    ]
    name: str
    ongoingOperations: _list[str]
    outputVariables: _list[UnitVariable]
    pendingOperations: _list[str]
    release: str
    scheduledOperations: _list[str]
    state: typing_extensions.Literal[
        "UNIT_STATE_UNSPECIFIED",
        "UNIT_STATE_NOT_PROVISIONED",
        "UNIT_STATE_PROVISIONING",
        "UNIT_STATE_UPDATING",
        "UNIT_STATE_DEPROVISIONING",
        "UNIT_STATE_READY",
        "UNIT_STATE_ERROR",
    ]
    systemCleanupAt: str
    systemManagedState: typing_extensions.Literal[
        "SYSTEM_MANAGED_STATE_UNSPECIFIED",
        "SYSTEM_MANAGED_STATE_ACTIVE",
        "SYSTEM_MANAGED_STATE_INACTIVE",
        "SYSTEM_MANAGED_STATE_DECOMMISSIONED",
    ]
    tenant: str
    uid: str
    unitKind: str
    updateTime: str

@typing.type_check_only
class UnitCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "STATUS_UNKNOWN", "STATUS_TRUE", "STATUS_FALSE"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_READY",
        "TYPE_UPDATING",
        "TYPE_PROVISIONED",
        "TYPE_OPERATION_ERROR",
    ]

@typing.type_check_only
class UnitDependency(typing_extensions.TypedDict, total=False):
    alias: str
    unit: str

@typing.type_check_only
class UnitKind(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    defaultRelease: str
    dependencies: _list[Dependency]
    etag: str
    inputVariableMappings: _list[VariableMapping]
    labels: dict[str, typing.Any]
    name: str
    outputVariableMappings: _list[VariableMapping]
    saas: str
    uid: str
    updateTime: str

@typing.type_check_only
class UnitOperation(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    cancel: bool
    conditions: _list[UnitOperationCondition]
    createTime: str
    deleteTime: str
    deprovision: Deprovision
    engineState: str
    errorCategory: typing_extensions.Literal[
        "UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED",
        "NOT_APPLICABLE",
        "FATAL",
        "RETRIABLE",
        "IGNORABLE",
        "STANDARD",
    ]
    etag: str
    labels: dict[str, typing.Any]
    name: str
    parentUnitOperation: str
    provision: Provision
    rollout: str
    schedule: Schedule
    state: typing_extensions.Literal[
        "UNIT_OPERATION_STATE_UNKNOWN",
        "UNIT_OPERATION_STATE_PENDING",
        "UNIT_OPERATION_STATE_SCHEDULED",
        "UNIT_OPERATION_STATE_RUNNING",
        "UNIT_OPERATION_STATE_SUCCEEDED",
        "UNIT_OPERATION_STATE_FAILED",
        "UNIT_OPERATION_STATE_CANCELLED",
    ]
    uid: str
    unit: str
    updateTime: str
    upgrade: Upgrade

@typing.type_check_only
class UnitOperationCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "STATUS_UNKNOWN", "STATUS_TRUE", "STATUS_FALSE"
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "TYPE_SCHEDULED",
        "TYPE_RUNNING",
        "TYPE_SUCCEEDED",
        "TYPE_CANCELLED",
        "TYPE_APP_CREATED",
        "TYPE_APP_COMPONENTS_REGISTERED",
    ]

@typing.type_check_only
class UnitVariable(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "STRING", "INT", "BOOL"]
    value: str
    variable: str

@typing.type_check_only
class Upgrade(typing_extensions.TypedDict, total=False):
    inputVariables: _list[UnitVariable]
    release: str

AlternativeVariableMapping = typing_extensions.TypedDict(
    "AlternativeVariableMapping",
    {
        "from": FromMapping,
        "to": ToMapping,
        "variable": str,
    },
    total=False,
)

@typing.type_check_only
class VariableMapping(AlternativeVariableMapping): ...
