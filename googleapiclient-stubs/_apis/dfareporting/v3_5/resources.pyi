import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DfareportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountActiveAdSummariesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, summaryAccountId: str, **kwargs: typing.Any
        ) -> AccountActiveAdSummaryHttpRequest: ...

    @typing.type_check_only
    class AccountPermissionGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountPermissionGroupHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> AccountPermissionGroupsListResponseHttpRequest: ...

    @typing.type_check_only
    class AccountPermissionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountPermissionHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> AccountPermissionsListResponseHttpRequest: ...

    @typing.type_check_only
    class AccountUserProfilesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            body: AccountUserProfile = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfileHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            active: bool = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            subaccountId: str = ...,
            userRoleId: str = ...,
            **kwargs: typing.Any
        ) -> AccountUserProfilesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccountUserProfilesListResponseHttpRequest,
            previous_response: AccountUserProfilesListResponse,
        ) -> AccountUserProfilesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
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

    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            active: bool = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> AccountsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AccountsListResponseHttpRequest,
            previous_response: AccountsListResponse,
        ) -> AccountsListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self, *, profileId: str, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...

    @typing.type_check_only
    class AdsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            active: bool = ...,
            advertiserId: str = ...,
            archived: bool = ...,
            audienceSegmentIds: str | _list[str] = ...,
            campaignIds: str | _list[str] = ...,
            compatibility: typing_extensions.Literal[
                "DISPLAY",
                "DISPLAY_INTERSTITIAL",
                "APP",
                "APP_INTERSTITIAL",
                "IN_STREAM_VIDEO",
                "IN_STREAM_AUDIO",
            ] = ...,
            creativeIds: str | _list[str] = ...,
            creativeOptimizationConfigurationIds: str | _list[str] = ...,
            dynamicClickTracker: bool = ...,
            ids: str | _list[str] = ...,
            landingPageIds: str | _list[str] = ...,
            maxResults: int = ...,
            overriddenEventTagId: str = ...,
            pageToken: str = ...,
            placementIds: str | _list[str] = ...,
            remarketingListIds: str | _list[str] = ...,
            searchString: str = ...,
            sizeIds: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            sslCompliant: bool = ...,
            sslRequired: bool = ...,
            type: typing_extensions.Literal[
                "AD_SERVING_STANDARD_AD",
                "AD_SERVING_DEFAULT_AD",
                "AD_SERVING_CLICK_TRACKER",
                "AD_SERVING_TRACKING",
                "AD_SERVING_BRAND_SAFE_AD",
            ]
            | _list[
                typing_extensions.Literal[
                    "AD_SERVING_STANDARD_AD",
                    "AD_SERVING_DEFAULT_AD",
                    "AD_SERVING_CLICK_TRACKER",
                    "AD_SERVING_TRACKING",
                    "AD_SERVING_BRAND_SAFE_AD",
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> AdsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AdsListResponseHttpRequest,
            previous_response: AdsListResponse,
        ) -> AdsListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...
        def update(
            self, *, profileId: str, body: Ad = ..., **kwargs: typing.Any
        ) -> AdHttpRequest: ...

    @typing.type_check_only
    class AdvertiserGroupsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def insert(
            self, *, profileId: str, body: AdvertiserGroup = ..., **kwargs: typing.Any
        ) -> AdvertiserGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> AdvertiserGroupsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AdvertiserGroupsListResponseHttpRequest,
            previous_response: AdvertiserGroupsListResponse,
        ) -> AdvertiserGroupsListResponseHttpRequest | None: ...
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

    @typing.type_check_only
    class AdvertiserLandingPagesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def insert(
            self, *, profileId: str, body: LandingPage = ..., **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserIds: str | _list[str] = ...,
            archived: bool = ...,
            campaignIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            subaccountId: str = ...,
            **kwargs: typing.Any
        ) -> AdvertiserLandingPagesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AdvertiserLandingPagesListResponseHttpRequest,
            previous_response: AdvertiserLandingPagesListResponse,
        ) -> AdvertiserLandingPagesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: LandingPage = ...,
            **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...
        def update(
            self, *, profileId: str, body: LandingPage = ..., **kwargs: typing.Any
        ) -> LandingPageHttpRequest: ...

    @typing.type_check_only
    class AdvertisersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserGroupIds: str | _list[str] = ...,
            floodlightConfigurationIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            includeAdvertisersWithoutGroupsOnly: bool = ...,
            maxResults: int = ...,
            onlyParent: bool = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            status: typing_extensions.Literal["APPROVED", "ON_HOLD"] = ...,
            subaccountId: str = ...,
            **kwargs: typing.Any
        ) -> AdvertisersListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: AdvertisersListResponseHttpRequest,
            previous_response: AdvertisersListResponse,
        ) -> AdvertisersListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: Advertiser = ...,
            **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def update(
            self, *, profileId: str, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...

    @typing.type_check_only
    class BrowsersResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> BrowsersListResponseHttpRequest: ...

    @typing.type_check_only
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
            maxResults: int = ...,
            pageToken: str = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> CampaignCreativeAssociationsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CampaignCreativeAssociationsListResponseHttpRequest,
            previous_response: CampaignCreativeAssociationsListResponse,
        ) -> CampaignCreativeAssociationsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class CampaignsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserGroupIds: str | _list[str] = ...,
            advertiserIds: str | _list[str] = ...,
            archived: bool = ...,
            atLeastOneOptimizationActivity: bool = ...,
            excludedIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            overriddenEventTagId: str = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            subaccountId: str = ...,
            **kwargs: typing.Any
        ) -> CampaignsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CampaignsListResponseHttpRequest,
            previous_response: CampaignsListResponse,
        ) -> CampaignsListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...
        def update(
            self, *, profileId: str, body: Campaign = ..., **kwargs: typing.Any
        ) -> CampaignHttpRequest: ...

    @typing.type_check_only
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
            ids: str | _list[str] = ...,
            maxChangeTime: str = ...,
            maxResults: int = ...,
            minChangeTime: str = ...,
            objectIds: str | _list[str] = ...,
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
                "OBJECT_ADVERTISER_CUSTOMER_LINK",
            ] = ...,
            pageToken: str = ...,
            searchString: str = ...,
            userProfileIds: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> ChangeLogsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ChangeLogsListResponseHttpRequest,
            previous_response: ChangeLogsListResponse,
        ) -> ChangeLogsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class CitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            profileId: str,
            countryDartIds: str | _list[str] = ...,
            dartIds: str | _list[str] = ...,
            namePrefix: str = ...,
            regionDartIds: str | _list[str] = ...,
            **kwargs: typing.Any
        ) -> CitiesListResponseHttpRequest: ...

    @typing.type_check_only
    class ConnectionTypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ConnectionTypeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> ConnectionTypesListResponseHttpRequest: ...

    @typing.type_check_only
    class ContentCategoriesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
        def insert(
            self, *, profileId: str, body: ContentCategory = ..., **kwargs: typing.Any
        ) -> ContentCategoryHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> ContentCategoriesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ContentCategoriesListResponseHttpRequest,
            previous_response: ContentCategoriesListResponse,
        ) -> ContentCategoriesListResponseHttpRequest | None: ...
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

    @typing.type_check_only
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

    @typing.type_check_only
    class CountriesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, dartId: str, **kwargs: typing.Any
        ) -> CountryHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> CountriesListResponseHttpRequest: ...

    @typing.type_check_only
    class CreativeAssetsResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            profileId: str,
            advertiserId: str,
            body: CreativeAssetMetadata = ...,
            **kwargs: typing.Any
        ) -> CreativeAssetMetadataHttpRequest: ...

    @typing.type_check_only
    class CreativeFieldValuesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, creativeFieldId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, creativeFieldId: str, id: str, **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            body: CreativeFieldValue = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValueHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            creativeFieldId: str,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "VALUE"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldValuesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativeFieldValuesListResponseHttpRequest,
            previous_response: CreativeFieldValuesListResponse,
        ) -> CreativeFieldValuesListResponseHttpRequest | None: ...
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

    @typing.type_check_only
    class CreativeFieldsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
            advertiserIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativeFieldsListResponseHttpRequest,
            previous_response: CreativeFieldsListResponse,
        ) -> CreativeFieldsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: CreativeField = ...,
            **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...
        def update(
            self, *, profileId: str, body: CreativeField = ..., **kwargs: typing.Any
        ) -> CreativeFieldHttpRequest: ...

    @typing.type_check_only
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
            advertiserIds: str | _list[str] = ...,
            groupNumber: int = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> CreativeGroupsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativeGroupsListResponseHttpRequest,
            previous_response: CreativeGroupsListResponse,
        ) -> CreativeGroupsListResponseHttpRequest | None: ...
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

    @typing.type_check_only
    class CreativesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            active: bool = ...,
            advertiserId: str = ...,
            archived: bool = ...,
            campaignId: str = ...,
            companionCreativeIds: str | _list[str] = ...,
            creativeFieldIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            renderingIds: str | _list[str] = ...,
            searchString: str = ...,
            sizeIds: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            studioCreativeId: str = ...,
            types: typing_extensions.Literal[
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
            | _list[
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
            ] = ...,
            **kwargs: typing.Any
        ) -> CreativesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativesListResponseHttpRequest,
            previous_response: CreativesListResponse,
        ) -> CreativesListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def update(
            self, *, profileId: str, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...

    @typing.type_check_only
    class DimensionValuesResource(googleapiclient.discovery.Resource):
        def query(
            self,
            *,
            profileId: str,
            body: DimensionValueRequest = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DimensionValueListHttpRequest: ...
        def query_next(
            self,
            previous_request: DimensionValueListHttpRequest,
            previous_response: DimensionValueList,
        ) -> DimensionValueListHttpRequest | None: ...

    @typing.type_check_only
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
            acceptsInStreamVideoPlacements: bool = ...,
            acceptsInterstitialPlacements: bool = ...,
            acceptsPublisherPaidPlacements: bool = ...,
            active: bool = ...,
            dfpNetworkCode: str = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> DirectorySitesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DirectorySitesListResponseHttpRequest,
            previous_response: DirectorySitesListResponse,
        ) -> DirectorySitesListResponseHttpRequest | None: ...

    @typing.type_check_only
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
            advertiserId: str = ...,
            names: str | _list[str] = ...,
            objectId: str = ...,
            objectType: typing_extensions.Literal[
                "OBJECT_ADVERTISER", "OBJECT_AD", "OBJECT_CREATIVE", "OBJECT_PLACEMENT"
            ] = ...,
            **kwargs: typing.Any
        ) -> DynamicTargetingKeysListResponseHttpRequest: ...

    @typing.type_check_only
    class EventTagsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def insert(
            self, *, profileId: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            adId: str = ...,
            advertiserId: str = ...,
            campaignId: str = ...,
            definitionsOnly: bool = ...,
            enabled: bool = ...,
            eventTagTypes: typing_extensions.Literal[
                "IMPRESSION_IMAGE_EVENT_TAG",
                "IMPRESSION_JAVASCRIPT_EVENT_TAG",
                "CLICK_THROUGH_EVENT_TAG",
            ]
            | _list[
                typing_extensions.Literal[
                    "IMPRESSION_IMAGE_EVENT_TAG",
                    "IMPRESSION_JAVASCRIPT_EVENT_TAG",
                    "CLICK_THROUGH_EVENT_TAG",
                ]
            ] = ...,
            ids: str | _list[str] = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> EventTagsListResponseHttpRequest: ...
        def patch(
            self, *, profileId: str, id: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...
        def update(
            self, *, profileId: str, body: EventTag = ..., **kwargs: typing.Any
        ) -> EventTagHttpRequest: ...

    @typing.type_check_only
    class FilesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, reportId: str, fileId: str, **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            scope: typing_extensions.Literal["ALL", "MINE", "SHARED_WITH_ME"] = ...,
            sortField: typing_extensions.Literal["ID", "LAST_MODIFIED_TIME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> FileListHttpRequest: ...
        def list_next(
            self, previous_request: FileListHttpRequest, previous_response: FileList
        ) -> FileListHttpRequest | None: ...

    @typing.type_check_only
    class FloodlightActivitiesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def generatetag(
            self,
            *,
            profileId: str,
            floodlightActivityId: str = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivitiesGenerateTagResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def insert(
            self,
            *,
            profileId: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str = ...,
            floodlightActivityGroupIds: str | _list[str] = ...,
            floodlightActivityGroupName: str = ...,
            floodlightActivityGroupTagString: str = ...,
            floodlightActivityGroupType: typing_extensions.Literal[
                "COUNTER", "SALE"
            ] = ...,
            floodlightConfigurationId: str = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            tagString: str = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivitiesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: FloodlightActivitiesListResponseHttpRequest,
            previous_response: FloodlightActivitiesListResponse,
        ) -> FloodlightActivitiesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: FloodlightActivity = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityHttpRequest: ...

    @typing.type_check_only
    class FloodlightActivityGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightActivityGroupHttpRequest: ...
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
            advertiserId: str = ...,
            floodlightConfigurationId: str = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            type: typing_extensions.Literal["COUNTER", "SALE"] = ...,
            **kwargs: typing.Any
        ) -> FloodlightActivityGroupsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: FloodlightActivityGroupsListResponseHttpRequest,
            previous_response: FloodlightActivityGroupsListResponse,
        ) -> FloodlightActivityGroupsListResponseHttpRequest | None: ...
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

    @typing.type_check_only
    class FloodlightConfigurationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...
        def list(
            self, *, profileId: str, ids: str | _list[str] = ..., **kwargs: typing.Any
        ) -> FloodlightConfigurationsListResponseHttpRequest: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: FloodlightConfiguration = ...,
            **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            body: FloodlightConfiguration = ...,
            **kwargs: typing.Any
        ) -> FloodlightConfigurationHttpRequest: ...

    @typing.type_check_only
    class InventoryItemsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> InventoryItemHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            ids: str | _list[str] = ...,
            inPlan: bool = ...,
            maxResults: int = ...,
            orderId: str | _list[str] = ...,
            pageToken: str = ...,
            siteId: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            type: typing_extensions.Literal[
                "PLANNING_PLACEMENT_TYPE_REGULAR", "PLANNING_PLACEMENT_TYPE_CREDIT"
            ] = ...,
            **kwargs: typing.Any
        ) -> InventoryItemsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: InventoryItemsListResponseHttpRequest,
            previous_response: InventoryItemsListResponse,
        ) -> InventoryItemsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class LanguagesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> LanguagesListResponseHttpRequest: ...

    @typing.type_check_only
    class MetrosResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> MetrosListResponseHttpRequest: ...

    @typing.type_check_only
    class MobileAppsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> MobileAppHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            directories: typing_extensions.Literal[
                "UNKNOWN",
                "APPLE_APP_STORE",
                "GOOGLE_PLAY_STORE",
                "ROKU_APP_STORE",
                "AMAZON_FIRETV_APP_STORE",
                "PLAYSTATION_APP_STORE",
                "APPLE_TV_APP_STORE",
                "XBOX_APP_STORE",
                "SAMSUNG_TV_APP_STORE",
                "ANDROID_TV_APP_STORE",
                "GENERIC_CTV_APP_STORE",
            ]
            | _list[
                typing_extensions.Literal[
                    "UNKNOWN",
                    "APPLE_APP_STORE",
                    "GOOGLE_PLAY_STORE",
                    "ROKU_APP_STORE",
                    "AMAZON_FIRETV_APP_STORE",
                    "PLAYSTATION_APP_STORE",
                    "APPLE_TV_APP_STORE",
                    "XBOX_APP_STORE",
                    "SAMSUNG_TV_APP_STORE",
                    "ANDROID_TV_APP_STORE",
                    "GENERIC_CTV_APP_STORE",
                ]
            ] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            **kwargs: typing.Any
        ) -> MobileAppsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: MobileAppsListResponseHttpRequest,
            previous_response: MobileAppsListResponse,
        ) -> MobileAppsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class MobileCarriersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> MobileCarrierHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> MobileCarriersListResponseHttpRequest: ...

    @typing.type_check_only
    class OperatingSystemVersionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> OperatingSystemVersionHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> OperatingSystemVersionsListResponseHttpRequest: ...

    @typing.type_check_only
    class OperatingSystemsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, dartId: str, **kwargs: typing.Any
        ) -> OperatingSystemHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> OperatingSystemsListResponseHttpRequest: ...

    @typing.type_check_only
    class OrderDocumentsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> OrderDocumentHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            approved: bool = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            orderId: str | _list[str] = ...,
            pageToken: str = ...,
            searchString: str = ...,
            siteId: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> OrderDocumentsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OrderDocumentsListResponseHttpRequest,
            previous_response: OrderDocumentsListResponse,
        ) -> OrderDocumentsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrdersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, projectId: str, id: str, **kwargs: typing.Any
        ) -> OrderHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            projectId: str,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            siteId: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> OrdersListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OrdersListResponseHttpRequest,
            previous_response: OrdersListResponse,
        ) -> OrdersListResponseHttpRequest | None: ...

    @typing.type_check_only
    class PlacementGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def insert(
            self, *, profileId: str, body: PlacementGroup = ..., **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserIds: str | _list[str] = ...,
            archived: bool = ...,
            campaignIds: str | _list[str] = ...,
            contentCategoryIds: str | _list[str] = ...,
            directorySiteIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxEndDate: str = ...,
            maxResults: int = ...,
            maxStartDate: str = ...,
            minEndDate: str = ...,
            minStartDate: str = ...,
            pageToken: str = ...,
            placementGroupType: typing_extensions.Literal[
                "PLACEMENT_PACKAGE", "PLACEMENT_ROADBLOCK"
            ] = ...,
            placementStrategyIds: str | _list[str] = ...,
            pricingTypes: typing_extensions.Literal[
                "PRICING_TYPE_CPM",
                "PRICING_TYPE_CPC",
                "PRICING_TYPE_CPA",
                "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                "PRICING_TYPE_FLAT_RATE_CLICKS",
                "PRICING_TYPE_CPM_ACTIVEVIEW",
            ]
            | _list[
                typing_extensions.Literal[
                    "PRICING_TYPE_CPM",
                    "PRICING_TYPE_CPC",
                    "PRICING_TYPE_CPA",
                    "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                    "PRICING_TYPE_FLAT_RATE_CLICKS",
                    "PRICING_TYPE_CPM_ACTIVEVIEW",
                ]
            ] = ...,
            searchString: str = ...,
            siteIds: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> PlacementGroupsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlacementGroupsListResponseHttpRequest,
            previous_response: PlacementGroupsListResponse,
        ) -> PlacementGroupsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: PlacementGroup = ...,
            **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...
        def update(
            self, *, profileId: str, body: PlacementGroup = ..., **kwargs: typing.Any
        ) -> PlacementGroupHttpRequest: ...

    @typing.type_check_only
    class PlacementStrategiesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def insert(
            self, *, profileId: str, body: PlacementStrategy = ..., **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> PlacementStrategiesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlacementStrategiesListResponseHttpRequest,
            previous_response: PlacementStrategiesListResponse,
        ) -> PlacementStrategiesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: PlacementStrategy = ...,
            **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...
        def update(
            self, *, profileId: str, body: PlacementStrategy = ..., **kwargs: typing.Any
        ) -> PlacementStrategyHttpRequest: ...

    @typing.type_check_only
    class PlacementsResource(googleapiclient.discovery.Resource):
        def generatetags(
            self,
            *,
            profileId: str,
            campaignId: str = ...,
            placementIds: str | _list[str] = ...,
            tagFormats: typing_extensions.Literal[
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
                "PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT",
            ]
            | _list[
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
                    "PLACEMENT_TAG_TRACKING_THIRD_PARTY_MEASUREMENT",
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> PlacementsGenerateTagsResponseHttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Placement = ..., **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserIds: str | _list[str] = ...,
            archived: bool = ...,
            campaignIds: str | _list[str] = ...,
            compatibilities: typing_extensions.Literal[
                "DISPLAY",
                "DISPLAY_INTERSTITIAL",
                "APP",
                "APP_INTERSTITIAL",
                "IN_STREAM_VIDEO",
                "IN_STREAM_AUDIO",
            ]
            | _list[
                typing_extensions.Literal[
                    "DISPLAY",
                    "DISPLAY_INTERSTITIAL",
                    "APP",
                    "APP_INTERSTITIAL",
                    "IN_STREAM_VIDEO",
                    "IN_STREAM_AUDIO",
                ]
            ] = ...,
            contentCategoryIds: str | _list[str] = ...,
            directorySiteIds: str | _list[str] = ...,
            groupIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxEndDate: str = ...,
            maxResults: int = ...,
            maxStartDate: str = ...,
            minEndDate: str = ...,
            minStartDate: str = ...,
            pageToken: str = ...,
            paymentSource: typing_extensions.Literal[
                "PLACEMENT_AGENCY_PAID", "PLACEMENT_PUBLISHER_PAID"
            ] = ...,
            placementStrategyIds: str | _list[str] = ...,
            pricingTypes: typing_extensions.Literal[
                "PRICING_TYPE_CPM",
                "PRICING_TYPE_CPC",
                "PRICING_TYPE_CPA",
                "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                "PRICING_TYPE_FLAT_RATE_CLICKS",
                "PRICING_TYPE_CPM_ACTIVEVIEW",
            ]
            | _list[
                typing_extensions.Literal[
                    "PRICING_TYPE_CPM",
                    "PRICING_TYPE_CPC",
                    "PRICING_TYPE_CPA",
                    "PRICING_TYPE_FLAT_RATE_IMPRESSIONS",
                    "PRICING_TYPE_FLAT_RATE_CLICKS",
                    "PRICING_TYPE_CPM_ACTIVEVIEW",
                ]
            ] = ...,
            searchString: str = ...,
            siteIds: str | _list[str] = ...,
            sizeIds: str | _list[str] = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> PlacementsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: PlacementsListResponseHttpRequest,
            previous_response: PlacementsListResponse,
        ) -> PlacementsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: Placement = ...,
            **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...
        def update(
            self, *, profileId: str, body: Placement = ..., **kwargs: typing.Any
        ) -> PlacementHttpRequest: ...

    @typing.type_check_only
    class PlatformTypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> PlatformTypeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> PlatformTypesListResponseHttpRequest: ...

    @typing.type_check_only
    class PostalCodesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, code: str, **kwargs: typing.Any
        ) -> PostalCodeHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> PostalCodesListResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> ProjectsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ProjectsListResponseHttpRequest,
            previous_response: ProjectsListResponse,
        ) -> ProjectsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class RegionsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> RegionsListResponseHttpRequest: ...

    @typing.type_check_only
    class RemarketingListSharesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, remarketingListId: str, **kwargs: typing.Any
        ) -> RemarketingListShareHttpRequest: ...
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

    @typing.type_check_only
    class RemarketingListsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def insert(
            self, *, profileId: str, body: RemarketingList = ..., **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str,
            active: bool = ...,
            floodlightActivityId: str = ...,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> RemarketingListsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: RemarketingListsListResponseHttpRequest,
            previous_response: RemarketingListsListResponse,
        ) -> RemarketingListsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: RemarketingList = ...,
            **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...
        def update(
            self, *, profileId: str, body: RemarketingList = ..., **kwargs: typing.Any
        ) -> RemarketingListHttpRequest: ...

    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CompatibleFieldsResource(googleapiclient.discovery.Resource):
            def query(
                self, *, profileId: str, body: Report = ..., **kwargs: typing.Any
            ) -> CompatibleFieldsHttpRequest: ...

        @typing.type_check_only
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
                maxResults: int = ...,
                pageToken: str = ...,
                sortField: typing_extensions.Literal["ID", "LAST_MODIFIED_TIME"] = ...,
                sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
                **kwargs: typing.Any
            ) -> FileListHttpRequest: ...
            def list_next(
                self, previous_request: FileListHttpRequest, previous_response: FileList
            ) -> FileListHttpRequest | None: ...

        def delete(
            self, *, profileId: str, reportId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, reportId: str, **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Report = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            scope: typing_extensions.Literal["ALL", "MINE"] = ...,
            sortField: typing_extensions.Literal[
                "ID", "LAST_MODIFIED_TIME", "NAME"
            ] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> ReportListHttpRequest: ...
        def list_next(
            self, previous_request: ReportListHttpRequest, previous_response: ReportList
        ) -> ReportListHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            reportId: str,
            body: Report = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def run(
            self,
            *,
            profileId: str,
            reportId: str,
            synchronous: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def update(
            self,
            *,
            profileId: str,
            reportId: str,
            body: Report = ...,
            **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def compatibleFields(self) -> CompatibleFieldsResource: ...
        def files(self) -> FilesResource: ...

    @typing.type_check_only
    class SitesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def insert(
            self, *, profileId: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            acceptsInStreamVideoPlacements: bool = ...,
            acceptsInterstitialPlacements: bool = ...,
            acceptsPublisherPaidPlacements: bool = ...,
            adWordsSite: bool = ...,
            approved: bool = ...,
            campaignIds: str | _list[str] = ...,
            directorySiteIds: str | _list[str] = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            subaccountId: str = ...,
            unmappedSite: bool = ...,
            **kwargs: typing.Any
        ) -> SitesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SitesListResponseHttpRequest,
            previous_response: SitesListResponse,
        ) -> SitesListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...
        def update(
            self, *, profileId: str, body: Site = ..., **kwargs: typing.Any
        ) -> SiteHttpRequest: ...

    @typing.type_check_only
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
            height: int = ...,
            iabStandard: bool = ...,
            ids: str | _list[str] = ...,
            width: int = ...,
            **kwargs: typing.Any
        ) -> SizesListResponseHttpRequest: ...

    @typing.type_check_only
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
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> SubaccountsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: SubaccountsListResponseHttpRequest,
            previous_response: SubaccountsListResponse,
        ) -> SubaccountsListResponseHttpRequest | None: ...
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

    @typing.type_check_only
    class TargetableRemarketingListsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> TargetableRemarketingListHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str,
            active: bool = ...,
            maxResults: int = ...,
            name: str = ...,
            pageToken: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> TargetableRemarketingListsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: TargetableRemarketingListsListResponseHttpRequest,
            previous_response: TargetableRemarketingListsListResponse,
        ) -> TargetableRemarketingListsListResponseHttpRequest | None: ...

    @typing.type_check_only
    class TargetingTemplatesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def insert(
            self, *, profileId: str, body: TargetingTemplate = ..., **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            advertiserId: str = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            **kwargs: typing.Any
        ) -> TargetingTemplatesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: TargetingTemplatesListResponseHttpRequest,
            previous_response: TargetingTemplatesListResponse,
        ) -> TargetingTemplatesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            profileId: str,
            id: str,
            body: TargetingTemplate = ...,
            **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...
        def update(
            self, *, profileId: str, body: TargetingTemplate = ..., **kwargs: typing.Any
        ) -> TargetingTemplateHttpRequest: ...

    @typing.type_check_only
    class UserProfilesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> UserProfileHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> UserProfileListHttpRequest: ...

    @typing.type_check_only
    class UserRolePermissionGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRolePermissionGroupHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> UserRolePermissionGroupsListResponseHttpRequest: ...

    @typing.type_check_only
    class UserRolePermissionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRolePermissionHttpRequest: ...
        def list(
            self, *, profileId: str, ids: str | _list[str] = ..., **kwargs: typing.Any
        ) -> UserRolePermissionsListResponseHttpRequest: ...

    @typing.type_check_only
    class UserRolesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, profileId: str, id: str, **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def insert(
            self, *, profileId: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def list(
            self,
            *,
            profileId: str,
            accountUserRoleOnly: bool = ...,
            ids: str | _list[str] = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            searchString: str = ...,
            sortField: typing_extensions.Literal["ID", "NAME"] = ...,
            sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"] = ...,
            subaccountId: str = ...,
            **kwargs: typing.Any
        ) -> UserRolesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: UserRolesListResponseHttpRequest,
            previous_response: UserRolesListResponse,
        ) -> UserRolesListResponseHttpRequest | None: ...
        def patch(
            self, *, profileId: str, id: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...
        def update(
            self, *, profileId: str, body: UserRole = ..., **kwargs: typing.Any
        ) -> UserRoleHttpRequest: ...

    @typing.type_check_only
    class VideoFormatsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, profileId: str, id: int, **kwargs: typing.Any
        ) -> VideoFormatHttpRequest: ...
        def list(
            self, *, profileId: str, **kwargs: typing.Any
        ) -> VideoFormatsListResponseHttpRequest: ...

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
    def accountActiveAdSummaries(self) -> AccountActiveAdSummariesResource: ...
    def accountPermissionGroups(self) -> AccountPermissionGroupsResource: ...
    def accountPermissions(self) -> AccountPermissionsResource: ...
    def accountUserProfiles(self) -> AccountUserProfilesResource: ...
    def accounts(self) -> AccountsResource: ...
    def ads(self) -> AdsResource: ...
    def advertiserGroups(self) -> AdvertiserGroupsResource: ...
    def advertiserLandingPages(self) -> AdvertiserLandingPagesResource: ...
    def advertisers(self) -> AdvertisersResource: ...
    def browsers(self) -> BrowsersResource: ...
    def campaignCreativeAssociations(self) -> CampaignCreativeAssociationsResource: ...
    def campaigns(self) -> CampaignsResource: ...
    def changeLogs(self) -> ChangeLogsResource: ...
    def cities(self) -> CitiesResource: ...
    def connectionTypes(self) -> ConnectionTypesResource: ...
    def contentCategories(self) -> ContentCategoriesResource: ...
    def conversions(self) -> ConversionsResource: ...
    def countries(self) -> CountriesResource: ...
    def creativeAssets(self) -> CreativeAssetsResource: ...
    def creativeFieldValues(self) -> CreativeFieldValuesResource: ...
    def creativeFields(self) -> CreativeFieldsResource: ...
    def creativeGroups(self) -> CreativeGroupsResource: ...
    def creatives(self) -> CreativesResource: ...
    def dimensionValues(self) -> DimensionValuesResource: ...
    def directorySites(self) -> DirectorySitesResource: ...
    def dynamicTargetingKeys(self) -> DynamicTargetingKeysResource: ...
    def eventTags(self) -> EventTagsResource: ...
    def files(self) -> FilesResource: ...
    def floodlightActivities(self) -> FloodlightActivitiesResource: ...
    def floodlightActivityGroups(self) -> FloodlightActivityGroupsResource: ...
    def floodlightConfigurations(self) -> FloodlightConfigurationsResource: ...
    def inventoryItems(self) -> InventoryItemsResource: ...
    def languages(self) -> LanguagesResource: ...
    def metros(self) -> MetrosResource: ...
    def mobileApps(self) -> MobileAppsResource: ...
    def mobileCarriers(self) -> MobileCarriersResource: ...
    def operatingSystemVersions(self) -> OperatingSystemVersionsResource: ...
    def operatingSystems(self) -> OperatingSystemsResource: ...
    def orderDocuments(self) -> OrderDocumentsResource: ...
    def orders(self) -> OrdersResource: ...
    def placementGroups(self) -> PlacementGroupsResource: ...
    def placementStrategies(self) -> PlacementStrategiesResource: ...
    def placements(self) -> PlacementsResource: ...
    def platformTypes(self) -> PlatformTypesResource: ...
    def postalCodes(self) -> PostalCodesResource: ...
    def projects(self) -> ProjectsResource: ...
    def regions(self) -> RegionsResource: ...
    def remarketingListShares(self) -> RemarketingListSharesResource: ...
    def remarketingLists(self) -> RemarketingListsResource: ...
    def reports(self) -> ReportsResource: ...
    def sites(self) -> SitesResource: ...
    def sizes(self) -> SizesResource: ...
    def subaccounts(self) -> SubaccountsResource: ...
    def targetableRemarketingLists(self) -> TargetableRemarketingListsResource: ...
    def targetingTemplates(self) -> TargetingTemplatesResource: ...
    def userProfiles(self) -> UserProfilesResource: ...
    def userRolePermissionGroups(self) -> UserRolePermissionGroupsResource: ...
    def userRolePermissions(self) -> UserRolePermissionsResource: ...
    def userRoles(self) -> UserRolesResource: ...
    def videoFormats(self) -> VideoFormatsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AccountActiveAdSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountActiveAdSummary: ...

