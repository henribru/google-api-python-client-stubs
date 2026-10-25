import typing

_list = list

@typing.type_check_only
class AccessControlSettings(typing.TypedDict, total=False):
    allowlistedMediaPlanners: _list[str]

@typing.type_check_only
class ActivateCuratedPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ActivateDataSegmentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class AdSize(typing.TypedDict, total=False):
    height: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PIXEL", "INTERSTITIAL", "NATIVE", "FLUID"]
    width: str

@typing.type_check_only
class CriteriaTargeting(typing.TypedDict, total=False):
    excludedCriteriaIds: _list[str]
    targetedCriteriaIds: _list[str]

@typing.type_check_only
class CuratedPackage(typing.TypedDict, total=False):
    accessSettings: AccessControlSettings
    createTime: str
    curationFeeVisibility: typing.Literal[
        "CURATION_FEE_VISIBILITY_UNSPECIFIED", "DISCLOSED", "NON_DISCLOSED"
    ]
    description: str
    displayName: str
    feeCpm: Money
    floorPriceCpm: Money
    millipercentOfMediaFee: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    targeting: PackageTargeting
    updateTime: str

@typing.type_check_only
class DataSegment(typing.TypedDict, total=False):
    cpmFee: Money
    createTime: str
    millipercentOfMediaFee: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "SUSPENDED"]
    updateTime: str
    userListId: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    fixed: FixedDateRange
    relative: typing.Literal[
        "RELATIVE_DATE_RANGE_UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "THIS_WEEK_TO_DATE",
        "THIS_WEEK_TO_YESTERDAY",
        "THIS_MONTH_TO_DATE",
        "THIS_MONTH_TO_YESTERDAY",
        "THIS_QUARTER_TO_DATE",
        "THIS_QUARTER_TO_YESTERDAY",
        "THIS_YEAR_TO_DATE",
        "THIS_YEAR_TO_YESTERDAY",
        "LAST_WEEK",
        "LAST_WEEK_STARTING_SUNDAY",
        "LAST_MONTH",
        "LAST_QUARTER",
        "LAST_YEAR",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_60_DAYS",
        "LAST_90_DAYS",
        "LAST_93_DAYS",
        "LAST_180_DAYS",
        "LAST_360_DAYS",
        "LAST_365_DAYS",
        "LAST_3_MONTHS",
        "LAST_6_MONTHS",
        "LAST_12_MONTHS",
        "ALL_AVAILABLE",
    ]

@typing.type_check_only
class DeactivateCuratedPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeactivateDataSegmentRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DoubleList(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchReportResultRowsResponse(typing.TypedDict, total=False):
    dateRanges: _list[FixedDateRange]
    nextPageToken: str
    rows: _list[Row]
    runTime: str
    totalRowCount: int

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "ADVERTISER_DOMAIN",
        "COUNTRY",
        "CURATION_DATA_SEGMENT_ID",
        "CURATION_DATA_SEGMENT_RESPONSE_STATUS",
        "CURATION_DATA_SEGMENT_RESPONSE_STATUS_NAME",
        "CURATOR_FEE_TYPE",
        "DATE",
        "DEAL_ID",
        "DEAL_NAME",
        "DETECTED_ADVERTISER_NAME",
        "DSP_NAME",
        "DSP_SEAT_ID",
        "ENVIRONMENT",
        "ENVIRONMENT_NAME",
        "HOLDING_COMPANY_NAME",
        "HOUR",
        "MOBILE_APP_ID",
        "MOBILE_APP_NAME",
        "MOBILE_OS",
        "MONTH",
        "PACKAGE_FEE_VISIBILITY",
        "PLATFORM",
        "PUBLISHER_DOMAIN",
        "PUBLISHER_ID",
        "PUBLISHER_NAME",
        "WEEK",
    ]
    metric: typing.Literal[
        "METRIC_UNSPECIFIED",
        "ACTIVE_VIEW_MEASURABILITY_RATE",
        "ACTIVE_VIEW_MEASURABLE",
        "ACTIVE_VIEW_VIEWABILITY_RATE",
        "ACTIVE_VIEW_VIEWABLE",
        "AUCTIONS_WON",
        "BIDS",
        "BIDS_IN_AUCTION",
        "BID_REQUESTS",
        "CLICKS",
        "CURATION_PARTNER_FEE",
        "DATA_SEGMENT_REQUESTS",
        "IMPRESSIONS",
        "SPEND",
    ]

@typing.type_check_only
class FieldFilter(typing.TypedDict, total=False):
    field: Field
    operation: typing.Literal[
        "IN",
        "NOT_IN",
        "CONTAINS",
        "NOT_CONTAINS",
        "LESS_THAN",
        "LESS_THAN_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_EQUALS",
        "BETWEEN",
        "MATCHES",
        "NOT_MATCHES",
    ]
    values: _list[ReportValue]

