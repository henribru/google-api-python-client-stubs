import typing

import typing_extensions

class Assignment(typing_extensions.TypedDict, total=False):
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]
    assignee: str
    jobType: typing_extensions.Literal[
        "JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY", "ML_EXTERNAL"
    ]

class CreateSlotPoolMetadata(typing_extensions.TypedDict, total=False):
    slotPool: str

class CapacityCommitment(typing_extensions.TypedDict, total=False):
    renewalPlan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]
    name: str
    commitmentStartTime: str
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    failureStatus: Status
    commitmentEndTime: str
    slotCount: str

class MoveAssignmentRequest(typing_extensions.TypedDict, total=False):
    destinationId: str

class MergeCapacityCommitmentsRequest(typing_extensions.TypedDict, total=False):
    capacityCommitmentIds: typing.List[str]

class ListCapacityCommitmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    capacityCommitments: typing.List[CapacityCommitment]

class ListAssignmentsResponse(typing_extensions.TypedDict, total=False):
    assignments: typing.List[Assignment]
    nextPageToken: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Reservation(typing_extensions.TypedDict, total=False):
    ignoreIdleSlots: bool
    updateTime: str
    name: str
    slotCapacity: str
    creationTime: str

class SplitCapacityCommitmentRequest(typing_extensions.TypedDict, total=False):
    slotCount: str

class SearchAssignmentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    assignments: typing.List[Assignment]

class BiReservation(typing_extensions.TypedDict, total=False):
    name: str
    size: str
    updateTime: str

class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    reservations: typing.List[Reservation]
    nextPageToken: str

class SplitCapacityCommitmentResponse(typing_extensions.TypedDict, total=False):
    second: CapacityCommitment
    first: CapacityCommitment

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
