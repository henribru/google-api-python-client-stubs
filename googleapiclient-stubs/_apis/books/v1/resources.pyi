import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class BooksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BookshelvesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class VolumesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                userId: str,
                shelf: str,
                maxResults: int | None = ...,
                showPreorders: bool | None = ...,
                source: str | None = ...,
                startIndex: int | None = ...,
                **kwargs: typing.Any,
            ) -> VolumesHttpRequest: ...

        def get(
            self,
            *,
            userId: str,
            shelf: str,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> BookshelfHttpRequest: ...
        def list(
            self, *, userId: str, source: str | None = ..., **kwargs: typing.Any
        ) -> BookshelvesHttpRequest: ...
        def volumes(self) -> VolumesResource: ...

    @typing.type_check_only
    class CloudloadingResource(googleapiclient.discovery.Resource):
        def addBook(
            self,
            *,
            drive_document_id: str | None = ...,
            mime_type: str | None = ...,
            name: str | None = ...,
            upload_client_token: str | None = ...,
            **kwargs: typing.Any,
        ) -> BooksCloudloadingResourceHttpRequest: ...
        def deleteBook(
            self, *, volumeId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def updateBook(
            self, *, body: BooksCloudloadingResource, **kwargs: typing.Any
        ) -> BooksCloudloadingResourceHttpRequest: ...

    @typing.type_check_only
    class DictionaryResource(googleapiclient.discovery.Resource):
        def listOfflineMetadata(
            self, *, cpksver: str, **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...

    @typing.type_check_only
    class FamilysharingResource(googleapiclient.discovery.Resource):
        def getFamilyInfo(
            self, *, source: str | None = ..., **kwargs: typing.Any
        ) -> FamilyInfoHttpRequest: ...
        def share(
            self,
            *,
            docId: str | None = ...,
            source: str | None = ...,
            volumeId: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def unshare(
            self,
            *,
            docId: str | None = ...,
            source: str | None = ...,
            volumeId: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...

    @typing.type_check_only
    class LayersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnnotationDataResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationDataId: str,
                contentVersion: str,
                allowWebDefinitions: bool | None = ...,
                h: int | None = ...,
                locale: str | None = ...,
                scale: int | None = ...,
                source: str | None = ...,
                w: int | None = ...,
                **kwargs: typing.Any,
            ) -> DictionaryAnnotationdataHttpRequest: ...
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                contentVersion: str,
                annotationDataId: str | _list[str] | None = ...,
                h: int | None = ...,
                locale: str | None = ...,
                maxResults: int | None = ...,
                pageToken: str | None = ...,
                scale: int | None = ...,
                source: str | None = ...,
                updatedMax: str | None = ...,
                updatedMin: str | None = ...,
                w: int | None = ...,
                **kwargs: typing.Any,
            ) -> AnnotationsdataHttpRequest: ...
            def list_next(
                self,
                previous_request: AnnotationsdataHttpRequest,
                previous_response: Annotationsdata,
            ) -> AnnotationsdataHttpRequest | None: ...

        @typing.type_check_only
        class VolumeAnnotationsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationId: str,
                locale: str | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> VolumeannotationHttpRequest: ...
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                contentVersion: str,
                endOffset: str | None = ...,
                endPosition: str | None = ...,
                locale: str | None = ...,
                maxResults: int | None = ...,
                pageToken: str | None = ...,
                showDeleted: bool | None = ...,
                source: str | None = ...,
                startOffset: str | None = ...,
                startPosition: str | None = ...,
                updatedMax: str | None = ...,
                updatedMin: str | None = ...,
                volumeAnnotationsVersion: str | None = ...,
                **kwargs: typing.Any,
            ) -> VolumeannotationsHttpRequest: ...
            def list_next(
                self,
                previous_request: VolumeannotationsHttpRequest,
                previous_response: Volumeannotations,
            ) -> VolumeannotationsHttpRequest | None: ...

        def get(
            self,
            *,
            volumeId: str,
            summaryId: str,
            contentVersion: str | None = ...,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> LayersummaryHttpRequest: ...
        def list(
            self,
            *,
            volumeId: str,
            contentVersion: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> LayersummariesHttpRequest: ...
        def annotationData(self) -> AnnotationDataResource: ...
        def volumeAnnotations(self) -> VolumeAnnotationsResource: ...

    @typing.type_check_only
    class MyconfigResource(googleapiclient.discovery.Resource):
        def getUserSettings(
            self, *, country: str | None = ..., **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...
        def releaseDownloadAccess(
            self,
            *,
            cpksver: str,
            volumeIds: str | _list[str],
            locale: str | None = ...,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> DownloadAccessesHttpRequest: ...
        def requestAccess(
            self,
            *,
            cpksver: str,
            nonce: str,
            source: str,
            volumeId: str,
            licenseTypes: typing.Literal[
                "LICENSE_TYPES_UNDEFINED", "BOTH", "CONCURRENT", "DOWNLOAD"
            ]
            | None = ...,
            locale: str | None = ...,
            **kwargs: typing.Any,
        ) -> RequestAccessDataHttpRequest: ...
        def syncVolumeLicenses(
            self,
            *,
            cpksver: str,
            nonce: str,
            source: str,
            features: typing.Literal["FEATURES_UNDEFINED", "RENTALS"]
            | _list[typing.Literal["FEATURES_UNDEFINED", "RENTALS"]]
            | None = ...,
            includeNonComicsSeries: bool | None = ...,
            locale: str | None = ...,
            showPreorders: bool | None = ...,
            volumeIds: str | _list[str] | None = ...,
            **kwargs: typing.Any,
        ) -> VolumesHttpRequest: ...
        def updateUserSettings(
            self, *, body: Usersettings, **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...

    @typing.type_check_only
    class MylibraryResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnnotationsResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                annotationId: str,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def insert(
                self,
                *,
                body: Annotation,
                annotationId: str | None = ...,
                country: str | None = ...,
                showOnlySummaryInResponse: bool | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> AnnotationHttpRequest: ...
            def list(
                self,
                *,
                contentVersion: str | None = ...,
                layerId: str | None = ...,
                layerIds: str | _list[str] | None = ...,
                maxResults: int | None = ...,
                pageToken: str | None = ...,
                showDeleted: bool | None = ...,
                source: str | None = ...,
                updatedMax: str | None = ...,
                updatedMin: str | None = ...,
                volumeId: str | None = ...,
                **kwargs: typing.Any,
            ) -> AnnotationsHttpRequest: ...
            def list_next(
                self,
                previous_request: AnnotationsHttpRequest,
                previous_response: Annotations,
            ) -> AnnotationsHttpRequest | None: ...
            def summary(
                self,
                *,
                layerIds: str | _list[str],
                volumeId: str,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> AnnotationsSummaryHttpRequest: ...
            def update(
                self,
                *,
                annotationId: str,
                body: Annotation,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> AnnotationHttpRequest: ...

        @typing.type_check_only
        class BookshelvesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VolumesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    shelf: str,
                    country: str | None = ...,
                    maxResults: int | None = ...,
                    projection: typing.Literal["PROJECTION_UNDEFINED", "FULL", "LITE"]
                    | None = ...,
                    q: str | None = ...,
                    showPreorders: bool | None = ...,
                    source: str | None = ...,
                    startIndex: int | None = ...,
                    **kwargs: typing.Any,
                ) -> VolumesHttpRequest: ...

            def addVolume(
                self,
                *,
                shelf: str,
                volumeId: str,
                reason: typing.Literal[
                    "REASON_UNDEFINED", "IOS_PREX", "IOS_SEARCH", "ONBOARDING"
                ]
                | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def clearVolumes(
                self, *, shelf: str, source: str | None = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, shelf: str, source: str | None = ..., **kwargs: typing.Any
            ) -> BookshelfHttpRequest: ...
            def list(
                self, *, source: str | None = ..., **kwargs: typing.Any
            ) -> BookshelvesHttpRequest: ...
            def moveVolume(
                self,
                *,
                shelf: str,
                volumeId: str,
                volumePosition: int,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def removeVolume(
                self,
                *,
                shelf: str,
                volumeId: str,
                reason: typing.Literal["REASON_UNDEFINED", "ONBOARDING"] | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def volumes(self) -> VolumesResource: ...

        @typing.type_check_only
        class ReadingpositionsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                contentVersion: str | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> ReadingPositionHttpRequest: ...
            def setPosition(
                self,
                *,
                volumeId: str,
                position: str,
                timestamp: str,
                action: typing.Literal[
                    "ACTION_UNDEFINED",
                    "bookmark",
                    "chapter",
                    "next-page",
                    "prev-page",
                    "scroll",
                    "search",
                ]
                | None = ...,
                contentVersion: str | None = ...,
                deviceCookie: str | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...

        def annotations(self) -> AnnotationsResource: ...
        def bookshelves(self) -> BookshelvesResource: ...
        def readingpositions(self) -> ReadingpositionsResource: ...

    @typing.type_check_only
    class NotificationResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            notification_id: str,
            locale: str | None = ...,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> NotificationHttpRequest: ...

    @typing.type_check_only
    class OnboardingResource(googleapiclient.discovery.Resource):
        def listCategories(
            self, *, locale: str | None = ..., **kwargs: typing.Any
        ) -> CategoryHttpRequest: ...
        def listCategoryVolumes(
            self,
            *,
            categoryId: str | _list[str] | None = ...,
            locale: str | None = ...,
            maxAllowedMaturityRating: typing.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ]
            | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> Volume2HttpRequest: ...
        def listCategoryVolumes_next(
            self, previous_request: Volume2HttpRequest, previous_response: Volume2
        ) -> Volume2HttpRequest | None: ...

    @typing.type_check_only
    class PersonalizedstreamResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            locale: str | None = ...,
            maxAllowedMaturityRating: typing.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ]
            | None = ...,
            source: str | None = ...,
            **kwargs: typing.Any,
        ) -> DiscoveryclustersHttpRequest: ...

    @typing.type_check_only
    class PromoofferResource(googleapiclient.discovery.Resource):
        def accept(
            self,
            *,
            androidId: str | None = ...,
            device: str | None = ...,
            manufacturer: str | None = ...,
            model: str | None = ...,
            offerId: str | None = ...,
            product: str | None = ...,
            serial: str | None = ...,
            volumeId: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def dismiss(
            self,
            *,
            androidId: str | None = ...,
            device: str | None = ...,
            manufacturer: str | None = ...,
            model: str | None = ...,
            offerId: str | None = ...,
            product: str | None = ...,
            serial: str | None = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            androidId: str | None = ...,
            device: str | None = ...,
            manufacturer: str | None = ...,
            model: str | None = ...,
            product: str | None = ...,
            serial: str | None = ...,
            **kwargs: typing.Any,
        ) -> OffersHttpRequest: ...

    @typing.type_check_only
    class SeriesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MembershipResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                series_id: str,
                page_size: int | None = ...,
                page_token: str | None = ...,
                **kwargs: typing.Any,
            ) -> SeriesmembershipHttpRequest: ...

        def get(
            self, *, series_id: str | _list[str], **kwargs: typing.Any
        ) -> SeriesHttpRequest: ...
        def membership(self) -> MembershipResource: ...

    @typing.type_check_only
    class VolumesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssociatedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                volumeId: str,
                association: typing.Literal[
                    "ASSOCIATION_UNDEFINED",
                    "end-of-sample",
                    "end-of-volume",
                    "related-for-play",
                ]
                | None = ...,
                locale: str | None = ...,
                maxAllowedMaturityRating: typing.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ]
                | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> VolumesHttpRequest: ...

        @typing.type_check_only
        class MybooksResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                acquireMethod: typing.Literal[
                    "ACQUIRE_METHOD_UNDEFINED",
                    "FAMILY_SHARED",
                    "PREORDERED",
                    "PREVIOUSLY_RENTED",
                    "PUBLIC_DOMAIN",
                    "PURCHASED",
                    "RENTED",
                    "SAMPLE",
                    "UPLOADED",
                ]
                | _list[
                    typing.Literal[
                        "ACQUIRE_METHOD_UNDEFINED",
                        "FAMILY_SHARED",
                        "PREORDERED",
                        "PREVIOUSLY_RENTED",
                        "PUBLIC_DOMAIN",
                        "PURCHASED",
                        "RENTED",
                        "SAMPLE",
                        "UPLOADED",
                    ]
                ]
                | None = ...,
                country: str | None = ...,
                locale: str | None = ...,
                maxResults: int | None = ...,
                processingState: typing.Literal[
                    "PROCESSING_STATE_UNDEFINED",
                    "COMPLETED_FAILED",
                    "COMPLETED_SUCCESS",
                    "RUNNING",
                ]
                | _list[
                    typing.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ]
                ]
                | None = ...,
                source: str | None = ...,
                startIndex: int | None = ...,
                **kwargs: typing.Any,
            ) -> VolumesHttpRequest: ...

        @typing.type_check_only
        class RecommendedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                locale: str | None = ...,
                maxAllowedMaturityRating: typing.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ]
                | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> VolumesHttpRequest: ...
            def rate(
                self,
                *,
                rating: typing.Literal["RATING_UNDEFINED", "HAVE_IT", "NOT_INTERESTED"],
                volumeId: str,
                locale: str | None = ...,
                source: str | None = ...,
                **kwargs: typing.Any,
            ) -> BooksVolumesRecommendedRateResponseHttpRequest: ...

        @typing.type_check_only
        class UseruploadedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                locale: str | None = ...,
                maxResults: int | None = ...,
                processingState: typing.Literal[
                    "PROCESSING_STATE_UNDEFINED",
                    "COMPLETED_FAILED",
                    "COMPLETED_SUCCESS",
                    "RUNNING",
                ]
                | _list[
                    typing.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ]
                ]
                | None = ...,
                source: str | None = ...,
                startIndex: int | None = ...,
                volumeId: str | _list[str] | None = ...,
                **kwargs: typing.Any,
            ) -> VolumesHttpRequest: ...

        def get(
            self,
            *,
            volumeId: str,
            country: str | None = ...,
            includeNonComicsSeries: bool | None = ...,
            partner: str | None = ...,
            projection: typing.Literal["PROJECTION_UNDEFINED", "FULL", "LITE"]
            | None = ...,
            source: str | None = ...,
            user_library_consistent_read: bool | None = ...,
            **kwargs: typing.Any,
        ) -> VolumeHttpRequest: ...
        def list(
            self,
            *,
            q: str,
            download: typing.Literal["DOWNLOAD_UNDEFINED", "EPUB"] | None = ...,
            filter: typing.Literal[
                "FILTER_UNDEFINED",
                "ebooks",
                "free-ebooks",
                "full",
                "paid-ebooks",
                "partial",
            ]
            | None = ...,
            langRestrict: str | None = ...,
            libraryRestrict: typing.Literal[
                "LIBRARY_RESTRICT_UNDEFINED", "my-library", "no-restrict"
            ]
            | None = ...,
            maxAllowedMaturityRating: typing.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ]
            | None = ...,
            maxResults: int | None = ...,
            orderBy: typing.Literal["ORDER_BY_UNDEFINED", "newest", "relevance"]
            | None = ...,
            partner: str | None = ...,
            printType: typing.Literal[
                "PRINT_TYPE_UNDEFINED", "ALL", "BOOKS", "MAGAZINES"
            ]
            | None = ...,
            projection: typing.Literal["PROJECTION_UNDEFINED", "FULL", "LITE"]
            | None = ...,
            showPreorders: bool | None = ...,
            source: str | None = ...,
            startIndex: int | None = ...,
            **kwargs: typing.Any,
        ) -> VolumesHttpRequest: ...
        def associated(self) -> AssociatedResource: ...
        def mybooks(self) -> MybooksResource: ...
        def recommended(self) -> RecommendedResource: ...
        def useruploaded(self) -> UseruploadedResource: ...

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
    def bookshelves(self) -> BookshelvesResource: ...
    def cloudloading(self) -> CloudloadingResource: ...
    def dictionary(self) -> DictionaryResource: ...
    def familysharing(self) -> FamilysharingResource: ...
    def layers(self) -> LayersResource: ...
    def myconfig(self) -> MyconfigResource: ...
    def mylibrary(self) -> MylibraryResource: ...
    def notification(self) -> NotificationResource: ...
    def onboarding(self) -> OnboardingResource: ...
    def personalizedstream(self) -> PersonalizedstreamResource: ...
    def promooffer(self) -> PromoofferResource: ...
    def series(self) -> SeriesResource: ...
    def volumes(self) -> VolumesResource: ...

@typing.type_check_only
class AnnotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Annotation: ...

@typing.type_check_only
class AnnotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Annotations: ...

@typing.type_check_only
class AnnotationsSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnnotationsSummary: ...

@typing.type_check_only
class AnnotationsdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Annotationsdata: ...

@typing.type_check_only
class BooksCloudloadingResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BooksCloudloadingResource: ...

@typing.type_check_only
class BooksVolumesRecommendedRateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BooksVolumesRecommendedRateResponse: ...

@typing.type_check_only
class BookshelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Bookshelf: ...

@typing.type_check_only
class BookshelvesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Bookshelves: ...

@typing.type_check_only
class CategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Category: ...

@typing.type_check_only
class DictionaryAnnotationdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DictionaryAnnotationdata: ...

@typing.type_check_only
class DiscoveryclustersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Discoveryclusters: ...

@typing.type_check_only
class DownloadAccessesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DownloadAccesses: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FamilyInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FamilyInfo: ...

@typing.type_check_only
class LayersummariesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Layersummaries: ...

@typing.type_check_only
class LayersummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Layersummary: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Metadata: ...

@typing.type_check_only
class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Notification: ...

@typing.type_check_only
class OffersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Offers: ...

@typing.type_check_only
class ReadingPositionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReadingPosition: ...

@typing.type_check_only
class RequestAccessDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RequestAccessData: ...

@typing.type_check_only
class SeriesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Series: ...

@typing.type_check_only
class SeriesmembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Seriesmembership: ...

@typing.type_check_only
class UsersettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Usersettings: ...

@typing.type_check_only
class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volume: ...

@typing.type_check_only
class Volume2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volume2: ...

@typing.type_check_only
class VolumeannotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volumeannotation: ...

@typing.type_check_only
class VolumeannotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volumeannotations: ...

@typing.type_check_only
class VolumesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Volumes: ...
