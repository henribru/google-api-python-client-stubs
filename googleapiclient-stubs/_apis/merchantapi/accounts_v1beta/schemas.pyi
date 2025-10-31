import typing

import typing_extensions

_list = list

@typing.type_check_only
class About(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class AcceptTermsOfServiceResponse(typing_extensions.TypedDict, total=False):
    termsOfServiceAgreementState: TermsOfServiceAgreementState

@typing.type_check_only
class Accepted(typing_extensions.TypedDict, total=False):
    acceptedBy: str
    termsOfService: str
    validUntil: Date

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    accountId: str
    accountName: str
    adultContent: bool
    languageCode: str
    name: str
    testAccount: bool
    timeZone: TimeZone

@typing.type_check_only
class AccountAggregation(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AccountIssue(typing_extensions.TypedDict, total=False):
    detail: str
    documentationUri: str
    impactedDestinations: _list[ImpactedDestination]
    name: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "SUGGESTION"
    ]
    title: str

@typing.type_check_only
class AccountManagement(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AccountRelationship(typing_extensions.TypedDict, total=False):
    accountIdAlias: str
    name: str
    provider: str
    providerDisplayName: str

@typing.type_check_only
class AccountService(typing_extensions.TypedDict, total=False):
    accountAggregation: AccountAggregation
    accountManagement: AccountManagement
    campaignsManagement: CampaignsManagement
    externalAccountId: str
    handshake: Handshake
    localListingManagement: LocalListingManagement
    mutability: typing_extensions.Literal[
        "MUTABILITY_UNSPECIFIED", "MUTABLE", "IMMUTABLE"
    ]
    name: str
    productsManagement: ProductsManagement
    provider: str
    providerDisplayName: str

@typing.type_check_only
class AddAccountService(typing_extensions.TypedDict, total=False):
    accountAggregation: AccountAggregation
    provider: str

@typing.type_check_only
class AddUser(typing_extensions.TypedDict, total=False):
    user: User
    userId: str

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    administrativeArea: str
    city: str
    postalCode: str
    regionCode: str
    streetAddress: str

@typing.type_check_only
class ApproveAccountServiceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AutofeedSettings(typing_extensions.TypedDict, total=False):
    eligible: bool
    enableProducts: bool
    name: str

@typing.type_check_only
class AutomaticImageImprovements(typing_extensions.TypedDict, total=False):
    accountImageImprovementsSettings: ImageImprovementsAccountLevelSettings
    effectiveAllowAutomaticImageImprovements: bool

@typing.type_check_only
class AutomaticImprovements(typing_extensions.TypedDict, total=False):
    imageImprovements: AutomaticImageImprovements
    itemUpdates: AutomaticItemUpdates
    name: str
    shippingImprovements: AutomaticShippingImprovements

@typing.type_check_only
class AutomaticItemUpdates(typing_extensions.TypedDict, total=False):
    accountItemUpdatesSettings: ItemUpdatesAccountLevelSettings
    effectiveAllowAvailabilityUpdates: bool
    effectiveAllowConditionUpdates: bool
    effectiveAllowPriceUpdates: bool
    effectiveAllowStrictAvailabilityUpdates: bool

@typing.type_check_only
class AutomaticShippingImprovements(typing_extensions.TypedDict, total=False):
    allowShippingImprovements: bool

@typing.type_check_only
class BusinessDayConfig(typing_extensions.TypedDict, total=False):
    businessDays: _list[
        typing_extensions.Literal[
            "WEEKDAY_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]

@typing.type_check_only
class BusinessIdentity(typing_extensions.TypedDict, total=False):
    blackOwned: IdentityAttribute
    latinoOwned: IdentityAttribute
    name: str
    promotionsConsent: typing_extensions.Literal[
        "PROMOTIONS_CONSENT_UNSPECIFIED",
        "PROMOTIONS_CONSENT_GIVEN",
        "PROMOTIONS_CONSENT_DENIED",
    ]
    smallBusiness: IdentityAttribute
    veteranOwned: IdentityAttribute
    womenOwned: IdentityAttribute

@typing.type_check_only
class BusinessInfo(typing_extensions.TypedDict, total=False):
    address: PostalAddress
    customerService: CustomerService
    koreanBusinessRegistrationNumber: str
    name: str
    phone: PhoneNumber
    phoneVerificationState: typing_extensions.Literal[
        "PHONE_VERIFICATION_STATE_UNSPECIFIED",
        "PHONE_VERIFICATION_STATE_VERIFIED",
        "PHONE_VERIFICATION_STATE_UNVERIFIED",
    ]

@typing.type_check_only
class CampaignsManagement(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CarrierRate(typing_extensions.TypedDict, total=False):
    carrier: str
    carrierService: str
    flatAdjustment: Price
    name: str
    originPostalCode: str
    percentageAdjustment: str

@typing.type_check_only
class CheckoutSettings(typing_extensions.TypedDict, total=False):
    effectiveEnrollmentState: typing_extensions.Literal[
        "CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED", "INACTIVE", "ENROLLED", "OPTED_OUT"
    ]
    effectiveReviewState: typing_extensions.Literal[
        "CHECKOUT_REVIEW_STATE_UNSPECIFIED", "IN_REVIEW", "APPROVED", "DISAPPROVED"
    ]
    effectiveUriSettings: UriSettings
    eligibleDestinations: _list[
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
    enrollmentState: typing_extensions.Literal[
        "CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED", "INACTIVE", "ENROLLED", "OPTED_OUT"
    ]
    name: str
    reviewState: typing_extensions.Literal[
        "CHECKOUT_REVIEW_STATE_UNSPECIFIED", "IN_REVIEW", "APPROVED", "DISAPPROVED"
    ]
    uriSettings: UriSettings

@typing.type_check_only
class ClaimHomepageRequest(typing_extensions.TypedDict, total=False):
    overwrite: bool

@typing.type_check_only
class CreateAndConfigureAccountRequest(typing_extensions.TypedDict, total=False):
    account: Account
    service: _list[AddAccountService]
    user: _list[AddUser]
    users: _list[CreateUserRequest]

@typing.type_check_only
class CreateUserRequest(typing_extensions.TypedDict, total=False):
    parent: str
    user: User
    userId: str

@typing.type_check_only
class CustomerService(typing_extensions.TypedDict, total=False):
    email: str
    phone: PhoneNumber
    uri: str

@typing.type_check_only
class CutoffConfig(typing_extensions.TypedDict, total=False):
    localCutoffTime: LocalCutoffTime
    noDeliveryPostCutoff: bool
    storeCloseOffsetHours: str

@typing.type_check_only
class CutoffTime(typing_extensions.TypedDict, total=False):
    hour: int
    minute: int
    timeZone: str

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeliveryTime(typing_extensions.TypedDict, total=False):
    cutoffTime: CutoffTime
    handlingBusinessDayConfig: BusinessDayConfig
    maxHandlingDays: int
    maxTransitDays: int
    minHandlingDays: int
    minTransitDays: int
    transitBusinessDayConfig: BusinessDayConfig
    transitTimeTable: TransitTable
    warehouseBasedDeliveryTimes: _list[WarehouseBasedDeliveryTime]

@typing.type_check_only
class DeveloperRegistration(typing_extensions.TypedDict, total=False):
    gcpIds: _list[str]
    name: str

@typing.type_check_only
class DisableProgramRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Distance(typing_extensions.TypedDict, total=False):
    unit: typing_extensions.Literal["UNIT_UNSPECIFIED", "MILES", "KILOMETERS"]
    value: str

@typing.type_check_only
class EmailPreferences(typing_extensions.TypedDict, total=False):
    name: str
    newsAndTips: typing_extensions.Literal[
        "OPT_IN_STATE_UNSPECIFIED", "OPTED_OUT", "OPTED_IN", "UNCONFIRMED"
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableProgramRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FindLfpProvidersResponse(typing_extensions.TypedDict, total=False):
    lfpProviders: _list[LfpProvider]
    nextPageToken: str

@typing.type_check_only
class GbpAccount(typing_extensions.TypedDict, total=False):
    gbpAccountId: str
    gbpAccountName: str
    listingCount: str
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "USER", "BUSINESS_ACCOUNT"]

@typing.type_check_only
class GeoTargetArea(typing_extensions.TypedDict, total=False):
    geotargetCriteriaIds: _list[str]

@typing.type_check_only
class GetAccountForGcpRegistrationResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Handshake(typing_extensions.TypedDict, total=False):
    actor: typing_extensions.Literal["ACTOR_UNSPECIFIED", "ACCOUNT", "OTHER_PARTY"]
    approvalState: typing_extensions.Literal[
        "APPROVAL_STATE_UNSPECIFIED", "PENDING", "ESTABLISHED", "REJECTED"
    ]

@typing.type_check_only
class Headers(typing_extensions.TypedDict, total=False):
    locations: _list[LocationIdSet]
    numberOfItems: _list[str]
    postalCodeGroupNames: _list[str]
    prices: _list[Price]
    weights: _list[Weight]

@typing.type_check_only
class Homepage(typing_extensions.TypedDict, total=False):
    claimed: bool
    name: str
    uri: str

@typing.type_check_only
class IdentityAttribute(typing_extensions.TypedDict, total=False):
    identityDeclaration: typing_extensions.Literal[
        "IDENTITY_DECLARATION_UNSPECIFIED",
        "SELF_IDENTIFIES_AS",
        "DOES_NOT_SELF_IDENTIFY_AS",
    ]

@typing.type_check_only
class ImageImprovementsAccountLevelSettings(typing_extensions.TypedDict, total=False):
    allowAutomaticImageImprovements: bool

@typing.type_check_only
class Impact(typing_extensions.TypedDict, total=False):
    regionCode: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "SUGGESTION"
    ]

@typing.type_check_only
class ImpactedDestination(typing_extensions.TypedDict, total=False):
    impacts: _list[Impact]
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
class InStock(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class InventoryVerification(typing_extensions.TypedDict, total=False):
    contact: str
    contactEmail: str
    contactState: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ACTION_REQUIRED",
        "INACTIVE",
        "RUNNING",
        "SUCCEEDED",
        "SUSPENDED",
    ]

@typing.type_check_only
class ItemUpdatesAccountLevelSettings(typing_extensions.TypedDict, total=False):
    allowAvailabilityUpdates: bool
    allowConditionUpdates: bool
    allowPriceUpdates: bool
    allowStrictAvailabilityUpdates: bool

@typing.type_check_only
class LfpLink(typing_extensions.TypedDict, total=False):
    externalAccountId: str
    lfpProvider: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]

@typing.type_check_only
class LfpProvider(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    regionCode: str

@typing.type_check_only
class LinkGbpAccountRequest(typing_extensions.TypedDict, total=False):
    gbpEmail: str

@typing.type_check_only
class LinkGbpAccountResponse(typing_extensions.TypedDict, total=False):
    response: Empty

@typing.type_check_only
class LinkLfpProviderRequest(typing_extensions.TypedDict, total=False):
    externalAccountId: str

@typing.type_check_only
class LinkLfpProviderResponse(typing_extensions.TypedDict, total=False):
    response: Empty

@typing.type_check_only
class ListAccountIssuesResponse(typing_extensions.TypedDict, total=False):
    accountIssues: _list[AccountIssue]
    nextPageToken: str

@typing.type_check_only
class ListAccountRelationshipsResponse(typing_extensions.TypedDict, total=False):
    accountRelationships: _list[AccountRelationship]
    nextPageToken: str

@typing.type_check_only
class ListAccountServicesResponse(typing_extensions.TypedDict, total=False):
    accountServices: _list[AccountService]
    nextPageToken: str

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListGbpAccountsResponse(typing_extensions.TypedDict, total=False):
    gbpAccounts: _list[GbpAccount]
    nextPageToken: str

@typing.type_check_only
class ListOmnichannelSettingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    omnichannelSettings: _list[OmnichannelSetting]

@typing.type_check_only
class ListOnlineReturnPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    onlineReturnPolicies: _list[OnlineReturnPolicy]

@typing.type_check_only
class ListProgramsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    programs: _list[Program]

@typing.type_check_only
class ListRegionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    regions: _list[Region]

@typing.type_check_only
class ListSubAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListUsersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class LocalCutoffTime(typing_extensions.TypedDict, total=False):
    hour: str
    minute: str

@typing.type_check_only
class LocalListingManagement(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LocationIdSet(typing_extensions.TypedDict, total=False):
    locationIds: _list[str]

@typing.type_check_only
class LoyaltyProgram(typing_extensions.TypedDict, total=False):
    loyaltyProgramTiers: _list[LoyaltyProgramTiers]
    programLabel: str

@typing.type_check_only
class LoyaltyProgramTiers(typing_extensions.TypedDict, total=False):
    tierLabel: str

@typing.type_check_only
class MinimumOrderValueTable(typing_extensions.TypedDict, total=False):
    storeCodeSetWithMovs: _list[StoreCodeSetWithMov]

@typing.type_check_only
class OmnichannelSetting(typing_extensions.TypedDict, total=False):
    about: About
    inStock: InStock
    inventoryVerification: InventoryVerification
    lfpLink: LfpLink
    lsfType: typing_extensions.Literal[
        "LSF_TYPE_UNSPECIFIED", "GHLSF", "MHLSF_BASIC", "MHLSF_FULL"
    ]
    name: str
    odo: OnDisplayToOrder
    pickup: Pickup
    regionCode: str

@typing.type_check_only
class OnDisplayToOrder(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class OnlineReturnPolicy(typing_extensions.TypedDict, total=False):
    acceptDefectiveOnly: bool
    acceptExchange: bool
    countries: _list[str]
    itemConditions: _list[
        typing_extensions.Literal["ITEM_CONDITION_UNSPECIFIED", "NEW", "USED"]
    ]
    label: str
    name: str
    policy: Policy
    processRefundDays: int
    restockingFee: RestockingFee
    returnLabelSource: typing_extensions.Literal[
        "RETURN_LABEL_SOURCE_UNSPECIFIED",
        "DOWNLOAD_AND_PRINT",
        "IN_THE_PACKAGE",
        "CUSTOMER_RESPONSIBILITY",
    ]
    returnMethods: _list[
        typing_extensions.Literal[
            "RETURN_METHOD_UNSPECIFIED", "BY_MAIL", "IN_STORE", "AT_A_KIOSK"
        ]
    ]
    returnPolicyId: str
    returnPolicyUri: str
    returnShippingFee: ReturnShippingFee
    seasonalOverrides: _list[SeasonalOverride]

@typing.type_check_only
class PhoneNumber(typing_extensions.TypedDict, total=False):
    e164Number: str
    extension: str
    shortCode: ShortCode

@typing.type_check_only
class Pickup(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    days: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "NUMBER_OF_DAYS_AFTER_DELIVERY",
        "NO_RETURNS",
        "LIFETIME_RETURNS",
    ]

@typing.type_check_only
class PostalAddress(typing_extensions.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class PostalCodeArea(typing_extensions.TypedDict, total=False):
    postalCodes: _list[PostalCodeRange]
    regionCode: str

@typing.type_check_only
class PostalCodeRange(typing_extensions.TypedDict, total=False):
    begin: str
    end: str

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
    resourceType: typing_extensions.Literal["RESOURCE_UNSPECIFIED", "PRODUCT"]

@typing.type_check_only
class ProductsManagement(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Program(typing_extensions.TypedDict, total=False):
    activeRegionCodes: _list[str]
    documentationUri: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NOT_ELIGIBLE", "ELIGIBLE", "ENABLED"
    ]
    unmetRequirements: _list[Requirement]

@typing.type_check_only
class ProposeAccountServiceRequest(typing_extensions.TypedDict, total=False):
    accountService: AccountService
    provider: str

@typing.type_check_only
class RateGroup(typing_extensions.TypedDict, total=False):
    applicableShippingLabels: _list[str]
    carrierRates: _list[CarrierRate]
    mainTable: Table
    name: str
    singleValue: Value
    subtables: _list[Table]

@typing.type_check_only
class Region(typing_extensions.TypedDict, total=False):
    displayName: str
    geotargetArea: GeoTargetArea
    name: str
    postalCodeArea: PostalCodeArea
    regionalInventoryEligible: bool
    shippingEligible: bool

@typing.type_check_only
class RegisterGcpRequest(typing_extensions.TypedDict, total=False):
    developerEmail: str

@typing.type_check_only
class RejectAccountServiceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RequestInventoryVerificationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RequestInventoryVerificationResponse(typing_extensions.TypedDict, total=False):
    omnichannelSetting: OmnichannelSetting

@typing.type_check_only
class Required(typing_extensions.TypedDict, total=False):
    termsOfService: str
    tosFileUri: str

@typing.type_check_only
class Requirement(typing_extensions.TypedDict, total=False):
    affectedRegionCodes: _list[str]
    documentationUri: str
    title: str

@typing.type_check_only
class RestockingFee(typing_extensions.TypedDict, total=False):
    fixedFee: Price
    microPercent: int

@typing.type_check_only
class ReturnShippingFee(typing_extensions.TypedDict, total=False):
    fixedFee: Price
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "FIXED", "CUSTOMER_PAYING_ACTUAL_FEE"
    ]

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    cells: _list[Value]

@typing.type_check_only
class SeasonalOverride(typing_extensions.TypedDict, total=False):
    endDate: Date
    label: str
    returnDays: int
    returnUntilDate: Date
    startDate: Date

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    active: bool
    currencyCode: str
    deliveryCountries: _list[str]
    deliveryTime: DeliveryTime
    loyaltyPrograms: _list[LoyaltyProgram]
    minimumOrderValue: Price
    minimumOrderValueTable: MinimumOrderValueTable
    rateGroups: _list[RateGroup]
    serviceName: str
    shipmentType: typing_extensions.Literal[
        "SHIPMENT_TYPE_UNSPECIFIED", "DELIVERY", "LOCAL_DELIVERY", "COLLECTION_POINT"
    ]
    storeConfig: StoreConfig

@typing.type_check_only
class ShippingSettings(typing_extensions.TypedDict, total=False):
    etag: str
    name: str
    services: _list[Service]
    warehouses: _list[Warehouse]

@typing.type_check_only
class ShortCode(typing_extensions.TypedDict, total=False):
    number: str
    regionCode: str

@typing.type_check_only
class StoreCodeSetWithMov(typing_extensions.TypedDict, total=False):
    storeCodes: _list[str]
    value: Price

@typing.type_check_only
class StoreConfig(typing_extensions.TypedDict, total=False):
    cutoffConfig: CutoffConfig
    serviceRadius: Distance
    storeCodes: _list[str]
    storeServiceType: typing_extensions.Literal[
        "STORE_SERVICE_TYPE_UNSPECIFIED", "ALL_STORES", "SELECTED_STORES"
    ]

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: _list[Row]

@typing.type_check_only
class TermsOfService(typing_extensions.TypedDict, total=False):
    external: bool
    fileUri: str
    kind: typing_extensions.Literal[
        "TERMS_OF_SERVICE_KIND_UNSPECIFIED", "MERCHANT_CENTER"
    ]
    name: str
    regionCode: str

@typing.type_check_only
class TermsOfServiceAgreementState(typing_extensions.TypedDict, total=False):
    accepted: Accepted
    name: str
    regionCode: str
    required: Required
    termsOfServiceKind: typing_extensions.Literal[
        "TERMS_OF_SERVICE_KIND_UNSPECIFIED", "MERCHANT_CENTER"
    ]

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TransitTable(typing_extensions.TypedDict, total=False):
    postalCodeGroupNames: _list[str]
    rows: _list[TransitTimeRow]
    transitTimeLabels: _list[str]

@typing.type_check_only
class TransitTimeRow(typing_extensions.TypedDict, total=False):
    values: _list[TransitTimeValue]

@typing.type_check_only
class TransitTimeValue(typing_extensions.TypedDict, total=False):
    maxTransitDays: int
    minTransitDays: int

@typing.type_check_only
class UnclaimHomepageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UnregisterGcpRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UriSettings(typing_extensions.TypedDict, total=False):
    cartUriTemplate: str
    checkoutUriTemplate: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    accessRights: _list[
        typing_extensions.Literal[
            "ACCESS_RIGHT_UNSPECIFIED",
            "STANDARD",
            "READ_ONLY",
            "ADMIN",
            "PERFORMANCE_REPORTING",
            "API_DEVELOPER",
        ]
    ]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "PENDING", "VERIFIED"]

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    carrierRate: str
    flatRate: Price
    noShipping: bool
    pricePercentage: str
    subtable: str

@typing.type_check_only
class Warehouse(typing_extensions.TypedDict, total=False):
    businessDayConfig: BusinessDayConfig
    cutoffTime: WarehouseCutoffTime
    handlingDays: str
    name: str
    shippingAddress: Address

@typing.type_check_only
class WarehouseBasedDeliveryTime(typing_extensions.TypedDict, total=False):
    carrier: str
    carrierService: str
    warehouse: str

@typing.type_check_only
class WarehouseCutoffTime(typing_extensions.TypedDict, total=False):
    hour: int
    minute: int

@typing.type_check_only
class Weight(typing_extensions.TypedDict, total=False):
    amountMicros: str
    unit: typing_extensions.Literal["WEIGHT_UNIT_UNSPECIFIED", "POUND", "KILOGRAM"]
