import typing

_list = list

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Device(typing.TypedDict, total=False):
    name: str
    parentRelations: _list[GoogleHomeEnterpriseSdmV1ParentRelation]
    traits: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest(
    typing.TypedDict, total=False
):
    command: str
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse(
    typing.TypedDict, total=False
):
    results: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListDevicesResponse(typing.TypedDict, total=False):
    devices: _list[GoogleHomeEnterpriseSdmV1Device]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListRoomsResponse(typing.TypedDict, total=False):
    rooms: _list[GoogleHomeEnterpriseSdmV1Room]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListStructuresResponse(typing.TypedDict, total=False):
    structures: _list[GoogleHomeEnterpriseSdmV1Structure]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ParentRelation(typing.TypedDict, total=False):
    displayName: str
    parent: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Room(typing.TypedDict, total=False):
    name: str
    traits: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Structure(typing.TypedDict, total=False):
    name: str
    traits: dict[str, typing.Any]
