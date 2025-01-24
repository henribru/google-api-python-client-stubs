import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LfpInventory(typing_extensions.TypedDict, total=False):
    availability: str
    collectionTime: str
    contentLanguage: str
    feedLabel: str
    gtin: str
    name: str
    offerId: str
    pickupMethod: str
    pickupSla: str
    price: Price
    quantity: str
    regionCode: str
    storeCode: str
    targetAccount: str

@typing.type_check_only
class LfpSale(typing_extensions.TypedDict, total=False):
    contentLanguage: str
    feedLabel: str
    gtin: str
    name: str
    offerId: str
    price: Price
    quantity: str
    regionCode: str
    saleTime: str
    storeCode: str
    targetAccount: str
    uid: str

@typing.type_check_only
class LfpStore(typing_extensions.TypedDict, total=False):
    gcidCategory: _list[str]
    matchingState: typing_extensions.Literal[
        "STORE_MATCHING_STATE_UNSPECIFIED",
        "STORE_MATCHING_STATE_MATCHED",
        "STORE_MATCHING_STATE_FAILED",
    ]
    matchingStateHint: str
    name: str
    phoneNumber: str
    placeId: str
    storeAddress: str
    storeCode: str
    storeName: str
    targetAccount: str
    websiteUri: str

@typing.type_check_only
class ListLfpStoresResponse(typing_extensions.TypedDict, total=False):
    lfpStores: _list[LfpStore]
    nextPageToken: str

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
