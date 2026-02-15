import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessControlSettings(typing_extensions.TypedDict, total=False):
    allowlistedMediaPlanners: _list[str]

@typing.type_check_only
class ActivateCuratedPackageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ActivateDataSegmentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AdSize(typing_extensions.TypedDict, total=False):
    height: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"
    ]
    width: str

@typing.type_check_only
class CriteriaTargeting(typing_extensions.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

@typing.type_check_only
class CuratedPackage(typing_extensions.TypedDict, total=False):
    accessSettings: AccessControlSettings
    createTime: str
    description: str
    displayName: str
    feeCpm: Money
    floorPriceCpm: Money
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    targeting: PackageTargeting
    updateTime: str

@typing.type_check_only
class DataSegment(typing_extensions.TypedDict, total=False):
    cpmFee: Money
    createTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    updateTime: str

@typing.type_check_only
class DeactivateCuratedPackageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateDataSegmentRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListCuratedPackagesResponse(typing_extensions.TypedDict, total=False):
    curatedPackages: _list[CuratedPackage]
    nextPageToken: str

@typing.type_check_only
class ListDataSegmentsResponse(typing_extensions.TypedDict, total=False):
    dataSegments: _list[DataSegment]
    nextPageToken: str

@typing.type_check_only
class ListMediaPlannersResponse(typing_extensions.TypedDict, total=False):
    mediaPlanners: _list[MediaPlanner]
    nextPageToken: str

@typing.type_check_only
class MediaPlanner(typing_extensions.TypedDict, total=False):
    accountId: str
    ancestorNames: _list[str]
    displayName: str
    name: str

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class PackagePlacementTargeting(typing_extensions.TypedDict, total=False):
    includedMobileAppCategoryTargeting: _list[str]
    mobileAppTargeting: StringTargetingDimension
    uriTargeting: StringTargetingDimension

@typing.type_check_only
class PackagePublisherProvidedSignalsTargeting(
    typing_extensions.TypedDict, total=False
):
    audienceTargeting: TaxonomyTargeting
    contentTargeting: TaxonomyTargeting
    videoAndAudioSignalsTargeting: StringTargetingDimension

@typing.type_check_only
class PackageTargeting(typing_extensions.TypedDict, total=False):
    geoTargeting: CriteriaTargeting
    includedAcceleratedMobilePageType: typing_extensions.Literal[
        "ACCELERATED_MOBILE_PAGE_TYPE_UNSPECIFIED",
        "ACCELERATED_MOBILE_PAGE_TYPE_NON_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP_STORY",
    ]
    includedAdSizes: _list[AdSize]
    includedAuthorizedSellerStatuses: _list[
        typing_extensions.Literal[
            "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
            "AUTHORIZED_SELLER_STATUS_DIRECT",
            "AUTHORIZED_SELLER_STATUS_RESELLER",
        ]
    ]
    includedCreativeFormat: typing_extensions.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED",
        "CREATIVE_FORMAT_DISPLAY",
        "CREATIVE_FORMAT_VIDEO",
        "CREATIVE_FORMAT_AUDIO",
    ]
    includedDataSegments: _list[str]
    includedDeviceTypes: _list[
        typing_extensions.Literal[
            "DEVICE_TYPE_UNSPECIFIED",
            "DEVICE_TYPE_PERSONAL_COMPUTER",
            "DEVICE_TYPE_CONNECTED_TV",
            "DEVICE_TYPE_PHONE",
            "DEVICE_TYPE_TABLET",
        ]
    ]
    includedEnvironment: typing_extensions.Literal[
        "ENVIRONMENT_UNSPECIFIED", "ENVIRONMENT_SITE", "ENVIRONMENT_APP"
    ]
    includedNativeInventoryTypes: _list[
        typing_extensions.Literal[
            "NATIVE_INVENTORY_TYPE_UNSPECIFIED",
            "NATIVE_INVENTORY_TYPE_NATIVE_ONLY",
            "NATIVE_INVENTORY_TYPE_NATIVE_OR_BANNER",
        ]
    ]
    includedOpenMeasurementTypes: _list[
        typing_extensions.Literal[
            "OPEN_MEASUREMENT_TYPE_UNSPECIFIED", "OPEN_MEASUREMENT_TYPE_OMID_V1"
        ]
    ]
    includedRestrictedCategories: _list[
        typing_extensions.Literal[
            "RESTRICTED_CATEGORY_UNSPECIFIED",
            "RESTRICTED_CATEGORY_ALCOHOL",
            "RESTRICTED_CATEGORY_GAMBLING",
        ]
    ]
    includedRewardedType: typing_extensions.Literal[
        "REWARDED_TYPE_UNSPECIFIED",
        "REWARDED_TYPE_NON_REWARDED",
        "REWARDED_TYPE_REWARDED",
    ]
    languageTargeting: StringTargetingDimension
    minimumPredictedClickThroughRatePercentageMillis: str
    minimumPredictedViewabilityPercentage: str
    placementTargeting: PackagePlacementTargeting
    publisherProvidedSignalsTargeting: PackagePublisherProvidedSignalsTargeting
    publisherTargeting: StringTargetingDimension
    verticalTargeting: CriteriaTargeting
    videoTargeting: PackageVideoTargeting

