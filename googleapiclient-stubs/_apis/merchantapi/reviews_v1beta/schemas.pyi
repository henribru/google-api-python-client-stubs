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
class ListMerchantReviewsResponse(typing_extensions.TypedDict, total=False):
    merchantReviews: _list[MerchantReview]
    nextPageToken: str

@typing.type_check_only
class ListProductReviewsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    productReviews: _list[ProductReview]

@typing.type_check_only
class MerchantReview(typing_extensions.TypedDict, total=False):
    attributes: MerchantReviewAttributes
    customAttributes: _list[CustomAttribute]
    dataSource: str
    merchantReviewId: str
    merchantReviewStatus: MerchantReviewStatus
    name: str

@typing.type_check_only
class MerchantReviewAttributes(typing_extensions.TypedDict, total=False):
    collectionMethod: typing_extensions.Literal[
        "COLLECTION_METHOD_UNSPECIFIED",
        "MERCHANT_UNSOLICITED",
        "POINT_OF_SALE",
        "AFTER_FULFILLMENT",
    ]
    content: str
    isAnonymous: bool
    maxRating: str
    merchantDisplayName: str
    merchantId: str
    merchantLink: str
    merchantRatingLink: str
    minRating: str
    rating: float
    reviewCountry: str
    reviewLanguage: str
    reviewTime: str
    reviewerId: str
    reviewerUsername: str
    title: str

@typing.type_check_only
class MerchantReviewDestinationStatus(typing_extensions.TypedDict, total=False):
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
class MerchantReviewItemLevelIssue(typing_extensions.TypedDict, total=False):
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
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DISAPPROVED"
    ]

@typing.type_check_only
class MerchantReviewStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    destinationStatuses: _list[MerchantReviewDestinationStatus]
    itemLevelIssues: _list[MerchantReviewItemLevelIssue]
    lastUpdateTime: str

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
class ProductReview(typing_extensions.TypedDict, total=False):
    attributes: ProductReviewAttributes
    customAttributes: _list[CustomAttribute]
    dataSource: str
    name: str
    productReviewId: str
    productReviewStatus: ProductReviewStatus

@typing.type_check_only
class ProductReviewAttributes(typing_extensions.TypedDict, total=False):
    aggregatorName: str
    asins: _list[str]
    brands: _list[str]
    collectionMethod: typing_extensions.Literal[
        "COLLECTION_METHOD_UNSPECIFIED", "UNSOLICITED", "POST_FULFILLMENT"
    ]
    cons: _list[str]
    content: str
    gtins: _list[str]
    isSpam: bool
    maxRating: str
    minRating: str
    mpns: _list[str]
    productLinks: _list[str]
    productNames: _list[str]
    pros: _list[str]
    publisherFavicon: str
    publisherName: str
    rating: float
    reviewCountry: str
    reviewLanguage: str
    reviewLink: ReviewLink
    reviewTime: str
    reviewerId: str
    reviewerImageLinks: _list[str]
    reviewerIsAnonymous: bool
    reviewerUsername: str
    skus: _list[str]
    subclientName: str
    title: str
    transactionId: str

@typing.type_check_only
class ProductReviewDestinationStatus(typing_extensions.TypedDict, total=False):
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
class ProductReviewItemLevelIssue(typing_extensions.TypedDict, total=False):
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
        "SEVERITY_UNSPECIFIED", "NOT_IMPACTED", "DISAPPROVED"
    ]

@typing.type_check_only
class ProductReviewStatus(typing_extensions.TypedDict, total=False):
    createTime: str
    destinationStatuses: _list[ProductReviewDestinationStatus]
    itemLevelIssues: _list[ProductReviewItemLevelIssue]
    lastUpdateTime: str

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
class ReviewLink(typing_extensions.TypedDict, total=False):
    link: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SINGLETON", "GROUP"]
