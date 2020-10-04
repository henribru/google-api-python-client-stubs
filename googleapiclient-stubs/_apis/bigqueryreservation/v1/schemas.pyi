import typing

import typing_extensions
@typing.type_check_only
class Assignment(typing_extensions.TypedDict, total=False):
    assignee: str
    jobType: typing_extensions.Literal[
        "JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY", "ML_EXTERNAL"
    ]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

@typing.type_check_only
class BiReservation(typing_extensions.TypedDict, total=False):
    name: str
    size: str
    updateTime: str

@typing.type_check_only
class CapacityCommitment(typing_extensions.TypedDict, total=False):
    commitmentEndTime: str
    commitmentStartTime: str
    failureStatus: Status
    name: str
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    renewalPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    slotCount: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class CreateSlotPoolMetadata(typing_extensions.TypedDict, total=False):
    slotPool: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
    nextPageToken: str

@typing.type_check_only
class ListCapacityCommitmentsResponse(typing_extensions.TypedDict, total=False):
    capacityCommitments: typing.List[CapacityCommitment]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: typing.List[Reservation]

@typing.type_check_only
class MergeCapacityCommitmentsRequest(typing_extensions.TypedDict, total=False):
    capacityCommitmentIds: typing.List[str]

@typing.type_check_only
class MoveAssignmentRequest(typing_extensions.TypedDict, total=False):
    destinationId: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    creationTime: str
    ignoreIdleSlots: bool
    name: str
    slotCapacity: str
    updateTime: str

@typing.type_check_only
class SearchAllAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
    nextPageToken: str

@typing.type_check_only
class SearchAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
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
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
