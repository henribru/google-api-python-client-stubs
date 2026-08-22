import typing

_list = list

@typing.type_check_only
class AggregationInfo(typing.TypedDict, total=False):
    aggregationCount: int
    aggregationInterval: typing.Literal[
        "AGGREGATION_INTERVAL_UNSPECIFIED", "DAILY", "MONTHLY"
    ]
    aggregationLevel: typing.Literal[
        "AGGREGATION_LEVEL_UNSPECIFIED", "ACCOUNT", "PROJECT"
    ]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BillingAccount(typing.TypedDict, total=False):
    currencyCode: str
    displayName: str
    masterBillingAccount: str
    name: str
    open: bool
    parent: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Category(typing.TypedDict, total=False):
    resourceFamily: str
    resourceGroup: str
    serviceDisplayName: str
    usageType: str

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GeoTaxonomy(typing.TypedDict, total=False):
    regions: _list[str]
    type: typing.Literal["TYPE_UNSPECIFIED", "GLOBAL", "REGIONAL", "MULTI_REGIONAL"]

@typing.type_check_only
class ListBillingAccountsResponse(typing.TypedDict, total=False):
    billingAccounts: _list[BillingAccount]
    nextPageToken: str

@typing.type_check_only
class ListProjectBillingInfoResponse(typing.TypedDict, total=False):
    nextPageToken: str
    projectBillingInfo: _list[ProjectBillingInfo]

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class ListSkusResponse(typing.TypedDict, total=False):
    nextPageToken: str
    skus: _list[Sku]

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class MoveBillingAccountRequest(typing.TypedDict, total=False):
    destinationParent: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PricingExpression(typing.TypedDict, total=False):
    baseUnit: str
    baseUnitConversionFactor: float
    baseUnitDescription: str
    displayQuantity: float
    tieredRates: _list[TierRate]
    usageUnit: str
    usageUnitDescription: str

@typing.type_check_only
class PricingInfo(typing.TypedDict, total=False):
    aggregationInfo: AggregationInfo
    currencyConversionRate: float
    effectiveTime: str
    pricingExpression: PricingExpression
    summary: str

@typing.type_check_only
class ProjectBillingInfo(typing.TypedDict, total=False):
    billingAccountName: str
    billingEnabled: bool
    name: str
    projectId: str

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    businessEntityName: str
    displayName: str
    name: str
    serviceId: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Sku(typing.TypedDict, total=False):
    category: Category
    description: str
    geoTaxonomy: GeoTaxonomy
    name: str
    pricingInfo: _list[PricingInfo]
    serviceProviderName: str
    serviceRegions: _list[str]
    skuId: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TierRate(typing.TypedDict, total=False):
    startUsageAmount: float
    unitPrice: Money
