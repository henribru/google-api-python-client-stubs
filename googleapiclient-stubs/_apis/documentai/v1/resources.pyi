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
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProcessorTypesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1ListProcessorTypesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDocumentaiV1ListProcessorTypesResponseHttpRequest,
                    previous_response: GoogleCloudDocumentaiV1ListProcessorTypesResponse,
                ) -> GoogleCloudDocumentaiV1ListProcessorTypesResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProcessorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class HumanReviewConfigResource(googleapiclient.discovery.Resource):
                    def reviewDocument(
                        self,
                        *,
                        humanReviewConfig: str,
                        body: GoogleCloudDocumentaiV1ReviewDocumentRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ProcessorVersionsResource(googleapiclient.discovery.Resource):
                    def batchProcess(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1BatchProcessRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def deploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1DeployProcessorVersionRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDocumentaiV1ProcessorVersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDocumentaiV1ListProcessorVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDocumentaiV1ListProcessorVersionsResponseHttpRequest,
                        previous_response: GoogleCloudDocumentaiV1ListProcessorVersionsResponse,
                    ) -> GoogleCloudDocumentaiV1ListProcessorVersionsResponseHttpRequest | None: ...
                    def process(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1ProcessRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDocumentaiV1ProcessResponseHttpRequest: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1UndeployProcessorVersionRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchProcess(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1BatchProcessRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDocumentaiV1Processor = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1ProcessorHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1DisableProcessorRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1EnableProcessorRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1ProcessorHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1ListProcessorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDocumentaiV1ListProcessorsResponseHttpRequest,
                    previous_response: GoogleCloudDocumentaiV1ListProcessorsResponse,
                ) -> GoogleCloudDocumentaiV1ListProcessorsResponseHttpRequest | None: ...
                def process(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1ProcessRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1ProcessResponseHttpRequest: ...
                def setDefaultProcessorVersion(
                    self,
                    *,
                    processor: str,
                    body: GoogleCloudDocumentaiV1SetDefaultProcessorVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def humanReviewConfig(self) -> HumanReviewConfigResource: ...
                def processorVersions(self) -> ProcessorVersionsResource: ...

            def fetchProcessorTypes(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudDocumentaiV1FetchProcessorTypesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def operations(self) -> OperationsResource: ...
            def processorTypes(self) -> ProcessorTypesResource: ...
            def processors(self) -> ProcessorsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class Uiv1beta3Resource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LocationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudLocationLocationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                    previous_response: GoogleCloudLocationListLocationsResponse,
                ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
                def operations(self) -> OperationsResource: ...

            def locations(self) -> LocationsResource: ...

        def projects(self) -> ProjectsResource: ...

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
    def uiv1beta3(self) -> Uiv1beta3Resource: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1FetchProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1FetchProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ListProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ListProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ListProcessorVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ListProcessorVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ListProcessorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ListProcessorsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ProcessResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1Processor: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessorVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ProcessorVersion: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
