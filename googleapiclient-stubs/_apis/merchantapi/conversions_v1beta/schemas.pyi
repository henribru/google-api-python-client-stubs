import typing

import typing_extensions

_list = list

@typing.type_check_only
class AttributionSettings(typing_extensions.TypedDict, total=False):
    attributionLookbackWindowDays: int
    attributionModel: typing_extensions.Literal[
        "ATTRIBUTION_MODEL_UNSPECIFIED",
        "CROSS_CHANNEL_LAST_CLICK",
        "ADS_PREFERRED_LAST_CLICK",
        "CROSS_CHANNEL_DATA_DRIVEN",
        "CROSS_CHANNEL_FIRST_CLICK",
        "CROSS_CHANNEL_LINEAR",
        "CROSS_CHANNEL_POSITION_BASED",
        "CROSS_CHANNEL_TIME_DECAY",
    ]
    conversionType: _list[ConversionType]

@typing.type_check_only
class ConversionSource(typing_extensions.TypedDict, total=False):
    controller: typing_extensions.Literal[
        "CONTROLLER_UNSPECIFIED", "MERCHANT", "YOUTUBE_AFFILIATES"
    ]
    expireTime: str
    googleAnalyticsLink: GoogleAnalyticsLink
    merchantCenterDestination: MerchantCenterDestination
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "PENDING"
    ]

@typing.type_check_only
class ConversionType(typing_extensions.TypedDict, total=False):
    name: str
    report: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAnalyticsLink(typing_extensions.TypedDict, total=False):
    attributionSettings: AttributionSettings
    property: str
    propertyId: str

@typing.type_check_only
class ListConversionSourcesResponse(typing_extensions.TypedDict, total=False):
    conversionSources: _list[ConversionSource]
    nextPageToken: str

@typing.type_check_only
class MerchantCenterDestination(typing_extensions.TypedDict, total=False):
    attributionSettings: AttributionSettings
    currencyCode: str
    destination: str
    displayName: str

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
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductStatusChangeMessage(typing_extensions.TypedDict, total=False):
    account: str
    attribute: typing_extensions.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class UndeleteConversionSourceRequest(typing_extensions.TypedDict, total=False): ...
