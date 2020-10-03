import typing

import typing_extensions

class ListBillingAccountsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    billingAccounts: typing.List[BillingAccount]

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListSkusResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    skus: typing.List[Sku]

class BillingAccount(typing_extensions.TypedDict, total=False):
    masterBillingAccount: str
    displayName: str
    name: str
    open: bool

class Money(typing_extensions.TypedDict, total=False):
    units: str
    nanos: int
    currencyCode: str

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str
    auditConfigs: typing.List[AuditConfig]

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]

class PricingInfo(typing_extensions.TypedDict, total=False):
    currencyConversionRate: float
    summary: str
    effectiveTime: str
    pricingExpression: PricingExpression
    aggregationInfo: AggregationInfo

class GeoTaxonomy(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GLOBAL", "REGIONAL", "MULTI_REGIONAL"
    ]
    regions: typing.List[str]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    condition: Expr

class AggregationInfo(typing_extensions.TypedDict, total=False):
    aggregationLevel: typing_extensions.Literal[
        "AGGREGATION_LEVEL_UNSPECIFIED", "ACCOUNT", "PROJECT"
    ]
    aggregationInterval: typing_extensions.Literal[
        "AGGREGATION_INTERVAL_UNSPECIFIED", "DAILY", "MONTHLY"
    ]
    aggregationCount: int

class Category(typing_extensions.TypedDict, total=False):
    resourceGroup: str
    usageType: str
    serviceDisplayName: str
    resourceFamily: str

class ListProjectBillingInfoResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projectBillingInfo: typing.List[ProjectBillingInfo]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class TierRate(typing_extensions.TypedDict, total=False):
    startUsageAmount: float
    unitPrice: Money

class PricingExpression(typing_extensions.TypedDict, total=False):
    baseUnit: str
    baseUnitDescription: str
    usageUnit: str
    displayQuantity: float
    usageUnitDescription: str
    baseUnitConversionFactor: float
    tieredRates: typing.List[TierRate]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    title: str
    expression: str
    location: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class Service(typing_extensions.TypedDict, total=False):
    serviceId: str
    displayName: str
    businessEntityName: str
    name: str

class Sku(typing_extensions.TypedDict, total=False):
    name: str
    serviceProviderName: str
    description: str
    geoTaxonomy: GeoTaxonomy
    skuId: str
    pricingInfo: typing.List[PricingInfo]
    serviceRegions: typing.List[str]
    category: Category

class ProjectBillingInfo(typing_extensions.TypedDict, total=False):
    billingEnabled: bool
    name: str
    billingAccountName: str
    projectId: str
