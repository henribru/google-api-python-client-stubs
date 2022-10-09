import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BeyondCorpResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class InsightsResource(googleapiclient.discovery.Resource):
                def configuredInsight(
                    self,
                    *,
                    insight: str,
                    aggregation: typing_extensions.Literal[
                        "AGGREGATION_UNSPECIFIED",
                        "HOURLY",
                        "DAILY",
                        "WEEKLY",
                        "MONTHLY",
                        "CUSTOM_DATE_RANGE",
                    ] = ...,
                    customGrouping_fieldFilter: str = ...,
                    customGrouping_groupFields: str | _list[str] = ...,
                    endTime: str = ...,
                    fieldFilter: str = ...,
                    group: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    startTime: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest: ...
                def configuredInsight_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest | None: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest | None: ...

            def insights(self) -> InsightsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection = ...,
                    appConnectionId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolve(
                    self,
                    *,
                    parent: str,
                    appConnectorId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest: ...
                def resolve_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class AppConnectorsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector = ...,
                    appConnectorId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse,
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    appConnector: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolveInstanceConfig(
                    self, *, appConnector: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class AppGatewaysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: AppGateway = ...,
                    appGatewayId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AppGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListAppGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAppGatewaysResponseHttpRequest,
                    previous_response: ListAppGatewaysResponse,
                ) -> ListAppGatewaysResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ApplicationsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientConnectorServicesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ClientConnectorService = ...,
                    clientConnectorServiceId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClientConnectorServiceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListClientConnectorServicesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClientConnectorServicesResponseHttpRequest,
                    previous_response: ListClientConnectorServicesResponse,
                ) -> ListClientConnectorServicesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ClientConnectorService = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientGatewaysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ClientGateway = ...,
                    clientGatewayId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClientGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListClientGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClientGatewaysResponseHttpRequest,
                    previous_response: ListClientGatewaysResponse,
                ) -> ListClientGatewaysResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Connection = ...,
                    connectionId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolve(
                    self,
                    *,
                    parent: str,
                    connectorId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ResolveConnectionsResponseHttpRequest: ...
                def resolve_next(
                    self,
                    previous_request: ResolveConnectionsResponseHttpRequest,
                    previous_response: ResolveConnectionsResponse,
                ) -> ResolveConnectionsResponseHttpRequest | None: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ConnectorsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Connector = ...,
                    connectorId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectorHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListConnectorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectorsResponseHttpRequest,
                    previous_response: ListConnectorsResponse,
                ) -> ListConnectorsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Connector = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    connector: str,
                    body: ReportStatusRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolveInstanceConfig(
                    self, *, connector: str, **kwargs: typing.Any
                ) -> ResolveInstanceConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class InsightsResource(googleapiclient.discovery.Resource):
                def configuredInsight(
                    self,
                    *,
                    insight: str,
                    aggregation: typing_extensions.Literal[
                        "AGGREGATION_UNSPECIFIED",
                        "HOURLY",
                        "DAILY",
                        "WEEKLY",
                        "MONTHLY",
                        "CUSTOM_DATE_RANGE",
                    ] = ...,
                    customGrouping_fieldFilter: str = ...,
                    customGrouping_groupFields: str | _list[str] = ...,
                    endTime: str = ...,
                    fieldFilter: str = ...,
                    group: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    startTime: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest: ...
                def configuredInsight_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest | None: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest | None: ...

            @typing.type_check_only
            class NetConnectionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnection = ...,
                    netConnectionId: str = ...,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponse,
                ) -> GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnection = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def appConnections(self) -> AppConnectionsResource: ...
            def appConnectors(self) -> AppConnectorsResource: ...
            def appGateways(self) -> AppGatewaysResource: ...
            def applications(self) -> ApplicationsResource: ...
            def clientConnectorServices(self) -> ClientConnectorServicesResource: ...
            def clientGateways(self) -> ClientGatewaysResource: ...
            def connections(self) -> ConnectionsResource: ...
            def connectors(self) -> ConnectorsResource: ...
            def insights(self) -> InsightsResource: ...
            def netConnections(self) -> NetConnectionsResource: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AppGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppGateway: ...

@typing.type_check_only
class ClientConnectorServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClientConnectorService: ...

@typing.type_check_only
class ClientGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClientGateway: ...

@typing.type_check_only
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Connection: ...

@typing.type_check_only
class ConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Connector: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnectionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnection: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class ListAppGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAppGatewaysResponse: ...

@typing.type_check_only
class ListClientConnectorServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClientConnectorServicesResponse: ...

@typing.type_check_only
class ListClientGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClientGatewaysResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectorsResponse: ...

@typing.type_check_only
class ResolveConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResolveConnectionsResponse: ...

@typing.type_check_only
class ResolveInstanceConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResolveInstanceConfigResponse: ...
