import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DocumentResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
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
        class LocationsResource(googleapiclient.discovery.Resource):
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
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
            def documents(self) -> DocumentsResource: ...
            def operations(self) -> OperationsResource: ...
        def operations(self) -> OperationsResource: ...
        def documents(self) -> DocumentsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleCloudDocumentaiV1beta2DocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudDocumentaiV1beta2Document: ...
