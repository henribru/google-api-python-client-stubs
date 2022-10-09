import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudChannelV1ActivateEntitlementRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1AdminUser(typing_extensions.TypedDict, total=False):
    email: str
    familyName: str
    givenName: str

@typing.type_check_only
class GoogleCloudChannelV1AssociationInfo(typing_extensions.TypedDict, total=False):
    baseEntitlement: str

@typing.type_check_only
class GoogleCloudChannelV1CancelEntitlementRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1ChangeOfferRequest(typing_extensions.TypedDict, total=False):
    offer: str
    parameters: _list[GoogleCloudChannelV1Parameter]
    purchaseOrderId: str
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1ChangeParametersRequest(
    typing_extensions.TypedDict, total=False
):
    parameters: _list[GoogleCloudChannelV1Parameter]
    purchaseOrderId: str
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1ChangeRenewalSettingsRequest(
    typing_extensions.TypedDict, total=False
):
    renewalSettings: GoogleCloudChannelV1RenewalSettings
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1ChannelPartnerLink(typing_extensions.TypedDict, total=False):
    channelPartnerCloudIdentityInfo: GoogleCloudChannelV1CloudIdentityInfo
    createTime: str
    inviteLinkUri: str
    linkState: typing_extensions.Literal[
        "CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED",
        "INVITED",
        "ACTIVE",
        "REVOKED",
        "SUSPENDED",
    ]
    name: str
    publicId: str
    resellerCloudIdentityId: str
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1ChannelPartnerRepricingConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    repricingConfig: GoogleCloudChannelV1RepricingConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequest(
    typing_extensions.TypedDict, total=False
):
    domain: str

@typing.type_check_only
class GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponse(
    typing_extensions.TypedDict, total=False
):
    cloudIdentityAccounts: _list[GoogleCloudChannelV1CloudIdentityCustomerAccount]

@typing.type_check_only
class GoogleCloudChannelV1CloudIdentityCustomerAccount(
    typing_extensions.TypedDict, total=False
):
    customerCloudIdentityId: str
    customerName: str
    existing: bool
    owned: bool

@typing.type_check_only
class GoogleCloudChannelV1CloudIdentityInfo(typing_extensions.TypedDict, total=False):
    adminConsoleUri: str
    alternateEmail: str
    customerType: typing_extensions.Literal[
        "CUSTOMER_TYPE_UNSPECIFIED", "DOMAIN", "TEAM"
    ]
    eduData: GoogleCloudChannelV1EduData
    isDomainVerified: bool
    languageCode: str
    phoneNumber: str
    primaryDomain: str

@typing.type_check_only
class GoogleCloudChannelV1CommitmentSettings(typing_extensions.TypedDict, total=False):
    endTime: str
    renewalSettings: GoogleCloudChannelV1RenewalSettings
    startTime: str

@typing.type_check_only
class GoogleCloudChannelV1Constraints(typing_extensions.TypedDict, total=False):
    customerConstraints: GoogleCloudChannelV1CustomerConstraints

@typing.type_check_only
class GoogleCloudChannelV1ContactInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str
    firstName: str
    lastName: str
    phone: str
    title: str

@typing.type_check_only
class GoogleCloudChannelV1CreateEntitlementRequest(
    typing_extensions.TypedDict, total=False
):
    entitlement: GoogleCloudChannelV1Entitlement
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1Customer(typing_extensions.TypedDict, total=False):
    alternateEmail: str
    channelPartnerId: str
    cloudIdentityId: str
    cloudIdentityInfo: GoogleCloudChannelV1CloudIdentityInfo
    createTime: str
    domain: str
    languageCode: str
    name: str
    orgDisplayName: str
    orgPostalAddress: GoogleTypePostalAddress
    primaryContactInfo: GoogleCloudChannelV1ContactInfo
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1CustomerConstraints(typing_extensions.TypedDict, total=False):
    allowedCustomerTypes: _list[str]
    allowedRegions: _list[str]
    promotionalOrderTypes: _list[str]

@typing.type_check_only
class GoogleCloudChannelV1CustomerEvent(typing_extensions.TypedDict, total=False):
    customer: str
    eventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PRIMARY_DOMAIN_CHANGED", "PRIMARY_DOMAIN_VERIFIED"
    ]

