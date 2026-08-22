import typing

_list = list

@typing.type_check_only
class CustomAttribute(typing.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class InventoryLoyaltyProgram(typing.TypedDict, total=False):
    cashbackForFutureUse: Price
    loyaltyPoints: str
    memberPriceEffectiveInterval: Interval
    price: Price
    programLabel: str
    shippingLabel: str
    tierLabel: str

@typing.type_check_only
class ListLocalInventoriesResponse(typing.TypedDict, total=False):
    localInventories: _list[LocalInventory]
    nextPageToken: str

@typing.type_check_only
class ListRegionalInventoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    regionalInventories: _list[RegionalInventory]

@typing.type_check_only
class LocalInventory(typing.TypedDict, total=False):
    account: str
    base64EncodedName: str
    localInventoryAttributes: LocalInventoryAttributes
    name: str
    storeCode: str

@typing.type_check_only
class LocalInventoryAttributes(typing.TypedDict, total=False):
    availability: typing.Literal[
        "LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED",
        "IN_STOCK",
        "LIMITED_AVAILABILITY",
        "ON_DISPLAY_TO_ORDER",
        "OUT_OF_STOCK",
    ]
    customAttributes: _list[CustomAttribute]
    instoreProductLocation: str
    localShippingLabel: str
    loyaltyPrograms: _list[InventoryLoyaltyProgram]
    pickupMethod: typing.Literal[
        "PICKUP_METHOD_UNSPECIFIED", "BUY", "RESERVE", "SHIP_TO_STORE", "NOT_SUPPORTED"
    ]
    pickupSla: typing.Literal[
        "PICKUP_SLA_UNSPECIFIED",
        "SAME_DAY",
        "NEXT_DAY",
        "TWO_DAY",
        "THREE_DAY",
        "FOUR_DAY",
        "FIVE_DAY",
        "SIX_DAY",
        "SEVEN_DAY",
        "MULTI_WEEK",
    ]
    price: Price
    quantity: str
    salePrice: Price
    salePriceEffectiveDate: Interval

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

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
class RegionalInventory(typing.TypedDict, total=False):
    account: str
    base64EncodedName: str
    name: str
    region: str
    regionalInventoryAttributes: RegionalInventoryAttributes

@typing.type_check_only
class RegionalInventoryAttributes(typing.TypedDict, total=False):
    availability: typing.Literal[
        "REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED", "IN_STOCK", "OUT_OF_STOCK"
    ]
    loyaltyPrograms: _list[InventoryLoyaltyProgram]
    price: Price
    salePrice: Price
    salePriceEffectiveDate: Interval
