import typing

_list = list

@typing.type_check_only
class Attachment(typing.TypedDict, total=False):
    mimeType: _list[str]
    name: str

@typing.type_check_only
class BatchCreatePermissionsRequest(typing.TypedDict, total=False):
    requests: _list[CreatePermissionRequest]

@typing.type_check_only
class BatchCreatePermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[Permission]

@typing.type_check_only
class BatchDeletePermissionsRequest(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class CreatePermissionRequest(typing.TypedDict, total=False):
    parent: str
    permission: Permission

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Family(typing.TypedDict, total=False): ...

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class ListContent(typing.TypedDict, total=False):
    listItems: _list[ListItem]

@typing.type_check_only
class ListItem(typing.TypedDict, total=False):
    checked: bool
    childListItems: _list[ListItem]
    text: TextContent

@typing.type_check_only
class ListNotesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    notes: _list[Note]

@typing.type_check_only
class Note(typing.TypedDict, total=False):
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
class Permission(typing.TypedDict, total=False):
    deleted: bool
    email: str
    family: Family
    group: Group
    name: str
    role: typing.Literal["ROLE_UNSPECIFIED", "OWNER", "WRITER"]
    user: User

@typing.type_check_only
class Section(typing.TypedDict, total=False):
    list: ListContent
    text: TextContent

@typing.type_check_only
class TextContent(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    email: str