@typing.type_check_only
class GoogleCloudChannelV1CustomerRepricingConfig(
    typing_extensions.TypedDict, total=False
):
    name: str
    repricingConfig: GoogleCloudChannelV1RepricingConfig
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1EduData(typing_extensions.TypedDict, total=False):
    instituteSize: typing_extensions.Literal[
        "INSTITUTE_SIZE_UNSPECIFIED",
        "SIZE_1_100",
        "SIZE_101_500",
        "SIZE_501_1000",
        "SIZE_1001_2000",
        "SIZE_2001_5000",
        "SIZE_5001_10000",
        "SIZE_10001_OR_MORE",
    ]
    instituteType: typing_extensions.Literal[
        "INSTITUTE_TYPE_UNSPECIFIED", "K12", "UNIVERSITY"
    ]
    website: str

@typing.type_check_only
class GoogleCloudChannelV1Entitlement(typing_extensions.TypedDict, total=False):
    associationInfo: GoogleCloudChannelV1AssociationInfo
    commitmentSettings: GoogleCloudChannelV1CommitmentSettings
    createTime: str
    name: str
    offer: str
    parameters: _list[GoogleCloudChannelV1Parameter]
    provisionedService: GoogleCloudChannelV1ProvisionedService
    provisioningState: typing_extensions.Literal[
        "PROVISIONING_STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"
    ]
    purchaseOrderId: str
    suspensionReasons: _list[str]
    trialSettings: GoogleCloudChannelV1TrialSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1EntitlementEvent(typing_extensions.TypedDict, total=False):
    entitlement: str
    eventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CREATED",
        "PRICE_PLAN_SWITCHED",
        "COMMITMENT_CHANGED",
        "RENEWED",
        "SUSPENDED",
        "ACTIVATED",
        "CANCELLED",
        "SKU_CHANGED",
        "RENEWAL_SETTING_CHANGED",
        "PAID_SERVICE_STARTED",
        "LICENSE_ASSIGNMENT_CHANGED",
        "LICENSE_CAP_CHANGED",
    ]

@typing.type_check_only
class GoogleCloudChannelV1ImportCustomerRequest(
    typing_extensions.TypedDict, total=False
):
    authToken: str
    channelPartnerId: str
    cloudIdentityId: str
    customer: str
    domain: str
    overwriteIfExists: bool

