import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    accountType: typing.Literal[
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
class AccountLabel(typing.TypedDict, total=False):
    accountId: str
    description: str
    displayName: str
    labelId: str
    labelType: typing.Literal["LABEL_TYPE_UNSPECIFIED", "MANUAL", "AUTOMATIC"]
    name: str

@typing.type_check_only
class Attributes(typing.TypedDict, total=False):
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
    maxRating: str
    minRating: str
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
    rating: float
    reviewCount: str
    size: str
    sizeSystem: str
    sizeTypes: _list[str]
    title: str

@typing.type_check_only
class Certification(typing.TypedDict, total=False):
    authority: str
    code: str
    name: str

@typing.type_check_only
class CssProduct(typing.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    cssProductStatus: CssProductStatus
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    name: str
    rawProvidedId: str

@typing.type_check_only
class CssProductInput(typing.TypedDict, total=False):
    attributes: Attributes
    contentLanguage: str
    customAttributes: _list[CustomAttribute]
    feedLabel: str
    finalName: str
    freshnessTime: str
    name: str
    rawProvidedId: str

@typing.type_check_only
class CssProductStatus(typing.TypedDict, total=False):
    creationDate: str
    destinationStatuses: _list[DestinationStatus]
    googleExpirationDate: str
    itemLevelIssues: _list[ItemLevelIssue]
    lastUpdateDate: str

@typing.type_check_only
class CustomAttribute(typing.TypedDict, total=False):
    groupValues: _list[CustomAttribute]
    name: str
    value: str

@typing.type_check_only
class DestinationStatus(typing.TypedDict, total=False):
    approvedCountries: _list[str]
    destination: str
    disapprovedCountries: _list[str]
    pendingCountries: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HeadlineOfferInstallment(typing.TypedDict, total=False):
    amount: Price
    downpayment: Price
    months: str

@typing.type_check_only
class HeadlineOfferSubscriptionCost(typing.TypedDict, total=False):
    amount: Price
    period: typing.Literal["SUBSCRIPTION_PERIOD_UNSPECIFIED", "MONTH", "YEAR"]
    periodLength: str

@typing.type_check_only
class ItemLevelIssue(typing.TypedDict, total=False):
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
class ListAccountLabelsResponse(typing.TypedDict, total=False):
    accountLabels: _list[AccountLabel]
    nextPageToken: str

@typing.type_check_only
class ListChildAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListCssProductsResponse(typing.TypedDict, total=False):
    cssProducts: _list[CssProduct]
    nextPageToken: str

@typing.type_check_only
class ListQuotaGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    quotaGroups: _list[QuotaGroup]

@typing.type_check_only
class MethodDetails(typing.TypedDict, total=False):
    method: str
    path: str
    subapi: str
    version: str

@typing.type_check_only
class Price(typing.TypedDict, total=False):
    amountMicros: str
    currencyCode: str

@typing.type_check_only
class ProductDetail(typing.TypedDict, total=False):
    attributeName: str
    attributeValue: str
    sectionName: str

@typing.type_check_only
class ProductDimension(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class ProductWeight(typing.TypedDict, total=False):
    unit: str
    value: float

@typing.type_check_only
class QuotaGroup(typing.TypedDict, total=False):
    methodDetails: _list[MethodDetails]
    name: str
    quotaLimit: str
    quotaMinuteLimit: str
    quotaUsage: str

@typing.type_check_only
class UpdateAccountLabelsRequest(typing.TypedDict, total=False):
    labelIds: _list[str]
    parent: str
