import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Device(typing_extensions.TypedDict, total=False):
    name: str
    parentRelations: _list[GoogleHomeEnterpriseSdmV1ParentRelation]
    traits: dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest(
    typing_extensions.TypedDict, total=False
):
    command: str
    params: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse(
    typing_extensions.TypedDict, total=False
):
    results: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: _list[GoogleHomeEnterpriseSdmV1Device]
    nextPageToken: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListRoomsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rooms: _list[GoogleHomeEnterpriseSdmV1Room]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListStructuresResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    structures: _list[GoogleHomeEnterpriseSdmV1Structure]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ParentRelation(typing_extensions.TypedDict, total=False):
    displayName: str
    parent: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Room(typing_extensions.TypedDict, total=False):
    name: str
    traits: dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Structure(typing_extensions.TypedDict, total=False):
    name: str
    traits: dict[str, typing.Any]
