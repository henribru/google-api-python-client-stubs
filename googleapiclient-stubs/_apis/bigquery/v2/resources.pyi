import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BigqueryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DatasetsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            projectId: str,
            datasetId: str,
            deleteContents: bool = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            datasetId: str,
            accessPolicyVersion: int = ...,
            datasetView: typing_extensions.Literal[
                "DATASET_VIEW_UNSPECIFIED", "METADATA", "ACL", "FULL"
            ] = ...,
            **kwargs: typing.Any,
        ) -> DatasetHttpRequest: ...
        def insert(
            self,
            *,
            projectId: str,
            body: Dataset = ...,
            accessPolicyVersion: int = ...,
            **kwargs: typing.Any,
        ) -> DatasetHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            all: bool = ...,
            filter: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> DatasetListHttpRequest: ...
        def list_next(
            self,
            previous_request: DatasetListHttpRequest,
            previous_response: DatasetList,
        ) -> DatasetListHttpRequest | None: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Dataset = ...,
            accessPolicyVersion: int = ...,
            **kwargs: typing.Any,
        ) -> DatasetHttpRequest: ...
        def undelete(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: UndeleteDatasetRequest = ...,
            **kwargs: typing.Any,
        ) -> DatasetHttpRequest: ...
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Dataset = ...,
            accessPolicyVersion: int = ...,
            **kwargs: typing.Any,
        ) -> DatasetHttpRequest: ...

    @typing.type_check_only
    class JobsResource(googleapiclient.discovery.Resource):
        def cancel(
            self,
            *,
            projectId: str,
            jobId: str,
            location: str = ...,
            **kwargs: typing.Any,
        ) -> JobCancelResponseHttpRequest: ...
        def delete(
            self,
            *,
            projectId: str,
            jobId: str,
            location: str = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            jobId: str,
            location: str = ...,
            **kwargs: typing.Any,
        ) -> JobHttpRequest: ...
        def getQueryResults(
            self,
            *,
            projectId: str,
            jobId: str,
            formatOptions_useInt64Timestamp: bool = ...,
            location: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            startIndex: str = ...,
            timeoutMs: int = ...,
            **kwargs: typing.Any,
        ) -> GetQueryResultsResponseHttpRequest: ...
        def getQueryResults_next(
            self,
            previous_request: GetQueryResultsResponseHttpRequest,
            previous_response: GetQueryResultsResponse,
        ) -> GetQueryResultsResponseHttpRequest | None: ...
        def insert(
            self, *, projectId: str, body: Job = ..., **kwargs: typing.Any
        ) -> JobHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            allUsers: bool = ...,
            maxCreationTime: str = ...,
            maxResults: int = ...,
            minCreationTime: str = ...,
            pageToken: str = ...,
            parentJobId: str = ...,
            projection: typing_extensions.Literal["full", "minimal"] = ...,
            stateFilter: typing_extensions.Literal["done", "pending", "running"]
            | _list[typing_extensions.Literal["done", "pending", "running"]] = ...,
            **kwargs: typing.Any,
        ) -> JobListHttpRequest: ...
        def list_next(
            self, previous_request: JobListHttpRequest, previous_response: JobList
        ) -> JobListHttpRequest | None: ...
        def query(
            self, *, projectId: str, body: QueryRequest = ..., **kwargs: typing.Any
        ) -> QueryResponseHttpRequest: ...

    @typing.type_check_only
    class ModelsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, projectId: str, datasetId: str, modelId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, projectId: str, datasetId: str, modelId: str, **kwargs: typing.Any
        ) -> ModelHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListModelsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListModelsResponseHttpRequest,
            previous_response: ListModelsResponse,
        ) -> ListModelsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            modelId: str,
            body: Model = ...,
            **kwargs: typing.Any,
        ) -> ModelHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def getServiceAccount(
            self, *, projectId: str, **kwargs: typing.Any
        ) -> GetServiceAccountResponseHttpRequest: ...
        def list(
            self, *, maxResults: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ProjectListHttpRequest: ...
        def list_next(
            self,
            previous_request: ProjectListHttpRequest,
            previous_response: ProjectList,
        ) -> ProjectListHttpRequest | None: ...

    @typing.type_check_only
    class RoutinesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            readMask: str = ...,
            **kwargs: typing.Any,
        ) -> RoutineHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Routine = ...,
            **kwargs: typing.Any,
        ) -> RoutineHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            filter: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            readMask: str = ...,
            **kwargs: typing.Any,
        ) -> ListRoutinesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListRoutinesResponseHttpRequest,
            previous_response: ListRoutinesResponse,
        ) -> ListRoutinesResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            routineId: str,
            body: Routine = ...,
            **kwargs: typing.Any,
        ) -> RoutineHttpRequest: ...

    @typing.type_check_only
    class RowAccessPoliciesResource(googleapiclient.discovery.Resource):
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListRowAccessPoliciesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListRowAccessPoliciesResponseHttpRequest,
            previous_response: ListRowAccessPoliciesResponse,
        ) -> ListRowAccessPoliciesResponseHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class TabledataResource(googleapiclient.discovery.Resource):
        def insertAll(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: TableDataInsertAllRequest = ...,
            **kwargs: typing.Any,
        ) -> TableDataInsertAllResponseHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            formatOptions_useInt64Timestamp: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            selectedFields: str = ...,
            startIndex: str = ...,
            **kwargs: typing.Any,
        ) -> TableDataListHttpRequest: ...
        def list_next(
            self,
            previous_request: TableDataListHttpRequest,
            previous_response: TableDataList,
        ) -> TableDataListHttpRequest | None: ...

    @typing.type_check_only
    class TablesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, projectId: str, datasetId: str, tableId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            selectedFields: str = ...,
            view: typing_extensions.Literal[
                "TABLE_METADATA_VIEW_UNSPECIFIED", "BASIC", "STORAGE_STATS", "FULL"
            ] = ...,
            **kwargs: typing.Any,
        ) -> TableHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            projectId: str,
            datasetId: str,
            body: Table = ...,
            **kwargs: typing.Any,
        ) -> TableHttpRequest: ...
        def list(
            self,
            *,
            projectId: str,
            datasetId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> TableListHttpRequest: ...
        def list_next(
            self, previous_request: TableListHttpRequest, previous_response: TableList
        ) -> TableListHttpRequest | None: ...
        def patch(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: Table = ...,
            autodetect_schema: bool = ...,
            **kwargs: typing.Any,
        ) -> TableHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            projectId: str,
            datasetId: str,
            tableId: str,
            body: Table = ...,
            autodetect_schema: bool = ...,
            **kwargs: typing.Any,
        ) -> TableHttpRequest: ...

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
    def jobs(self) -> JobsResource: ...
    def models(self) -> ModelsResource: ...
    def projects(self) -> ProjectsResource: ...
    def routines(self) -> RoutinesResource: ...
    def rowAccessPolicies(self) -> RowAccessPoliciesResource: ...
    def tabledata(self) -> TabledataResource: ...
    def tables(self) -> TablesResource: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Dataset: ...

@typing.type_check_only
class DatasetListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatasetList: ...

@typing.type_check_only
class GetQueryResultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetQueryResultsResponse: ...

@typing.type_check_only
class GetServiceAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetServiceAccountResponse: ...

@typing.type_check_only
class JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Job: ...

@typing.type_check_only
class JobCancelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> JobCancelResponse: ...

@typing.type_check_only
class JobListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> JobList: ...

@typing.type_check_only
class ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListModelsResponse: ...

@typing.type_check_only
class ListRoutinesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRoutinesResponse: ...

@typing.type_check_only
class ListRowAccessPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRowAccessPoliciesResponse: ...

@typing.type_check_only
class ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Model: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ProjectListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProjectList: ...

@typing.type_check_only
class QueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryResponse: ...

@typing.type_check_only
class RoutineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Routine: ...

@typing.type_check_only
class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Table: ...

@typing.type_check_only
class TableDataInsertAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TableDataInsertAllResponse: ...

@typing.type_check_only
class TableDataListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TableDataList: ...

@typing.type_check_only
class TableListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TableList: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...
