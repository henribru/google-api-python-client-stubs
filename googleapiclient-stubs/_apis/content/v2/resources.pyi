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
            self,
            *,
            body: AccountsCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> AccountsCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            accountId: str,
            dryRun: bool = ...,
            force: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, accountId: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            body: Account = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
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
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccountsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccountsListResponseHttpRequest,
            previous_response: AccountsListResponse,
        ) -> AccountsListResponseHttpRequest | None: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: Account = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...

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
            self,
            *,
            body: AccounttaxCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> AccountTaxHttpRequest: ...

    @typing.type_check_only
    class DatafeedsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: DatafeedsCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> DatafeedsCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def fetchnow(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> DatafeedsFetchNowResponseHttpRequest: ...
        def get(
            self, *, merchantId: str, datafeedId: str, **kwargs: typing.Any
        ) -> DatafeedHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            body: Datafeed = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
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
            dryRun: bool = ...,
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
    class LiasettingsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: LiasettingsCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> LiaSettingsHttpRequest: ...

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
        def get(
            self, *, merchantId: str, returnId: str, **kwargs: typing.Any
        ) -> MerchantOrderReturnHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            createdEndDate: str = ...,
            createdStartDate: str = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "RETURN_CREATION_TIME_DESC", "RETURN_CREATION_TIME_ASC"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OrderreturnsListResponseHttpRequest,
            previous_response: OrderreturnsListResponse,
        ) -> OrderreturnsListResponseHttpRequest | None: ...

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
        def custombatch(
            self, *, body: OrdersCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> OrdersCustomBatchResponseHttpRequest: ...
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
                "TEMPLATE1", "TEMPLATE2", "TEMPLATE1A", "TEMPLATE1B", "TEMPLATE3"
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
        def refund(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersRefundRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersRefundResponseHttpRequest: ...
        def rejectreturnlineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersRejectReturnLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersRejectReturnLineItemResponseHttpRequest: ...
        def returnlineitem(
            self,
            *,
            merchantId: str,
            orderId: str,
            body: OrdersReturnLineItemRequest = ...,
            **kwargs: typing.Any
        ) -> OrdersReturnLineItemResponseHttpRequest: ...
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
    class PosResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: PosCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> PosCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            storeCode: str,
            dryRun: bool = ...,
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> PosStoreHttpRequest: ...
        def inventory(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosInventoryRequest = ...,
            dryRun: bool = ...,
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> PosSaleResponseHttpRequest: ...

    @typing.type_check_only
    class ProductsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: ProductsCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> ProductsCustomBatchResponseHttpRequest: ...
        def delete(
            self,
            *,
            merchantId: str,
            productId: str,
            dryRun: bool = ...,
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            includeInvalidInsertedItems: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProductsListResponseHttpRequest,
            previous_response: ProductsListResponse,
        ) -> ProductsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProductstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: ProductstatusesCustomBatchRequest = ...,
            includeAttributes: bool = ...,
            **kwargs: typing.Any
        ) -> ProductstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            productId: str,
            destinations: str | _list[str] = ...,
            includeAttributes: bool = ...,
            **kwargs: typing.Any
        ) -> ProductStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: str | _list[str] = ...,
            includeAttributes: bool = ...,
            includeInvalidInsertedItems: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProductstatusesListResponseHttpRequest,
            previous_response: ProductstatusesListResponse,
        ) -> ProductstatusesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class ShippingsettingsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: ShippingsettingsCustomBatchRequest = ...,
            dryRun: bool = ...,
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
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> ShippingSettingsHttpRequest: ...

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
    def datafeeds(self) -> DatafeedsResource: ...
    def datafeedstatuses(self) -> DatafeedstatusesResource: ...
    def liasettings(self) -> LiasettingsResource: ...
    def orderinvoices(self) -> OrderinvoicesResource: ...
    def orderreports(self) -> OrderreportsResource: ...
    def orderreturns(self) -> OrderreturnsResource: ...
    def orders(self) -> OrdersResource: ...
    def pos(self) -> PosResource: ...
    def products(self) -> ProductsResource: ...
    def productstatuses(self) -> ProductstatusesResource: ...
    def shippingsettings(self) -> ShippingsettingsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

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
class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsListResponse: ...

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
class OrderreturnsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderreturnsListResponse: ...

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
class OrdersCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersCustomBatchResponse: ...

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
class OrdersRefundResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersRefundResponse: ...

@typing.type_check_only
class OrdersRejectReturnLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersRejectReturnLineItemResponse: ...

@typing.type_check_only
class OrdersReturnLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersReturnLineItemResponse: ...

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
