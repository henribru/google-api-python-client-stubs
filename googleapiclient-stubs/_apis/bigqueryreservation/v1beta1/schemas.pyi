import typing

_list = list

@typing.type_check_only
class Assignment(typing.TypedDict, total=False):
    assignee: str
    jobType: typing.Literal["JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY", "ML_EXTERNAL"]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

@typing.type_check_only
class BiReservation(typing.TypedDict, total=False):
    name: str
    preferredTables: _list[TableReference]
    size: str
    updateTime: str

@typing.type_check_only
class CapacityCommitment(typing.TypedDict, total=False):
    commitmentEndTime: str
    commitmentStartTime: str
    failureStatus: Status
    multiRegionAuxiliary: bool
    name: str
    plan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    renewalPlan: typing.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    slotCount: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListAssignmentsResponse(typing.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class ListCapacityCommitmentsResponse(typing.TypedDict, total=False):
    capacityCommitments: _list[CapacityCommitment]
    nextPageToken: str

@typing.type_check_only
class ListReservationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class MergeCapacityCommitmentsRequest(typing.TypedDict, total=False):
    capacityCommitmentIds: _list[str]

@typing.type_check_only
class MoveAssignmentRequest(typing.TypedDict, total=False):
    destinationId: str

@typing.type_check_only
class Reservation(typing.TypedDict, total=False):
    concurrency: str
    creationTime: str
    ignoreIdleSlots: bool
    multiRegionAuxiliary: bool
    name: str
    slotCapacity: str
    updateTime: str

@typing.type_check_only
class SearchAssignmentsResponse(typing.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

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
