import typing

_list = list

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
class AuthorizationCode(typing.TypedDict, total=False):
    code: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ConfigureContactSettingsRequest(typing.TypedDict, total=False):
    contactNotices: _list[
        typing.Literal[
            "CONTACT_NOTICE_UNSPECIFIED", "PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT"
        ]
    ]
    contactSettings: ContactSettings
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class ConfigureDnsSettingsRequest(typing.TypedDict, total=False):
    dnsSettings: DnsSettings
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class ConfigureManagementSettingsRequest(typing.TypedDict, total=False):
    managementSettings: ManagementSettings
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class Contact(typing.TypedDict, total=False):
    email: str
    faxNumber: str
    phoneNumber: str
    postalAddress: PostalAddress

@typing.type_check_only
class ContactSettings(typing.TypedDict, total=False):
    adminContact: Contact
    privacy: typing.Literal[
        "CONTACT_PRIVACY_UNSPECIFIED",
        "PUBLIC_CONTACT_DATA",
        "PRIVATE_CONTACT_DATA",
        "REDACTED_CONTACT_DATA",
    ]
    registrantContact: Contact
    technicalContact: Contact

@typing.type_check_only
class CustomDns(typing.TypedDict, total=False):
    dsRecords: _list[DsRecord]
    nameServers: _list[str]

@typing.type_check_only
class DnsSettings(typing.TypedDict, total=False):
    customDns: CustomDns
    glueRecords: _list[GlueRecord]
    googleDomainsDns: GoogleDomainsDns
    googleDomainsRedirectsDataAvailable: bool

@typing.type_check_only
class Domain(typing.TypedDict, total=False):
    domainName: str
    resourceState: typing.Literal[
        "RESOURCE_STATE_UNSPECIFIED",
        "IMPORTABLE",
        "UNSUPPORTED",
        "SUSPENDED",
        "EXPIRED",
        "DELETED",
    ]
    yearlyPrice: Money

@typing.type_check_only
class DomainForwarding(typing.TypedDict, total=False):
    pathForwarding: bool
    pemCertificate: str
    redirectType: typing.Literal["REDIRECT_TYPE_UNSPECIFIED", "TEMPORARY", "PERMANENT"]
    sslEnabled: bool
    subdomain: str
    targetUri: str

@typing.type_check_only
class DsRecord(typing.TypedDict, total=False):
    algorithm: typing.Literal[
        "ALGORITHM_UNSPECIFIED",
        "RSAMD5",
        "DH",
        "DSA",
        "ECC",
        "RSASHA1",
        "DSANSEC3SHA1",
        "RSASHA1NSEC3SHA1",
        "RSASHA256",
        "RSASHA512",
        "ECCGOST",
        "ECDSAP256SHA256",
        "ECDSAP384SHA384",
        "ED25519",
        "ED448",
        "INDIRECT",
        "PRIVATEDNS",
        "PRIVATEOID",
    ]
    digest: str
    digestType: typing.Literal[
        "DIGEST_TYPE_UNSPECIFIED", "SHA1", "SHA256", "GOST3411", "SHA384"
    ]
    keyTag: int

@typing.type_check_only
class EmailForwarding(typing.TypedDict, total=False):
    alias: str
    targetEmailAddress: str

@typing.type_check_only
class ExportRegistrationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GeoPolicy(typing.TypedDict, total=False):
    enableFencing: bool
    item: _list[GeoPolicyItem]

@typing.type_check_only
class GeoPolicyItem(typing.TypedDict, total=False):
    healthCheckedTargets: HealthCheckTargets
    location: str
    rrdata: _list[str]
    signatureRrdata: _list[str]

@typing.type_check_only
class GlueRecord(typing.TypedDict, total=False):
    hostName: str
    ipv4Addresses: _list[str]
    ipv6Addresses: _list[str]

@typing.type_check_only
class GoogleDomainsDns(typing.TypedDict, total=False):
    dsRecords: _list[DsRecord]
    dsState: typing.Literal[
        "DS_STATE_UNSPECIFIED", "DS_RECORDS_UNPUBLISHED", "DS_RECORDS_PUBLISHED"
    ]
    nameServers: _list[str]

@typing.type_check_only
class HealthCheckTargets(typing.TypedDict, total=False):
    externalEndpoints: _list[str]
    internalLoadBalancer: _list[LoadBalancerTarget]

