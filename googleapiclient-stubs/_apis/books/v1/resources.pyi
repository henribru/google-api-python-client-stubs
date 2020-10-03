import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BooksResource(googleapiclient.discovery.Resource):
    class PromoofferResource(googleapiclient.discovery.Resource):
        def accept(
            self,
            *,
            offerId: str = ...,
            product: str = ...,
            androidId: str = ...,
            model: str = ...,
            serial: str = ...,
            device: str = ...,
            manufacturer: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            model: str = ...,
            product: str = ...,
            androidId: str = ...,
            manufacturer: str = ...,
            serial: str = ...,
            device: str = ...,
            **kwargs: typing.Any
        ) -> OffersHttpRequest: ...
        def dismiss(
            self,
            *,
            manufacturer: str = ...,
            product: str = ...,
            androidId: str = ...,
            offerId: str = ...,
            serial: str = ...,
            model: str = ...,
            device: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class LayersResource(googleapiclient.discovery.Resource):
        class AnnotationDataResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                locale: str = ...,
                pageToken: str = ...,
                h: int = ...,
                annotationDataId: typing.Union[str, typing.List[str]] = ...,
                scale: int = ...,
                maxResults: int = ...,
                updatedMax: str = ...,
                w: int = ...,
                contentVersion: str = ...,
                updatedMin: str = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationsdataHttpRequest: ...
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationDataId: str,
                source: str = ...,
                w: int = ...,
                h: int = ...,
                scale: int = ...,
                locale: str = ...,
                allowWebDefinitions: bool = ...,
                contentVersion: str = ...,
                **kwargs: typing.Any
            ) -> DictionaryAnnotationdataHttpRequest: ...
        class VolumeAnnotationsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                volumeId: str,
                layerId: str,
                annotationId: str,
                source: str = ...,
                locale: str = ...,
                **kwargs: typing.Any
            ) -> VolumeannotationHttpRequest: ...
            def list(
                self,
                *,
                volumeId: str,
                layerId: str,
                updatedMin: str = ...,
                startOffset: str = ...,
                endPosition: str = ...,
                startPosition: str = ...,
                pageToken: str = ...,
                source: str = ...,
                endOffset: str = ...,
                maxResults: int = ...,
                updatedMax: str = ...,
                contentVersion: str = ...,
                showDeleted: bool = ...,
                volumeAnnotationsVersion: str = ...,
                locale: str = ...,
                **kwargs: typing.Any
            ) -> VolumeannotationsHttpRequest: ...
        def get(
            self,
            *,
            volumeId: str,
            summaryId: str,
            contentVersion: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> LayersummaryHttpRequest: ...
        def list(
            self,
            *,
            volumeId: str,
            pageToken: str = ...,
            source: str = ...,
            contentVersion: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> LayersummariesHttpRequest: ...
        def annotationData(self) -> AnnotationDataResource: ...
        def volumeAnnotations(self) -> VolumeAnnotationsResource: ...
    class NotificationResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            source: str = ...,
            notification_id: str = ...,
            locale: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
    class PersonalizedstreamResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            locale: str = ...,
            source: str = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            **kwargs: typing.Any
        ) -> DiscoveryclustersHttpRequest: ...
    class BookshelvesResource(googleapiclient.discovery.Resource):
        class VolumesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                userId: str,
                shelf: str,
                maxResults: int = ...,
                startIndex: int = ...,
                source: str = ...,
                showPreorders: bool = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        def get(
            self, *, userId: str, shelf: str, source: str = ..., **kwargs: typing.Any
        ) -> BookshelfHttpRequest: ...
        def list(
            self, *, userId: str, source: str = ..., **kwargs: typing.Any
        ) -> BookshelvesHttpRequest: ...
        def volumes(self) -> VolumesResource: ...
    class DictionaryResource(googleapiclient.discovery.Resource):
        def listOfflineMetadata(
            self, *, cpksver: str = ..., **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...
    class CloudloadingResource(googleapiclient.discovery.Resource):
        def deleteBook(
            self, *, volumeId: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def updateBook(
            self, *, body: BooksCloudloadingResource = ..., **kwargs: typing.Any
        ) -> BooksCloudloadingResourceHttpRequest: ...
        def addBook(
            self,
            *,
            mime_type: str = ...,
            drive_document_id: str = ...,
            upload_client_token: str = ...,
            name: str = ...,
            **kwargs: typing.Any
        ) -> BooksCloudloadingResourceHttpRequest: ...
    class OnboardingResource(googleapiclient.discovery.Resource):
        def listCategories(
            self, *, locale: str = ..., **kwargs: typing.Any
        ) -> CategoryHttpRequest: ...
        def listCategoryVolumes(
            self,
            *,
            categoryId: typing.Union[str, typing.List[str]] = ...,
            pageSize: int = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            pageToken: str = ...,
            locale: str = ...,
            **kwargs: typing.Any
        ) -> Volume2HttpRequest: ...
    class MyconfigResource(googleapiclient.discovery.Resource):
        def requestAccess(
            self,
            *,
            source: str = ...,
            licenseTypes: typing_extensions.Literal[
                "LICENSE_TYPES_UNDEFINED", "BOTH", "CONCURRENT", "DOWNLOAD"
            ] = ...,
            volumeId: str = ...,
            locale: str = ...,
            cpksver: str = ...,
            nonce: str = ...,
            **kwargs: typing.Any
        ) -> RequestAccessDataHttpRequest: ...
        def syncVolumeLicenses(
            self,
            *,
            features: typing.Union[
                typing_extensions.Literal["FEATURES_UNDEFINED", "RENTALS"],
                typing.List[typing_extensions.Literal["FEATURES_UNDEFINED", "RENTALS"]],
            ] = ...,
            volumeIds: typing.Union[str, typing.List[str]] = ...,
            locale: str = ...,
            cpksver: str = ...,
            nonce: str = ...,
            showPreorders: bool = ...,
            source: str = ...,
            includeNonComicsSeries: bool = ...,
            **kwargs: typing.Any
        ) -> VolumesHttpRequest: ...
        def updateUserSettings(
            self, *, body: Usersettings = ..., **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...
        def releaseDownloadAccess(
            self,
            *,
            volumeIds: typing.Union[str, typing.List[str]] = ...,
            source: str = ...,
            cpksver: str = ...,
            locale: str = ...,
            **kwargs: typing.Any
        ) -> DownloadAccessesHttpRequest: ...
        def getUserSettings(
            self, *, country: str = ..., **kwargs: typing.Any
        ) -> UsersettingsHttpRequest: ...
    class FamilysharingResource(googleapiclient.discovery.Resource):
        def unshare(
            self,
            *,
            source: str = ...,
            docId: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getFamilyInfo(
            self, *, source: str = ..., **kwargs: typing.Any
        ) -> FamilyInfoHttpRequest: ...
        def share(
            self,
            *,
            docId: str = ...,
            source: str = ...,
            volumeId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    class SeriesResource(googleapiclient.discovery.Resource):
        class MembershipResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                series_id: str = ...,
                page_token: str = ...,
                page_size: int = ...,
                **kwargs: typing.Any
            ) -> SeriesmembershipHttpRequest: ...
        def get(
            self,
            *,
            series_id: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> SeriesHttpRequest: ...
        def membership(self) -> MembershipResource: ...
    class VolumesResource(googleapiclient.discovery.Resource):
        class RecommendedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                source: str = ...,
                maxAllowedMaturityRating: typing_extensions.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ] = ...,
                locale: str = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
            def rate(
                self,
                *,
                locale: str = ...,
                source: str = ...,
                volumeId: str = ...,
                rating: typing_extensions.Literal[
                    "RATING_UNDEFINED", "HAVE_IT", "NOT_INTERESTED"
                ] = ...,
                **kwargs: typing.Any
            ) -> BooksVolumesRecommendedRateResponseHttpRequest: ...
        class MybooksResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                acquireMethod: typing.Union[
                    typing_extensions.Literal[
                        "ACQUIRE_METHOD_UNDEFINED",
                        "FAMILY_SHARED",
                        "PREORDERED",
                        "PREVIOUSLY_RENTED",
                        "PUBLIC_DOMAIN",
                        "PURCHASED",
                        "RENTED",
                        "SAMPLE",
                        "UPLOADED",
                    ],
                    typing.List[
                        typing_extensions.Literal[
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
                    ],
                ] = ...,
                maxResults: int = ...,
                startIndex: int = ...,
                country: str = ...,
                locale: str = ...,
                processingState: typing.Union[
                    typing_extensions.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "PROCESSING_STATE_UNDEFINED",
                            "COMPLETED_FAILED",
                            "COMPLETED_SUCCESS",
                            "RUNNING",
                        ]
                    ],
                ] = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        class AssociatedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                volumeId: str,
                maxAllowedMaturityRating: typing_extensions.Literal[
                    "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
                ] = ...,
                source: str = ...,
                locale: str = ...,
                association: typing_extensions.Literal[
                    "ASSOCIATION_UNDEFINED",
                    "end-of-sample",
                    "end-of-volume",
                    "related-for-play",
                ] = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        class UseruploadedResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                startIndex: int = ...,
                source: str = ...,
                volumeId: typing.Union[str, typing.List[str]] = ...,
                processingState: typing.Union[
                    typing_extensions.Literal[
                        "PROCESSING_STATE_UNDEFINED",
                        "COMPLETED_FAILED",
                        "COMPLETED_SUCCESS",
                        "RUNNING",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "PROCESSING_STATE_UNDEFINED",
                            "COMPLETED_FAILED",
                            "COMPLETED_SUCCESS",
                            "RUNNING",
                        ]
                    ],
                ] = ...,
                locale: str = ...,
                maxResults: int = ...,
                **kwargs: typing.Any
            ) -> VolumesHttpRequest: ...
        def get(
            self,
            *,
            volumeId: str,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "FULL", "LITE"
            ] = ...,
            user_library_consistent_read: bool = ...,
            partner: str = ...,
            includeNonComicsSeries: bool = ...,
            country: str = ...,
            source: str = ...,
            **kwargs: typing.Any
        ) -> VolumeHttpRequest: ...
        def list(
            self,
            *,
            projection: typing_extensions.Literal[
                "PROJECTION_UNDEFINED", "FULL", "LITE"
            ] = ...,
            printType: typing_extensions.Literal[
                "PRINT_TYPE_UNDEFINED", "ALL", "BOOKS", "MAGAZINES"
            ] = ...,
            showPreorders: bool = ...,
            langRestrict: str = ...,
            libraryRestrict: typing_extensions.Literal[
                "LIBRARY_RESTRICT_UNDEFINED", "my-library", "no-restrict"
            ] = ...,
            orderBy: typing_extensions.Literal[
                "ORDER_BY_UNDEFINED", "newest", "relevance"
            ] = ...,
            partner: str = ...,
            source: str = ...,
            maxResults: int = ...,
            filter: typing_extensions.Literal[
                "FILTER_UNDEFINED",
                "ebooks",
                "free-ebooks",
                "full",
                "paid-ebooks",
                "partial",
            ] = ...,
            startIndex: int = ...,
            maxAllowedMaturityRating: typing_extensions.Literal[
                "MAX_ALLOWED_MATURITY_RATING_UNDEFINED", "MATURE", "not-mature"
            ] = ...,
            download: typing_extensions.Literal["DOWNLOAD_UNDEFINED", "EPUB"] = ...,
            q: str = ...,
            **kwargs: typing.Any
        ) -> VolumesHttpRequest: ...
        def recommended(self) -> RecommendedResource: ...
        def mybooks(self) -> MybooksResource: ...
        def associated(self) -> AssociatedResource: ...
        def useruploaded(self) -> UseruploadedResource: ...
    class MylibraryResource(googleapiclient.discovery.Resource):
        class ReadingpositionsResource(googleapiclient.discovery.Resource):
            def setPosition(
                self,
                *,
                volumeId: str,
                position: str = ...,
                contentVersion: str = ...,
                source: str = ...,
                action: typing_extensions.Literal[
                    "ACTION_UNDEFINED",
                    "bookmark",
                    "chapter",
                    "next-page",
                    "prev-page",
                    "scroll",
                    "search",
                ] = ...,
                timestamp: str = ...,
                deviceCookie: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                volumeId: str,
                source: str = ...,
                contentVersion: str = ...,
                **kwargs: typing.Any
            ) -> ReadingPositionHttpRequest: ...
        class BookshelvesResource(googleapiclient.discovery.Resource):
            class VolumesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    shelf: str,
                    source: str = ...,
                    projection: typing_extensions.Literal[
                        "PROJECTION_UNDEFINED", "FULL", "LITE"
                    ] = ...,
                    startIndex: int = ...,
                    country: str = ...,
                    maxResults: int = ...,
                    showPreorders: bool = ...,
                    q: str = ...,
                    **kwargs: typing.Any
                ) -> VolumesHttpRequest: ...
            def removeVolume(
                self,
                *,
                shelf: str,
                reason: typing_extensions.Literal[
                    "REASON_UNDEFINED", "ONBOARDING"
                ] = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def addVolume(
                self,
                *,
                shelf: str,
                reason: typing_extensions.Literal[
                    "REASON_UNDEFINED", "IOS_PREX", "IOS_SEARCH", "ONBOARDING"
                ] = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def moveVolume(
                self,
                *,
                shelf: str,
                volumePosition: int = ...,
                source: str = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def clearVolumes(
                self, *, shelf: str, source: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, shelf: str, source: str = ..., **kwargs: typing.Any
            ) -> BookshelfHttpRequest: ...
            def list(
                self, *, source: str = ..., **kwargs: typing.Any
            ) -> BookshelvesHttpRequest: ...
            def volumes(self) -> VolumesResource: ...
        class AnnotationsResource(googleapiclient.discovery.Resource):
            def insert(
                self,
                *,
                body: Annotation = ...,
                annotationId: str = ...,
                country: str = ...,
                showOnlySummaryInResponse: bool = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationHttpRequest: ...
            def update(
                self,
                *,
                annotationId: str,
                body: Annotation = ...,
                source: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationHttpRequest: ...
            def summary(
                self,
                *,
                layerIds: typing.Union[str, typing.List[str]] = ...,
                volumeId: str = ...,
                **kwargs: typing.Any
            ) -> AnnotationsSummaryHttpRequest: ...
            def list(
                self,
                *,
                pageToken: str = ...,
                source: str = ...,
                maxResults: int = ...,
                updatedMax: str = ...,
                layerIds: typing.Union[str, typing.List[str]] = ...,
                updatedMin: str = ...,
                contentVersion: str = ...,
                volumeId: str = ...,
                layerId: str = ...,
                showDeleted: bool = ...,
                **kwargs: typing.Any
            ) -> AnnotationsHttpRequest: ...
            def delete(
                self, *, annotationId: str, source: str = ..., **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        def readingpositions(self) -> ReadingpositionsResource: ...
        def bookshelves(self) -> BookshelvesResource: ...
        def annotations(self) -> AnnotationsResource: ...
    def promooffer(self) -> PromoofferResource: ...
    def layers(self) -> LayersResource: ...
    def notification(self) -> NotificationResource: ...
    def personalizedstream(self) -> PersonalizedstreamResource: ...
    def bookshelves(self) -> BookshelvesResource: ...
    def dictionary(self) -> DictionaryResource: ...
    def cloudloading(self) -> CloudloadingResource: ...
    def onboarding(self) -> OnboardingResource: ...
    def myconfig(self) -> MyconfigResource: ...
    def familysharing(self) -> FamilysharingResource: ...
    def series(self) -> SeriesResource: ...
    def volumes(self) -> VolumesResource: ...
    def mylibrary(self) -> MylibraryResource: ...

class LayersummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Layersummary: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class AnnotationsSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AnnotationsSummary: ...

class VolumeannotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumeannotation: ...

class SeriesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Series: ...

class SeriesmembershipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Seriesmembership: ...

class DiscoveryclustersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Discoveryclusters: ...

class FamilyInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FamilyInfo: ...

class VolumeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volume: ...

class AnnotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotation: ...

class AnnotationsdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotationsdata: ...

class AnnotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotations: ...

class BooksVolumesRecommendedRateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BooksVolumesRecommendedRateResponse: ...

class BookshelfHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bookshelf: ...

class DownloadAccessesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DownloadAccesses: ...

class UsersettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Usersettings: ...

class VolumeannotationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumeannotations: ...

class Volume2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volume2: ...

class BooksCloudloadingResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BooksCloudloadingResource: ...

class RequestAccessDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RequestAccessData: ...

class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Metadata: ...

class LayersummariesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Layersummaries: ...

class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Notification: ...

class ReadingPositionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReadingPosition: ...

class OffersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Offers: ...

class DictionaryAnnotationdataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DictionaryAnnotationdata: ...

class CategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Category: ...

class BookshelvesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bookshelves: ...

class VolumesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Volumes: ...
