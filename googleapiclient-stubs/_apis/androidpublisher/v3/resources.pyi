import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AndroidPublisherResource(googleapiclient.discovery.Resource):
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
                **kwargs: typing.Any
            ) -> BundleHttpRequest: ...
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
            self, *, packageName: str, editId: str, **kwargs: typing.Any
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
        def deobfuscationfiles(self) -> DeobfuscationfilesResource: ...
        def details(self) -> DetailsResource: ...
        def expansionfiles(self) -> ExpansionfilesResource: ...
        def images(self) -> ImagesResource: ...
        def listings(self) -> ListingsResource: ...
        def testers(self) -> TestersResource: ...
        def tracks(self) -> TracksResource: ...
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
    def edits(self) -> EditsResource: ...
    def inappproducts(self) -> InappproductsResource: ...
    def internalappsharingartifacts(self) -> InternalappsharingartifactsResource: ...
    def orders(self) -> OrdersResource: ...
    def purchases(self) -> PurchasesResource: ...
    def reviews(self) -> ReviewsResource: ...
    def systemapks(self) -> SystemapksResource: ...

@typing.type_check_only
class ApkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Apk: ...

@typing.type_check_only
class ApksAddExternallyHostedResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ApksAddExternallyHostedResponse: ...

@typing.type_check_only
class ApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ApksListResponse: ...

@typing.type_check_only
class AppDetailsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AppDetails: ...

@typing.type_check_only
class AppEditHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AppEdit: ...

@typing.type_check_only
class BundleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Bundle: ...

@typing.type_check_only
class BundlesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BundlesListResponse: ...

@typing.type_check_only
class DeobfuscationFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DeobfuscationFilesUploadResponse: ...

@typing.type_check_only
class ExpansionFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ExpansionFile: ...

@typing.type_check_only
class ExpansionFilesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ExpansionFilesUploadResponse: ...

@typing.type_check_only
class ImagesDeleteAllResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ImagesDeleteAllResponse: ...

@typing.type_check_only
class ImagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ImagesListResponse: ...

@typing.type_check_only
class ImagesUploadResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ImagesUploadResponse: ...

@typing.type_check_only
class InAppProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InAppProduct: ...

@typing.type_check_only
class InappproductsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InappproductsListResponse: ...

@typing.type_check_only
class InternalAppSharingArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> InternalAppSharingArtifact: ...

@typing.type_check_only
class ListingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Listing: ...

@typing.type_check_only
class ListingsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListingsListResponse: ...

@typing.type_check_only
class ProductPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ProductPurchase: ...

@typing.type_check_only
class ReviewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Review: ...

@typing.type_check_only
class ReviewsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReviewsListResponse: ...

@typing.type_check_only
class ReviewsReplyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReviewsReplyResponse: ...

@typing.type_check_only
class SubscriptionPurchaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SubscriptionPurchase: ...

@typing.type_check_only
class SubscriptionPurchasesDeferResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SubscriptionPurchasesDeferResponse: ...

@typing.type_check_only
class SystemApksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SystemApksListResponse: ...

@typing.type_check_only
class TestersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Testers: ...

@typing.type_check_only
class TrackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Track: ...

@typing.type_check_only
class TracksListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TracksListResponse: ...

@typing.type_check_only
class VariantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Variant: ...

@typing.type_check_only
class VoidedPurchasesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VoidedPurchasesListResponse: ...
