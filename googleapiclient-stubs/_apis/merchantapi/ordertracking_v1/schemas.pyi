import typing

_list = list

@typing.type_check_only
class DateTime(typing.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: TimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class LineItemDetails(typing.TypedDict, total=False):
    brand: str
    gtins: _list[str]
    lineItemId: str
    mpn: str
    productId: str
    productTitle: str
    quantity: str

@typing.type_check_only
class OrderTrackingSignal(typing.TypedDict, total=False):
    customerShippingFee: Price
    deliveryPostalCode: str
    deliveryRegionCode: str
    lineItems: _list[LineItemDetails]
    merchantId: str
    orderCreatedTime: DateTime
    orderId: str
    orderTrackingSignalId: str
    shipmentLineItemMapping: _list[ShipmentLineItemMapping]
    shippingInfo: _list[ShippingInfo]

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
class ShipmentLineItemMapping(typing.TypedDict, total=False):
    lineItemId: str
    quantity: str
    shipmentId: str

@typing.type_check_only
class ShippingInfo(typing.TypedDict, total=False):
    actualDeliveryTime: DateTime
    carrier: str
    carrierService: str
    earliestDeliveryPromiseTime: DateTime
    latestDeliveryPromiseTime: DateTime
    originPostalCode: str
    originRegionCode: str
    shipmentId: str
    shippedTime: DateTime
    shippingStatus: typing.Literal["SHIPPING_STATE_UNSPECIFIED", "SHIPPED", "DELIVERED"]
    trackingId: str

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str
