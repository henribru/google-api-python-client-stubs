import typing

import typing_extensions

class GoogleHomeEnterpriseSdmV1Room(typing_extensions.TypedDict, total=False):
    name: str
    traits: typing.Dict[str, typing.Any]

class GoogleHomeEnterpriseSdmV1Device(typing_extensions.TypedDict, total=False):
    traits: typing.Dict[str, typing.Any]
    parentRelations: typing.List[GoogleHomeEnterpriseSdmV1ParentRelation]
    name: str
    assignee: str
    type: str

class GoogleHomeEnterpriseSdmV1ListRoomsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rooms: typing.List[GoogleHomeEnterpriseSdmV1Room]

class GoogleHomeEnterpriseSdmV1Structure(typing_extensions.TypedDict, total=False):
    traits: typing.Dict[str, typing.Any]
    name: str
    parentRelations: typing.List[GoogleHomeEnterpriseSdmV1StructureParentRelation]

class GoogleHomeEnterpriseSdmV1StructureParentRelation(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    parent: str

class GoogleHomeEnterpriseSdmV1ParentRelation(typing_extensions.TypedDict, total=False):
    parent: str
    displayName: str

class GoogleHomeEnterpriseSdmV1ListDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    devices: typing.List[GoogleHomeEnterpriseSdmV1Device]

class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest(
    typing_extensions.TypedDict, total=False
):
    params: typing.Dict[str, typing.Any]
    command: str

class GoogleHomeEnterpriseSdmV1ListStructuresResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    structures: typing.List[GoogleHomeEnterpriseSdmV1Structure]

class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse(
    typing_extensions.TypedDict, total=False
):
    results: typing.Dict[str, typing.Any]
