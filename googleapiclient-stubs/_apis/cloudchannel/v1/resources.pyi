import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudchannelResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChannelPartnerLinksResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ChannelPartnerRepricingConfigsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1ChannelPartnerRepricingConfig = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ChannelPartnerRepricingConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1ChannelPartnerRepricingConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponse,
                ) -> (
                    GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChannelPartnerRepricingConfig = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ChannelPartnerRepricingConfigHttpRequest: ...

            @typing.type_check_only
            class CustomersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1Customer = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1ImportCustomerRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ListCustomersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListCustomersResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListCustomersResponse,
                ) -> GoogleCloudChannelV1ListCustomersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1Customer = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1CustomerHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1ChannelPartnerLink = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal["UNSPECIFIED", "BASIC", "FULL"] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal["UNSPECIFIED", "BASIC", "FULL"] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListChannelPartnerLinksResponse,
            ) -> (
                GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudChannelV1UpdateChannelPartnerLinkRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
            def channelPartnerRepricingConfigs(
                self,
            ) -> ChannelPartnerRepricingConfigsResource: ...
            def customers(self) -> CustomersResource: ...

        @typing.type_check_only
        class CustomersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomerRepricingConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1CustomerRepricingConfig = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1CustomerRepricingConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1CustomerRepricingConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudChannelV1ListCustomerRepricingConfigsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListCustomerRepricingConfigsResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListCustomerRepricingConfigsResponse,
                ) -> (
                    GoogleCloudChannelV1ListCustomerRepricingConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1CustomerRepricingConfig = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1CustomerRepricingConfigHttpRequest: ...

            @typing.type_check_only
            class EntitlementsResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ActivateEntitlementRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1CancelEntitlementRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeOffer(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeOfferRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeParameters(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeParametersRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeRenewalSettings(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeRenewalSettingsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1CreateEntitlementRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1EntitlementHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ListEntitlementsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListEntitlementsResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListEntitlementsResponse,
                ) -> GoogleCloudChannelV1ListEntitlementsResponseHttpRequest | None: ...
                def listEntitlementChanges(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudChannelV1ListEntitlementChangesResponseHttpRequest: ...
                def listEntitlementChanges_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListEntitlementChangesResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListEntitlementChangesResponse,
                ) -> (
                    GoogleCloudChannelV1ListEntitlementChangesResponseHttpRequest | None
                ): ...
                def lookupOffer(
                    self, *, entitlement: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1OfferHttpRequest: ...
                def startPaidService(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1StartPaidServiceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def suspend(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1SuspendEntitlementRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1Customer = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def import_(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1ImportCustomerRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListCustomersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListCustomersResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListCustomersResponse,
            ) -> GoogleCloudChannelV1ListCustomersResponseHttpRequest | None: ...
            def listPurchasableOffers(
                self,
                *,
                customer: str,
                changeOfferPurchase_billingAccount: str = ...,
                changeOfferPurchase_entitlement: str = ...,
                changeOfferPurchase_newSku: str = ...,
                createEntitlementPurchase_billingAccount: str = ...,
                createEntitlementPurchase_sku: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest: ...
            def listPurchasableOffers_next(
                self,
                previous_request: GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListPurchasableOffersResponse,
            ) -> (
                GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest | None
            ): ...
            def listPurchasableSkus(
                self,
                *,
                customer: str,
                changeOfferPurchase_changeType: typing_extensions.Literal[
                    "CHANGE_TYPE_UNSPECIFIED", "UPGRADE", "DOWNGRADE"
                ] = ...,
                changeOfferPurchase_entitlement: str = ...,
                createEntitlementPurchase_product: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest: ...
            def listPurchasableSkus_next(
                self,
                previous_request: GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListPurchasableSkusResponse,
            ) -> GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudChannelV1Customer = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def provisionCloudIdentity(
                self,
                *,
                customer: str,
                body: GoogleCloudChannelV1ProvisionCloudIdentityRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def queryEligibleBillingAccounts(
                self,
                *,
                customer: str,
                skus: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudChannelV1QueryEligibleBillingAccountsResponseHttpRequest
            ): ...
            def transferEntitlements(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1TransferEntitlementsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def transferEntitlementsToGoogle(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1TransferEntitlementsToGoogleRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def customerRepricingConfigs(self) -> CustomerRepricingConfigsResource: ...
            def entitlements(self) -> EntitlementsResource: ...

        @typing.type_check_only
        class OffersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                showFutureOffers: bool = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListOffersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListOffersResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListOffersResponse,
            ) -> GoogleCloudChannelV1ListOffersResponseHttpRequest | None: ...

        @typing.type_check_only
        class ReportJobsResource(googleapiclient.discovery.Resource):
            def fetchReportResults(
                self,
                *,
                reportJob: str,
                body: GoogleCloudChannelV1FetchReportResultsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1FetchReportResultsResponseHttpRequest: ...
            def fetchReportResults_next(
                self,
                previous_request: GoogleCloudChannelV1FetchReportResultsResponseHttpRequest,
                previous_response: GoogleCloudChannelV1FetchReportResultsResponse,
            ) -> GoogleCloudChannelV1FetchReportResultsResponseHttpRequest | None: ...

        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListReportsResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListReportsResponse,
            ) -> GoogleCloudChannelV1ListReportsResponseHttpRequest | None: ...
            def run(
                self,
                *,
                name: str,
                body: GoogleCloudChannelV1RunReportJobRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...

        @typing.type_check_only
        class SkuGroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BillableSkusResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudChannelV1ListSkuGroupBillableSkusResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudChannelV1ListSkuGroupBillableSkusResponseHttpRequest,
                    previous_response: GoogleCloudChannelV1ListSkuGroupBillableSkusResponse,
                ) -> (
                    GoogleCloudChannelV1ListSkuGroupBillableSkusResponseHttpRequest
                    | None
                ): ...

            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListSkuGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListSkuGroupsResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListSkuGroupsResponse,
            ) -> GoogleCloudChannelV1ListSkuGroupsResponseHttpRequest | None: ...
            def billableSkus(self) -> BillableSkusResource: ...

        def checkCloudIdentityAccountsExist(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseHttpRequest: ...
        def listSubscribers(
            self,
            *,
            account: str,
            integrator: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1ListSubscribersResponseHttpRequest: ...
        def listSubscribers_next(
            self,
            previous_request: GoogleCloudChannelV1ListSubscribersResponseHttpRequest,
            previous_response: GoogleCloudChannelV1ListSubscribersResponse,
        ) -> GoogleCloudChannelV1ListSubscribersResponseHttpRequest | None: ...
        def listTransferableOffers(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1ListTransferableOffersRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest: ...
        def listTransferableOffers_next(
            self,
            previous_request: GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest,
            previous_response: GoogleCloudChannelV1ListTransferableOffersResponse,
        ) -> GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest | None: ...
        def listTransferableSkus(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1ListTransferableSkusRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest: ...
        def listTransferableSkus_next(
            self,
            previous_request: GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest,
            previous_response: GoogleCloudChannelV1ListTransferableSkusResponse,
        ) -> GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest | None: ...
        def register(
            self,
            *,
            account: str,
            body: GoogleCloudChannelV1RegisterSubscriberRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1RegisterSubscriberResponseHttpRequest: ...
        def unregister(
            self,
            *,
            account: str,
            body: GoogleCloudChannelV1UnregisterSubscriberRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1UnregisterSubscriberResponseHttpRequest: ...
        def channelPartnerLinks(self) -> ChannelPartnerLinksResource: ...
        def customers(self) -> CustomersResource: ...
        def offers(self) -> OffersResource: ...
        def reportJobs(self) -> ReportJobsResource: ...
        def reports(self) -> ReportsResource: ...
        def skuGroups(self) -> SkuGroupsResource: ...

    @typing.type_check_only
    class IntegratorsResource(googleapiclient.discovery.Resource):
        def listSubscribers(
            self,
            *,
            integrator: str,
            account: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1ListSubscribersResponseHttpRequest: ...
        def listSubscribers_next(
            self,
            previous_request: GoogleCloudChannelV1ListSubscribersResponseHttpRequest,
            previous_response: GoogleCloudChannelV1ListSubscribersResponse,
        ) -> GoogleCloudChannelV1ListSubscribersResponseHttpRequest | None: ...
        def registerSubscriber(
            self,
            *,
            integrator: str,
            body: GoogleCloudChannelV1RegisterSubscriberRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1RegisterSubscriberResponseHttpRequest: ...
        def unregisterSubscriber(
            self,
            *,
            integrator: str,
            body: GoogleCloudChannelV1UnregisterSubscriberRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1UnregisterSubscriberResponseHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self,
            *,
            name: str,
            body: GoogleLongrunningCancelOperationRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
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
    class ProductsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SkusResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                account: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudChannelV1ListSkusResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudChannelV1ListSkusResponseHttpRequest,
                previous_response: GoogleCloudChannelV1ListSkusResponse,
            ) -> GoogleCloudChannelV1ListSkusResponseHttpRequest | None: ...

        def list(
            self,
            *,
            account: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudChannelV1ListProductsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleCloudChannelV1ListProductsResponseHttpRequest,
            previous_response: GoogleCloudChannelV1ListProductsResponse,
        ) -> GoogleCloudChannelV1ListProductsResponseHttpRequest | None: ...
        def skus(self) -> SkusResource: ...

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
    def accounts(self) -> AccountsResource: ...
    def integrators(self) -> IntegratorsResource: ...
    def operations(self) -> OperationsResource: ...
    def products(self) -> ProductsResource: ...

@typing.type_check_only
class GoogleCloudChannelV1ChannelPartnerLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ChannelPartnerLink: ...

@typing.type_check_only
class GoogleCloudChannelV1ChannelPartnerRepricingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ChannelPartnerRepricingConfig: ...

@typing.type_check_only
class GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1Customer: ...

@typing.type_check_only
class GoogleCloudChannelV1CustomerRepricingConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1CustomerRepricingConfig: ...

@typing.type_check_only
class GoogleCloudChannelV1EntitlementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1Entitlement: ...

@typing.type_check_only
class GoogleCloudChannelV1FetchReportResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1FetchReportResultsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListChannelPartnerLinksResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListCustomerRepricingConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListCustomerRepricingConfigsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListCustomersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListCustomersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListEntitlementChangesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListEntitlementChangesResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListEntitlementsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListEntitlementsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListProductsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListPurchasableOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListPurchasableSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListReportsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSkuGroupBillableSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListSkuGroupBillableSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSkuGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListSkuGroupsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSkusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSubscribersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListSubscribersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListTransferableOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1ListTransferableSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1OfferHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1Offer: ...

@typing.type_check_only
class GoogleCloudChannelV1QueryEligibleBillingAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1QueryEligibleBillingAccountsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1RegisterSubscriberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1RegisterSubscriberResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1UnregisterSubscriberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudChannelV1UnregisterSubscriberResponse: ...

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
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
