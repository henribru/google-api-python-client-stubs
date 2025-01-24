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
                body: GoogleCloudAiplatformV1beta1DatasetVersion = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, readMask: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudAiplatformV1beta1DatasetVersionHttpRequest: ...
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
            ) -> GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest,
                previous_response: GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse,
            ) -> (
                GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudAiplatformV1beta1DatasetVersion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1DatasetVersionHttpRequest: ...
            def restore(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def create(
            self,
            *,
            body: GoogleCloudAiplatformV1beta1Dataset = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudAiplatformV1beta1DatasetHttpRequest: ...
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
        ) -> GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest,
            previous_response: GoogleCloudAiplatformV1beta1ListDatasetsResponse,
        ) -> GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleCloudAiplatformV1beta1Dataset = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1DatasetHttpRequest: ...
        def datasetVersions(self) -> DatasetVersionsResource: ...

    @typing.type_check_only
    class EndpointsResource(googleapiclient.discovery.Resource):
        def computeTokens(
            self,
            *,
            endpoint: str,
            body: GoogleCloudAiplatformV1beta1ComputeTokensRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1ComputeTokensResponseHttpRequest: ...
        def countTokens(
            self,
            *,
            endpoint: str,
            body: GoogleCloudAiplatformV1beta1CountTokensRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1CountTokensResponseHttpRequest: ...
        def generateContent(
            self,
            *,
            model: str,
            body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...
        def streamGenerateContent(
            self,
            *,
            model: str,
            body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            parent: str,
            body: GoogleCloudAiplatformV1beta1UploadRagFileRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudAiplatformV1beta1UploadRagFileResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AgentsResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class AppsResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class BatchPredictionJobsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1CancelBatchPredictionJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1BatchPredictionJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1BatchPredictionJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1BatchPredictionJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class CachedContentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1CachedContent = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1CachedContentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1CachedContentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListCachedContentsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListCachedContentsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListCachedContentsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListCachedContentsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1CachedContent = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1CachedContentHttpRequest: ...

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
                    body: GoogleCloudAiplatformV1beta1CancelCustomJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1CustomJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1CustomJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1CustomJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListCustomJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListCustomJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListCustomJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListCustomJobsResponseHttpRequest | None
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
                    body: GoogleCloudAiplatformV1beta1CancelDataLabelingJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1DataLabelingJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1DataLabelingJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1DataLabelingJobHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponseHttpRequest
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
                    ) -> GoogleCloudAiplatformV1beta1AnnotationSpecHttpRequest: ...
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
                        ) -> GoogleCloudAiplatformV1beta1ListAnnotationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListAnnotationsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListAnnotationsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListAnnotationsResponseHttpRequest
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
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListDataItemsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListDataItemsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListDataItemsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListDataItemsResponseHttpRequest
                        | None
                    ): ...
                    def annotations(self) -> AnnotationsResource: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class DatasetVersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1DatasetVersion = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1DatasetVersionHttpRequest: ...
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
                    ) -> GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1DatasetVersion = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1DatasetVersionHttpRequest: ...
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
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListSavedQueriesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListSavedQueriesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListSavedQueriesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListSavedQueriesResponseHttpRequest
                        | None
                    ): ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Dataset = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ExportDataRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1DatasetHttpRequest: ...
                def import_(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ImportDataRequest = ...,
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
                ) -> GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListDatasetsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1DatasetHttpRequest: ...
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
                ) -> GoogleCloudAiplatformV1beta1SearchDataItemsResponseHttpRequest: ...
                def searchDataItems_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchDataItemsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchDataItemsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchDataItemsResponseHttpRequest
                    | None
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
                    body: GoogleCloudAiplatformV1beta1CreateDeploymentResourcePoolRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1DeploymentResourcePoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1DeploymentResourcePool = ...,
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
                ) -> (
                    GoogleCloudAiplatformV1beta1QueryDeployedModelsResponseHttpRequest
                ): ...
                def queryDeployedModels_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1QueryDeployedModelsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1QueryDeployedModelsResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class EdgeDevicesResource(googleapiclient.discovery.Resource):
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
                    body: GoogleCloudAiplatformV1beta1ComputeTokensRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ComputeTokensResponseHttpRequest: ...
                def countTokens(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1CountTokensRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1CountTokensResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Endpoint = ...,
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
                    body: GoogleCloudAiplatformV1beta1DeployModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def directPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1DirectPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1DirectPredictResponseHttpRequest: ...
                def directRawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1DirectRawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1DirectRawPredictResponseHttpRequest
                ): ...
                def explain(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1ExplainRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ExplainResponseHttpRequest: ...
                def fetchPredictOperation(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1FetchPredictOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generateContent(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1EndpointHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListEndpointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListEndpointsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListEndpointsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListEndpointsResponseHttpRequest | None
                ): ...
                def mutateDeployedModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1MutateDeployedModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Endpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1EndpointHttpRequest: ...
                def predict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1PredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1PredictResponseHttpRequest: ...
                def predictLongRunning(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1PredictLongRunningRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def rawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1RawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def serverStreamingPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1StreamingPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1StreamingPredictResponseHttpRequest
                ): ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def streamGenerateContent(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...
                def streamRawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1StreamRawPredictRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def undeployModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1beta1UndeployModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1UpdateEndpointLongRunningRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def chat(self) -> ChatResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class EvaluationTasksResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ExampleStoresResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ExtensionControllersResource(googleapiclient.discovery.Resource):
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

                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ExtensionsResource(googleapiclient.discovery.Resource):
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

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def execute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ExecuteExtensionRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ExecuteExtensionResponseHttpRequest
                ): ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1ExtensionHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Extension = ...,
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
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListExtensionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListExtensionsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListExtensionsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListExtensionsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Extension = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ExtensionHttpRequest: ...
                def query(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1QueryExtensionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1QueryExtensionResponseHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class FeatureGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FeatureMonitorsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FeatureMonitorJobsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1beta1FeatureMonitorJob = ...,
                            featureMonitorJobId: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudAiplatformV1beta1FeatureMonitorJobHttpRequest
                        ): ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudAiplatformV1beta1FeatureMonitorJobHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponseHttpRequest
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
                        body: GoogleCloudAiplatformV1beta1FeatureMonitor = ...,
                        featureMonitorId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1FeatureMonitorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponseHttpRequest
                        | None
                    ): ...
                    def featureMonitorJobs(self) -> FeatureMonitorJobsResource: ...
                    def operations(self) -> OperationsResource: ...

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

                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1Feature = ...,
                        featureId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        featureStatsAndAnomalySpec_latestStatsCount: int = ...,
                        featureStatsAndAnomalySpec_statsTimeRange_endTime: str = ...,
                        featureStatsAndAnomalySpec_statsTimeRange_startTime: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1FeatureHttpRequest: ...
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
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListFeaturesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1Feature = ...,
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
                    body: GoogleCloudAiplatformV1beta1FeatureGroup = ...,
                    featureGroupId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1FeatureGroupHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListFeatureGroupsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListFeatureGroupsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListFeatureGroupsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListFeatureGroupsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1FeatureGroup = ...,
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
                def featureMonitors(self) -> FeatureMonitorsResource: ...
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
                        ) -> GoogleCloudAiplatformV1beta1FeatureViewSyncHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponseHttpRequest
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
                        body: GoogleCloudAiplatformV1beta1FeatureView = ...,
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
                        body: GoogleCloudAiplatformV1beta1FetchFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1FeatureViewHttpRequest: ...
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
                        GoogleCloudAiplatformV1beta1ListFeatureViewsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListFeatureViewsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListFeatureViewsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListFeatureViewsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1FeatureView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def searchNearestEntities(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1beta1SearchNearestEntitiesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def streamingFetchFeatureValues(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesResponseHttpRequest: ...
                    def sync(
                        self,
                        *,
                        featureView: str,
                        body: GoogleCloudAiplatformV1beta1SyncFeatureViewRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1SyncFeatureViewResponseHttpRequest
                    ): ...
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
                    body: GoogleCloudAiplatformV1beta1FeatureOnlineStore = ...,
                    featureOnlineStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1FeatureOnlineStoreHttpRequest: ...
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
                ) -> GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1FeatureOnlineStore = ...,
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
                            body: GoogleCloudAiplatformV1beta1BatchCreateFeaturesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1beta1Feature = ...,
                            featureId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            featureStatsAndAnomalySpec_latestStatsCount: int = ...,
                            featureStatsAndAnomalySpec_statsTimeRange_endTime: str = ...,
                            featureStatsAndAnomalySpec_statsTimeRange_startTime: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1FeatureHttpRequest: ...
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
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListFeaturesResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudAiplatformV1beta1Feature = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1FeatureHttpRequest: ...
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
                        body: GoogleCloudAiplatformV1beta1EntityType = ...,
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
                        body: GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def exportFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1beta1ExportFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1EntityTypeHttpRequest: ...
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
                        body: GoogleCloudAiplatformV1beta1ImportFeatureValuesRequest = ...,
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
                        GoogleCloudAiplatformV1beta1ListEntityTypesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListEntityTypesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListEntityTypesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListEntityTypesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1EntityType = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1EntityTypeHttpRequest: ...
                    def readFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1beta1ReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHttpRequest
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
                        body: GoogleCloudAiplatformV1beta1StreamingReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHttpRequest
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
                        body: GoogleCloudAiplatformV1beta1WriteFeatureValuesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1WriteFeatureValuesResponseHttpRequest: ...
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
                    body: GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Featurestore = ...,
                    featurestoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1FeaturestoreHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1GetIamPolicyRequest = ...,
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
                ) -> (
                    GoogleCloudAiplatformV1beta1ListFeaturestoresResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListFeaturestoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListFeaturestoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListFeaturestoresResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Featurestore = ...,
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
                ) -> GoogleCloudAiplatformV1beta1SearchFeaturesResponseHttpRequest: ...
                def searchFeatures_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchFeaturesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchFeaturesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchFeaturesResponseHttpRequest | None
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
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1CancelHyperparameterTuningJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1HyperparameterTuningJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1HyperparameterTuningJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1HyperparameterTuningJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1IndexEndpoint = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1beta1DeployIndexRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def findNeighbors(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1beta1FindNeighborsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1FindNeighborsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1IndexEndpointHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListIndexEndpointsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListIndexEndpointsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListIndexEndpointsResponseHttpRequest
                    | None
                ): ...
                def mutateDeployedIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1beta1DeployedIndex = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1IndexEndpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1IndexEndpointHttpRequest: ...
                def readIndexDatapoints(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1beta1ReadIndexDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponseHttpRequest
                ): ...
                def undeployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1beta1UndeployIndexRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1Index = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1IndexHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListIndexesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListIndexesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListIndexesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListIndexesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Index = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def removeDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1beta1RemoveDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1RemoveDatapointsResponseHttpRequest
                ): ...
                def upsertDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1beta1UpsertDatapointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1UpsertDatapointsResponseHttpRequest
                ): ...
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
                        body: GoogleCloudAiplatformV1beta1Artifact = ...,
                        artifactId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ArtifactHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1ArtifactHttpRequest: ...
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
                        GoogleCloudAiplatformV1beta1ListArtifactsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListArtifactsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListArtifactsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListArtifactsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1Artifact = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ArtifactHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1PurgeArtifactsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryArtifactLineageSubgraph(
                        self,
                        *,
                        artifact: str,
                        filter: str = ...,
                        maxHops: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1LineageSubgraphHttpRequest: ...
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
                        body: GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponseHttpRequest: ...
                    def addContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1beta1AddContextChildrenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1AddContextChildrenResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1Context = ...,
                        contextId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ContextHttpRequest: ...
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
                    ) -> GoogleCloudAiplatformV1beta1ContextHttpRequest: ...
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
                        GoogleCloudAiplatformV1beta1ListContextsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListContextsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListContextsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListContextsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1Context = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ContextHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1PurgeContextsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryContextLineageSubgraph(
                        self, *, context: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1LineageSubgraphHttpRequest: ...
                    def removeContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1beta1RemoveContextChildrenRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1RemoveContextChildrenResponseHttpRequest: ...
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
                        body: GoogleCloudAiplatformV1beta1AddExecutionEventsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1AddExecutionEventsResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1Execution = ...,
                        executionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ExecutionHttpRequest: ...
                    def delete(
                        self, *, name: str, etag: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1ExecutionHttpRequest: ...
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
                        GoogleCloudAiplatformV1beta1ListExecutionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListExecutionsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListExecutionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1Execution = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ExecutionHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1PurgeExecutionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryExecutionInputsAndOutputs(
                        self, *, execution: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1LineageSubgraphHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class MetadataSchemasResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1MetadataSchema = ...,
                        metadataSchemaId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1MetadataSchemaHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1MetadataSchemaHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListMetadataSchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListMetadataSchemasResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListMetadataSchemasResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1MetadataStore = ...,
                    metadataStoreId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1MetadataStoreHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListMetadataStoresResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListMetadataStoresResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListMetadataStoresResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListMetadataStoresResponseHttpRequest
                    | None
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
                    body: GoogleCloudAiplatformV1beta1BatchMigrateResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1SearchMigratableResourcesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobHttpRequest
                ): ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1PauseModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ResumeModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def searchModelDeploymentMonitoringStatsAnomalies(
                    self,
                    *,
                    modelDeploymentMonitoringJob: str,
                    body: GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest: ...
                def searchModelDeploymentMonitoringStatsAnomalies_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ModelMonitorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ModelMonitoringJobsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1ModelMonitoringJob = ...,
                        modelMonitoringJobId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ModelMonitoringJobHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1ModelMonitoringJobHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1ModelMonitor = ...,
                    modelMonitorId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1ModelMonitorHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListModelMonitorsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListModelMonitorsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListModelMonitorsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListModelMonitorsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ModelMonitor = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def searchModelMonitoringAlerts(
                    self,
                    *,
                    modelMonitor: str,
                    body: GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponseHttpRequest: ...
                def searchModelMonitoringAlerts_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponseHttpRequest
                    | None
                ): ...
                def searchModelMonitoringStats(
                    self,
                    *,
                    modelMonitor: str,
                    body: GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponseHttpRequest: ...
                def searchModelMonitoringStats_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponseHttpRequest
                    | None
                ): ...
                def modelMonitoringJobs(self) -> ModelMonitoringJobsResource: ...
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
                            body: GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudAiplatformV1beta1ModelEvaluationSliceHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponseHttpRequest
                            | None
                        ): ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1ModelEvaluationHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1ImportModelEvaluationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ModelEvaluationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListModelEvaluationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListModelEvaluationsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListModelEvaluationsResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1CopyModelRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1ExportModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1ModelHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListModelsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListModelsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListModelsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListModelsResponseHttpRequest | None
                ): ...
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
                ) -> (
                    GoogleCloudAiplatformV1beta1ListModelVersionsResponseHttpRequest
                ): ...
                def listVersions_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListModelVersionsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListModelVersionsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListModelVersionsResponseHttpRequest
                    | None
                ): ...
                def mergeVersionAliases(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1MergeVersionAliasesRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ModelHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Model = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ModelHttpRequest: ...
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
                    body: GoogleCloudAiplatformV1beta1UpdateExplanationDatasetRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1UploadModelRequest = ...,
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
                    ) -> GoogleCloudAiplatformV1beta1NasTrialDetailHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponseHttpRequest
                        | None
                    ): ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1CancelNasJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1NasJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1NasJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1NasJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListNasJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListNasJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListNasJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListNasJobsResponseHttpRequest | None
                ): ...
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
                    body: GoogleCloudAiplatformV1beta1NotebookExecutionJob = ...,
                    notebookExecutionJobId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generateAccessToken(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1GenerateAccessTokenResponseHttpRequest
                ): ...
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
                ) -> GoogleCloudAiplatformV1beta1NotebookExecutionJobHttpRequest: ...
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
                ) -> GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponseHttpRequest
                    | None
                ): ...
                def reportEvent(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ReportExecutionEventRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ReportExecutionEventResponseHttpRequest
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
                    body: GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate = ...,
                    notebookRuntimeTemplateId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateHttpRequest: ...
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
                ) -> GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateHttpRequest: ...
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
                    body: GoogleCloudAiplatformV1beta1AssignNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def generateAccessToken(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1GenerateAccessTokenRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1GenerateAccessTokenResponseHttpRequest
                ): ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1NotebookRuntimeHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponseHttpRequest
                    | None
                ): ...
                def reportEvent(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ReportRuntimeEventResponseHttpRequest
                ): ...
                def start(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1StartNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1StopNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upgrade(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1UpgradeNotebookRuntimeRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1PersistentResource = ...,
                    persistentResourceId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1PersistentResourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListPersistentResourcesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListPersistentResourcesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListPersistentResourcesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1PersistentResource = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reboot(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1RebootPersistentResourceRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1BatchCancelPipelineJobsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1BatchDeletePipelineJobsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1CancelPipelineJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1PipelineJob = ...,
                    pipelineJobId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1PipelineJobHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1PipelineJobHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListPipelineJobsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListPipelineJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListPipelineJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListPipelineJobsResponseHttpRequest
                    | None
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
                        body: GoogleCloudAiplatformV1beta1ComputeTokensRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ComputeTokensResponseHttpRequest
                    ): ...
                    def countTokens(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1CountTokensRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1CountTokensResponseHttpRequest: ...
                    def fetchPredictOperation(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1FetchPredictOperationRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def generateContent(
                        self,
                        *,
                        model: str,
                        body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest
                    ): ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def predict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1PredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1PredictResponseHttpRequest: ...
                    def predictLongRunning(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1PredictLongRunningRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def rawPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1RawPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def serverStreamingPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1StreamingPredictRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1StreamingPredictResponseHttpRequest
                    ): ...
                    def streamGenerateContent(
                        self,
                        *,
                        model: str,
                        body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest
                    ): ...
                    def streamRawPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1beta1StreamRawPredictRequest = ...,
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
                    ) -> GoogleCloudAiplatformV1beta1RagFileHttpRequest: ...
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1ImportRagFilesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListRagFilesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListRagFilesResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListRagFilesResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListRagFilesResponseHttpRequest
                        | None
                    ): ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1RagCorpus = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1RagCorpusHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListRagCorporaResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListRagCorporaResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListRagCorporaResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListRagCorporaResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1RagCorpus = ...,
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
                    body: GoogleCloudAiplatformV1beta1ReasoningEngine = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1ReasoningEngineHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListReasoningEnginesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListReasoningEnginesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListReasoningEnginesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListReasoningEnginesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ReasoningEngine = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def query(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1QueryReasoningEngineRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1QueryReasoningEngineResponseHttpRequest
                ): ...
                def streamQuery(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1StreamQueryReasoningEngineRequest = ...,
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
                    body: GoogleCloudAiplatformV1beta1Schedule = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ScheduleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1ScheduleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListSchedulesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListSchedulesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListSchedulesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListSchedulesResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Schedule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ScheduleHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1PauseScheduleRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1ResumeScheduleRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class SolversResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                    body: GoogleCloudAiplatformV1beta1SpecialistPool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1SpecialistPoolHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1SpecialistPool = ...,
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
                        body: GoogleCloudAiplatformV1beta1AddTrialMeasurementRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1TrialHttpRequest: ...
                    def checkTrialEarlyStoppingState(
                        self,
                        *,
                        trialName: str,
                        body: GoogleCloudAiplatformV1beta1CheckTrialEarlyStoppingStateRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def complete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1CompleteTrialRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1TrialHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1Trial = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1TrialHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1beta1TrialHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1ListTrialsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListTrialsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListTrialsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListTrialsResponseHttpRequest | None
                    ): ...
                    def listOptimalTrials(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1ListOptimalTrialsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListOptimalTrialsResponseHttpRequest
                    ): ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1StopTrialRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1TrialHttpRequest: ...
                    def suggest(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1SuggestTrialsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Study = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1StudyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1StudyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListStudiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListStudiesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListStudiesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListStudiesResponseHttpRequest | None
                ): ...
                def lookup(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1LookupStudyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1StudyHttpRequest: ...
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
                                body: GoogleCloudAiplatformV1beta1TensorboardTimeSeries = ...,
                                tensorboardTimeSeriesId: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1beta1TensorboardTimeSeriesHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...
                            def exportTensorboardTimeSeries(
                                self,
                                *,
                                tensorboardTimeSeries: str,
                                body: GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def exportTensorboardTimeSeries_next(
                                self,
                                previous_request: GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponseHttpRequest,
                                previous_response: GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse,
                            ) -> (
                                GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponseHttpRequest
                                | None
                            ): ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudAiplatformV1beta1TensorboardTimeSeriesHttpRequest: ...
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
                            ) -> GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponseHttpRequest,
                                previous_response: GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse,
                            ) -> (
                                GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponseHttpRequest
                                | None
                            ): ...
                            def patch(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudAiplatformV1beta1TensorboardTimeSeries = ...,
                                updateMask: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1beta1TensorboardTimeSeriesHttpRequest: ...
                            def read(
                                self,
                                *,
                                tensorboardTimeSeries: str,
                                filter: str = ...,
                                maxDataPoints: int = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def readBlobData(
                                self,
                                *,
                                timeSeries: str,
                                blobIds: str | _list[str] = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponseHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1beta1TensorboardRun = ...,
                            tensorboardRunId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1TensorboardRunHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1beta1TensorboardRunHttpRequest: ...
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
                        ) -> GoogleCloudAiplatformV1beta1ListTensorboardRunsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudAiplatformV1beta1ListTensorboardRunsResponseHttpRequest,
                            previous_response: GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse,
                        ) -> (
                            GoogleCloudAiplatformV1beta1ListTensorboardRunsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudAiplatformV1beta1TensorboardRun = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1TensorboardRunHttpRequest: ...
                        def write(
                            self,
                            *,
                            tensorboardRun: str,
                            body: GoogleCloudAiplatformV1beta1WriteTensorboardRunDataRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponseHttpRequest: ...
                        def operations(self) -> OperationsResource: ...
                        def timeSeries(self) -> TimeSeriesResource: ...

                    def batchCreate(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1beta1TensorboardExperiment = ...,
                        tensorboardExperimentId: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1TensorboardExperimentHttpRequest
                    ): ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1beta1TensorboardExperimentHttpRequest
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
                    ) -> GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponseHttpRequest,
                        previous_response: GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse,
                    ) -> (
                        GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1beta1TensorboardExperiment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudAiplatformV1beta1TensorboardExperimentHttpRequest
                    ): ...
                    def write(
                        self,
                        *,
                        tensorboardExperiment: str,
                        body: GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponseHttpRequest: ...
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
                ) -> GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1Tensorboard = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1TensorboardHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListTensorboardsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListTensorboardsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListTensorboardsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListTensorboardsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1Tensorboard = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def readSize(
                    self, *, tensorboard: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponseHttpRequest
                ): ...
                def readUsage(
                    self, *, tensorboard: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponseHttpRequest
                ): ...
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
                    body: GoogleCloudAiplatformV1beta1CancelTrainingPipelineRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1TrainingPipeline = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1TrainingPipelineHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1TrainingPipelineHttpRequest: ...
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
                    GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponseHttpRequest
                    | None
                ): ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class TuningJobsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...

                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1beta1CancelTuningJobRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1TuningJob = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1TuningJobHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1beta1TuningJobHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAiplatformV1beta1ListTuningJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1beta1ListTuningJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1beta1ListTuningJobsResponse,
                ) -> (
                    GoogleCloudAiplatformV1beta1ListTuningJobsResponseHttpRequest | None
                ): ...
                def rebaseTunedModel(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1beta1RebaseTunedModelRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            def augmentPrompt(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1beta1AugmentPromptRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1AugmentPromptResponseHttpRequest: ...
            def corroborateContent(
                self,
                *,
                parent: str,
                body: GoogleCloudAiplatformV1beta1CorroborateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1CorroborateContentResponseHttpRequest: ...
            def deploy(
                self,
                *,
                destination: str,
                body: GoogleCloudAiplatformV1beta1DeployPublisherModelRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def evaluateInstances(
                self,
                *,
                location: str,
                body: GoogleCloudAiplatformV1beta1EvaluateInstancesRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1EvaluateInstancesResponseHttpRequest: ...
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
                body: GoogleCloudAiplatformV1beta1RetrieveContextsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1RetrieveContextsResponseHttpRequest: ...
            def agents(self) -> AgentsResource: ...
            def apps(self) -> AppsResource: ...
            def batchPredictionJobs(self) -> BatchPredictionJobsResource: ...
            def cachedContents(self) -> CachedContentsResource: ...
            def customJobs(self) -> CustomJobsResource: ...
            def dataLabelingJobs(self) -> DataLabelingJobsResource: ...
            def datasets(self) -> DatasetsResource: ...
            def deploymentResourcePools(self) -> DeploymentResourcePoolsResource: ...
            def edgeDevices(self) -> EdgeDevicesResource: ...
            def endpoints(self) -> EndpointsResource: ...
            def evaluationTasks(self) -> EvaluationTasksResource: ...
            def exampleStores(self) -> ExampleStoresResource: ...
            def extensionControllers(self) -> ExtensionControllersResource: ...
            def extensions(self) -> ExtensionsResource: ...
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
            def modelMonitors(self) -> ModelMonitorsResource: ...
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
            def solvers(self) -> SolversResource: ...
            def specialistPools(self) -> SpecialistPoolsResource: ...
            def studies(self) -> StudiesResource: ...
            def tensorboards(self) -> TensorboardsResource: ...
            def trainingPipelines(self) -> TrainingPipelinesResource: ...
            def tuningJobs(self) -> TuningJobsResource: ...

        def getCacheConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudAiplatformV1beta1CacheConfigHttpRequest: ...
        def updateCacheConfig(
            self,
            *,
            name: str,
            body: GoogleCloudAiplatformV1beta1CacheConfig = ...,
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
                body: GoogleCloudAiplatformV1beta1ComputeTokensRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1ComputeTokensResponseHttpRequest: ...
            def countTokens(
                self,
                *,
                endpoint: str,
                body: GoogleCloudAiplatformV1beta1CountTokensRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1CountTokensResponseHttpRequest: ...
            def generateContent(
                self,
                *,
                model: str,
                body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...
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
            ) -> GoogleCloudAiplatformV1beta1PublisherModelHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                languageCode: str = ...,
                listAllVersions: bool = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "PUBLISHER_MODEL_VIEW_UNSPECIFIED",
                    "PUBLISHER_MODEL_VIEW_BASIC",
                    "PUBLISHER_MODEL_VIEW_FULL",
                    "PUBLISHER_MODEL_VERSION_VIEW_BASIC",
                ] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1ListPublisherModelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudAiplatformV1beta1ListPublisherModelsResponseHttpRequest,
                previous_response: GoogleCloudAiplatformV1beta1ListPublisherModelsResponse,
            ) -> (
                GoogleCloudAiplatformV1beta1ListPublisherModelsResponseHttpRequest
                | None
            ): ...
            def streamGenerateContent(
                self,
                *,
                model: str,
                body: GoogleCloudAiplatformV1beta1GenerateContentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest: ...

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
class GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1AddContextArtifactsAndExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1AddContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AddExecutionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1AddExecutionEventsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AnnotationSpecHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1AnnotationSpec: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Artifact: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1AugmentPromptResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1AugmentPromptResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1BatchCreateTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1BatchCreateTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1BatchImportEvaluatedAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchPredictionJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1BatchPredictionJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1BatchReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CacheConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1CacheConfig: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CachedContentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1CachedContent: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ComputeTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ComputeTokensResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Context: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CorroborateContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1CorroborateContentResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CountTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1CountTokensResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1CustomJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1CustomJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DataLabelingJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1DataLabelingJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Dataset: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DatasetVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1DatasetVersion: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DeploymentResourcePoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1DeploymentResourcePool: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1DirectPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1DirectRawPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1DirectRawPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Endpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EntityTypeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1EntityType: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1EvaluateInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1EvaluateInstancesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecuteExtensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ExecuteExtensionResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExecutionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Execution: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExplainResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ExplainResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ExportTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ExtensionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Extension: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Feature: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureGroup: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureMonitor: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureMonitorJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureMonitorJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureOnlineStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureOnlineStore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureView: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeatureViewSyncHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FeatureViewSync: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FeaturestoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Featurestore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FetchFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FetchFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1FindNeighborsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1FindNeighborsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateAccessTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1GenerateAccessTokenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1GenerateContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1GenerateContentResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1HyperparameterTuningJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1HyperparameterTuningJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Index: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1IndexEndpointHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1IndexEndpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1LineageSubgraphHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1LineageSubgraph: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListArtifactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListArtifactsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListBatchPredictionJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCachedContentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListCachedContentsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListContextsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListCustomJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListCustomJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListDataLabelingJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListDatasetVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListDeploymentResourcePoolsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListExtensionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListExtensionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureGroupsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureMonitorJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureMonitorsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureOnlineStoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureViewSyncsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeatureViewsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeatureViewsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListFeaturestoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListFeaturestoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListHyperparameterTuningJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListIndexEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListIndexesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListMetadataSchemasResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListMetadataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListMetadataStoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelDeploymentMonitoringJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelEvaluationSlicesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelMonitoringJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelMonitorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelMonitorsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListNasJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListNasTrialDetailsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListNotebookExecutionJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListNotebookRuntimeTemplatesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListNotebookRuntimesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListOptimalTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListOptimalTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPersistentResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListPersistentResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPipelineJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListPipelineJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListPublisherModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListPublisherModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagCorporaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListRagCorporaResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListRagFilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListRagFilesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListReasoningEnginesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListReasoningEnginesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSavedQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListSavedQueriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSchedulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListSchedulesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListSpecialistPoolsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListStudiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListStudiesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTensorboardExperimentsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTensorboardsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTensorboardsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTrainingPipelinesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ListTuningJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ListTuningJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1MetadataSchema: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1MetadataStoreHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1MetadataStore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Model: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ModelDeploymentMonitoringJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ModelEvaluation: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelEvaluationSliceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ModelEvaluationSlice: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ModelMonitor: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ModelMonitoringJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ModelMonitoringJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1NasJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NasTrialDetailHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1NasTrialDetail: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookExecutionJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1NotebookExecutionJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1NotebookRuntime: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1NotebookRuntimeTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1NotebookRuntimeTemplate: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PersistentResourceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1PersistentResource: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PipelineJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1PipelineJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1PredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1PublisherModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1PublisherModel: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryDeployedModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1QueryDeployedModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryExtensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1QueryExtensionResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1QueryReasoningEngineResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1QueryReasoningEngineResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagCorpusHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1RagCorpus: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RagFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1RagFile: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadIndexDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadTensorboardBlobDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadTensorboardSizeResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReadTensorboardUsageResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReasoningEngineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReasoningEngine: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1RemoveContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RemoveDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1RemoveDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportExecutionEventResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReportExecutionEventResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ReportRuntimeEventResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1ReportRuntimeEventResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1RetrieveContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1RetrieveContextsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1ScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Schedule: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchMigratableResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchModelMonitoringAlertsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchModelMonitoringStatsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SearchNearestEntitiesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SpecialistPoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SpecialistPool: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1StreamingFetchFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StreamingPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1StreamingPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1StudyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Study: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1SyncFeatureViewResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1SyncFeatureViewResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Tensorboard: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardExperimentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1TensorboardExperiment: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardRunHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1TensorboardRun: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TensorboardTimeSeriesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1TensorboardTimeSeries: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrainingPipelineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1TrainingPipeline: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TrialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1Trial: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1TuningJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1TuningJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UploadRagFileResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1UploadRagFileResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1UpsertDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1UpsertDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1WriteFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1WriteTensorboardExperimentDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAiplatformV1beta1WriteTensorboardRunDataResponse: ...

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
