import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccountLimit(typing_extensions.TypedDict, total=False):
    name: str
    products: ProductLimit

@typing.type_check_only
class ListAccountLimitsResponse(typing_extensions.TypedDict, total=False):
    accountLimits: _list[AccountLimit]
    nextPageToken: str

@typing.type_check_only
class ListQuotaGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    quotaGroups: _list[QuotaGroup]

@typing.type_check_only
class MethodDetails(typing_extensions.TypedDict, total=False):
    method: str
    path: str
    subapi: str
    version: str

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
        "YOUTUBE_AFFILIATE",
        "YOUTUBE_SHOPPING",
        "CLOUD_RETAIL",
        "LOCAL_CLOUD_RETAIL",
        "PRODUCT_REVIEWS",
        "MERCHANT_REVIEWS",
        "YOUTUBE_CHECKOUT",
    ]

@typing.type_check_only
class ProductLimit(typing_extensions.TypedDict, total=False):
    limit: str
    scope: typing_extensions.Literal["SCOPE_UNSPECIFIED", "ADS_NON_EEA", "ADS_EEA"]

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
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class QuotaGroup(typing_extensions.TypedDict, total=False):
    methodDetails: _list[MethodDetails]
    name: str
    quotaLimit: str
    quotaMinuteLimit: str
    quotaUsage: str
