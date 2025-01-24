import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                class ConnectionSchemaMetadataResource(
                    googleapiclient.discovery.Resource
                ):
                    def getAction(
                        self, *, name: str, actionId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def getEntityType(
                        self, *, name: str, entityId: str = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def listActions(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListActionsResponseHttpRequest: ...
                    def listActions_next(
                        self,
                        previous_request: ListActionsResponseHttpRequest,
                        previous_response: ListActionsResponse,
                    ) -> ListActionsResponseHttpRequest | None: ...
                    def listEntityTypes(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "VIEW_UNSPECIFIED", "BASIC"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListEntityTypesResponseHttpRequest: ...
                    def listEntityTypes_next(
                        self,
                        previous_request: ListEntityTypesResponseHttpRequest,
                        previous_response: ListEntityTypesResponse,
                    ) -> ListEntityTypesResponseHttpRequest | None: ...
                    def refresh(
                        self,
                        *,
                        name: str,
                        body: RefreshConnectionSchemaMetadataRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class EventSubscriptionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: EventSubscription = ...,
                        eventSubscriptionId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EventSubscriptionHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListEventSubscriptionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListEventSubscriptionsResponseHttpRequest,
                        previous_response: ListEventSubscriptionsResponse,
                    ) -> ListEventSubscriptionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: EventSubscription = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def retry(
                        self,
                        *,
                        name: str,
                        body: RetryEventSubscriptionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class RuntimeActionSchemasResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        schemaAsString: bool = ...,
                        **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ConnectionHttpRequest: ...
                def getConnectionSchemaMetadata(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionSchemaMetadataHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ListConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectionsResponseHttpRequest,
                    previous_response: ListConnectionsResponse,
                ) -> ListConnectionsResponseHttpRequest | None: ...
                def listenEvent(
                    self,
                    *,
                    resourcePath: str,
                    body: ListenEventRequest = ...,
                    **kwargs: typing.Any,
                ) -> ListenEventResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Connection = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def repairEventing(
                    self,
                    *,
                    name: str,
                    body: RepairEventingRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def search(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any,
                ) -> SearchConnectionsResponseHttpRequest: ...
                def search_next(
                    self,
                    previous_request: SearchConnectionsResponseHttpRequest,
                    previous_response: SearchConnectionsResponse,
                ) -> SearchConnectionsResponseHttpRequest | None: ...
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
                def connectionSchemaMetadata(
                    self,
                ) -> ConnectionSchemaMetadataResource: ...
                def eventSubscriptions(self) -> EventSubscriptionsResource: ...
                def runtimeActionSchemas(self) -> RuntimeActionSchemasResource: ...
                def runtimeEntitySchemas(self) -> RuntimeEntitySchemasResource: ...

            @typing.type_check_only
            class CustomConnectorsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CustomConnectorVersionsResource(
                    googleapiclient.discovery.Resource
                ):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def deprecate(
                        self,
                        *,
                        name: str,
                        body: DeprecateCustomConnectorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def publish(
                        self,
                        *,
                        name: str,
                        body: PublishCustomConnectorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def withdraw(
                        self,
                        *,
                        name: str,
                        body: WithdrawCustomConnectorVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def validateCustomConnectorSpec(
                    self,
                    *,
                    parent: str,
                    body: ValidateCustomConnectorSpecRequest = ...,
                    **kwargs: typing.Any,
                ) -> ValidateCustomConnectorSpecResponseHttpRequest: ...
                def customConnectorVersions(
                    self,
                ) -> CustomConnectorVersionsResource: ...

            @typing.type_check_only
            class EndpointAttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: EndpointAttachment = ...,
                    endpointAttachmentId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "ENDPOINT_ATTACHMENT_VIEW_UNSPECIFIED",
                        "ENDPOINT_ATTACHMENT_VIEW_BASIC",
                        "ENDPOINT_ATTACHMENT_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> EndpointAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "ENDPOINT_ATTACHMENT_VIEW_UNSPECIFIED",
                        "ENDPOINT_ATTACHMENT_VIEW_BASIC",
                        "ENDPOINT_ATTACHMENT_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListEndpointAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEndpointAttachmentsResponseHttpRequest,
                    previous_response: ListEndpointAttachmentsResponse,
                ) -> ListEndpointAttachmentsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: EndpointAttachment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CustomConnectorsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class CustomConnectorVersionsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CustomConnectorVersion = ...,
                            customConnectorVersionId: str = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> CustomConnectorVersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListCustomConnectorVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListCustomConnectorVersionsResponseHttpRequest,
                            previous_response: ListCustomConnectorVersionsResponse,
                        ) -> ListCustomConnectorVersionsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: CustomConnector = ...,
                        customConnectorId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> CustomConnectorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListCustomConnectorsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListCustomConnectorsResponseHttpRequest,
                        previous_response: ListCustomConnectorsResponse,
                    ) -> ListCustomConnectorsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: CustomConnector = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def customConnectorVersions(
                        self,
                    ) -> CustomConnectorVersionsResource: ...

                @typing.type_check_only
                class ManagedZonesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ManagedZone = ...,
                        managedZoneId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ManagedZoneHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListManagedZonesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListManagedZonesResponseHttpRequest,
                        previous_response: ListManagedZonesResponse,
                    ) -> ListManagedZonesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ManagedZone = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...

                def getSettings(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SettingsHttpRequest: ...
                def updateSettings(
                    self,
                    *,
                    name: str,
                    body: Settings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def customConnectors(self) -> CustomConnectorsResource: ...
                def managedZones(self) -> ManagedZonesResource: ...

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

            @typing.type_check_only
            class ProvidersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConnectorsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class EventtypesResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> EventTypeHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> ListEventTypesResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: ListEventTypesResponseHttpRequest,
                                previous_response: ListEventTypesResponse,
                            ) -> ListEventTypesResponseHttpRequest | None: ...

                        def fetchAuthSchema(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "AUTH_SCHEMA_VIEW_UNSPECIFIED", "BASIC", "JSON_SCHEMA"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> FetchAuthSchemaResponseHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "CONNECTOR_VERSION_VIEW_UNSPECIFIED",
                                "CONNECTOR_VERSION_VIEW_BASIC",
                                "CONNECTOR_VERSION_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any,
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
                            **kwargs: typing.Any,
                        ) -> ListConnectorVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListConnectorVersionsResponseHttpRequest,
                            previous_response: ListConnectorVersionsResponse,
                        ) -> ListConnectorVersionsResponseHttpRequest | None: ...
                        def eventtypes(self) -> EventtypesResource: ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConnectorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def connectors(self) -> ConnectorsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getRegionalSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> RegionalSettingsHttpRequest: ...
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
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def updateRegionalSettings(
                self,
                *,
                name: str,
                body: RegionalSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def connections(self) -> ConnectionsResource: ...
            def customConnectors(self) -> CustomConnectorsResource: ...
            def endpointAttachments(self) -> EndpointAttachmentsResource: ...
            def global_(self) -> GlobalResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connection: ...

@typing.type_check_only
class ConnectionSchemaMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConnectionSchemaMetadata: ...

@typing.type_check_only
class ConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connector: ...

@typing.type_check_only
class ConnectorVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConnectorVersion: ...

@typing.type_check_only
class CustomConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomConnector: ...

@typing.type_check_only
class CustomConnectorVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomConnectorVersion: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EndpointAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EndpointAttachment: ...

@typing.type_check_only
class EventSubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventSubscription: ...

@typing.type_check_only
class EventTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventType: ...

@typing.type_check_only
class FetchAuthSchemaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchAuthSchemaResponse: ...

@typing.type_check_only
class ListActionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListActionsResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListConnectorVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectorVersionsResponse: ...

@typing.type_check_only
class ListConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectorsResponse: ...

@typing.type_check_only
class ListCustomConnectorVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomConnectorVersionsResponse: ...

@typing.type_check_only
class ListCustomConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomConnectorsResponse: ...

@typing.type_check_only
class ListEndpointAttachmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEndpointAttachmentsResponse: ...

@typing.type_check_only
class ListEntityTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEntityTypesResponse: ...

@typing.type_check_only
class ListEventSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEventSubscriptionsResponse: ...

@typing.type_check_only
class ListEventTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEventTypesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListManagedZonesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListManagedZonesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProvidersResponse: ...

@typing.type_check_only
class ListRuntimeActionSchemasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimeActionSchemasResponse: ...

@typing.type_check_only
class ListRuntimeEntitySchemasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimeEntitySchemasResponse: ...

@typing.type_check_only
class ListenEventResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListenEventResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class ManagedZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManagedZone: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Provider: ...

@typing.type_check_only
class RegionalSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RegionalSettings: ...

@typing.type_check_only
class RuntimeConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RuntimeConfig: ...

@typing.type_check_only
class SearchConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchConnectionsResponse: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Settings: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class ValidateCustomConnectorSpecResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ValidateCustomConnectorSpecResponse: ...
