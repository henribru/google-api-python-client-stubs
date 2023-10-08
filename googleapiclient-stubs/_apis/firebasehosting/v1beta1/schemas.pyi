import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActingUser(typing_extensions.TypedDict, total=False):
    email: str
    imageUrl: str

@typing.type_check_only
class CertDnsChallenge(typing_extensions.TypedDict, total=False):
    domainName: str
    token: str

@typing.type_check_only
class CertHttpChallenge(typing_extensions.TypedDict, total=False):
    path: str
    token: str

@typing.type_check_only
class CertVerification(typing_extensions.TypedDict, total=False):
    dns: DnsUpdates
    http: HttpUpdate

@typing.type_check_only
class Certificate(typing_extensions.TypedDict, total=False):
    createTime: str
    expireTime: str
    issues: _list[Status]
    state: typing_extensions.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TEMPORARY", "GROUPED", "PROJECT_GROUPED", "DEDICATED"
    ]
    verification: CertVerification

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    createTime: str
    expireTime: str
    labels: dict[str, typing.Any]
    name: str
    release: Release
    retainedReleaseCount: int
    ttl: str
    updateTime: str
    url: str

@typing.type_check_only
class CloneVersionRequest(typing_extensions.TypedDict, total=False):
    exclude: PathFilter
    finalize: bool
    include: PathFilter
    sourceVersion: str

@typing.type_check_only
class CloudRunRewrite(typing_extensions.TypedDict, total=False):
    region: str
    serviceId: str
    tag: str

@typing.type_check_only
class CustomDomain(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    cert: Certificate
    certPreference: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TEMPORARY", "GROUPED", "PROJECT_GROUPED", "DEDICATED"
    ]
    createTime: str
    deleteTime: str
    etag: str
    expireTime: str
    hostState: typing_extensions.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_MISMATCH",
        "HOST_CONFLICT",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    labels: dict[str, typing.Any]
    name: str
    ownershipState: typing_extensions.Literal[
        "OWNERSHIP_STATE_UNSPECIFIED",
        "OWNERSHIP_MISSING",
        "OWNERSHIP_UNREACHABLE",
        "OWNERSHIP_MISMATCH",
        "OWNERSHIP_CONFLICT",
        "OWNERSHIP_PENDING",
        "OWNERSHIP_ACTIVE",
    ]
    reconciling: bool
    redirectTarget: str
    requiredDnsUpdates: DnsUpdates
    updateTime: str

@typing.type_check_only
class CustomDomainMetadata(typing_extensions.TypedDict, total=False):
    certState: typing_extensions.Literal[
        "CERT_STATE_UNSPECIFIED",
        "CERT_PREPARING",
        "CERT_VALIDATING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_EXPIRING_SOON",
        "CERT_EXPIRED",
    ]
    hostState: typing_extensions.Literal[
        "HOST_STATE_UNSPECIFIED",
        "HOST_UNHOSTED",
        "HOST_UNREACHABLE",
        "HOST_MISMATCH",
        "HOST_CONFLICT",
        "HOST_ACTIVE",
    ]
    issues: _list[Status]
    liveMigrationSteps: _list[LiveMigrationStep]
    ownershipState: typing_extensions.Literal[
        "OWNERSHIP_STATE_UNSPECIFIED",
        "OWNERSHIP_MISSING",
        "OWNERSHIP_UNREACHABLE",
        "OWNERSHIP_MISMATCH",
        "OWNERSHIP_CONFLICT",
        "OWNERSHIP_PENDING",
        "OWNERSHIP_ACTIVE",
    ]
    quickSetupUpdates: DnsUpdates

@typing.type_check_only
class DnsRecord(typing_extensions.TypedDict, total=False):
    domainName: str
    rdata: str
    requiredAction: typing_extensions.Literal["NONE", "ADD", "REMOVE"]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "A", "CNAME", "TXT", "AAAA", "CAA"
    ]

@typing.type_check_only
class DnsRecordSet(typing_extensions.TypedDict, total=False):
    checkError: Status
    domainName: str
    records: _list[DnsRecord]

@typing.type_check_only
class DnsUpdates(typing_extensions.TypedDict, total=False):
    checkTime: str
    desired: _list[DnsRecordSet]
    discovered: _list[DnsRecordSet]

@typing.type_check_only
class Domain(typing_extensions.TypedDict, total=False):
    domainName: str
    domainRedirect: DomainRedirect
    provisioning: DomainProvisioning
    site: str
    status: typing_extensions.Literal[
        "DOMAIN_STATUS_UNSPECIFIED",
        "DOMAIN_CHANGE_PENDING",
        "DOMAIN_ACTIVE",
        "DOMAIN_VERIFICATION_REQUIRED",
        "DOMAIN_VERIFICATION_LOST",
    ]
    updateTime: str

