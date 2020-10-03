import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DfareportingResource(googleapiclient.discovery.Resource):
    class ContentCategoriesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            searchString: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> ContentCategoriesListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: ContentCategory = ...,
            **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
        def update(
            self, *, profileId: str, body: ContentCategory = ..., **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
        def insert(
            self, *, profileId: str, body: ContentCategory = ..., **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
    class EventTagsResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, profileId: str, id: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def insert(
            self, *, profileId: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            definitionsOnly: bool = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            campaignId: str = ...,
            adId: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            enabled: bool = ...,
            eventTagTypes: typing.Union[
                typing_extensions.Literal[
                    "IMPRESSION_IMAGE_EVENT_TAG",
                    "IMPRESSION_JAVASCRIPT_EVENT_TAG",
                    "CLICK_THROUGH_EVENT_TAG",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "IMPRESSION_IMAGE_EVENT_TAG",
                        "IMPRESSION_JAVASCRIPT_EVENT_TAG",
                        "CLICK_THROUGH_EVENT_TAG",
                    ]
                ],
            ] = ...,
            searchString: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> EventTagsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def update(
            self, *, profileId: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class CampaignCreativeAssociationsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            profileId: str,
            campaignId: str,
            body: CampaignCreativeAssociation = ...,
            **kwargs: typing.Any
        ) -> CampaignCreativeAssociationHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            campaignId: str,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> CampaignCreativeAssociationsListResponseHttpRequest: ...
    class CustomEventsResource(googleapiclient.discovery.Resource):
        def batchinsert(
            self,
            *,
            profileId: str,
            body: CustomEventsBatchInsertRequest = ...,
            **kwargs: typing.Any
        ) -> CustomEventsBatchInsertResponseHttpRequest: ...
    class PlacementsResource(googleapiclient.discovery.Resource):
        def update(
            self, *, profileId: str, body: Placement = ..., **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxStartDate: str = ...,
            directorySiteIds: typing.Union[str, typing.List[str]] = ...,
            contentCategoryIds: typing.Union[str, typing.List[str]] = ...,
            archived: bool = ...,
            pricingTypes: typing.Union[
                typing_extensions.Literal[
                    "PRICING_TYPE_CPM",
                    "PRICING_TYPE_CPC",
                    "PRICING_TYPE_CPA",
                    "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                    "PRICING_TYPE_FLAT_RATE_CLICKS",
                    "PRICING_TYPE_CPM_ACTIVEVIEW",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "PRICING_TYPE_CPM",
                        "PRICING_TYPE_CPC",
                        "PRICING_TYPE_CPA",
                        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                        "PRICING_TYPE_FLAT_RATE_CLICKS",
                        "PRICING_TYPE_CPM_ACTIVEVIEW",
                    ]
                ],
            ] = ...,
            compatibilities: typing.Union[
                typing_extensions.Literal[
                    "DISPLAY",
                    "DISPLAY_INTERSTITIAL",
                    "APP",
                    "APP_INTERSTITIAL",
                    "IN_STREAM_VIDEO",
                    "IN_STREAM_AUDIO",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "DISPLAY",
                        "DISPLAY_INTERSTITIAL",
                        "APP",
                        "APP_INTERSTITIAL",
                        "IN_STREAM_VIDEO",
                        "IN_STREAM_AUDIO",
                    ]
                ],
            ] = ...,
            minEndDate: str = ...,
            maxResults: int = ...,
            groupIds: typing.Union[str, typing.List[str]] = ...,
            sizeIds: typing.Union[str, typing.List[str]] = ...,
            campaignIds: typing.Union[str, typing.List[str]] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            siteIds: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            minStartDate: str = ...,
            placementStrategyIds: typing.Union[str, typing.List[str]] = ...,
            paymentSource: typing_extensions.Literal[
                "PLACEMENT_AGENCY_PAID", "PLACEMENT_PUBLISHER_PAID"
            ] = ...,
            maxEndDate: str = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> PlacementsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: Placement = ...,
            **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Placement = ..., **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def generatetags(
            self,
            *,
            profileId: str,
            tagFormats: typing.Union[
                typing_extensions.Literal[
                    "PLACEMENT_TAG_STANDARD",
                    "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
                    "PLACEMENT_TAG_IFRAME_ILAYER",
                    "PLACEMENT_TAG_INTERNAL_REDIRECT",
                    "PLACEMENT_TAG_JAVASCRIPT",
                    "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
                    "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
                    "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
                    "PLACEMENT_TAG_CLICK_COMMANDS",
                    "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
                    "PLACEMENT_TAG_TRACKING",
                    "PLACEMENT_TAG_TRACKING_IFRAME",
                    "PLACEMENT_TAG_TRACKING_JAVASCRIPT",
                    "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
                    "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
                    "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
                    "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
                    "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
                    "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "PLACEMENT_TAG_STANDARD",
                        "PLACEMENT_TAG_IFRAME_JAVASCRIPT",
                        "PLACEMENT_TAG_IFRAME_ILAYER",
                        "PLACEMENT_TAG_INTERNAL_REDIRECT",
                        "PLACEMENT_TAG_JAVASCRIPT",
                        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT",
                        "PLACEMENT_TAG_INTERSTITIAL_INTERNAL_REDIRECT",
                        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT",
                        "PLACEMENT_TAG_CLICK_COMMANDS",
                        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH",
                        "PLACEMENT_TAG_TRACKING",
                        "PLACEMENT_TAG_TRACKING_IFRAME",
                        "PLACEMENT_TAG_TRACKING_JAVASCRIPT",
                        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_3",
                        "PLACEMENT_TAG_IFRAME_JAVASCRIPT_LEGACY",
                        "PLACEMENT_TAG_JAVASCRIPT_LEGACY",
                        "PLACEMENT_TAG_INTERSTITIAL_IFRAME_JAVASCRIPT_LEGACY",
                        "PLACEMENT_TAG_INTERSTITIAL_JAVASCRIPT_LEGACY",
                        "PLACEMENT_TAG_INSTREAM_VIDEO_PREFETCH_VAST_4",
                    ]
                ],
            ] = ...,
            placementIds: typing.Union[str, typing.List[str]] = ...,
            campaignId: str = ...,
            **kwargs: typing.Any
        ) -> PlacementsGenerateTagsResponseHttpRequest: ...
    class DimensionValuesResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            profileId: str,
            body: DimensionValueRequest = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> DimensionValueListHttpRequest: ...
    class DirectorySitesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> DirectorySiteHttpRequest: ...
        def insert(
            self, *, profileId: str, body: DirectorySite = ..., **kwargs: typing.Any
        ) -> DirectorySiteHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            acceptsInStreamVideoPlacements: bool = ...,
            acceptsPublisherPaidPlacements: bool = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            active: bool = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            searchString: str = ...,
            pageToken: str = ...,
            acceptsInterstitialPlacements: bool = ...,
            dfpNetworkCode: str = ...,
            **kwargs: typing.Any
        ) -> DirectorySitesListResponseHttpRequest: ...
    class AdvertiserGroupsResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: AdvertiserGroup = ...,
            **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def update(
            self, *, profileId: str, body: AdvertiserGroup = ..., **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def insert(
            self, *, profileId: str, body: AdvertiserGroup = ..., **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            searchString: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            maxResults: int = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> AdvertiserGroupsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class AccountUserProfilesResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            profileId: str,
            body: AccountUserProfile = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: AccountUserProfile = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: AccountUserProfile = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            pageToken: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            userRoleId: str = ...,
            active: bool = ...,
            maxResults: int = ...,
            searchString: str = ...,
            subaccountId: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfilesListResponseHttpRequest: ...
    class DynamicTargetingKeysResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            profileId: str,
            objectId: str,
            name: str,
            objectType: typing_extensions.Literal[
                "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
            ],
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            body: DynamicTargetingKey = ...,
            **kwargs: typing.Any
        ) -> DynamicTargetingKeyHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            objectId: str = ...,
            names: typing.Union[str, typing.List[str]] = ...,
            objectType: typing_extensions.Literal[
                "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
            ] = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> DynamicTargetingKeysListResponseHttpRequest: ...
    class ConversionsResource(googleapiclient.discovery.Resource):
        def batchinsert(
            self,
            *,
            profileId: str,
            body: ConversionsBatchInsertRequest = ...,
            **kwargs: typing.Any
        ) -> ConversionsBatchInsertResponseHttpRequest: ...
        def batchupdate(
            self,
            *,
            profileId: str,
            body: ConversionsBatchUpdateRequest = ...,
            **kwargs: typing.Any
        ) -> ConversionsBatchUpdateResponseHttpRequest: ...
    class UserRolePermissionGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRolePermissionGroupHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> UserRolePermissionGroupsListResponseHttpRequest: ...
    class OperatingSystemVersionsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> OperatingSystemVersionsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> OperatingSystemVersionHttpRequest: ...
    class OrderDocumentsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> OrderDocumentHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            orderId: typing.Union[str, typing.List[str]] = ...,
            searchString: str = ...,
            approved: bool = ...,
            maxResults: int = ...,
            siteId: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> OrderDocumentsListResponseHttpRequest: ...
    class PostalCodesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, code: str, **kwargs: typing.Any
        ) -> PostalCodeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> PostalCodesListResponseHttpRequest: ...
    class AdvertiserLandingPagesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def insert(
            self, *, profileId: str, body: LandingPage = ..., **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def update(
            self, *, profileId: str, body: LandingPage = ..., **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            searchString: str = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            subaccountId: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            archived: bool = ...,
            campaignIds: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> AdvertiserLandingPagesListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: LandingPage = ...,
            **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
    class UserRolesResource(googleapiclient.discovery.Resource):
        def update(
            self, *, profileId: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def patch(
            self, *, profileId: str, id: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            subaccountId: str = ...,
            accountUserRoleOnly: bool = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> UserRolesListResponseHttpRequest: ...
        def insert(
            self, *, profileId: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
    class AccountPermissionGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountPermissionGroupHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> AccountPermissionGroupsListResponseHttpRequest: ...
    class AccountPermissionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountPermissionHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> AccountPermissionsListResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            searchString: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> ProjectsListResponseHttpRequest: ...
    class FilesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            pageToken: str = ...,
            scope: typing_extensions.Literal["ALL", "MINE", "SHARED_WITH_ME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sortField: typing_extensions.Literal["ID", "LAST_MODIFIED_TIME"] = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> FileListHttpRequest: ...
        def get(
            self, *, reportId: str, fileId: str, **kwargs: typing.Any
        ) -> FileHttpRequest: ...
    class InventoryItemsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> InventoryItemHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            type: typing_extensions.Literal[
                "PLANNING_PLACEMENT_TYPE_REGULAR", "PLANNING_PLACEMENT_TYPE_CREDIT"
            ] = ...,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            siteId: typing.Union[str, typing.List[str]] = ...,
            orderId: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            inPlan: bool = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> InventoryItemsListResponseHttpRequest: ...
    class CreativeFieldsResource(googleapiclient.discovery.Resource):
        def update(
            self, *, profileId: str, body: CreativeField = ..., **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: CreativeField = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...
        def insert(
            self, *, profileId: str, body: CreativeField = ..., **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldsListResponseHttpRequest: ...
    class CreativeGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CreativeGroupHttpRequest: ...
        def insert(
            self, *, profileId: str, body: CreativeGroup = ..., **kwargs: typing.Any
        ) -> CreativeGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            groupNumber: int = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            searchString: str = ...,
            **kwargs: typing.Any
        ) -> CreativeGroupsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: CreativeGroup = ...,
            **kwargs: typing.Any
        ) -> CreativeGroupHttpRequest: ...
        def update(
            self, *, profileId: str, body: CreativeGroup = ..., **kwargs: typing.Any
        ) -> CreativeGroupHttpRequest: ...
    class CreativeFieldValuesResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            id: str,
            body: CreativeFieldValue = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            body: CreativeFieldValue = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            body: CreativeFieldValue = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def delete(
            self, *, profileId: str, creativeFieldId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, creativeFieldId: str, id: str, **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            searchString: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sortField: typing_extensions.Literal["ID", "VALUE"] = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValuesListResponseHttpRequest: ...
    class VideoFormatsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: int, **kwargs: typing.Any
        ) -> VideoFormatHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> VideoFormatsListResponseHttpRequest: ...
    class MobileCarriersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> MobileCarriersListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> MobileCarrierHttpRequest: ...
    class LanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> LanguagesListResponseHttpRequest: ...
    class TargetableRemarketingListsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> TargetableRemarketingListHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str,
            maxResults: int = ...,
            name: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            active: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TargetableRemarketingListsListResponseHttpRequest: ...
    class ReportsResource(googleapiclient.discovery.Resource):
        class FilesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                profileId: str,
                reportId: str,
                fileId: str,
                **kwargs: typing.Any
            ) -> FileHttpRequest: ...
            def list(
                self,
                *,
                profileId: str,
                reportId: str,
                pageToken: str = ...,
                sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
                maxResults: int = ...,
                sortField: typing_extensions.Literal["ID", "LAST_MODIFIED_TIME"] = ...,
                **kwargs: typing.Any
            ) -> FileListHttpRequest: ...
        class CompatibleFieldsResource(googleapiclient.discovery.Resource):
            def query(
                self, *, profileId: str, body: Report = ..., **kwargs: typing.Any
            ) -> CompatibleFieldsHttpRequest: ...
        def run(
            self,
            *,
            profileId: str,
            reportId: str,
            synchronous: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Report = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def get(
            self, *, profileId: str, reportId: str, **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def delete(
            self, *, profileId: str, reportId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            scope: typing_extensions.Literal["ALL", "MINE"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal[
                "ID", "LAST_MODIFIED_TIME", "NAME"
            ] = ...,
            **kwargs: typing.Any
        ) -> ReportListHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            reportId: str,
            body: Report = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            reportId: str,
            body: Report = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def files(self) -> FilesResource: ...
        def compatibleFields(self) -> CompatibleFieldsResource: ...
    class TargetingTemplatesResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, profileId: str, body: TargetingTemplate = ..., **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: TargetingTemplate = ...,
            **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            pageToken: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            advertiserId: str = ...,
            maxResults: int = ...,
            searchString: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> TargetingTemplatesListResponseHttpRequest: ...
        def update(
            self, *, profileId: str, body: TargetingTemplate = ..., **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
    class ChangeLogsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ChangeLogHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            action: typing_extensions.Literal[
                "ACTION_CREATE",
                "ACTION_UPDATE",
                "ACTION_DELETE",
                "ACTION_ENABLE",
                "ACTION_DISABLE",
                "ACTION_ADD",
                "ACTION_REMOVE",
                "ACTION_MARK_AS_DEFAULT",
                "ACTION_ASSOCIATE",
                "ACTION_ASSIGN",
                "ACTION_UNASSIGN",
                "ACTION_SEND",
                "ACTION_LINK",
                "ACTION_UNLINK",
                "ACTION_PUSH",
                "ACTION_EMAIL_TAGS",
                "ACTION_SHARE",
            ] = ...,
            maxResults: int = ...,
            searchString: str = ...,
            pageToken: str = ...,
            objectType: typing_extensions.Literal[
                "OBJECT_ADVERTISER",
                "OBJECT_FLOODLIGHT_CONFIGURATION",
                "OBJECT_AD",
                "OBJECT_FLOODLIGHT_ACTVITY",
                "OBJECT_CAMPAIGN",
                "OBJECT_FLOODLIGHT_ACTIVITY_GROUP",
                "OBJECT_CREATIVE",
                "OBJECT_PLACEMENT",
                "OBJECT_DFA_SITE",
                "OBJECT_USER_ROLE",
                "OBJECT_USER_PROFILE",
                "OBJECT_ADVERTISER_GROUP",
                "OBJECT_ACCOUNT",
                "OBJECT_SUBACCOUNT",
                "OBJECT_RICHMEDIA_CREATIVE",
                "OBJECT_INSTREAM_CREATIVE",
                "OBJECT_MEDIA_ORDER",
                "OBJECT_CONTENT_CATEGORY",
                "OBJECT_PLACEMENT_STRATEGY",
                "OBJECT_SD_SITE",
                "OBJECT_SIZE",
                "OBJECT_CREATIVE_GROUP",
                "OBJECT_CREATIVE_ASSET",
                "OBJECT_USER_PROFILE_FILTER",
                "OBJECT_LANDING_PAGE",
                "OBJECT_CREATIVE_FIELD",
                "OBJECT_REMARKETING_LIST",
                "OBJECT_PROVIDED_LIST_CLIENT",
                "OBJECT_EVENT_TAG",
                "OBJECT_CREATIVE_BUNDLE",
                "OBJECT_BILLING_ACCOUNT_GROUP",
                "OBJECT_BILLING_FEATURE",
                "OBJECT_RATE_CARD",
                "OBJECT_ACCOUNT_BILLING_FEATURE",
                "OBJECT_BILLING_MINIMUM_FEE",
                "OBJECT_BILLING_PROFILE",
                "OBJECT_PLAYSTORE_LINK",
                "OBJECT_TARGETING_TEMPLATE",
                "OBJECT_SEARCH_LIFT_STUDY",
                "OBJECT_FLOODLIGHT_DV360_LINK",
            ] = ...,
            userProfileIds: typing.Union[str, typing.List[str]] = ...,
            objectIds: typing.Union[str, typing.List[str]] = ...,
            maxChangeTime: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            minChangeTime: str = ...,
            **kwargs: typing.Any
        ) -> ChangeLogsListResponseHttpRequest: ...
    class OperatingSystemsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> OperatingSystemsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, dartId: str, **kwargs: typing.Any
        ) -> OperatingSystemHttpRequest: ...
    class PlacementGroupsResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: PlacementGroup = ...,
            **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxStartDate: str = ...,
            placementStrategyIds: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            contentCategoryIds: typing.Union[str, typing.List[str]] = ...,
            maxEndDate: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            campaignIds: typing.Union[str, typing.List[str]] = ...,
            archived: bool = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            siteIds: typing.Union[str, typing.List[str]] = ...,
            placementGroupType: typing_extensions.Literal[
                "PLACEMENT_PACKAGE", "PLACEMENT_ROADBLOCK"
            ] = ...,
            maxResults: int = ...,
            pricingTypes: typing.Union[
                typing_extensions.Literal[
                    "PRICING_TYPE_CPM",
                    "PRICING_TYPE_CPC",
                    "PRICING_TYPE_CPA",
                    "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                    "PRICING_TYPE_FLAT_RATE_CLICKS",
                    "PRICING_TYPE_CPM_ACTIVEVIEW",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "PRICING_TYPE_CPM",
                        "PRICING_TYPE_CPC",
                        "PRICING_TYPE_CPA",
                        "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                        "PRICING_TYPE_FLAT_RATE_CLICKS",
                        "PRICING_TYPE_CPM_ACTIVEVIEW",
                    ]
                ],
            ] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            directorySiteIds: typing.Union[str, typing.List[str]] = ...,
            minEndDate: str = ...,
            minStartDate: str = ...,
            **kwargs: typing.Any
        ) -> PlacementGroupsListResponseHttpRequest: ...
        def update(
            self, *, profileId: str, body: PlacementGroup = ..., **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def insert(
            self, *, profileId: str, body: PlacementGroup = ..., **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
    class RemarketingListSharesResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: RemarketingListShare = ...,
            **kwargs: typing.Any
        ) -> RemarketingListShareHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: RemarketingListShare = ...,
            **kwargs: typing.Any
        ) -> RemarketingListShareHttpRequest: ...
        def get(
            self, *, profileId: str, remarketingListId: str, **kwargs: typing.Any
        ) -> RemarketingListShareHttpRequest: ...
    class PlatformTypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlatformTypeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> PlatformTypesListResponseHttpRequest: ...
    class MetrosResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> MetrosListResponseHttpRequest: ...
    class CitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            regionDartIds: typing.Union[str, typing.List[str]] = ...,
            namePrefix: str = ...,
            countryDartIds: typing.Union[str, typing.List[str]] = ...,
            dartIds: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> CitiesListResponseHttpRequest: ...
    class FloodlightActivitiesResource(googleapiclient.discovery.Resource):
        def generatetag(
            self,
            *,
            profileId: str,
            floodlightActivityId: str = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivitiesGenerateTagResponseHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            advertiserId: str = ...,
            floodlightActivityGroupTagString: str = ...,
            floodlightActivityGroupName: str = ...,
            searchString: str = ...,
            floodlightActivityGroupIds: typing.Union[str, typing.List[str]] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            floodlightConfigurationId: str = ...,
            floodlightActivityGroupType: typing_extensions.Literal[
                "COUNTER", "SALE"
            ] = ...,
            maxResults: int = ...,
            tagString: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivitiesListResponseHttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
    class AdsResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, profileId: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def update(
            self, *, profileId: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            placementIds: typing.Union[str, typing.List[str]] = ...,
            active: bool = ...,
            sslCompliant: bool = ...,
            archived: bool = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sslRequired: bool = ...,
            overriddenEventTagId: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            campaignIds: typing.Union[str, typing.List[str]] = ...,
            creativeOptimizationConfigurationIds: typing.Union[
                str, typing.List[str]
            ] = ...,
            dynamicClickTracker: bool = ...,
            compatibility: typing_extensions.Literal[
                "DISPLAY",
                "DISPLAY_INTERSTITIAL",
                "APP",
                "APP_INTERSTITIAL",
                "IN_STREAM_VIDEO",
                "IN_STREAM_AUDIO",
            ] = ...,
            advertiserId: str = ...,
            searchString: str = ...,
            landingPageIds: typing.Union[str, typing.List[str]] = ...,
            audienceSegmentIds: typing.Union[str, typing.List[str]] = ...,
            type: typing.Union[
                typing_extensions.Literal[
                    "AD_SERVING_STANDARD_AD",
                    "AD_SERVING_DEFAULT_AD",
                    "AD_SERVING_CLICK_TRACKER",
                    "AD_SERVING_TRACKING",
                    "AD_SERVING_BRAND_SAFE_AD",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "AD_SERVING_STANDARD_AD",
                        "AD_SERVING_DEFAULT_AD",
                        "AD_SERVING_CLICK_TRACKER",
                        "AD_SERVING_TRACKING",
                        "AD_SERVING_BRAND_SAFE_AD",
                    ]
                ],
            ] = ...,
            remarketingListIds: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            sizeIds: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            creativeIds: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> AdsListResponseHttpRequest: ...
        def patch(
            self, *, profileId: str, id: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdHttpRequest: ...
    class FloodlightConfigurationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> FloodlightConfigurationsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: FloodlightConfiguration = ...,
            **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: FloodlightConfiguration = ...,
            **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...
    class UserRolePermissionsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> UserRolePermissionsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRolePermissionHttpRequest: ...
    class CreativeAssetsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            profileId: str,
            advertiserId: str,
            body: CreativeAssetMetadata = ...,
            **kwargs: typing.Any
        ) -> CreativeAssetMetadataHttpRequest: ...
    class RemarketingListsResource(googleapiclient.discovery.Resource):
        def update(
            self, *, profileId: str, body: RemarketingList = ..., **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str,
            pageToken: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            name: str = ...,
            maxResults: int = ...,
            active: bool = ...,
            floodlightActivityId: str = ...,
            **kwargs: typing.Any
        ) -> RemarketingListsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def insert(
            self, *, profileId: str, body: RemarketingList = ..., **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: RemarketingList = ...,
            **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
    class SubaccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> SubaccountHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Subaccount = ..., **kwargs: typing.Any
        ) -> SubaccountHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            pageToken: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            searchString: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> SubaccountsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: Subaccount = ...,
            **kwargs: typing.Any
        ) -> SubaccountHttpRequest: ...
        def update(
            self, *, profileId: str, body: Subaccount = ..., **kwargs: typing.Any
        ) -> SubaccountHttpRequest: ...
    class CreativesResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, profileId: str, id: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def update(
            self, *, profileId: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            active: bool = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            advertiserId: str = ...,
            creativeFieldIds: typing.Union[str, typing.List[str]] = ...,
            campaignId: str = ...,
            pageToken: str = ...,
            types: typing.Union[
                typing_extensions.Literal[
                    "IMAGE",
                    "DISPLAY_REDIRECT",
                    "CUSTOM_DISPLAY",
                    "INTERNAL_REDIRECT",
                    "CUSTOM_DISPLAY_INTERSTITIAL",
                    "INTERSTITIAL_INTERNAL_REDIRECT",
                    "TRACKING_TEXT",
                    "RICH_MEDIA_DISPLAY_BANNER",
                    "RICH_MEDIA_INPAGE_FLOATING",
                    "RICH_MEDIA_IM_EXPAND",
                    "RICH_MEDIA_DISPLAY_EXPANDING",
                    "RICH_MEDIA_DISPLAY_INTERSTITIAL",
                    "RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL",
                    "RICH_MEDIA_MOBILE_IN_APP",
                    "FLASH_INPAGE",
                    "INSTREAM_VIDEO",
                    "VPAID_LINEAR_VIDEO",
                    "VPAID_NON_LINEAR_VIDEO",
                    "INSTREAM_VIDEO_REDIRECT",
                    "RICH_MEDIA_PEEL_DOWN",
                    "HTML5_BANNER",
                    "DISPLAY",
                    "DISPLAY_IMAGE_GALLERY",
                    "BRAND_SAFE_DEFAULT_INSTREAM_VIDEO",
                    "INSTREAM_AUDIO",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "IMAGE",
                        "DISPLAY_REDIRECT",
                        "CUSTOM_DISPLAY",
                        "INTERNAL_REDIRECT",
                        "CUSTOM_DISPLAY_INTERSTITIAL",
                        "INTERSTITIAL_INTERNAL_REDIRECT",
                        "TRACKING_TEXT",
                        "RICH_MEDIA_DISPLAY_BANNER",
                        "RICH_MEDIA_INPAGE_FLOATING",
                        "RICH_MEDIA_IM_EXPAND",
                        "RICH_MEDIA_DISPLAY_EXPANDING",
                        "RICH_MEDIA_DISPLAY_INTERSTITIAL",
                        "RICH_MEDIA_DISPLAY_MULTI_FLOATING_INTERSTITIAL",
                        "RICH_MEDIA_MOBILE_IN_APP",
                        "FLASH_INPAGE",
                        "INSTREAM_VIDEO",
                        "VPAID_LINEAR_VIDEO",
                        "VPAID_NON_LINEAR_VIDEO",
                        "INSTREAM_VIDEO_REDIRECT",
                        "RICH_MEDIA_PEEL_DOWN",
                        "HTML5_BANNER",
                        "DISPLAY",
                        "DISPLAY_IMAGE_GALLERY",
                        "BRAND_SAFE_DEFAULT_INSTREAM_VIDEO",
                        "INSTREAM_AUDIO",
                    ]
                ],
            ] = ...,
            searchString: str = ...,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            renderingIds: typing.Union[str, typing.List[str]] = ...,
            sizeIds: typing.Union[str, typing.List[str]] = ...,
            studioCreativeId: str = ...,
            companionCreativeIds: typing.Union[str, typing.List[str]] = ...,
            archived: bool = ...,
            **kwargs: typing.Any
        ) -> CreativesListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
    class SizesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> SizeHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Size = ..., **kwargs: typing.Any
        ) -> SizeHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            width: int = ...,
            height: int = ...,
            iabStandard: bool = ...,
            **kwargs: typing.Any
        ) -> SizesListResponseHttpRequest: ...
    class SitesResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, profileId: str, id: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            acceptsInterstitialPlacements: bool = ...,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            unmappedSite: bool = ...,
            acceptsInStreamVideoPlacements: bool = ...,
            subaccountId: str = ...,
            acceptsPublisherPaidPlacements: bool = ...,
            adWordsSite: bool = ...,
            pageToken: str = ...,
            searchString: str = ...,
            approved: bool = ...,
            directorySiteIds: typing.Union[str, typing.List[str]] = ...,
            campaignIds: typing.Union[str, typing.List[str]] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> SitesListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def update(
            self, *, profileId: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
    class BrowsersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> BrowsersListResponseHttpRequest: ...
    class OrdersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            pageToken: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            siteId: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            searchString: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> OrdersListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> OrderHttpRequest: ...
    class CampaignsResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, profileId: str, id: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def update(
            self, *, profileId: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            pageToken: str = ...,
            excludedIds: typing.Union[str, typing.List[str]] = ...,
            archived: bool = ...,
            advertiserIds: typing.Union[str, typing.List[str]] = ...,
            searchString: str = ...,
            advertiserGroupIds: typing.Union[str, typing.List[str]] = ...,
            subaccountId: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            maxResults: int = ...,
            overriddenEventTagId: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            atLeastOneOptimizationActivity: bool = ...,
            **kwargs: typing.Any
        ) -> CampaignsListResponseHttpRequest: ...
    class FloodlightActivityGroupsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            profileId: str,
            body: FloodlightActivityGroup = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            type: typing_extensions.Literal["COUNTER", "SALE"] = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            floodlightConfigurationId: str = ...,
            advertiserId: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            searchString: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityGroupsListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightActivityGroupHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: FloodlightActivityGroup = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityGroupHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: FloodlightActivityGroup = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityGroupHttpRequest: ...
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def patch(
            self, *, profileId: str, id: str, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self, *, profileId: str, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            searchString: str = ...,
            active: bool = ...,
            pageToken: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> AccountsListResponseHttpRequest: ...
    class PlacementStrategiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            ids: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> PlacementStrategiesListResponseHttpRequest: ...
        def insert(
            self, *, profileId: str, body: PlacementStrategy = ..., **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def update(
            self, *, profileId: str, body: PlacementStrategy = ..., **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: PlacementStrategy = ...,
            **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
    class MobileAppsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> MobileAppHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            searchString: str = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            directories: typing.Union[
                typing_extensions.Literal[
                    "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_PLAY_STORE"
                ],
                typing.List[
                    typing_extensions.Literal[
                        "UNKNOWN", "APPLE_APP_STORE", "GOOGLE_PLAY_STORE"
                    ]
                ],
            ] = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> MobileAppsListResponseHttpRequest: ...
    class RegionsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> RegionsListResponseHttpRequest: ...
    class ConnectionTypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ConnectionTypeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> ConnectionTypesListResponseHttpRequest: ...
    class CountriesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> CountriesListResponseHttpRequest: ...
        def get(
            self, *, profileId: str, dartId: str, **kwargs: typing.Any
        ) -> CountryHttpRequest: ...
    class AccountActiveAdSummariesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, summaryAccountId: str, **kwargs: typing.Any
        ) -> AccountActiveAdSummaryHttpRequest: ...
    class AdvertisersResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, profileId: str, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: Advertiser = ...,
            **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            ids: typing.Union[str, typing.List[str]] = ...,
            status: typing_extensions.Literal["APPROVED", "ON_HOLD"] = ...,
            includeAdvertisersWithoutGroupsOnly: bool = ...,
            pageToken: str = ...,
            floodlightConfigurationIds: typing.Union[str, typing.List[str]] = ...,
            advertiserGroupIds: typing.Union[str, typing.List[str]] = ...,
            searchString: str = ...,
            subaccountId: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            onlyParent: bool = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            **kwargs: typing.Any
        ) -> AdvertisersListResponseHttpRequest: ...
        def update(
            self, *, profileId: str, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
    class UserProfilesResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> UserProfileListHttpRequest: ...
        def get(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> UserProfileHttpRequest: ...
    def contentCategories(self) -> ContentCategoriesResource: ...
    def eventTags(self) -> EventTagsResource: ...
    def campaignCreativeAssociations(self) -> CampaignCreativeAssociationsResource: ...
    def customEvents(self) -> CustomEventsResource: ...
    def placements(self) -> PlacementsResource: ...
    def dimensionValues(self) -> DimensionValuesResource: ...
    def directorySites(self) -> DirectorySitesResource: ...
    def advertiserGroups(self) -> AdvertiserGroupsResource: ...
    def accountUserProfiles(self) -> AccountUserProfilesResource: ...
    def dynamicTargetingKeys(self) -> DynamicTargetingKeysResource: ...
    def conversions(self) -> ConversionsResource: ...
    def userRolePermissionGroups(self) -> UserRolePermissionGroupsResource: ...
    def operatingSystemVersions(self) -> OperatingSystemVersionsResource: ...
    def orderDocuments(self) -> OrderDocumentsResource: ...
    def postalCodes(self) -> PostalCodesResource: ...
    def advertiserLandingPages(self) -> AdvertiserLandingPagesResource: ...
    def userRoles(self) -> UserRolesResource: ...
    def accountPermissionGroups(self) -> AccountPermissionGroupsResource: ...
    def accountPermissions(self) -> AccountPermissionsResource: ...
    def projects(self) -> ProjectsResource: ...
    def files(self) -> FilesResource: ...
    def inventoryItems(self) -> InventoryItemsResource: ...
    def creativeFields(self) -> CreativeFieldsResource: ...
    def creativeGroups(self) -> CreativeGroupsResource: ...
    def creativeFieldValues(self) -> CreativeFieldValuesResource: ...
    def videoFormats(self) -> VideoFormatsResource: ...
    def mobileCarriers(self) -> MobileCarriersResource: ...
    def languages(self) -> LanguagesResource: ...
    def targetableRemarketingLists(self) -> TargetableRemarketingListsResource: ...
    def reports(self) -> ReportsResource: ...
    def targetingTemplates(self) -> TargetingTemplatesResource: ...
    def changeLogs(self) -> ChangeLogsResource: ...
    def operatingSystems(self) -> OperatingSystemsResource: ...
    def placementGroups(self) -> PlacementGroupsResource: ...
    def remarketingListShares(self) -> RemarketingListSharesResource: ...
    def platformTypes(self) -> PlatformTypesResource: ...
    def metros(self) -> MetrosResource: ...
    def cities(self) -> CitiesResource: ...
    def floodlightActivities(self) -> FloodlightActivitiesResource: ...
    def ads(self) -> AdsResource: ...
    def floodlightConfigurations(self) -> FloodlightConfigurationsResource: ...
    def userRolePermissions(self) -> UserRolePermissionsResource: ...
    def creativeAssets(self) -> CreativeAssetsResource: ...
    def remarketingLists(self) -> RemarketingListsResource: ...
    def subaccounts(self) -> SubaccountsResource: ...
    def creatives(self) -> CreativesResource: ...
    def sizes(self) -> SizesResource: ...
    def sites(self) -> SitesResource: ...
    def browsers(self) -> BrowsersResource: ...
    def orders(self) -> OrdersResource: ...
    def campaigns(self) -> CampaignsResource: ...
    def floodlightActivityGroups(self) -> FloodlightActivityGroupsResource: ...
    def accounts(self) -> AccountsResource: ...
    def placementStrategies(self) -> PlacementStrategiesResource: ...
    def mobileApps(self) -> MobileAppsResource: ...
    def regions(self) -> RegionsResource: ...
    def connectionTypes(self) -> ConnectionTypesResource: ...
    def countries(self) -> CountriesResource: ...
    def accountActiveAdSummaries(self) -> AccountActiveAdSummariesResource: ...
    def advertisers(self) -> AdvertisersResource: ...
    def userProfiles(self) -> UserProfilesResource: ...

class UserRolePermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRolePermission: ...

class CustomEventsBatchInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomEventsBatchInsertResponse: ...

class DirectorySiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DirectorySite: ...

class ProjectsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProjectsListResponse: ...

class OperatingSystemVersionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperatingSystemVersionsListResponse: ...

class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Report: ...

class DynamicTargetingKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DynamicTargetingKey: ...

class OrdersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrdersListResponse: ...

class UserRolePermissionGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRolePermissionGroupsListResponse: ...

class DynamicTargetingKeysListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DynamicTargetingKeysListResponse: ...

class DimensionValueListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DimensionValueList: ...

class FileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FileList: ...

class PlatformTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlatformType: ...

class SizesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SizesListResponse: ...

class ContentCategoriesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContentCategoriesListResponse: ...

class BrowsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BrowsersListResponse: ...

class CountriesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CountriesListResponse: ...

class UserProfileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserProfileList: ...

class LandingPageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LandingPage: ...

class OrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Order: ...

class ChangeLogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChangeLog: ...

class FloodlightActivityGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightActivityGroup: ...

class PlacementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Placement: ...

class CampaignCreativeAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CampaignCreativeAssociation: ...

class ConnectionTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConnectionType: ...

class CreativesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativesListResponse: ...

class OrderDocumentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderDocumentsListResponse: ...

class AccountUserProfilesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountUserProfilesListResponse: ...

class ChangeLogsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChangeLogsListResponse: ...

class OperatingSystemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperatingSystem: ...

class UserRolesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRolesListResponse: ...

class UserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserProfile: ...

class CreativeAssetMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeAssetMetadata: ...

class PlatformTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlatformTypesListResponse: ...

class FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> File: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class OperatingSystemsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperatingSystemsListResponse: ...

class FloodlightActivityGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightActivityGroupsListResponse: ...

class OperatingSystemVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperatingSystemVersion: ...

class FloodlightActivitiesGenerateTagResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightActivitiesGenerateTagResponse: ...

class CompatibleFieldsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompatibleFields: ...

class FloodlightActivityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightActivity: ...

class CreativeFieldValueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeFieldValue: ...

class AdsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdsListResponse: ...

class RegionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionsListResponse: ...

class SizeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Size: ...

class UserRolePermissionGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRolePermissionGroup: ...

class AccountPermissionGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountPermissionGroupsListResponse: ...

class CreativeGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeGroup: ...

class CitiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CitiesListResponse: ...

class ContentCategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContentCategory: ...

class MobileCarriersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileCarriersListResponse: ...

class CreativeFieldValuesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeFieldValuesListResponse: ...

class AccountPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountPermission: ...

class VideoFormatHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoFormat: ...

class SubaccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubaccountsListResponse: ...

class CampaignCreativeAssociationsListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CampaignCreativeAssociationsListResponse: ...

class PlacementsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementsListResponse: ...

class CreativeFieldsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeFieldsListResponse: ...

class FloodlightActivitiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightActivitiesListResponse: ...

class CreativeFieldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeField: ...

class AdvertiserLandingPagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdvertiserLandingPagesListResponse: ...

class AccountPermissionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountPermissionsListResponse: ...

class AccountPermissionGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountPermissionGroup: ...

class EventTagsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EventTagsListResponse: ...

class MobileAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileApp: ...

class AccountUserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountUserProfile: ...

class EventTagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EventTag: ...

class SubaccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subaccount: ...

class AdHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Ad: ...

class PostalCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PostalCode: ...

class TargetingTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetingTemplate: ...

class FloodlightConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightConfiguration: ...

class InventoryItemsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventoryItemsListResponse: ...

class VideoFormatsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VideoFormatsListResponse: ...

class FloodlightConfigurationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightConfigurationsListResponse: ...

class ConnectionTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConnectionTypesListResponse: ...

class OrderDocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrderDocument: ...

class TargetingTemplatesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetingTemplatesListResponse: ...

class MobileCarrierHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileCarrier: ...

class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Site: ...

class RemarketingListShareHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemarketingListShare: ...

class AdvertiserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Advertiser: ...

class AdvertisersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdvertisersListResponse: ...

class ConversionsBatchInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConversionsBatchInsertResponse: ...

class RemarketingListsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemarketingListsListResponse: ...

class PlacementStrategiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementStrategiesListResponse: ...

class CampaignsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CampaignsListResponse: ...

class RemarketingListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RemarketingList: ...

class PlacementGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementGroupsListResponse: ...

class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsListResponse: ...

class InventoryItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventoryItem: ...

class ConversionsBatchUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConversionsBatchUpdateResponse: ...

class PostalCodesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PostalCodesListResponse: ...

class CountryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Country: ...

class TargetableRemarketingListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetableRemarketingList: ...

class MobileAppsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MobileAppsListResponse: ...

class TargetableRemarketingListsListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetableRemarketingListsListResponse: ...

class MetrosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MetrosListResponse: ...

class LanguagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LanguagesListResponse: ...

class UserRoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRole: ...

class CampaignHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Campaign: ...

class SitesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SitesListResponse: ...

class DirectorySitesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DirectorySitesListResponse: ...

class AdvertiserGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdvertiserGroup: ...

class CreativeGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeGroupsListResponse: ...

class AdvertiserGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AdvertiserGroupsListResponse: ...

class ReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReportList: ...

class AccountActiveAdSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountActiveAdSummary: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...

class PlacementStrategyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementStrategy: ...

class PlacementGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementGroup: ...

class PlacementsGenerateTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PlacementsGenerateTagsResponse: ...

class UserRolePermissionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserRolePermissionsListResponse: ...