@typing.type_check_only
class Filter(typing.TypedDict, total=False):
    andFilter: FilterList
    fieldFilter: FieldFilter
    notFilter: Filter
    orFilter: FilterList

@typing.type_check_only
class FilterList(typing.TypedDict, total=False):
    filters: _list[Filter]

@typing.type_check_only
class FixedDateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class IntList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ListCuratedPackagesResponse(typing.TypedDict, total=False):
    curatedPackages: _list[CuratedPackage]
    nextPageToken: str

@typing.type_check_only
class ListDataSegmentsResponse(typing.TypedDict, total=False):
    dataSegments: _list[DataSegment]
    nextPageToken: str

@typing.type_check_only
class ListMediaPlannersResponse(typing.TypedDict, total=False):
    mediaPlanners: _list[MediaPlanner]
    nextPageToken: str

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]
    totalSize: int

@typing.type_check_only
class MediaPlanner(typing.TypedDict, total=False):
    accountId: str
    ancestorNames: _list[str]
    displayName: str
    name: str

@typing.type_check_only
class MetricValueGroup(typing.TypedDict, total=False):
    primaryValues: _list[ReportValue]

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PackagePlacementTargeting(typing.TypedDict, total=False):
    includedMobileAppCategoryTargeting: _list[str]
    mobileAppTargeting: StringTargetingDimension
    uriTargeting: StringTargetingDimension

@typing.type_check_only
class PackagePublisherProvidedSignalsTargeting(typing.TypedDict, total=False):
    audienceTargeting: TaxonomyTargeting
    contentTargeting: TaxonomyTargeting
    videoAndAudioSignalsTargeting: StringTargetingDimension

