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
            view: typing_extensions.Literal["css", "merchant"] = ...,
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
            pageToken: str = ...,
            view: typing_extensions.Literal["css", "merchant"] = ...,
            **kwargs: typing.Any
        ) -> AccountsListResponseHttpRequest: ...
        def listlinks(
            self,
            *,
            merchantId: str,
            accountId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> AccountsListLinksResponseHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountTax = ...,
            **kwargs: typing.Any
        ) -> AccountTaxHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            body: Datafeed = ...,
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
            **kwargs: typing.Any
        ) -> LiaSettingsHttpRequest: ...
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
        def acknowledge(
            self,
            *,
            merchantId: str,
            returnId: str,
            body: OrderreturnsAcknowledgeRequest = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsAcknowledgeResponseHttpRequest: ...
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
            googleOrderIds: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal[
                "returnCreationTimeAsc", "returnCreationTimeDesc"
            ] = ...,
            pageToken: str = ...,
            shipmentStates: typing.Union[
                typing_extensions.Literal[
                    "completed", "new", "pending", "shipped", "undeliverable"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "completed", "new", "pending", "shipped", "undeliverable"
                    ]
                ],
            ] = ...,
            shipmentStatus: typing.Union[
                typing_extensions.Literal["inProgress", "new", "processed"],
                typing.List[
                    typing_extensions.Literal["inProgress", "new", "processed"]
                ],
            ] = ...,
            shipmentTrackingNumbers: typing.Union[str, typing.List[str]] = ...,
            shipmentTypes: typing.Union[
                typing_extensions.Literal[
                    "byMail", "contactCustomerSupport", "returnless"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "byMail", "contactCustomerSupport", "returnless"
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsListResponseHttpRequest: ...
        def process(
            self,
            *,
            merchantId: str,
            returnId: str,
            body: OrderreturnsProcessRequest = ...,
            **kwargs: typing.Any
        ) -> OrderreturnsProcessResponseHttpRequest: ...
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
                "template1",
                "template1a",
                "template1b",
                "template2",
                "template3",
                "template4",
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
    class ProductstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: ProductstatusesCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ProductstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            productId: str,
            destinations: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> ProductStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ProductstatusesListResponseHttpRequest: ...
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
    class SettlementtransactionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            merchantId: str,
            settlementId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            transactionIds: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> SettlementtransactionsListResponseHttpRequest: ...
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
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: ShippingSettings = ...,
            **kwargs: typing.Any
        ) -> ShippingSettingsHttpRequest: ...
    def accounts(self) -> AccountsResource: ...
    def accountstatuses(self) -> AccountstatusesResource: ...
    def accounttax(self) -> AccounttaxResource: ...
    def datafeeds(self) -> DatafeedsResource: ...
    def datafeedstatuses(self) -> DatafeedstatusesResource: ...
    def liasettings(self) -> LiasettingsResource: ...
    def localinventory(self) -> LocalinventoryResource: ...
    def orderinvoices(self) -> OrderinvoicesResource: ...
    def orderreports(self) -> OrderreportsResource: ...
    def orderreturns(self) -> OrderreturnsResource: ...
    def orders(self) -> OrdersResource: ...
    def pos(self) -> PosResource: ...
    def products(self) -> ProductsResource: ...
    def productstatuses(self) -> ProductstatusesResource: ...
    def pubsubnotificationsettings(self) -> PubsubnotificationsettingsResource: ...
    def regionalinventory(self) -> RegionalinventoryResource: ...
    def returnaddress(self) -> ReturnaddressResource: ...
    def returnpolicy(self) -> ReturnpolicyResource: ...
    def settlementreports(self) -> SettlementreportsResource: ...
    def settlementtransactions(self) -> SettlementtransactionsResource: ...
    def shippingsettings(self) -> ShippingsettingsResource: ...

class LiasettingsRequestGmbAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsRequestGmbAccessResponse: ...

class ReturnpolicyListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnpolicyListResponse: ...

class OrdersShipLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersShipLineItemsResponse: ...

class PosSaleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosSaleResponse: ...

class OrdersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersListResponse: ...

class OrdersInStoreRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersInStoreRefundLineItemResponse: ...

class OrdersGetByMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersGetByMerchantOrderIdResponse: ...

class RegionalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionalinventoryCustomBatchResponse: ...

class ShippingsettingsGetSupportedHolidaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsGetSupportedHolidaysResponse: ...

class DatafeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Datafeed: ...

class AccountTaxHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountTax: ...

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

class OrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Order: ...

class DatafeedstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedstatusesListResponse: ...

class RegionalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionalInventory: ...

class ReturnAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnAddress: ...

class AccountsListLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsListLinksResponse: ...

class OrdersAdvanceTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersAdvanceTestOrderResponse: ...

class ShippingsettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingsettingsListResponse: ...

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

class SettlementreportsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SettlementreportsListResponse: ...

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

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class OrdersRefundItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersRefundItemResponse: ...

class AccountsUpdateLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsUpdateLabelsResponse: ...

class OrdersCancelResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCancelResponse: ...

class OrderreturnsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreturnsListResponse: ...

class OrdersUpdateShipmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateShipmentResponse: ...

class ReturnpolicyCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnpolicyCustomBatchResponse: ...

class OrderinvoicesCreateRefundInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderinvoicesCreateRefundInvoiceResponse: ...

class DatafeedStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedStatus: ...

class LocalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LocalInventory: ...

class ProductsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductsCustomBatchResponse: ...

class LiasettingsListPosDataProvidersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsListPosDataProvidersResponse: ...

class PosInventoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosInventoryResponse: ...

class SettlementReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SettlementReport: ...

class OrdersUpdateMerchantOrderIdResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateMerchantOrderIdResponse: ...

class OrdersRefundOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersRefundOrderResponse: ...

class AccountsAuthInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsAuthInfoResponse: ...

class OrderreturnsProcessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreturnsProcessResponse: ...

class PosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PosListResponse: ...

class SettlementtransactionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SettlementtransactionsListResponse: ...

class OrderinvoicesCreateChargeInvoiceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderinvoicesCreateChargeInvoiceResponse: ...

class OrdersReturnRefundLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersReturnRefundLineItemResponse: ...

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

class DatafeedsFetchNowResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedsFetchNowResponse: ...

class ReturnPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnPolicy: ...

class OrdersCancelLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCancelLineItemResponse: ...

class LiasettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsCustomBatchResponse: ...

class OrdersAcknowledgeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersAcknowledgeResponse: ...

class ReturnaddressListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnaddressListResponse: ...

class LiasettingsRequestInventoryVerificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiasettingsRequestInventoryVerificationResponse: ...

class OrderreportsListTransactionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreportsListTransactionsResponse: ...

class AccountstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountstatusesCustomBatchResponse: ...

class OrderreturnsAcknowledgeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderreturnsAcknowledgeResponse: ...

class PubsubNotificationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PubsubNotificationSettings: ...

class LocalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LocalinventoryCustomBatchResponse: ...

class ProductstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductstatusesListResponse: ...

class OrdersSetLineItemMetadataResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersSetLineItemMetadataResponse: ...

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

class ShippingSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShippingSettings: ...

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

class AccountsLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsLinkResponse: ...

class AccounttaxCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccounttaxCustomBatchResponse: ...

class ProductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductsListResponse: ...

class ProductStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductStatus: ...

class LiaSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LiaSettings: ...

class DatafeedsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DatafeedsCustomBatchResponse: ...

class AccountsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsCustomBatchResponse: ...

class AccountstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountstatusesListResponse: ...

class OrdersUpdateLineItemShippingDetailsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersUpdateLineItemShippingDetailsResponse: ...

class ReturnaddressCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReturnaddressCustomBatchResponse: ...

class OrdersGetTestOrderTemplateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersGetTestOrderTemplateResponse: ...

class AccounttaxListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccounttaxListResponse: ...

class OrdersCreateTestOrderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersCreateTestOrderResponse: ...