@typing.type_check_only
class GoogleCloudChannelV1ListChannelPartnerLinksResponse(
    typing_extensions.TypedDict, total=False
):
    channelPartnerLinks: _list[GoogleCloudChannelV1ChannelPartnerLink]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListChannelPartnerRepricingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    channelPartnerRepricingConfigs: _list[
        GoogleCloudChannelV1ChannelPartnerRepricingConfig
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListCustomerRepricingConfigsResponse(
    typing_extensions.TypedDict, total=False
):
    customerRepricingConfigs: _list[GoogleCloudChannelV1CustomerRepricingConfig]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListCustomersResponse(
    typing_extensions.TypedDict, total=False
):
    customers: _list[GoogleCloudChannelV1Customer]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListEntitlementsResponse(
    typing_extensions.TypedDict, total=False
):
    entitlements: _list[GoogleCloudChannelV1Entitlement]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListOffersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    offers: _list[GoogleCloudChannelV1Offer]

@typing.type_check_only
class GoogleCloudChannelV1ListProductsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    products: _list[GoogleCloudChannelV1Product]

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableOffersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    purchasableOffers: _list[GoogleCloudChannelV1PurchasableOffer]

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableSkusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    purchasableSkus: _list[GoogleCloudChannelV1PurchasableSku]

@typing.type_check_only
class GoogleCloudChannelV1ListSkusResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    skus: _list[GoogleCloudChannelV1Sku]

@typing.type_check_only
class GoogleCloudChannelV1ListSubscribersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    serviceAccounts: _list[str]
    topic: str

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableOffersRequest(
    typing_extensions.TypedDict, total=False
):
    cloudIdentityId: str
    customerName: str
    languageCode: str
    pageSize: int
    pageToken: str
    sku: str

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableOffersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    transferableOffers: _list[GoogleCloudChannelV1TransferableOffer]

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableSkusRequest(
    typing_extensions.TypedDict, total=False
):
    authToken: str
    cloudIdentityId: str
    customerName: str
    languageCode: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableSkusResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    transferableSkus: _list[GoogleCloudChannelV1TransferableSku]

@typing.type_check_only
class GoogleCloudChannelV1MarketingInfo(typing_extensions.TypedDict, total=False):
    defaultLogo: GoogleCloudChannelV1Media
    description: str
    displayName: str

@typing.type_check_only
class GoogleCloudChannelV1Media(typing_extensions.TypedDict, total=False):
    content: str
    title: str
    type: typing_extensions.Literal["MEDIA_TYPE_UNSPECIFIED", "MEDIA_TYPE_IMAGE"]

@typing.type_check_only
class GoogleCloudChannelV1Offer(typing_extensions.TypedDict, total=False):
    constraints: GoogleCloudChannelV1Constraints
    endTime: str
    marketingInfo: GoogleCloudChannelV1MarketingInfo
    name: str
    parameterDefinitions: _list[GoogleCloudChannelV1ParameterDefinition]
    plan: GoogleCloudChannelV1Plan
    priceByResources: _list[GoogleCloudChannelV1PriceByResource]
    sku: GoogleCloudChannelV1Sku
    startTime: str

@typing.type_check_only
class GoogleCloudChannelV1OperationMetadata(typing_extensions.TypedDict, total=False):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE_ENTITLEMENT",
        "CHANGE_RENEWAL_SETTINGS",
        "START_PAID_SERVICE",
        "ACTIVATE_ENTITLEMENT",
        "SUSPEND_ENTITLEMENT",
        "CANCEL_ENTITLEMENT",
        "TRANSFER_ENTITLEMENTS",
        "TRANSFER_ENTITLEMENTS_TO_GOOGLE",
        "CHANGE_OFFER",
        "CHANGE_PARAMETERS",
        "PROVISION_CLOUD_IDENTITY",
    ]

@typing.type_check_only
class GoogleCloudChannelV1Parameter(typing_extensions.TypedDict, total=False):
    editable: bool
    name: str
    value: GoogleCloudChannelV1Value

@typing.type_check_only
class GoogleCloudChannelV1ParameterDefinition(typing_extensions.TypedDict, total=False):
    allowedValues: _list[GoogleCloudChannelV1Value]
    maxValue: GoogleCloudChannelV1Value
    minValue: GoogleCloudChannelV1Value
    name: str
    optional: bool
    parameterType: typing_extensions.Literal[
        "PARAMETER_TYPE_UNSPECIFIED", "INT64", "STRING", "DOUBLE"
    ]

@typing.type_check_only
class GoogleCloudChannelV1PercentageAdjustment(
    typing_extensions.TypedDict, total=False
):
    percentage: GoogleTypeDecimal

@typing.type_check_only
class GoogleCloudChannelV1Period(typing_extensions.TypedDict, total=False):
    duration: int
    periodType: typing_extensions.Literal[
        "PERIOD_TYPE_UNSPECIFIED", "DAY", "MONTH", "YEAR"
    ]

@typing.type_check_only
class GoogleCloudChannelV1Plan(typing_extensions.TypedDict, total=False):
    billingAccount: str
    paymentCycle: GoogleCloudChannelV1Period
    paymentPlan: typing_extensions.Literal[
        "PAYMENT_PLAN_UNSPECIFIED", "COMMITMENT", "FLEXIBLE", "FREE", "TRIAL", "OFFLINE"
    ]
    paymentType: typing_extensions.Literal[
        "PAYMENT_TYPE_UNSPECIFIED", "PREPAY", "POSTPAY"
    ]
    trialPeriod: GoogleCloudChannelV1Period

@typing.type_check_only
class GoogleCloudChannelV1Price(typing_extensions.TypedDict, total=False):
    basePrice: GoogleTypeMoney
    discount: float
    effectivePrice: GoogleTypeMoney
    externalPriceUri: str

