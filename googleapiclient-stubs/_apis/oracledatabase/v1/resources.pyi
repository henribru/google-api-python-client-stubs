import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class OracleDatabaseResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AutonomousDatabaseBackupsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutonomousDatabaseBackupsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutonomousDatabaseBackupsResponseHttpRequest,
                    previous_response: ListAutonomousDatabaseBackupsResponse,
                ) -> ListAutonomousDatabaseBackupsResponseHttpRequest | None: ...

            @typing.type_check_only
            class AutonomousDatabaseCharacterSetsResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutonomousDatabaseCharacterSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutonomousDatabaseCharacterSetsResponseHttpRequest,
                    previous_response: ListAutonomousDatabaseCharacterSetsResponse,
                ) -> ListAutonomousDatabaseCharacterSetsResponseHttpRequest | None: ...

            @typing.type_check_only
            class AutonomousDatabasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AutonomousDatabase = ...,
                    autonomousDatabaseId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def failover(
                    self,
                    *,
                    name: str,
                    body: FailoverAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def generateWallet(
                    self,
                    *,
                    name: str,
                    body: GenerateAutonomousDatabaseWalletRequest = ...,
                    **kwargs: typing.Any,
                ) -> GenerateAutonomousDatabaseWalletResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AutonomousDatabaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutonomousDatabasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutonomousDatabasesResponseHttpRequest,
                    previous_response: ListAutonomousDatabasesResponse,
                ) -> ListAutonomousDatabasesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: AutonomousDatabase = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def restart(
                    self,
                    *,
                    name: str,
                    body: RestartAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def restore(
                    self,
                    *,
                    name: str,
                    body: RestoreAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def start(
                    self,
                    *,
                    name: str,
                    body: StartAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: StopAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def switchover(
                    self,
                    *,
                    name: str,
                    body: SwitchoverAutonomousDatabaseRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class AutonomousDbVersionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAutonomousDbVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAutonomousDbVersionsResponseHttpRequest,
                    previous_response: ListAutonomousDbVersionsResponse,
                ) -> ListAutonomousDbVersionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class CloudExadataInfrastructuresResource(
                googleapiclient.discovery.Resource
            ):
                @typing.type_check_only
                class DbServersResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDbServersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDbServersResponseHttpRequest,
                        previous_response: ListDbServersResponse,
                    ) -> ListDbServersResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudExadataInfrastructure = ...,
                    cloudExadataInfrastructureId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudExadataInfrastructureHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCloudExadataInfrastructuresResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCloudExadataInfrastructuresResponseHttpRequest,
                    previous_response: ListCloudExadataInfrastructuresResponse,
                ) -> ListCloudExadataInfrastructuresResponseHttpRequest | None: ...
                def dbServers(self) -> DbServersResource: ...

            @typing.type_check_only
            class CloudVmClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DbNodesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDbNodesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDbNodesResponseHttpRequest,
                        previous_response: ListDbNodesResponse,
                    ) -> ListDbNodesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: CloudVmCluster = ...,
                    cloudVmClusterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    force: bool = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CloudVmClusterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCloudVmClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCloudVmClustersResponseHttpRequest,
                    previous_response: ListCloudVmClustersResponse,
                ) -> ListCloudVmClustersResponseHttpRequest | None: ...
                def dbNodes(self) -> DbNodesResource: ...

            @typing.type_check_only
            class DatabaseCharacterSetsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDatabaseCharacterSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatabaseCharacterSetsResponseHttpRequest,
                    previous_response: ListDatabaseCharacterSetsResponse,
                ) -> ListDatabaseCharacterSetsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DatabasesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatabaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDatabasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatabasesResponseHttpRequest,
                    previous_response: ListDatabasesResponse,
                ) -> ListDatabasesResponseHttpRequest | None: ...

            @typing.type_check_only
            class DbSystemInitialStorageSizesResource(
                googleapiclient.discovery.Resource
            ):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDbSystemInitialStorageSizesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDbSystemInitialStorageSizesResponseHttpRequest,
                    previous_response: ListDbSystemInitialStorageSizesResponse,
                ) -> ListDbSystemInitialStorageSizesResponseHttpRequest | None: ...

            @typing.type_check_only
            class DbSystemShapesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDbSystemShapesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDbSystemShapesResponseHttpRequest,
                    previous_response: ListDbSystemShapesResponse,
                ) -> ListDbSystemShapesResponseHttpRequest | None: ...

            @typing.type_check_only
            class DbSystemsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: DbSystem = ...,
                    dbSystemId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DbSystemHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDbSystemsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDbSystemsResponseHttpRequest,
                    previous_response: ListDbSystemsResponse,
                ) -> ListDbSystemsResponseHttpRequest | None: ...

            @typing.type_check_only
            class DbVersionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDbVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDbVersionsResponseHttpRequest,
                    previous_response: ListDbVersionsResponse,
                ) -> ListDbVersionsResponseHttpRequest | None: ...

            @typing.type_check_only
            class EntitlementsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListEntitlementsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEntitlementsResponseHttpRequest,
                    previous_response: ListEntitlementsResponse,
                ) -> ListEntitlementsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ExadbVmClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DbNodesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDbNodesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDbNodesResponseHttpRequest,
                        previous_response: ListDbNodesResponse,
                    ) -> ListDbNodesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: ExadbVmCluster = ...,
                    exadbVmClusterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ExadbVmClusterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListExadbVmClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListExadbVmClustersResponseHttpRequest,
                    previous_response: ListExadbVmClustersResponse,
                ) -> ListExadbVmClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ExadbVmCluster = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def removeVirtualMachine(
                    self,
                    *,
                    name: str,
                    body: RemoveVirtualMachineExadbVmClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def dbNodes(self) -> DbNodesResource: ...

            @typing.type_check_only
            class ExascaleDbStorageVaultsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ExascaleDbStorageVault = ...,
                    exascaleDbStorageVaultId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ExascaleDbStorageVaultHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListExascaleDbStorageVaultsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListExascaleDbStorageVaultsResponseHttpRequest,
                    previous_response: ListExascaleDbStorageVaultsResponse,
                ) -> ListExascaleDbStorageVaultsResponseHttpRequest | None: ...

            @typing.type_check_only
            class GiVersionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class MinorVersionsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListMinorVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMinorVersionsResponseHttpRequest,
                        previous_response: ListMinorVersionsResponse,
                    ) -> ListMinorVersionsResponseHttpRequest | None: ...

                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListGiVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGiVersionsResponseHttpRequest,
                    previous_response: ListGiVersionsResponse,
                ) -> ListGiVersionsResponseHttpRequest | None: ...
                def minorVersions(self) -> MinorVersionsResource: ...

            @typing.type_check_only
            class OdbNetworksResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OdbSubnetsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: OdbSubnet = ...,
                        odbSubnetId: str = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OdbSubnetHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListOdbSubnetsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOdbSubnetsResponseHttpRequest,
                        previous_response: ListOdbSubnetsResponse,
                    ) -> ListOdbSubnetsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: OdbNetwork = ...,
                    odbNetworkId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OdbNetworkHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOdbNetworksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOdbNetworksResponseHttpRequest,
                    previous_response: ListOdbNetworksResponse,
                ) -> ListOdbNetworksResponseHttpRequest | None: ...
                def odbSubnets(self) -> OdbSubnetsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
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
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class PluggableDatabasesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PluggableDatabaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPluggableDatabasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPluggableDatabasesResponseHttpRequest,
                    previous_response: ListPluggableDatabasesResponse,
                ) -> ListPluggableDatabasesResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def autonomousDatabaseBackups(
                self,
            ) -> AutonomousDatabaseBackupsResource: ...
            def autonomousDatabaseCharacterSets(
                self,
            ) -> AutonomousDatabaseCharacterSetsResource: ...
            def autonomousDatabases(self) -> AutonomousDatabasesResource: ...
            def autonomousDbVersions(self) -> AutonomousDbVersionsResource: ...
            def cloudExadataInfrastructures(
                self,
            ) -> CloudExadataInfrastructuresResource: ...
            def cloudVmClusters(self) -> CloudVmClustersResource: ...
            def databaseCharacterSets(self) -> DatabaseCharacterSetsResource: ...
            def databases(self) -> DatabasesResource: ...
            def dbSystemInitialStorageSizes(
                self,
            ) -> DbSystemInitialStorageSizesResource: ...
            def dbSystemShapes(self) -> DbSystemShapesResource: ...
            def dbSystems(self) -> DbSystemsResource: ...
            def dbVersions(self) -> DbVersionsResource: ...
            def entitlements(self) -> EntitlementsResource: ...
            def exadbVmClusters(self) -> ExadbVmClustersResource: ...
            def exascaleDbStorageVaults(self) -> ExascaleDbStorageVaultsResource: ...
            def giVersions(self) -> GiVersionsResource: ...
            def odbNetworks(self) -> OdbNetworksResource: ...
            def operations(self) -> OperationsResource: ...
            def pluggableDatabases(self) -> PluggableDatabasesResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AutonomousDatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutonomousDatabase: ...

