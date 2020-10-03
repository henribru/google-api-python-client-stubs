import typing

import typing_extensions

class DomainRedirect(typing_extensions.TypedDict, total=False):
    domainName: str
    type: typing_extensions.Literal["REDIRECT_TYPE_UNSPECIFIED", "MOVED_PERMANENTLY"]

class PopulateVersionFilesRequest(typing_extensions.TypedDict, total=False):
    files: typing.Dict[str, typing.Any]

class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: typing.List[Release]

class Header(typing_extensions.TypedDict, total=False):
    regex: str
    headers: typing.Dict[str, typing.Any]
    glob: str

class Release(typing_extensions.TypedDict, total=False):
    releaseUser: ActingUser
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "DEPLOY", "ROLLBACK", "SITE_DISABLE"
    ]
    version: Version
    releaseTime: str
    message: str
    name: str

class PreviewConfig(typing_extensions.TypedDict, total=False):
    expireTime: str
    active: bool

class ListDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[Domain]

class Channel(typing_extensions.TypedDict, total=False):
    createTime: str
    ttl: str
    expireTime: str
    name: str
    release: Release
    retainedReleaseCount: int
    labels: typing.Dict[str, typing.Any]
    updateTime: str
    url: str

class PopulateVersionFilesResponse(typing_extensions.TypedDict, total=False):
    uploadRequiredHashes: typing.List[str]
    uploadUrl: str

class Rewrite(typing_extensions.TypedDict, total=False):
    dynamicLinks: bool
    run: CloudRunRewrite
    function: str
    glob: str
    path: str
    regex: str

class VersionFile(typing_extensions.TypedDict, total=False):
    hash: str
    path: str
    status: typing_extensions.Literal["STATUS_UNSPECIFIED", "EXPECTED", "ACTIVE"]

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class ListChannelsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    channels: typing.List[Channel]

class SiteConfig(typing_extensions.TypedDict, total=False):
    maxVersions: str
    cloudLoggingEnabled: bool

class Empty(typing_extensions.TypedDict, total=False): ...

class PathFilter(typing_extensions.TypedDict, total=False):
    regexes: typing.List[str]

class ActingUser(typing_extensions.TypedDict, total=False):
    email: str
    imageUrl: str

class CloudRunRewrite(typing_extensions.TypedDict, total=False):
    serviceId: str
    region: str

class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[Version]
    nextPageToken: str

class Version(typing_extensions.TypedDict, total=False):
    fileCount: str
    versionBytes: str
    finalizeTime: str
    config: ServingConfig
    labels: typing.Dict[str, typing.Any]
    status: typing_extensions.Literal[
        "VERSION_STATUS_UNSPECIFIED",
        "CREATED",
        "FINALIZED",
        "DELETED",
        "ABANDONED",
        "EXPIRED",
        "CLONING",
    ]
    createUser: ActingUser
    finalizeUser: ActingUser
    deleteUser: ActingUser
    createTime: str
    preview: PreviewConfig
    deleteTime: str
    name: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class Domain(typing_extensions.TypedDict, total=False):
    status: typing_extensions.Literal[
        "DOMAIN_STATUS_UNSPECIFIED",
        "DOMAIN_CHANGE_PENDING",
        "DOMAIN_ACTIVE",
        "DOMAIN_VERIFICATION_REQUIRED",
        "DOMAIN_VERIFICATION_LOST",
    ]
    updateTime: str
    site: str
    domainRedirect: DomainRedirect
    domainName: str
    provisioning: DomainProvisioning

class CertHttpChallenge(typing_extensions.TypedDict, total=False):
    token: str
    path: str

class ServingConfig(typing_extensions.TypedDict, total=False):
    cleanUrls: bool
    redirects: typing.List[Redirect]
    rewrites: typing.List[Rewrite]
    i18n: I18nConfig
    trailingSlashBehavior: typing_extensions.Literal[
        "TRAILING_SLASH_BEHAVIOR_UNSPECIFIED", "ADD", "REMOVE"
    ]
    appAssociation: typing_extensions.Literal["AUTO", "NONE"]
    headers: typing.List[Header]

class CloneVersionRequest(typing_extensions.TypedDict, total=False):
    sourceVersion: str
    finalize: bool
    exclude: PathFilter
    include: PathFilter

class DomainProvisioning(typing_extensions.TypedDict, total=False):
    certChallengeDns: CertDnsChallenge
    discoveredIps: typing.List[str]
    dnsFetchTime: str
    expectedIps: typing.List[str]
    certChallengeHttp: CertHttpChallenge
    certChallengeDiscoveredTxt: typing.List[str]
    dnsStatus: typing_extensions.Literal[
        "DNS_STATUS_UNSPECIFIED",
        "DNS_PENDING",
        "DNS_MISSING",
        "DNS_PARTIAL_MATCH",
        "DNS_MATCH",
        "DNS_EXTRANEOUS_MATCH",
    ]
    certStatus: typing_extensions.Literal[
        "CERT_STATUS_UNSPECIFIED",
        "CERT_PENDING",
        "CERT_MISSING",
        "CERT_PROCESSING",
        "CERT_PROPAGATING",
        "CERT_ACTIVE",
        "CERT_ERROR",
    ]

class ListVersionFilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    files: typing.List[VersionFile]

class I18nConfig(typing_extensions.TypedDict, total=False):
    root: str

class CertDnsChallenge(typing_extensions.TypedDict, total=False):
    domainName: str
    token: str

class Redirect(typing_extensions.TypedDict, total=False):
    glob: str
    location: str
    regex: str
    statusCode: int
