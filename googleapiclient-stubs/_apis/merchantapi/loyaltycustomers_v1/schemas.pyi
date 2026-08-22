import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddressInfo(typing_extensions.TypedDict, total=False):
    city: str
    familyName: str
    givenName: str
    postalCode: str
    regionCode: str
    state: str

@typing.type_check_only
class LoyaltyCustomer(typing_extensions.TypedDict, total=False):
    loyaltyTier: typing_extensions.Literal[
        "LOYALTY_TIER_UNSPECIFIED",
        "TIER1",
        "TIER2",
        "TIER3",
        "TIER4",
        "TIER5",
        "TIER6",
        "TIER7",
        "NON_MEMBER",
    ]
    pointBalance: str
    userIdentifier: UserIdentifier

@typing.type_check_only
class ManageLoyaltyCustomerMatchRequest(typing_extensions.TypedDict, total=False):
    loyaltyCustomer: LoyaltyCustomer

@typing.type_check_only
class ManageLoyaltyCustomerMatchResponse(typing_extensions.TypedDict, total=False):
    loyaltyCustomer: LoyaltyCustomer

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
class ProductStatusChangeMessage(typing_extensions.TypedDict, total=False):
    account: str
    attribute: typing_extensions.Literal["ATTRIBUTE_UNSPECIFIED", "STATUS"]
    changes: _list[ProductChange]
    eventTime: str
    expirationTime: str
    managingAccount: str
    resource: str
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_UNSPECIFIED", "PRODUCT", "ACCOUNT_SERVICE"
    ]

@typing.type_check_only
class UserIdentifier(typing_extensions.TypedDict, total=False):
    address: AddressInfo
    emailAddress: str
    phoneNumber: str
