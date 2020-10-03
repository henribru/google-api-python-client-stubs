import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BigqueryResource(googleapiclient.discovery.Resource):
    class DatasetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            projectId: str,
            maxResults: int = ...,
            filter: str = ...,
            all: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DatasetListHttpRequest: ...
        def get(
            self, *, projectId: str, datasetId: str, **kwargs: typing.Any
        ) -> DatasetHttpRequest: ...
        def delete(
            self,
            *,
            projectId: str,
            datasetId: str,
            deleteContents: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self, *, projectId: str, body: Dataset = ..., **kwargs: typing.Any
        ) -> DatasetHttpRequest: ...
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Dataset = ...,
            **kwargs: typing.Any
        ) -> DatasetHttpRequest: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Dataset = ...,
            **kwargs: typing.Any
        ) -> DatasetHttpRequest: ...
    class JobsResource(googleapiclient.discovery.Resource):
        def query(
            self, *, projectId: str, body: QueryRequest = ..., **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            jobId: str,
            location: str = ...,
            **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            maxResults: int = ...,
            allUsers: bool = ...,
            maxCreationTime: str = ...,
            minCreationTime: str = ...,
            parentJobId: str = ...,
            projection: typing_extensions.Literal["full", "minimal"] = ...,
            stateFilter: typing.Union[
                typing_extensions.Literal["done", "pending", "running"],
                typing.List[typing_extensions.Literal["done", "pending", "running"]],
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> JobListHttpRequest: ...
        def insert(
            self, *, projectId: str, body: Job = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def getQueryResults(
            self,
            *,
            projectId: str,
            jobId: str,
            startIndex: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            location: str = ...,
            timeoutMs: int = ...,
            **kwargs: typing.Any
        ) -> GetQueryResultsResponseHttpRequest: ...
        def cancel(
            self,
            *,
            projectId: str,
            jobId: str,
            location: str = ...,
            **kwargs: typing.Any
        ) -> JobCancelResponseHttpRequest: ...
    class TablesResource(googleapiclient.discovery.Resource):
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: Table = ...,
            **kwargs: typing.Any
        ) -> TableHttpRequest: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: Table = ...,
            **kwargs: typing.Any
        ) -> TableHttpRequest: ...
        def insert(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Table = ...,
            **kwargs: typing.Any
        ) -> TableHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            selectedFields: str = ...,
            **kwargs: typing.Any
        ) -> TableHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def delete(
            self, *, projectId: str, datasetId: str, tableId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TableListHttpRequest: ...
    class ModelsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, projectId: str, datasetId: str, modelId: str, **kwargs: typing.Any
        ) -> ModelHttpRequest: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            modelId: str,
            body: Model = ...,
            **kwargs: typing.Any
        ) -> ModelHttpRequest: ...
        def delete(
            self, *, projectId: str, datasetId: str, modelId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ListModelsResponseHttpRequest: ...
    class RoutinesResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            body: Routine = ...,
            **kwargs: typing.Any
        ) -> RoutineHttpRequest: ...
        def delete(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            readMask: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListRoutinesResponseHttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            readMask: str = ...,
            **kwargs: typing.Any
        ) -> RoutineHttpRequest: ...
        def insert(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Routine = ...,
            **kwargs: typing.Any
        ) -> RoutineHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageToken: str = ..., maxResults: int = ..., **kwargs: typing.Any
        ) -> ProjectListHttpRequest: ...
        def getServiceAccount(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> GetServiceAccountResponseHttpRequest: ...
    class TabledataResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            pageToken: str = ...,
            startIndex: str = ...,
            selectedFields: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> TableDataListHttpRequest: ...
        def insertAll(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: TableDataInsertAllRequest = ...,
            **kwargs: typing.Any
        ) -> TableDataInsertAllResponseHttpRequest: ...
    def datasets(self) -> DatasetsResource: ...
    def jobs(self) -> JobsResource: ...
    def tables(self) -> TablesResource: ...
    def models(self) -> ModelsResource: ...
    def routines(self) -> RoutinesResource: ...
    def projects(self) -> ProjectsResource: ...
    def tabledata(self) -> TabledataResource: ...

class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Job: ...

class JobCancelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> JobCancelResponse: ...

class ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListModelsResponse: ...

class JobListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> JobList: ...

class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> QueryResponse: ...

class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Dataset: ...

class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Table: ...

class RoutineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Routine: ...

class ProjectListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProjectList: ...

class ListRoutinesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRoutinesResponse: ...

class GetQueryResultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetQueryResultsResponse: ...

class TableDataListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TableDataList: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Model: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class TableListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TableList: ...

class TableDataInsertAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TableDataInsertAllResponse: ...

class GetServiceAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetServiceAccountResponse: ...

class DatasetListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatasetList: ...
