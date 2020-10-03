import typing

import typing_extensions

class Attributes(typing_extensions.TypedDict, total=False):
    brand: str
    size: str
    ageGroup: str
    scent: str
    sizeSystem: str
    gender: str
    sizeType: str
    material: str
    imageLink: Image
    title: str
    capacity: Capacity
    itemGroupId: str
    videoLink: typing.List[str]
    count: Count
    flavor: str
    excludedDestination: typing.List[str]
    additionalImageLink: typing.List[Image]
    disclosureDate: str
    productType: typing.List[str]
    targetClientId: str
    pattern: str
    productDetail: typing.List[ProductDetail]
    releaseDate: str
    productLine: str
    productPageUrl: str
    gtin: typing.List[str]
    theme: str
    productName: str
    includedDestination: typing.List[str]
    color: str
    suggestedRetailPrice: Price
    description: str
    featureDescription: typing.List[FeatureDescription]
    richProductContent: typing.List[str]
    format: str
    mpn: str

class Product(typing_extensions.TypedDict, total=False):
    productId: str
    contentLanguage: str
    name: str
    attributes: Attributes
    targetCountry: str
    parent: str
    issues: typing.List[Issue]
    destinationStatuses: typing.List[DestinationStatus]

class Count(typing_extensions.TypedDict, total=False):
    value: str
    unit: str

class Capacity(typing_extensions.TypedDict, total=False):
    unit: str
    value: str

class Price(typing_extensions.TypedDict, total=False):
    amount: str
    currency: str

class FeatureDescription(typing_extensions.TypedDict, total=False):
    text: str
    image: Image
    headline: str

class Image(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "PENDING_PROCESSING",
        "PENDING_CRAWL",
        "OK",
        "ROBOTED",
        "XROBOTED",
        "CRAWL_ERROR",
        "PROCESSING_ERROR",
        "DECODING_ERROR",
        "TOO_BIG",
        "CRAWL_SKIPPED",
        "HOSTLOADED",
        "HTTP_404",
    ]
    imageUrl: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "CRAWLED", "UPLOADED"]

class Issue(typing_extensions.TypedDict, total=False):
    timestamp: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]
    description: str
    resolution: typing_extensions.Literal[
        "RESOLUTION_UNSPECIFIED", "USER_ACTION", "PENDING_PROCESSING"
    ]
    attribute: str
    title: str
    type: str
    destination: str

class Empty(typing_extensions.TypedDict, total=False): ...

class DestinationStatus(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal["UNKNOWN", "ACTIVE", "PENDING", "DISAPPROVED"]
    destination: str

class ProductDetail(typing_extensions.TypedDict, total=False):
    sectionName: str
    attributeValue: str
    attributeName: str

class ListProductsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    products: typing.List[Product]
