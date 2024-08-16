import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> ListDeviceTierConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDeviceTierConfigsResponseHttpRequest,
                previous_response: ListDeviceTierConfigsResponse,
            ) -> ListDeviceTierConfigsResponseHttpRequest | None: ...

        def dataSafety(
            self,
            *,
            packageName: str,
            body: SafetyLabelsUpdateRequest = ...,
            **kwargs: typing.Any,
        ) -> SafetyLabelsUpdateResponseHttpRequest: ...
        def deviceTierConfigs(self) -> DeviceTierConfigsResource: ...

    @typing.type_check_only
    class ApprecoveryResource(googleapiclient.discovery.Resource):
        def addTargeting(
            self,
            *,
            packageName: str,
            appRecoveryId: str,
            body: AddTargetingRequest = ...,
            **kwargs: typing.Any,
        ) -> AddTargetingResponseHttpRequest: ...
        def cancel(
            self,
            *,
            packageName: str,
            appRecoveryId: str,
            body: CancelAppRecoveryRequest = ...,
            **kwargs: typing.Any,
        ) -> CancelAppRecoveryResponseHttpRequest: ...
        def create(
            self,
            *,
            packageName: str,
            body: CreateDraftAppRecoveryRequest = ...,
            **kwargs: typing.Any,
        ) -> AppRecoveryActionHttpRequest: ...
        def deploy(
            self,
            *,
            packageName: str,
            appRecoveryId: str,
            body: DeployAppRecoveryRequest = ...,
            **kwargs: typing.Any,
        ) -> DeployAppRecoveryResponseHttpRequest: ...
        def list(
            self, *, packageName: str, versionCode: str = ..., **kwargs: typing.Any
        ) -> ListAppRecoveriesResponseHttpRequest: ...

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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> AppDetailsHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                body: AppDetails = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> ImagesUploadResponseHttpRequest: ...

        @typing.type_check_only
        class ListingsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> ListingHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                body: Listing = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> TestersHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Testers = ...,
                **kwargs: typing.Any,
            ) -> TestersHttpRequest: ...

        @typing.type_check_only
        class TracksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                packageName: str,
                editId: str,
                body: TrackConfig = ...,
                **kwargs: typing.Any,
            ) -> TrackHttpRequest: ...
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
                **kwargs: typing.Any,
            ) -> TrackHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Track = ...,
                **kwargs: typing.Any,
            ) -> TrackHttpRequest: ...

        def commit(
            self,
            *,
            packageName: str,
            editId: str,
            changesNotSentForReview: bool = ...,
            **kwargs: typing.Any,
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
    class ExternaltransactionsResource(googleapiclient.discovery.Resource):
        def createexternaltransaction(
            self,
            *,
            parent: str,
            body: ExternalTransaction = ...,
            externalTransactionId: str = ...,
            **kwargs: typing.Any,
        ) -> ExternalTransactionHttpRequest: ...
        def getexternaltransaction(
            self, *, name: str, **kwargs: typing.Any
        ) -> ExternalTransactionHttpRequest: ...
        def refundexternaltransaction(
            self,
            *,
            name: str,
            body: RefundExternalTransactionRequest = ...,
            **kwargs: typing.Any,
        ) -> ExternalTransactionHttpRequest: ...

    @typing.type_check_only
    class GeneratedapksResource(googleapiclient.discovery.Resource):
        def download(
            self,
            *,
            packageName: str,
            versionCode: int,
            downloadId: str,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def download_media(
            self,
            *,
            packageName: str,
            versionCode: int,
            downloadId: str,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
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
            **kwargs: typing.Any,
        ) -> GrantHttpRequest: ...

    @typing.type_check_only
    class InappproductsResource(googleapiclient.discovery.Resource):
        def batchDelete(
            self,
            *,
            packageName: str,
            body: InappproductsBatchDeleteRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def batchGet(
            self, *, packageName: str, sku: str | _list[str] = ..., **kwargs: typing.Any
        ) -> InappproductsBatchGetResponseHttpRequest: ...
        def batchUpdate(
            self,
            *,
            packageName: str,
            body: InappproductsBatchUpdateRequest = ...,
            **kwargs: typing.Any,
        ) -> InappproductsBatchUpdateResponseHttpRequest: ...
        def delete(
            self,
            *,
            packageName: str,
            sku: str,
            latencyTolerance: typing_extensions.Literal[
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
            ] = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> InAppProductHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            maxResults: int = ...,
            startIndex: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> InappproductsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            latencyTolerance: typing_extensions.Literal[
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
            ] = ...,
            **kwargs: typing.Any,
        ) -> InAppProductHttpRequest: ...
        def update(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            allowMissing: bool = ...,
            autoConvertMissingPrices: bool = ...,
            latencyTolerance: typing_extensions.Literal[
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
                "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
            ] = ...,
            **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
                    ) -> SubscriptionOfferHttpRequest: ...
                    def batchGet(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        body: BatchGetSubscriptionOffersRequest = ...,
                        **kwargs: typing.Any,
                    ) -> BatchGetSubscriptionOffersResponseHttpRequest: ...
                    def batchUpdate(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        body: BatchUpdateSubscriptionOffersRequest = ...,
                        **kwargs: typing.Any,
                    ) -> BatchUpdateSubscriptionOffersResponseHttpRequest: ...
                    def batchUpdateStates(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        body: BatchUpdateSubscriptionOfferStatesRequest = ...,
                        **kwargs: typing.Any,
                    ) -> BatchUpdateSubscriptionOfferStatesResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        body: SubscriptionOffer = ...,
                        offerId: str = ...,
                        regionsVersion_version: str = ...,
                        **kwargs: typing.Any,
                    ) -> SubscriptionOfferHttpRequest: ...
                    def deactivate(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        body: DeactivateSubscriptionOfferRequest = ...,
                        **kwargs: typing.Any,
                    ) -> SubscriptionOfferHttpRequest: ...
                    def delete(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        **kwargs: typing.Any,
                    ) -> googleapiclient.http.HttpRequest: ...
                    def get(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        offerId: str,
                        **kwargs: typing.Any,
                    ) -> SubscriptionOfferHttpRequest: ...
                    def list(
                        self,
                        *,
                        packageName: str,
                        productId: str,
                        basePlanId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
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
                        allowMissing: bool = ...,
                        latencyTolerance: typing_extensions.Literal[
                            "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
                            "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
                            "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
                        ] = ...,
                        regionsVersion_version: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> SubscriptionOfferHttpRequest: ...

                def activate(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: ActivateBasePlanRequest = ...,
                    **kwargs: typing.Any,
                ) -> SubscriptionHttpRequest: ...
                def batchMigratePrices(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    body: BatchMigrateBasePlanPricesRequest = ...,
                    **kwargs: typing.Any,
                ) -> BatchMigrateBasePlanPricesResponseHttpRequest: ...
                def batchUpdateStates(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    body: BatchUpdateBasePlanStatesRequest = ...,
                    **kwargs: typing.Any,
                ) -> BatchUpdateBasePlanStatesResponseHttpRequest: ...
                def deactivate(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: DeactivateBasePlanRequest = ...,
                    **kwargs: typing.Any,
                ) -> SubscriptionHttpRequest: ...
                def delete(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    **kwargs: typing.Any,
                ) -> googleapiclient.http.HttpRequest: ...
                def migratePrices(
                    self,
                    *,
                    packageName: str,
                    productId: str,
                    basePlanId: str,
                    body: MigrateBasePlanPricesRequest = ...,
                    **kwargs: typing.Any,
                ) -> MigrateBasePlanPricesResponseHttpRequest: ...
                def offers(self) -> OffersResource: ...

            def archive(
                self,
                *,
                packageName: str,
                productId: str,
                body: ArchiveSubscriptionRequest = ...,
                **kwargs: typing.Any,
            ) -> SubscriptionHttpRequest: ...
            def batchGet(
                self,
                *,
                packageName: str,
                productIds: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> BatchGetSubscriptionsResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                packageName: str,
                body: BatchUpdateSubscriptionsRequest = ...,
                **kwargs: typing.Any,
            ) -> BatchUpdateSubscriptionsResponseHttpRequest: ...
            def create(
                self,
                *,
                packageName: str,
                body: Subscription = ...,
                productId: str = ...,
                regionsVersion_version: str = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                allowMissing: bool = ...,
                latencyTolerance: typing_extensions.Literal[
                    "PRODUCT_UPDATE_LATENCY_TOLERANCE_UNSPECIFIED",
                    "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_SENSITIVE",
                    "PRODUCT_UPDATE_LATENCY_TOLERANCE_LATENCY_TOLERANT",
                ] = ...,
                regionsVersion_version: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SubscriptionHttpRequest: ...
            def basePlans(self) -> BasePlansResource: ...

        def convertRegionPrices(
            self,
            *,
            packageName: str,
            body: ConvertRegionPricesRequest = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def consume(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def cancel(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def defer(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                body: SubscriptionPurchasesDeferRequest = ...,
                **kwargs: typing.Any,
            ) -> SubscriptionPurchasesDeferResponseHttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any,
            ) -> SubscriptionPurchaseHttpRequest: ...
            def refund(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def revoke(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...

        @typing.type_check_only
        class Subscriptionsv2Resource(googleapiclient.discovery.Resource):
            def get(
                self, *, packageName: str, token: str, **kwargs: typing.Any
            ) -> SubscriptionPurchaseV2HttpRequest: ...
            def revoke(
                self,
                *,
                packageName: str,
                token: str,
                body: RevokeSubscriptionPurchaseRequest = ...,
                **kwargs: typing.Any,
            ) -> RevokeSubscriptionPurchaseResponseHttpRequest: ...

        @typing.type_check_only
        class VoidedpurchasesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                packageName: str,
                endTime: str = ...,
                includeQuantityBasedPartialRefund: bool = ...,
                maxResults: int = ...,
                startIndex: int = ...,
                startTime: str = ...,
                token: str = ...,
                type: int = ...,
                **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ReviewHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            maxResults: int = ...,
            startIndex: int = ...,
            token: str = ...,
            translationLanguage: str = ...,
            **kwargs: typing.Any,
        ) -> ReviewsListResponseHttpRequest: ...
        def reply(
            self,
            *,
            packageName: str,
            reviewId: str,
            body: ReviewsReplyRequest = ...,
            **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> VariantHttpRequest: ...
            def download(
                self,
                *,
                packageName: str,
                versionCode: str,
                variantId: int,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def download_media(
                self,
                *,
                packageName: str,
                versionCode: str,
                variantId: int,
                **kwargs: typing.Any,
            ) -> BytesHttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                versionCode: str,
                variantId: int,
                **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def applications(self) -> ApplicationsResource: ...
    def apprecovery(self) -> ApprecoveryResource: ...
    def edits(self) -> EditsResource: ...
    def externaltransactions(self) -> ExternaltransactionsResource: ...
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
class AddTargetingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddTargetingResponse: ...

@typing.type_check_only
class ApkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Apk: ...

@typing.type_check_only
class ApksAddExternallyHostedResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ApksAddExternallyHostedResponse: ...

@typing.type_check_only
class ApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ApksListResponse: ...

@typing.type_check_only
class AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppDetails: ...

@typing.type_check_only
class AppEditHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppEdit: ...

@typing.type_check_only
class AppRecoveryActionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppRecoveryAction: ...

@typing.type_check_only
class BatchGetSubscriptionOffersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetSubscriptionOffersResponse: ...

@typing.type_check_only
class BatchGetSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetSubscriptionsResponse: ...

@typing.type_check_only
class BatchMigrateBasePlanPricesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchMigrateBasePlanPricesResponse: ...

@typing.type_check_only
class BatchUpdateBasePlanStatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateBasePlanStatesResponse: ...

@typing.type_check_only
class BatchUpdateSubscriptionOfferStatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateSubscriptionOfferStatesResponse: ...

@typing.type_check_only
class BatchUpdateSubscriptionOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateSubscriptionOffersResponse: ...

@typing.type_check_only
class BatchUpdateSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateSubscriptionsResponse: ...

@typing.type_check_only
class BundleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Bundle: ...

@typing.type_check_only
class BundlesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BundlesListResponse: ...

@typing.type_check_only
class CancelAppRecoveryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelAppRecoveryResponse: ...

@typing.type_check_only
class ConvertRegionPricesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConvertRegionPricesResponse: ...

@typing.type_check_only
class DeobfuscationFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeobfuscationFilesUploadResponse: ...

@typing.type_check_only
class DeployAppRecoveryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeployAppRecoveryResponse: ...

@typing.type_check_only
class DeviceTierConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeviceTierConfig: ...

@typing.type_check_only
class ExpansionFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExpansionFile: ...

@typing.type_check_only
class ExpansionFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExpansionFilesUploadResponse: ...

@typing.type_check_only
class ExternalTransactionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExternalTransaction: ...

@typing.type_check_only
class GeneratedApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GeneratedApksListResponse: ...

@typing.type_check_only
class GrantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Grant: ...

@typing.type_check_only
class ImagesDeleteAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImagesDeleteAllResponse: ...

@typing.type_check_only
class ImagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImagesListResponse: ...

@typing.type_check_only
class ImagesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ImagesUploadResponse: ...

@typing.type_check_only
class InAppProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InAppProduct: ...

@typing.type_check_only
class InappproductsBatchGetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InappproductsBatchGetResponse: ...

@typing.type_check_only
class InappproductsBatchUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InappproductsBatchUpdateResponse: ...

@typing.type_check_only
class InappproductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InappproductsListResponse: ...

@typing.type_check_only
class InternalAppSharingArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InternalAppSharingArtifact: ...

@typing.type_check_only
class ListAppRecoveriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAppRecoveriesResponse: ...

@typing.type_check_only
class ListDeviceTierConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeviceTierConfigsResponse: ...

@typing.type_check_only
class ListSubscriptionOffersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubscriptionOffersResponse: ...

@typing.type_check_only
class ListSubscriptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubscriptionsResponse: ...

@typing.type_check_only
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUsersResponse: ...

@typing.type_check_only
class ListingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Listing: ...

@typing.type_check_only
class ListingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListingsListResponse: ...

@typing.type_check_only
class MigrateBasePlanPricesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MigrateBasePlanPricesResponse: ...

@typing.type_check_only
class ProductPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProductPurchase: ...

@typing.type_check_only
class ReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Review: ...

@typing.type_check_only
class ReviewsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReviewsListResponse: ...

@typing.type_check_only
class ReviewsReplyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReviewsReplyResponse: ...

@typing.type_check_only
class RevokeSubscriptionPurchaseResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RevokeSubscriptionPurchaseResponse: ...

@typing.type_check_only
class SafetyLabelsUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SafetyLabelsUpdateResponse: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...

@typing.type_check_only
class SubscriptionOfferHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionOffer: ...

@typing.type_check_only
class SubscriptionPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionPurchase: ...

@typing.type_check_only
class SubscriptionPurchaseV2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionPurchaseV2: ...

@typing.type_check_only
class SubscriptionPurchasesDeferResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SubscriptionPurchasesDeferResponse: ...

@typing.type_check_only
class SystemApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SystemApksListResponse: ...

@typing.type_check_only
class TestersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Testers: ...

@typing.type_check_only
class TrackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Track: ...

@typing.type_check_only
class TrackCountryAvailabilityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TrackCountryAvailability: ...

@typing.type_check_only
class TracksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TracksListResponse: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...

@typing.type_check_only
class VariantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Variant: ...

@typing.type_check_only
class VoidedPurchasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VoidedPurchasesListResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