@typing.type_check_only
class AccountPermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountPermission: ...

@typing.type_check_only
class AccountPermissionGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountPermissionGroup: ...

@typing.type_check_only
class AccountPermissionGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountPermissionGroupsListResponse: ...

@typing.type_check_only
class AccountPermissionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountPermissionsListResponse: ...

@typing.type_check_only
class AccountUserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountUserProfile: ...

@typing.type_check_only
class AccountUserProfilesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountUserProfilesListResponse: ...

@typing.type_check_only
class AccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsListResponse: ...

@typing.type_check_only
class AdHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Ad: ...

@typing.type_check_only
class AdsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdsListResponse: ...

@typing.type_check_only
class AdvertiserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Advertiser: ...

@typing.type_check_only
class AdvertiserGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdvertiserGroup: ...

@typing.type_check_only
class AdvertiserGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdvertiserGroupsListResponse: ...

@typing.type_check_only
class AdvertiserLandingPagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdvertiserLandingPagesListResponse: ...

@typing.type_check_only
class AdvertisersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AdvertisersListResponse: ...

@typing.type_check_only
class BrowsersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BrowsersListResponse: ...

@typing.type_check_only
class CampaignHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Campaign: ...

@typing.type_check_only
class CampaignCreativeAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CampaignCreativeAssociation: ...

@typing.type_check_only
class CampaignCreativeAssociationsListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CampaignCreativeAssociationsListResponse: ...

@typing.type_check_only
class CampaignsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CampaignsListResponse: ...

@typing.type_check_only
class ChangeLogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChangeLog: ...

@typing.type_check_only
class ChangeLogsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChangeLogsListResponse: ...

@typing.type_check_only
class CitiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CitiesListResponse: ...

@typing.type_check_only
class CompatibleFieldsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CompatibleFields: ...

@typing.type_check_only
class ConnectionTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectionType: ...

@typing.type_check_only
class ConnectionTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConnectionTypesListResponse: ...

@typing.type_check_only
class ContentCategoriesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ContentCategoriesListResponse: ...

@typing.type_check_only
class ContentCategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ContentCategory: ...

@typing.type_check_only
class ConversionsBatchInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConversionsBatchInsertResponse: ...

@typing.type_check_only
class ConversionsBatchUpdateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConversionsBatchUpdateResponse: ...

@typing.type_check_only
class CountriesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CountriesListResponse: ...

@typing.type_check_only
class CountryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Country: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Creative: ...

@typing.type_check_only
class CreativeAssetMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeAssetMetadata: ...

@typing.type_check_only
class CreativeFieldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeField: ...

@typing.type_check_only
class CreativeFieldValueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeFieldValue: ...

