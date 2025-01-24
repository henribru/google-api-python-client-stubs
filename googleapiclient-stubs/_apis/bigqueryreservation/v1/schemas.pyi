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
    ]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

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
class FailoverReservationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class ListCapacityCommitmentsResponse(typing_extensions.TypedDict, total=False):
    capacityCommitments: _list[CapacityCommitment]
    nextPageToken: str

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class MergeCapacityCommitmentsRequest(typing_extensions.TypedDict, total=False):
    capacityCommitmentIds: _list[str]

@typing.type_check_only
class MoveAssignmentRequest(typing_extensions.TypedDict, total=False):
    assignmentId: str
    destinationId: str

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
    multiRegionAuxiliary: bool
    name: str
    originalPrimaryLocation: str
    primaryLocation: str
    secondaryLocation: str
    slotCapacity: str
    updateTime: str

@typing.type_check_only
class SearchAllAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

@typing.type_check_only
class SearchAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: _list[Assignment]
    nextPageToken: str

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