@typing.type_check_only
class PackageTargeting(typing.TypedDict, total=False):
    geoTargeting: CriteriaTargeting
    includedAcceleratedMobilePageType: typing.Literal[
        "ACCELERATED_MOBILE_PAGE_TYPE_UNSPECIFIED",
        "ACCELERATED_MOBILE_PAGE_TYPE_NON_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP",
        "ACCELERATED_MOBILE_PAGE_TYPE_AMP_STORY",
    ]
    includedAdSizes: _list[AdSize]
    includedAuthorizedSellerStatuses: _list[
        typing.Literal[
            "AUTHORIZED_SELLER_STATUS_UNSPECIFIED",
            "AUTHORIZED_SELLER_STATUS_DIRECT",
            "AUTHORIZED_SELLER_STATUS_RESELLER",
        ]
    ]
    includedCreativeFormat: typing.Literal[
        "CREATIVE_FORMAT_UNSPECIFIED",
        "CREATIVE_FORMAT_DISPLAY",
        "CREATIVE_FORMAT_VIDEO",
        "CREATIVE_FORMAT_AUDIO",
    ]
    includedDataSegments: _list[str]
    includedDeviceTypes: _list[
        typing.Literal[
            "DEVICE_TYPE_UNSPECIFIED",
            "DEVICE_TYPE_PERSONAL_COMPUTER",
            "DEVICE_TYPE_CONNECTED_TV",
            "DEVICE_TYPE_PHONE",
            "DEVICE_TYPE_TABLET",
        ]
    ]
    includedEnvironment: typing.Literal[
        "ENVIRONMENT_UNSPECIFIED", "ENVIRONMENT_SITE", "ENVIRONMENT_APP"
    ]
    includedNativeInventoryTypes: _list[
        typing.Literal[
            "NATIVE_INVENTORY_TYPE_UNSPECIFIED",
            "NATIVE_INVENTORY_TYPE_NATIVE_ONLY",
            "NATIVE_INVENTORY_TYPE_NATIVE_OR_BANNER",
        ]
    ]
    includedOpenMeasurementTypes: _list[
        typing.Literal[
            "OPEN_MEASUREMENT_TYPE_UNSPECIFIED", "OPEN_MEASUREMENT_TYPE_OMID_V1"
        ]
    ]
    includedRestrictedCategories: _list[
        typing.Literal[
            "RESTRICTED_CATEGORY_UNSPECIFIED",
            "RESTRICTED_CATEGORY_ALCOHOL",
            "RESTRICTED_CATEGORY_GAMBLING",
        ]
    ]
    includedRewardedType: typing.Literal[
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
class PackageVideoTargeting(typing.TypedDict, total=False):
    includedContentDeliveryMethod: typing.Literal[
        "CONTENT_DELIVERY_METHOD_UNSPECIFIED",
        "CONTENT_DELIVERY_METHOD_STREAMING",
        "CONTENT_DELIVERY_METHOD_PROGRESSIVE",
    ]
    includedMaximumAdDurationTargeting: typing.Literal[
        "MAXIMUM_VIDEO_AD_DURATION_UNSPECIFIED",
        "MAXIMUM_VIDEO_AD_DURATION_FIFTEEN_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_TWENTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_THIRTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_SIXTY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_NINETY_SECONDS",
        "MAXIMUM_VIDEO_AD_DURATION_ONE_HUNDRED_TWENTY_SECONDS",
    ]
    includedMimeTypes: _list[
        typing.Literal[
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
        typing.Literal[
            "PLAYBACK_METHOD_UNSPECIFIED",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_ON",
            "PLAYBACK_METHOD_AUTO_PLAY_SOUND_OFF",
            "PLAYBACK_METHOD_CLICK_TO_PLAY",
        ]
    ]
    includedPlayerSizeTargeting: VideoPlayerSizeTargeting
    includedPositionTypes: _list[
        typing.Literal[
            "POSITION_TYPE_UNSPECIFIED",
            "POSITION_TYPE_MIDROLL",
            "POSITION_TYPE_POSTROLL",
            "POSITION_TYPE_PREROLL",
        ]
    ]
    minimumPredictedCompletionRatePercentage: str
    plcmtTargeting: VideoPlcmtTargeting

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    locale: str
    name: str
    reportDefinition: ReportDefinition
    reportId: str
    updateTime: str

@typing.type_check_only
class ReportDefinition(typing.TypedDict, total=False):
    currencyCode: str
    dateRange: DateRange
    dimensions: _list[
        typing.Literal[
            "DIMENSION_UNSPECIFIED",
            "ADVERTISER_DOMAIN",
            "COUNTRY",
            "CURATION_DATA_SEGMENT_ID",
            "CURATION_DATA_SEGMENT_RESPONSE_STATUS",
            "CURATION_DATA_SEGMENT_RESPONSE_STATUS_NAME",
            "CURATOR_FEE_TYPE",
            "DATE",
            "DEAL_ID",
            "DEAL_NAME",
            "DETECTED_ADVERTISER_NAME",
            "DSP_NAME",
            "DSP_SEAT_ID",
            "ENVIRONMENT",
            "ENVIRONMENT_NAME",
            "HOLDING_COMPANY_NAME",
            "HOUR",
            "MOBILE_APP_ID",
            "MOBILE_APP_NAME",
            "MOBILE_OS",
            "MONTH",
            "PACKAGE_FEE_VISIBILITY",
            "PLATFORM",
            "PUBLISHER_DOMAIN",
            "PUBLISHER_ID",
            "PUBLISHER_NAME",
            "WEEK",
        ]
    ]
    filters: _list[Filter]
    metrics: _list[
        typing.Literal[
            "METRIC_UNSPECIFIED",
            "ACTIVE_VIEW_MEASURABILITY_RATE",
            "ACTIVE_VIEW_MEASURABLE",
            "ACTIVE_VIEW_VIEWABILITY_RATE",
            "ACTIVE_VIEW_VIEWABLE",
            "AUCTIONS_WON",
            "BIDS",
            "BIDS_IN_AUCTION",
            "BID_REQUESTS",
            "CLICKS",
            "CURATION_PARTNER_FEE",
            "DATA_SEGMENT_REQUESTS",
            "IMPRESSIONS",
            "SPEND",
        ]
    ]
    sorts: _list[Sort]
    timeZone: str
    timeZoneSource: typing.Literal[
        "TIME_ZONE_SOURCE_UNSPECIFIED", "AD_EXCHANGE", "UTC", "PROVIDED"
    ]

@typing.type_check_only
class ReportValue(typing.TypedDict, total=False):
    boolValue: bool
    bytesValue: str
    doubleListValue: DoubleList
    doubleValue: float
    intListValue: IntList
    intValue: str
    stringListValue: StringList
    stringValue: str

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    dimensionValues: _list[ReportValue]
    metricValueGroups: _list[MetricValueGroup]

@typing.type_check_only
class RunReportMetadata(typing.TypedDict, total=False):
    percentComplete: int
    report: str

@typing.type_check_only
class RunReportRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunReportResponse(typing.TypedDict, total=False):
    reportResult: str

@typing.type_check_only
class Sort(typing.TypedDict, total=False):
    descending: bool
    field: Field

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class StringTargetingDimension(typing.TypedDict, total=False):
    selectionType: typing.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    values: _list[str]

@typing.type_check_only
class TaxonomyTargeting(typing.TypedDict, total=False):
    excludedTaxonomyIds: _list[str]
    targetedTaxonomyIds: _list[str]

@typing.type_check_only
class VideoPlayerSizeTargeting(typing.TypedDict, total=False):
    minimumHeight: str
    minimumWidth: str

@typing.type_check_only
class VideoPlcmtTargeting(typing.TypedDict, total=False):
    selectionType: typing.Literal[
        "SELECTION_TYPE_UNSPECIFIED", "SELECTION_TYPE_INCLUDE", "SELECTION_TYPE_EXCLUDE"
    ]
    videoPlcmtTypes: _list[
        typing.Literal[
            "VIDEO_PLCMT_TYPE_UNSPECIFIED",
            "INSTREAM",
            "ACCOMPANYING_CONTENT",
            "INTERSTITIAL",
            "NO_CONTENT",
        ]
    ]
