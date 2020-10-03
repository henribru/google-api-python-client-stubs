import typing

import typing_extensions

class Task(typing_extensions.TypedDict, total=False):
    title: str
    position: str
    selfLink: str
    updated: str
    hidden: bool
    parent: str
    id: str
    etag: str
    notes: str
    due: str
    kind: str
    links: typing.List[typing.Dict[str, typing.Any]]
    status: str
    completed: str
    deleted: bool

class TaskList(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    id: str
    updated: str
    title: str
    selfLink: str

class Tasks(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    etag: str
    items: typing.List[Task]

class TaskLists(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    items: typing.List[TaskList]
    nextPageToken: str
