import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
            def operations(self) -> OperationsResource: ...
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
                def operations(self) -> OperationsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def uiv1beta3(self) -> Uiv1beta3Resource: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1FetchProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1FetchProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ListProcessorVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ListProcessorVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ListProcessorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ListProcessorsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ProcessResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1Processor: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1ProcessorVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDocumentaiV1ProcessorVersion: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
