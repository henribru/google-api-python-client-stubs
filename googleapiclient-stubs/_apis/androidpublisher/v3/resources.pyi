import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AndroidPublisherResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApplicationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeviceTierConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                packageName: str,
                body: DeviceTierConfig = ...,
                allowUnknownDevices: bool = ...,
                **kwargs: typing.Any
            ) -> DeviceTierConfigHttpRequest: ...
            def get(
                self, *, packageName: str, deviceTierConfigId: str, **kwargs: typing.Any
            ) -> DeviceTierConfigHttpRequest: ...
            def list(
                self,
                *,
                packageName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDeviceTierConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDeviceTierConfigsResponseHttpRequest,
                previous_response: ListDeviceTierConfigsResponse,
            ) -> ListDeviceTierConfigsResponseHttpRequest | None: ...

        def deviceTierConfigs(self) -> DeviceTierConfigsResource: ...

    @typing.type_check_only
    class EditsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ApksResource(googleapiclient.discovery.Resource):
            def addexternallyhosted(
                self,
                *,
                packageName: str,
                editId: str,
                body: ApksAddExternallyHostedRequest = ...,
                **kwargs: typing.Any
            ) -> ApksAddExternallyHostedResponseHttpRequest: ...
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> ApksListResponseHttpRequest: ...
            def upload(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> ApkHttpRequest: ...

        @typing.type_check_only
        class BundlesResource(googleapiclient.discovery.Resource):
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> BundlesListResponseHttpRequest: ...
            def upload(
                self,
                *,
                packageName: str,
                editId: str,
                ackBundleInstallationWarning: bool = ...,
                deviceTierConfigId: str = ...,
                **kwargs: typing.Any
            ) -> BundleHttpRequest: ...

        @typing.type_check_only
        class CountryavailabilityResource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, editId: str, track: str, **kwargs: typing.Any
            ) -> TrackCountryAvailabilityHttpRequest: ...

        @typing.type_check_only
        class DeobfuscationfilesResource(googleapiclient.discovery.Resource):
            def upload(
                self,
                *,
                packageName: str,
                editId: str,
                apkVersionCode: int,
                deobfuscationFileType: typing_extensions.Literal[
                    "deobfuscationFileTypeUnspecified", "proguard", "nativeCode"
                ],
                **kwargs: typing.Any
            ) -> DeobfuscationFilesUploadResponseHttpRequest: ...

        @typing.type_check_only
        class DetailsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> AppDetailsHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                body: AppDetails = ...,
                **kwargs: typing.Any
            ) -> AppDetailsHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                body: AppDetails = ...,
                **kwargs: typing.Any
            ) -> AppDetailsHttpRequest: ...

        @typing.type_check_only
        class ExpansionfilesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                packageName: str,
                editId: str,
                apkVersionCode: int,
                expansionFileType: typing_extensions.Literal[
                    "expansionFileTypeUnspecified", "main", "patch"
                ],
                **kwargs: typing.Any
            ) -> ExpansionFileHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                apkVersionCode: int,
                expansionFileType: typing_extensions.Literal[
                    "expansionFileTypeUnspecified", "main", "patch"
                ],
                body: ExpansionFile = ...,
                **kwargs: typing.Any
            ) -> ExpansionFileHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                apkVersionCode: int,
                expansionFileType: typing_extensions.Literal[
                    "expansionFileTypeUnspecified", "main", "patch"
                ],
                body: ExpansionFile = ...,
                **kwargs: typing.Any
            ) -> ExpansionFileHttpRequest: ...
            def upload(
                self,
                *,
                packageName: str,
                editId: str,
                apkVersionCode: int,
                expansionFileType: typing_extensions.Literal[
                    "expansionFileTypeUnspecified", "main", "patch"
                ],
                **kwargs: typing.Any
            ) -> ExpansionFilesUploadResponseHttpRequest: ...

        @typing.type_check_only
        class ImagesResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                imageType: typing_extensions.Literal[
                    "appImageTypeUnspecified",
                    "phoneScreenshots",
                    "sevenInchScreenshots",
                    "tenInchScreenshots",
                    "tvScreenshots",
                    "wearScreenshots",
                    "icon",
                    "featureGraphic",
                    "tvBanner",
                ],
                imageId: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def deleteall(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                imageType: typing_extensions.Literal[
                    "appImageTypeUnspecified",
                    "phoneScreenshots",
                    "sevenInchScreenshots",
                    "tenInchScreenshots",
                    "tvScreenshots",
                    "wearScreenshots",
                    "icon",
                    "featureGraphic",
                    "tvBanner",
                ],
                **kwargs: typing.Any
            ) -> ImagesDeleteAllResponseHttpRequest: ...
            def list(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                imageType: typing_extensions.Literal[
                    "appImageTypeUnspecified",
                    "phoneScreenshots",
                    "sevenInchScreenshots",
                    "tenInchScreenshots",
                    "tvScreenshots",
                    "wearScreenshots",
                    "icon",
                    "featureGraphic",
                    "tvBanner",
                ],
                **kwargs: typing.Any
            ) -> ImagesListResponseHttpRequest: ...
            def upload(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                imageType: typing_extensions.Literal[
                    "appImageTypeUnspecified",
                    "phoneScreenshots",
                    "sevenInchScreenshots",
                    "tenInchScreenshots",
                    "tvScreenshots",
                    "wearScreenshots",
                    "icon",
                    "featureGraphic",
                    "tvBanner",
                ],
                **kwargs: typing.Any
            ) -> ImagesUploadResponseHttpRequest: ...

        @typing.type_check_only
        class ListingsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def deleteall(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> ListingsListResponseHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                body: Listing = ...,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                body: Listing = ...,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...

        @typing.type_check_only
        class TestersResource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, editId: str, track: str, **kwargs: typing.Any
            ) -> TestersHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Testers = ...,
                **kwargs: typing.Any
            ) -> TestersHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Testers = ...,
                **kwargs: typing.Any
            ) -> TestersHttpRequest: ...

        @typing.type_check_only
        class TracksResource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, editId: str, track: str, **kwargs: typing.Any
            ) -> TrackHttpRequest: ...
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> TracksListResponseHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Track = ...,
                **kwargs: typing.Any
            ) -> TrackHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Track = ...,
                **kwargs: typing.Any
            ) -> TrackHttpRequest: ...

        def commit(
            self,
            *,
            packageName: str,
            editId: str,
            changesNotSentForReview: bool = ...,
            **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def delete(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def insert(
            self, *, packageName: str, body: AppEdit = ..., **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def validate(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def apks(self) -> ApksResource: ...
        def bundles(self) -> BundlesResource: ...
        def countryavailability(self) -> CountryavailabilityResource: ...
        def deobfuscationfiles(self) -> DeobfuscationfilesResource: ...
        def details(self) -> DetailsResource: ...
        def expansionfiles(self) -> ExpansionfilesResource: ...
        def images(self) -> ImagesResource: ...
        def listings(self) -> ListingsResource: ...
        def testers(self) -> TestersResource: ...
        def tracks(self) -> TracksResource: ...

    @typing.type_check_only
    class GeneratedapksResource(googleapiclient.discovery.Resource):
        def download(
            self,
            *,
            packageName: str,
            versionCode: int,
            downloadId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self, *, packageName: str, versionCode: int, **kwargs: typing.Any
        ) -> GeneratedApksListResponseHttpRequest: ...

    @typing.type_check_only
    class GrantsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, parent: str, body: Grant = ..., **kwargs: typing.Any
        ) -> GrantHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Grant = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GrantHttpRequest: ...

    @typing.type_check_only
    class InappproductsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, packageName: str, sku: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, packageName: str, sku: str, **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def insert(
            self,
            *,
            packageName: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            maxResults: int = ...,
            startIndex: int = ...,
            token: str = ...,
            **kwargs: typing.Any
        ) -> InappproductsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def update(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            allowMissing: bool = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...

    @typing.type_check_only
    class InternalappsharingartifactsResource(googleapiclient.discovery.Resource):
        def uploadapk(
            self, *, packageName: str, **kwargs: typing.Any
        ) -> InternalAppSharingArtifactHttpRequest: ...
        def uploadbundle(
            self, *, packageName: str, **kwargs: typing.Any
        ) -> InternalAppSharingArtifactHttpRequest: ...

    @typing.type_check_only
    class MonetizationResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BasePlansResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OffersResource(googleapiclient.discovery.Resource):
                    def activate(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        body: ActivateSubscriptionOfferRequest = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionOfferHttpRequest: ...
                    def create(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        body: SubscriptionOffer = ...,
                        offerId: str = ...,
                        regionsVersion_version: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionOfferHttpRequest: ...
                    def deactivate(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        body: DeactivateSubscriptionOfferRequest = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionOfferHttpRequest: ...
                    def delete(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        **kwargs: typing.Any
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        **kwargs: typing.Any
                    ) -> SubscriptionOfferHttpRequest: ...
                    def list(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListSubscriptionOffersResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSubscriptionOffersResponseHttpRequest,
                        previous_response: ListSubscriptionOffersResponse,
                    ) -> ListSubscriptionOffersResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        body: SubscriptionOffer = ...,
                        regionsVersion_version: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> SubscriptionOfferHttpRequest: ...

                def activate(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: ActivateBasePlanRequest = ...,
                    **kwargs: typing.Any
                ) -> SubscriptionHttpRequest: ...
                def deactivate(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: DeactivateBasePlanRequest = ...,
                    **kwargs: typing.Any
                ) -> SubscriptionHttpRequest: ...
                def delete(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def migratePrices(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: MigrateBasePlanPricesRequest = ...,
                    **kwargs: typing.Any
                ) -> MigrateBasePlanPricesResponseHttpRequest: ...
                def offers(self) -> OffersResource: ...

            def archive(
                self,
                *,
                packageName: str,
                productId: str,
                body: ArchiveSubscriptionRequest = ...,
                **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def create(
                self,
                *,
                packageName: str,
                body: Subscription = ...,
                productId: str = ...,
                regionsVersion_version: str = ...,
                **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def delete(
                self, *, packageName: str, productId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, packageName: str, productId: str, **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def list(
                self,
                *,
                packageName: str,
                pageSize: int = ...,
                pageToken: str = ...,
                showArchived: bool = ...,
                **kwargs: typing.Any
            ) -> ListSubscriptionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSubscriptionsResponseHttpRequest,
                previous_response: ListSubscriptionsResponse,
            ) -> ListSubscriptionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                packageName: str,
                productId: str,
                body: Subscription = ...,
                regionsVersion_version: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SubscriptionHttpRequest: ...
            def basePlans(self) -> BasePlansResource: ...

        def convertRegionPrices(
            self,
            *,
            packageName: str,
            body: ConvertRegionPricesRequest = ...,
            **kwargs: typing.Any
        ) -> ConvertRegionPricesResponseHttpRequest: ...
        def subscriptions(self) -> SubscriptionsResource: ...

    @typing.type_check_only
    class OrdersResource(googleapiclient.discovery.Resource):
        def refund(
            self,
            *,
            packageName: str,
            orderId: str,
            revoke: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class PurchasesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProductsResource(googleapiclient.discovery.Resource):
            def acknowledge(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                body: ProductPurchasesAcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                **kwargs: typing.Any
            ) -> ProductPurchaseHttpRequest: ...

        @typing.type_check_only
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def acknowledge(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                body: SubscriptionPurchasesAcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def cancel(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def defer(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                body: SubscriptionPurchasesDeferRequest = ...,
                **kwargs: typing.Any
            ) -> SubscriptionPurchasesDeferResponseHttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> SubscriptionPurchaseHttpRequest: ...
            def refund(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def revoke(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...

        @typing.type_check_only
        class Subscriptionsv2Resource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, token: str, **kwargs: typing.Any
            ) -> SubscriptionPurchaseV2HttpRequest: ...

        @typing.type_check_only
        class VoidedpurchasesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                packageName: str,
                endTime: str = ...,
                maxResults: int = ...,
                startIndex: int = ...,
                startTime: str = ...,
                token: str = ...,
                type: int = ...,
                **kwargs: typing.Any
            ) -> VoidedPurchasesListResponseHttpRequest: ...

        def products(self) -> ProductsResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
        def subscriptionsv2(self) -> Subscriptionsv2Resource: ...
        def voidedpurchases(self) -> VoidedpurchasesResource: ...

    @typing.type_check_only
    class ReviewsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            packageName: str,
            reviewId: str,
            translationLanguage: str = ...,
            **kwargs: typing.Any
        ) -> ReviewHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            maxResults: int = ...,
            startIndex: int = ...,
            token: str = ...,
            translationLanguage: str = ...,
            **kwargs: typing.Any
        ) -> ReviewsListResponseHttpRequest: ...
        def reply(
            self,
            *,
            packageName: str,
            reviewId: str,
            body: ReviewsReplyRequest = ...,
            **kwargs: typing.Any
        ) -> ReviewsReplyResponseHttpRequest: ...

    @typing.type_check_only
    class SystemapksResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class VariantsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                packageName: str,
                versionCode: str,
                body: Variant = ...,
                **kwargs: typing.Any
            ) -> VariantHttpRequest: ...
            def download(
                self,
                *,
                packageName: str,
                versionCode: str,
                variantId: int,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                versionCode: str,
                variantId: int,
                **kwargs: typing.Any
            ) -> VariantHttpRequest: ...
            def list(
                self, *, packageName: str, versionCode: str, **kwargs: typing.Any
            ) -> SystemApksListResponseHttpRequest: ...

        def variants(self) -> VariantsResource: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def create(
            self, *, parent: str, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListUsersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListUsersResponseHttpRequest,
            previous_response: ListUsersResponse,
        ) -> ListUsersResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: User = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> UserHttpRequest: ...

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
    def applications(self) -> ApplicationsResource: ...
    def edits(self) -> EditsResource: ...
    def generatedapks(self) -> GeneratedapksResource: ...
    def grants(self) -> GrantsResource: ...
    def inappproducts(self) -> InappproductsResource: ...
    def internalappsharingartifacts(self) -> InternalappsharingartifactsResource: ...
    def monetization(self) -> MonetizationResource: ...
    def orders(self) -> OrdersResource: ...
    def purchases(self) -> PurchasesResource: ...
    def reviews(self) -> ReviewsResource: ...
    def systemapks(self) -> SystemapksResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class ApkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Apk: ...

@typing.type_check_only
class ApksAddExternallyHostedResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApksAddExternallyHostedResponse: ...

@typing.type_check_only
class ApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApksListResponse: ...

@typing.type_check_only
class AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppDetails: ...

@typing.type_check_only
class AppEditHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppEdit: ...

@typing.type_check_only
class BundleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Bundle: ...

@typing.type_check_only
class BundlesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BundlesListResponse: ...

@typing.type_check_only
class ConvertRegionPricesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConvertRegionPricesResponse: ...

@typing.type_check_only
class DeobfuscationFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeobfuscationFilesUploadResponse: ...

@typing.type_check_only
class DeviceTierConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeviceTierConfig: ...

@typing.type_check_only
class ExpansionFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExpansionFile: ...

@typing.type_check_only
class ExpansionFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExpansionFilesUploadResponse: ...

@typing.type_check_only
class GeneratedApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GeneratedApksListResponse: ...

@typing.type_check_only
class GrantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Grant: ...

@typing.type_check_only
class ImagesDeleteAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImagesDeleteAllResponse: ...

@typing.type_check_only
class ImagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImagesListResponse: ...

@typing.type_check_only
class ImagesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImagesUploadResponse: ...

@typing.type_check_only
class InAppProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InAppProduct: ...

@typing.type_check_only
class InappproductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InappproductsListResponse: ...

@typing.type_check_only
class InternalAppSharingArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InternalAppSharingArtifact: ...

@typing.type_check_only
class ListDeviceTierConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDeviceTierConfigsResponse: ...

@typing.type_check_only
class ListSubscriptionOffersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSubscriptionOffersResponse: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUsersResponse: ...

@typing.type_check_only
class ListingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Listing: ...

@typing.type_check_only
class ListingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListingsListResponse: ...

@typing.type_check_only
class MigrateBasePlanPricesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MigrateBasePlanPricesResponse: ...

@typing.type_check_only
class ProductPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductPurchase: ...

@typing.type_check_only
class ReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Review: ...

@typing.type_check_only
class ReviewsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReviewsListResponse: ...

@typing.type_check_only
class ReviewsReplyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReviewsReplyResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionOfferHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubscriptionOffer: ...

@typing.type_check_only
class SubscriptionPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubscriptionPurchase: ...

@typing.type_check_only
class SubscriptionPurchaseV2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubscriptionPurchaseV2: ...

@typing.type_check_only
class SubscriptionPurchasesDeferResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubscriptionPurchasesDeferResponse: ...

@typing.type_check_only
class SystemApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SystemApksListResponse: ...

@typing.type_check_only
class TestersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Testers: ...

@typing.type_check_only
class TrackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Track: ...

@typing.type_check_only
class TrackCountryAvailabilityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TrackCountryAvailability: ...

@typing.type_check_only
class TracksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TracksListResponse: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> User: ...

@typing.type_check_only
class VariantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Variant: ...

@typing.type_check_only
class VoidedPurchasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VoidedPurchasesListResponse: ...
