import typing

import typing_extensions

_list = list

@typing.type_check_only
class Assignment(typing_extensions.TypedDict, total=False):
    assignee: str
    enableGeminiInBigquery: bool
    jobType: typing_extensions.Literal[
        "JOB_TYPE_UNSPECIFIED",
        "PIPELINE",
        "QUERY",
        "ML_EXTERNAL",
        "BACKGROUND",
        "CONTINUOUS",
        "BACKGROUND_CHANGE_DATA_CAPTURE",
        "BACKGROUND_COLUMN_METADATA_INDEX",
        "BACKGROUND_SEARCH_INDEX_REFRESH",
    ]
    name: str
    schedulingPolicy: SchedulingPolicy
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Autoscale(typing_extensions.TypedDict, total=False):
    currentSlots: str
    maxSlots: str

@typing.type_check_only
class BiReservation(typing_extensions.TypedDict, total=False):
    name: str
    preferredTables: _list[TableReference]
    size: str
    updateTime: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CapacityCommitment(typing_extensions.TypedDict, total=False):
    commitmentEndTime: str
    commitmentStartTime: str
    edition: typing_extensions.Literal[
        "EDITION_UNSPECIFIED", "STANDARD", "ENTERPRISE", "ENTERPRISE_PLUS"
    ]
    failureStatus: Status
    isFlatRate: bool
    multiRegionAuxiliary: bool
    name: str
    plan: typing_extensions.Literal[
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
    renewalPlan: typing_extensions.Literal[
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
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FailoverReservationRequest(typing_extensions.TypedDict, total=False):
    failoverMode: typing_extensions.Literal["FAILOVER_MODE_UNSPECIFIED", "SOFT", "HARD"]

@typing.type_check_only
class ListAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class ListCapacityCommitmentsResponse(typing_extensions.TypedDict, total=False):
    capacityCommitments: _list[CapacityCommitment]
    nextPageToken: str

@typing.type_check_only
class ListReservationGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservationGroups: _list[ReservationGroup]

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class MergeCapacityCommitmentsRequest(typing_extensions.TypedDict, total=False):
    capacityCommitmentId: str
    capacityCommitmentIds: _list[str]

@typing.type_check_only
class MoveAssignmentRequest(typing_extensions.TypedDict, total=False):
    assignmentId: str
    destinationId: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ReplicationStatus(typing_extensions.TypedDict, total=False):
    error: Status
    lastErrorTime: str
    lastReplicationTime: str
    softFailoverStartTime: str

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    autoscale: Autoscale
    concurrency: str
    creationTime: str
    edition: typing_extensions.Literal[
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
    scalingMode: typing_extensions.Literal[
        "SCALING_MODE_UNSPECIFIED", "AUTOSCALE_ONLY", "IDLE_SLOTS_ONLY", "ALL_SLOTS"
    ]
    schedulingPolicy: SchedulingPolicy
    secondaryLocation: str
    slotCapacity: str
    updateTime: str

@typing.type_check_only
class ReservationGroup(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class SchedulingPolicy(typing_extensions.TypedDict, total=False):
    concurrency: str
    maxSlots: str

@typing.type_check_only
class SearchAllAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class SearchAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SplitCapacityCommitmentRequest(typing_extensions.TypedDict, total=False):
    slotCount: str

@typing.type_check_only
class SplitCapacityCommitmentResponse(typing_extensions.TypedDict, total=False):
    first: CapacityCommitment
    second: CapacityCommitment

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str
    tableId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
