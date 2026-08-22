import typing

_list = list

@typing.type_check_only
class AdSource(typing.TypedDict, total=False):
    adSourceId: str
    name: str
    title: str

@typing.type_check_only
class AdUnit(typing.TypedDict, total=False):
    adFormat: str
    adTypes: _list[str]
    adUnitId: str
    appId: str
    displayName: str
    name: str
    rewardSettings: AdUnitRewardSettings

@typing.type_check_only
class AdUnitMapping(typing.TypedDict, total=False):
    adUnitConfigurations: dict[str, typing.Any]
    adapterId: str
    displayName: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED"]

@typing.type_check_only
class AdUnitRewardSettings(typing.TypedDict, total=False):
    unitAmount: str
    unitType: str

@typing.type_check_only
class Adapter(typing.TypedDict, total=False):
    adapterConfigMetadata: _list[AdapterAdapterConfigMetadata]
    adapterId: str
    formats: _list[str]
    name: str
    platform: str
    title: str

@typing.type_check_only
class AdapterAdapterConfigMetadata(typing.TypedDict, total=False):
    adapterConfigMetadataId: str
    adapterConfigMetadataLabel: str
    isRequired: bool

@typing.type_check_only
class App(typing.TypedDict, total=False):
    appApprovalState: typing.Literal[
        "APP_APPROVAL_STATE_UNSPECIFIED", "ACTION_REQUIRED", "IN_REVIEW", "APPROVED"
    ]
    appId: str
    linkedAppInfo: AppLinkedAppInfo
    manualAppInfo: AppManualAppInfo
    name: str
    platform: str

@typing.type_check_only
class AppLinkedAppInfo(typing.TypedDict, total=False):
    androidAppStores: _list[
        typing.Literal[
            "ANDROID_APP_STORE_UNSPECIFIED",
            "GOOGLE_PLAY_APP_STORE",
            "AMAZON_APP_STORE",
            "OPPO_APP_STORE",
            "SAMSUNG_APP_STORE",
            "VIVO_APP_STORE",
            "XIAOMI_APP_STORE",
        ]
    ]
    appStoreId: str
    displayName: str

