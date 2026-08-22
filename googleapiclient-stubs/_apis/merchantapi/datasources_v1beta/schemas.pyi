import typing

_list = list

@typing.type_check_only
class DataSource(typing.TypedDict, total=False):
    dataSourceId: str
    displayName: str
    fileInput: FileInput
    input: typing.Literal["INPUT_UNSPECIFIED", "API", "FILE", "UI", "AUTOFEED"]
    localInventoryDataSource: LocalInventoryDataSource
    merchantReviewDataSource: MerchantReviewDataSource
    name: str
    primaryProductDataSource: PrimaryProductDataSource
    productReviewDataSource: ProductReviewDataSource
    promotionDataSource: PromotionDataSource
    regionalInventoryDataSource: RegionalInventoryDataSource
    supplementalProductDataSource: SupplementalProductDataSource

@typing.type_check_only
class DataSourceReference(typing.TypedDict, total=False):
    primaryDataSourceName: str
    self: bool
    supplementalDataSourceName: str

@typing.type_check_only
class DefaultRule(typing.TypedDict, total=False):
    takeFromDataSources: _list[DataSourceReference]

@typing.type_check_only
class Destination(typing.TypedDict, total=False):
    destination: typing.Literal[
        "DESTINATION_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LOCAL_LISTINGS",
        "YOUTUBE_SHOPPING",
        "YOUTUBE_SHOPPING_CHECKOUT",
        "YOUTUBE_AFFILIATE",
        "FREE_VEHICLE_LISTINGS",
        "VEHICLE_ADS",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
    ]
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED"]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchDataSourceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FetchSettings(typing.TypedDict, total=False):
    dayOfMonth: int
    dayOfWeek: typing.Literal[
        "DAY_OF_WEEK_UNSPECIFIED",
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY",
    ]
    enabled: bool
    fetchUri: str
    frequency: typing.Literal[
        "FREQUENCY_UNSPECIFIED",
        "FREQUENCY_DAILY",
        "FREQUENCY_WEEKLY",
        "FREQUENCY_MONTHLY",
    ]
    password: str
    timeOfDay: TimeOfDay
    timeZone: str
    username: str

@typing.type_check_only
class FileInput(typing.TypedDict, total=False):
    fetchSettings: FetchSettings
    fileInputType: typing.Literal[
        "FILE_INPUT_TYPE_UNSPECIFIED", "UPLOAD", "FETCH", "GOOGLE_SHEETS"
    ]
    fileName: str

@typing.type_check_only
class FileUpload(typing.TypedDict, total=False):
    dataSourceId: str
    issues: _list[Issue]
    itemsCreated: str
    itemsTotal: str
    itemsUpdated: str
    name: str
    processingState: typing.Literal[
        "PROCESSING_STATE_UNSPECIFIED", "FAILED", "IN_PROGRESS", "SUCCEEDED"
    ]
    uploadTime: str

@typing.type_check_only
class Issue(typing.TypedDict, total=False):
    code: str
    count: str
    description: str
    documentationUri: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "WARNING", "ERROR"]
    title: str

@typing.type_check_only
class ListDataSourcesResponse(typing.TypedDict, total=False):
    dataSources: _list[DataSource]
    nextPageToken: str

@typing.type_check_only
class LocalInventoryDataSource(typing.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str

@typing.type_check_only
class MerchantReviewDataSource(typing.TypedDict, total=False): ...

@typing.type_check_only
class PrimaryProductDataSource(typing.TypedDict, total=False):
    channel: typing.Literal[
        "CHANNEL_UNSPECIFIED", "ONLINE_PRODUCTS", "LOCAL_PRODUCTS", "PRODUCTS"
    ]
    contentLanguage: str
    countries: _list[str]
    defaultRule: DefaultRule
    destinations: _list[Destination]
    feedLabel: str

@typing.type_check_only
class ProductChange(typing.TypedDict, total=False):
    newValue: str
    oldValue: str
    regionCode: str
    reportingContext: typing.Literal[
        "REPORTING_CONTEXT_ENUM_UNSPECIFIED",
        "SHOPPING_ADS",
        "DISCOVERY_ADS",
        "DEMAND_GEN_ADS",
        "DEMAND_GEN_ADS_DISCOVER_SURFACE",
        "VIDEO_ADS",
        "DISPLAY_ADS",
        "LOCAL_INVENTORY_ADS",
        "VEHICLE_INVENTORY_ADS",
        "FREE_LISTINGS",
        "FREE_LISTINGS_UCP_CHECKOUT",
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductReviewDataSource(typing.TypedDict, total=False): ...

@typing.type_check_only
class ProductStatusChangeMessage(typing.TypedDict, total=False):
    account: str
    attribute: typing.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    eventTime: str
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing.Literal["RESOURCE_UNSPECIFIED", "PRODUCT", "ACCOUNT_SERVICE"]

@typing.type_check_only
class PromotionDataSource(typing.TypedDict, total=False):
    contentLanguage: str
    targetCountry: str

@typing.type_check_only
class RegionalInventoryDataSource(typing.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str

@typing.type_check_only
class SupplementalProductDataSource(typing.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str
    referencingPrimaryDataSources: _list[DataSourceReference]

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int
