import typing

import typing_extensions

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    mimeType: typing.List[str]
    name: str

@typing.type_check_only
class BatchCreatePermissionsRequest(typing_extensions.TypedDict, total=False):
    requests: typing.List[CreatePermissionRequest]

@typing.type_check_only
class BatchCreatePermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[Permission]

@typing.type_check_only
class BatchDeletePermissionsRequest(typing_extensions.TypedDict, total=False):
    names: typing.List[str]

@typing.type_check_only
class CreatePermissionRequest(typing_extensions.TypedDict, total=False):
    parent: str
    permission: Permission

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Family(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class ListContent(typing_extensions.TypedDict, total=False):
    listItems: typing.List[ListItem]

@typing.type_check_only
class ListItem(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: typing.List[Note]

@typing.type_check_only
class Note(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    deleted: bool
    email: str
    family: Family
    group: Group
    name: str
    role: typing_extensions.Literal["ROLE_UNSPECIFIED", "OWNER", "WRITER"]
    user: User

@typing.type_check_only
class Section(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class TextContent(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    email: str