@typing.type_check_only
class GoogleCloudChannelV1PriceByResource(typing_extensions.TypedDict, total=False):
    price: GoogleCloudChannelV1Price
    pricePhases: _list[GoogleCloudChannelV1PricePhase]
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "SEAT",
        "MAU",
        "GB",
        "LICENSED_USER",
        "MINUTES",
        "IAAS_USAGE",
        "SUBSCRIPTION",
    ]

@typing.type_check_only
class GoogleCloudChannelV1PricePhase(typing_extensions.TypedDict, total=False):
    firstPeriod: int
    lastPeriod: int
    periodType: typing_extensions.Literal[
        "PERIOD_TYPE_UNSPECIFIED", "DAY", "MONTH", "YEAR"
    ]
    price: GoogleCloudChannelV1Price
    priceTiers: _list[GoogleCloudChannelV1PriceTier]

@typing.type_check_only
class GoogleCloudChannelV1PriceTier(typing_extensions.TypedDict, total=False):
    firstResource: int
    lastResource: int
    price: GoogleCloudChannelV1Price

@typing.type_check_only
class GoogleCloudChannelV1Product(typing_extensions.TypedDict, total=False):
    marketingInfo: GoogleCloudChannelV1MarketingInfo
    name: str

@typing.type_check_only
class GoogleCloudChannelV1ProvisionCloudIdentityRequest(
    typing_extensions.TypedDict, total=False
):
    cloudIdentityInfo: GoogleCloudChannelV1CloudIdentityInfo
    user: GoogleCloudChannelV1AdminUser
    validateOnly: bool

@typing.type_check_only
class GoogleCloudChannelV1ProvisionedService(typing_extensions.TypedDict, total=False):
    productId: str
    provisioningId: str
    skuId: str

@typing.type_check_only
class GoogleCloudChannelV1PurchasableOffer(typing_extensions.TypedDict, total=False):
    offer: GoogleCloudChannelV1Offer

@typing.type_check_only
class GoogleCloudChannelV1PurchasableSku(typing_extensions.TypedDict, total=False):
    sku: GoogleCloudChannelV1Sku

