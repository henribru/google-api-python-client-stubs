import typing

_list = list

@typing.type_check_only
class Assignment(typing.TypedDict, total=False):
    assignee: str
    enableGeminiInBigquery: bool
    jobType: typing.Literal[
        "JOB_TYPE_UNSPECIFIED",
        "PIPELINE",
        "QUERY",
        "ML_EXTERNAL",
        "BACKGROUND",
        "CONTINUOUS",
        "BACKGROUND_CHANGE_DATA_CAPTURE",
        "BACKGROUND_COLUMN_METADATA_INDEX",
        "BACKGROUND_SEARCH_INDEX_REFRESH",
        "AUTOMATIC_MATERIALIZED_VIEW_REFRESH",
    ]
    name: str
    principal: str
    schedulingPolicy: SchedulingPolicy
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Autoscale(typing.TypedDict, total=False):
    currentSlots: str
    maxSlots: str

@typing.type_check_only
class BiReservation(typing.TypedDict, total=False):
    name: str
    preferredTables: _list[TableReference]
    size: str
    updateTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CapacityCommitment(typing.TypedDict, total=False):
    commitmentEndTime: str
    commitmentStartTime: str
    edition: typing.Literal[
        "EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    failureStatus: Status
    isFlatRate: bool
    multiRegionAuxiliary: bool
    name: str
    plan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "FLEX",
        "FLEX_FLAT_RATE",
        "TRIAL",
        "MONTHLY",
        "MONTHLY_FLAT_RATE",
        "ANNUAL",
        "ANNUAL_FLAT_RATE",
        "THREE_YEAR",
        "NONE",
    ]
    renewalPlan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED",
        "FLEX",
        "FLEX_FLAT_RATE",
        "TRIAL",
        "MONTHLY",
        "MONTHLY_FLAT_RATE",
        "ANNUAL",
        "ANNUAL_FLAT_RATE",
        "THREE_YEAR",
        "NONE",
    ]
    slotCount: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FailoverReservationRequest(typing.TypedDict, total=False):
    failoverMode: typing.Literal["FAILOVER_MODE_UNSPECIFIED", "SOFT", "HARD"]

@typing.type_check_only
class ListAssignmentsResponse(typing.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class ListCapacityCommitmentsResponse(typing.TypedDict, total=False):
    capacityCommitments: _list[CapacityCommitment]
    nextPageToken: str

@typing.type_check_only
class ListReservationGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reservationGroups: _list[ReservationGroup]

@typing.type_check_only
class ListReservationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class MergeCapacityCommitmentsRequest(typing.TypedDict, total=False):
    capacityCommitmentId: str
    capacityCommitmentIds: _list[str]

@typing.type_check_only
class MoveAssignmentRequest(typing.TypedDict, total=False):
    assignmentId: str
    destinationId: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReplicationStatus(typing.TypedDict, total=False):
    error: Status
    lastErrorTime: str
    lastReplicationTime: str
    softFailoverStartTime: str

@typing.type_check_only
class Reservation(typing.TypedDict, total=False):
    autoscale: Autoscale
    concurrency: str
    creationTime: str
    edition: typing.Literal[
        "EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    ignoreIdleSlots: bool
    labels: dict[str, typing.Any]
    maxSlots: str
    multiRegionAuxiliary: bool
    name: str
    originalPrimaryLocation: str
    primaryLocation: str
    replicationStatus: ReplicationStatus
    reservationGroup: str
    reservationGroupPath: _list[str]
    scalingMode: typing.Literal[
        "SCALING_MODE_UNSPECIFIED", "AUTOSCALE_ONLY", "IDLE_SLOTS_ONLY", "ALL_SLOTS"
    ]
    schedulingPolicy: SchedulingPolicy
    secondaryLocation: str
    slotCapacity: str
    updateTime: str

@typing.type_check_only
class ReservationGroup(typing.TypedDict, total=False):
    name: str
    parentGroup: str

@typing.type_check_only
class SchedulingPolicy(typing.TypedDict, total=False):
    concurrency: str
    maxSlots: str

@typing.type_check_only
class SearchAllAssignmentsResponse(typing.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class SearchAssignmentsResponse(typing.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SplitCapacityCommitmentRequest(typing.TypedDict, total=False):
    slotCount: str

@typing.type_check_only
class SplitCapacityCommitmentResponse(typing.TypedDict, total=False):
    first: CapacityCommitment
    second: CapacityCommitment

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableReference(typing.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
