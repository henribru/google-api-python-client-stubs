import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessQAndAResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class QuestionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AnswersResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAnswersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAnswersResponseHttpRequest,
                    previous_response: ListAnswersResponse,
                ) -> ListAnswersResponseHttpRequest | None: ...
                def upsert(
                    self,
                    *,
                    parent: str,
                    body: UpsertAnswerRequest = ...,
                    **kwargs: typing.Any
                ) -> AnswerHttpRequest: ...

            def create(
                self, *, parent: str, body: Question = ..., **kwargs: typing.Any
            ) -> QuestionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                answersPerQuestion: int = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListQuestionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListQuestionsResponseHttpRequest,
                previous_response: ListQuestionsResponse,
            ) -> ListQuestionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Question = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> QuestionHttpRequest: ...
            def answers(self) -> AnswersResource: ...

        def questions(self) -> QuestionsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class AnswerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Answer: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAnswersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAnswersResponse: ...

@typing.type_check_only
class ListQuestionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListQuestionsResponse: ...

@typing.type_check_only
class QuestionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Question: ...
