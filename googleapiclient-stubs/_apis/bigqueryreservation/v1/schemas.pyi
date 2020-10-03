import typing

import typing_extensions

class ListCapacityCommitmentsResponse(typing_extensions.TypedDict, total=False):
    capacityCommitments: typing.List[CapacityCommitment]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Reservation(typing_extensions.TypedDict, total=False):
    slotCapacity: str
    name: str
    ignoreIdleSlots: bool
    creationTime: str
    updateTime: str

class SearchAllAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
    nextPageToken: str

class MoveAssignmentRequest(typing_extensions.TypedDict, total=False):
    destinationId: str

class ListAssignmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    assignments: typing.List[Assignment]

class Assignment(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]
    assignee: str
    jobType: typing_extensions.Literal[
        "JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY", "ML_EXTERNAL"
    ]
    name: str

class SearchAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
    nextPageToken: str

class SplitCapacityCommitmentRequest(typing_extensions.TypedDict, total=False):
    slotCount: str

class MergeCapacityCommitmentsRequest(typing_extensions.TypedDict, total=False):
    capacityCommitmentIds: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class BiReservation(typing_extensions.TypedDict, total=False):
    name: str
    updateTime: str
    size: str

class Empty(typing_extensions.TypedDict, total=False): ...

class SplitCapacityCommitmentResponse(typing_extensions.TypedDict, total=False):
    second: CapacityCommitment
    first: CapacityCommitment

class CreateSlotPoolMetadata(typing_extensions.TypedDict, total=False):
    slotPool: str

class CapacityCommitment(typing_extensions.TypedDict, total=False):
    renewalPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    name: str
    slotCount: str
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]
    commitmentStartTime: str
    failureStatus: Status
    commitmentEndTime: str

class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    reservations: typing.List[Reservation]
    nextPageToken: str
