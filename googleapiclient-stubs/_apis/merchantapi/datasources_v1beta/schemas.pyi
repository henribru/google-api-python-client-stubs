import typing

import typing_extensions

_list = list

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    displayName: str
    fileInput: FileInput
    input: typing_extensions.Literal[
        "INPUT_UNSPECIFIED", "API", "FILE", "UI", "AUTOFEED"
    ]
    localInventoryDataSource: LocalInventoryDataSource
    name: str
    primaryProductDataSource: PrimaryProductDataSource
    promotionDataSource: PromotionDataSource
    regionalInventoryDataSource: RegionalInventoryDataSource
    supplementalProductDataSource: SupplementalProductDataSource

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchDataSourceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FetchSettings(typing_extensions.TypedDict, total=False):
    dayOfMonth: int
    dayOfWeek: typing_extensions.Literal[
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
    frequency: typing_extensions.Literal[
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
class FileInput(typing_extensions.TypedDict, total=False):
    fetchSettings: FetchSettings
    fileInputType: typing_extensions.Literal[
        "FILE_INPUT_TYPE_UNSPECIFIED", "UPLOAD", "FETCH", "GOOGLE_SHEETS"
    ]
    fileName: str

@typing.type_check_only
class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSources: _list[DataSource]
    nextPageToken: str

@typing.type_check_only
class LocalInventoryDataSource(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str

@typing.type_check_only
class PrimaryProductDataSource(typing_extensions.TypedDict, total=False):
    channel: typing_extensions.Literal[
        "CHANNEL_UNSPECIFIED", "ONLINE_PRODUCTS", "LOCAL_PRODUCTS", "PRODUCTS"
    ]
    contentLanguage: str
    countries: _list[str]
    feedLabel: str

@typing.type_check_only
class ProductChange(typing_extensions.TypedDict, total=False):
    newValue: str
    oldValue: str
    regionCode: str
    reportingContext: typing_extensions.Literal[
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
        "FREE_LOCAL_LISTINGS",
        "FREE_LOCAL_VEHICLE_LISTINGS",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
    ]

@typing.type_check_only
class ProductStatusChangeMessage(typing_extensions.TypedDict, total=False):
    account: str
    attribute: typing_extensions.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class PromotionDataSource(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    targetCountry: str

@typing.type_check_only
class RegionalInventoryDataSource(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str

@typing.type_check_only
class SupplementalProductDataSource(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int
