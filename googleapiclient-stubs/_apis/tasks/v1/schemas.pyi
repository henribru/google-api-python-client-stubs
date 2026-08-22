import typing

_list = list

@typing.type_check_only
class AssignmentInfo(typing.TypedDict, total=False):
    driveResourceInfo: DriveResourceInfo
    linkToTask: str
    spaceInfo: SpaceInfo
    surfaceType: typing.Literal[
        "CONTEXT_TYPE_UNSPECIFIED", "GMAIL", "DOCUMENT", "SPACE"
    ]

@typing.type_check_only
class DriveResourceInfo(typing.TypedDict, total=False):
    driveFileId: str
    resourceKey: str

@typing.type_check_only
class SpaceInfo(typing.TypedDict, total=False):
    space: str

@typing.type_check_only
class Task(typing.TypedDict, total=False):
    assignmentInfo: AssignmentInfo
    completed: str
    deleted: bool
    due: str
    etag: str
    hidden: bool
    id: str
    kind: str
    links: _list[dict[str, typing.Any]]
    notes: str
    parent: str
    position: str
    selfLink: str
    status: str
    title: str
    updated: str
    webViewLink: str

@typing.type_check_only
class TaskList(typing.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    selfLink: str
    title: str
    updated: str

@typing.type_check_only
class TaskLists(typing.TypedDict, total=False):
    etag: str
    items: _list[TaskList]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Tasks(typing.TypedDict, total=False):
    etag: str
    items: _list[Task]
    kind: str
    nextPageToken: str
