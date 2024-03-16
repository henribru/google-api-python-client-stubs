import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DocumentResource(googleapiclient.discovery.Resource):
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ProcessorTypesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta3ProcessorTypeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudDocumentaiV1beta3ListProcessorTypesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDocumentaiV1beta3ListProcessorTypesResponseHttpRequest,
                    previous_response: GoogleCloudDocumentaiV1beta3ListProcessorTypesResponse,
                ) -> (
                    GoogleCloudDocumentaiV1beta3ListProcessorTypesResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class ProcessorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DatasetResource(googleapiclient.discovery.Resource):
                    def batchDeleteDocuments(
                        self,
                        *,
                        dataset: str,
                        body: GoogleCloudDocumentaiV1beta3BatchDeleteDocumentsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def getDatasetSchema(
                        self,
                        *,
                        name: str,
                        visibleFieldsOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDocumentaiV1beta3DatasetSchemaHttpRequest: ...
                    def getDocument(
                        self,
                        *,
                        dataset: str,
                        documentId_gcsManagedDocId_cwDocId: str = ...,
                        documentId_gcsManagedDocId_gcsUri: str = ...,
                        documentId_revisionRef_latestProcessorVersion: str = ...,
                        documentId_revisionRef_revisionCase: typing_extensions.Literal[
                            "REVISION_CASE_UNSPECIFIED",
                            "LATEST_HUMAN_REVIEW",
                            "LATEST_TIMESTAMP",
                            "BASE_OCR_REVISION",
                        ] = ...,
                        documentId_revisionRef_revisionId: str = ...,
                        documentId_unmanagedDocId_docId: str = ...,
                        pageRange_end: int = ...,
                        pageRange_start: int = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDocumentaiV1beta3GetDocumentResponseHttpRequest: ...
                    def importDocuments(
                        self,
                        *,
                        dataset: str,
                        body: GoogleCloudDocumentaiV1beta3ImportDocumentsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def listDocuments(
                        self,
                        *,
                        dataset: str,
                        body: GoogleCloudDocumentaiV1beta3ListDocumentsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudDocumentaiV1beta3ListDocumentsResponseHttpRequest
                    ): ...
                    def listDocuments_next(
                        self,
                        previous_request: GoogleCloudDocumentaiV1beta3ListDocumentsResponseHttpRequest,
                        previous_response: GoogleCloudDocumentaiV1beta3ListDocumentsResponse,
                    ) -> (
                        GoogleCloudDocumentaiV1beta3ListDocumentsResponseHttpRequest
                        | None
                    ): ...
                    def updateDatasetSchema(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3DatasetSchema = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDocumentaiV1beta3DatasetSchemaHttpRequest: ...

                @typing.type_check_only
                class HumanReviewConfigResource(googleapiclient.discovery.Resource):
                    def reviewDocument(
                        self,
                        *,
                        humanReviewConfig: str,
                        body: GoogleCloudDocumentaiV1beta3ReviewDocumentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class ProcessorVersionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class EvaluationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDocumentaiV1beta3EvaluationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudDocumentaiV1beta3ListEvaluationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDocumentaiV1beta3ListEvaluationsResponseHttpRequest,
                            previous_response: GoogleCloudDocumentaiV1beta3ListEvaluationsResponse,
                        ) -> (
                            GoogleCloudDocumentaiV1beta3ListEvaluationsResponseHttpRequest
                            | None
                        ): ...

                    def batchProcess(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3BatchProcessRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def deploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3DeployProcessorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def evaluateProcessorVersion(
                        self,
                        *,
                        processorVersion: str,
                        body: GoogleCloudDocumentaiV1beta3EvaluateProcessorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDocumentaiV1beta3ProcessorVersionHttpRequest: ...
                    def importProcessorVersion(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDocumentaiV1beta3ImportProcessorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponseHttpRequest,
                        previous_response: GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponse,
                    ) -> (
                        GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponseHttpRequest
                        | None
                    ): ...
                    def process(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3ProcessRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest: ...
                    def train(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDocumentaiV1beta3TrainProcessorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDocumentaiV1beta3UndeployProcessorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def evaluations(self) -> EvaluationsResource: ...

                def batchProcess(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3BatchProcessRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDocumentaiV1beta3Processor = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDocumentaiV1beta3ProcessorHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3DisableProcessorRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3EnableProcessorRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDocumentaiV1beta3ProcessorHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest,
                    previous_response: GoogleCloudDocumentaiV1beta3ListProcessorsResponse,
                ) -> (
                    GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest | None
                ): ...
                def process(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3ProcessRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest: ...
                def setDefaultProcessorVersion(
                    self,
                    *,
                    processor: str,
                    body: GoogleCloudDocumentaiV1beta3SetDefaultProcessorVersionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def updateDataset(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDocumentaiV1beta3Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def dataset(self) -> DatasetResource: ...
                def humanReviewConfig(self) -> HumanReviewConfigResource: ...
                def processorVersions(self) -> ProcessorVersionsResource: ...

            def fetchProcessorTypes(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponseHttpRequest: ...
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
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def operations(self) -> OperationsResource: ...
            def processorTypes(self) -> ProcessorTypesResource: ...
            def processors(self) -> ProcessorsResource: ...

        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3DatasetSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3DatasetSchema: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3EvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3Evaluation: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3FetchProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3GetDocumentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3GetDocumentResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListDocumentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ListDocumentsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ListEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ListProcessorTypesResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ListProcessorVersionsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ListProcessorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ListProcessorsResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ProcessResponse: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3Processor: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ProcessorType: ...

@typing.type_check_only
class GoogleCloudDocumentaiV1beta3ProcessorVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudDocumentaiV1beta3ProcessorVersion: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
