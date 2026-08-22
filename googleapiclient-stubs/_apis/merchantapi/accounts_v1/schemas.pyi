import typing

_list = list

@typing.type_check_only
class About(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class AcceptTermsOfServiceResponse(typing.TypedDict, total=False):
    termsOfServiceAgreementState: TermsOfServiceAgreementState

@typing.type_check_only
class Accepted(typing.TypedDict, total=False):
    acceptedBy: str
    termsOfService: str
    validUntil: Date

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    accountId: str
    accountName: str
    adultContent: bool
    languageCode: str
    name: str
    testAccount: bool
    timeZone: TimeZone

@typing.type_check_only
class AccountAggregation(typing.TypedDict, total=False): ...

@typing.type_check_only
class AccountIssue(typing.TypedDict, total=False):
    detail: str
    documentationUri: str
    impactedDestinations: _list[ImpactedDestination]
    name: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "SUGGESTION"]
    title: str

@typing.type_check_only
class AccountManagement(typing.TypedDict, total=False): ...

@typing.type_check_only
class AccountRelationship(typing.TypedDict, total=False):
    accountIdAlias: str
    name: str
    provider: str
    providerDisplayName: str

@typing.type_check_only
class AccountService(typing.TypedDict, total=False):
    accountAggregation: AccountAggregation
    accountManagement: AccountManagement
    campaignsManagement: CampaignsManagement
    comparisonShopping: ComparisonShopping
    externalAccountId: str
    handshake: Handshake
    localListingManagement: LocalListingManagement
    mutability: typing.Literal["MUTABILITY_UNSPECIFIED", "MUTABLE", "IMMUTABLE"]
    name: str
    productsManagement: ProductsManagement
    provider: str
    providerDisplayName: str

@typing.type_check_only
class AddAccountService(typing.TypedDict, total=False):
    accountAggregation: AccountAggregation
    accountManagement: AccountManagement
    campaignsManagement: CampaignsManagement
    comparisonShopping: ComparisonShopping
    externalAccountId: str
    productsManagement: ProductsManagement
    provider: str

@typing.type_check_only
class AddUser(typing.TypedDict, total=False):
    user: User
    userId: str
    verificationMailSettings: VerificationMailSettings

@typing.type_check_only
class Address(typing.TypedDict, total=False):
    administrativeArea: str
    city: str
    postalCode: str
    regionCode: str
    streetAddress: str

@typing.type_check_only
class ApproveAccountServiceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class AutofeedSettings(typing.TypedDict, total=False):
    eligible: bool
    enableProducts: bool
    name: str

@typing.type_check_only
class AutomaticImageImprovements(typing.TypedDict, total=False):
    accountImageImprovementsSettings: ImageImprovementsAccountLevelSettings
    effectiveAllowAutomaticImageImprovements: bool

@typing.type_check_only
class AutomaticImprovements(typing.TypedDict, total=False):
    imageImprovements: AutomaticImageImprovements
    itemUpdates: AutomaticItemUpdates
    name: str
    shippingImprovements: AutomaticShippingImprovements

@typing.type_check_only
class AutomaticItemUpdates(typing.TypedDict, total=False):
    accountItemUpdatesSettings: ItemUpdatesAccountLevelSettings
    effectiveAllowAvailabilityUpdates: bool
    effectiveAllowConditionUpdates: bool
    effectiveAllowPriceUpdates: bool
    effectiveAllowStrictAvailabilityUpdates: bool

@typing.type_check_only
class AutomaticShippingImprovements(typing.TypedDict, total=False):
    allowShippingImprovements: bool

@typing.type_check_only
class BatchCreateRegionsRequest(typing.TypedDict, total=False):
    requests: _list[CreateRegionRequest]

@typing.type_check_only
class BatchCreateRegionsResponse(typing.TypedDict, total=False):
    regions: _list[Region]

@typing.type_check_only
class BatchDeleteRegionsRequest(typing.TypedDict, total=False):
    requests: _list[DeleteRegionRequest]

@typing.type_check_only
class BatchUpdateRegionsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateRegionRequest]

@typing.type_check_only
class BatchUpdateRegionsResponse(typing.TypedDict, total=False):
    regions: _list[Region]

