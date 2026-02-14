import typing

import typing_extensions

_list = list

@typing.type_check_only
class CustomerLicense(typing_extensions.TypedDict, total=False):
    applicationId: str
    customerId: str
    editions: _list[Editions]
    id: str
    kind: str
    state: str

@typing.type_check_only
class Editions(typing_extensions.TypedDict, total=False):
    assignedSeats: int
    editionId: str
    seatCount: int

@typing.type_check_only
class UserLicense(typing_extensions.TypedDict, total=False):
    applicationId: str
    customerId: str
    editionId: str
    enabled: bool
    id: str
    kind: str
    state: str
    userId: str
