import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AuthorizationCode(typing_extensions.TypedDict, total=False):
    code: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class ConfigureContactSettingsRequest(typing_extensions.TypedDict, total=False):
    contactNotices: _list[str]
    contactSettings: ContactSettings
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class ConfigureDnsSettingsRequest(typing_extensions.TypedDict, total=False):
    dnsSettings: DnsSettings
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class ConfigureManagementSettingsRequest(typing_extensions.TypedDict, total=False):
    managementSettings: ManagementSettings
    updateMask: str

@typing.type_check_only
class Contact(typing_extensions.TypedDict, total=False):
    email: str
    faxNumber: str
    phoneNumber: str
    postalAddress: PostalAddress

@typing.type_check_only
class ContactSettings(typing_extensions.TypedDict, total=False):
    adminContact: Contact
    privacy: typing_extensions.Literal[
        "CONTACT_PRIVACY_UNSPECIFIED",
        "PUBLIC_CONTACT_DATA",
        "PRIVATE_CONTACT_DATA",
        "REDACTED_CONTACT_DATA",
    ]
    registrantContact: Contact
    technicalContact: Contact

@typing.type_check_only
class CustomDns(typing_extensions.TypedDict, total=False):
    dsRecords: _list[DsRecord]
    nameServers: _list[str]

@typing.type_check_only
class DnsSettings(typing_extensions.TypedDict, total=False):
    customDns: CustomDns
    glueRecords: _list[GlueRecord]
    googleDomainsDns: GoogleDomainsDns

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    domainName: str
    resourceState: typing_extensions.Literal[
        "RESOURCE_STATE_UNSPECIFIED",
        "IMPORTABLE",
        "UNSUPPORTED",
        "SUSPENDED",
        "EXPIRED",
        "DELETED",
    ]
    yearlyPrice: Money

@typing.type_check_only
class DsRecord(typing_extensions.TypedDict, total=False):
    algorithm: typing_extensions.Literal[
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
    digestType: typing_extensions.Literal[
        "DIGEST_TYPE_UNSPECIFIED", "SHA1", "SHA256", "GOST3411", "SHA384"
    ]
    keyTag: int

@typing.type_check_only
class ExportRegistrationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GlueRecord(typing_extensions.TypedDict, total=False):
    hostName: str
    ipv4Addresses: _list[str]
    ipv6Addresses: _list[str]

@typing.type_check_only
class GoogleDomainsDns(typing_extensions.TypedDict, total=False):
    dsRecords: _list[DsRecord]
    dsState: typing_extensions.Literal[
        "DS_STATE_UNSPECIFIED", "DS_RECORDS_UNPUBLISHED", "DS_RECORDS_PUBLISHED"
    ]
    nameServers: _list[str]

@typing.type_check_only
class ImportDomainRequest(typing_extensions.TypedDict, total=False):
    domainName: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListRegistrationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    registrations: _list[Registration]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManagementSettings(typing_extensions.TypedDict, total=False):
    renewalMethod: typing_extensions.Literal[
        "RENEWAL_METHOD_UNSPECIFIED", "AUTOMATIC_RENEWAL", "MANUAL_RENEWAL"
    ]
    transferLockState: typing_extensions.Literal[
        "TRANSFER_LOCK_STATE_UNSPECIFIED", "UNLOCKED", "LOCKED"
    ]

@typing.type_check_only
class Money(typing_extensions.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

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
class RegisterDomainRequest(typing_extensions.TypedDict, total=False):
    contactNotices: _list[str]
    domainNotices: _list[str]
    registration: Registration
    validateOnly: bool
    yearlyPrice: Money

@typing.type_check_only
class RegisterParameters(typing_extensions.TypedDict, total=False):
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED", "AVAILABLE", "UNAVAILABLE", "UNSUPPORTED", "UNKNOWN"
    ]
    domainName: str
    domainNotices: _list[str]
    supportedPrivacy: _list[str]
    yearlyPrice: Money

@typing.type_check_only
class Registration(typing_extensions.TypedDict, total=False):
    contactSettings: ContactSettings
    createTime: str
    dnsSettings: DnsSettings
    domainName: str
    expireTime: str
    issues: _list[str]
    labels: dict[str, typing.Any]
    managementSettings: ManagementSettings
    name: str
    pendingContactSettings: ContactSettings
    registerFailureReason: typing_extensions.Literal[
        "REGISTER_FAILURE_REASON_UNSPECIFIED",
        "REGISTER_FAILURE_REASON_UNKNOWN",
        "DOMAIN_NOT_AVAILABLE",
        "INVALID_CONTACTS",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REGISTRATION_PENDING",
        "REGISTRATION_FAILED",
        "TRANSFER_PENDING",
        "TRANSFER_FAILED",
        "IMPORT_PENDING",
        "ACTIVE",
        "SUSPENDED",
        "EXPORTED",
    ]
    supportedPrivacy: _list[str]
    transferFailureReason: typing_extensions.Literal[
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
class ResetAuthorizationCodeRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetrieveImportableDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class RetrieveRegisterParametersResponse(typing_extensions.TypedDict, total=False):
    registerParameters: RegisterParameters

@typing.type_check_only
class RetrieveTransferParametersResponse(typing_extensions.TypedDict, total=False):
    transferParameters: TransferParameters

@typing.type_check_only
class SearchDomainsResponse(typing_extensions.TypedDict, total=False):
    registerParameters: _list[RegisterParameters]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TransferDomainRequest(typing_extensions.TypedDict, total=False):
    authorizationCode: AuthorizationCode
    contactNotices: _list[str]
    registration: Registration
    validateOnly: bool
    yearlyPrice: Money

@typing.type_check_only
class TransferParameters(typing_extensions.TypedDict, total=False):
    currentRegistrar: str
    currentRegistrarUri: str
    domainName: str
    nameServers: _list[str]
    supportedPrivacy: _list[str]
    transferLockState: typing_extensions.Literal[
        "TRANSFER_LOCK_STATE_UNSPECIFIED", "UNLOCKED", "LOCKED"
    ]
    yearlyPrice: Money
