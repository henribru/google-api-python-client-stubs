import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class TasksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class TasklistsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def insert(
            self, *, body: TaskList, **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> TaskListsHttpRequest: ...
        def list_next(
            self, previous_request: TaskListsHttpRequest, previous_response: TaskLists
        ) -> TaskListsHttpRequest | None: ...
        def patch(
            self, *, tasklist: str, body: TaskList, **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...
        def update(
            self, *, tasklist: str, body: TaskList, **kwargs: typing.Any
        ) -> TaskListHttpRequest: ...

    @typing.type_check_only
    class TasksResource(googleapiclient.discovery.Resource):
        def clear(
            self, *, tasklist: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def delete(
            self, *, tasklist: str, task: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, tasklist: str, task: str, **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def insert(
            self,
            *,
            tasklist: str,
            body: Task,
            parent: str | None = ...,
            previous: str | None = ...,
            **kwargs: typing.Any,
        ) -> TaskHttpRequest: ...
        def list(
            self,
            *,
            tasklist: str,
            completedMax: str | None = ...,
            completedMin: str | None = ...,
            dueMax: str | None = ...,
            dueMin: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            showAssigned: bool | None = ...,
            showCompleted: bool | None = ...,
            showDeleted: bool | None = ...,
            showHidden: bool | None = ...,
            updatedMin: str | None = ...,
            **kwargs: typing.Any,
        ) -> TasksHttpRequest: ...
        def list_next(
            self, previous_request: TasksHttpRequest, previous_response: Tasks
        ) -> TasksHttpRequest | None: ...
        def move(
            self,
            *,
            tasklist: str,
            task: str,
            destinationTasklist: str | None = ...,
            parent: str | None = ...,
            previous: str | None = ...,
            **kwargs: typing.Any,
        ) -> TaskHttpRequest: ...
        def patch(
            self, *, tasklist: str, task: str, body: Task, **kwargs: typing.Any
        ) -> TaskHttpRequest: ...
        def update(
            self, *, tasklist: str, task: str, body: Task, **kwargs: typing.Any
        ) -> TaskHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def tasklists(self) -> TasklistsResource: ...
    def tasks(self) -> TasksResource: ...

@typing.type_check_only
class TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Task: ...

@typing.type_check_only
class TaskListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TaskList: ...

@typing.type_check_only
class TaskListsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TaskLists: ...

@typing.type_check_only
class TasksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Tasks: ...
