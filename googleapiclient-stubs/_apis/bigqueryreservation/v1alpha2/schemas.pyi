import typing

import typing_extensions

class SearchReservationGrantsResponse(typing_extensions.TypedDict, total=False):
    reservationGrants: typing.List[ReservationGrant]
    nextPageToken: str

class Reservation(typing_extensions.TypedDict, total=False):
    name: str
    slotCapacity: str
    useParentReservation: bool

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class ReservationGrant(typing_extensions.TypedDict, total=False):
    name: str
    reservation: str
    jobType: typing_extensions.Literal["JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY"]
    grantee: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

class Empty(typing_extensions.TypedDict, total=False): ...

class ListReservationGrantsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservationGrants: typing.List[ReservationGrant]

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status

class ListSlotPoolsResponse(typing_extensions.TypedDict, total=False):
    slotPools: typing.List[SlotPool]
    nextPageToken: str

class SlotPool(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]
    commitmentEndTime: str
    slotCount: str
    failureStatus: Status
    name: str
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]

class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    reservations: typing.List[Reservation]
    nextPageToken: str

class CreateSlotPoolMetadata(typing_extensions.TypedDict, total=False):
    slotPool: str
