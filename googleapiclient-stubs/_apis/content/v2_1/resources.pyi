import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ShoppingContentResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CredentialsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                accountId: str,
                body: AccountCredentials = ...,
                **kwargs: typing.Any
            ) -> AccountCredentialsHttpRequest: ...

        @typing.type_check_only
        class LabelsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, accountId: str, body: AccountLabel = ..., **kwargs: typing.Any
            ) -> AccountLabelHttpRequest: ...
            def delete(
                self, *, accountId: str, labelId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAccountLabelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountLabelsResponseHttpRequest,
                previous_response: ListAccountLabelsResponse,
            ) -> ListAccountLabelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                accountId: str,
                labelId: str,
                body: AccountLabel = ...,
                **kwargs: typing.Any
            ) -> AccountLabelHttpRequest: ...

        @typing.type_check_only
        class ReturncarrierResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                accountId: str,
                body: AccountReturnCarrier = ...,
                **kwargs: typing.Any
            ) -> AccountReturnCarrierHttpRequest: ...
            def delete(
                self, *, accountId: str, carrierAccountId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def list(
                self, *, accountId: str, **kwargs: typing.Any
            ) -> ListAccountReturnCarrierResponseHttpRequest: ...
            def patch(
                self,
                *,
                accountId: str,
                carrierAccountId: str,
                body: AccountReturnCarrier = ...,
                **kwargs: typing.Any
            ) -> AccountReturnCarrierHttpRequest: ...

        def authinfo(
            self, **kwargs: typing.Any
        ) -> AccountsAuthInfoResponseHttpRequest: ...
        def claimwebsite(
            self,
            *,
            merchantId: str,
            accountId: str,
            overwrite: bool = ...,
            **kwargs: typing.Any
        ) -> AccountsClaimWebsiteResponseHttpRequest: ...
        def custombatch(
            self, *, body: AccountsCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> AccountsCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            accountId: str,
            force: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            accountId: str,
            view: typing_extensions.Literal["MERCHANT", "CSS"] = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def insert(
            self, *, merchantId: str, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def link(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountsLinkRequest = ...,
            **kwargs: typing.Any
        ) -> AccountsLinkResponseHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            label: str = ...,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal["MERCHANT", "CSS"] = ...,
            **kwargs: typing.Any
        ) -> AccountsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccountsListResponseHttpRequest,
            previous_response: AccountsListResponse,
        ) -> AccountsListResponseHttpRequest | None: ...
        def listlinks(
            self,
            *,
            merchantId: str,
            accountId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccountsListLinksResponseHttpRequest: ...
        def listlinks_next(
            self,
            previous_request: AccountsListLinksResponseHttpRequest,
            previous_response: AccountsListLinksResponse,
        ) -> AccountsListLinksResponseHttpRequest | None: ...
        def requestphoneverification(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: RequestPhoneVerificationRequest = ...,
            **kwargs: typing.Any
        ) -> RequestPhoneVerificationResponseHttpRequest: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: Account = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def updatelabels(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountsUpdateLabelsRequest = ...,
            **kwargs: typing.Any
        ) -> AccountsUpdateLabelsResponseHttpRequest: ...
        def verifyphonenumber(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: VerifyPhoneNumberRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyPhoneNumberResponseHttpRequest: ...
        def credentials(self) -> CredentialsResource: ...
        def labels(self) -> LabelsResource: ...
        def returncarrier(self) -> ReturncarrierResource: ...

    @typing.type_check_only
    class AccountstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: AccountstatusesCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> AccountstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            accountId: str,
            destinations: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> AccountStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: str | _list[str] = ...,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccountstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccountstatusesListResponseHttpRequest,
            previous_response: AccountstatusesListResponse,
        ) -> AccountstatusesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class AccounttaxResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: AccounttaxCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> AccounttaxCustomBatchResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, accountId: str, **kwargs: typing.Any
        ) -> AccountTaxHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccounttaxListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccounttaxListResponseHttpRequest,
            previous_response: AccounttaxListResponse,
        ) -> AccounttaxListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountTax = ...,
            **kwargs: typing.Any
        ) -> AccountTaxHttpRequest: ...

    @typing.type_check_only
    class BuyongoogleprogramsResource(googleapiclient.discovery.Resource):
        def activate(
            self,
            *,
            merchantId: str,
            regionCode: str,
            body: ActivateBuyOnGoogleProgramRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, regionCode: str, **kwargs: typing.Any
        ) -> BuyOnGoogleProgramStatusHttpRequest: ...
        def onboard(
            self,
            *,
            merchantId: str,
            regionCode: str,
            body: OnboardBuyOnGoogleProgramRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self,
            *,
            merchantId: str,
            regionCode: str,
            body: BuyOnGoogleProgramStatus = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> BuyOnGoogleProgramStatusHttpRequest: ...
        def pause(
            self,
            *,
            merchantId: str,
            regionCode: str,
            body: PauseBuyOnGoogleProgramRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def requestreview(
            self,
            *,
            merchantId: str,
            regionCode: str,
            body: RequestReviewBuyOnGoogleProgramRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class CollectionsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, merchantId: str, body: Collection = ..., **kwargs: typing.Any
        ) -> CollectionHttpRequest: ...
        def delete(
            self, *, merchantId: str, collectionId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, collectionId: str, **kwargs: typing.Any
        ) -> CollectionHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListCollectionsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCollectionsResponseHttpRequest,
            previous_response: ListCollectionsResponse,
        ) -> ListCollectionsResponseHttpRequest | None: ...

    @typing.type_check_only
    class CollectionstatusesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, merchantId: str, collectionId: str, **kwargs: typing.Any
        ) -> CollectionStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListCollectionStatusesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCollectionStatusesResponseHttpRequest,
            previous_response: ListCollectionStatusesResponse,
        ) -> ListCollectionStatusesResponseHttpRequest | None: ...

    @typing.type_check_only
    class CssesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, cssGroupId: str, cssDomainId: str, **kwargs: typing.Any
        ) -> CssHttpRequest: ...
        def list(
            self,
            *,
            cssGroupId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListCssesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCssesResponseHttpRequest,
            previous_response: ListCssesResponse,
        ) -> ListCssesResponseHttpRequest | None: ...
        def updatelabels(
            self,
            *,
            cssGroupId: str,
            cssDomainId: str,
            body: LabelIds = ...,
            **kwargs: typing.Any
        ) -> CssHttpRequest: ...

    @typing.type_check_only
    class DatafeedsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: DatafeedsCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> DatafeedsCustomBatchResponseHttpRequest: ...
        def delete(
            self, *, merchantId: str, datafeedId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def fetchnow(
            self, *, merchantId: str, datafeedId: str, **kwargs: typing.Any
        ) -> DatafeedsFetchNowResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, datafeedId: str, **kwargs: typing.Any
        ) -> DatafeedHttpRequest: ...
        def insert(
            self, *, merchantId: str, body: Datafeed = ..., **kwargs: typing.Any
        ) -> DatafeedHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DatafeedsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DatafeedsListResponseHttpRequest,
            previous_response: DatafeedsListResponse,
        ) -> DatafeedsListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            body: Datafeed = ...,
            **kwargs: typing.Any
        ) -> DatafeedHttpRequest: ...

    @typing.type_check_only
    class DatafeedstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: DatafeedstatusesCustomBatchRequest = ...,
            **kwargs: typing.Any
        ) -> DatafeedstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            country: str = ...,
            language: str = ...,
            **kwargs: typing.Any
        ) -> DatafeedStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DatafeedstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DatafeedstatusesListResponseHttpRequest,
            previous_response: DatafeedstatusesListResponse,
        ) -> DatafeedstatusesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class FreelistingsprogramResource(googleapiclient.discovery.Resource):
        def get(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> FreeListingsProgramStatusHttpRequest: ...
        def requestreview(
            self,
            *,
            merchantId: str,
            body: RequestReviewFreeListingsRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class LiasettingsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: LiasettingsCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> LiasettingsCustomBatchResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, accountId: str, **kwargs: typing.Any
        ) -> LiaSettingsHttpRequest: ...
        def getaccessiblegmbaccounts(
            self, *, merchantId: str, accountId: str, **kwargs: typing.Any
        ) -> LiasettingsGetAccessibleGmbAccountsResponseHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LiasettingsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: LiasettingsListResponseHttpRequest,
            previous_response: LiasettingsListResponse,
        ) -> LiasettingsListResponseHttpRequest | None: ...
        def listposdataproviders(
            self, **kwargs: typing.Any
        ) -> LiasettingsListPosDataProvidersResponseHttpRequest: ...
        def requestgmbaccess(
            self,
            *,
            merchantId: str,
            accountId: str,
            gmbEmail: str,
            **kwargs: typing.Any
        ) -> LiasettingsRequestGmbAccessResponseHttpRequest: ...
        def requestinventoryverification(
            self, *, merchantId: str, accountId: str, country: str, **kwargs: typing.Any
        ) -> LiasettingsRequestInventoryVerificationResponseHttpRequest: ...
        def setinventoryverificationcontact(
            self,
            *,
            merchantId: str,
            accountId: str,
            country: str,
            language: str,
            contactName: str,
            contactEmail: str,
            **kwargs: typing.Any
        ) -> LiasettingsSetInventoryVerificationContactResponseHttpRequest: ...
        def setposdataprovider(
            self,
            *,
            merchantId: str,
            accountId: str,
            country: str,
            posDataProviderId: str = ...,
            posExternalAccountId: str = ...,
            **kwargs: typing.Any
        ) -> LiasettingsSetPosDataProviderResponseHttpRequest: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: LiaSettings = ...,
            **kwargs: typing.Any
        ) -> LiaSettingsHttpRequest: ...

    @typing.type_check_only
    class LocalinventoryResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: LocalinventoryCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> LocalinventoryCustomBatchResponseHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            productId: str,
            body: LocalInventory = ...,
            **kwargs: typing.Any
        ) -> LocalInventoryHttpRequest: ...

    @typing.type_check_only
    class OrderinvoicesResource(googleapiclient.discovery.Resource):
        def createchargeinvoice(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrderinvoicesCreateChargeInvoiceRequest = ...,
            **kwargs: typing.Any
        ) -> OrderinvoicesCreateChargeInvoiceResponseHttpRequest: ...
        def createrefundinvoice(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrderinvoicesCreateRefundInvoiceRequest = ...,
            **kwargs: typing.Any
        ) -> OrderinvoicesCreateRefundInvoiceResponseHttpRequest: ...

    @typing.type_check_only
    class OrderreportsResource(googleapiclient.discovery.Resource):
        def listdisbursements(
            self,
            *,
            merchantId: str,
            disbursementEndDate: str = ...,
            disbursementStartDate: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OrderreportsListDisbursementsResponseHttpRequest: ...
        def listdisbursements_next(
            self,
            previous_request: OrderreportsListDisbursementsResponseHttpRequest,
            previous_response: OrderreportsListDisbursementsResponse,
        ) -> OrderreportsListDisbursementsResponseHttpRequest | None: ...
        def listtransactions(
            self,
            *,
            merchantId: str,
            disbursementId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            transactionEndDate: str = ...,
            transactionStartDate: str = ...,
            **kwargs: typing.Any
        ) -> OrderreportsListTransactionsResponseHttpRequest: ...
        def listtransactions_next(
            self,
            previous_request: OrderreportsListTransactionsResponseHttpRequest,
            previous_response: OrderreportsListTransactionsResponse,
        ) -> OrderreportsListTransactionsResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrderreturnsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LabelsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                merchantId: str,
                returnId: str,
                body: ReturnShippingLabel = ...,
                **kwargs: typing.Any
            ) -> ReturnShippingLabelHttpRequest: ...

        def acknowledge(
            self,
            *,
            merchantId: str,
            returnId: str,
            body: OrderreturnsAcknowledgeRequest = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsAcknowledgeResponseHttpRequest: ...
        def createorderreturn(
            self,
            *,
            merchantId: str,
            body: OrderreturnsCreateOrderReturnRequest = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsCreateOrderReturnResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, returnId: str, **kwargs: typing.Any
        ) -> MerchantOrderReturnHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            acknowledged: bool = ...,
            createdEndDate: str = ...,
            createdStartDate: str = ...,
            googleOrderIds: str | _list[str] = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "RETURN_CREATION_TIME_DESC", "RETURN_CREATION_TIME_ASC"
            ] = ...,
            pageToken: str = ...,
            shipmentStates: typing_extensions.Literal[
                "NEW", "SHIPPED", "COMPLETED", "UNDELIVERABLE", "PENDING"
            ]
            | _list[
                typing_extensions.Literal[
                    "NEW", "SHIPPED", "COMPLETED", "UNDELIVERABLE", "PENDING"
                ]
            ] = ...,
            shipmentStatus: typing_extensions.Literal["NEW", "IN_PROGRESS", "PROCESSED"]
            | _list[typing_extensions.Literal["NEW", "IN_PROGRESS", "PROCESSED"]] = ...,
            shipmentTrackingNumbers: str | _list[str] = ...,
            shipmentTypes: typing_extensions.Literal[
                "BY_MAIL", "RETURNLESS", "CONTACT_CUSTOMER_SUPPORT"
            ]
            | _list[
                typing_extensions.Literal[
                    "BY_MAIL", "RETURNLESS", "CONTACT_CUSTOMER_SUPPORT"
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OrderreturnsListResponseHttpRequest,
            previous_response: OrderreturnsListResponse,
        ) -> OrderreturnsListResponseHttpRequest | None: ...
        def process(
            self,
            *,
            merchantId: str,
            returnId: str,
            body: OrderreturnsProcessRequest = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsProcessResponseHttpRequest: ...
        def labels(self) -> LabelsResource: ...

    @typing.type_check_only
    class OrdersResource(googleapiclient.discovery.Resource):
        def acknowledge(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersAcknowledgeRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersAcknowledgeResponseHttpRequest: ...
        def advancetestorder(
            self, *, merchantId: str, orderId: str, **kwargs: typing.Any
        ) -> OrdersAdvanceTestOrderResponseHttpRequest: ...
        def cancel(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersCancelRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersCancelResponseHttpRequest: ...
        def cancellineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersCancelLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersCancelLineItemResponseHttpRequest: ...
        def canceltestorderbycustomer(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersCancelTestOrderByCustomerRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersCancelTestOrderByCustomerResponseHttpRequest: ...
        def captureOrder(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: CaptureOrderRequest = ...,
            **kwargs: typing.Any
        ) -> CaptureOrderResponseHttpRequest: ...
        def createtestorder(
            self,
            *,
            merchantId: str,
            body: OrdersCreateTestOrderRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersCreateTestOrderResponseHttpRequest: ...
        def createtestreturn(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersCreateTestReturnRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersCreateTestReturnResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, orderId: str, **kwargs: typing.Any
        ) -> OrderHttpRequest: ...
        def getbymerchantorderid(
            self, *, merchantId: str, merchantOrderId: str, **kwargs: typing.Any
        ) -> OrdersGetByMerchantOrderIdResponseHttpRequest: ...
        def gettestordertemplate(
            self,
            *,
            merchantId: str,
            templateName: typing_extensions.Literal[
                "TEMPLATE1",
                "TEMPLATE2",
                "TEMPLATE1A",
                "TEMPLATE1B",
                "TEMPLATE3",
                "TEMPLATE4",
            ],
            country: str = ...,
            **kwargs: typing.Any
        ) -> OrdersGetTestOrderTemplateResponseHttpRequest: ...
        def instorerefundlineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersInStoreRefundLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersInStoreRefundLineItemResponseHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            acknowledged: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            placedDateEnd: str = ...,
            placedDateStart: str = ...,
            statuses: typing_extensions.Literal[
                "ACTIVE",
                "COMPLETED",
                "CANCELED",
                "IN_PROGRESS",
                "PENDING_SHIPMENT",
                "PARTIALLY_SHIPPED",
                "SHIPPED",
                "PARTIALLY_DELIVERED",
                "DELIVERED",
                "PARTIALLY_RETURNED",
                "RETURNED",
            ]
            | _list[
                typing_extensions.Literal[
                    "ACTIVE",
                    "COMPLETED",
                    "CANCELED",
                    "IN_PROGRESS",
                    "PENDING_SHIPMENT",
                    "PARTIALLY_SHIPPED",
                    "SHIPPED",
                    "PARTIALLY_DELIVERED",
                    "DELIVERED",
                    "PARTIALLY_RETURNED",
                    "RETURNED",
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> OrdersListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OrdersListResponseHttpRequest,
            previous_response: OrdersListResponse,
        ) -> OrdersListResponseHttpRequest | None: ...
        def refunditem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersRefundItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersRefundItemResponseHttpRequest: ...
        def refundorder(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersRefundOrderRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersRefundOrderResponseHttpRequest: ...
        def rejectreturnlineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersRejectReturnLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersRejectReturnLineItemResponseHttpRequest: ...
        def returnrefundlineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersReturnRefundLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersReturnRefundLineItemResponseHttpRequest: ...
        def setlineitemmetadata(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersSetLineItemMetadataRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersSetLineItemMetadataResponseHttpRequest: ...
        def shiplineitems(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersShipLineItemsRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersShipLineItemsResponseHttpRequest: ...
        def updatelineitemshippingdetails(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersUpdateLineItemShippingDetailsRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersUpdateLineItemShippingDetailsResponseHttpRequest: ...
        def updatemerchantorderid(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersUpdateMerchantOrderIdRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersUpdateMerchantOrderIdResponseHttpRequest: ...
        def updateshipment(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersUpdateShipmentRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersUpdateShipmentResponseHttpRequest: ...

    @typing.type_check_only
    class OrdertrackingsignalsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: OrderTrackingSignal = ...,
            **kwargs: typing.Any
        ) -> OrderTrackingSignalHttpRequest: ...

    @typing.type_check_only
    class PosResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: PosCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> PosCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            storeCode: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            storeCode: str,
            **kwargs: typing.Any
        ) -> PosStoreHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosStore = ...,
            **kwargs: typing.Any
        ) -> PosStoreHttpRequest: ...
        def inventory(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosInventoryRequest = ...,
            **kwargs: typing.Any
        ) -> PosInventoryResponseHttpRequest: ...
        def list(
            self, *, merchantId: str, targetMerchantId: str, **kwargs: typing.Any
        ) -> PosListResponseHttpRequest: ...
        def sale(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosSaleRequest = ...,
            **kwargs: typing.Any
        ) -> PosSaleResponseHttpRequest: ...

    @typing.type_check_only
    class ProductdeliverytimeResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: ProductDeliveryTime = ...,
            **kwargs: typing.Any
        ) -> ProductDeliveryTimeHttpRequest: ...
        def delete(
            self, *, merchantId: str, productId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, productId: str, **kwargs: typing.Any
        ) -> ProductDeliveryTimeHttpRequest: ...

    @typing.type_check_only
    class ProductsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: ProductsCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ProductsCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            productId: str,
            feedId: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, productId: str, **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            body: Product = ...,
            feedId: str = ...,
            **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProductsListResponseHttpRequest,
            previous_response: ProductsListResponse,
        ) -> ProductsListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            merchantId: str,
            productId: str,
            body: Product = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> ProductHttpRequest: ...

    @typing.type_check_only
    class ProductstatusesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RepricingreportsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                merchantId: str,
                productId: str,
                endDate: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                ruleId: str = ...,
                startDate: str = ...,
                **kwargs: typing.Any
            ) -> ListRepricingProductReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRepricingProductReportsResponseHttpRequest,
                previous_response: ListRepricingProductReportsResponse,
            ) -> ListRepricingProductReportsResponseHttpRequest | None: ...

        def custombatch(
            self, *, body: ProductstatusesCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ProductstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            productId: str,
            destinations: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> ProductStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProductstatusesListResponseHttpRequest,
            previous_response: ProductstatusesListResponse,
        ) -> ProductstatusesListResponseHttpRequest | None: ...
        def repricingreports(self) -> RepricingreportsResource: ...

    @typing.type_check_only
    class PromotionsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, merchantId: str, body: Promotion = ..., **kwargs: typing.Any
        ) -> PromotionHttpRequest: ...
        def get(
            self, *, merchantId: str, id: str, **kwargs: typing.Any
        ) -> PromotionHttpRequest: ...

    @typing.type_check_only
    class PubsubnotificationsettingsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> PubsubNotificationSettingsHttpRequest: ...
        def update(
            self,
            *,
            merchantId: str,
            body: PubsubNotificationSettings = ...,
            **kwargs: typing.Any
        ) -> PubsubNotificationSettingsHttpRequest: ...

    @typing.type_check_only
    class RegionalinventoryResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: RegionalinventoryCustomBatchRequest = ...,
            **kwargs: typing.Any
        ) -> RegionalinventoryCustomBatchResponseHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            productId: str,
            body: RegionalInventory = ...,
            **kwargs: typing.Any
        ) -> RegionalInventoryHttpRequest: ...

    @typing.type_check_only
    class RegionsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: Region = ...,
            regionId: str = ...,
            **kwargs: typing.Any
        ) -> RegionHttpRequest: ...
        def delete(
            self, *, merchantId: str, regionId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, regionId: str, **kwargs: typing.Any
        ) -> RegionHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListRegionsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListRegionsResponseHttpRequest,
            previous_response: ListRegionsResponse,
        ) -> ListRegionsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            merchantId: str,
            regionId: str,
            body: Region = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> RegionHttpRequest: ...

    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def search(
            self, *, merchantId: str, body: SearchRequest = ..., **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchResponseHttpRequest,
            previous_response: SearchResponse,
        ) -> SearchResponseHttpRequest | None: ...

    @typing.type_check_only
    class RepricingrulesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RepricingreportsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                merchantId: str,
                ruleId: str,
                endDate: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                startDate: str = ...,
                **kwargs: typing.Any
            ) -> ListRepricingRuleReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRepricingRuleReportsResponseHttpRequest,
                previous_response: ListRepricingRuleReportsResponse,
            ) -> ListRepricingRuleReportsResponseHttpRequest | None: ...

        def create(
            self,
            *,
            merchantId: str,
            body: RepricingRule = ...,
            ruleId: str = ...,
            **kwargs: typing.Any
        ) -> RepricingRuleHttpRequest: ...
        def delete(
            self, *, merchantId: str, ruleId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, ruleId: str, **kwargs: typing.Any
        ) -> RepricingRuleHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            countryCode: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListRepricingRulesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListRepricingRulesResponseHttpRequest,
            previous_response: ListRepricingRulesResponse,
        ) -> ListRepricingRulesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            merchantId: str,
            ruleId: str,
            body: RepricingRule = ...,
            **kwargs: typing.Any
        ) -> RepricingRuleHttpRequest: ...
        def repricingreports(self) -> RepricingreportsResource: ...

    @typing.type_check_only
    class ReturnaddressResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: ReturnaddressCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ReturnaddressCustomBatchResponseHttpRequest: ...
        def delete(
            self, *, merchantId: str, returnAddressId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, returnAddressId: str, **kwargs: typing.Any
        ) -> ReturnAddressHttpRequest: ...
        def insert(
            self, *, merchantId: str, body: ReturnAddress = ..., **kwargs: typing.Any
        ) -> ReturnAddressHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            country: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ReturnaddressListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ReturnaddressListResponseHttpRequest,
            previous_response: ReturnaddressListResponse,
        ) -> ReturnaddressListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ReturnpolicyResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: ReturnpolicyCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ReturnpolicyCustomBatchResponseHttpRequest: ...
        def delete(
            self, *, merchantId: str, returnPolicyId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, returnPolicyId: str, **kwargs: typing.Any
        ) -> ReturnPolicyHttpRequest: ...
        def insert(
            self, *, merchantId: str, body: ReturnPolicy = ..., **kwargs: typing.Any
        ) -> ReturnPolicyHttpRequest: ...
        def list(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ReturnpolicyListResponseHttpRequest: ...

    @typing.type_check_only
    class ReturnpolicyonlineResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: ReturnPolicyOnline = ...,
            **kwargs: typing.Any
        ) -> ReturnPolicyOnlineHttpRequest: ...
        def delete(
            self, *, merchantId: str, returnPolicyId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, returnPolicyId: str, **kwargs: typing.Any
        ) -> ReturnPolicyOnlineHttpRequest: ...
        def list(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ListReturnPolicyOnlineResponseHttpRequest: ...
        def patch(
            self,
            *,
            merchantId: str,
            returnPolicyId: str,
            body: ReturnPolicyOnline = ...,
            **kwargs: typing.Any
        ) -> ReturnPolicyOnlineHttpRequest: ...

    @typing.type_check_only
    class SettlementreportsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, merchantId: str, settlementId: str, **kwargs: typing.Any
        ) -> SettlementReportHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            transferEndDate: str = ...,
            transferStartDate: str = ...,
            **kwargs: typing.Any
        ) -> SettlementreportsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SettlementreportsListResponseHttpRequest,
            previous_response: SettlementreportsListResponse,
        ) -> SettlementreportsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class SettlementtransactionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            merchantId: str,
            settlementId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            transactionIds: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> SettlementtransactionsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SettlementtransactionsListResponseHttpRequest,
            previous_response: SettlementtransactionsListResponse,
        ) -> SettlementtransactionsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ShippingsettingsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: ShippingsettingsCustomBatchRequest = ...,
            **kwargs: typing.Any
        ) -> ShippingsettingsCustomBatchResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, accountId: str, **kwargs: typing.Any
        ) -> ShippingSettingsHttpRequest: ...
        def getsupportedcarriers(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ShippingsettingsGetSupportedCarriersResponseHttpRequest: ...
        def getsupportedholidays(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ShippingsettingsGetSupportedHolidaysResponseHttpRequest: ...
        def getsupportedpickupservices(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ShippingsettingsGetSupportedPickupServicesResponseHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ShippingsettingsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ShippingsettingsListResponseHttpRequest,
            previous_response: ShippingsettingsListResponse,
        ) -> ShippingsettingsListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: ShippingSettings = ...,
            **kwargs: typing.Any
        ) -> ShippingSettingsHttpRequest: ...

    @typing.type_check_only
    class ShoppingadsprogramResource(googleapiclient.discovery.Resource):
        def get(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> ShoppingAdsProgramStatusHttpRequest: ...
        def requestreview(
            self,
            *,
            merchantId: str,
            body: RequestReviewShoppingAdsRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def accountstatuses(self) -> AccountstatusesResource: ...
    def accounttax(self) -> AccounttaxResource: ...
    def buyongoogleprograms(self) -> BuyongoogleprogramsResource: ...
    def collections(self) -> CollectionsResource: ...
    def collectionstatuses(self) -> CollectionstatusesResource: ...
    def csses(self) -> CssesResource: ...
    def datafeeds(self) -> DatafeedsResource: ...
    def datafeedstatuses(self) -> DatafeedstatusesResource: ...
    def freelistingsprogram(self) -> FreelistingsprogramResource: ...
    def liasettings(self) -> LiasettingsResource: ...
    def localinventory(self) -> LocalinventoryResource: ...
    def orderinvoices(self) -> OrderinvoicesResource: ...
    def orderreports(self) -> OrderreportsResource: ...
    def orderreturns(self) -> OrderreturnsResource: ...
    def orders(self) -> OrdersResource: ...
    def ordertrackingsignals(self) -> OrdertrackingsignalsResource: ...
    def pos(self) -> PosResource: ...
    def productdeliverytime(self) -> ProductdeliverytimeResource: ...
    def products(self) -> ProductsResource: ...
    def productstatuses(self) -> ProductstatusesResource: ...
    def promotions(self) -> PromotionsResource: ...
    def pubsubnotificationsettings(self) -> PubsubnotificationsettingsResource: ...
    def regionalinventory(self) -> RegionalinventoryResource: ...
    def regions(self) -> RegionsResource: ...
    def reports(self) -> ReportsResource: ...
    def repricingrules(self) -> RepricingrulesResource: ...
    def returnaddress(self) -> ReturnaddressResource: ...
    def returnpolicy(self) -> ReturnpolicyResource: ...
    def returnpolicyonline(self) -> ReturnpolicyonlineResource: ...
    def settlementreports(self) -> SettlementreportsResource: ...
    def settlementtransactions(self) -> SettlementtransactionsResource: ...
    def shippingsettings(self) -> ShippingsettingsResource: ...
    def shoppingadsprogram(self) -> ShoppingadsprogramResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AccountCredentialsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountCredentials: ...

@typing.type_check_only
class AccountLabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountLabel: ...

@typing.type_check_only
class AccountReturnCarrierHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountReturnCarrier: ...

@typing.type_check_only
class AccountStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountStatus: ...

@typing.type_check_only
class AccountTaxHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountTax: ...

@typing.type_check_only
class AccountsAuthInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsAuthInfoResponse: ...

@typing.type_check_only
class AccountsClaimWebsiteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsClaimWebsiteResponse: ...

@typing.type_check_only
class AccountsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsCustomBatchResponse: ...

@typing.type_check_only
class AccountsLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsLinkResponse: ...

@typing.type_check_only
class AccountsListLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsListLinksResponse: ...

@typing.type_check_only
class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsListResponse: ...

@typing.type_check_only
class AccountsUpdateLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsUpdateLabelsResponse: ...

@typing.type_check_only
class AccountstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountstatusesCustomBatchResponse: ...

@typing.type_check_only
class AccountstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountstatusesListResponse: ...

@typing.type_check_only
class AccounttaxCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccounttaxCustomBatchResponse: ...

@typing.type_check_only
class AccounttaxListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccounttaxListResponse: ...

@typing.type_check_only
class BuyOnGoogleProgramStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BuyOnGoogleProgramStatus: ...

@typing.type_check_only
class CaptureOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CaptureOrderResponse: ...

@typing.type_check_only
class CollectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Collection: ...

@typing.type_check_only
class CollectionStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CollectionStatus: ...

@typing.type_check_only
class CssHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Css: ...

@typing.type_check_only
class DatafeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Datafeed: ...

@typing.type_check_only
class DatafeedStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedStatus: ...

@typing.type_check_only
class DatafeedsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedsCustomBatchResponse: ...

@typing.type_check_only
class DatafeedsFetchNowResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedsFetchNowResponse: ...

@typing.type_check_only
class DatafeedsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedsListResponse: ...

@typing.type_check_only
class DatafeedstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedstatusesCustomBatchResponse: ...

@typing.type_check_only
class DatafeedstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DatafeedstatusesListResponse: ...

@typing.type_check_only
class FreeListingsProgramStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FreeListingsProgramStatus: ...

@typing.type_check_only
class LiaSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiaSettings: ...

@typing.type_check_only
class LiasettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsCustomBatchResponse: ...

@typing.type_check_only
class LiasettingsGetAccessibleGmbAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsGetAccessibleGmbAccountsResponse: ...

@typing.type_check_only
class LiasettingsListPosDataProvidersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsListPosDataProvidersResponse: ...

@typing.type_check_only
class LiasettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsListResponse: ...

@typing.type_check_only
class LiasettingsRequestGmbAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsRequestGmbAccessResponse: ...

@typing.type_check_only
class LiasettingsRequestInventoryVerificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsRequestInventoryVerificationResponse: ...

@typing.type_check_only
class LiasettingsSetInventoryVerificationContactResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsSetInventoryVerificationContactResponse: ...

@typing.type_check_only
class LiasettingsSetPosDataProviderResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LiasettingsSetPosDataProviderResponse: ...

@typing.type_check_only
class ListAccountLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountLabelsResponse: ...

@typing.type_check_only
class ListAccountReturnCarrierResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountReturnCarrierResponse: ...

@typing.type_check_only
class ListCollectionStatusesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCollectionStatusesResponse: ...

@typing.type_check_only
class ListCollectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCollectionsResponse: ...

@typing.type_check_only
class ListCssesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCssesResponse: ...

@typing.type_check_only
class ListRegionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRegionsResponse: ...

@typing.type_check_only
class ListRepricingProductReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRepricingProductReportsResponse: ...

@typing.type_check_only
class ListRepricingRuleReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRepricingRuleReportsResponse: ...

@typing.type_check_only
class ListRepricingRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRepricingRulesResponse: ...

@typing.type_check_only
class ListReturnPolicyOnlineResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReturnPolicyOnlineResponse: ...

@typing.type_check_only
class LocalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LocalInventory: ...

@typing.type_check_only
class LocalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LocalinventoryCustomBatchResponse: ...

@typing.type_check_only
class MerchantOrderReturnHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MerchantOrderReturn: ...

@typing.type_check_only
class OrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Order: ...

@typing.type_check_only
class OrderTrackingSignalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderTrackingSignal: ...

@typing.type_check_only
class OrderinvoicesCreateChargeInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderinvoicesCreateChargeInvoiceResponse: ...

@typing.type_check_only
class OrderinvoicesCreateRefundInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderinvoicesCreateRefundInvoiceResponse: ...

@typing.type_check_only
class OrderreportsListDisbursementsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreportsListDisbursementsResponse: ...

@typing.type_check_only
class OrderreportsListTransactionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreportsListTransactionsResponse: ...

@typing.type_check_only
class OrderreturnsAcknowledgeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreturnsAcknowledgeResponse: ...

@typing.type_check_only
class OrderreturnsCreateOrderReturnResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreturnsCreateOrderReturnResponse: ...

@typing.type_check_only
class OrderreturnsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreturnsListResponse: ...

@typing.type_check_only
class OrderreturnsProcessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreturnsProcessResponse: ...

@typing.type_check_only
class OrdersAcknowledgeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersAcknowledgeResponse: ...

@typing.type_check_only
class OrdersAdvanceTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersAdvanceTestOrderResponse: ...

@typing.type_check_only
class OrdersCancelLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCancelLineItemResponse: ...

@typing.type_check_only
class OrdersCancelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCancelResponse: ...

@typing.type_check_only
class OrdersCancelTestOrderByCustomerResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCancelTestOrderByCustomerResponse: ...

@typing.type_check_only
class OrdersCreateTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCreateTestOrderResponse: ...

@typing.type_check_only
class OrdersCreateTestReturnResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCreateTestReturnResponse: ...

@typing.type_check_only
class OrdersGetByMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersGetByMerchantOrderIdResponse: ...

@typing.type_check_only
class OrdersGetTestOrderTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersGetTestOrderTemplateResponse: ...

@typing.type_check_only
class OrdersInStoreRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersInStoreRefundLineItemResponse: ...

@typing.type_check_only
class OrdersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersListResponse: ...

@typing.type_check_only
class OrdersRefundItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersRefundItemResponse: ...

@typing.type_check_only
class OrdersRefundOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersRefundOrderResponse: ...

@typing.type_check_only
class OrdersRejectReturnLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersRejectReturnLineItemResponse: ...

@typing.type_check_only
class OrdersReturnRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersReturnRefundLineItemResponse: ...

@typing.type_check_only
class OrdersSetLineItemMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersSetLineItemMetadataResponse: ...

@typing.type_check_only
class OrdersShipLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersShipLineItemsResponse: ...

@typing.type_check_only
class OrdersUpdateLineItemShippingDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersUpdateLineItemShippingDetailsResponse: ...

@typing.type_check_only
class OrdersUpdateMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersUpdateMerchantOrderIdResponse: ...

@typing.type_check_only
class OrdersUpdateShipmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersUpdateShipmentResponse: ...

@typing.type_check_only
class PosCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PosCustomBatchResponse: ...

@typing.type_check_only
class PosInventoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PosInventoryResponse: ...

@typing.type_check_only
class PosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PosListResponse: ...

@typing.type_check_only
class PosSaleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PosSaleResponse: ...

@typing.type_check_only
class PosStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PosStore: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Product: ...

@typing.type_check_only
class ProductDeliveryTimeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductDeliveryTime: ...

@typing.type_check_only
class ProductStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductStatus: ...

@typing.type_check_only
class ProductsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductsCustomBatchResponse: ...

@typing.type_check_only
class ProductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductsListResponse: ...

@typing.type_check_only
class ProductstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductstatusesCustomBatchResponse: ...

@typing.type_check_only
class ProductstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductstatusesListResponse: ...

@typing.type_check_only
class PromotionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Promotion: ...

@typing.type_check_only
class PubsubNotificationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PubsubNotificationSettings: ...

@typing.type_check_only
class RegionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Region: ...

@typing.type_check_only
class RegionalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionalInventory: ...

@typing.type_check_only
class RegionalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionalinventoryCustomBatchResponse: ...

@typing.type_check_only
class RepricingRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RepricingRule: ...

@typing.type_check_only
class RequestPhoneVerificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RequestPhoneVerificationResponse: ...

@typing.type_check_only
class ReturnAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnAddress: ...

@typing.type_check_only
class ReturnPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnPolicy: ...

@typing.type_check_only
class ReturnPolicyOnlineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnPolicyOnline: ...

@typing.type_check_only
class ReturnShippingLabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnShippingLabel: ...

@typing.type_check_only
class ReturnaddressCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnaddressCustomBatchResponse: ...

@typing.type_check_only
class ReturnaddressListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnaddressListResponse: ...

@typing.type_check_only
class ReturnpolicyCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnpolicyCustomBatchResponse: ...

@typing.type_check_only
class ReturnpolicyListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReturnpolicyListResponse: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchResponse: ...

@typing.type_check_only
class SettlementReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SettlementReport: ...

@typing.type_check_only
class SettlementreportsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SettlementreportsListResponse: ...

@typing.type_check_only
class SettlementtransactionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SettlementtransactionsListResponse: ...

@typing.type_check_only
class ShippingSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingSettings: ...

@typing.type_check_only
class ShippingsettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingsettingsCustomBatchResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedCarriersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingsettingsGetSupportedCarriersResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedHolidaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingsettingsGetSupportedHolidaysResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedPickupServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingsettingsGetSupportedPickupServicesResponse: ...

@typing.type_check_only
class ShippingsettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShippingsettingsListResponse: ...

@typing.type_check_only
class ShoppingAdsProgramStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShoppingAdsProgramStatus: ...

@typing.type_check_only
class VerifyPhoneNumberResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VerifyPhoneNumberResponse: ...