@typing.type_check_only
class CreativeFieldValuesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeFieldValuesListResponse: ...

@typing.type_check_only
class CreativeFieldsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeFieldsListResponse: ...

@typing.type_check_only
class CreativeGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeGroup: ...

@typing.type_check_only
class CreativeGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeGroupsListResponse: ...

@typing.type_check_only
class CreativesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativesListResponse: ...

@typing.type_check_only
class DimensionValueListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DimensionValueList: ...

@typing.type_check_only
class DirectorySiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectorySite: ...

@typing.type_check_only
class DirectorySitesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DirectorySitesListResponse: ...

@typing.type_check_only
class DynamicTargetingKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DynamicTargetingKey: ...

@typing.type_check_only
class DynamicTargetingKeysListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DynamicTargetingKeysListResponse: ...

@typing.type_check_only
class EventTagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EventTag: ...

@typing.type_check_only
class EventTagsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EventTagsListResponse: ...

@typing.type_check_only
class FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> File: ...

@typing.type_check_only
class FileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FileList: ...

@typing.type_check_only
class FloodlightActivitiesGenerateTagResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightActivitiesGenerateTagResponse: ...

@typing.type_check_only
class FloodlightActivitiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightActivitiesListResponse: ...

@typing.type_check_only
class FloodlightActivityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightActivity: ...

