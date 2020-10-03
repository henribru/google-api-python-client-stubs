import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ShoppingContentResource(googleapiclient.discovery.Resource):
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
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: Account = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
    class AccountstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: AccountstatusesCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> AccountstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            accountId: str,
            destinations: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> AccountStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccountstatusesListResponseHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountTax = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> AccountTaxHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            body: Datafeed = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> DatafeedHttpRequest: ...
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
    class InventoryResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: InventoryCustomBatchRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> InventoryCustomBatchResponseHttpRequest: ...
        def set(
            self,
            *,
            merchantId: str,
            storeCode: str,
            productId: str,
            body: InventorySetRequest = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> InventorySetResponseHttpRequest: ...
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
            contactEmail: str,
            contactName: str,
            country: str,
            language: str,
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
    class OrderreportsResource(googleapiclient.discovery.Resource):
        def listdisbursements(
            self,
            *,
            merchantId: str,
            disbursementStartDate: str,
            disbursementEndDate: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OrderreportsListDisbursementsResponseHttpRequest: ...
        def listtransactions(
            self,
            *,
            merchantId: str,
            disbursementId: str,
            transactionStartDate: str,
            maxResults: int = ...,
            pageToken: str = ...,
            transactionEndDate: str = ...,
            **kwargs: typing.Any
        ) -> OrderreportsListTransactionsResponseHttpRequest: ...
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
                "returnCreationTimeAsc", "returnCreationTimeDesc"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsListResponseHttpRequest: ...
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
                "template1", "template1a", "template1b", "template2", "template3"
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
            statuses: typing.Union[
                typing_extensions.Literal[
                    "active",
                    "canceled",
                    "completed",
                    "delivered",
                    "inProgress",
                    "partiallyDelivered",
                    "partiallyReturned",
                    "partiallyShipped",
                    "pendingShipment",
                    "returned",
                    "shipped",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "active",
                        "canceled",
                        "completed",
                        "delivered",
                        "inProgress",
                        "partiallyDelivered",
                        "partiallyReturned",
                        "partiallyShipped",
                        "pendingShipment",
                        "returned",
                        "shipped",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> OrdersListResponseHttpRequest: ...
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
            destinations: typing.Union[str, typing.List[str]] = ...,
            includeAttributes: bool = ...,
            **kwargs: typing.Any
        ) -> ProductStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: typing.Union[str, typing.List[str]] = ...,
            includeAttributes: bool = ...,
            includeInvalidInsertedItems: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductstatusesListResponseHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: ShippingSettings = ...,
            dryRun: bool = ...,
            **kwargs: typing.Any
        ) -> ShippingSettingsHttpRequest: ...
    def accounts(self) -> AccountsResource: ...
    def accountstatuses(self) -> AccountstatusesResource: ...
    def accounttax(self) -> AccounttaxResource: ...
    def datafeeds(self) -> DatafeedsResource: ...
    def datafeedstatuses(self) -> DatafeedstatusesResource: ...
    def inventory(self) -> InventoryResource: ...
    def liasettings(self) -> LiasettingsResource: ...
    def orderinvoices(self) -> OrderinvoicesResource: ...
    def orderreports(self) -> OrderreportsResource: ...
    def orderreturns(self) -> OrderreturnsResource: ...
    def orders(self) -> OrdersResource: ...
    def pos(self) -> PosResource: ...
    def products(self) -> ProductsResource: ...
    def productstatuses(self) -> ProductstatusesResource: ...
    def shippingsettings(self) -> ShippingsettingsResource: ...

class AccountsAuthInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsAuthInfoResponse: ...

class LiasettingsRequestGmbAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsRequestGmbAccessResponse: ...

class OrdersShipLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersShipLineItemsResponse: ...

class PosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosListResponse: ...

class OrdersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersListResponse: ...

class OrderinvoicesCreateChargeInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderinvoicesCreateChargeInvoiceResponse: ...

class OrdersInStoreRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersInStoreRefundLineItemResponse: ...

class OrdersGetByMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersGetByMerchantOrderIdResponse: ...

class OrdersReturnRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersReturnRefundLineItemResponse: ...

class PosSaleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosSaleResponse: ...

class ShippingsettingsGetSupportedHolidaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsGetSupportedHolidaysResponse: ...

class AccountsClaimWebsiteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsClaimWebsiteResponse: ...

class OrdersCreateTestReturnResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCreateTestReturnResponse: ...

class LiasettingsSetInventoryVerificationContactResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsSetInventoryVerificationContactResponse: ...

class DatafeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Datafeed: ...

class DatafeedsFetchNowResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedsFetchNowResponse: ...

class AccountTaxHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountTax: ...

class OrdersCancelLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCancelLineItemResponse: ...

class OrderreportsListDisbursementsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreportsListDisbursementsResponse: ...

class PosCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosCustomBatchResponse: ...

class PosStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosStore: ...

class ShippingsettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsCustomBatchResponse: ...

class LiasettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsCustomBatchResponse: ...

class OrdersAcknowledgeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersAcknowledgeResponse: ...

class LiasettingsRequestInventoryVerificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsRequestInventoryVerificationResponse: ...

class OrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Order: ...

class DatafeedstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedstatusesListResponse: ...

class OrderreportsListTransactionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreportsListTransactionsResponse: ...

class AccountstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountstatusesCustomBatchResponse: ...

class OrdersAdvanceTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersAdvanceTestOrderResponse: ...

class ShippingsettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsListResponse: ...

class ProductstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductstatusesListResponse: ...

class DatafeedstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedstatusesCustomBatchResponse: ...

class LiasettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsListResponse: ...

class OrdersRejectReturnLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersRejectReturnLineItemResponse: ...

class OrdersSetLineItemMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersSetLineItemMetadataResponse: ...

class OrdersReturnLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersReturnLineItemResponse: ...

class ShippingsettingsGetSupportedPickupServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsGetSupportedPickupServicesResponse: ...

class AccountStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountStatus: ...

class LiasettingsSetPosDataProviderResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsSetPosDataProviderResponse: ...

class MerchantOrderReturnHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MerchantOrderReturn: ...

class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsListResponse: ...

class DatafeedsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedsListResponse: ...

class LiasettingsGetAccessibleGmbAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsGetAccessibleGmbAccountsResponse: ...

class ShippingSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingSettings: ...

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class ProductstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductstatusesCustomBatchResponse: ...

class OrdersCancelTestOrderByCustomerResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCancelTestOrderByCustomerResponse: ...

class ShippingsettingsGetSupportedCarriersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsGetSupportedCarriersResponse: ...

class InventorySetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventorySetResponse: ...

class InventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventoryCustomBatchResponse: ...

class OrdersRefundResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersRefundResponse: ...

class OrdersGetTestOrderTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersGetTestOrderTemplateResponse: ...

class OrdersCancelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCancelResponse: ...

class AccountsLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsLinkResponse: ...

class AccounttaxCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccounttaxCustomBatchResponse: ...

class OrderreturnsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreturnsListResponse: ...

class ProductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductsListResponse: ...

class ProductStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductStatus: ...

class OrdersUpdateShipmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateShipmentResponse: ...

class LiaSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiaSettings: ...

class OrderinvoicesCreateRefundInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderinvoicesCreateRefundInvoiceResponse: ...

class DatafeedsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedsCustomBatchResponse: ...

class AccountsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsCustomBatchResponse: ...

class DatafeedStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedStatus: ...

class ProductsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductsCustomBatchResponse: ...

class AccountstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountstatusesListResponse: ...

class LiasettingsListPosDataProvidersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsListPosDataProvidersResponse: ...

class OrdersUpdateLineItemShippingDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateLineItemShippingDetailsResponse: ...

class PosInventoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosInventoryResponse: ...

class OrdersCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCustomBatchResponse: ...

class OrdersUpdateMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateMerchantOrderIdResponse: ...

class AccounttaxListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccounttaxListResponse: ...

class OrdersCreateTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCreateTestOrderResponse: ...
