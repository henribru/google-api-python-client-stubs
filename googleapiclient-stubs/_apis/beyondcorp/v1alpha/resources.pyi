import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BeyondCorpResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PartnerTenantsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class BrowserDlpRulesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self,
                            *,
                            name: str,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRuleHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def list(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule = ...,
                            requestId: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    @typing.type_check_only
                    class ProxyConfigsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self,
                            *,
                            name: str,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfigHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponseHttpRequest,
                            previous_response: GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse,
                        ) -> (
                            GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig = ...,
                            requestId: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant = ...,
                        requestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenantHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponseHttpRequest,
                        previous_response: GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse,
                    ) -> (
                        GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant = ...,
                        requestId: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def browserDlpRules(self) -> BrowserDlpRulesResource: ...
                    def proxyConfigs(self) -> ProxyConfigsResource: ...

                def partnerTenants(self) -> PartnerTenantsResource: ...

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
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest: ...
                def configuredInsight_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest
                    | None
                ): ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    aggregation: typing_extensions.Literal[
                        "AGGREGATION_UNSPECIFIED",
                        "HOURLY",
                        "DAILY",
                        "WEEKLY",
                        "MONTHLY",
                        "CUSTOM_DATE_RANGE",
                    ] = ...,
                    endTime: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    startTime: str = ...,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class SubscriptionsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscriptionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscriptionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscriptionHttpRequest: ...
                def restart(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponseHttpRequest: ...

            def global_(self) -> GlobalResource: ...
            def insights(self) -> InsightsResource: ...
            def operations(self) -> OperationsResource: ...
            def subscriptions(self) -> SubscriptionsResource: ...

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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionHttpRequest
                ): ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection = ...,
                    allowMissing: bool = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolve(
                    self,
                    *,
                    parent: str,
                    appConnectorId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest: ...
                def resolve_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest
                    | None
                ): ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorHttpRequest
                ): ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse,
                ) -> (
                    GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    appConnector: str,
                    body: GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolveInstanceConfig(
                    self, *, appConnector: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> AppGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def shouldThrottle(
                    self,
                    *,
                    name: str,
                    port: int = ...,
                    requestedAmount: str = ...,
                    **kwargs: typing.Any,
                ) -> ShouldThrottleResponseHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ApplicationDomainsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ApplicationsResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientConnectorServicesResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class ClientGatewaysResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectionHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolve(
                    self,
                    *,
                    parent: str,
                    connectorId: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectorHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def reportStatus(
                    self,
                    *,
                    connector: str,
                    body: ReportStatusRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def resolveInstanceConfig(
                    self, *, connector: str, **kwargs: typing.Any
                ) -> ResolveInstanceConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SecurityGatewaysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ApplicationsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication = ...,
                            applicationId: str = ...,
                            requestId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication = ...,
                            requestId: str = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                    def applications(self) -> ApplicationsResource: ...

                def securityGateways(self) -> SecurityGatewaysResource: ...

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
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest: ...
                def configuredInsight_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest
                    | None
                ): ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    aggregation: typing_extensions.Literal[
                        "AGGREGATION_UNSPECIFIED",
                        "HOURLY",
                        "DAILY",
                        "WEEKLY",
                        "MONTHLY",
                        "CUSTOM_DATE_RANGE",
                    ] = ...,
                    endTime: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    startTime: str = ...,
                    view: typing_extensions.Literal[
                        "INSIGHT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse,
                ) -> (
                    GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest
                    | None
                ): ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class SecurityGatewaysResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ApplicationsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self,
                        *,
                        name: str,
                        requestId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponseHttpRequest,
                        previous_response: GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse,
                    ) -> (
                        GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponseHttpRequest
                        | None
                    ): ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleIamV1PolicyHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway = ...,
                    requestId: str = ...,
                    securityGatewayId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    requestId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponseHttpRequest,
                    previous_response: GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse,
                ) -> (
                    GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def applications(self) -> ApplicationsResource: ...

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
                **kwargs: typing.Any,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def appConnections(self) -> AppConnectionsResource: ...
            def appConnectors(self) -> AppConnectorsResource: ...
            def appGateways(self) -> AppGatewaysResource: ...
            def applicationDomains(self) -> ApplicationDomainsResource: ...
            def applications(self) -> ApplicationsResource: ...
            def clientConnectorServices(self) -> ClientConnectorServicesResource: ...
            def clientGateways(self) -> ClientGatewaysResource: ...
            def connections(self) -> ConnectionsResource: ...
            def connectors(self) -> ConnectorsResource: ...
            def global_(self) -> GlobalResource: ...
            def insights(self) -> InsightsResource: ...
            def operations(self) -> OperationsResource: ...
            def securityGateways(self) -> SecurityGatewaysResource: ...

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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AppGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppGateway: ...

@typing.type_check_only
class ConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connection: ...

@typing.type_check_only
class ConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connector: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenantHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant: ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse
    ): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse
    ): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse
    ): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscriptionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse: ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class ListAppGatewaysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppGatewaysResponse: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectorsResponse: ...

@typing.type_check_only
class ResolveConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResolveConnectionsResponse: ...

@typing.type_check_only
class ResolveInstanceConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResolveInstanceConfigResponse: ...

@typing.type_check_only
class ShouldThrottleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShouldThrottleResponse: ...