@typing.type_check_only
class FloodlightActivityGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightActivityGroup: ...

@typing.type_check_only
class FloodlightActivityGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightActivityGroupsListResponse: ...

@typing.type_check_only
class FloodlightConfigurationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightConfiguration: ...

@typing.type_check_only
class FloodlightConfigurationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FloodlightConfigurationsListResponse: ...

@typing.type_check_only
class InventoryItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InventoryItem: ...

@typing.type_check_only
class InventoryItemsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InventoryItemsListResponse: ...

@typing.type_check_only
class LandingPageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LandingPage: ...

@typing.type_check_only
class LanguagesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LanguagesListResponse: ...

@typing.type_check_only
class MetrosListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MetrosListResponse: ...

@typing.type_check_only
class MobileAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileApp: ...

@typing.type_check_only
class MobileAppsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileAppsListResponse: ...

@typing.type_check_only
class MobileCarrierHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileCarrier: ...

@typing.type_check_only
class MobileCarriersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MobileCarriersListResponse: ...

@typing.type_check_only
class OperatingSystemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperatingSystem: ...

@typing.type_check_only
class OperatingSystemVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperatingSystemVersion: ...

@typing.type_check_only
class OperatingSystemVersionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperatingSystemVersionsListResponse: ...

@typing.type_check_only
class OperatingSystemsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperatingSystemsListResponse: ...

