import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AiplatformResource(googleapiclient.discovery.Resource):
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1BatchPredictionJob = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1CustomJob = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1DataLabelingJob = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def export(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ExportDataRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, readMask: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1DatasetHttpRequest: ...
                def import_(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ImportDataRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    body: GoogleCloudAiplatformV1Endpoint = ...,
                    endpointId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deployModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1DeployModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def explain(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1ExplainRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ExplainResponseHttpRequest: ...
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Endpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1EndpointHttpRequest: ...
                def predict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1PredictRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1PredictResponseHttpRequest: ...
                def rawPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1RawPredictRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def serverStreamingPredict(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1StreamingPredictRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest: ...
                def undeployModel(
                    self,
                    *,
                    endpoint: str,
                    body: GoogleCloudAiplatformV1UndeployModelRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
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
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
                            ) -> GoogleLongrunningOperationHttpRequest: ...

                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1BatchCreateFeaturesRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1Feature = ...,
                            featureId: str = ...,
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def deleteFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1DeleteFeatureValuesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def exportFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ExportFeatureValuesRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1EntityTypeHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def importFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ImportFeatureValuesRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1EntityTypeHttpRequest: ...
                    def readFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1ReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def streamingReadFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1StreamingReadFeatureValuesRequest = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest
                    ): ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        permissions: str | _list[str] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def writeFeatureValues(
                        self,
                        *,
                        entityType: str,
                        body: GoogleCloudAiplatformV1WriteFeatureValuesRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Featurestore = ...,
                    featurestoreId: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def searchFeatures(
                    self,
                    *,
                    location: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1HyperparameterTuningJob = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def deployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1DeployIndexRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def findNeighbors(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1FindNeighborsRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1IndexEndpoint = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1IndexEndpointHttpRequest: ...
                def readIndexDatapoints(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1ReadIndexDatapointsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ReadIndexDatapointsResponseHttpRequest: ...
                def undeployIndex(
                    self,
                    *,
                    indexEndpoint: str,
                    body: GoogleCloudAiplatformV1UndeployIndexRequest = ...,
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def removeDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1RemoveDatapointsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1RemoveDatapointsResponseHttpRequest: ...
                def upsertDatapoints(
                    self,
                    *,
                    index: str,
                    body: GoogleCloudAiplatformV1UpsertDatapointsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1UpsertDatapointsResponseHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class MetadataStoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ArtifactsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Artifact = ...,
                        artifactId: str = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ArtifactHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeArtifactsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryArtifactLineageSubgraph(
                        self,
                        *,
                        artifact: str,
                        filter: str = ...,
                        maxHops: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...

                @typing.type_check_only
                class ContextsResource(googleapiclient.discovery.Resource):
                    def addContextArtifactsAndExecutions(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponseHttpRequest: ...
                    def addContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1AddContextChildrenRequest = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1AddContextChildrenResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Context = ...,
                        contextId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ContextHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        etag: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ContextHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeContextsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryContextLineageSubgraph(
                        self, *, context: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...
                    def removeContextChildren(
                        self,
                        *,
                        context: str,
                        body: GoogleCloudAiplatformV1RemoveContextChildrenRequest = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1RemoveContextChildrenResponseHttpRequest
                    ): ...

                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    def addExecutionEvents(
                        self,
                        *,
                        execution: str,
                        body: GoogleCloudAiplatformV1AddExecutionEventsRequest = ...,
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1AddExecutionEventsResponseHttpRequest
                    ): ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Execution = ...,
                        executionId: str = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ExecutionHttpRequest: ...
                    def purge(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1PurgeExecutionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def queryExecutionInputsAndOutputs(
                        self, *, execution: str, **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1LineageSubgraphHttpRequest: ...

                @typing.type_check_only
                class MetadataSchemasResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1MetadataSchema = ...,
                        metadataSchemaId: str = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1MetadataStore = ...,
                    metadataStoreId: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1SearchMigratableResourcesRequest = ...,
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1PauseModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ResumeModelDeploymentMonitoringJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def searchModelDeploymentMonitoringStatsAnomalies(
                    self,
                    *,
                    modelDeploymentMonitoringJob: str,
                    body: GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest = ...,
                    **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1ModelEvaluationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1Model = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ModelHttpRequest: ...
                def updateExplanationDataset(
                    self,
                    *,
                    model: str,
                    body: GoogleCloudAiplatformV1UpdateExplanationDatasetRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1UploadModelRequest = ...,
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1NasJob = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNasJobsResponse,
                ) -> GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest | None: ...
                def nasTrialDetails(self) -> NasTrialDetailsResource: ...

            @typing.type_check_only
            class NotebookRuntimeTemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1NotebookRuntimeTemplate = ...,
                    notebookRuntimeTemplateId: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest,
                    previous_response: GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse,
                ) -> (
                    GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest
                    | None
                ): ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    permissions: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class NotebookRuntimesResource(googleapiclient.discovery.Resource):
                def assign(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1AssignNotebookRuntimeRequest = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    body: GoogleCloudAiplatformV1CancelPipelineJobRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1PipelineJob = ...,
                    pipelineJobId: str = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    def predict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1PredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1PredictResponseHttpRequest: ...
                    def rawPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1RawPredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def serverStreamingPredict(
                        self,
                        *,
                        endpoint: str,
                        body: GoogleCloudAiplatformV1StreamingPredictRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest: ...

                def models(self) -> ModelsResource: ...

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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleCloudAiplatformV1ScheduleHttpRequest: ...
                def pause(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1PauseScheduleRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudAiplatformV1ResumeScheduleRequest = ...,
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def checkTrialEarlyStoppingState(
                        self,
                        *,
                        trialName: str,
                        body: GoogleCloudAiplatformV1CheckTrialEarlyStoppingStateRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def complete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1CompleteTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1Trial = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> (
                        GoogleCloudAiplatformV1ListOptimalTrialsResponseHttpRequest
                    ): ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudAiplatformV1StopTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TrialHttpRequest: ...
                    def suggest(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1SuggestTrialsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1Study = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                                    **kwargs: typing.Any
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
                                    **kwargs: typing.Any
                                ) -> GoogleLongrunningOperationHttpRequest: ...

                            def batchCreate(
                                self,
                                *,
                                parent: str,
                                runsId: str,
                                body: GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesRequest = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponseHttpRequest: ...
                            def batchRead(
                                self,
                                *,
                                tensorboard: str,
                                experimentsId: str,
                                runsId: str,
                                timeSeries: str | _list[str] = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudAiplatformV1TensorboardTimeSeries = ...,
                                tensorboardTimeSeriesId: str = ...,
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
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
                                **kwargs: typing.Any
                            ) -> (
                                GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest
                            ): ...
                            def read(
                                self,
                                *,
                                tensorboardTimeSeries: str,
                                filter: str = ...,
                                maxDataPoints: int = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponseHttpRequest: ...
                            def readBlobData(
                                self,
                                *,
                                timeSeries: str,
                                blobIds: str | _list[str] = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudAiplatformV1ReadTensorboardBlobDataResponseHttpRequest: ...
                            def operations(self) -> OperationsResource: ...

                        def batchCreate(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1BatchCreateTensorboardRunsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudAiplatformV1TensorboardRun = ...,
                            tensorboardRunId: str = ...,
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
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
                            **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1TensorboardRunHttpRequest: ...
                        def write(
                            self,
                            *,
                            tensorboardRun: str,
                            body: GoogleCloudAiplatformV1WriteTensorboardRunDataRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudAiplatformV1WriteTensorboardRunDataResponseHttpRequest: ...
                        def operations(self) -> OperationsResource: ...
                        def timeSeries(self) -> TimeSeriesResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudAiplatformV1TensorboardExperiment = ...,
                        tensorboardExperimentId: str = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
                    ) -> GoogleCloudAiplatformV1TensorboardExperimentHttpRequest: ...
                    def write(
                        self,
                        *,
                        tensorboardExperiment: str,
                        body: GoogleCloudAiplatformV1WriteTensorboardExperimentDataRequest = ...,
                        **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    body: GoogleCloudAiplatformV1Tensorboard = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
                        **kwargs: typing.Any
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
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudAiplatformV1TrainingPipeline = ...,
                    **kwargs: typing.Any
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
                    **kwargs: typing.Any
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
            def batchPredictionJobs(self) -> BatchPredictionJobsResource: ...
            def customJobs(self) -> CustomJobsResource: ...
            def dataLabelingJobs(self) -> DataLabelingJobsResource: ...
            def datasets(self) -> DatasetsResource: ...
            def deploymentResourcePools(self) -> DeploymentResourcePoolsResource: ...
            def endpoints(self) -> EndpointsResource: ...
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
            def notebookRuntimeTemplates(self) -> NotebookRuntimeTemplatesResource: ...
            def notebookRuntimes(self) -> NotebookRuntimesResource: ...
            def operations(self) -> OperationsResource: ...
            def pipelineJobs(self) -> PipelineJobsResource: ...
            def publishers(self) -> PublishersResource: ...
            def schedules(self) -> SchedulesResource: ...
            def specialistPools(self) -> SpecialistPoolsResource: ...
            def studies(self) -> StudiesResource: ...
            def tensorboards(self) -> TensorboardsResource: ...
            def trainingPipelines(self) -> TrainingPipelinesResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class PublishersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ModelsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                languageCode: str = ...,
                view: typing_extensions.Literal[
                    "PUBLISHER_MODEL_VIEW_UNSPECIFIED",
                    "PUBLISHER_MODEL_VIEW_BASIC",
                    "PUBLISHER_MODEL_VIEW_FULL",
                    "PUBLISHER_MODEL_VERSION_VIEW_BASIC",
                ] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudAiplatformV1PublisherModelHttpRequest: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def publishers(self) -> PublishersResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1AddContextArtifactsAndExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1AddContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AddExecutionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1AddExecutionEventsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1AnnotationSpecHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1AnnotationSpec: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Artifact: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1BatchCreateTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1BatchCreateTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1BatchImportEvaluatedAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchPredictionJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1BatchPredictionJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1BatchReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Context: ...

@typing.type_check_only
class GoogleCloudAiplatformV1CustomJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1CustomJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DataLabelingJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1DataLabelingJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Dataset: ...

@typing.type_check_only
class GoogleCloudAiplatformV1DatasetVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1DatasetVersion: ...

@typing.type_check_only
class GoogleCloudAiplatformV1EndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Endpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1EntityTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1EntityType: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Execution: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExplainResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ExplainResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ExportTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeatureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Feature: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FeaturestoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Featurestore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1FindNeighborsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1FindNeighborsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1HyperparameterTuningJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1HyperparameterTuningJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Index: ...

@typing.type_check_only
class GoogleCloudAiplatformV1IndexEndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1IndexEndpoint: ...

@typing.type_check_only
class GoogleCloudAiplatformV1LineageSubgraphHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1LineageSubgraph: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListAnnotationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListAnnotationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListArtifactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListArtifactsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListBatchPredictionJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListBatchPredictionJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListContextsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListContextsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListCustomJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListCustomJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDataLabelingJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListDataLabelingJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListDatasetVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListEntityTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListEntityTypesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListFeaturestoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListFeaturestoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListHyperparameterTuningJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexEndpointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListIndexEndpointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListIndexesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListMetadataSchemasResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListMetadataStoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListMetadataStoresResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListModelDeploymentMonitoringJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationSlicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListModelEvaluationSlicesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListModelEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListModelVersionsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListModelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListModelsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListNasJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNasTrialDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListNasTrialDetailsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListNotebookRuntimeTemplatesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListNotebookRuntimesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListNotebookRuntimesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListOptimalTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListOptimalTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListPipelineJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListPipelineJobsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSavedQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListSavedQueriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSchedulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListSchedulesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListSpecialistPoolsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListSpecialistPoolsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListStudiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListStudiesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTensorboardExperimentsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardRunsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTensorboardRunsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTensorboardTimeSeriesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTensorboardsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTensorboardsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrainingPipelinesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTrainingPipelinesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ListTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ListTrialsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1MetadataSchema: ...

@typing.type_check_only
class GoogleCloudAiplatformV1MetadataStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1MetadataStore: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Model: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelDeploymentMonitoringJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ModelDeploymentMonitoringJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ModelEvaluation: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ModelEvaluationSliceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ModelEvaluationSlice: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NasJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1NasJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NasTrialDetailHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1NasTrialDetail: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1NotebookRuntime: ...

@typing.type_check_only
class GoogleCloudAiplatformV1NotebookRuntimeTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1NotebookRuntimeTemplate: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PipelineJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1PipelineJob: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1PredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1PublisherModelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1PublisherModel: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadIndexDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadIndexDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardBlobDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadTensorboardBlobDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardSizeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadTensorboardSizeResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadTensorboardTimeSeriesDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ReadTensorboardUsageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1ReadTensorboardUsageResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveContextChildrenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1RemoveContextChildrenResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1RemoveDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1RemoveDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1ScheduleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Schedule: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1SearchDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1SearchFeaturesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchMigratableResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1SearchMigratableResourcesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> (
        GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesResponse
    ): ...

@typing.type_check_only
class GoogleCloudAiplatformV1SpecialistPoolHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1SpecialistPool: ...

@typing.type_check_only
class GoogleCloudAiplatformV1StreamingPredictResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1StreamingPredictResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1StudyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Study: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Tensorboard: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardExperimentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1TensorboardExperiment: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardRunHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1TensorboardRun: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TensorboardTimeSeriesHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1TensorboardTimeSeries: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrainingPipelineHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1TrainingPipeline: ...

@typing.type_check_only
class GoogleCloudAiplatformV1TrialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1Trial: ...

@typing.type_check_only
class GoogleCloudAiplatformV1UpsertDatapointsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1UpsertDatapointsResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteFeatureValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1WriteFeatureValuesResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1WriteTensorboardExperimentDataResponse: ...

@typing.type_check_only
class GoogleCloudAiplatformV1WriteTensorboardRunDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudAiplatformV1WriteTensorboardRunDataResponse: ...

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
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

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
