import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AiplatformResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DatasetsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatasetVersionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1DatasetVersion = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, readMask: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudAiplatformV1DatasetVersionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                readMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest,
                previous_response: GoogleCloudAiplatformV1ListDatasetVersionsResponse,
            ) -> (
                GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudAiplatformV1DatasetVersion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1DatasetVersionHttpRequest: ...
            def restore(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def create(
            self,
            *,
            body: GoogleCloudAiplatformV1Dataset = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudAiplatformV1DatasetHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            readMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest,
            previous_response: GoogleCloudAiplatformV1ListDatasetsResponse,
        ) -> GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleCloudAiplatformV1Dataset = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1DatasetHttpRequest: ...
        def datasetVersions(self) -> DatasetVersionsResource: ...

    @typing.type_check_only
    class EndpointsResource(googleapiclient.discovery.Resource):
        def computeTokens(
            self,
            *,
            endpoint: str,
            body: GoogleCloudAiplatformV1ComputeTokensRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1ComputeTokensResponseHttpRequest: ...
        def countTokens(
            self,
            *,
            endpoint: str,
            body: GoogleCloudAiplatformV1CountTokensRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1CountTokensResponseHttpRequest: ...
        def generateContent(
            self,
            *,
            model: str,
            body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
        def streamGenerateContent(
            self,
            *,
            model: str,
            body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            parent: str,
            body: GoogleCloudAiplatformV1UploadRagFileRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1UploadRagFileResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BatchPredictionJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelBatchPredictionJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1BatchPredictionJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1BatchPredictionJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1BatchPredictionJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1ListBatchPredictionJobsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListBatchPredictionJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListBatchPredictionJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListBatchPredictionJobsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class CachedContentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1CachedContent = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1CachedContentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1CachedContentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListCachedContentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListCachedContentsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListCachedContentsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListCachedContentsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CachedContent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1CachedContentHttpRequest: ...

            @typing.type_check_only
            class CustomJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelCustomJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1CustomJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1CustomJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1CustomJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListCustomJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListCustomJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListCustomJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListCustomJobsResponseHttpRequest | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class DataLabelingJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelDataLabelingJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1DataLabelingJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1DataLabelingJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1DataLabelingJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListDataLabelingJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListDataLabelingJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListDataLabelingJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListDataLabelingJobsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AnnotationSpecsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def get(
                        self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1AnnotationSpecHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class DataItemsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnnotationsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def cancel(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def delete(
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...
                            def wait(
                                self,
                                *,
                                name: str,
                                timeout: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudAiplatformV1ListAnnotationsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1ListAnnotationsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1ListAnnotationsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1ListAnnotationsResponseHttpRequest
                            | None
                        ): ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListDataItemsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListDataItemsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListDataItemsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListDataItemsResponseHttpRequest | None
                    ): ...
                    def annotations(self) -> AnnotationsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class DatasetVersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1DatasetVersion = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1DatasetVersionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListDatasetVersionsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1DatasetVersion = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1DatasetVersionHttpRequest: ...
                    def restore(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class SavedQueriesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListSavedQueriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListSavedQueriesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListSavedQueriesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListSavedQueriesResponseHttpRequest
                        | None
                    ): ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Dataset = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ExportDataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1DatasetHttpRequest: ...
                def import_(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ImportDataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListDatasetsResponse,
                ) -> GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1DatasetHttpRequest: ...
                def searchDataItems(
                    self,
                    *,
                    dataset: str,
                    annotationFilters: str | _list[str] = ...,
                    annotationsFilter: str = ...,
                    annotationsLimit: int = ...,
                    dataItemFilter: str = ...,
                    dataLabelingJob: str = ...,
                    fieldMask: str = ...,
                    orderBy: str = ...,
                    orderByAnnotation_orderBy: str = ...,
                    orderByAnnotation_savedQuery: str = ...,
                    orderByDataItem: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    savedQuery: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1SearchDataItemsResponseHttpRequest: ...
                def searchDataItems_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1SearchDataItemsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1SearchDataItemsResponse,
                ) -> (
                    GoogleCloudAiplatformV1SearchDataItemsResponseHttpRequest | None
                ): ...
                def annotationSpecs(self) -> AnnotationSpecsResource: ...
                def dataItems(self) -> DataItemsResource: ...
                def datasetVersions(self) -> DatasetVersionsResource: ...
                def operations(self) -> OperationsResource: ...
                def savedQueries(self) -> SavedQueriesResource: ...

            @typing.type_check_only
            class DeploymentResourcePoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1CreateDeploymentResourcePoolRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1DeploymentResourcePoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1DeploymentResourcePool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def queryDeployedModels(
                    self,
                    *,
                    deploymentResourcePool: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1QueryDeployedModelsResponseHttpRequest: ...
                def queryDeployedModels_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1QueryDeployedModelsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1QueryDeployedModelsResponse,
                ) -> (
                    GoogleCloudAiplatformV1QueryDeployedModelsResponseHttpRequest | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class EndpointsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ChatResource(googleapiclient.discovery.Resource):
                    def completions(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleApiHttpBody = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def computeTokens(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1ComputeTokensRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ComputeTokensResponseHttpRequest: ...
                def countTokens(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1CountTokensRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1CountTokensResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Endpoint = ...,
                    endpointId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deployModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1DeployModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def directPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1DirectPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1DirectPredictResponseHttpRequest: ...
                def directRawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1DirectRawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1DirectRawPredictResponseHttpRequest: ...
                def explain(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1ExplainRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ExplainResponseHttpRequest: ...
                def fetchPredictOperation(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1FetchPredictOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generateContent(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1EndpointHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListEndpointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListEndpointsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListEndpointsResponse,
                ) -> GoogleCloudAiplatformV1ListEndpointsResponseHttpRequest | None: ...
                def mutateDeployedModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1MutateDeployedModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Endpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1EndpointHttpRequest: ...
                def predict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1PredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1PredictResponseHttpRequest: ...
                def predictLongRunning(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1PredictLongRunningRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def rawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1RawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def serverStreamingPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1StreamingPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest: ...
                def streamGenerateContent(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
                def streamRawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1StreamRawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def undeployModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1UndeployModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1UpdateEndpointLongRunningRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def chat(self) -> ChatResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class FeatureGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FeaturesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def listWait(
                            self,
                            *,
                            name: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                        def listWait_next(
                            self,
                            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                            previous_response: GoogleLongrunningListOperationsResponse,
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1BatchCreateFeaturesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Feature = ...,
                        featureId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1FeatureHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        latestStatsCount: int = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListFeaturesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1Feature = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def listWait(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def listWait_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1FeatureGroup = ...,
                    featureGroupId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1FeatureGroupHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListFeatureGroupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListFeatureGroupsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListFeatureGroupsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListFeatureGroupsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1FeatureGroup = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def features(self) -> FeaturesResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class FeatureOnlineStoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FeatureViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FeatureViewSyncsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1FeatureViewSyncHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1ListFeatureViewSyncsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1ListFeatureViewSyncsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1ListFeatureViewSyncsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1ListFeatureViewSyncsResponseHttpRequest
                            | None
                        ): ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def listWait(
                            self,
                            *,
                            name: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                        def listWait_next(
                            self,
                            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                            previous_response: GoogleLongrunningListOperationsResponse,
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1FeatureView = ...,
                        featureViewId: str = ...,
                        runSyncImmediately: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def fetchFeatureValues(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1FetchFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1FetchFeatureValuesResponseHttpRequest
                    ): ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1FeatureViewHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListFeatureViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListFeatureViewsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListFeatureViewsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListFeatureViewsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1FeatureView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def searchNearestEntities(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1SearchNearestEntitiesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1SearchNearestEntitiesResponseHttpRequest
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def sync(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1SyncFeatureViewRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1SyncFeatureViewResponseHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        permissions: str | _list[str] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def featureViewSyncs(self) -> FeatureViewSyncsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def listWait(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                    def listWait_next(
                        self,
                        previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                        previous_response: GoogleLongrunningListOperationsResponse,
                    ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1FeatureOnlineStore = ...,
                    featureOnlineStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1FeatureOnlineStoreHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1ListFeatureOnlineStoresResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListFeatureOnlineStoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListFeatureOnlineStoresResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1FeatureOnlineStore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def featureViews(self) -> FeatureViewsResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class FeaturestoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntityTypesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FeaturesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def cancel(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def delete(
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...
                            def wait(
                                self,
                                *,
                                name: str,
                                timeout: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1BatchCreateFeaturesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1Feature = ...,
                            featureId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1FeatureHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            latestStatsCount: int = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1ListFeaturesResponse,
                        ) -> (
                            GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudAiplatformV1Feature = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1FeatureHttpRequest: ...
                        def operations(self) -> OperationsResource: ...

                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1EntityType = ...,
                        entityTypeId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def deleteFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1DeleteFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def exportFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ExportFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1EntityTypeHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def importFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ImportFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListEntityTypesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListEntityTypesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListEntityTypesResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1EntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1EntityTypeHttpRequest: ...
                    def readFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def streamingReadFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest
                    ): ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        permissions: str | _list[str] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def writeFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1WriteFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1WriteFeatureValuesResponseHttpRequest
                    ): ...
                    def features(self) -> FeaturesResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchReadFeatureValues(
                    self,
                    *,
                    featurestore: str,
                    body: GoogleCloudAiplatformV1BatchReadFeatureValuesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Featurestore = ...,
                    featurestoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1FeaturestoreHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListFeaturestoresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListFeaturestoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListFeaturestoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListFeaturestoresResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Featurestore = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def searchFeatures(
                    self,
                    *,
                    location: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1SearchFeaturesResponseHttpRequest: ...
                def searchFeatures_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1SearchFeaturesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1SearchFeaturesResponse,
                ) -> (
                    GoogleCloudAiplatformV1SearchFeaturesResponseHttpRequest | None
                ): ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def entityTypes(self) -> EntityTypesResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class HyperparameterTuningJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelHyperparameterTuningJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1HyperparameterTuningJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1HyperparameterTuningJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1HyperparameterTuningJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class IndexEndpointsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1IndexEndpoint = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1DeployIndexRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def findNeighbors(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1FindNeighborsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1FindNeighborsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1IndexEndpointHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListIndexEndpointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListIndexEndpointsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListIndexEndpointsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListIndexEndpointsResponseHttpRequest | None
                ): ...
                def mutateDeployedIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1DeployedIndex = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1IndexEndpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1IndexEndpointHttpRequest: ...
                def readIndexDatapoints(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1ReadIndexDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ReadIndexDatapointsResponseHttpRequest: ...
                def undeployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1UndeployIndexRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class IndexesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Index = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1IndexHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListIndexesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListIndexesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListIndexesResponse,
                ) -> GoogleCloudAiplatformV1ListIndexesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Index = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def removeDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1RemoveDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1RemoveDatapointsResponseHttpRequest: ...
                def upsertDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1UpsertDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1UpsertDatapointsResponseHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class MetadataStoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ArtifactsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Artifact = ...,
                        artifactId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ArtifactHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ArtifactHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListArtifactsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListArtifactsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListArtifactsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListArtifactsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1Artifact = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ArtifactHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeArtifactsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryArtifactLineageSubgraph(
                        self,
                        *,
                        artifact: str,
                        filter: str = ...,
                        maxHops: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class ContextsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def addContextArtifactsAndExecutions(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponseHttpRequest: ...
                    def addContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1AddContextChildrenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1AddContextChildrenResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Context = ...,
                        contextId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ContextHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ContextHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListContextsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListContextsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListContextsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListContextsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1Context = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ContextHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeContextsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryContextLineageSubgraph(
                        self, *, context: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...
                    def removeContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1RemoveContextChildrenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1RemoveContextChildrenResponseHttpRequest
                    ): ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def addExecutionEvents(
                        self,
                        *,
                        execution: str,
                        body: GoogleCloudAiplatformV1AddExecutionEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1AddExecutionEventsResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Execution = ...,
                        executionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ExecutionHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ExecutionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListExecutionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListExecutionsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListExecutionsResponseHttpRequest | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1Execution = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ExecutionHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeExecutionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryExecutionInputsAndOutputs(
                        self, *, execution: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class MetadataSchemasResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1MetadataSchema = ...,
                        metadataSchemaId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1MetadataSchemaHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1MetadataSchemaHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ListMetadataSchemasResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListMetadataSchemasResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListMetadataSchemasResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListMetadataSchemasResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1MetadataStore = ...,
                    metadataStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1MetadataStoreHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListMetadataStoresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListMetadataStoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListMetadataStoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListMetadataStoresResponseHttpRequest | None
                ): ...
                def artifacts(self) -> ArtifactsResource: ...
                def contexts(self) -> ContextsResource: ...
                def executions(self) -> ExecutionsResource: ...
                def metadataSchemas(self) -> MetadataSchemasResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class MigratableResourcesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchMigrate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1BatchMigrateResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1SearchMigratableResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1SearchMigratableResourcesResponseHttpRequest
                ): ...
                def search_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1SearchMigratableResourcesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1SearchMigratableResourcesResponse,
                ) -> (
                    GoogleCloudAiplatformV1SearchMigratableResourcesResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ModelDeploymentMonitoringJobsResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1ModelDeploymentMonitoringJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ModelDeploymentMonitoringJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ModelDeploymentMonitoringJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ModelDeploymentMonitoringJob = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1PauseModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ResumeModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def searchModelDeploymentMonitoringStatsAnomalies(
                    self,
                    *,
                    modelDeploymentMonitoringJob: str,
                    body: GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest: ...
                def searchModelDeploymentMonitoringStatsAnomalies_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse,
                ) -> (
                    GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ModelsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EvaluationsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class SlicesResource(googleapiclient.discovery.Resource):
                        def batchImport(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1ModelEvaluationSliceHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1ListModelEvaluationSlicesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1ListModelEvaluationSlicesResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse,
                        ) -> (
                            GoogleCloudAiplatformV1ListModelEvaluationSlicesResponseHttpRequest
                            | None
                        ): ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ModelEvaluationHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1ImportModelEvaluationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ModelEvaluationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ListModelEvaluationsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListModelEvaluationsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListModelEvaluationsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListModelEvaluationsResponseHttpRequest
                        | None
                    ): ...
                    def operations(self) -> OperationsResource: ...
                    def slices(self) -> SlicesResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def copy(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1CopyModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deleteVersion(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ExportModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListModelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListModelsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListModelsResponse,
                ) -> GoogleCloudAiplatformV1ListModelsResponseHttpRequest | None: ...
                def listVersions(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListModelVersionsResponseHttpRequest: ...
                def listVersions_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListModelVersionsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListModelVersionsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListModelVersionsResponseHttpRequest | None
                ): ...
                def mergeVersionAliases(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1MergeVersionAliasesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Model = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def updateExplanationDataset(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1UpdateExplanationDatasetRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1UploadModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def evaluations(self) -> EvaluationsResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class NasJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NasTrialDetailsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1NasTrialDetailHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ListNasTrialDetailsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListNasTrialDetailsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListNasTrialDetailsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListNasTrialDetailsResponseHttpRequest
                        | None
                    ): ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelNasJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1NasJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1NasJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1NasJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNasJobsResponse,
                ) -> GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest | None: ...
                def nasTrialDetails(self) -> NasTrialDetailsResource: ...

            @typing.type_check_only
            class NotebookExecutionJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1NotebookExecutionJob = ...,
                    notebookExecutionJobId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "NOTEBOOK_EXECUTION_JOB_VIEW_UNSPECIFIED",
                        "NOTEBOOK_EXECUTION_JOB_VIEW_BASIC",
                        "NOTEBOOK_EXECUTION_JOB_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1NotebookExecutionJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "NOTEBOOK_EXECUTION_JOB_VIEW_UNSPECIFIED",
                        "NOTEBOOK_EXECUTION_JOB_VIEW_BASIC",
                        "NOTEBOOK_EXECUTION_JOB_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1ListNotebookExecutionJobsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNotebookExecutionJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNotebookExecutionJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListNotebookExecutionJobsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class NotebookRuntimeTemplatesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1NotebookRuntimeTemplate = ...,
                    notebookRuntimeTemplateId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1NotebookRuntimeTemplateHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1NotebookRuntimeTemplate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1NotebookRuntimeTemplateHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class NotebookRuntimesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def assign(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1AssignNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1NotebookRuntimeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListNotebookRuntimesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNotebookRuntimesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNotebookRuntimesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListNotebookRuntimesResponseHttpRequest
                    | None
                ): ...
                def start(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1StartNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1StopNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1UpgradeNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def delete(
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
                def wait(
                    self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class PersistentResourcesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1PersistentResource = ...,
                    persistentResourceId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1PersistentResourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1ListPersistentResourcesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListPersistentResourcesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListPersistentResourcesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListPersistentResourcesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1PersistentResource = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reboot(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1RebootPersistentResourceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class PipelineJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchCancel(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1BatchCancelPipelineJobsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1BatchDeletePipelineJobsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelPipelineJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1PipelineJob = ...,
                    pipelineJobId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1PipelineJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1PipelineJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListPipelineJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListPipelineJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListPipelineJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListPipelineJobsResponseHttpRequest | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class PublishersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ModelsResource(googleapiclient.discovery.Resource):
                    def computeTokens(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1ComputeTokensRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ComputeTokensResponseHttpRequest: ...
                    def countTokens(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1CountTokensRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1CountTokensResponseHttpRequest: ...
                    def fetchPredictOperation(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1FetchPredictOperationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def generateContent(
                        self,
                        *,
                        model: str,
                        body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
                    def predict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1PredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1PredictResponseHttpRequest: ...
                    def predictLongRunning(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1PredictLongRunningRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rawPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1RawPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def serverStreamingPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1StreamingPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest: ...
                    def streamGenerateContent(
                        self,
                        *,
                        model: str,
                        body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
                    def streamRawPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1StreamRawPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...

                def models(self) -> ModelsResource: ...

            @typing.type_check_only
            class RagCorporaResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class RagFilesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1RagFileHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1ImportRagFilesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListRagFilesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListRagFilesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListRagFilesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListRagFilesResponseHttpRequest | None
                    ): ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1RagCorpus = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1RagCorpusHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListRagCorporaResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListRagCorporaResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListRagCorporaResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListRagCorporaResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1RagCorpus = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def ragFiles(self) -> RagFilesResource: ...

            @typing.type_check_only
            class ReasoningEnginesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1ReasoningEngine = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ReasoningEngineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListReasoningEnginesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListReasoningEnginesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListReasoningEnginesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListReasoningEnginesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ReasoningEngine = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def query(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1QueryReasoningEngineRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1QueryReasoningEngineResponseHttpRequest: ...
                def streamQuery(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1StreamQueryReasoningEngineRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class SchedulesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Schedule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ScheduleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ScheduleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListSchedulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListSchedulesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListSchedulesResponse,
                ) -> GoogleCloudAiplatformV1ListSchedulesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Schedule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ScheduleHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1PauseScheduleRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ResumeScheduleRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class SpecialistPoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1SpecialistPool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1SpecialistPoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListSpecialistPoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListSpecialistPoolsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListSpecialistPoolsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListSpecialistPoolsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1SpecialistPool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class StudiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class TrialsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    def addTrialMeasurement(
                        self,
                        *,
                        trialName: str,
                        body: GoogleCloudAiplatformV1AddTrialMeasurementRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def checkTrialEarlyStoppingState(
                        self,
                        *,
                        trialName: str,
                        body: GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def complete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1CompleteTrialRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Trial = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListTrialsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListTrialsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListTrialsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListTrialsResponseHttpRequest | None
                    ): ...
                    def listOptimalTrials(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1ListOptimalTrialsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1ListOptimalTrialsResponseHttpRequest
                    ): ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1StopTrialRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def suggest(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1SuggestTrialsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Study = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1StudyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1StudyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListStudiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListStudiesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListStudiesResponse,
                ) -> GoogleCloudAiplatformV1ListStudiesResponseHttpRequest | None: ...
                def lookup(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1LookupStudyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1StudyHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def trials(self) -> TrialsResource: ...

            @typing.type_check_only
            class TensorboardsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExperimentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def delete(
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
                        ) -> (
                            GoogleLongrunningListOperationsResponseHttpRequest | None
                        ): ...
                        def wait(
                            self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...

                    @typing.type_check_only
                    class RunsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class OperationsResource(googleapiclient.discovery.Resource):
                            def cancel(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleProtobufEmptyHttpRequest: ...
                            def delete(
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
                            ) -> (
                                GoogleLongrunningListOperationsResponseHttpRequest
                                | None
                            ): ...
                            def wait(
                                self,
                                *,
                                name: str,
                                timeout: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        @typing.type_check_only
                        class TimeSeriesResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class OperationsResource(
                                googleapiclient.discovery.Resource
                            ):
                                def cancel(
                                    self, *, name: str, **kwargs: typing.Any
                                ) -> GoogleProtobufEmptyHttpRequest: ...
                                def delete(
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
                                ) -> (
                                    GoogleLongrunningListOperationsResponseHttpRequest
                                ): ...
                                def list_next(
                                    self,
                                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                                    previous_response: GoogleLongrunningListOperationsResponse,
                                ) -> (
                                    GoogleLongrunningListOperationsResponseHttpRequest
                                    | None
                                ): ...
                                def wait(
                                    self,
                                    *,
                                    name: str,
                                    timeout: str = ...,
                                    **kwargs: typing.Any,
                                ) -> GoogleLongrunningOperationHttpRequest: ...

                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudAiplatformV1TensorboardTimeSeries = ...,
                                tensorboardTimeSeriesId: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest
                            ): ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def exportTensorboardTimeSeries(
                                self,
                                *,
                                tensorboardTimeSeries: str,
                                body: GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def exportTensorboardTimeSeries_next(
                                self,
                                previous_request: GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponseHttpRequest,
                                previous_response: GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse,
                            ) -> (
                                GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponseHttpRequest
                                | None
                            ): ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest
                            ): ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                readMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponseHttpRequest,
                                previous_response: GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse,
                            ) -> (
                                GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudAiplatformV1TensorboardTimeSeries = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> (
                                GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest
                            ): ...
                            def read(
                                self,
                                *,
                                tensorboardTimeSeries: str,
                                filter: str = ...,
                                maxDataPoints: int = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def readBlobData(
                                self,
                                *,
                                timeSeries: str,
                                blobIds: str | _list[str] = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1ReadTensorboardBlobDataResponseHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1TensorboardRun = ...,
                            tensorboardRunId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1TensorboardRunHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1TensorboardRunHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1ListTensorboardRunsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1ListTensorboardRunsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1ListTensorboardRunsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1ListTensorboardRunsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudAiplatformV1TensorboardRun = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1TensorboardRunHttpRequest: ...
                        def write(
                            self,
                            *,
                            tensorboardRun: str,
                            body: GoogleCloudAiplatformV1WriteTensorboardRunDataRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1WriteTensorboardRunDataResponseHttpRequest: ...
                        def operations(self) -> OperationsResource: ...
                        def timeSeries(self) -> TimeSeriesResource: ...

                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1TensorboardExperiment = ...,
                        tensorboardExperimentId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TensorboardExperimentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TensorboardExperimentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1ListTensorboardExperimentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1ListTensorboardExperimentsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1ListTensorboardExperimentsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1ListTensorboardExperimentsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1TensorboardExperiment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1TensorboardExperimentHttpRequest: ...
                    def write(
                        self,
                        *,
                        tensorboardExperiment: str,
                        body: GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponseHttpRequest: ...
                    def operations(self) -> OperationsResource: ...
                    def runs(self) -> RunsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def batchRead(
                    self,
                    *,
                    tensorboard: str,
                    timeSeries: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Tensorboard = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1TensorboardHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListTensorboardsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListTensorboardsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListTensorboardsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListTensorboardsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Tensorboard = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def readSize(
                    self, *, tensorboard: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ReadTensorboardSizeResponseHttpRequest: ...
                def readUsage(
                    self, *, tensorboard: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ReadTensorboardUsageResponseHttpRequest: ...
                def experiments(self) -> ExperimentsResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class TrainingPipelinesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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
                    def wait(
                        self, *, name: str, timeout: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelTrainingPipelineRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1TrainingPipeline = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1TrainingPipelineHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1TrainingPipelineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1ListTrainingPipelinesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListTrainingPipelinesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListTrainingPipelinesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListTrainingPipelinesResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class TuningJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def delete(
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

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1CancelTuningJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1TuningJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1TuningJobHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1TuningJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1ListTuningJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListTuningJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListTuningJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListTuningJobsResponseHttpRequest | None
                ): ...
                def rebaseTunedModel(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1RebaseTunedModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            def augmentPrompt(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1AugmentPromptRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1AugmentPromptResponseHttpRequest: ...
            def corroborateContent(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1CorroborateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1CorroborateContentResponseHttpRequest: ...
            def evaluateInstances(
                self,
                *,
                location: str,
                body: GoogleCloudAiplatformV1EvaluateInstancesRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1EvaluateInstancesResponseHttpRequest: ...
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
            def retrieveContexts(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1RetrieveContextsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1RetrieveContextsResponseHttpRequest: ...
            def batchPredictionJobs(self) -> BatchPredictionJobsResource: ...
            def cachedContents(self) -> CachedContentsResource: ...
            def customJobs(self) -> CustomJobsResource: ...
            def dataLabelingJobs(self) -> DataLabelingJobsResource: ...
            def datasets(self) -> DatasetsResource: ...
            def deploymentResourcePools(self) -> DeploymentResourcePoolsResource: ...
            def endpoints(self) -> EndpointsResource: ...
            def featureGroups(self) -> FeatureGroupsResource: ...
            def featureOnlineStores(self) -> FeatureOnlineStoresResource: ...
            def featurestores(self) -> FeaturestoresResource: ...
            def hyperparameterTuningJobs(self) -> HyperparameterTuningJobsResource: ...
            def indexEndpoints(self) -> IndexEndpointsResource: ...
            def indexes(self) -> IndexesResource: ...
            def metadataStores(self) -> MetadataStoresResource: ...
            def migratableResources(self) -> MigratableResourcesResource: ...
            def modelDeploymentMonitoringJobs(
                self,
            ) -> ModelDeploymentMonitoringJobsResource: ...
            def models(self) -> ModelsResource: ...
            def nasJobs(self) -> NasJobsResource: ...
            def notebookExecutionJobs(self) -> NotebookExecutionJobsResource: ...
            def notebookRuntimeTemplates(self) -> NotebookRuntimeTemplatesResource: ...
            def notebookRuntimes(self) -> NotebookRuntimesResource: ...
            def operations(self) -> OperationsResource: ...
            def persistentResources(self) -> PersistentResourcesResource: ...
            def pipelineJobs(self) -> PipelineJobsResource: ...
            def publishers(self) -> PublishersResource: ...
            def ragCorpora(self) -> RagCorporaResource: ...
            def reasoningEngines(self) -> ReasoningEnginesResource: ...
            def schedules(self) -> SchedulesResource: ...
            def specialistPools(self) -> SpecialistPoolsResource: ...
            def studies(self) -> StudiesResource: ...
            def tensorboards(self) -> TensorboardsResource: ...
            def trainingPipelines(self) -> TrainingPipelinesResource: ...
            def tuningJobs(self) -> TuningJobsResource: ...

        def getCacheConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudAiplatformV1CacheConfigHttpRequest: ...
        def updateCacheConfig(
            self,
            *,
            name: str,
            body: GoogleCloudAiplatformV1CacheConfig = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class PublishersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ModelsResource(googleapiclient.discovery.Resource):
            def computeTokens(
                self,
                *,
                endpoint: str,
                body: GoogleCloudAiplatformV1ComputeTokensRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1ComputeTokensResponseHttpRequest: ...
            def countTokens(
                self,
                *,
                endpoint: str,
                body: GoogleCloudAiplatformV1CountTokensRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1CountTokensResponseHttpRequest: ...
            def generateContent(
                self,
                *,
                model: str,
                body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                huggingFaceToken: str = ...,
                isHuggingFaceModel: bool = ...,
                languageCode: str = ...,
                view: typing_extensions.Literal[
                    "PUBLISHER_MODEL_VIEW_UNSPECIFIED",
                    "PUBLISHER_MODEL_VIEW_BASIC",
                    "PUBLISHER_MODEL_VIEW_FULL",
                    "PUBLISHER_MODEL_VERSION_VIEW_BASIC",
                ] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1PublisherModelHttpRequest: ...
            def streamGenerateContent(
                self,
                *,
                model: str,
                body: GoogleCloudAiplatformV1GenerateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1GenerateContentResponseHttpRequest: ...

        def models(self) -> ModelsResource: ...

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
    def datasets(self) -> DatasetsResource: ...
    def endpoints(self) -> EndpointsResource: ...
    def media(self) -> MediaResource: ...
    def projects(self) -> ProjectsResource: ...
    def publishers(self) -> PublishersResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1AddContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1AddExecutionEventsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AnnotationSpecHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1AnnotationSpec: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Artifact: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AugmentPromptResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1AugmentPromptResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1BatchPredictionJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CacheConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1CacheConfig: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CachedContentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1CachedContent: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ComputeTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ComputeTokensResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Context: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CorroborateContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1CorroborateContentResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CountTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1CountTokensResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CustomJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1CustomJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DataLabelingJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1DataLabelingJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Dataset: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1DatasetVersion: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DeploymentResourcePoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1DeploymentResourcePool: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DirectPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1DirectPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DirectRawPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1DirectRawPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1EndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Endpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1EntityType: ...

@typing.type_check_only
class GoogleCloudAiplatformV1EvaluateInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1EvaluateInstancesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Execution: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExplainResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ExplainResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Feature: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FeatureGroup: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureOnlineStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FeatureOnlineStore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FeatureView: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureViewSyncHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FeatureViewSync: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Featurestore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FetchFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FetchFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1FindNeighborsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1GenerateContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1GenerateContentResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1HyperparameterTuningJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1HyperparameterTuningJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Index: ...

@typing.type_check_only
class GoogleCloudAiplatformV1IndexEndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1IndexEndpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1LineageSubgraphHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1LineageSubgraph: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListArtifactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListArtifactsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListBatchPredictionJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListBatchPredictionJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListCachedContentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListCachedContentsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListContextsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListCustomJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListCustomJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataLabelingJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListDataLabelingJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListDatasetVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListDeploymentResourcePoolsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeatureGroupsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureOnlineStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeatureOnlineStoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewSyncsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeatureViewSyncsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeatureViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeatureViewsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturestoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListFeaturestoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListIndexEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListIndexesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListMetadataSchemasResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListMetadataStoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationSlicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListModelEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListModelVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListNasJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasTrialDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListNasTrialDetailsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookExecutionJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListNotebookExecutionJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListNotebookRuntimesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListOptimalTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListPersistentResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListPersistentResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListPipelineJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListPipelineJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagCorporaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListRagCorporaResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListRagFilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListRagFilesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListReasoningEnginesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListReasoningEnginesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSavedQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListSavedQueriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSchedulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListSchedulesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSpecialistPoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListSpecialistPoolsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListStudiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListStudiesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTensorboardExperimentsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTensorboardsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrainingPipelinesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTrainingPipelinesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTuningJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ListTuningJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1MetadataSchema: ...

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1MetadataStore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Model: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ModelDeploymentMonitoringJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ModelEvaluation: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ModelEvaluationSlice: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1NasJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NasTrialDetailHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1NasTrialDetail: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookExecutionJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1NotebookExecutionJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1NotebookRuntime: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1NotebookRuntimeTemplate: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PersistentResourceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1PersistentResource: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1PipelineJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1PredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1PublisherModel: ...

@typing.type_check_only
class GoogleCloudAiplatformV1QueryDeployedModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1QueryDeployedModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1QueryReasoningEngineResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1QueryReasoningEngineResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagCorpusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1RagCorpus: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RagFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1RagFile: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadIndexDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardBlobDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardSizeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadTensorboardSizeResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReadTensorboardUsageResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReasoningEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1ReasoningEngine: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1RemoveContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1RemoveDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RetrieveContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1RetrieveContextsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Schedule: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SearchDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SearchFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SearchMigratableResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse
    ): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchNearestEntitiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SearchNearestEntitiesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SpecialistPoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SpecialistPool: ...

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1StreamingPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1StudyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Study: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SyncFeatureViewResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1SyncFeatureViewResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Tensorboard: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardExperimentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1TensorboardExperiment: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardRunHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1TensorboardRun: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1TensorboardTimeSeries: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingPipelineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1TrainingPipeline: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1Trial: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TuningJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1TuningJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1UploadRagFileResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1UploadRagFileResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1UpsertDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1WriteFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1WriteTensorboardRunDataResponse: ...

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
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

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
