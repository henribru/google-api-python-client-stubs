import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FormsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FormsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ResponsesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, formId: str, responseId: str, **kwargs: typing.Any
            ) -> FormResponseHttpRequest: ...
            def list(
                self,
                *,
                formId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListFormResponsesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListFormResponsesResponseHttpRequest,
                previous_response: ListFormResponsesResponse,
            ) -> ListFormResponsesResponseHttpRequest | None: ...

        @typing.type_check_only
        class WatchesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                formId: str,
                body: CreateWatchRequest = ...,
                **kwargs: typing.Any,
            ) -> WatchHttpRequest: ...
            def delete(
                self, *, formId: str, watchId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self, *, formId: str, **kwargs: typing.Any
            ) -> ListWatchesResponseHttpRequest: ...
            def renew(
                self,
                *,
                formId: str,
                watchId: str,
                body: RenewWatchRequest = ...,
                **kwargs: typing.Any,
            ) -> WatchHttpRequest: ...

        def batchUpdate(
            self,
            *,
            formId: str,
            body: BatchUpdateFormRequest = ...,
            **kwargs: typing.Any,
        ) -> BatchUpdateFormResponseHttpRequest: ...
        def create(
            self, *, body: Form = ..., unpublished: bool = ..., **kwargs: typing.Any
        ) -> FormHttpRequest: ...
        def get(self, *, formId: str, **kwargs: typing.Any) -> FormHttpRequest: ...
        def setPublishSettings(
            self,
            *,
            formId: str,
            body: SetPublishSettingsRequest = ...,
            **kwargs: typing.Any,
        ) -> SetPublishSettingsResponseHttpRequest: ...
        def responses(self) -> ResponsesResource: ...
        def watches(self) -> WatchesResource: ...

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
    def forms(self) -> FormsResource: ...

@typing.type_check_only
class BatchUpdateFormResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateFormResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FormHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Form: ...

@typing.type_check_only
class FormResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FormResponse: ...

@typing.type_check_only
class ListFormResponsesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFormResponsesResponse: ...

@typing.type_check_only
class ListWatchesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWatchesResponse: ...

@typing.type_check_only
class SetPublishSettingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SetPublishSettingsResponse: ...

@typing.type_check_only
class WatchHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Watch: ...