@typing.type_check_only
class CloudExadataInfrastructureHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CloudExadataInfrastructure: ...

@typing.type_check_only
class CloudVmClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CloudVmCluster: ...

@typing.type_check_only
class DatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Database: ...

@typing.type_check_only
class DbSystemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DbSystem: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ExadbVmClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExadbVmCluster: ...

@typing.type_check_only
class ExascaleDbStorageVaultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExascaleDbStorageVault: ...

@typing.type_check_only
class GenerateAutonomousDatabaseWalletResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateAutonomousDatabaseWalletResponse: ...

@typing.type_check_only
class ListAutonomousDatabaseBackupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutonomousDatabaseBackupsResponse: ...

@typing.type_check_only
class ListAutonomousDatabaseCharacterSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutonomousDatabaseCharacterSetsResponse: ...

@typing.type_check_only
class ListAutonomousDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutonomousDatabasesResponse: ...

@typing.type_check_only
class ListAutonomousDbVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAutonomousDbVersionsResponse: ...

@typing.type_check_only
class ListCloudExadataInfrastructuresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCloudExadataInfrastructuresResponse: ...

@typing.type_check_only
class ListCloudVmClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCloudVmClustersResponse: ...

@typing.type_check_only
class ListDatabaseCharacterSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabaseCharacterSetsResponse: ...

@typing.type_check_only
class ListDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDatabasesResponse: ...

@typing.type_check_only
class ListDbNodesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbNodesResponse: ...

@typing.type_check_only
class ListDbServersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbServersResponse: ...

@typing.type_check_only
class ListDbSystemInitialStorageSizesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbSystemInitialStorageSizesResponse: ...

@typing.type_check_only
class ListDbSystemShapesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbSystemShapesResponse: ...

@typing.type_check_only
class ListDbSystemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbSystemsResponse: ...

@typing.type_check_only
class ListDbVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbVersionsResponse: ...

@typing.type_check_only
class ListEntitlementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEntitlementsResponse: ...

@typing.type_check_only
class ListExadbVmClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExadbVmClustersResponse: ...

@typing.type_check_only
class ListExascaleDbStorageVaultsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExascaleDbStorageVaultsResponse: ...

@typing.type_check_only
class ListGiVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGiVersionsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMinorVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMinorVersionsResponse: ...

@typing.type_check_only
class ListOdbNetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOdbNetworksResponse: ...

@typing.type_check_only
class ListOdbSubnetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOdbSubnetsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPluggableDatabasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPluggableDatabasesResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OdbNetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OdbNetwork: ...

@typing.type_check_only
class OdbSubnetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OdbSubnet: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PluggableDatabaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PluggableDatabase: ...
