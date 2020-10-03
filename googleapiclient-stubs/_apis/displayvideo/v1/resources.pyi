import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DisplayVideoResource(googleapiclient.discovery.Resource):
    class SdfdownloadtasksResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def create(
            self, *, body: CreateSdfDownloadTaskRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...
    class AdvertisersResource(googleapiclient.discovery.Resource):
        class ChannelsResource(googleapiclient.discovery.Resource):
            class SitesResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    urlOrAppId: str,
                    partnerId: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    body: BulkEditSitesRequest = ...,
                    **kwargs: typing.Any
                ) -> BulkEditSitesResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    partnerId: str = ...,
                    orderBy: str = ...,
                    **kwargs: typing.Any
                ) -> ListSitesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    advertiserId: str,
                    channelId: str,
                    body: Site = ...,
                    partnerId: str = ...,
                    **kwargs: typing.Any
                ) -> SiteHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                channelId: str,
                body: Channel = ...,
                updateMask: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def create(
                self,
                *,
                advertiserId: str,
                body: Channel = ...,
                partnerId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def get(
                self,
                *,
                advertiserId: str,
                channelId: str,
                partnerId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                orderBy: str = ...,
                partnerId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListChannelsResponseHttpRequest: ...
            def sites(self) -> SitesResource: ...
        class NegativeKeywordListsResource(googleapiclient.discovery.Resource):
            class NegativeKeywordsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    body: NegativeKeyword = ...,
                    **kwargs: typing.Any
                ) -> NegativeKeywordHttpRequest: ...
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    body: BulkEditNegativeKeywordsRequest = ...,
                    **kwargs: typing.Any
                ) -> BulkEditNegativeKeywordsResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    keywordValue: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    negativeKeywordListId: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    orderBy: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListNegativeKeywordsResponseHttpRequest: ...
            def get(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                **kwargs: typing.Any
            ) -> NegativeKeywordListHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                body: NegativeKeywordList = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NegativeKeywordListHttpRequest: ...
            def delete(
                self,
                *,
                advertiserId: str,
                negativeKeywordListId: str,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                advertiserId: str,
                body: NegativeKeywordList = ...,
                **kwargs: typing.Any
            ) -> NegativeKeywordListHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListNegativeKeywordListsResponseHttpRequest: ...
            def negativeKeywords(self) -> NegativeKeywordsResource: ...
        class LineItemsResource(googleapiclient.discovery.Resource):
            class TargetingTypesResource(googleapiclient.discovery.Resource):
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
                        ],
                        body: AssignedTargetingOption = ...,
                        **kwargs: typing.Any
                    ) -> AssignedTargetingOptionHttpRequest: ...
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
                        ],
                        assignedTargetingOptionId: str,
                        **kwargs: typing.Any
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
                        ],
                        orderBy: str = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ListLineItemAssignedTargetingOptionsResponseHttpRequest: ...
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
                        ],
                        assignedTargetingOptionId: str,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                def assignedTargetingOptions(
                    self,
                ) -> AssignedTargetingOptionsResource: ...
            def delete(
                self, *, advertiserId: str, lineItemId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def bulkEditLineItemAssignedTargetingOptions(
                self,
                *,
                advertiserId: str,
                lineItemId: str,
                body: BulkEditLineItemAssignedTargetingOptionsRequest = ...,
                **kwargs: typing.Any
            ) -> BulkEditLineItemAssignedTargetingOptionsResponseHttpRequest: ...
            def create(
                self, *, advertiserId: str, body: LineItem = ..., **kwargs: typing.Any
            ) -> LineItemHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                orderBy: str = ...,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListLineItemsResponseHttpRequest: ...
            def get(
                self, *, advertiserId: str, lineItemId: str, **kwargs: typing.Any
            ) -> LineItemHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                lineItemId: str,
                body: LineItem = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LineItemHttpRequest: ...
            def bulkListLineItemAssignedTargetingOptions(
                self,
                *,
                advertiserId: str,
                lineItemId: str,
                filter: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> BulkListLineItemAssignedTargetingOptionsResponseHttpRequest: ...
            def targetingTypes(self) -> TargetingTypesResource: ...
        class AssetsResource(googleapiclient.discovery.Resource):
            def upload(
                self,
                *,
                advertiserId: str,
                body: CreateAssetRequest = ...,
                **kwargs: typing.Any
            ) -> CreateAssetResponseHttpRequest: ...
        class CreativesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, advertiserId: str, creativeId: str, **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def delete(
                self, *, advertiserId: str, creativeId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                creativeId: str,
                body: Creative = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                pageToken: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def create(
                self, *, advertiserId: str, body: Creative = ..., **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
        class CampaignsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                advertiserId: str,
                pageSize: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListCampaignsResponseHttpRequest: ...
            def delete(
                self, *, advertiserId: str, campaignId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, advertiserId: str, body: Campaign = ..., **kwargs: typing.Any
            ) -> CampaignHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                campaignId: str,
                body: Campaign = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CampaignHttpRequest: ...
            def get(
                self, *, advertiserId: str, campaignId: str, **kwargs: typing.Any
            ) -> CampaignHttpRequest: ...
        class InsertionOrdersResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                advertiserId: str,
                insertionOrderId: str,
                body: InsertionOrder = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> InsertionOrderHttpRequest: ...
            def delete(
                self, *, advertiserId: str, insertionOrderId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, advertiserId: str, insertionOrderId: str, **kwargs: typing.Any
            ) -> InsertionOrderHttpRequest: ...
            def create(
                self,
                *,
                advertiserId: str,
                body: InsertionOrder = ...,
                **kwargs: typing.Any
            ) -> InsertionOrderHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                orderBy: str = ...,
                filter: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListInsertionOrdersResponseHttpRequest: ...
        class TargetingTypesResource(googleapiclient.discovery.Resource):
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
                    ],
                    body: AssignedTargetingOption = ...,
                    **kwargs: typing.Any
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
                    ],
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
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
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any
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
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def assignedTargetingOptions(self) -> AssignedTargetingOptionsResource: ...
        class LocationListsResource(googleapiclient.discovery.Resource):
            class AssignedLocationsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    assignedLocationId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListAssignedLocationsResponseHttpRequest: ...
                def bulkEdit(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    body: BulkEditAssignedLocationsRequest = ...,
                    **kwargs: typing.Any
                ) -> BulkEditAssignedLocationsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    advertiserId: str,
                    locationListId: str,
                    body: AssignedLocation = ...,
                    **kwargs: typing.Any
                ) -> AssignedLocationHttpRequest: ...
            def get(
                self, *, advertiserId: str, locationListId: str, **kwargs: typing.Any
            ) -> LocationListHttpRequest: ...
            def create(
                self,
                *,
                advertiserId: str,
                body: LocationList = ...,
                **kwargs: typing.Any
            ) -> LocationListHttpRequest: ...
            def list(
                self,
                *,
                advertiserId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationListsResponseHttpRequest: ...
            def patch(
                self,
                *,
                advertiserId: str,
                locationListId: str,
                body: LocationList = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LocationListHttpRequest: ...
            def assignedLocations(self) -> AssignedLocationsResource: ...
        def audit(
            self, *, advertiserId: str, readMask: str = ..., **kwargs: typing.Any
        ) -> AuditAdvertiserResponseHttpRequest: ...
        def create(
            self, *, body: Advertiser = ..., **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def get(
            self, *, advertiserId: str, **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def bulkEditAdvertiserAssignedTargetingOptions(
            self,
            *,
            advertiserId: str,
            body: BulkEditAdvertiserAssignedTargetingOptionsRequest = ...,
            **kwargs: typing.Any
        ) -> BulkEditAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
        def patch(
            self,
            *,
            advertiserId: str,
            body: Advertiser = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> AdvertiserHttpRequest: ...
        def delete(
            self, *, advertiserId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def bulkListAdvertiserAssignedTargetingOptions(
            self,
            *,
            advertiserId: str,
            orderBy: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            filter: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any
        ) -> ListAdvertisersResponseHttpRequest: ...
        def channels(self) -> ChannelsResource: ...
        def negativeKeywordLists(self) -> NegativeKeywordListsResource: ...
        def lineItems(self) -> LineItemsResource: ...
        def assets(self) -> AssetsResource: ...
        def creatives(self) -> CreativesResource: ...
        def campaigns(self) -> CampaignsResource: ...
        def insertionOrders(self) -> InsertionOrdersResource: ...
        def targetingTypes(self) -> TargetingTypesResource: ...
        def locationLists(self) -> LocationListsResource: ...
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GoogleBytestreamMediaHttpRequest: ...
    class TargetingTypesResource(googleapiclient.discovery.Resource):
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
                ],
                targetingOptionId: str,
                advertiserId: str = ...,
                **kwargs: typing.Any
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
                ],
                filter: str = ...,
                advertiserId: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTargetingOptionsResponseHttpRequest: ...
        def targetingOptions(self) -> TargetingOptionsResource: ...
    class PartnersResource(googleapiclient.discovery.Resource):
        class ChannelsResource(googleapiclient.discovery.Resource):
            class SitesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    body: Site = ...,
                    advertiserId: str = ...,
                    **kwargs: typing.Any
                ) -> SiteHttpRequest: ...
                def delete(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    urlOrAppId: str,
                    advertiserId: str = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    advertiserId: str = ...,
                    orderBy: str = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListSitesResponseHttpRequest: ...
                def bulkEdit(
                    self,
                    *,
                    partnerId: str,
                    channelId: str,
                    body: BulkEditSitesRequest = ...,
                    **kwargs: typing.Any
                ) -> BulkEditSitesResponseHttpRequest: ...
            def create(
                self,
                *,
                partnerId: str,
                body: Channel = ...,
                advertiserId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                partnerId: str,
                pageToken: str = ...,
                orderBy: str = ...,
                filter: str = ...,
                advertiserId: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListChannelsResponseHttpRequest: ...
            def get(
                self,
                *,
                partnerId: str,
                channelId: str,
                advertiserId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def patch(
                self,
                *,
                partnerId: str,
                channelId: str,
                body: Channel = ...,
                updateMask: str = ...,
                advertiserId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def sites(self) -> SitesResource: ...
        class TargetingTypesResource(googleapiclient.discovery.Resource):
            class AssignedTargetingOptionsResource(googleapiclient.discovery.Resource):
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
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
                    ],
                    orderBy: str = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListPartnerAssignedTargetingOptionsResponseHttpRequest: ...
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
                    ],
                    assignedTargetingOptionId: str,
                    **kwargs: typing.Any
                ) -> AssignedTargetingOptionHttpRequest: ...
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
                    ],
                    body: AssignedTargetingOption = ...,
                    **kwargs: typing.Any
                ) -> AssignedTargetingOptionHttpRequest: ...
            def assignedTargetingOptions(self) -> AssignedTargetingOptionsResource: ...
        def bulkEditPartnerAssignedTargetingOptions(
            self,
            *,
            partnerId: str,
            body: BulkEditPartnerAssignedTargetingOptionsRequest = ...,
            **kwargs: typing.Any
        ) -> BulkEditPartnerAssignedTargetingOptionsResponseHttpRequest: ...
        def get(
            self, *, partnerId: str, **kwargs: typing.Any
        ) -> PartnerHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            orderBy: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListPartnersResponseHttpRequest: ...
        def channels(self) -> ChannelsResource: ...
        def targetingTypes(self) -> TargetingTypesResource: ...
    class GoogleAudiencesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            googleAudienceId: str,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAudienceHttpRequest: ...
        def list(
            self,
            *,
            orderBy: str = ...,
            partnerId: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> ListGoogleAudiencesResponseHttpRequest: ...
    class InventorySourceGroupsResource(googleapiclient.discovery.Resource):
        class AssignedInventorySourcesResource(googleapiclient.discovery.Resource):
            def bulkEdit(
                self,
                *,
                inventorySourceGroupId: str,
                body: BulkEditAssignedInventorySourcesRequest = ...,
                **kwargs: typing.Any
            ) -> BulkEditAssignedInventorySourcesResponseHttpRequest: ...
            def delete(
                self,
                *,
                inventorySourceGroupId: str,
                assignedInventorySourceId: str,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                inventorySourceGroupId: str,
                body: AssignedInventorySource = ...,
                advertiserId: str = ...,
                partnerId: str = ...,
                **kwargs: typing.Any
            ) -> AssignedInventorySourceHttpRequest: ...
            def list(
                self,
                *,
                inventorySourceGroupId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                partnerId: str = ...,
                filter: str = ...,
                orderBy: str = ...,
                advertiserId: str = ...,
                **kwargs: typing.Any
            ) -> ListAssignedInventorySourcesResponseHttpRequest: ...
        def get(
            self,
            *,
            inventorySourceGroupId: str,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> InventorySourceGroupHttpRequest: ...
        def list(
            self,
            *,
            orderBy: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> ListInventorySourceGroupsResponseHttpRequest: ...
        def patch(
            self,
            *,
            inventorySourceGroupId: str,
            body: InventorySourceGroup = ...,
            partnerId: str = ...,
            advertiserId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> InventorySourceGroupHttpRequest: ...
        def create(
            self,
            *,
            body: InventorySourceGroup = ...,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any
        ) -> InventorySourceGroupHttpRequest: ...
        def delete(
            self,
            *,
            inventorySourceGroupId: str,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def assignedInventorySources(self) -> AssignedInventorySourcesResource: ...
    class CustomListsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, customListId: str, advertiserId: str = ..., **kwargs: typing.Any
        ) -> CustomListHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            filter: str = ...,
            advertiserId: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListCustomListsResponseHttpRequest: ...
    class FirstAndThirdPartyAudiencesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            firstAndThirdPartyAudienceId: str,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> FirstAndThirdPartyAudienceHttpRequest: ...
        def list(
            self,
            *,
            partnerId: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            advertiserId: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            **kwargs: typing.Any
        ) -> ListFirstAndThirdPartyAudiencesResponseHttpRequest: ...
    class FloodlightGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, floodlightGroupId: str, partnerId: str = ..., **kwargs: typing.Any
        ) -> FloodlightGroupHttpRequest: ...
        def patch(
            self,
            *,
            floodlightGroupId: str,
            body: FloodlightGroup = ...,
            updateMask: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any
        ) -> FloodlightGroupHttpRequest: ...
    class CombinedAudiencesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            advertiserId: str = ...,
            filter: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any
        ) -> ListCombinedAudiencesResponseHttpRequest: ...
        def get(
            self,
            *,
            combinedAudienceId: str,
            advertiserId: str = ...,
            partnerId: str = ...,
            **kwargs: typing.Any
        ) -> CombinedAudienceHttpRequest: ...
    class UsersResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            userId: str,
            body: User = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> UserHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListUsersResponseHttpRequest: ...
        def delete(self, *, userId: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def bulkEditAssignedUserRoles(
            self,
            *,
            userId: str,
            body: BulkEditAssignedUserRolesRequest = ...,
            **kwargs: typing.Any
        ) -> BulkEditAssignedUserRolesResponseHttpRequest: ...
        def get(self, *, userId: str, **kwargs: typing.Any) -> UserHttpRequest: ...
        def create(
            self, *, body: User = ..., **kwargs: typing.Any
        ) -> UserHttpRequest: ...
    class InventorySourcesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            advertiserId: str = ...,
            partnerId: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListInventorySourcesResponseHttpRequest: ...
        def get(
            self, *, inventorySourceId: str, partnerId: str = ..., **kwargs: typing.Any
        ) -> InventorySourceHttpRequest: ...
    class CustomBiddingAlgorithmsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            orderBy: str = ...,
            pageToken: str = ...,
            partnerId: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> ListCustomBiddingAlgorithmsResponseHttpRequest: ...
        def get(
            self,
            *,
            customBiddingAlgorithmId: str,
            partnerId: str = ...,
            advertiserId: str = ...,
            **kwargs: typing.Any
        ) -> CustomBiddingAlgorithmHttpRequest: ...
    def sdfdownloadtasks(self) -> SdfdownloadtasksResource: ...
    def advertisers(self) -> AdvertisersResource: ...
    def media(self) -> MediaResource: ...
    def targetingTypes(self) -> TargetingTypesResource: ...
    def partners(self) -> PartnersResource: ...
    def googleAudiences(self) -> GoogleAudiencesResource: ...
    def inventorySourceGroups(self) -> InventorySourceGroupsResource: ...
    def customLists(self) -> CustomListsResource: ...
    def firstAndThirdPartyAudiences(self) -> FirstAndThirdPartyAudiencesResource: ...
    def floodlightGroups(self) -> FloodlightGroupsResource: ...
    def combinedAudiences(self) -> CombinedAudiencesResource: ...
    def users(self) -> UsersResource: ...
    def inventorySources(self) -> InventorySourcesResource: ...
    def customBiddingAlgorithms(self) -> CustomBiddingAlgorithmsResource: ...

class AssignedTargetingOptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AssignedTargetingOption: ...

class ListNegativeKeywordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNegativeKeywordsResponse: ...

class ListFirstAndThirdPartyAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFirstAndThirdPartyAudiencesResponse: ...

class ListNegativeKeywordListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNegativeKeywordListsResponse: ...

class InventorySourceGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventorySourceGroup: ...

class BulkListAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkListAdvertiserAssignedTargetingOptionsResponse: ...

class ListAssignedInventorySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssignedInventorySourcesResponse: ...

class ListPartnersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPartnersResponse: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class BulkListLineItemAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkListLineItemAssignedTargetingOptionsResponse: ...

class ListGoogleAudiencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGoogleAudiencesResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class CustomListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomList: ...

class ListCombinedAudiencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCombinedAudiencesResponse: ...

class AssignedLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AssignedLocation: ...

class PartnerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Partner: ...

class BulkEditAssignedInventorySourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditAssignedInventorySourcesResponse: ...

class AuditAdvertiserResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AuditAdvertiserResponse: ...

class CreateAssetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateAssetResponse: ...

class GoogleBytestreamMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleBytestreamMedia: ...

class ListPartnerAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPartnerAssignedTargetingOptionsResponse: ...

class BulkEditPartnerAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditPartnerAssignedTargetingOptionsResponse: ...

class LocationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LocationList: ...

class ListAssignedLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssignedLocationsResponse: ...

class ListLocationListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationListsResponse: ...

class ListCustomListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCustomListsResponse: ...

class CombinedAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CombinedAudience: ...

class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativesResponse: ...

class BulkEditAssignedLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditAssignedLocationsResponse: ...

class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Site: ...

class InventorySourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InventorySource: ...

class AdvertiserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Advertiser: ...

class BulkEditNegativeKeywordsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditNegativeKeywordsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class AssignedInventorySourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AssignedInventorySource: ...

class NegativeKeywordListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NegativeKeywordList: ...

class GoogleAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAudience: ...

class FirstAndThirdPartyAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirstAndThirdPartyAudience: ...

class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListChannelsResponse: ...

class NegativeKeywordHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NegativeKeyword: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class ListInventorySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInventorySourcesResponse: ...

class ListLineItemAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLineItemAssignedTargetingOptionsResponse: ...

class BulkEditAssignedUserRolesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditAssignedUserRolesResponse: ...

class CustomBiddingAlgorithmHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomBiddingAlgorithm: ...

class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUsersResponse: ...

class BulkEditSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditSitesResponse: ...

class BulkEditLineItemAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditLineItemAssignedTargetingOptionsResponse: ...

class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSitesResponse: ...

class TargetingOptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetingOption: ...

class LineItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LineItem: ...

class ListCampaignsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCampaignsResponse: ...

class ListAdvertisersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAdvertisersResponse: ...

class FloodlightGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FloodlightGroup: ...

class ListTargetingOptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTargetingOptionsResponse: ...

class CampaignHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Campaign: ...

class ListLineItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLineItemsResponse: ...

class BulkEditAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BulkEditAdvertiserAssignedTargetingOptionsResponse: ...

class ListAdvertiserAssignedTargetingOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAdvertiserAssignedTargetingOptionsResponse: ...

class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> User: ...

class ListCustomBiddingAlgorithmsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCustomBiddingAlgorithmsResponse: ...

class ListInventorySourceGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInventorySourceGroupsResponse: ...

class InsertionOrderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InsertionOrder: ...

class ListInsertionOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInsertionOrdersResponse: ...
