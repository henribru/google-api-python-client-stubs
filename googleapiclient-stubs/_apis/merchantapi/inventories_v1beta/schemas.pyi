import typing

import typing_extensions

_list = list

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListLocalInventoriesResponse(typing_extensions.TypedDict, total=False):
    localInventories: _list[LocalInventory]
    nextPageToken: str

@typing.type_check_only
class ListRegionalInventoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regionalInventories: _list[RegionalInventory]

@typing.type_check_only
class LocalInventory(typing_extensions.TypedDict, total=False):
    account: str
    availability: str
    customAttributes: _list[CustomAttribute]
    instoreProductLocation: str
    name: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: str
    salePrice: Price
    salePriceEffectiveDate: Interval
    storeCode: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

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
class RegionalInventory(typing_extensions.TypedDict, total=False):
    account: str
    availability: str
    customAttributes: _list[CustomAttribute]
    name: str
    price: Price
    region: str
    salePrice: Price
    salePriceEffectiveDate: Interval
