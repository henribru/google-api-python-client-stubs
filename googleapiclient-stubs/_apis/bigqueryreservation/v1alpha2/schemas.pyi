import typing

import typing_extensions

_list = list

@typing.type_check_only
class CreateSlotPoolMetadata(typing_extensions.TypedDict, total=False):
    slotPool: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListReservationGrantsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservationGrants: _list[ReservationGrant]

@typing.type_check_only
class ListReservationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservations: _list[Reservation]

@typing.type_check_only
class ListSlotPoolsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    slotPools: _list[SlotPool]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Reservation(typing_extensions.TypedDict, total=False):
    name: str
    slotCapacity: str
    useParentReservation: bool

@typing.type_check_only
class ReservationGrant(typing_extensions.TypedDict, total=False):
    grantee: str
    jobType: typing_extensions.Literal["JOB_TYPE_UNSPECIFIED", "PIPELINE", "QUERY"]
    name: str
    reservation: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE"]

@typing.type_check_only
class SearchReservationGrantsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reservationGrants: _list[ReservationGrant]

@typing.type_check_only
class SlotPool(typing_extensions.TypedDict, total=False):
    commitmentEndTime: str
    failureStatus: Status
    name: str
    plan: typing_extensions.Literal[
        "COMMITMENT_PLAN_UNSPECIFIED", "FLEX", "TRIAL", "MONTHLY", "ANNUAL"
    ]
    slotCount: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "ACTIVE", "FAILED"]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
