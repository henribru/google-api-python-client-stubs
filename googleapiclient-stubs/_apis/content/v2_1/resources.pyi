import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> AccountLabelHttpRequest: ...

        @typing.type_check_only
        class ReturncarrierResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                accountId: str,
                body: AccountReturnCarrier = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            accountId: str,
            view: typing_extensions.Literal["MERCHANT", "CSS"] = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> RequestPhoneVerificationResponseHttpRequest: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: Account = ...,
            **kwargs: typing.Any,
        ) -> AccountHttpRequest: ...
        def updatelabels(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: AccountsUpdateLabelsRequest = ...,
            **kwargs: typing.Any,
        ) -> AccountsUpdateLabelsResponseHttpRequest: ...
        def verifyphonenumber(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: VerifyPhoneNumberRequest = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> AccountStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: str | _list[str] = ...,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> AccountTaxHttpRequest: ...

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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ListCollectionStatusesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCollectionStatusesResponseHttpRequest,
            previous_response: ListCollectionStatusesResponse,
        ) -> ListCollectionStatusesResponseHttpRequest | None: ...

    @typing.type_check_only
    class ConversionsourcesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, merchantId: str, body: ConversionSource = ..., **kwargs: typing.Any
        ) -> ConversionSourceHttpRequest: ...
        def delete(
            self, *, merchantId: str, conversionSourceId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, merchantId: str, conversionSourceId: str, **kwargs: typing.Any
        ) -> ConversionSourceHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any,
        ) -> ListConversionSourcesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListConversionSourcesResponseHttpRequest,
            previous_response: ListConversionSourcesResponse,
        ) -> ListConversionSourcesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            merchantId: str,
            conversionSourceId: str,
            body: ConversionSource = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ConversionSourceHttpRequest: ...
        def undelete(
            self,
            *,
            merchantId: str,
            conversionSourceId: str,
            body: UndeleteConversionSourceRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...

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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> DatafeedHttpRequest: ...

    @typing.type_check_only
    class DatafeedstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: DatafeedstatusesCustomBatchRequest = ...,
            **kwargs: typing.Any,
        ) -> DatafeedstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            datafeedId: str,
            country: str = ...,
            feedLabel: str = ...,
            language: str = ...,
            **kwargs: typing.Any,
        ) -> DatafeedStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> DatafeedstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DatafeedstatusesListResponseHttpRequest,
            previous_response: DatafeedstatusesListResponse,
        ) -> DatafeedstatusesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class FreelistingsprogramResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CheckoutsettingsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, merchantId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, merchantId: str, **kwargs: typing.Any
            ) -> CheckoutSettingsHttpRequest: ...
            def insert(
                self,
                *,
                merchantId: str,
                body: InsertCheckoutSettingsRequest = ...,
                **kwargs: typing.Any,
            ) -> CheckoutSettingsHttpRequest: ...

        def get(
            self, *, merchantId: str, **kwargs: typing.Any
        ) -> FreeListingsProgramStatusHttpRequest: ...
        def requestreview(
            self,
            *,
            merchantId: str,
            body: RequestReviewFreeListingsRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def checkoutsettings(self) -> CheckoutsettingsResource: ...

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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> LiasettingsSetInventoryVerificationContactResponseHttpRequest: ...
        def setomnichannelexperience(
            self,
            *,
            merchantId: str,
            accountId: str,
            country: str = ...,
            lsfType: str = ...,
            pickupTypes: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> LiaOmnichannelExperienceHttpRequest: ...
        def setposdataprovider(
            self,
            *,
            merchantId: str,
            accountId: str,
            country: str,
            posDataProviderId: str = ...,
            posExternalAccountId: str = ...,
            **kwargs: typing.Any,
        ) -> LiasettingsSetPosDataProviderResponseHttpRequest: ...
        def update(
            self,
            *,
            merchantId: str,
            accountId: str,
            body: LiaSettings = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> LocalInventoryHttpRequest: ...

    @typing.type_check_only
    class MerchantsupportResource(googleapiclient.discovery.Resource):
        def renderaccountissues(
            self,
            *,
            merchantId: str,
            body: RenderAccountIssuesRequestPayload = ...,
            languageCode: str = ...,
            timeZone: str = ...,
            **kwargs: typing.Any,
        ) -> RenderAccountIssuesResponseHttpRequest: ...
        def renderproductissues(
            self,
            *,
            merchantId: str,
            productId: str,
            body: RenderProductIssuesRequestPayload = ...,
            languageCode: str = ...,
            timeZone: str = ...,
            **kwargs: typing.Any,
        ) -> RenderProductIssuesResponseHttpRequest: ...
        def triggeraction(
            self,
            *,
            merchantId: str,
            body: TriggerActionPayload = ...,
            languageCode: str = ...,
            **kwargs: typing.Any,
        ) -> TriggerActionResponseHttpRequest: ...

    @typing.type_check_only
    class OrdertrackingsignalsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: OrderTrackingSignal = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            storeCode: str,
            **kwargs: typing.Any,
        ) -> PosStoreHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosStore = ...,
            **kwargs: typing.Any,
        ) -> PosStoreHttpRequest: ...
        def inventory(
            self,
            *,
            merchantId: str,
            targetMerchantId: str,
            body: PosInventoryRequest = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> PosSaleResponseHttpRequest: ...

    @typing.type_check_only
    class ProductdeliverytimeResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: ProductDeliveryTime = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ProductHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ProductHttpRequest: ...

    @typing.type_check_only
    class ProductstatusesResource(googleapiclient.discovery.Resource):
        def custombatch(
            self, *, body: ProductstatusesCustomBatchRequest = ..., **kwargs: typing.Any
        ) -> ProductstatusesCustomBatchResponseHttpRequest: ...
        def get(
            self,
            *,
            merchantId: str,
            productId: str,
            destinations: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> ProductStatusHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            destinations: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ProductstatusesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProductstatusesListResponseHttpRequest,
            previous_response: ProductstatusesListResponse,
        ) -> ProductstatusesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class PromotionsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, merchantId: str, body: Promotion = ..., **kwargs: typing.Any
        ) -> PromotionHttpRequest: ...
        def get(
            self, *, merchantId: str, id: str, **kwargs: typing.Any
        ) -> PromotionHttpRequest: ...
        def list(
            self,
            *,
            merchantId: str,
            countryCode: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListPromotionResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPromotionResponseHttpRequest,
            previous_response: ListPromotionResponse,
        ) -> ListPromotionResponseHttpRequest | None: ...

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
            **kwargs: typing.Any,
        ) -> PubsubNotificationSettingsHttpRequest: ...

    @typing.type_check_only
    class QuotasResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            merchantId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListMethodQuotasResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListMethodQuotasResponseHttpRequest,
            previous_response: ListMethodQuotasResponse,
        ) -> ListMethodQuotasResponseHttpRequest | None: ...

    @typing.type_check_only
    class RecommendationsResource(googleapiclient.discovery.Resource):
        def generate(
            self,
            *,
            merchantId: str,
            allowedTag: str | _list[str] = ...,
            languageCode: str = ...,
            **kwargs: typing.Any,
        ) -> GenerateRecommendationsResponseHttpRequest: ...
        def reportInteraction(
            self,
            *,
            merchantId: str,
            body: ReportInteractionRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class RegionalinventoryResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: RegionalinventoryCustomBatchRequest = ...,
            **kwargs: typing.Any,
        ) -> RegionalinventoryCustomBatchResponseHttpRequest: ...
        def insert(
            self,
            *,
            merchantId: str,
            productId: str,
            body: RegionalInventory = ...,
            **kwargs: typing.Any,
        ) -> RegionalInventoryHttpRequest: ...

    @typing.type_check_only
    class RegionsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            merchantId: str,
            body: Region = ...,
            regionId: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ReturnPolicyOnlineHttpRequest: ...

    @typing.type_check_only
    class ShippingsettingsResource(googleapiclient.discovery.Resource):
        def custombatch(
            self,
            *,
            body: ShippingsettingsCustomBatchRequest = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accounts(self) -> AccountsResource: ...
    def accountstatuses(self) -> AccountstatusesResource: ...
    def accounttax(self) -> AccounttaxResource: ...
    def collections(self) -> CollectionsResource: ...
    def collectionstatuses(self) -> CollectionstatusesResource: ...
    def conversionsources(self) -> ConversionsourcesResource: ...
    def csses(self) -> CssesResource: ...
    def datafeeds(self) -> DatafeedsResource: ...
    def datafeedstatuses(self) -> DatafeedstatusesResource: ...
    def freelistingsprogram(self) -> FreelistingsprogramResource: ...
    def liasettings(self) -> LiasettingsResource: ...
    def localinventory(self) -> LocalinventoryResource: ...
    def merchantsupport(self) -> MerchantsupportResource: ...
    def ordertrackingsignals(self) -> OrdertrackingsignalsResource: ...
    def pos(self) -> PosResource: ...
    def productdeliverytime(self) -> ProductdeliverytimeResource: ...
    def products(self) -> ProductsResource: ...
    def productstatuses(self) -> ProductstatusesResource: ...
    def promotions(self) -> PromotionsResource: ...
    def pubsubnotificationsettings(self) -> PubsubnotificationsettingsResource: ...
    def quotas(self) -> QuotasResource: ...
    def recommendations(self) -> RecommendationsResource: ...
    def regionalinventory(self) -> RegionalinventoryResource: ...
    def regions(self) -> RegionsResource: ...
    def reports(self) -> ReportsResource: ...
    def returnaddress(self) -> ReturnaddressResource: ...
    def returnpolicy(self) -> ReturnpolicyResource: ...
    def returnpolicyonline(self) -> ReturnpolicyonlineResource: ...
    def shippingsettings(self) -> ShippingsettingsResource: ...
    def shoppingadsprogram(self) -> ShoppingadsprogramResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Account: ...

@typing.type_check_only
class AccountCredentialsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountCredentials: ...

@typing.type_check_only
class AccountLabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountLabel: ...

@typing.type_check_only
class AccountReturnCarrierHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountReturnCarrier: ...

@typing.type_check_only
class AccountStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountStatus: ...

@typing.type_check_only
class AccountTaxHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountTax: ...

@typing.type_check_only
class AccountsAuthInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsAuthInfoResponse: ...

@typing.type_check_only
class AccountsClaimWebsiteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsClaimWebsiteResponse: ...

@typing.type_check_only
class AccountsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsCustomBatchResponse: ...

@typing.type_check_only
class AccountsLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsLinkResponse: ...

@typing.type_check_only
class AccountsListLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsListLinksResponse: ...

@typing.type_check_only
class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsListResponse: ...

@typing.type_check_only
class AccountsUpdateLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountsUpdateLabelsResponse: ...

@typing.type_check_only
class AccountstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountstatusesCustomBatchResponse: ...

@typing.type_check_only
class AccountstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountstatusesListResponse: ...

@typing.type_check_only
class AccounttaxCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccounttaxCustomBatchResponse: ...

@typing.type_check_only
class AccounttaxListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccounttaxListResponse: ...

@typing.type_check_only
class CheckoutSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckoutSettings: ...

@typing.type_check_only
class CollectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Collection: ...

@typing.type_check_only
class CollectionStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CollectionStatus: ...

@typing.type_check_only
class ConversionSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConversionSource: ...

@typing.type_check_only
class CssHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Css: ...

@typing.type_check_only
class DatafeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Datafeed: ...

@typing.type_check_only
class DatafeedStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedStatus: ...

@typing.type_check_only
class DatafeedsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedsCustomBatchResponse: ...

@typing.type_check_only
class DatafeedsFetchNowResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedsFetchNowResponse: ...

@typing.type_check_only
class DatafeedsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedsListResponse: ...

@typing.type_check_only
class DatafeedstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedstatusesCustomBatchResponse: ...

@typing.type_check_only
class DatafeedstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DatafeedstatusesListResponse: ...

@typing.type_check_only
class FreeListingsProgramStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FreeListingsProgramStatus: ...

@typing.type_check_only
class GenerateRecommendationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateRecommendationsResponse: ...

@typing.type_check_only
class LiaOmnichannelExperienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiaOmnichannelExperience: ...

@typing.type_check_only
class LiaSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiaSettings: ...

@typing.type_check_only
class LiasettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsCustomBatchResponse: ...

@typing.type_check_only
class LiasettingsGetAccessibleGmbAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsGetAccessibleGmbAccountsResponse: ...

@typing.type_check_only
class LiasettingsListPosDataProvidersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsListPosDataProvidersResponse: ...

@typing.type_check_only
class LiasettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsListResponse: ...

@typing.type_check_only
class LiasettingsRequestGmbAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsRequestGmbAccessResponse: ...

@typing.type_check_only
class LiasettingsRequestInventoryVerificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsRequestInventoryVerificationResponse: ...

@typing.type_check_only
class LiasettingsSetInventoryVerificationContactResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsSetInventoryVerificationContactResponse: ...

@typing.type_check_only
class LiasettingsSetPosDataProviderResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LiasettingsSetPosDataProviderResponse: ...

@typing.type_check_only
class ListAccountLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountLabelsResponse: ...

@typing.type_check_only
class ListAccountReturnCarrierResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountReturnCarrierResponse: ...

@typing.type_check_only
class ListCollectionStatusesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCollectionStatusesResponse: ...

@typing.type_check_only
class ListCollectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCollectionsResponse: ...

@typing.type_check_only
class ListConversionSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConversionSourcesResponse: ...

@typing.type_check_only
class ListCssesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCssesResponse: ...

@typing.type_check_only
class ListMethodQuotasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMethodQuotasResponse: ...

@typing.type_check_only
class ListPromotionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPromotionResponse: ...

@typing.type_check_only
class ListRegionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRegionsResponse: ...

@typing.type_check_only
class ListReturnPolicyOnlineResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReturnPolicyOnlineResponse: ...

@typing.type_check_only
class LocalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LocalInventory: ...

@typing.type_check_only
class LocalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LocalinventoryCustomBatchResponse: ...

@typing.type_check_only
class OrderTrackingSignalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OrderTrackingSignal: ...

@typing.type_check_only
class PosCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PosCustomBatchResponse: ...

@typing.type_check_only
class PosInventoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PosInventoryResponse: ...

@typing.type_check_only
class PosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PosListResponse: ...

@typing.type_check_only
class PosSaleResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PosSaleResponse: ...

@typing.type_check_only
class PosStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PosStore: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Product: ...

@typing.type_check_only
class ProductDeliveryTimeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductDeliveryTime: ...

@typing.type_check_only
class ProductStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductStatus: ...

@typing.type_check_only
class ProductsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductsCustomBatchResponse: ...

@typing.type_check_only
class ProductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductsListResponse: ...

@typing.type_check_only
class ProductstatusesCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductstatusesCustomBatchResponse: ...

@typing.type_check_only
class ProductstatusesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductstatusesListResponse: ...

@typing.type_check_only
class PromotionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Promotion: ...

@typing.type_check_only
class PubsubNotificationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PubsubNotificationSettings: ...

@typing.type_check_only
class RegionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Region: ...

@typing.type_check_only
class RegionalInventoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RegionalInventory: ...

@typing.type_check_only
class RegionalinventoryCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RegionalinventoryCustomBatchResponse: ...

@typing.type_check_only
class RenderAccountIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RenderAccountIssuesResponse: ...

@typing.type_check_only
class RenderProductIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RenderProductIssuesResponse: ...

@typing.type_check_only
class RequestPhoneVerificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RequestPhoneVerificationResponse: ...

@typing.type_check_only
class ReturnAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnAddress: ...

@typing.type_check_only
class ReturnPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnPolicy: ...

@typing.type_check_only
class ReturnPolicyOnlineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnPolicyOnline: ...

@typing.type_check_only
class ReturnaddressCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnaddressCustomBatchResponse: ...

@typing.type_check_only
class ReturnaddressListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnaddressListResponse: ...

@typing.type_check_only
class ReturnpolicyCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnpolicyCustomBatchResponse: ...

@typing.type_check_only
class ReturnpolicyListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReturnpolicyListResponse: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchResponse: ...

@typing.type_check_only
class ShippingSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingSettings: ...

@typing.type_check_only
class ShippingsettingsCustomBatchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingsettingsCustomBatchResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedCarriersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingsettingsGetSupportedCarriersResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedHolidaysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingsettingsGetSupportedHolidaysResponse: ...

@typing.type_check_only
class ShippingsettingsGetSupportedPickupServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingsettingsGetSupportedPickupServicesResponse: ...

@typing.type_check_only
class ShippingsettingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingsettingsListResponse: ...

@typing.type_check_only
class ShoppingAdsProgramStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShoppingAdsProgramStatus: ...

@typing.type_check_only
class TriggerActionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TriggerActionResponse: ...

@typing.type_check_only
class VerifyPhoneNumberResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyPhoneNumberResponse: ...