@typing.type_check_only
class OrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Order: ...

@typing.type_check_only
class OrderDocumentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderDocument: ...

@typing.type_check_only
class OrderDocumentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrderDocumentsListResponse: ...

@typing.type_check_only
class OrdersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrdersListResponse: ...

@typing.type_check_only
class PlacementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Placement: ...

@typing.type_check_only
class PlacementGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementGroup: ...

@typing.type_check_only
class PlacementGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementGroupsListResponse: ...

@typing.type_check_only
class PlacementStrategiesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementStrategiesListResponse: ...

@typing.type_check_only
class PlacementStrategyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementStrategy: ...

@typing.type_check_only
class PlacementsGenerateTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementsGenerateTagsResponse: ...

@typing.type_check_only
class PlacementsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlacementsListResponse: ...

@typing.type_check_only
class PlatformTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlatformType: ...

@typing.type_check_only
class PlatformTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PlatformTypesListResponse: ...

@typing.type_check_only
class PostalCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PostalCode: ...

@typing.type_check_only
class PostalCodesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PostalCodesListResponse: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Project: ...

@typing.type_check_only
class ProjectsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProjectsListResponse: ...

@typing.type_check_only
class RegionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionsListResponse: ...

@typing.type_check_only
class RemarketingListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RemarketingList: ...