@typing.type_check_only
class PackageVideoTargeting(typing_extensions.TypedDict, total=False):
    includedContentDeliveryMethod: typing_extensions.Literal[
        "CONTENT_DELIVERY_METHOD_UNSPECIFIED",
        "CONTENT_DELIVERY_METHOD_STREAMING",
        "CONTENT_DELIVERY_METHOD_PROGRESSIVE",
    ]
    includedMaximumAdDurationTargeting: typing_extensions.Literal[
        "MAXIMUM_VIDEO_AD_DURATION_UNSPECIFIED",
        "MAXIMUM_VIDEO_AD_DURATION_FIFTEEN_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_TWENTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_THIRTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_SIXTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_NINETY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_ONE_HUNDRED_TWENTY_SECONDS",
    ]
    includedMimeTypes: _list[
        typing_extensions.Literal[
            "VIDEO_MIME_TYPE_UNSPECIFIED",
            "VIDEO_MIME_TYPE_THREEGPP",
            "VIDEO_MIME_TYPE_APPLICATION_MPEGURL",
            "VIDEO_MIME_TYPE_MP4",
            "VIDEO_MIME_TYPE_APPLICATION_MPEGDASH",
            "VIDEO_MIME_TYPE_APPLICATION_JAVASCRIPT",
            "VIDEO_MIME_TYPE_WEBM",
        ]
    ]
    includedPlaybackMethods: _list[
        typing_extensions.Literal[
            "PLAYBACK_METHOD_UNSPECIFIED",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_ON",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_OFF",
            "PLAYBACK_METHOD_CLICK_TO_PLAY",
        ]
    ]
    includedPlayerSizeTargeting: VideoPlayerSizeTargeting
    includedPositionTypes: _list[
        typing_extensions.Literal[
            "POSITION_TYPE_UNSPECIFIED",
            "POSITION_TYPE_MIDROLL",
            "POSITION_TYPE_POSTROLL",
            "POSITION_TYPE_PREROLL",
        ]
    ]
    minimumPredictedCompletionRatePercentage: str
    plcmtTargeting: VideoPlcmtTargeting

@typing.type_check_only
class StringTargetingDimension(typing_extensions.TypedDict, total=False):
    selectionType: typing_extensions.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    values: _list[str]

@typing.type_check_only
class TaxonomyTargeting(typing_extensions.TypedDict, total=False):
    excludedTaxonomyIds: _list[str]
    targetedTaxonomyIds: _list[str]

@typing.type_check_only
class VideoPlayerSizeTargeting(typing_extensions.TypedDict, total=False):
    minimumHeight: str
    minimumWidth: str

@typing.type_check_only
class VideoPlcmtTargeting(typing_extensions.TypedDict, total=False):
    selectionType: typing_extensions.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    videoPlcmtTypes: _list[
        typing_extensions.Literal[
            "VIDEO_PLCMT_TYPE_UNSPECIFIED",
            "INSTREAM",
            "ACCOMPANYING_CONTENT",
            "INTERSTITIAL",
            "NO_CONTENT",
        ]
    ]