@typing.type_check_only
class ImportDomainRequest(typing.TypedDict, total=False):
    domainName: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class InitiatePushTransferRequest(typing.TypedDict, total=False):
    tag: str
    validateOnly: bool

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListRegistrationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    registrations: _list[Registration]

@typing.type_check_only
class LoadBalancerTarget(typing.TypedDict, total=False):
    ipAddress: str
    ipProtocol: typing.Literal["UNDEFINED", "TCP", "UDP"]
    loadBalancerType: typing.Literal[
        "NONE", "GLOBAL_L7ILB", "REGIONAL_L4ILB", "REGIONAL_L7ILB"
    ]
    networkUrl: str
    port: str
    project: str
    region: str

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagementSettings(typing.TypedDict, total=False):
    effectiveTransferLockState: typing.Literal[
        "TRANSFER_LOCK_STATE_UNSPECIFIED", "UNLOCKED", "LOCKED"
    ]
    preferredRenewalMethod: typing.Literal[
        "RENEWAL_METHOD_UNSPECIFIED",
        "AUTOMATIC_RENEWAL",
        "MANUAL_RENEWAL",
        "RENEWAL_DISABLED",
    ]
    renewalMethod: typing.Literal[
        "RENEWAL_METHOD_UNSPECIFIED",
        "AUTOMATIC_RENEWAL",
        "MANUAL_RENEWAL",
        "RENEWAL_DISABLED",
    ]
    transferLockState: typing.Literal[
        "TRANSFER_LOCK_STATE_UNSPECIFIED", "UNLOCKED", "LOCKED"
    ]

