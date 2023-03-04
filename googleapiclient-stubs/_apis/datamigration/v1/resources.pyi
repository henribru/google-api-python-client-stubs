import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DatabaseMigrationServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ConnectionProfilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ConnectionProfile = ...,
                    connectionProfileId: str = ...,
                    requestId: str = ...,
                    skipValidation: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionProfileHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListConnectionProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectionProfilesResponseHttpRequest,
                    previous_response: ListConnectionProfilesResponse,
                ) -> ListConnectionProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ConnectionProfile = ...,
                    requestId: str = ...,
                    skipValidation: bool = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ConversionWorkspacesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MappingRulesResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: ImportMappingRulesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def apply(
                    self,
                    *,
                    name: str,
                    body: ApplyConversionWorkspaceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def commit(
                    self,
                    *,
                    name: str,
                    body: CommitConversionWorkspaceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def convert(
                    self,
                    *,
                    name: str,
                    body: ConvertConversionWorkspaceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: ConversionWorkspace = ...,
                    conversionWorkspaceId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def describeConversionWorkspaceRevisions(
                    self,
                    *,
                    conversionWorkspace: str,
                    commitId: str = ...,
                    **kwargs: typing.Any
                ) -> DescribeConversionWorkspaceRevisionsResponseHttpRequest: ...
                def describeDatabaseEntities(
                    self,
                    *,
                    conversionWorkspace: str,
                    commitId: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    tree: typing_extensions.Literal[
                        "DB_TREE_TYPE_UNSPECIFIED",
                        "SOURCE_TREE",
                        "DRAFT_TREE",
                        "DESTINATION_TREE",
                    ] = ...,
                    uncommitted: bool = ...,
                    **kwargs: typing.Any
                ) -> DescribeDatabaseEntitiesResponseHttpRequest: ...
                def describeDatabaseEntities_next(
                    self,
                    previous_request: DescribeDatabaseEntitiesResponseHttpRequest,
                    previous_response: DescribeDatabaseEntitiesResponse,
                ) -> DescribeDatabaseEntitiesResponseHttpRequest | None: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConversionWorkspaceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListConversionWorkspacesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConversionWorkspacesResponseHttpRequest,
                    previous_response: ListConversionWorkspacesResponse,
                ) -> ListConversionWorkspacesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ConversionWorkspace = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def rollback(
                    self,
                    *,
                    name: str,
                    body: RollbackConversionWorkspaceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def searchBackgroundJobs(
                    self,
                    *,
                    conversionWorkspace: str,
                    completedUntilTime: str = ...,
                    maxSize: int = ...,
                    returnMostRecentPerJobType: bool = ...,
                    **kwargs: typing.Any
                ) -> SearchBackgroundJobsResponseHttpRequest: ...
                def seed(
                    self,
                    *,
                    name: str,
                    body: SeedConversionWorkspaceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def mappingRules(self) -> MappingRulesResource: ...

            @typing.type_check_only
            class MigrationJobsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: MigrationJob = ...,
                    migrationJobId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def generateSshScript(
                    self,
                    *,
                    migrationJob: str,
                    body: GenerateSshScriptRequest = ...,
                    **kwargs: typing.Any
                ) -> SshScriptHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> MigrationJobHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListMigrationJobsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListMigrationJobsResponseHttpRequest,
                    previous_response: ListMigrationJobsResponse,
                ) -> ListMigrationJobsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: MigrationJob = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def promote(
                    self,
                    *,
                    name: str,
                    body: PromoteMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def restart(
                    self,
                    *,
                    name: str,
                    body: RestartMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def resume(
                    self,
                    *,
                    name: str,
                    body: ResumeMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def verify(
                    self,
                    *,
                    name: str,
                    body: VerifyMigrationJobRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PrivateConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: PrivateConnection = ...,
                    privateConnectionId: str = ...,
                    requestId: str = ...,
                    skipValidation: bool = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PrivateConnectionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListPrivateConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPrivateConnectionsResponseHttpRequest,
                    previous_response: ListPrivateConnectionsResponse,
                ) -> ListPrivateConnectionsResponseHttpRequest | None: ...

            def fetchStaticIps(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> FetchStaticIpsResponseHttpRequest: ...
            def fetchStaticIps_next(
                self,
                previous_request: FetchStaticIpsResponseHttpRequest,
                previous_response: FetchStaticIpsResponse,
            ) -> FetchStaticIpsResponseHttpRequest | None: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def connectionProfiles(self) -> ConnectionProfilesResource: ...
            def conversionWorkspaces(self) -> ConversionWorkspacesResource: ...
            def migrationJobs(self) -> MigrationJobsResource: ...
            def operations(self) -> OperationsResource: ...
            def privateConnections(self) -> PrivateConnectionsResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ConnectionProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectionProfile: ...

@typing.type_check_only
class ConversionWorkspaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConversionWorkspace: ...

@typing.type_check_only
class DescribeConversionWorkspaceRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DescribeConversionWorkspaceRevisionsResponse: ...

@typing.type_check_only
class DescribeDatabaseEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DescribeDatabaseEntitiesResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FetchStaticIpsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FetchStaticIpsResponse: ...

@typing.type_check_only
class ListConnectionProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionProfilesResponse: ...

@typing.type_check_only
class ListConversionWorkspacesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConversionWorkspacesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMigrationJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMigrationJobsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPrivateConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPrivateConnectionsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MigrationJobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MigrationJob: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class PrivateConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PrivateConnection: ...

@typing.type_check_only
class SearchBackgroundJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchBackgroundJobsResponse: ...

@typing.type_check_only
class SshScriptHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SshScript: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
