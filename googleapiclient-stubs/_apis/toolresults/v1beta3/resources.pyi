import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ToolResultsResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class HistoriesResource(googleapiclient.discovery.Resource):
            class ExecutionsResource(googleapiclient.discovery.Resource):
                class StepsResource(googleapiclient.discovery.Resource):
                    class PerfSampleSeriesResource(googleapiclient.discovery.Resource):
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
                                pageToken: str = ...,
                                pageSize: int = ...,
                                **kwargs: typing.Any
                            ) -> ListPerfSamplesResponseHttpRequest: ...
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
                            filter: typing.Union[
                                typing_extensions.Literal[
                                    "perfMetricTypeUnspecified",
                                    "memory",
                                    "cpu",
                                    "network",
                                    "graphics",
                                ],
                                typing.List[
                                    typing_extensions.Literal[
                                        "perfMetricTypeUnspecified",
                                        "memory",
                                        "cpu",
                                        "network",
                                        "graphics",
                                    ]
                                ],
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListPerfSampleSeriesResponseHttpRequest: ...
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
                        def samples(self) -> SamplesResource: ...
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
                    def accessibilityClusters(
                        self, *, name: str, locale: str = ..., **kwargs: typing.Any
                    ) -> ListStepAccessibilityClustersResponseHttpRequest: ...
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
                    def perfSampleSeries(self) -> PerfSampleSeriesResource: ...
                    def testCases(self) -> TestCasesResource: ...
                    def thumbnails(self) -> ThumbnailsResource: ...
                    def perfMetricsSummary(self) -> PerfMetricsSummaryResource: ...
                class ClustersResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        **kwargs: typing.Any
                    ) -> ListScreenshotClustersResponseHttpRequest: ...
                    def get(
                        self,
                        *,
                        projectId: str,
                        historyId: str,
                        executionId: str,
                        clusterId: str,
                        **kwargs: typing.Any
                    ) -> ScreenshotClusterHttpRequest: ...
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
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListEnvironmentsResponseHttpRequest: ...
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
                def list(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListExecutionsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    executionId: str,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def create(
                    self,
                    *,
                    projectId: str,
                    historyId: str,
                    body: Execution = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> ExecutionHttpRequest: ...
                def steps(self) -> StepsResource: ...
                def clusters(self) -> ClustersResource: ...
                def environments(self) -> EnvironmentsResource: ...
            def get(
                self, *, projectId: str, historyId: str, **kwargs: typing.Any
            ) -> HistoryHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filterByName: str = ...,
                **kwargs: typing.Any
            ) -> ListHistoriesResponseHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: History = ...,
                requestId: str = ...,
                **kwargs: typing.Any
            ) -> HistoryHttpRequest: ...
            def executions(self) -> ExecutionsResource: ...
        def getSettings(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectSettingsHttpRequest: ...
        def initializeSettings(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> ProjectSettingsHttpRequest: ...
        def histories(self) -> HistoriesResource: ...
    def projects(self) -> ProjectsResource: ...

class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListEnvironmentsResponse: ...

class HistoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> History: ...

class ScreenshotClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ScreenshotCluster: ...

class ListPerfSampleSeriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPerfSampleSeriesResponse: ...

class BatchCreatePerfSamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchCreatePerfSamplesResponse: ...

class ListScreenshotClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListScreenshotClustersResponse: ...

class PerfSampleSeriesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PerfSampleSeries: ...

class ProjectSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProjectSettings: ...

class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Environment: ...

class ListStepsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListStepsResponse: ...

class ListStepThumbnailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListStepThumbnailsResponse: ...

class ExecutionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Execution: ...

class ListTestCasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTestCasesResponse: ...

class ListHistoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHistoriesResponse: ...

class ListPerfSamplesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPerfSamplesResponse: ...

class StepHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Step: ...

class TestCaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestCase: ...

class ListStepAccessibilityClustersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListStepAccessibilityClustersResponse: ...

class ListExecutionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListExecutionsResponse: ...

class PerfMetricsSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PerfMetricsSummary: ...