@typing.type_check_only
class Money(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

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
class PrimaryBackupPolicy(typing.TypedDict, total=False):
    backupGeoTargets: GeoPolicy
    primaryTargets: HealthCheckTargets
    trickleTraffic: float

@typing.type_check_only
class RRSetRoutingPolicy(typing.TypedDict, total=False):
    geo: GeoPolicy
    geoPolicy: GeoPolicy
    healthCheck: str
    primaryBackup: PrimaryBackupPolicy
    wrr: WrrPolicy
    wrrPolicy: WrrPolicy

@typing.type_check_only
class RegisterDomainRequest(typing.TypedDict, total=False):
    contactNotices: _list[
        typing.Literal[
            "CONTACT_NOTICE_UNSPECIFIED", "PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT"
        ]
    ]
    domainNotices: _list[typing.Literal["DOMAIN_NOTICE_UNSPECIFIED", "HSTS_PRELOADED"]]
    registration: Registration
    validateOnly: bool
    yearlyPrice: Money

@typing.type_check_only
class RegisterParameters(typing.TypedDict, total=False):
    availability: typing.Literal[
        "AVAILABILITY_UNSPECIFIED", "AVAILABLE", "UNAVAILABLE", "UNSUPPORTED", "UNKNOWN"
    ]
    domainName: str
    domainNotices: _list[typing.Literal["DOMAIN_NOTICE_UNSPECIFIED", "HSTS_PRELOADED"]]
    supportedPrivacy: _list[
        typing.Literal[
            "CONTACT_PRIVACY_UNSPECIFIED",
            "PUBLIC_CONTACT_DATA",
            "PRIVATE_CONTACT_DATA",
            "REDACTED_CONTACT_DATA",
        ]
    ]
    yearlyPrice: Money

@typing.type_check_only
class Registration(typing.TypedDict, total=False):
    contactSettings: ContactSettings
    createTime: str
    dnsSettings: DnsSettings
    domainName: str
    domainProperties: _list[
        typing.Literal[
            "DOMAIN_PROPERTY_UNSPECIFIED",
            "TRANSFER_LOCK_UNSUPPORTED_BY_REGISTRY",
            "REQUIRE_PUSH_TRANSFER",
        ]
    ]
    expireTime: str
    issues: _list[
        typing.Literal[
            "ISSUE_UNSPECIFIED",
            "CONTACT_SUPPORT",
            "UNVERIFIED_EMAIL",
            "PROBLEM_WITH_BILLING",
            "DNS_NOT_ACTIVATED",
            "AUTO_RENEWAL_UPDATE_NOT_EFFECTIVE",
        ]
    ]
    labels: dict[str, typing.Any]
    managementSettings: ManagementSettings
    name: str
    pendingContactSettings: ContactSettings
    provider: typing.Literal["REGISTRAR_UNSPECIFIED", "GOOGLE_DOMAINS", "SQUARESPACE"]
    registerFailureReason: typing.Literal[
        "REGISTER_FAILURE_REASON_UNSPECIFIED",
        "REGISTER_FAILURE_REASON_UNKNOWN",
        "DOMAIN_NOT_AVAILABLE",
        "INVALID_CONTACTS",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REGISTRATION_PENDING",
        "REGISTRATION_FAILED",
        "TRANSFER_PENDING",
        "TRANSFER_FAILED",
        "IMPORT_PENDING",
        "ACTIVE",
        "SUSPENDED",
        "EXPORTED",
        "EXPIRED",
    ]
    supportedPrivacy: _list[
        typing.Literal[
            "CONTACT_PRIVACY_UNSPECIFIED",
            "PUBLIC_CONTACT_DATA",
            "PRIVATE_CONTACT_DATA",
            "REDACTED_CONTACT_DATA",
        ]
    ]
    transferFailureReason: typing.Literal[
        "TRANSFER_FAILURE_REASON_UNSPECIFIED",
        "TRANSFER_FAILURE_REASON_UNKNOWN",
        "EMAIL_CONFIRMATION_FAILURE",
        "DOMAIN_NOT_REGISTERED",
        "DOMAIN_HAS_TRANSFER_LOCK",
        "INVALID_AUTHORIZATION_CODE",
        "TRANSFER_CANCELLED",
        "TRANSFER_REJECTED",
        "INVALID_REGISTRANT_EMAIL_ADDRESS",
        "DOMAIN_NOT_ELIGIBLE_FOR_TRANSFER",
        "TRANSFER_ALREADY_PENDING",
    ]

@typing.type_check_only
class RenewDomainRequest(typing.TypedDict, total=False):
    validateOnly: bool
    yearlyPrice: Money

@typing.type_check_only
class ResetAuthorizationCodeRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResourceRecordSet(typing.TypedDict, total=False):
    name: str
    routingPolicy: RRSetRoutingPolicy
    rrdata: _list[str]
    signatureRrdata: _list[str]
    ttl: int
    type: str

@typing.type_check_only
class RetrieveGoogleDomainsDnsRecordsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rrset: _list[ResourceRecordSet]

@typing.type_check_only
class RetrieveGoogleDomainsForwardingConfigResponse(typing.TypedDict, total=False):
    domainForwardings: _list[DomainForwarding]
    emailForwardings: _list[EmailForwarding]

@typing.type_check_only
class RetrieveImportableDomainsResponse(typing.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class RetrieveRegisterParametersResponse(typing.TypedDict, total=False):
    registerParameters: RegisterParameters

@typing.type_check_only
class RetrieveTransferParametersResponse(typing.TypedDict, total=False):
    transferParameters: TransferParameters

@typing.type_check_only
class SearchDomainsResponse(typing.TypedDict, total=False):
    registerParameters: _list[RegisterParameters]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TransferDomainRequest(typing.TypedDict, total=False):
    authorizationCode: AuthorizationCode
    contactNotices: _list[
        typing.Literal[
            "CONTACT_NOTICE_UNSPECIFIED", "PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT"
        ]
    ]
    registration: Registration
    validateOnly: bool
    yearlyPrice: Money

@typing.type_check_only
class TransferParameters(typing.TypedDict, total=False):
    currentRegistrar: str
    currentRegistrarUri: str
    domainName: str
    nameServers: _list[str]
    supportedPrivacy: _list[
        typing.Literal[
            "CONTACT_PRIVACY_UNSPECIFIED",
            "PUBLIC_CONTACT_DATA",
            "PRIVATE_CONTACT_DATA",
            "REDACTED_CONTACT_DATA",
        ]
    ]
    transferLockState: typing.Literal[
        "TRANSFER_LOCK_STATE_UNSPECIFIED", "UNLOCKED", "LOCKED"
    ]
    yearlyPrice: Money

@typing.type_check_only
class WrrPolicy(typing.TypedDict, total=False):
    item: _list[WrrPolicyItem]

@typing.type_check_only
class WrrPolicyItem(typing.TypedDict, total=False):
    healthCheckedTargets: HealthCheckTargets
    rrdata: _list[str]
    signatureRrdata: _list[str]
    weight: float
