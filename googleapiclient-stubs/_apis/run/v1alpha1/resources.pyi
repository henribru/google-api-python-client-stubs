import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudRunResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class NamespacesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class JobsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Job, **kwargs: typing.Any
            ) -> JobHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                apiVersion: str | None = ...,
                kind: str | None = ...,
                propagationPolicy: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> JobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldSelector: str | None = ...,
                includeUninitialized: bool | None = ...,
                labelSelector: str | None = ...,
                limit: int | None = ...,
                resourceVersion: str | None = ...,
                watch: bool | None = ...,
                **kwargs: typing.Any,
            ) -> ListJobsResponseHttpRequest: ...

        def jobs(self) -> JobsResource: ...

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
    def namespaces(self) -> NamespacesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Job: ...

@typing.type_check_only
class ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListJobsResponse: ...