@typing.type_check_only
class GoogleCloudChannelV1RegisterSubscriberRequest(
    typing_extensions.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudChannelV1RegisterSubscriberResponse(
    typing_extensions.TypedDict, total=False
):
    topic: str

@typing.type_check_only
class GoogleCloudChannelV1RenewalSettings(typing_extensions.TypedDict, total=False):
    enableRenewal: bool
    paymentCycle: GoogleCloudChannelV1Period
    paymentPlan: typing_extensions.Literal[
        "PAYMENT_PLAN_UNSPECIFIED", "COMMITMENT", "FLEXIBLE", "FREE", "TRIAL", "OFFLINE"
    ]
    resizeUnitCount: bool

@typing.type_check_only
class GoogleCloudChannelV1RepricingAdjustment(typing_extensions.TypedDict, total=False):
    percentageAdjustment: GoogleCloudChannelV1PercentageAdjustment

@typing.type_check_only
class GoogleCloudChannelV1RepricingConfig(typing_extensions.TypedDict, total=False):
    adjustment: GoogleCloudChannelV1RepricingAdjustment
    channelPartnerGranularity: GoogleCloudChannelV1RepricingConfigChannelPartnerGranularity
    effectiveInvoiceMonth: GoogleTypeDate
    entitlementGranularity: GoogleCloudChannelV1RepricingConfigEntitlementGranularity
    rebillingBasis: typing_extensions.Literal[
        "REBILLING_BASIS_UNSPECIFIED", "COST_AT_LIST", "DIRECT_CUSTOMER_COST"
    ]

@typing.type_check_only
class GoogleCloudChannelV1RepricingConfigChannelPartnerGranularity(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudChannelV1RepricingConfigEntitlementGranularity(
    typing_extensions.TypedDict, total=False
):
    entitlement: str

@typing.type_check_only
class GoogleCloudChannelV1Sku(typing_extensions.TypedDict, total=False):
    marketingInfo: GoogleCloudChannelV1MarketingInfo
    name: str
    product: GoogleCloudChannelV1Product

@typing.type_check_only
class GoogleCloudChannelV1StartPaidServiceRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1SubscriberEvent(typing_extensions.TypedDict, total=False):
    customerEvent: GoogleCloudChannelV1CustomerEvent
    entitlementEvent: GoogleCloudChannelV1EntitlementEvent

@typing.type_check_only
class GoogleCloudChannelV1SuspendEntitlementRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1TransferEligibility(typing_extensions.TypedDict, total=False):
    description: str
    ineligibilityReason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "PENDING_TOS_ACCEPTANCE",
        "SKU_NOT_ELIGIBLE",
        "SKU_SUSPENDED",
    ]
    isEligible: bool

@typing.type_check_only
class GoogleCloudChannelV1TransferEntitlementsRequest(
    typing_extensions.TypedDict, total=False
):
    authToken: str
    entitlements: _list[GoogleCloudChannelV1Entitlement]
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1TransferEntitlementsResponse(
    typing_extensions.TypedDict, total=False
):
    entitlements: _list[GoogleCloudChannelV1Entitlement]

@typing.type_check_only
class GoogleCloudChannelV1TransferEntitlementsToGoogleRequest(
    typing_extensions.TypedDict, total=False
):
    entitlements: _list[GoogleCloudChannelV1Entitlement]
    requestId: str

@typing.type_check_only
class GoogleCloudChannelV1TransferableOffer(typing_extensions.TypedDict, total=False):
    offer: GoogleCloudChannelV1Offer

@typing.type_check_only
class GoogleCloudChannelV1TransferableSku(typing_extensions.TypedDict, total=False):
    legacySku: GoogleCloudChannelV1Sku
    sku: GoogleCloudChannelV1Sku
    transferEligibility: GoogleCloudChannelV1TransferEligibility

@typing.type_check_only
class GoogleCloudChannelV1TrialSettings(typing_extensions.TypedDict, total=False):
    endTime: str
    trial: bool

@typing.type_check_only
class GoogleCloudChannelV1UnregisterSubscriberRequest(
    typing_extensions.TypedDict, total=False
):
    serviceAccount: str

@typing.type_check_only
class GoogleCloudChannelV1UnregisterSubscriberResponse(
    typing_extensions.TypedDict, total=False
):
    topic: str

@typing.type_check_only
class GoogleCloudChannelV1UpdateChannelPartnerLinkRequest(
    typing_extensions.TypedDict, total=False
):
    channelPartnerLink: GoogleCloudChannelV1ChannelPartnerLink
    updateMask: str

@typing.type_check_only
class GoogleCloudChannelV1Value(typing_extensions.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    int64Value: str
    protoValue: dict[str, typing.Any]
    stringValue: str

@typing.type_check_only
class GoogleCloudChannelV1alpha1AssociationInfo(
    typing_extensions.TypedDict, total=False
):
    baseEntitlement: str

@typing.type_check_only
class GoogleCloudChannelV1alpha1ChannelPartnerEvent(
    typing_extensions.TypedDict, total=False
):
    channelPartner: str
    eventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "LINK_STATE_CHANGED", "PARTNER_ADVANTAGE_INFO_CHANGED"
    ]

@typing.type_check_only
class GoogleCloudChannelV1alpha1CommitmentSettings(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    renewalSettings: GoogleCloudChannelV1alpha1RenewalSettings
    startTime: str

@typing.type_check_only
class GoogleCloudChannelV1alpha1CustomerEvent(typing_extensions.TypedDict, total=False):
    customer: str
    eventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "PRIMARY_DOMAIN_CHANGED", "PRIMARY_DOMAIN_VERIFIED"
    ]

@typing.type_check_only
class GoogleCloudChannelV1alpha1Entitlement(typing_extensions.TypedDict, total=False):
    assignedUnits: int
    associationInfo: GoogleCloudChannelV1alpha1AssociationInfo
    channelPartnerId: str
    commitmentSettings: GoogleCloudChannelV1alpha1CommitmentSettings
    createTime: str
    maxUnits: int
    name: str
    numUnits: int
    offer: str
    parameters: _list[GoogleCloudChannelV1alpha1Parameter]
    provisionedService: GoogleCloudChannelV1alpha1ProvisionedService
    provisioningState: typing_extensions.Literal[
        "PROVISIONING_STATE_UNSPECIFIED",
        "ACTIVE",
        "CANCELED",
        "COMPLETE",
        "PENDING",
        "SUSPENDED",
    ]
    purchaseOrderId: str
    suspensionReasons: _list[str]
    trialSettings: GoogleCloudChannelV1alpha1TrialSettings
    updateTime: str

@typing.type_check_only
class GoogleCloudChannelV1alpha1EntitlementEvent(
    typing_extensions.TypedDict, total=False
):
    entitlement: str
    eventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CREATED",
        "PRICE_PLAN_SWITCHED",
        "COMMITMENT_CHANGED",
        "RENEWED",
        "SUSPENDED",
        "ACTIVATED",
        "CANCELLED",
        "SKU_CHANGED",
        "RENEWAL_SETTING_CHANGED",
        "PAID_SERVICE_STARTED",
        "LICENSE_ASSIGNMENT_CHANGED",
        "LICENSE_CAP_CHANGED",
    ]