@typing.type_check_only
class AppManualAppInfo(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class BatchCreateAdUnitMappingsRequest(typing.TypedDict, total=False):
    requests: _list[CreateAdUnitMappingRequest]

@typing.type_check_only
class BatchCreateAdUnitMappingsResponse(typing.TypedDict, total=False):
    adUnitMappings: _list[AdUnitMapping]

@typing.type_check_only
class CampaignReportSpec(typing.TypedDict, total=False):
    dateRange: DateRange
    dimensions: _list[
        typing.Literal[
            "DIMENSION_UNSPECIFIED",
            "DATE",
            "CAMPAIGN_ID",
            "CAMPAIGN_NAME",
            "AD_ID",
            "AD_NAME",
            "PLACEMENT_ID",
            "PLACEMENT_NAME",
            "PLACEMENT_PLATFORM",
            "COUNTRY",
            "FORMAT",
        ]
    ]
    languageCode: str
    metrics: _list[
        typing.Literal[
            "METRIC_UNSPECIFIED",
            "IMPRESSIONS",
            "CLICKS",
            "CLICK_THROUGH_RATE",
            "INSTALLS",
            "ESTIMATED_COST",
            "AVERAGE_CPI",
            "INTERACTIONS",
        ]
    ]

@typing.type_check_only
class CreateAdUnitMappingRequest(typing.TypedDict, total=False):
    adUnitMapping: AdUnitMapping
    parent: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateRange(typing.TypedDict, total=False):
    endDate: Date
    startDate: Date

@typing.type_check_only
class GenerateCampaignReportRequest(typing.TypedDict, total=False):
    reportSpec: CampaignReportSpec

@typing.type_check_only
class GenerateCampaignReportResponse(typing.TypedDict, total=False):
    rows: _list[ReportRow]

@typing.type_check_only
class GenerateMediationReportRequest(typing.TypedDict, total=False):
    reportSpec: MediationReportSpec

@typing.type_check_only
class GenerateMediationReportResponse(typing.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class GenerateNetworkReportRequest(typing.TypedDict, total=False):
    reportSpec: NetworkReportSpec

@typing.type_check_only
class GenerateNetworkReportResponse(typing.TypedDict, total=False):
    footer: ReportFooter
    header: ReportHeader
    row: ReportRow

@typing.type_check_only
class ListAdSourcesResponse(typing.TypedDict, total=False):
    adSources: _list[AdSource]
    nextPageToken: str

@typing.type_check_only
class ListAdUnitMappingsResponse(typing.TypedDict, total=False):
    adUnitMappings: _list[AdUnitMapping]
    nextPageToken: str

@typing.type_check_only
class ListAdUnitsResponse(typing.TypedDict, total=False):
    adUnits: _list[AdUnit]
    nextPageToken: str

@typing.type_check_only
class ListAdaptersResponse(typing.TypedDict, total=False):
    adapters: _list[Adapter]
    nextPageToken: str

@typing.type_check_only
class ListAppsResponse(typing.TypedDict, total=False):
    apps: _list[App]
    nextPageToken: str

@typing.type_check_only
class ListMediationGroupsResponse(typing.TypedDict, total=False):
    mediationGroups: _list[MediationGroup]
    nextPageToken: str

@typing.type_check_only
class ListPublisherAccountsResponse(typing.TypedDict, total=False):
    account: _list[PublisherAccount]
    nextPageToken: str

@typing.type_check_only
class LocalizationSettings(typing.TypedDict, total=False):
    currencyCode: str
    languageCode: str

@typing.type_check_only
class MediationAbExperiment(typing.TypedDict, total=False):
    controlMediationLines: _list[MediationAbExperimentExperimentMediationLine]
    displayName: str
    endTime: str
    experimentId: str
    mediationGroupId: str
    name: str
    startTime: str
    state: typing.Literal["EXPERIMENT_STATE_UNSPECIFIED", "EXPIRED", "RUNNING", "ENDED"]
    treatmentMediationLines: _list[MediationAbExperimentExperimentMediationLine]
    treatmentTrafficPercentage: str
    variantLeader: typing.Literal[
        "VARIANT_LEADER_UNSPECIFIED",
        "CONTROL",
        "TREATMENT",
        "INSUFFICIENT_DATA",
        "TOO_EARLY_TO_CALL",
        "NO_VARIANT_LEADER",
    ]

@typing.type_check_only
class MediationAbExperimentExperimentMediationLine(typing.TypedDict, total=False):
    mediationGroupLine: MediationGroupMediationGroupLine

@typing.type_check_only
class MediationGroup(typing.TypedDict, total=False):
    displayName: str
    mediationAbExperimentState: typing.Literal[
        "EXPERIMENT_STATE_UNSPECIFIED", "RUNNING", "NOT_RUNNING"
    ]
    mediationGroupId: str
    mediationGroupLines: dict[str, typing.Any]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]
    targeting: MediationGroupTargeting

@typing.type_check_only
class MediationGroupMediationGroupLine(typing.TypedDict, total=False):
    adSourceId: str
    adUnitMappings: dict[str, typing.Any]
    cpmMicros: str
    cpmMode: typing.Literal["CPM_MODE_UNSPECIFIED", "LIVE", "MANUAL", "ANO"]
    displayName: str
    experimentVariant: typing.Literal[
        "VARIANT_UNSPECIFIED", "VARIANT_A", "VARIANT_B", "ORIGINAL"
    ]
    id: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED", "REMOVED"]

@typing.type_check_only
class MediationGroupTargeting(typing.TypedDict, total=False):
    adUnitIds: _list[str]
    excludedRegionCodes: _list[str]
    format: str
    idfaTargeting: typing.Literal[
        "IDFA_TARGETING_UNSPECIFIED", "ALL", "AVAILABLE", "NOT_AVAILABLE"
    ]
    platform: str
    targetedRegionCodes: _list[str]

@typing.type_check_only
class MediationReportSpec(typing.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[MediationReportSpecDimensionFilter]
    dimensions: _list[
        typing.Literal[
            "DIMENSION_UNSPECIFIED",
            "DATE",
            "MONTH",
            "WEEK",
            "AD_SOURCE",
            "AD_SOURCE_INSTANCE",
            "AD_UNIT",
            "APP",
            "MEDIATION_GROUP",
            "COUNTRY",
            "FORMAT",
            "PLATFORM",
            "MOBILE_OS_VERSION",
            "GMA_SDK_VERSION",
            "APP_VERSION_NAME",
            "SERVING_RESTRICTION",
        ]
    ]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[
        typing.Literal[
            "METRIC_UNSPECIFIED",
            "AD_REQUESTS",
            "CLICKS",
            "ESTIMATED_EARNINGS",
            "IMPRESSIONS",
            "IMPRESSION_CTR",
            "MATCHED_REQUESTS",
            "MATCH_RATE",
            "OBSERVED_ECPM",
        ]
    ]
    sortConditions: _list[MediationReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class MediationReportSpecDimensionFilter(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_SOURCE",
        "AD_SOURCE_INSTANCE",
        "AD_UNIT",
        "APP",
        "MEDIATION_GROUP",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    matchesAny: StringList

@typing.type_check_only
class MediationReportSpecSortCondition(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_SOURCE",
        "AD_SOURCE_INSTANCE",
        "AD_UNIT",
        "APP",
        "MEDIATION_GROUP",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    metric: typing.Literal[
        "METRIC_UNSPECIFIED",
        "AD_REQUESTS",
        "CLICKS",
        "ESTIMATED_EARNINGS",
        "IMPRESSIONS",
        "IMPRESSION_CTR",
        "MATCHED_REQUESTS",
        "MATCH_RATE",
        "OBSERVED_ECPM",
    ]
    order: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class NetworkReportSpec(typing.TypedDict, total=False):
    dateRange: DateRange
    dimensionFilters: _list[NetworkReportSpecDimensionFilter]
    dimensions: _list[
        typing.Literal[
            "DIMENSION_UNSPECIFIED",
            "DATE",
            "MONTH",
            "WEEK",
            "AD_UNIT",
            "APP",
            "AD_TYPE",
            "COUNTRY",
            "FORMAT",
            "PLATFORM",
            "MOBILE_OS_VERSION",
            "GMA_SDK_VERSION",
            "APP_VERSION_NAME",
            "SERVING_RESTRICTION",
        ]
    ]
    localizationSettings: LocalizationSettings
    maxReportRows: int
    metrics: _list[
        typing.Literal[
            "METRIC_UNSPECIFIED",
            "AD_REQUESTS",
            "CLICKS",
            "ESTIMATED_EARNINGS",
            "IMPRESSIONS",
            "IMPRESSION_CTR",
            "IMPRESSION_RPM",
            "MATCHED_REQUESTS",
            "MATCH_RATE",
            "SHOW_RATE",
        ]
    ]
    sortConditions: _list[NetworkReportSpecSortCondition]
    timeZone: str

@typing.type_check_only
class NetworkReportSpecDimensionFilter(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_UNIT",
        "APP",
        "AD_TYPE",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    matchesAny: StringList

@typing.type_check_only
class NetworkReportSpecSortCondition(typing.TypedDict, total=False):
    dimension: typing.Literal[
        "DIMENSION_UNSPECIFIED",
        "DATE",
        "MONTH",
        "WEEK",
        "AD_UNIT",
        "APP",
        "AD_TYPE",
        "COUNTRY",
        "FORMAT",
        "PLATFORM",
        "MOBILE_OS_VERSION",
        "GMA_SDK_VERSION",
        "APP_VERSION_NAME",
        "SERVING_RESTRICTION",
    ]
    metric: typing.Literal[
        "METRIC_UNSPECIFIED",
        "AD_REQUESTS",
        "CLICKS",
        "ESTIMATED_EARNINGS",
        "IMPRESSIONS",
        "IMPRESSION_CTR",
        "IMPRESSION_RPM",
        "MATCHED_REQUESTS",
        "MATCH_RATE",
        "SHOW_RATE",
    ]
    order: typing.Literal["SORT_ORDER_UNSPECIFIED", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class PublisherAccount(typing.TypedDict, total=False):
    currencyCode: str
    name: str
    publisherId: str
    reportingTimeZone: str

@typing.type_check_only
class ReportFooter(typing.TypedDict, total=False):
    matchingRowCount: str
    warnings: _list[ReportWarning]

@typing.type_check_only
class ReportHeader(typing.TypedDict, total=False):
    dateRange: DateRange
    localizationSettings: LocalizationSettings
    reportingTimeZone: str

@typing.type_check_only
class ReportRow(typing.TypedDict, total=False):
    dimensionValues: dict[str, typing.Any]
    metricValues: dict[str, typing.Any]

@typing.type_check_only
class ReportRowDimensionValue(typing.TypedDict, total=False):
    displayLabel: str
    value: str

@typing.type_check_only
class ReportRowMetricValue(typing.TypedDict, total=False):
    doubleValue: float
    integerValue: str
    microsValue: str

@typing.type_check_only
class ReportWarning(typing.TypedDict, total=False):
    description: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "DATA_BEFORE_ACCOUNT_TIMEZONE_CHANGE",
        "DATA_DELAYED",
        "OTHER",
        "REPORT_CURRENCY_NOT_ACCOUNT_CURRENCY",
    ]

@typing.type_check_only
class StopMediationAbExperimentRequest(typing.TypedDict, total=False):
    variantChoice: typing.Literal[
        "VARIANT_CHOICE_UNSPECIFIED", "VARIANT_CHOICE_A", "VARIANT_CHOICE_B"
    ]

@typing.type_check_only
class StringList(typing.TypedDict, total=False):
    values: _list[str]
