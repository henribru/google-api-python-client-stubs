import typing

import typing_extensions

_list = list

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
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

@typing.type_check_only
class TaskList(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    selfLink: str
    title: str
    updated: str

@typing.type_check_only
class TaskLists(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[TaskList]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Tasks(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Task]
    kind: str
    nextPageToken: str
