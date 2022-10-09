import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ConnectorsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RuntimeActionSchemasResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListRuntimeActionSchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListRuntimeActionSchemasResponseHttpRequest,
                        previous_response: ListRuntimeActionSchemasResponse,
                    ) -> ListRuntimeActionSchemasResponseHttpRequest | None: ...

                @typing.type_check_only
                class RuntimeEntitySchemasResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListRuntimeEntitySchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListRuntimeEntitySchemasResponseHttpRequest,
                        previous_response: ListRuntimeEntitySchemasResponse,
                    ) -> ListRuntimeEntitySchemasResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Connection = ...,
                    connectionId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "CONNECTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ConnectionHttpRequest: ...
                def getConnectionSchemaMetadata(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionSchemaMetadataHttpRequest: ...
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
                    view: typing_extensions.Literal[
                        "CONNECTION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectionsResponseHttpRequest,
                    previous_response: ListConnectionsResponse,
                ) -> ListConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Connection = ...,
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
                def runtimeActionSchemas(self) -> RuntimeActionSchemasResource: ...
                def runtimeEntitySchemas(self) -> RuntimeEntitySchemasResource: ...

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
            class ProvidersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConnectorsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "CONNECTOR_VERSION_VIEW_UNSPECIFIED",
                                "CONNECTOR_VERSION_VIEW_BASIC",
                                "CONNECTOR_VERSION_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ConnectorVersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "CONNECTOR_VERSION_VIEW_UNSPECIFIED",
                                "CONNECTOR_VERSION_VIEW_BASIC",
                                "CONNECTOR_VERSION_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListConnectorVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListConnectorVersionsResponseHttpRequest,
                            previous_response: ListConnectorVersionsResponse,
                        ) -> ListConnectorVersionsResponseHttpRequest | None: ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConnectorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListConnectorsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConnectorsResponseHttpRequest,
                        previous_response: ListConnectorsResponse,
                    ) -> ListConnectorsResponseHttpRequest | None: ...
                    def versions(self) -> VersionsResource: ...

                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProviderHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListProvidersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProvidersResponseHttpRequest,
                    previous_response: ListProvidersResponse,
                ) -> ListProvidersResponseHttpRequest | None: ...
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
                def connectors(self) -> ConnectorsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getRuntimeConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> RuntimeConfigHttpRequest: ...
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
            def connections(self) -> ConnectionsResource: ...
            def operations(self) -> OperationsResource: ...
            def providers(self) -> ProvidersResource: ...

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
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Connection: ...

@typing.type_check_only
class ConnectionSchemaMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectionSchemaMetadata: ...

@typing.type_check_only
class ConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Connector: ...

@typing.type_check_only
class ConnectorVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectorVersion: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListConnectorVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectorVersionsResponse: ...

@typing.type_check_only
class ListConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectorsResponse: ...

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
class ListProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProvidersResponse: ...

@typing.type_check_only
class ListRuntimeActionSchemasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRuntimeActionSchemasResponse: ...

@typing.type_check_only
class ListRuntimeEntitySchemasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRuntimeEntitySchemasResponse: ...

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
class ProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Provider: ...

@typing.type_check_only
class RuntimeConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RuntimeConfig: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...
