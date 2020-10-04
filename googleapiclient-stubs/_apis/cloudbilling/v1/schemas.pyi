import typing

import typing_extensions
@typing.type_check_only
class AggregationInfo(typing_extensions.TypedDict, total=False):
    aggregationCount: int
    aggregationInterval: typing_extensions.Literal[
        "AGGREGATION_INTERVAL_UNSPECIFIED", "DAILY", "MONTHLY"
    ]
    aggregationLevel: typing_extensions.Literal[
        "AGGREGATION_LEVEL_UNSPECIFIED", "ACCOUNT", "PROJECT"
    ]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BillingAccount(typing_extensions.TypedDict, total=False):
    displayName: str
    masterBillingAccount: str
    name: str
    open: bool

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Category(typing_extensions.TypedDict, total=False):
    resourceFamily: str
    resourceGroup: str
    serviceDisplayName: str
    usageType: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GeoTaxonomy(typing_extensions.TypedDict, total=False):
    regions: typing.List[str]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "GLOBAL", "REGIONAL", "MULTI_REGIONAL"
    ]

@typing.type_check_only
class ListBillingAccountsResponse(typing_extensions.TypedDict, total=False):
    billingAccounts: typing.List[BillingAccount]
    nextPageToken: str

@typing.type_check_only
class ListProjectBillingInfoResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    projectBillingInfo: typing.List[ProjectBillingInfo]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]

@typing.type_check_only
class ListSkusResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    skus: typing.List[Sku]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PricingExpression(typing_extensions.TypedDict, total=False):
    baseUnit: str
    baseUnitConversionFactor: float
    baseUnitDescription: str
    displayQuantity: float
    tieredRates: typing.List[TierRate]
    usageUnit: str
    usageUnitDescription: str

@typing.type_check_only
class PricingInfo(typing_extensions.TypedDict, total=False):
    aggregationInfo: AggregationInfo
    currencyConversionRate: float
    effectiveTime: str
    pricingExpression: PricingExpression
    summary: str

@typing.type_check_only
class ProjectBillingInfo(typing_extensions.TypedDict, total=False):
    billingAccountName: str
    billingEnabled: bool
    name: str
    projectId: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    businessEntityName: str
    displayName: str
    name: str
    serviceId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Sku(typing_extensions.TypedDict, total=False):
    category: Category
    description: str
    geoTaxonomy: GeoTaxonomy
    name: str
    pricingInfo: typing.List[PricingInfo]
    serviceProviderName: str
    serviceRegions: typing.List[str]
    skuId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TierRate(typing_extensions.TypedDict, total=False):
    startUsageAmount: float
    unitPrice: Money