@typing.type_check_only
class BusinessDayConfig(typing.TypedDict, total=False):
    businessDays: _list[
        typing.Literal[
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
class BusinessIdentity(typing.TypedDict, total=False):
    blackOwned: IdentityAttribute
    latinoOwned: IdentityAttribute
    name: str
    promotionsConsent: typing.Literal[
        "PROMOTIONS_CONSENT_UNSPECIFIED",
        "PROMOTIONS_CONSENT_GIVEN",
        "PROMOTIONS_CONSENT_DENIED",
    ]
    smallBusiness: IdentityAttribute
    veteranOwned: IdentityAttribute
    womenOwned: IdentityAttribute

@typing.type_check_only
class BusinessInfo(typing.TypedDict, total=False):
    address: PostalAddress
    customerService: CustomerService
    koreanBusinessRegistrationNumber: str
    name: str
    phone: PhoneNumber
    phoneVerificationState: typing.Literal[
        "PHONE_VERIFICATION_STATE_UNSPECIFIED",
        "PHONE_VERIFICATION_STATE_VERIFIED",
        "PHONE_VERIFICATION_STATE_UNVERIFIED",
    ]

@typing.type_check_only
class CampaignsManagement(typing.TypedDict, total=False): ...

@typing.type_check_only
class CarrierRate(typing.TypedDict, total=False):
    carrier: str
    carrierService: str
    flatAdjustment: Price
    name: str
    originPostalCode: str
    percentageAdjustment: str

@typing.type_check_only
class CheckoutSettings(typing.TypedDict, total=False):
    effectiveEnrollmentState: typing.Literal[
        "CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED", "INACTIVE", "ENROLLED", "OPTED_OUT"
    ]
    effectiveReviewState: typing.Literal[
        "CHECKOUT_REVIEW_STATE_UNSPECIFIED", "IN_REVIEW", "APPROVED", "DISAPPROVED"
    ]
    effectiveUriSettings: UriSettings
    eligibleDestinations: _list[
        typing.Literal[
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
    enrollmentState: typing.Literal[
        "CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED", "INACTIVE", "ENROLLED", "OPTED_OUT"
    ]
    name: str
    reviewState: typing.Literal[
        "CHECKOUT_REVIEW_STATE_UNSPECIFIED", "IN_REVIEW", "APPROVED", "DISAPPROVED"
    ]
    uriSettings: UriSettings

@typing.type_check_only
class ClaimHomepageRequest(typing.TypedDict, total=False):
    overwrite: bool

@typing.type_check_only
class ComparisonShopping(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateAndConfigureAccountRequest(typing.TypedDict, total=False):
    account: Account
    service: _list[AddAccountService]
    setAlias: _list[SetAliasForRelationship]
    user: _list[AddUser]

@typing.type_check_only
class CreateRegionRequest(typing.TypedDict, total=False):
    parent: str
    region: Region
    regionId: str

@typing.type_check_only
class CustomerService(typing.TypedDict, total=False):
    email: str
    phone: PhoneNumber
    uri: str

@typing.type_check_only
class CutoffConfig(typing.TypedDict, total=False):
    localCutoffTime: LocalCutoffTime
    noDeliveryPostCutoff: bool
    storeCloseOffsetHours: str

@typing.type_check_only
class CutoffTime(typing.TypedDict, total=False):
    hour: int
    minute: int
    timeZone: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeleteRegionRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class DeliveryTime(typing.TypedDict, total=False):
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
class DeveloperRegistration(typing.TypedDict, total=False):
    gcpIds: _list[str]
    name: str

@typing.type_check_only
class DisableProgramRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Distance(typing.TypedDict, total=False):
    unit: typing.Literal["UNIT_UNSPECIFIED", "MILES", "KILOMETERS"]
    value: str

@typing.type_check_only
class EmailPreferences(typing.TypedDict, total=False):
    name: str
    newsAndTips: typing.Literal[
        "OPT_IN_STATE_UNSPECIFIED", "OPTED_OUT", "OPTED_IN", "UNCONFIRMED"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnableProgramRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class FindLfpProvidersResponse(typing.TypedDict, total=False):
    lfpProviders: _list[LfpProvider]
    nextPageToken: str

@typing.type_check_only
class GbpAccount(typing.TypedDict, total=False):
    gbpAccountId: str
    gbpAccountName: str
    listingCount: str
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "USER", "BUSINESS_ACCOUNT"]

@typing.type_check_only
class GeoTargetArea(typing.TypedDict, total=False):
    geotargetCriteriaIds: _list[str]

@typing.type_check_only
class GetAccountForGcpRegistrationResponse(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Handshake(typing.TypedDict, total=False):
    actor: typing.Literal["ACTOR_UNSPECIFIED", "ACCOUNT", "OTHER_PARTY"]
    approvalState: typing.Literal[
        "APPROVAL_STATE_UNSPECIFIED", "PENDING", "WAITING", "ESTABLISHED", "REJECTED"
    ]

@typing.type_check_only
class Headers(typing.TypedDict, total=False):
    locations: _list[LocationIdSet]
    numberOfItems: _list[str]
    postalCodeGroupNames: _list[str]
    prices: _list[Price]
    weights: _list[Weight]

@typing.type_check_only
class Homepage(typing.TypedDict, total=False):
    claimed: bool
    name: str
    uri: str

@typing.type_check_only
class IdentityAttribute(typing.TypedDict, total=False):
    identityDeclaration: typing.Literal[
        "IDENTITY_DECLARATION_UNSPECIFIED",
        "SELF_IDENTIFIES_AS",
        "DOES_NOT_SELF_IDENTIFY_AS",
    ]

@typing.type_check_only
class ImageImprovementsAccountLevelSettings(typing.TypedDict, total=False):
    allowAutomaticImageImprovements: bool

@typing.type_check_only
class Impact(typing.TypedDict, total=False):
    regionCode: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "CRITICAL", "ERROR", "SUGGESTION"]

@typing.type_check_only
class ImpactedDestination(typing.TypedDict, total=False):
    impacts: _list[Impact]
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
class InStock(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class InventoryVerification(typing.TypedDict, total=False):
    contact: str
    contactEmail: str
    contactState: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ACTION_REQUIRED",
        "INACTIVE",
        "RUNNING",
        "SUCCEEDED",
        "SUSPENDED",
    ]

@typing.type_check_only
class ItemUpdatesAccountLevelSettings(typing.TypedDict, total=False):
    allowAvailabilityUpdates: bool
    allowConditionUpdates: bool
    allowPriceUpdates: bool
    allowStrictAvailabilityUpdates: bool

@typing.type_check_only
class LatLng(typing.TypedDict, total=False):
    latitude: float
    longitude: float

@typing.type_check_only
class LfpLink(typing.TypedDict, total=False):
    externalAccountId: str
    lfpProvider: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]

@typing.type_check_only
class LfpProvider(typing.TypedDict, total=False):
    displayName: str
    name: str
    regionCode: str

@typing.type_check_only
class LinkGbpAccountRequest(typing.TypedDict, total=False):
    gbpEmail: str

@typing.type_check_only
class LinkGbpAccountResponse(typing.TypedDict, total=False):
    response: Empty

@typing.type_check_only
class LinkLfpProviderRequest(typing.TypedDict, total=False):
    externalAccountId: str

@typing.type_check_only
class LinkLfpProviderResponse(typing.TypedDict, total=False):
    response: Empty

@typing.type_check_only
class ListAccountIssuesResponse(typing.TypedDict, total=False):
    accountIssues: _list[AccountIssue]
    nextPageToken: str

@typing.type_check_only
class ListAccountRelationshipsResponse(typing.TypedDict, total=False):
    accountRelationships: _list[AccountRelationship]
    nextPageToken: str

@typing.type_check_only
class ListAccountServicesResponse(typing.TypedDict, total=False):
    accountServices: _list[AccountService]
    nextPageToken: str

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListGbpAccountsResponse(typing.TypedDict, total=False):
    gbpAccounts: _list[GbpAccount]
    nextPageToken: str

@typing.type_check_only
class ListOmnichannelSettingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    omnichannelSettings: _list[OmnichannelSetting]

@typing.type_check_only
class ListOnlineReturnPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    onlineReturnPolicies: _list[OnlineReturnPolicy]

@typing.type_check_only
class ListProgramsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    programs: _list[Program]

@typing.type_check_only
class ListRegionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    regions: _list[Region]

@typing.type_check_only
class ListSubAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListUsersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    users: _list[User]

@typing.type_check_only
class LocalCutoffTime(typing.TypedDict, total=False):
    hour: str
    minute: str

@typing.type_check_only
class LocalListingManagement(typing.TypedDict, total=False): ...

@typing.type_check_only
class LocationIdSet(typing.TypedDict, total=False):
    locationIds: _list[str]

@typing.type_check_only
class LoyaltyProgram(typing.TypedDict, total=False):
    loyaltyProgramTiers: _list[LoyaltyProgramTiers]
    programLabel: str

@typing.type_check_only
class LoyaltyProgramTiers(typing.TypedDict, total=False):
    tierLabel: str

@typing.type_check_only
class MinimumOrderValueTable(typing.TypedDict, total=False):
    storeCodeSetWithMovs: _list[StoreCodeSetWithMov]

@typing.type_check_only
class OmnichannelSetting(typing.TypedDict, total=False):
    about: About
    inStock: InStock
    inventoryVerification: InventoryVerification
    lfpLink: LfpLink
    lsfType: typing.Literal[
        "LSF_TYPE_UNSPECIFIED", "GHLSF", "MHLSF_BASIC", "MHLSF_FULL"
    ]
    name: str
    odo: OnDisplayToOrder
    pickup: Pickup
    regionCode: str

@typing.type_check_only
class OnDisplayToOrder(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class OnlineReturnPolicy(typing.TypedDict, total=False):
    acceptDefectiveOnly: bool
    acceptExchange: bool
    countries: _list[str]
    itemConditions: _list[typing.Literal["ITEM_CONDITION_UNSPECIFIED", "NEW", "USED"]]
    label: str
    name: str
    policy: Policy
    processRefundDays: int
    restockingFee: RestockingFee
    returnLabelSource: typing.Literal[
        "RETURN_LABEL_SOURCE_UNSPECIFIED",
        "DOWNLOAD_AND_PRINT",
        "IN_THE_PACKAGE",
        "CUSTOMER_RESPONSIBILITY",
    ]
    returnMethods: _list[
        typing.Literal["RETURN_METHOD_UNSPECIFIED", "BY_MAIL", "IN_STORE", "AT_A_KIOSK"]
    ]
    returnPolicyId: str
    returnPolicyUri: str
    returnShippingFee: ReturnShippingFee
    seasonalOverrides: _list[SeasonalOverride]

@typing.type_check_only
class PhoneNumber(typing.TypedDict, total=False):
    e164Number: str
    extension: str
    shortCode: ShortCode

@typing.type_check_only
class Pickup(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "FAILED", "RUNNING", "ACTION_REQUIRED"
    ]
    uri: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    days: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "NUMBER_OF_DAYS_AFTER_DELIVERY",
        "NO_RETURNS",
        "LIFETIME_RETURNS",
    ]

@typing.type_check_only
class PostalAddress(typing.TypedDict, total=False):
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
class PostalCodeArea(typing.TypedDict, total=False):
    postalCodes: _list[PostalCodeRange]
    regionCode: str

@typing.type_check_only
class PostalCodeRange(typing.TypedDict, total=False):
    begin: str
    end: str

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
class ProductsManagement(typing.TypedDict, total=False): ...

@typing.type_check_only
class Program(typing.TypedDict, total=False):
    activeRegionCodes: _list[str]
    documentationUri: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "NOT_ELIGIBLE", "ELIGIBLE", "ENABLED"]
    unmetRequirements: _list[Requirement]

@typing.type_check_only
class ProposeAccountServiceRequest(typing.TypedDict, total=False):
    accountService: AccountService
    provider: str

@typing.type_check_only
class RadiusArea(typing.TypedDict, total=False):
    latLng: LatLng
    radius: float
    radiusUnits: typing.Literal["RADIUS_UNITS_UNSPECIFIED", "MILES", "KILOMETERS"]
    regionCode: str

@typing.type_check_only
class RateGroup(typing.TypedDict, total=False):
    applicableShippingLabels: _list[str]
    carrierRates: _list[CarrierRate]
    mainTable: Table
    name: str
    singleValue: Value
    subtables: _list[Table]

@typing.type_check_only
class Region(typing.TypedDict, total=False):
    displayName: str
    geotargetArea: GeoTargetArea
    name: str
    postalCodeArea: PostalCodeArea
    radiusArea: RadiusArea
    regionalInventoryEligible: bool
    shippingEligible: bool

@typing.type_check_only
class RegisterGcpRequest(typing.TypedDict, total=False):
    developerEmail: str

@typing.type_check_only
class RejectAccountServiceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RequestInventoryVerificationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RequestInventoryVerificationResponse(typing.TypedDict, total=False):
    omnichannelSetting: OmnichannelSetting

@typing.type_check_only
class Required(typing.TypedDict, total=False):
    termsOfService: str
    tosFileUri: str

@typing.type_check_only
class Requirement(typing.TypedDict, total=False):
    affectedRegionCodes: _list[str]
    documentationUri: str
    title: str

@typing.type_check_only
class RestockingFee(typing.TypedDict, total=False):
    fixedFee: Price
    microPercent: int

@typing.type_check_only
class ReturnShippingFee(typing.TypedDict, total=False):
    fixedFee: Price
    type: typing.Literal["TYPE_UNSPECIFIED", "FIXED", "CUSTOMER_PAYING_ACTUAL_FEE"]

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    cells: _list[Value]

@typing.type_check_only
class SeasonalOverride(typing.TypedDict, total=False):
    endDate: Date
    label: str
    returnDays: int
    returnUntilDate: Date
    startDate: Date

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    active: bool
    currencyCode: str
    deliveryCountries: _list[str]
    deliveryTime: DeliveryTime
    loyaltyPrograms: _list[LoyaltyProgram]
    minimumOrderValue: Price
    minimumOrderValueTable: MinimumOrderValueTable
    rateGroups: _list[RateGroup]
    serviceName: str
    shipmentType: typing.Literal[
        "SHIPMENT_TYPE_UNSPECIFIED", "DELIVERY", "LOCAL_DELIVERY", "COLLECTION_POINT"
    ]
    storeConfig: StoreConfig

@typing.type_check_only
class SetAliasForRelationship(typing.TypedDict, total=False):
    accountIdAlias: str
    provider: str

@typing.type_check_only
class ShippingSettings(typing.TypedDict, total=False):
    etag: str
    name: str
    services: _list[Service]
    warehouses: _list[Warehouse]

@typing.type_check_only
class ShortCode(typing.TypedDict, total=False):
    number: str
    regionCode: str

@typing.type_check_only
class StoreCodeSetWithMov(typing.TypedDict, total=False):
    storeCodes: _list[str]
    value: Price

@typing.type_check_only
class StoreConfig(typing.TypedDict, total=False):
    cutoffConfig: CutoffConfig
    serviceRadius: Distance
    storeCodes: _list[str]
    storeServiceType: typing.Literal[
        "STORE_SERVICE_TYPE_UNSPECIFIED", "ALL_STORES", "SELECTED_STORES"
    ]

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    columnHeaders: Headers
    name: str
    rowHeaders: Headers
    rows: _list[Row]

@typing.type_check_only
class TermsOfService(typing.TypedDict, total=False):
    external: bool
    fileUri: str
    kind: typing.Literal["TERMS_OF_SERVICE_KIND_UNSPECIFIED", "MERCHANT_CENTER"]
    name: str
    regionCode: str

@typing.type_check_only
class TermsOfServiceAgreementState(typing.TypedDict, total=False):
    accepted: Accepted
    name: str
    regionCode: str
    required: Required
    termsOfServiceKind: typing.Literal[
        "TERMS_OF_SERVICE_KIND_UNSPECIFIED", "MERCHANT_CENTER"
    ]

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

@typing.type_check_only
class TransitTable(typing.TypedDict, total=False):
    postalCodeGroupNames: _list[str]
    rows: _list[TransitTimeRow]
    transitTimeLabels: _list[str]

@typing.type_check_only
class TransitTimeRow(typing.TypedDict, total=False):
    values: _list[TransitTimeValue]

@typing.type_check_only
class TransitTimeValue(typing.TypedDict, total=False):
    maxTransitDays: int
    minTransitDays: int

@typing.type_check_only
class UnclaimHomepageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UnregisterGcpRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateRegionRequest(typing.TypedDict, total=False):
    region: Region
    updateMask: str

@typing.type_check_only
class UriSettings(typing.TypedDict, total=False):
    cartUriTemplate: str
    checkoutUriTemplate: str

@typing.type_check_only
class User(typing.TypedDict, total=False):
    accessRights: _list[
        typing.Literal[
            "ACCESS_RIGHT_UNSPECIFIED",
            "STANDARD",
            "READ_ONLY",
            "ADMIN",
            "PERFORMANCE_REPORTING",
            "API_DEVELOPER",
        ]
    ]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "PENDING", "VERIFIED"]

@typing.type_check_only
class Value(typing.TypedDict, total=False):
    carrierRate: str
    flatRate: Price
    noShipping: bool
    pricePercentage: str
    subtable: str

@typing.type_check_only
class VerificationMailSettings(typing.TypedDict, total=False):
    verificationMailMode: typing.Literal[
        "VERIFICATION_MAIL_MODE_UNSPECIFIED",
        "SEND_VERIFICATION_MAIL",
        "SUPPRESS_VERIFICATION_MAIL",
    ]

@typing.type_check_only
class VerifySelfRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Warehouse(typing.TypedDict, total=False):
    businessDayConfig: BusinessDayConfig
    cutoffTime: WarehouseCutoffTime
    handlingDays: str
    name: str
    shippingAddress: Address

@typing.type_check_only
class WarehouseBasedDeliveryTime(typing.TypedDict, total=False):
    carrier: str
    carrierService: str
    warehouse: str

@typing.type_check_only
class WarehouseCutoffTime(typing.TypedDict, total=False):
    hour: int
    minute: int

@typing.type_check_only
class Weight(typing.TypedDict, total=False):
    amountMicros: str
    unit: typing.Literal["WEIGHT_UNIT_UNSPECIFIED", "POUND", "KILOGRAM"]
