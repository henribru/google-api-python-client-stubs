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
                def restore(
                    self,
                    *,
                    name: str,
                    body: RestoreAutonomousDatabaseRequest = ...,
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
            class DbSystemShapesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
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
            class GiVersionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListGiVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListGiVersionsResponseHttpRequest,
                    previous_response: ListGiVersionsResponse,
                ) -> ListGiVersionsResponseHttpRequest | None: ...

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
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

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
            def dbSystemShapes(self) -> DbSystemShapesResource: ...
            def entitlements(self) -> EntitlementsResource: ...
            def giVersions(self) -> GiVersionsResource: ...
            def operations(self) -> OperationsResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

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
class ListDbSystemShapesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDbSystemShapesResponse: ...

@typing.type_check_only
class ListEntitlementsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEntitlementsResponse: ...

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
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...
