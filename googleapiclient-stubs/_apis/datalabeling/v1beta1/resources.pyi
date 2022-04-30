import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DataLabelingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnnotationSpecSetsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDatalabelingV1beta1CreateAnnotationSpecSetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1AnnotationSpecSetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1AnnotationSpecSetHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseHttpRequest,
                previous_response: GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponse,
            ) -> GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseHttpRequest | None: ...

        @typing.type_check_only
        class DatasetsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AnnotatedDatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DataItemsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1DataItemHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest,
                        previous_response: GoogleCloudDatalabelingV1beta1ListDataItemsResponse,
                    ) -> GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ExamplesResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, filter: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1ExampleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1ListExamplesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatalabelingV1beta1ListExamplesResponseHttpRequest,
                        previous_response: GoogleCloudDatalabelingV1beta1ListExamplesResponse,
                    ) -> GoogleCloudDatalabelingV1beta1ListExamplesResponseHttpRequest | None: ...

                @typing.type_check_only
                class FeedbackThreadsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FeedbackMessagesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDatalabelingV1beta1FeedbackMessage = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDatalabelingV1beta1FeedbackMessageHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseHttpRequest,
                            previous_response: GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponse,
                        ) -> GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseHttpRequest | None: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1FeedbackThreadHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseHttpRequest,
                        previous_response: GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponse,
                    ) -> GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseHttpRequest | None: ...
                    def feedbackMessages(self) -> FeedbackMessagesResource: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatalabelingV1beta1AnnotatedDatasetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseHttpRequest,
                    previous_response: GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponse,
                ) -> GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseHttpRequest | None: ...
                def dataItems(self) -> DataItemsResource: ...
                def examples(self) -> ExamplesResource: ...
                def feedbackThreads(self) -> FeedbackThreadsResource: ...

            @typing.type_check_only
            class DataItemsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatalabelingV1beta1DataItemHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest,
                    previous_response: GoogleCloudDatalabelingV1beta1ListDataItemsResponse,
                ) -> GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest | None: ...

            @typing.type_check_only
            class EvaluationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExampleComparisonsResource(googleapiclient.discovery.Resource):
                    def search(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDatalabelingV1beta1SearchExampleComparisonsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseHttpRequest: ...
                    def search_next(
                        self,
                        previous_request: GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseHttpRequest,
                        previous_response: GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponse,
                    ) -> GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseHttpRequest | None: ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatalabelingV1beta1EvaluationHttpRequest: ...
                def exampleComparisons(self) -> ExampleComparisonsResource: ...

            @typing.type_check_only
            class ImageResource(googleapiclient.discovery.Resource):
                def label(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatalabelingV1beta1LabelImageRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class TextResource(googleapiclient.discovery.Resource):
                def label(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatalabelingV1beta1LabelTextRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class VideoResource(googleapiclient.discovery.Resource):
                def label(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatalabelingV1beta1LabelVideoRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDatalabelingV1beta1CreateDatasetRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1DatasetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def exportData(
                self,
                *,
                name: str,
                body: GoogleCloudDatalabelingV1beta1ExportDataRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1DatasetHttpRequest: ...
            def importData(
                self,
                *,
                name: str,
                body: GoogleCloudDatalabelingV1beta1ImportDataRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1ListDatasetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDatalabelingV1beta1ListDatasetsResponseHttpRequest,
                previous_response: GoogleCloudDatalabelingV1beta1ListDatasetsResponse,
            ) -> GoogleCloudDatalabelingV1beta1ListDatasetsResponseHttpRequest | None: ...
            def annotatedDatasets(self) -> AnnotatedDatasetsResource: ...
            def dataItems(self) -> DataItemsResource: ...
            def evaluations(self) -> EvaluationsResource: ...
            def image(self) -> ImageResource: ...
            def text(self) -> TextResource: ...
            def video(self) -> VideoResource: ...

        @typing.type_check_only
        class EvaluationJobsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDatalabelingV1beta1CreateEvaluationJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1EvaluationJobHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1EvaluationJobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseHttpRequest,
                previous_response: GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponse,
            ) -> GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudDatalabelingV1beta1EvaluationJob = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1EvaluationJobHttpRequest: ...
            def pause(
                self,
                *,
                name: str,
                body: GoogleCloudDatalabelingV1beta1PauseEvaluationJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def resume(
                self,
                *,
                name: str,
                body: GoogleCloudDatalabelingV1beta1ResumeEvaluationJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...

        @typing.type_check_only
        class EvaluationsResource(googleapiclient.discovery.Resource):
            def search(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseHttpRequest,
                previous_response: GoogleCloudDatalabelingV1beta1SearchEvaluationsResponse,
            ) -> GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class InstructionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudDatalabelingV1beta1CreateInstructionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1InstructionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatalabelingV1beta1ListInstructionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudDatalabelingV1beta1ListInstructionsResponseHttpRequest,
                previous_response: GoogleCloudDatalabelingV1beta1ListInstructionsResponse,
            ) -> GoogleCloudDatalabelingV1beta1ListInstructionsResponseHttpRequest | None: ...

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

        def annotationSpecSets(self) -> AnnotationSpecSetsResource: ...
        def datasets(self) -> DatasetsResource: ...
        def evaluationJobs(self) -> EvaluationJobsResource: ...
        def evaluations(self) -> EvaluationsResource: ...
        def instructions(self) -> InstructionsResource: ...
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
class GoogleCloudDatalabelingV1beta1AnnotatedDatasetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1AnnotatedDataset: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1AnnotationSpecSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1AnnotationSpecSet: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1DataItemHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1DataItem: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1DatasetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1Dataset: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1Evaluation: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1EvaluationJobHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1EvaluationJob: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ExampleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1Example: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1FeedbackMessageHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1FeedbackMessage: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1FeedbackThreadHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1FeedbackThread: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1InstructionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1Instruction: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListAnnotatedDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListAnnotationSpecSetsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListDataItemsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListDataItemsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListDatasetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListDatasetsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListEvaluationJobsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListExamplesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListExamplesResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListFeedbackMessagesResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListFeedbackThreadsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1ListInstructionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1ListInstructionsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SearchEvaluationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1SearchEvaluationsResponse: ...

@typing.type_check_only
class GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatalabelingV1beta1SearchExampleComparisonsResponse: ...

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
