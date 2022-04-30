import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ToolResultsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class HistoriesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ExecutionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ClustersResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        clusterId: str,
                        **kwargs: typing.Any
                    ) -> ScreenshotClusterHttpRequest: ...
                    def list(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        **kwargs: typing.Any
                    ) -> ListScreenshotClustersResponseHttpRequest: ...

                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        environmentId: str,
                        **kwargs: typing.Any
                    ) -> EnvironmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEnvironmentsResponseHttpRequest,
                        previous_response: ListEnvironmentsResponse,
                    ) -> ListEnvironmentsResponseHttpRequest | None: ...

                @typing.type_check_only
                class StepsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class PerfMetricsSummaryResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            body: PerfMetricsSummary = ...,
                            **kwargs: typing.Any
                        ) -> PerfMetricsSummaryHttpRequest: ...

                    @typing.type_check_only
                    class PerfSampleSeriesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class SamplesResource(googleapiclient.discovery.Resource):
                            def batchCreate(
                                self,
                                *,
                                projectId: str,
                                historyId: str,
                                executionId: str,
                                stepId: str,
                                sampleSeriesId: str,
                                body: BatchCreatePerfSamplesRequest = ...,
                                **kwargs: typing.Any
                            ) -> BatchCreatePerfSamplesResponseHttpRequest: ...
                            def list(
                                self,
                                *,
                                projectId: str,
                                historyId: str,
                                executionId: str,
                                stepId: str,
                                sampleSeriesId: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> ListPerfSamplesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: ListPerfSamplesResponseHttpRequest,
                                previous_response: ListPerfSamplesResponse,
                            ) -> ListPerfSamplesResponseHttpRequest | None: ...

                        def create(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            body: PerfSampleSeries = ...,
                            **kwargs: typing.Any
                        ) -> PerfSampleSeriesHttpRequest: ...
                        def get(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            sampleSeriesId: str,
                            **kwargs: typing.Any
                        ) -> PerfSampleSeriesHttpRequest: ...
                        def list(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            filter: typing_extensions.Literal[
                                "perfMetricTypeUnspecified",
                                "memory",
                                "cpu",
                                "network",
                                "graphics",
                            ]
                            | _list[
                                typing_extensions.Literal[
                                    "perfMetricTypeUnspecified",
                                    "memory",
                                    "cpu",
                                    "network",
                                    "graphics",
                                ]
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListPerfSampleSeriesResponseHttpRequest: ...
                        def samples(self) -> SamplesResource: ...

                    @typing.type_check_only
                    class TestCasesResource(googleapiclient.discovery.Resource):
                        def get(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            testCaseId: str,
                            **kwargs: typing.Any
                        ) -> TestCaseHttpRequest: ...
                        def list(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListTestCasesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListTestCasesResponseHttpRequest,
                            previous_response: ListTestCasesResponse,
                        ) -> ListTestCasesResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class ThumbnailsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            projectId: str,
                            historyId: str,
                            executionId: str,
                            stepId: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListStepThumbnailsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListStepThumbnailsResponseHttpRequest,
                            previous_response: ListStepThumbnailsResponse,
                        ) -> ListStepThumbnailsResponseHttpRequest | None: ...

                    def accessibilityClusters(
                        self, *, name: str, locale: str = ..., **kwargs: typing.Any
                    ) -> ListStepAccessibilityClustersResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        body: Step = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> StepHttpRequest: ...
                    def get(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        stepId: str,
                        **kwargs: typing.Any
                    ) -> StepHttpRequest: ...
                    def getPerfMetricsSummary(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        stepId: str,
                        **kwargs: typing.Any
                    ) -> PerfMetricsSummaryHttpRequest: ...
                    def list(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListStepsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListStepsResponseHttpRequest,
                        previous_response: ListStepsResponse,
                    ) -> ListStepsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        stepId: str,
                        body: Step = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any
                    ) -> StepHttpRequest: ...
                    def publishXunitXmlFiles(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        stepId: str,
                        body: PublishXunitXmlFilesRequest = ...,
                        **kwargs: typing.Any
                    ) -> StepHttpRequest: ...
                    def perfMetricsSummary(self) -> PerfMetricsSummaryResource: ...
                    def perfSampleSeries(self) -> PerfSampleSeriesResource: ...
                    def testCases(self) -> TestCasesResource: ...
                    def thumbnails(self) -> ThumbnailsResource: ...

                def create(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    body: Execution = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    executionId: str,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListExecutionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListExecutionsResponseHttpRequest,
                    previous_response: ListExecutionsResponse,
                ) -> ListExecutionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    executionId: str,
                    body: Execution = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def clusters(self) -> ClustersResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def steps(self) -> StepsResource: ...

            def create(
                self,
                *,
                projectId: str,
                body: History = ...,
                requestId: str = ...,
                **kwargs: typing.Any
            ) -> HistoryHttpRequest: ...
            def get(
                self, *, projectId: str, historyId: str, **kwargs: typing.Any
            ) -> HistoryHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filterByName: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListHistoriesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListHistoriesResponseHttpRequest,
                previous_response: ListHistoriesResponse,
            ) -> ListHistoriesResponseHttpRequest | None: ...
            def executions(self) -> ExecutionsResource: ...

        def getSettings(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectSettingsHttpRequest: ...
        def initializeSettings(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectSettingsHttpRequest: ...
        def histories(self) -> HistoriesResource: ...

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
class BatchCreatePerfSamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchCreatePerfSamplesResponse: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Environment: ...

@typing.type_check_only
class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Execution: ...

@typing.type_check_only
class HistoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> History: ...

@typing.type_check_only
class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEnvironmentsResponse: ...

@typing.type_check_only
class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListExecutionsResponse: ...

@typing.type_check_only
class ListHistoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListHistoriesResponse: ...

@typing.type_check_only
class ListPerfSampleSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPerfSampleSeriesResponse: ...

@typing.type_check_only
class ListPerfSamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPerfSamplesResponse: ...

@typing.type_check_only
class ListScreenshotClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListScreenshotClustersResponse: ...

@typing.type_check_only
class ListStepAccessibilityClustersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListStepAccessibilityClustersResponse: ...

@typing.type_check_only
class ListStepThumbnailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListStepThumbnailsResponse: ...

@typing.type_check_only
class ListStepsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListStepsResponse: ...

@typing.type_check_only
class ListTestCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTestCasesResponse: ...

@typing.type_check_only
class PerfMetricsSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PerfMetricsSummary: ...

@typing.type_check_only
class PerfSampleSeriesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PerfSampleSeries: ...

@typing.type_check_only
class ProjectSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProjectSettings: ...

@typing.type_check_only
class ScreenshotClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ScreenshotCluster: ...

@typing.type_check_only
class StepHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Step: ...

@typing.type_check_only
class TestCaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestCase: ...
