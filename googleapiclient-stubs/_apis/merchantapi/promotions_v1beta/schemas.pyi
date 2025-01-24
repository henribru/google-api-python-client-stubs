import typing

import typing_extensions

_list = list

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    brandExclusion: _list[str]
    brandInclusion: _list[str]
    couponValueType: typing_extensions.Literal[
        "COUPON_VALUE_TYPE_UNSPECIFIED",
        "MONEY_OFF",
        "PERCENT_OFF",
        "BUY_M_GET_N_MONEY_OFF",
        "BUY_M_GET_N_PERCENT_OFF",
        "BUY_M_GET_MONEY_OFF",
        "BUY_M_GET_PERCENT_OFF",
        "FREE_GIFT",
        "FREE_GIFT_WITH_VALUE",
        "FREE_GIFT_WITH_ITEM_ID",
        "FREE_SHIPPING_STANDARD",
        "FREE_SHIPPING_OVERNIGHT",
        "FREE_SHIPPING_TWO_DAY",
    ]
    freeGiftDescription: str
    freeGiftItemId: str
    freeGiftValue: Price
    genericRedemptionCode: str
    getThisQuantityDiscounted: str
    itemGroupIdExclusion: _list[str]
    itemGroupIdInclusion: _list[str]
    itemIdExclusion: _list[str]
    itemIdInclusion: _list[str]
    limitQuantity: str
    limitValue: Price
    longTitle: str
    minimumPurchaseAmount: Price
    minimumPurchaseQuantity: str
    moneyOffAmount: Price
    offerType: typing_extensions.Literal[
        "OFFER_TYPE_UNSPECIFIED", "NO_CODE", "GENERIC_CODE"
    ]
    percentOff: str
    productApplicability: typing_extensions.Literal[
        "PRODUCT_APPLICABILITY_UNSPECIFIED", "ALL_PRODUCTS", "SPECIFIC_PRODUCTS"
    ]
    productTypeExclusion: _list[str]
    productTypeInclusion: _list[str]
    promotionDestinations: _list[
        typing_extensions.Literal[
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
    ]
    promotionDisplayTimePeriod: Interval
    promotionEffectiveTimePeriod: Interval
    promotionUrl: str
    storeApplicability: typing_extensions.Literal[
        "STORE_APPLICABILITY_UNSPECIFIED", "ALL_STORES", "SPECIFIC_STORES"
    ]
    storeCodesExclusion: _list[str]
    storeCodesInclusion: _list[str]

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class DestinationStatus(typing_extensions.TypedDict, total=False):
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
    status: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "IN_REVIEW",
        "REJECTED",
        "LIVE",
        "STOPPED",
        "EXPIRED",
        "PENDING",
    ]

@typing.type_check_only
class InsertPromotionRequest(typing_extensions.TypedDict, total=False):
    dataSource: str
    promotion: Promotion

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: _list[str]
    attribute: str
    code: str
    description: str
    detail: str
    documentation: str
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
    resolution: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DEMOTED", "DISAPPROVED"
    ]

@typing.type_check_only
class ListPromotionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    promotions: _list[Promotion]

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
class Promotion(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    dataSource: str
    name: str
    promotionId: str
    promotionStatus: PromotionStatus
    redemptionChannel: _list[
        typing_extensions.Literal[
            "REDEMPTION_CHANNEL_UNSPECIFIED", "IN_STORE", "ONLINE"
        ]
    ]
    targetCountry: str
    versionNumber: str

@typing.type_check_only
class PromotionStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[DestinationStatus]
    itemLevelIssues: _list[ItemLevelIssue]
    lastUpdateDate: str
