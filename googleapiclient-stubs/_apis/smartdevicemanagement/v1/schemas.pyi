import typing

import typing_extensions
@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Device(typing_extensions.TypedDict, total=False):
    name: str
    parentRelations: typing.List[GoogleHomeEnterpriseSdmV1ParentRelation]
    traits: typing.Dict[str, typing.Any]
    type: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandRequest(
    typing_extensions.TypedDict, total=False
):
    command: str
    params: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ExecuteDeviceCommandResponse(
    typing_extensions.TypedDict, total=False
):
    results: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListDevicesResponse(
    typing_extensions.TypedDict, total=False
):
    devices: typing.List[GoogleHomeEnterpriseSdmV1Device]
    nextPageToken: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListRoomsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    rooms: typing.List[GoogleHomeEnterpriseSdmV1Room]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ListStructuresResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    structures: typing.List[GoogleHomeEnterpriseSdmV1Structure]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1ParentRelation(typing_extensions.TypedDict, total=False):
    displayName: str
    parent: str

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Room(typing_extensions.TypedDict, total=False):
    name: str
    traits: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleHomeEnterpriseSdmV1Structure(typing_extensions.TypedDict, total=False):
    name: str
    traits: typing.Dict[str, typing.Any]
