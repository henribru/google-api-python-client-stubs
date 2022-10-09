import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BigtableAdminResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
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

            def operations(self) -> OperationsResource: ...

        def cancel(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def projects(self) -> ProjectsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppProfilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AppProfile = ...,
                    appProfileId: str = ...,
                    ignoreWarnings: bool = ...,
                    **kwargs: typing.Any
                ) -> AppProfileHttpRequest: ...
                def delete(
                    self, *, name: str, ignoreWarnings: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AppProfileHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAppProfilesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAppProfilesResponseHttpRequest,
                    previous_response: ListAppProfilesResponse,
                ) -> ListAppProfilesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AppProfile = ...,
                    ignoreWarnings: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BackupsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Backup = ...,
                        backupId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BackupHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
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
                    ) -> ListBackupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListBackupsResponseHttpRequest,
                        previous_response: ListBackupsResponse,
                    ) -> ListBackupsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Backup = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> BackupHttpRequest: ...
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
                class HotTabletsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        endTime: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        startTime: str = ...,
                        **kwargs: typing.Any
                    ) -> ListHotTabletsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListHotTabletsResponseHttpRequest,
                        previous_response: ListHotTabletsResponse,
                    ) -> ListHotTabletsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Cluster = ...,
                    clusterId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def list(
                    self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClustersResponseHttpRequest,
                    previous_response: ListClustersResponse,
                ) -> ListClustersResponseHttpRequest | None: ...
                def partialUpdateCluster(
                    self,
                    *,
                    name: str,
                    body: Cluster = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def update(
                    self, *, name: str, body: Cluster = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def backups(self) -> BackupsResource: ...
                def hotTablets(self) -> HotTabletsResource: ...

            @typing.type_check_only
            class TablesResource(googleapiclient.discovery.Resource):
                def checkConsistency(
                    self,
                    *,
                    name: str,
                    body: CheckConsistencyRequest = ...,
                    **kwargs: typing.Any
                ) -> CheckConsistencyResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateTableRequest = ...,
                    **kwargs: typing.Any
                ) -> TableHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def dropRowRange(
                    self,
                    *,
                    name: str,
                    body: DropRowRangeRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def generateConsistencyToken(
                    self,
                    *,
                    name: str,
                    body: GenerateConsistencyTokenRequest = ...,
                    **kwargs: typing.Any
                ) -> GenerateConsistencyTokenResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "VIEW_UNSPECIFIED",
                        "NAME_ONLY",
                        "SCHEMA_VIEW",
                        "REPLICATION_VIEW",
                        "ENCRYPTION_VIEW",
                        "FULL",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> TableHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "VIEW_UNSPECIFIED",
                        "NAME_ONLY",
                        "SCHEMA_VIEW",
                        "REPLICATION_VIEW",
                        "ENCRYPTION_VIEW",
                        "FULL",
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListTablesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTablesResponseHttpRequest,
                    previous_response: ListTablesResponse,
                ) -> ListTablesResponseHttpRequest | None: ...
                def modifyColumnFamilies(
                    self,
                    *,
                    name: str,
                    body: ModifyColumnFamiliesRequest = ...,
                    **kwargs: typing.Any
                ) -> TableHttpRequest: ...
                def restore(
                    self,
                    *,
                    parent: str,
                    body: RestoreTableRequest = ...,
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
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteTableRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: CreateInstanceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> InstanceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self, *, parent: str, pageToken: str = ..., **kwargs: typing.Any
            ) -> ListInstancesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInstancesResponseHttpRequest,
                previous_response: ListInstancesResponse,
            ) -> ListInstancesResponseHttpRequest | None: ...
            def partialUpdateInstance(
                self,
                *,
                name: str,
                body: Instance = ...,
                updateMask: str = ...,
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
            def update(
                self, *, name: str, body: Instance = ..., **kwargs: typing.Any
            ) -> InstanceHttpRequest: ...
            def appProfiles(self) -> AppProfilesResource: ...
            def clusters(self) -> ClustersResource: ...
            def tables(self) -> TablesResource: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
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

        def instances(self) -> InstancesResource: ...
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
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AppProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppProfile: ...

@typing.type_check_only
class BackupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Backup: ...

@typing.type_check_only
class CheckConsistencyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckConsistencyResponse: ...

@typing.type_check_only
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Cluster: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GenerateConsistencyTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GenerateConsistencyTokenResponse: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Instance: ...

@typing.type_check_only
class ListAppProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAppProfilesResponse: ...

@typing.type_check_only
class ListBackupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBackupsResponse: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListHotTabletsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListHotTabletsResponse: ...

@typing.type_check_only
class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListInstancesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListTablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTablesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

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
class TableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Table: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
