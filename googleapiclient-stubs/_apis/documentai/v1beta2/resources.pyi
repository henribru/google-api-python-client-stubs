import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DocumentResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DocumentsResource(googleapiclient.discovery.Resource):
            def batchProcess(
                self,
                *,
                parent: str,
                body: GoogleCloudDocumentaiV1beta2BatchProcessDocumentsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def process(
                self,
                *,
                parent: str,
                body: GoogleCloudDocumentaiV1beta2ProcessDocumentRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDocumentaiV1beta2DocumentHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DocumentsResource(googleapiclient.discovery.Resource):
                def batchProcess(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDocumentaiV1beta2BatchProcessDocumentsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def process(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDocumentaiV1beta2ProcessDocumentRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta2DocumentHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def documents(self) -> DocumentsResource: ...
            def operations(self) -> OperationsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def documents(self) -> DocumentsResource: ...
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta2DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1beta2Document: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...