@typing.type_check_only
class RemarketingListShareHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RemarketingListShare: ...

@typing.type_check_only
class RemarketingListsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RemarketingListsListResponse: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Report: ...

@typing.type_check_only
class ReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReportList: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Site: ...

@typing.type_check_only
class SitesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SitesListResponse: ...

@typing.type_check_only
class SizeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Size: ...

@typing.type_check_only
class SizesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SizesListResponse: ...

@typing.type_check_only
class SubaccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subaccount: ...

@typing.type_check_only
class SubaccountsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubaccountsListResponse: ...

@typing.type_check_only
class TargetableRemarketingListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetableRemarketingList: ...

@typing.type_check_only
class TargetableRemarketingListsListResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetableRemarketingListsListResponse: ...

@typing.type_check_only
class TargetingTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetingTemplate: ...

@typing.type_check_only
class TargetingTemplatesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetingTemplatesListResponse: ...

@typing.type_check_only
class UserProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserProfile: ...

@typing.type_check_only
class UserProfileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserProfileList: ...

@typing.type_check_only
class UserRoleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRole: ...

@typing.type_check_only
class UserRolePermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRolePermission: ...

@typing.type_check_only
class UserRolePermissionGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRolePermissionGroup: ...

@typing.type_check_only
class UserRolePermissionGroupsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRolePermissionGroupsListResponse: ...

@typing.type_check_only
class UserRolePermissionsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRolePermissionsListResponse: ...

@typing.type_check_only
class UserRolesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserRolesListResponse: ...

@typing.type_check_only
class VideoFormatHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VideoFormat: ...

@typing.type_check_only
class VideoFormatsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VideoFormatsListResponse: ...