@typing.type_check_only
class GoogleCloudChannelV1alpha1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "CREATE_ENTITLEMENT",
        "CHANGE_QUANTITY",
        "CHANGE_RENEWAL_SETTINGS",
        "CHANGE_PLAN",
        "START_PAID_SERVICE",
        "CHANGE_SKU",
        "ACTIVATE_ENTITLEMENT",
        "SUSPEND_ENTITLEMENT",
        "CANCEL_ENTITLEMENT",
        "TRANSFER_ENTITLEMENTS",
        "TRANSFER_ENTITLEMENTS_TO_GOOGLE",
        "CHANGE_OFFER",
        "CHANGE_PARAMETERS",
        "PROVISION_CLOUD_IDENTITY",
    ]

@typing.type_check_only
class GoogleCloudChannelV1alpha1Parameter(typing_extensions.TypedDict, total=False):
    editable: bool
    name: str
    value: GoogleCloudChannelV1alpha1Value

@typing.type_check_only
class GoogleCloudChannelV1alpha1Period(typing_extensions.TypedDict, total=False):
    duration: int
    periodType: typing_extensions.Literal[
        "PERIOD_TYPE_UNSPECIFIED", "DAY", "MONTH", "YEAR"
    ]

@typing.type_check_only
class GoogleCloudChannelV1alpha1ProvisionedService(
    typing_extensions.TypedDict, total=False
):
    productId: str
    provisioningId: str
    skuId: str

@typing.type_check_only
class GoogleCloudChannelV1alpha1RenewalSettings(
    typing_extensions.TypedDict, total=False
):
    disableCommitment: bool
    enableRenewal: bool
    paymentCycle: GoogleCloudChannelV1alpha1Period
    paymentOption: typing_extensions.Literal[
        "PAYMENT_OPTION_UNSPECIFIED", "ANNUAL", "MONTHLY"
    ]
    paymentPlan: typing_extensions.Literal[
        "PAYMENT_PLAN_UNSPECIFIED", "COMMITMENT", "FLEXIBLE", "FREE", "TRIAL", "OFFLINE"
    ]
    resizeUnitCount: bool

@typing.type_check_only
class GoogleCloudChannelV1alpha1SubscriberEvent(
    typing_extensions.TypedDict, total=False
):
    channelPartnerEvent: GoogleCloudChannelV1alpha1ChannelPartnerEvent
    customerEvent: GoogleCloudChannelV1alpha1CustomerEvent
    entitlementEvent: GoogleCloudChannelV1alpha1EntitlementEvent

@typing.type_check_only
class GoogleCloudChannelV1alpha1TransferEntitlementsResponse(
    typing_extensions.TypedDict, total=False
):
    entitlements: _list[GoogleCloudChannelV1alpha1Entitlement]

@typing.type_check_only
class GoogleCloudChannelV1alpha1TrialSettings(typing_extensions.TypedDict, total=False):
    endTime: str
    trial: bool

@typing.type_check_only
class GoogleCloudChannelV1alpha1Value(typing_extensions.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    int64Value: str
    protoValue: dict[str, typing.Any]
    stringValue: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDecimal(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleTypeMoney(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypePostalAddress(typing_extensions.TypedDict, total=False):
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
