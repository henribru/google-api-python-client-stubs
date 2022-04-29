import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SpeechResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            name: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomClassesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateCustomClassRequest = ...,
                    **kwargs: typing.Any
                ) -> CustomClassHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomClassHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCustomClassesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomClassesResponseHttpRequest,
                    previous_response: ListCustomClassesResponse,
                ) -> ListCustomClassesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CustomClass = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> CustomClassHttpRequest: ...

            @typing.type_check_only
            class PhraseSetsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreatePhraseSetRequest = ...,
                    **kwargs: typing.Any
                ) -> PhraseSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PhraseSetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPhraseSetResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPhraseSetResponseHttpRequest,
                    previous_response: ListPhraseSetResponse,
                ) -> ListPhraseSetResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: PhraseSet = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> PhraseSetHttpRequest: ...

            def customClasses(self) -> CustomClassesResource: ...
            def phraseSets(self) -> PhraseSetsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class SpeechResource(googleapiclient.discovery.Resource):
        def longrunningrecognize(
            self, *, body: LongRunningRecognizeRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def recognize(
            self, *, body: RecognizeRequest = ..., **kwargs: typing.Any
        ) -> RecognizeResponseHttpRequest: ...

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
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def speech(self) -> SpeechResource: ...

@typing.type_check_only
class CustomClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CustomClass: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListCustomClassesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCustomClassesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPhraseSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPhraseSetResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PhraseSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PhraseSet: ...

@typing.type_check_only
class RecognizeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RecognizeResponse: ...
