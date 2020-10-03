import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TasksResource(googleapiclient.discovery.Resource):
    class TasksResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            tasklist: str,
            body: Task = ...,
            previous: str = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def get(
            self, *, tasklist: str, task: str, **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def clear(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def move(
            self,
            *,
            tasklist: str,
            task: str,
            parent: str = ...,
            previous: str = ...,
            **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def delete(
            self, *, tasklist: str, task: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self, *, tasklist: str, task: str, body: Task = ..., **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def update(
            self, *, tasklist: str, task: str, body: Task = ..., **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def list(
            self,
            *,
            tasklist: str,
            pageToken: str = ...,
            showDeleted: bool = ...,
            maxResults: int = ...,
            dueMax: str = ...,
            completedMin: str = ...,
            completedMax: str = ...,
            showCompleted: bool = ...,
            updatedMin: str = ...,
            showHidden: bool = ...,
            dueMin: str = ...,
            **kwargs: typing.Any
        ) -> TasksHttpRequest: ...
    class TasklistsResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, tasklist: str, body: TaskList = ..., **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def insert(
            self, *, body: TaskList = ..., **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def get(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def update(
            self, *, tasklist: str, body: TaskList = ..., **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def list(
            self, *, pageToken: str = ..., maxResults: int = ..., **kwargs: typing.Any
        ) -> TaskListsHttpRequest: ...
        def delete(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    def tasks(self) -> TasksResource: ...
    def tasklists(self) -> TasklistsResource: ...

class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Task: ...

class TasksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Tasks: ...

class TaskListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TaskList: ...

class TaskListsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TaskLists: ...
