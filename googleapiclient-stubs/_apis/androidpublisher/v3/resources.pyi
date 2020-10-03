import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AndroidPublisherResource(googleapiclient.discovery.Resource):
    class InternalappsharingartifactsResource(googleapiclient.discovery.Resource):
        def uploadbundle(
            self, *, packageName: str, **kwargs: typing.Any
        ) -> InternalAppSharingArtifactHttpRequest: ...
        def uploadapk(
            self, *, packageName: str, **kwargs: typing.Any
        ) -> InternalAppSharingArtifactHttpRequest: ...
    class ReviewsResource(googleapiclient.discovery.Resource):
        def reply(
            self,
            *,
            packageName: str,
            reviewId: str,
            body: ReviewsReplyRequest = ...,
            **kwargs: typing.Any
        ) -> ReviewsReplyResponseHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            translationLanguage: str = ...,
            startIndex: int = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any
        ) -> ReviewsListResponseHttpRequest: ...
        def get(
            self,
            *,
            packageName: str,
            reviewId: str,
            translationLanguage: str = ...,
            **kwargs: typing.Any
        ) -> ReviewHttpRequest: ...
    class EditsResource(googleapiclient.discovery.Resource):
        class ExpansionfilesResource(googleapiclient.discovery.Resource):
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
        class ApksResource(googleapiclient.discovery.Resource):
            def upload(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> ApkHttpRequest: ...
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
        class TestersResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Testers = ...,
                **kwargs: typing.Any
            ) -> TestersHttpRequest: ...
            def get(
                self, *, packageName: str, editId: str, track: str, **kwargs: typing.Any
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
        class TracksResource(googleapiclient.discovery.Resource):
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> TracksListResponseHttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Track = ...,
                **kwargs: typing.Any
            ) -> TrackHttpRequest: ...
            def get(
                self, *, packageName: str, editId: str, track: str, **kwargs: typing.Any
            ) -> TrackHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                track: str,
                body: Track = ...,
                **kwargs: typing.Any
            ) -> TrackHttpRequest: ...
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
        class ListingsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> ListingsListResponseHttpRequest: ...
            def deleteall(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def update(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                body: Listing = ...,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...
            def patch(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                body: Listing = ...,
                **kwargs: typing.Any
            ) -> ListingHttpRequest: ...
            def delete(
                self,
                *,
                packageName: str,
                editId: str,
                language: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
        class ImagesResource(googleapiclient.discovery.Resource):
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
        class BundlesResource(googleapiclient.discovery.Resource):
            def upload(
                self,
                *,
                packageName: str,
                editId: str,
                ackBundleInstallationWarning: bool = ...,
                **kwargs: typing.Any
            ) -> BundleHttpRequest: ...
            def list(
                self, *, packageName: str, editId: str, **kwargs: typing.Any
            ) -> BundlesListResponseHttpRequest: ...
        def commit(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def insert(
            self, *, packageName: str, body: AppEdit = ..., **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def delete(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def validate(
            self, *, packageName: str, editId: str, **kwargs: typing.Any
        ) -> AppEditHttpRequest: ...
        def expansionfiles(self) -> ExpansionfilesResource: ...
        def apks(self) -> ApksResource: ...
        def details(self) -> DetailsResource: ...
        def testers(self) -> TestersResource: ...
        def tracks(self) -> TracksResource: ...
        def deobfuscationfiles(self) -> DeobfuscationfilesResource: ...
        def listings(self) -> ListingsResource: ...
        def images(self) -> ImagesResource: ...
        def bundles(self) -> BundlesResource: ...
    class PurchasesResource(googleapiclient.discovery.Resource):
        class VoidedpurchasesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                packageName: str,
                maxResults: int = ...,
                endTime: str = ...,
                startTime: str = ...,
                startIndex: int = ...,
                token: str = ...,
                type: int = ...,
                **kwargs: typing.Any
            ) -> VoidedPurchasesListResponseHttpRequest: ...
        class SubscriptionsResource(googleapiclient.discovery.Resource):
            def refund(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> SubscriptionPurchaseHttpRequest: ...
            def defer(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                body: SubscriptionPurchasesDeferRequest = ...,
                **kwargs: typing.Any
            ) -> SubscriptionPurchasesDeferResponseHttpRequest: ...
            def acknowledge(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                body: SubscriptionPurchasesAcknowledgeRequest = ...,
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
            def cancel(
                self,
                *,
                packageName: str,
                subscriptionId: str,
                token: str,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
        class ProductsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                **kwargs: typing.Any
            ) -> ProductPurchaseHttpRequest: ...
            def acknowledge(
                self,
                *,
                packageName: str,
                productId: str,
                token: str,
                body: ProductPurchasesAcknowledgeRequest = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
        def voidedpurchases(self) -> VoidedpurchasesResource: ...
        def subscriptions(self) -> SubscriptionsResource: ...
        def products(self) -> ProductsResource: ...
    class OrdersResource(googleapiclient.discovery.Resource):
        def refund(
            self,
            *,
            packageName: str,
            orderId: str,
            revoke: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class SystemapksResource(googleapiclient.discovery.Resource):
        class VariantsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, packageName: str, versionCode: str, **kwargs: typing.Any
            ) -> SystemApksListResponseHttpRequest: ...
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
            def create(
                self,
                *,
                packageName: str,
                versionCode: str,
                body: Variant = ...,
                **kwargs: typing.Any
            ) -> VariantHttpRequest: ...
        def variants(self) -> VariantsResource: ...
    class InappproductsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            packageName: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def get(
            self, *, packageName: str, sku: str, **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def update(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def patch(
            self,
            *,
            packageName: str,
            sku: str,
            body: InAppProduct = ...,
            autoConvertMissingPrices: bool = ...,
            **kwargs: typing.Any
        ) -> InAppProductHttpRequest: ...
        def list(
            self,
            *,
            packageName: str,
            token: str = ...,
            maxResults: int = ...,
            startIndex: int = ...,
            **kwargs: typing.Any
        ) -> InappproductsListResponseHttpRequest: ...
        def delete(
            self, *, packageName: str, sku: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    def internalappsharingartifacts(self) -> InternalappsharingartifactsResource: ...
    def reviews(self) -> ReviewsResource: ...
    def edits(self) -> EditsResource: ...
    def purchases(self) -> PurchasesResource: ...
    def orders(self) -> OrdersResource: ...
    def systemapks(self) -> SystemapksResource: ...
    def inappproducts(self) -> InappproductsResource: ...

class InternalAppSharingArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InternalAppSharingArtifact: ...

class BundlesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BundlesListResponse: ...

class TestersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Testers: ...

class ListingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListingsListResponse: ...

class ImagesDeleteAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImagesDeleteAllResponse: ...

class BundleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bundle: ...

class AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AppDetails: ...

class ExpansionFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExpansionFile: ...

class InAppProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InAppProduct: ...

class TrackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Track: ...

class ReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Review: ...

class DeobfuscationFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeobfuscationFilesUploadResponse: ...

class ImagesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImagesUploadResponse: ...

class ProductPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductPurchase: ...

class ApksAddExternallyHostedResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApksAddExternallyHostedResponse: ...

class ReviewsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReviewsListResponse: ...

class AppEditHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AppEdit: ...

class TracksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TracksListResponse: ...

class InappproductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InappproductsListResponse: ...

class ApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApksListResponse: ...

class SubscriptionPurchasesDeferResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubscriptionPurchasesDeferResponse: ...

class ReviewsReplyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReviewsReplyResponse: ...

class ApkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Apk: ...

class ListingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Listing: ...

class VoidedPurchasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VoidedPurchasesListResponse: ...

class ImagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImagesListResponse: ...

class SystemApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SystemApksListResponse: ...

class SubscriptionPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubscriptionPurchase: ...

class VariantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Variant: ...

class ExpansionFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExpansionFilesUploadResponse: ...
