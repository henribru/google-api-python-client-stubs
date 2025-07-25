import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DisplayVideoResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AdvertisersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdGroupAdsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, advertiserId: str, adGroupAdId: str, **kwargs: typing.Any
            ) -> AdGroupAdHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAdGroupAdsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdGroupAdsResponseHttpRequest,
                previous_response: ListAdGroupAdsResponse,
            ) -> ListAdGroupAdsResponseHttpRequest | None: ...

        @typing.type_check_only
        class AdGroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TargetingTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AssignedTargetingOptionsResource(
                    googleapiclient.discovery.Resource
                ):
                    def get(
                        self,
                        *,
                        advertiserId: str,
                        adGroupId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        assignedTargetingOptionId: str,
                        **kwargs: typing.Any,
                    ) -> AssignedTargetingOptionHttpRequest: ...
                    def list(
                        self,
                        *,
                        advertiserId: str,
                        adGroupId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAdGroupAssignedTargetingOptionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAdGroupAssignedTargetingOptionsResponseHttpRequest,
                        previous_response: ListAdGroupAssignedTargetingOptionsResponse,
                    ) -> (
                        ListAdGroupAssignedTargetingOptionsResponseHttpRequest | None
                    ): ...

                def assignedTargetingOptions(
                    self,
                ) -> AssignedTargetingOptionsResource: ...

            def bulkListAssignedTargetingOptions(
                self,
                *,
                advertiserId: str,
                adGroupIds: str | _list[str] = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> BulkListAdGroupAssignedTargetingOptionsResponseHttpRequest: ...
            def bulkListAssignedTargetingOptions_next(
                self,
                previous_request: BulkListAdGroupAssignedTargetingOptionsResponseHttpRequest,
                previous_response: BulkListAdGroupAssignedTargetingOptionsResponse,
            ) -> BulkListAdGroupAssignedTargetingOptionsResponseHttpRequest | None: ...
            def get(
                self, *, advertiserId: str, adGroupId: str, **kwargs: typing.Any
            ) -> AdGroupHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAdGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAdGroupsResponseHttpRequest,
                previous_response: ListAdGroupsResponse,
            ) -> ListAdGroupsResponseHttpRequest | None: ...
            def targetingTypes(self) -> TargetingTypesResource: ...

        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def upload(
                self,
                *,
                advertiserId: str,
                body: CreateAssetRequest = ...,
                **kwargs: typing.Any,
            ) -> CreateAssetResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, advertiserId: str, body: Campaign = ..., **kwargs: typing.Any
            ) -> CampaignHttpRequest: ...
            def delete(
                self, *, advertiserId: str, campaignId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, advertiserId: str, campaignId: str, **kwargs: typing.Any
            ) -> CampaignHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCampaignsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCampaignsResponseHttpRequest,
                previous_response: ListCampaignsResponse,
            ) -> ListCampaignsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                campaignId: str,
                body: Campaign = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> CampaignHttpRequest: ...

        @typing.type_check_only
        class ChannelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SitesResource(googleapiclient.discovery.Resource):
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    body: BulkEditSitesRequest = ...,
                    **kwargs: typing.Any,
                ) -> BulkEditSitesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    body: Site = ...,
                    partnerId: str = ...,
                    **kwargs: typing.Any,
                ) -> SiteHttpRequest: ...
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    urlOrAppId: str,
                    partnerId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    partnerId: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSitesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSitesResponseHttpRequest,
                    previous_response: ListSitesResponse,
                ) -> ListSitesResponseHttpRequest | None: ...
                def replace(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    body: ReplaceSitesRequest = ...,
                    **kwargs: typing.Any,
                ) -> ReplaceSitesResponseHttpRequest: ...

            def create(
                self,
                *,
                advertiserId: str,
                body: Channel = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def get(
                self,
                *,
                advertiserId: str,
                channelId: str,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ListChannelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListChannelsResponseHttpRequest,
                previous_response: ListChannelsResponse,
            ) -> ListChannelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                channelId: str,
                body: Channel = ...,
                partnerId: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def sites(self) -> SitesResource: ...

        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, advertiserId: str, body: Creative = ..., **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def delete(
                self, *, advertiserId: str, creativeId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, advertiserId: str, creativeId: str, **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListCreativesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCreativesResponseHttpRequest,
                previous_response: ListCreativesResponse,
            ) -> ListCreativesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                creativeId: str,
                body: Creative = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> CreativeHttpRequest: ...

        @typing.type_check_only
        class InsertionOrdersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                advertiserId: str,
                body: InsertionOrder = ...,
                **kwargs: typing.Any,
            ) -> InsertionOrderHttpRequest: ...
            def delete(
                self, *, advertiserId: str, insertionOrderId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, advertiserId: str, insertionOrderId: str, **kwargs: typing.Any
            ) -> InsertionOrderHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListInsertionOrdersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInsertionOrdersResponseHttpRequest,
                previous_response: ListInsertionOrdersResponse,
            ) -> ListInsertionOrdersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                insertionOrderId: str,
                body: InsertionOrder = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> InsertionOrderHttpRequest: ...

        @typing.type_check_only
        class InvoicesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                advertiserId: str,
                issueMonth: str = ...,
                loiSapinInvoiceType: typing_extensions.Literal[
                    "LOI_SAPIN_INVOICE_TYPE_UNSPECIFIED",
                    "LOI_SAPIN_INVOICE_TYPE_MEDIA",
                    "LOI_SAPIN_INVOICE_TYPE_PLATFORM",
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListInvoicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListInvoicesResponseHttpRequest,
                previous_response: ListInvoicesResponse,
            ) -> ListInvoicesResponseHttpRequest | None: ...
            def lookupInvoiceCurrency(
                self,
                *,
                advertiserId: str,
                invoiceMonth: str = ...,
                **kwargs: typing.Any,
            ) -> LookupInvoiceCurrencyResponseHttpRequest: ...

        @typing.type_check_only
        class LineItemsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class TargetingTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AssignedTargetingOptionsResource(
                    googleapiclient.discovery.Resource
                ):
                    def create(
                        self,
                        *,
                        advertiserId: str,
                        lineItemId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        body: AssignedTargetingOption = ...,
                        **kwargs: typing.Any,
                    ) -> AssignedTargetingOptionHttpRequest: ...
                    def delete(
                        self,
                        *,
                        advertiserId: str,
                        lineItemId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        assignedTargetingOptionId: str,
                        **kwargs: typing.Any,
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        advertiserId: str,
                        lineItemId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        assignedTargetingOptionId: str,
                        **kwargs: typing.Any,
                    ) -> AssignedTargetingOptionHttpRequest: ...
                    def list(
                        self,
                        *,
                        advertiserId: str,
                        lineItemId: str,
                        targetingType: typing_extensions.Literal[
                            "TARGETING_TYPE_UNSPECIFIED",
                            "TARGETING_TYPE_CHANNEL",
                            "TARGETING_TYPE_APP_CATEGORY",
                            "TARGETING_TYPE_APP",
                            "TARGETING_TYPE_URL",
                            "TARGETING_TYPE_DAY_AND_TIME",
                            "TARGETING_TYPE_AGE_RANGE",
                            "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                            "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                            "TARGETING_TYPE_GENDER",
                            "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                            "TARGETING_TYPE_USER_REWARDED_CONTENT",
                            "TARGETING_TYPE_PARENTAL_STATUS",
                            "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                            "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                            "TARGETING_TYPE_DEVICE_TYPE",
                            "TARGETING_TYPE_AUDIENCE_GROUP",
                            "TARGETING_TYPE_BROWSER",
                            "TARGETING_TYPE_HOUSEHOLD_INCOME",
                            "TARGETING_TYPE_ON_SCREEN_POSITION",
                            "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                            "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                            "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                            "TARGETING_TYPE_ENVIRONMENT",
                            "TARGETING_TYPE_CARRIER_AND_ISP",
                            "TARGETING_TYPE_OPERATING_SYSTEM",
                            "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                            "TARGETING_TYPE_KEYWORD",
                            "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                            "TARGETING_TYPE_VIEWABILITY",
                            "TARGETING_TYPE_CATEGORY",
                            "TARGETING_TYPE_INVENTORY_SOURCE",
                            "TARGETING_TYPE_LANGUAGE",
                            "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                            "TARGETING_TYPE_GEO_REGION",
                            "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                            "TARGETING_TYPE_EXCHANGE",
                            "TARGETING_TYPE_SUB_EXCHANGE",
                            "TARGETING_TYPE_POI",
                            "TARGETING_TYPE_BUSINESS_CHAIN",
                            "TARGETING_TYPE_CONTENT_DURATION",
                            "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                            "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                            "TARGETING_TYPE_OMID",
                            "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                            "TARGETING_TYPE_CONTENT_GENRE",
                            "TARGETING_TYPE_YOUTUBE_VIDEO",
                            "TARGETING_TYPE_YOUTUBE_CHANNEL",
                            "TARGETING_TYPE_SESSION_POSITION",
                            "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                        ],
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLineItemAssignedTargetingOptionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLineItemAssignedTargetingOptionsResponseHttpRequest,
                        previous_response: ListLineItemAssignedTargetingOptionsResponse,
                    ) -> (
                        ListLineItemAssignedTargetingOptionsResponseHttpRequest | None
                    ): ...

                def assignedTargetingOptions(
                    self,
                ) -> AssignedTargetingOptionsResource: ...

            def bulkEditAssignedTargetingOptions(
                self,
                *,
                advertiserId: str,
                body: BulkEditAssignedTargetingOptionsRequest = ...,
                **kwargs: typing.Any,
            ) -> BulkEditAssignedTargetingOptionsResponseHttpRequest: ...
            def bulkListAssignedTargetingOptions(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                lineItemIds: str | _list[str] = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> BulkListAssignedTargetingOptionsResponseHttpRequest: ...
            def bulkListAssignedTargetingOptions_next(
                self,
                previous_request: BulkListAssignedTargetingOptionsResponseHttpRequest,
                previous_response: BulkListAssignedTargetingOptionsResponse,
            ) -> BulkListAssignedTargetingOptionsResponseHttpRequest | None: ...
            def bulkUpdate(
                self,
                *,
                advertiserId: str,
                body: BulkUpdateLineItemsRequest = ...,
                **kwargs: typing.Any,
            ) -> BulkUpdateLineItemsResponseHttpRequest: ...
            def create(
                self, *, advertiserId: str, body: LineItem = ..., **kwargs: typing.Any
            ) -> LineItemHttpRequest: ...
            def delete(
                self, *, advertiserId: str, lineItemId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def duplicate(
                self,
                *,
                advertiserId: str,
                lineItemId: str,
                body: DuplicateLineItemRequest = ...,
                **kwargs: typing.Any,
            ) -> DuplicateLineItemResponseHttpRequest: ...
            def generateDefault(
                self,
                *,
                advertiserId: str,
                body: GenerateDefaultLineItemRequest = ...,
                **kwargs: typing.Any,
            ) -> LineItemHttpRequest: ...
            def get(
                self, *, advertiserId: str, lineItemId: str, **kwargs: typing.Any
            ) -> LineItemHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLineItemsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLineItemsResponseHttpRequest,
                previous_response: ListLineItemsResponse,
            ) -> ListLineItemsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                lineItemId: str,
                body: LineItem = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LineItemHttpRequest: ...
            def targetingTypes(self) -> TargetingTypesResource: ...

        @typing.type_check_only
        class LocationListsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AssignedLocationsResource(googleapiclient.discovery.Resource):
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    body: BulkEditAssignedLocationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> BulkEditAssignedLocationsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    body: AssignedLocation = ...,
                    **kwargs: typing.Any,
                ) -> AssignedLocationHttpRequest: ...
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    assignedLocationId: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAssignedLocationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAssignedLocationsResponseHttpRequest,
                    previous_response: ListAssignedLocationsResponse,
                ) -> ListAssignedLocationsResponseHttpRequest | None: ...

            def create(
                self,
                *,
                advertiserId: str,
                body: LocationList = ...,
                **kwargs: typing.Any,
            ) -> LocationListHttpRequest: ...
            def get(
                self, *, advertiserId: str, locationListId: str, **kwargs: typing.Any
            ) -> LocationListHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationListsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationListsResponseHttpRequest,
                previous_response: ListLocationListsResponse,
            ) -> ListLocationListsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                locationListId: str,
                body: LocationList = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LocationListHttpRequest: ...
            def assignedLocations(self) -> AssignedLocationsResource: ...

        @typing.type_check_only
        class NegativeKeywordListsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class NegativeKeywordsResource(googleapiclient.discovery.Resource):
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    body: BulkEditNegativeKeywordsRequest = ...,
                    **kwargs: typing.Any,
                ) -> BulkEditNegativeKeywordsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    body: NegativeKeyword = ...,
                    **kwargs: typing.Any,
                ) -> NegativeKeywordHttpRequest: ...
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    keywordValue: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListNegativeKeywordsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNegativeKeywordsResponseHttpRequest,
                    previous_response: ListNegativeKeywordsResponse,
                ) -> ListNegativeKeywordsResponseHttpRequest | None: ...
                def replace(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    body: ReplaceNegativeKeywordsRequest = ...,
                    **kwargs: typing.Any,
                ) -> ReplaceNegativeKeywordsResponseHttpRequest: ...

            def create(
                self,
                *,
                advertiserId: str,
                body: NegativeKeywordList = ...,
                **kwargs: typing.Any,
            ) -> NegativeKeywordListHttpRequest: ...
            def delete(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                **kwargs: typing.Any,
            ) -> NegativeKeywordListHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListNegativeKeywordListsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNegativeKeywordListsResponseHttpRequest,
                previous_response: ListNegativeKeywordListsResponse,
            ) -> ListNegativeKeywordListsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                body: NegativeKeywordList = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> NegativeKeywordListHttpRequest: ...
            def negativeKeywords(self) -> NegativeKeywordsResource: ...

        @typing.type_check_only
        class TargetingTypesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AssignedTargetingOptionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    advertiserId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    body: AssignedTargetingOption = ...,
                    **kwargs: typing.Any,
                ) -> AssignedTargetingOptionHttpRequest: ...
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    advertiserId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any,
                ) -> AssignedTargetingOptionHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListAdvertiserAssignedTargetingOptionsResponseHttpRequest,
                    previous_response: ListAdvertiserAssignedTargetingOptionsResponse,
                ) -> (
                    ListAdvertiserAssignedTargetingOptionsResponseHttpRequest | None
                ): ...

            def assignedTargetingOptions(self) -> AssignedTargetingOptionsResource: ...

        def audit(
            self, *, advertiserId: str, readMask: str = ..., **kwargs: typing.Any
        ) -> AuditAdvertiserResponseHttpRequest: ...
        def create(
            self, *, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def delete(
            self, *, advertiserId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def editAssignedTargetingOptions(
            self,
            *,
            advertiserId: str,
            body: BulkEditAdvertiserAssignedTargetingOptionsRequest = ...,
            **kwargs: typing.Any,
        ) -> BulkEditAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
        def get(
            self, *, advertiserId: str, **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListAdvertisersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAdvertisersResponseHttpRequest,
            previous_response: ListAdvertisersResponse,
        ) -> ListAdvertisersResponseHttpRequest | None: ...
        def listAssignedTargetingOptions(
            self,
            *,
            advertiserId: str,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
        def listAssignedTargetingOptions_next(
            self,
            previous_request: BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest,
            previous_response: BulkListAdvertiserAssignedTargetingOptionsResponse,
        ) -> BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            advertiserId: str,
            body: Advertiser = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> AdvertiserHttpRequest: ...
        def adGroupAds(self) -> AdGroupAdsResource: ...
        def adGroups(self) -> AdGroupsResource: ...
        def assets(self) -> AssetsResource: ...
        def campaigns(self) -> CampaignsResource: ...
        def channels(self) -> ChannelsResource: ...
        def creatives(self) -> CreativesResource: ...
        def insertionOrders(self) -> InsertionOrdersResource: ...
        def invoices(self) -> InvoicesResource: ...
        def lineItems(self) -> LineItemsResource: ...
        def locationLists(self) -> LocationListsResource: ...
        def negativeKeywordLists(self) -> NegativeKeywordListsResource: ...
        def targetingTypes(self) -> TargetingTypesResource: ...

    @typing.type_check_only
    class CombinedAudiencesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            combinedAudienceId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> CombinedAudienceHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListCombinedAudiencesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCombinedAudiencesResponseHttpRequest,
            previous_response: ListCombinedAudiencesResponse,
        ) -> ListCombinedAudiencesResponseHttpRequest | None: ...

    @typing.type_check_only
    class CustomBiddingAlgorithmsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class RulesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customBiddingAlgorithmId: str,
                body: CustomBiddingAlgorithmRules = ...,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> CustomBiddingAlgorithmRulesHttpRequest: ...
            def get(
                self,
                *,
                customBiddingAlgorithmId: str,
                customBiddingAlgorithmRulesId: str,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> CustomBiddingAlgorithmRulesHttpRequest: ...
            def list(
                self,
                *,
                customBiddingAlgorithmId: str,
                advertiserId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ListCustomBiddingAlgorithmRulesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCustomBiddingAlgorithmRulesResponseHttpRequest,
                previous_response: ListCustomBiddingAlgorithmRulesResponse,
            ) -> ListCustomBiddingAlgorithmRulesResponseHttpRequest | None: ...

        @typing.type_check_only
        class ScriptsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customBiddingAlgorithmId: str,
                body: CustomBiddingScript = ...,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> CustomBiddingScriptHttpRequest: ...
            def get(
                self,
                *,
                customBiddingAlgorithmId: str,
                customBiddingScriptId: str,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> CustomBiddingScriptHttpRequest: ...
            def list(
                self,
                *,
                customBiddingAlgorithmId: str,
                advertiserId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ListCustomBiddingScriptsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCustomBiddingScriptsResponseHttpRequest,
                previous_response: ListCustomBiddingScriptsResponse,
            ) -> ListCustomBiddingScriptsResponseHttpRequest | None: ...

        def create(
            self, *, body: CustomBiddingAlgorithm = ..., **kwargs: typing.Any
        ) -> CustomBiddingAlgorithmHttpRequest: ...
        def get(
            self,
            *,
            customBiddingAlgorithmId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> CustomBiddingAlgorithmHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListCustomBiddingAlgorithmsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCustomBiddingAlgorithmsResponseHttpRequest,
            previous_response: ListCustomBiddingAlgorithmsResponse,
        ) -> ListCustomBiddingAlgorithmsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            customBiddingAlgorithmId: str,
            body: CustomBiddingAlgorithm = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> CustomBiddingAlgorithmHttpRequest: ...
        def uploadRules(
            self,
            *,
            customBiddingAlgorithmId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> CustomBiddingAlgorithmRulesRefHttpRequest: ...
        def uploadScript(
            self,
            *,
            customBiddingAlgorithmId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> CustomBiddingScriptRefHttpRequest: ...
        def rules(self) -> RulesResource: ...
        def scripts(self) -> ScriptsResource: ...

    @typing.type_check_only
    class CustomListsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, customListId: str, advertiserId: str = ..., **kwargs: typing.Any
        ) -> CustomListHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListCustomListsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListCustomListsResponseHttpRequest,
            previous_response: ListCustomListsResponse,
        ) -> ListCustomListsResponseHttpRequest | None: ...

    @typing.type_check_only
    class FirstPartyAndPartnerAudiencesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: FirstPartyAndPartnerAudience = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any,
        ) -> FirstPartyAndPartnerAudienceHttpRequest: ...
        def editCustomerMatchMembers(
            self,
            *,
            firstPartyAndPartnerAudienceId: str,
            body: EditCustomerMatchMembersRequest = ...,
            **kwargs: typing.Any,
        ) -> EditCustomerMatchMembersResponseHttpRequest: ...
        def get(
            self,
            *,
            firstPartyAndPartnerAudienceId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> FirstPartyAndPartnerAudienceHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListFirstPartyAndPartnerAudiencesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListFirstPartyAndPartnerAudiencesResponseHttpRequest,
            previous_response: ListFirstPartyAndPartnerAudiencesResponse,
        ) -> ListFirstPartyAndPartnerAudiencesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            firstPartyAndPartnerAudienceId: str,
            body: FirstPartyAndPartnerAudience = ...,
            advertiserId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> FirstPartyAndPartnerAudienceHttpRequest: ...

    @typing.type_check_only
    class FloodlightGroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class FloodlightActivitiesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                floodlightGroupId: str,
                floodlightActivityId: str,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> FloodlightActivityHttpRequest: ...
            def list(
                self,
                *,
                floodlightGroupId: str,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ListFloodlightActivitiesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListFloodlightActivitiesResponseHttpRequest,
                previous_response: ListFloodlightActivitiesResponse,
            ) -> ListFloodlightActivitiesResponseHttpRequest | None: ...

        def get(
            self, *, floodlightGroupId: str, partnerId: str = ..., **kwargs: typing.Any
        ) -> FloodlightGroupHttpRequest: ...
        def patch(
            self,
            *,
            floodlightGroupId: str,
            body: FloodlightGroup = ...,
            partnerId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> FloodlightGroupHttpRequest: ...
        def floodlightActivities(self) -> FloodlightActivitiesResource: ...

    @typing.type_check_only
    class GoogleAudiencesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            googleAudienceId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleAudienceHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListGoogleAudiencesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListGoogleAudiencesResponseHttpRequest,
            previous_response: ListGoogleAudiencesResponse,
        ) -> ListGoogleAudiencesResponseHttpRequest | None: ...

    @typing.type_check_only
    class GuaranteedOrdersResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: GuaranteedOrder = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> GuaranteedOrderHttpRequest: ...
        def editGuaranteedOrderReadAccessors(
            self,
            *,
            guaranteedOrderId: str,
            body: EditGuaranteedOrderReadAccessorsRequest = ...,
            **kwargs: typing.Any,
        ) -> EditGuaranteedOrderReadAccessorsResponseHttpRequest: ...
        def get(
            self,
            *,
            guaranteedOrderId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> GuaranteedOrderHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListGuaranteedOrdersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListGuaranteedOrdersResponseHttpRequest,
            previous_response: ListGuaranteedOrdersResponse,
        ) -> ListGuaranteedOrdersResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            guaranteedOrderId: str,
            body: GuaranteedOrder = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GuaranteedOrderHttpRequest: ...

    @typing.type_check_only
    class InventorySourceGroupsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AssignedInventorySourcesResource(googleapiclient.discovery.Resource):
            def bulkEdit(
                self,
                *,
                inventorySourceGroupId: str,
                body: BulkEditAssignedInventorySourcesRequest = ...,
                **kwargs: typing.Any,
            ) -> BulkEditAssignedInventorySourcesResponseHttpRequest: ...
            def create(
                self,
                *,
                inventorySourceGroupId: str,
                body: AssignedInventorySource = ...,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> AssignedInventorySourceHttpRequest: ...
            def delete(
                self,
                *,
                inventorySourceGroupId: str,
                assignedInventorySourceId: str,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                inventorySourceGroupId: str,
                advertiserId: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any,
            ) -> ListAssignedInventorySourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAssignedInventorySourcesResponseHttpRequest,
                previous_response: ListAssignedInventorySourcesResponse,
            ) -> ListAssignedInventorySourcesResponseHttpRequest | None: ...

        def create(
            self,
            *,
            body: InventorySourceGroup = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceGroupHttpRequest: ...
        def delete(
            self,
            *,
            inventorySourceGroupId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            inventorySourceGroupId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceGroupHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListInventorySourceGroupsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListInventorySourceGroupsResponseHttpRequest,
            previous_response: ListInventorySourceGroupsResponse,
        ) -> ListInventorySourceGroupsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            inventorySourceGroupId: str,
            body: InventorySourceGroup = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceGroupHttpRequest: ...
        def assignedInventorySources(self) -> AssignedInventorySourcesResource: ...

    @typing.type_check_only
    class InventorySourcesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: InventorySource = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceHttpRequest: ...
        def editInventorySourceReadWriteAccessors(
            self,
            *,
            inventorySourceId: str,
            body: EditInventorySourceReadWriteAccessorsRequest = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceAccessorsHttpRequest: ...
        def get(
            self,
            *,
            inventorySourceId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceHttpRequest: ...
        def list(
            self,
            *,
            advertiserId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any,
        ) -> ListInventorySourcesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListInventorySourcesResponseHttpRequest,
            previous_response: ListInventorySourcesResponse,
        ) -> ListInventorySourcesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            inventorySourceId: str,
            body: InventorySource = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> InventorySourceHttpRequest: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GoogleBytestreamMediaHttpRequest: ...
        def download_media(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def upload(
            self,
            *,
            resourceName: str,
            body: GoogleBytestreamMedia = ...,
            **kwargs: typing.Any,
        ) -> GoogleBytestreamMediaHttpRequest: ...

    @typing.type_check_only
    class PartnersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChannelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SitesResource(googleapiclient.discovery.Resource):
                def bulkEdit(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    body: BulkEditSitesRequest = ...,
                    **kwargs: typing.Any,
                ) -> BulkEditSitesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    body: Site = ...,
                    advertiserId: str = ...,
                    **kwargs: typing.Any,
                ) -> SiteHttpRequest: ...
                def delete(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    urlOrAppId: str,
                    advertiserId: str = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    advertiserId: str = ...,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListSitesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListSitesResponseHttpRequest,
                    previous_response: ListSitesResponse,
                ) -> ListSitesResponseHttpRequest | None: ...
                def replace(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    body: ReplaceSitesRequest = ...,
                    **kwargs: typing.Any,
                ) -> ReplaceSitesResponseHttpRequest: ...

            def create(
                self,
                *,
                partnerId: str,
                body: Channel = ...,
                advertiserId: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def get(
                self,
                *,
                partnerId: str,
                channelId: str,
                advertiserId: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                partnerId: str,
                advertiserId: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListChannelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListChannelsResponseHttpRequest,
                previous_response: ListChannelsResponse,
            ) -> ListChannelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                partnerId: str,
                channelId: str,
                body: Channel = ...,
                advertiserId: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> ChannelHttpRequest: ...
            def sites(self) -> SitesResource: ...

        @typing.type_check_only
        class TargetingTypesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AssignedTargetingOptionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    partnerId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    body: AssignedTargetingOption = ...,
                    **kwargs: typing.Any,
                ) -> AssignedTargetingOptionHttpRequest: ...
                def delete(
                    self,
                    *,
                    partnerId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    partnerId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any,
                ) -> AssignedTargetingOptionHttpRequest: ...
                def list(
                    self,
                    *,
                    partnerId: str,
                    targetingType: typing_extensions.Literal[
                        "TARGETING_TYPE_UNSPECIFIED",
                        "TARGETING_TYPE_CHANNEL",
                        "TARGETING_TYPE_APP_CATEGORY",
                        "TARGETING_TYPE_APP",
                        "TARGETING_TYPE_URL",
                        "TARGETING_TYPE_DAY_AND_TIME",
                        "TARGETING_TYPE_AGE_RANGE",
                        "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                        "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                        "TARGETING_TYPE_GENDER",
                        "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                        "TARGETING_TYPE_USER_REWARDED_CONTENT",
                        "TARGETING_TYPE_PARENTAL_STATUS",
                        "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                        "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                        "TARGETING_TYPE_DEVICE_TYPE",
                        "TARGETING_TYPE_AUDIENCE_GROUP",
                        "TARGETING_TYPE_BROWSER",
                        "TARGETING_TYPE_HOUSEHOLD_INCOME",
                        "TARGETING_TYPE_ON_SCREEN_POSITION",
                        "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                        "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                        "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                        "TARGETING_TYPE_ENVIRONMENT",
                        "TARGETING_TYPE_CARRIER_AND_ISP",
                        "TARGETING_TYPE_OPERATING_SYSTEM",
                        "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                        "TARGETING_TYPE_KEYWORD",
                        "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                        "TARGETING_TYPE_VIEWABILITY",
                        "TARGETING_TYPE_CATEGORY",
                        "TARGETING_TYPE_INVENTORY_SOURCE",
                        "TARGETING_TYPE_LANGUAGE",
                        "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                        "TARGETING_TYPE_GEO_REGION",
                        "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                        "TARGETING_TYPE_EXCHANGE",
                        "TARGETING_TYPE_SUB_EXCHANGE",
                        "TARGETING_TYPE_POI",
                        "TARGETING_TYPE_BUSINESS_CHAIN",
                        "TARGETING_TYPE_CONTENT_DURATION",
                        "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                        "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                        "TARGETING_TYPE_OMID",
                        "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                        "TARGETING_TYPE_CONTENT_GENRE",
                        "TARGETING_TYPE_YOUTUBE_VIDEO",
                        "TARGETING_TYPE_YOUTUBE_CHANNEL",
                        "TARGETING_TYPE_SESSION_POSITION",
                        "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                    ],
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPartnerAssignedTargetingOptionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPartnerAssignedTargetingOptionsResponseHttpRequest,
                    previous_response: ListPartnerAssignedTargetingOptionsResponse,
                ) -> ListPartnerAssignedTargetingOptionsResponseHttpRequest | None: ...

            def assignedTargetingOptions(self) -> AssignedTargetingOptionsResource: ...

        def editAssignedTargetingOptions(
            self,
            *,
            partnerId: str,
            body: BulkEditPartnerAssignedTargetingOptionsRequest = ...,
            **kwargs: typing.Any,
        ) -> BulkEditPartnerAssignedTargetingOptionsResponseHttpRequest: ...
        def get(
            self, *, partnerId: str, **kwargs: typing.Any
        ) -> PartnerHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListPartnersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPartnersResponseHttpRequest,
            previous_response: ListPartnersResponse,
        ) -> ListPartnersResponseHttpRequest | None: ...
        def channels(self) -> ChannelsResource: ...
        def targetingTypes(self) -> TargetingTypesResource: ...

    @typing.type_check_only
    class SdfdownloadtasksResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def create(
            self, *, body: CreateSdfDownloadTaskRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class SdfuploadtasksResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class TargetingTypesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TargetingOptionsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                targetingType: typing_extensions.Literal[
                    "TARGETING_TYPE_UNSPECIFIED",
                    "TARGETING_TYPE_CHANNEL",
                    "TARGETING_TYPE_APP_CATEGORY",
                    "TARGETING_TYPE_APP",
                    "TARGETING_TYPE_URL",
                    "TARGETING_TYPE_DAY_AND_TIME",
                    "TARGETING_TYPE_AGE_RANGE",
                    "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                    "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                    "TARGETING_TYPE_GENDER",
                    "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                    "TARGETING_TYPE_USER_REWARDED_CONTENT",
                    "TARGETING_TYPE_PARENTAL_STATUS",
                    "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                    "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                    "TARGETING_TYPE_DEVICE_TYPE",
                    "TARGETING_TYPE_AUDIENCE_GROUP",
                    "TARGETING_TYPE_BROWSER",
                    "TARGETING_TYPE_HOUSEHOLD_INCOME",
                    "TARGETING_TYPE_ON_SCREEN_POSITION",
                    "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                    "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                    "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                    "TARGETING_TYPE_ENVIRONMENT",
                    "TARGETING_TYPE_CARRIER_AND_ISP",
                    "TARGETING_TYPE_OPERATING_SYSTEM",
                    "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                    "TARGETING_TYPE_KEYWORD",
                    "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                    "TARGETING_TYPE_VIEWABILITY",
                    "TARGETING_TYPE_CATEGORY",
                    "TARGETING_TYPE_INVENTORY_SOURCE",
                    "TARGETING_TYPE_LANGUAGE",
                    "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                    "TARGETING_TYPE_GEO_REGION",
                    "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                    "TARGETING_TYPE_EXCHANGE",
                    "TARGETING_TYPE_SUB_EXCHANGE",
                    "TARGETING_TYPE_POI",
                    "TARGETING_TYPE_BUSINESS_CHAIN",
                    "TARGETING_TYPE_CONTENT_DURATION",
                    "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                    "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                    "TARGETING_TYPE_OMID",
                    "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                    "TARGETING_TYPE_CONTENT_GENRE",
                    "TARGETING_TYPE_YOUTUBE_VIDEO",
                    "TARGETING_TYPE_YOUTUBE_CHANNEL",
                    "TARGETING_TYPE_SESSION_POSITION",
                    "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                ],
                targetingOptionId: str,
                advertiserId: str = ...,
                **kwargs: typing.Any,
            ) -> TargetingOptionHttpRequest: ...
            def list(
                self,
                *,
                targetingType: typing_extensions.Literal[
                    "TARGETING_TYPE_UNSPECIFIED",
                    "TARGETING_TYPE_CHANNEL",
                    "TARGETING_TYPE_APP_CATEGORY",
                    "TARGETING_TYPE_APP",
                    "TARGETING_TYPE_URL",
                    "TARGETING_TYPE_DAY_AND_TIME",
                    "TARGETING_TYPE_AGE_RANGE",
                    "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                    "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                    "TARGETING_TYPE_GENDER",
                    "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                    "TARGETING_TYPE_USER_REWARDED_CONTENT",
                    "TARGETING_TYPE_PARENTAL_STATUS",
                    "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                    "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                    "TARGETING_TYPE_DEVICE_TYPE",
                    "TARGETING_TYPE_AUDIENCE_GROUP",
                    "TARGETING_TYPE_BROWSER",
                    "TARGETING_TYPE_HOUSEHOLD_INCOME",
                    "TARGETING_TYPE_ON_SCREEN_POSITION",
                    "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                    "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                    "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                    "TARGETING_TYPE_ENVIRONMENT",
                    "TARGETING_TYPE_CARRIER_AND_ISP",
                    "TARGETING_TYPE_OPERATING_SYSTEM",
                    "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                    "TARGETING_TYPE_KEYWORD",
                    "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                    "TARGETING_TYPE_VIEWABILITY",
                    "TARGETING_TYPE_CATEGORY",
                    "TARGETING_TYPE_INVENTORY_SOURCE",
                    "TARGETING_TYPE_LANGUAGE",
                    "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                    "TARGETING_TYPE_GEO_REGION",
                    "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                    "TARGETING_TYPE_EXCHANGE",
                    "TARGETING_TYPE_SUB_EXCHANGE",
                    "TARGETING_TYPE_POI",
                    "TARGETING_TYPE_BUSINESS_CHAIN",
                    "TARGETING_TYPE_CONTENT_DURATION",
                    "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                    "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                    "TARGETING_TYPE_OMID",
                    "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                    "TARGETING_TYPE_CONTENT_GENRE",
                    "TARGETING_TYPE_YOUTUBE_VIDEO",
                    "TARGETING_TYPE_YOUTUBE_CHANNEL",
                    "TARGETING_TYPE_SESSION_POSITION",
                    "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                ],
                advertiserId: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListTargetingOptionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTargetingOptionsResponseHttpRequest,
                previous_response: ListTargetingOptionsResponse,
            ) -> ListTargetingOptionsResponseHttpRequest | None: ...
            def search(
                self,
                *,
                targetingType: typing_extensions.Literal[
                    "TARGETING_TYPE_UNSPECIFIED",
                    "TARGETING_TYPE_CHANNEL",
                    "TARGETING_TYPE_APP_CATEGORY",
                    "TARGETING_TYPE_APP",
                    "TARGETING_TYPE_URL",
                    "TARGETING_TYPE_DAY_AND_TIME",
                    "TARGETING_TYPE_AGE_RANGE",
                    "TARGETING_TYPE_REGIONAL_LOCATION_LIST",
                    "TARGETING_TYPE_PROXIMITY_LOCATION_LIST",
                    "TARGETING_TYPE_GENDER",
                    "TARGETING_TYPE_VIDEO_PLAYER_SIZE",
                    "TARGETING_TYPE_USER_REWARDED_CONTENT",
                    "TARGETING_TYPE_PARENTAL_STATUS",
                    "TARGETING_TYPE_CONTENT_INSTREAM_POSITION",
                    "TARGETING_TYPE_CONTENT_OUTSTREAM_POSITION",
                    "TARGETING_TYPE_DEVICE_TYPE",
                    "TARGETING_TYPE_AUDIENCE_GROUP",
                    "TARGETING_TYPE_BROWSER",
                    "TARGETING_TYPE_HOUSEHOLD_INCOME",
                    "TARGETING_TYPE_ON_SCREEN_POSITION",
                    "TARGETING_TYPE_THIRD_PARTY_VERIFIER",
                    "TARGETING_TYPE_DIGITAL_CONTENT_LABEL_EXCLUSION",
                    "TARGETING_TYPE_SENSITIVE_CATEGORY_EXCLUSION",
                    "TARGETING_TYPE_ENVIRONMENT",
                    "TARGETING_TYPE_CARRIER_AND_ISP",
                    "TARGETING_TYPE_OPERATING_SYSTEM",
                    "TARGETING_TYPE_DEVICE_MAKE_MODEL",
                    "TARGETING_TYPE_KEYWORD",
                    "TARGETING_TYPE_NEGATIVE_KEYWORD_LIST",
                    "TARGETING_TYPE_VIEWABILITY",
                    "TARGETING_TYPE_CATEGORY",
                    "TARGETING_TYPE_INVENTORY_SOURCE",
                    "TARGETING_TYPE_LANGUAGE",
                    "TARGETING_TYPE_AUTHORIZED_SELLER_STATUS",
                    "TARGETING_TYPE_GEO_REGION",
                    "TARGETING_TYPE_INVENTORY_SOURCE_GROUP",
                    "TARGETING_TYPE_EXCHANGE",
                    "TARGETING_TYPE_SUB_EXCHANGE",
                    "TARGETING_TYPE_POI",
                    "TARGETING_TYPE_BUSINESS_CHAIN",
                    "TARGETING_TYPE_CONTENT_DURATION",
                    "TARGETING_TYPE_CONTENT_STREAM_TYPE",
                    "TARGETING_TYPE_NATIVE_CONTENT_POSITION",
                    "TARGETING_TYPE_OMID",
                    "TARGETING_TYPE_AUDIO_CONTENT_TYPE",
                    "TARGETING_TYPE_CONTENT_GENRE",
                    "TARGETING_TYPE_YOUTUBE_VIDEO",
                    "TARGETING_TYPE_YOUTUBE_CHANNEL",
                    "TARGETING_TYPE_SESSION_POSITION",
                    "TARGETING_TYPE_CONTENT_THEME_EXCLUSION",
                ],
                body: SearchTargetingOptionsRequest = ...,
                **kwargs: typing.Any,
            ) -> SearchTargetingOptionsResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: SearchTargetingOptionsResponseHttpRequest,
                previous_response: SearchTargetingOptionsResponse,
            ) -> SearchTargetingOptionsResponseHttpRequest | None: ...

        def targetingOptions(self) -> TargetingOptionsResource: ...

    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        def bulkEditAssignedUserRoles(
            self,
            *,
            userId: str,
            body: BulkEditAssignedUserRolesRequest = ...,
            **kwargs: typing.Any,
        ) -> BulkEditAssignedUserRolesResponseHttpRequest: ...
        def create(
            self, *, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def delete(self, *, userId: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, userId: str, **kwargs: typing.Any) -> UserHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            orderBy: str = ...,
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
            userId: str,
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
    def advertisers(self) -> AdvertisersResource: ...
    def combinedAudiences(self) -> CombinedAudiencesResource: ...
    def customBiddingAlgorithms(self) -> CustomBiddingAlgorithmsResource: ...
    def customLists(self) -> CustomListsResource: ...
    def firstPartyAndPartnerAudiences(
        self,
    ) -> FirstPartyAndPartnerAudiencesResource: ...
    def floodlightGroups(self) -> FloodlightGroupsResource: ...
    def googleAudiences(self) -> GoogleAudiencesResource: ...
    def guaranteedOrders(self) -> GuaranteedOrdersResource: ...
    def inventorySourceGroups(self) -> InventorySourceGroupsResource: ...
    def inventorySources(self) -> InventorySourcesResource: ...
    def media(self) -> MediaResource: ...
    def partners(self) -> PartnersResource: ...
    def sdfdownloadtasks(self) -> SdfdownloadtasksResource: ...
    def sdfuploadtasks(self) -> SdfuploadtasksResource: ...
    def targetingTypes(self) -> TargetingTypesResource: ...
    def users(self) -> UsersResource: ...

@typing.type_check_only
class AdGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdGroup: ...

@typing.type_check_only
class AdGroupAdHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AdGroupAd: ...

@typing.type_check_only
class AdvertiserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Advertiser: ...

@typing.type_check_only
class AssignedInventorySourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AssignedInventorySource: ...

@typing.type_check_only
class AssignedLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AssignedLocation: ...

@typing.type_check_only
class AssignedTargetingOptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AssignedTargetingOption: ...

@typing.type_check_only
class AuditAdvertiserResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AuditAdvertiserResponse: ...

@typing.type_check_only
class BulkEditAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditAdvertiserAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkEditAssignedInventorySourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditAssignedInventorySourcesResponse: ...

@typing.type_check_only
class BulkEditAssignedLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditAssignedLocationsResponse: ...

@typing.type_check_only
class BulkEditAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkEditAssignedUserRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditAssignedUserRolesResponse: ...

@typing.type_check_only
class BulkEditNegativeKeywordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditNegativeKeywordsResponse: ...

@typing.type_check_only
class BulkEditPartnerAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditPartnerAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkEditSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkEditSitesResponse: ...

@typing.type_check_only
class BulkListAdGroupAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkListAdGroupAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkListAdvertiserAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkListAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkListAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class BulkUpdateLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BulkUpdateLineItemsResponse: ...

@typing.type_check_only
class CampaignHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Campaign: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class CombinedAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CombinedAudience: ...

@typing.type_check_only
class CreateAssetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CreateAssetResponse: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Creative: ...

@typing.type_check_only
class CustomBiddingAlgorithmHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomBiddingAlgorithm: ...

@typing.type_check_only
class CustomBiddingAlgorithmRulesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomBiddingAlgorithmRules: ...

@typing.type_check_only
class CustomBiddingAlgorithmRulesRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomBiddingAlgorithmRulesRef: ...

@typing.type_check_only
class CustomBiddingScriptHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomBiddingScript: ...

@typing.type_check_only
class CustomBiddingScriptRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomBiddingScriptRef: ...

@typing.type_check_only
class CustomListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomList: ...

@typing.type_check_only
class DuplicateLineItemResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DuplicateLineItemResponse: ...

@typing.type_check_only
class EditCustomerMatchMembersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EditCustomerMatchMembersResponse: ...

@typing.type_check_only
class EditGuaranteedOrderReadAccessorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EditGuaranteedOrderReadAccessorsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FirstPartyAndPartnerAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FirstPartyAndPartnerAudience: ...

@typing.type_check_only
class FloodlightActivityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FloodlightActivity: ...

@typing.type_check_only
class FloodlightGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FloodlightGroup: ...

@typing.type_check_only
class GoogleAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAudience: ...

@typing.type_check_only
class GoogleBytestreamMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleBytestreamMedia: ...

@typing.type_check_only
class GuaranteedOrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GuaranteedOrder: ...

@typing.type_check_only
class InsertionOrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InsertionOrder: ...

@typing.type_check_only
class InventorySourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InventorySource: ...

@typing.type_check_only
class InventorySourceAccessorsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InventorySourceAccessors: ...

@typing.type_check_only
class InventorySourceGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> InventorySourceGroup: ...

@typing.type_check_only
class LineItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LineItem: ...

@typing.type_check_only
class ListAdGroupAdsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdGroupAdsResponse: ...

@typing.type_check_only
class ListAdGroupAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdGroupAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class ListAdGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdGroupsResponse: ...

@typing.type_check_only
class ListAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdvertiserAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class ListAdvertisersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAdvertisersResponse: ...

@typing.type_check_only
class ListAssignedInventorySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAssignedInventorySourcesResponse: ...

@typing.type_check_only
class ListAssignedLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAssignedLocationsResponse: ...

@typing.type_check_only
class ListCampaignsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCampaignsResponse: ...

@typing.type_check_only
class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListChannelsResponse: ...

@typing.type_check_only
class ListCombinedAudiencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCombinedAudiencesResponse: ...

@typing.type_check_only
class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCreativesResponse: ...

@typing.type_check_only
class ListCustomBiddingAlgorithmRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomBiddingAlgorithmRulesResponse: ...

@typing.type_check_only
class ListCustomBiddingAlgorithmsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomBiddingAlgorithmsResponse: ...

@typing.type_check_only
class ListCustomBiddingScriptsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomBiddingScriptsResponse: ...

@typing.type_check_only
class ListCustomListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomListsResponse: ...

@typing.type_check_only
class ListFirstPartyAndPartnerAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFirstPartyAndPartnerAudiencesResponse: ...

@typing.type_check_only
class ListFloodlightActivitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFloodlightActivitiesResponse: ...

@typing.type_check_only
class ListGoogleAudiencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGoogleAudiencesResponse: ...

@typing.type_check_only
class ListGuaranteedOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGuaranteedOrdersResponse: ...

@typing.type_check_only
class ListInsertionOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInsertionOrdersResponse: ...

@typing.type_check_only
class ListInventorySourceGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInventorySourceGroupsResponse: ...

@typing.type_check_only
class ListInventorySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInventorySourcesResponse: ...

@typing.type_check_only
class ListInvoicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListInvoicesResponse: ...

@typing.type_check_only
class ListLineItemAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLineItemAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class ListLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLineItemsResponse: ...

@typing.type_check_only
class ListLocationListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationListsResponse: ...

@typing.type_check_only
class ListNegativeKeywordListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNegativeKeywordListsResponse: ...

@typing.type_check_only
class ListNegativeKeywordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNegativeKeywordsResponse: ...

@typing.type_check_only
class ListPartnerAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPartnerAssignedTargetingOptionsResponse: ...

@typing.type_check_only
class ListPartnersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPartnersResponse: ...

@typing.type_check_only
class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSitesResponse: ...

@typing.type_check_only
class ListTargetingOptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTargetingOptionsResponse: ...

@typing.type_check_only
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUsersResponse: ...

@typing.type_check_only
class LocationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LocationList: ...

@typing.type_check_only
class LookupInvoiceCurrencyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LookupInvoiceCurrencyResponse: ...

@typing.type_check_only
class NegativeKeywordHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NegativeKeyword: ...

@typing.type_check_only
class NegativeKeywordListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NegativeKeywordList: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PartnerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Partner: ...

@typing.type_check_only
class ReplaceNegativeKeywordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReplaceNegativeKeywordsResponse: ...

@typing.type_check_only
class ReplaceSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReplaceSitesResponse: ...

@typing.type_check_only
class SearchTargetingOptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchTargetingOptionsResponse: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Site: ...

@typing.type_check_only
class TargetingOptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TargetingOption: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
