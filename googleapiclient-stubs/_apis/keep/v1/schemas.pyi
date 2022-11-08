import typing

import typing_extensions

_list = list

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    mimeType: _list[str]
    name: str

@typing.type_check_only
class BatchCreatePermissionsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[CreatePermissionRequest]

@typing.type_check_only
class BatchCreatePermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[Permission]

@typing.type_check_only
class BatchDeletePermissionsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]

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
    listItems: _list[ListItem]

@typing.type_check_only
class ListItem(typing_extensions.TypedDict, total=False):
    checked: bool
    childListItems: _list[ListItem]
    text: TextContent

@typing.type_check_only
class ListNotesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    notes: _list[Note]

@typing.type_check_only
class Note(typing_extensions.TypedDict, total=False):
    attachments: _list[Attachment]
    body: Section
    createTime: str
    name: str
    permissions: _list[Permission]
    title: str
    trashTime: str
    trashed: bool
    updateTime: str

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
class Section(typing_extensions.TypedDict, total=False):
    list: ListContent
    text: TextContent

@typing.type_check_only
class TextContent(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    email: str