@typing.type_check_only
class DomainProvisioning(typing_extensions.TypedDict, total=False):
    certChallengeDiscoveredTxt: _list[str]
    certChallengeDns: CertDnsChallenge
    certChallengeHttp: CertHttpChallenge
    certStatus: typing_extensions.Literal[
        "CERT_STATUS_UNSPECIFIED",
        "CERT_PENDING",
        "CERT_MISSING",
        "CERT_PROCESSING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_ERROR",
    ]
    discoveredIps: _list[str]
    dnsFetchTime: str
    dnsStatus: typing_extensions.Literal[
        "DNS_STATUS_UNSPECIFIED",
        "DNS_PENDING",
        "DNS_MISSING",
        "DNS_PARTIAL_MATCH",
        "DNS_MATCH",
        "DNS_EXTRANEOUS_MATCH",
    ]
    expectedIps: _list[str]

@typing.type_check_only
class DomainRedirect(typing_extensions.TypedDict, total=False):
    domainName: str
    type: typing_extensions.Literal["REDIRECT_TYPE_UNSPECIFIED", "MOVED_PERMANENTLY"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Header(typing_extensions.TypedDict, total=False):
    glob: str
    headers: dict[str, typing.Any]
    regex: str

@typing.type_check_only
class HttpUpdate(typing_extensions.TypedDict, total=False):
    checkError: Status
    desired: str
    discovered: str
    lastCheckTime: str
    path: str

@typing.type_check_only
class I18nConfig(typing_extensions.TypedDict, total=False):
    root: str

@typing.type_check_only
class ListChannelsResponse(typing_extensions.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str

@typing.type_check_only
class ListCustomDomainsResponse(typing_extensions.TypedDict, total=False):
    customDomains: _list[CustomDomain]
    nextPageToken: str

@typing.type_check_only
class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[Domain]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]

@typing.type_check_only
class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class ListVersionFilesResponse(typing_extensions.TypedDict, total=False):
    files: _list[VersionFile]
    nextPageToken: str

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class LiveMigrationStep(typing_extensions.TypedDict, total=False):
    certVerification: CertVerification
    dnsUpdates: DnsUpdates
    issues: _list[Status]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "PREPARING",
        "PENDING",
        "INCOMPLETE",
        "PROCESSING",
        "COMPLETE",
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PathFilter(typing_extensions.TypedDict, total=False):
    regexes: _list[str]

@typing.type_check_only
class PopulateVersionFilesRequest(typing_extensions.TypedDict, total=False):
    files: dict[str, typing.Any]

@typing.type_check_only
class PopulateVersionFilesResponse(typing_extensions.TypedDict, total=False):
    uploadRequiredHashes: _list[str]
    uploadUrl: str

@typing.type_check_only
class Redirect(typing_extensions.TypedDict, total=False):
    glob: str
    location: str
    regex: str
    statusCode: int

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    message: str
    name: str
    releaseTime: str
    releaseUser: ActingUser
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "DEPLOY", "ROLLBACK", "SITE_DISABLE"
    ]
    version: Version

@typing.type_check_only
class Rewrite(typing_extensions.TypedDict, total=False):
    dynamicLinks: bool
    function: str
    functionRegion: str
    glob: str
    path: str
    regex: str
    run: CloudRunRewrite

@typing.type_check_only
class ServingConfig(typing_extensions.TypedDict, total=False):
    appAssociation: typing_extensions.Literal["AUTO", "NONE"]
    cleanUrls: bool
    headers: _list[Header]
    i18n: I18nConfig
    redirects: _list[Redirect]
    rewrites: _list[Rewrite]
    trailingSlashBehavior: typing_extensions.Literal[
        "TRAILING_SLASH_BEHAVIOR_UNSPECIFIED", "ADD", "REMOVE"
    ]

@typing.type_check_only
class Site(typing_extensions.TypedDict, total=False):
    appId: str
    defaultUrl: str
    labels: dict[str, typing.Any]
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DEFAULT_SITE", "USER_SITE"]

@typing.type_check_only
class SiteConfig(typing_extensions.TypedDict, total=False):
    cloudLoggingEnabled: bool
    maxVersions: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UndeleteCustomDomainRequest(typing_extensions.TypedDict, total=False):
    etag: str
    validateOnly: bool

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    config: ServingConfig
    createTime: str
    createUser: ActingUser
    deleteTime: str
    deleteUser: ActingUser
    fileCount: str
    finalizeTime: str
    finalizeUser: ActingUser
    labels: dict[str, typing.Any]
    name: str
    status: typing_extensions.Literal[
        "VERSION_STATUS_UNSPECIFIED",
        "CREATED",
        "FINALIZED",
        "DELETED",
        "ABANDONED",
        "EXPIRED",
        "CLONING",
    ]
    versionBytes: str

@typing.type_check_only
class VersionFile(typing_extensions.TypedDict, total=False):
    hash: str
    path: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "EXPECTED", "ACTIVE"]
