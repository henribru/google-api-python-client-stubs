import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountType: typing_extensions.Literal[
        "ACCOUNT_TYPE_UNSPECIFIED",
        "CSS_GROUP",
        "CSS_DOMAIN",
        "MC_PRIMARY_CSS_MCA",
        "MC_CSS_MCA",
        "MC_MARKETPLACE_MCA",
        "MC_OTHER_MCA",
        "MC_STANDALONE",
        "MC_MCA_SUBACCOUNT",
    ]
    automaticLabelIds: _list[str]
    displayName: str
    fullName: str
    homepageUri: str
    labelIds: _list[str]
    name: str
    parent: str

@typing.type_check_only
class AccountLabel(typing_extensions.TypedDict, total=False):
    accountId: str
    description: str
    displayName: str
    labelId: str
    labelType: typing_extensions.Literal[
        "LABEL_TYPE_UNSPECIFIED", "MANUAL", "AUTOMATIC"
    ]
    name: str

@typing.type_check_only
class Attributes(typing_extensions.TypedDict, total=False):
    additionalImageLinks: _list[str]
    adult: bool
    ageGroup: str
    brand: str
    certifications: _list[Certification]
    color: str
    cppAdsRedirect: str
    cppLink: str
    cppMobileLink: str
    customLabel0: str
    customLabel1: str
    customLabel2: str
    customLabel3: str
    customLabel4: str
    description: str
    excludedDestinations: _list[str]
    expirationDate: str
    gender: str
    googleProductCategory: str
    gtin: str
    headlineOfferCondition: str
    headlineOfferInstallment: HeadlineOfferInstallment
    headlineOfferLink: str
    headlineOfferMobileLink: str
    headlineOfferPrice: Price
    headlineOfferShippingPrice: Price
    headlineOfferSubscriptionCost: HeadlineOfferSubscriptionCost
    highPrice: Price
    imageLink: str
    includedDestinations: _list[str]
    isBundle: bool
    itemGroupId: str
    lowPrice: Price
    material: str
    mpn: str
    multipack: str
    numberOfOffers: str
    pattern: str
    pause: str
    productDetails: _list[ProductDetail]
    productHeight: ProductDimension
    productHighlights: _list[str]
    productLength: ProductDimension
    productTypes: _list[str]
    productWeight: ProductWeight
    productWidth: ProductDimension
    size: str
    sizeSystem: str
    sizeTypes: _list[str]
    title: str

@typing.type_check_only
class Certification(typing_extensions.TypedDict, total=False):
    authority: str
    code: str
    name: str

@typing.type_check_only
class CssProduct(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    cssProductStatus: CssProductStatus
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    name: str
    rawProvidedId: str

@typing.type_check_only
class CssProductInput(typing_extensions.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    finalName: str
    freshnessTime: str
    name: str
    rawProvidedId: str

@typing.type_check_only
class CssProductStatus(typing_extensions.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[DestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ItemLevelIssue]
    lastUpdateDate: str

@typing.type_check_only
class CustomAttribute(typing_extensions.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class DestinationStatus(typing_extensions.TypedDict, total=False):
    approvedCountries: _list[str]
    destination: str
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class HeadlineOfferInstallment(typing_extensions.TypedDict, total=False):
    amount: Price
    downpayment: Price
    months: str

@typing.type_check_only
class HeadlineOfferSubscriptionCost(typing_extensions.TypedDict, total=False):
    amount: Price
    period: typing_extensions.Literal[
        "SUBSCRIPTION_PERIOD_UNSPECIFIED", "MONTH", "YEAR"
    ]
    periodLength: str

@typing.type_check_only
class ItemLevelIssue(typing_extensions.TypedDict, total=False):
    applicableCountries: _list[str]
    attribute: str
    code: str
    description: str
    destination: str
    detail: str
    documentation: str
    resolution: str
    servability: str

@typing.type_check_only
class ListAccountLabelsResponse(typing_extensions.TypedDict, total=False):
    accountLabels: _list[AccountLabel]
    nextPageToken: str

@typing.type_check_only
class ListChildAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListCssProductsResponse(typing_extensions.TypedDict, total=False):
    cssProducts: _list[CssProduct]
    nextPageToken: str

@typing.type_check_only
class Price(typing_extensions.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class ProductDetail(typing_extensions.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductDimension(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductWeight(typing_extensions.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class UpdateAccountLabelsRequest(typing_extensions.TypedDict, total=False):
    labelIds: _list[str]
    parent: str
