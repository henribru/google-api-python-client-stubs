import typing

import typing_extensions

_list = list

@typing.type_check_only
class AffectedSoftware(typing_extensions.TypedDict, total=False):
    product: str
    vendor: str

@typing.type_check_only
class Alert(typing_extensions.TypedDict, total=False):
    aiSummary: str
    assets: _list[str]
    audit: Audit
    configurations: _list[str]
    detail: AlertDetail
    displayName: str
    duplicateOf: str
    duplicatedBy: _list[str]
    etag: str
    externalId: str
    findingCount: str
    findings: _list[str]
    name: str
    priorityAnalysis: PriorityAnalysis
    relevanceAnalysis: RelevanceAnalysis
    severityAnalysis: SeverityAnalysis
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NEW",
        "READ",
        "TRIAGED",
        "ESCALATED",
        "RESOLVED",
        "DUPLICATE",
        "FALSE_POSITIVE",
        "NOT_ACTIONABLE",
        "BENIGN",
        "TRACKED_EXTERNALLY",
    ]

@typing.type_check_only
class AlertDetail(typing_extensions.TypedDict, total=False):
    dataLeak: DataLeakAlertDetail
    detailType: str
    initialAccessBroker: InitialAccessBrokerAlertDetail
    insiderThreat: InsiderThreatAlertDetail
    suspiciousDomain: SuspiciousDomainAlertDetail
    targetTechnology: TargetTechnologyAlertDetail

@typing.type_check_only
class AlertDocument(typing_extensions.TypedDict, total=False):
    aiSummary: str
    author: str
    collectionTime: str
    content: str
    createTime: str
    ingestTime: str
    languageCode: str
    name: str
    source: str
    sourceUpdateTime: str
    sourceUri: str
    title: str
    translation: AlertDocumentTranslation

@typing.type_check_only
class AlertDocumentTranslation(typing_extensions.TypedDict, total=False):
    translatedContent: str
    translatedTitle: str

@typing.type_check_only
class AssetDiscoveryConfig(typing_extensions.TypedDict, total=False):
    lastScanCompleteTime: str
    lastScanStartTime: str
    scanFrequency: typing_extensions.Literal[
        "ASSET_DISCOVERY_SCAN_FREQUENCY_UNSPECIFIED",
        "ON_DEMAND",
        "WEEKLY",
        "DAILY",
        "MONTHLY",
    ]
    scopeExclusionAssets: _list[AssetDiscoverySeed]
    seedAssets: _list[AssetDiscoverySeed]
    workflow: typing_extensions.Literal[
        "ASSET_DISCOVERY_WORKFLOW_UNSPECIFIED",
        "EXTERNAL_DISCOVERY",
        "EXTERNAL_DISCOVERY_AND_ASSESSMENT",
        "MOBILE_APP_DISCOVERY",
    ]

@typing.type_check_only
class AssetDiscoverySeed(typing_extensions.TypedDict, total=False):
    seedType: typing_extensions.Literal[
        "ASSET_DISCOVERY_SEED_TYPE_UNSPECIFIED", "IP_ADDRESS", "NETWORK_SERVICE"
    ]
    seedValue: str

@typing.type_check_only
class Association(typing_extensions.TypedDict, total=False):
    id: str
    type: typing_extensions.Literal[
        "THREAT_INTEL_OBJECT_TYPE_UNSPECIFIED",
        "THREAT_INTEL_OBJECT_TYPE_THREAT_ACTOR",
        "THREAT_INTEL_OBJECT_TYPE_MALWARE",
        "THREAT_INTEL_OBJECT_TYPE_REPORT",
        "THREAT_INTEL_OBJECT_TYPE_CAMPAIGN",
        "THREAT_INTEL_OBJECT_TYPE_IOC_COLLECTION",
        "THREAT_INTEL_OBJECT_TYPE_SOFTWARE_AND_TOOLKITS",
        "THREAT_INTEL_OBJECT_TYPE_VULNERABILITY",
    ]

@typing.type_check_only
class Audit(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    updateTime: str
    updater: str

@typing.type_check_only
class CompromisedCredentialsFindingDetail(typing_extensions.TypedDict, total=False):
    author: str
    credentialService: str
    darkWebDoc: str
    externalReferenceUri: str
    fileDump: str
    fileDumpHashes: _list[str]
    fileDumpSizeBytes: str
    forum: str
    malwareFamily: str
    postedTime: str
    sourceUri: str
    userKey: str
    userSecretEvidence: str

@typing.type_check_only
class Configuration(typing_extensions.TypedDict, total=False):
    audit: Audit
    description: str
    detail: ConfigurationDetail
    displayName: str
    name: str
    provider: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DEPRECATED"
    ]
    version: str

@typing.type_check_only
class ConfigurationDetail(typing_extensions.TypedDict, total=False):
    assetDiscovery: AssetDiscoveryConfig
    customerProfile: CustomerProfileConfig
    detailType: str
    domainMonitoring: DomainMonitoringConfig
    initialAccessBroker: InitialAccessBrokerConfig
    technologyWatchlist: TechnologyWatchListConfig

@typing.type_check_only
class ConfigurationRevision(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    snapshot: Configuration

@typing.type_check_only
class CustomerProfileCitation(typing_extensions.TypedDict, total=False):
    citationId: str
    document: str
    retrievalTime: str
    source: str
    uri: str

@typing.type_check_only
class CustomerProfileCitedString(typing_extensions.TypedDict, total=False):
    citationIds: _list[str]
    value: str

@typing.type_check_only
class CustomerProfileCompany(typing_extensions.TypedDict, total=False):
    citationIds: _list[str]
    company: str

@typing.type_check_only
class CustomerProfileConfig(typing_extensions.TypedDict, total=False):
    citations: _list[CustomerProfileCitation]
    contactInfo: _list[CustomerProfileContactInfo]
    executives: _list[CustomerProfilePerson]
    industries: _list[CustomerProfileIndustry]
    locations: _list[CustomerProfileLocation]
    org: str
    orgSummary: str
    parentCompanies: _list[CustomerProfileCompany]
    products: _list[CustomerProfileProduct]
    securityConsiderations: CustomerProfileSecurityConsiderations
    summary: CustomerProfileSummary
    technologyPresence: str
    webPresences: _list[CustomerProfileWebPresence]

@typing.type_check_only
class CustomerProfileContactInfo(typing_extensions.TypedDict, total=False):
    address: str
    citationIds: _list[str]
    email: str
    label: str
    other: str
    phone: str

@typing.type_check_only
class CustomerProfileIndustry(typing_extensions.TypedDict, total=False):
    citationIds: _list[str]
    industry: str

@typing.type_check_only
class CustomerProfileLocation(typing_extensions.TypedDict, total=False):
    address: str
    brand: str
    citationIds: _list[str]
    facilityType: str

@typing.type_check_only
class CustomerProfilePerson(typing_extensions.TypedDict, total=False):
    citationIds: _list[str]
    name: str
    title: str

@typing.type_check_only
class CustomerProfileProduct(typing_extensions.TypedDict, total=False):
    brand: str
    citationIds: _list[str]
    product: str

@typing.type_check_only
class CustomerProfileSecurityConsiderations(typing_extensions.TypedDict, total=False):
    considerations: _list[str]
    note: str

@typing.type_check_only
class CustomerProfileSummary(typing_extensions.TypedDict, total=False):
    areaServed: CustomerProfileCitedString
    brands: CustomerProfileCitedString
    entityType: CustomerProfileCitedString
    founded: CustomerProfileCitedString
    headquarters: CustomerProfileCitedString
    industry: CustomerProfileCitedString
    keyPeopleSummary: CustomerProfileCitedString
    parentCompany: CustomerProfileCitedString
    primaryWebsite: CustomerProfileCitedString
    productsSummary: CustomerProfileCitedString
    servicesSummary: CustomerProfileCitedString
    title: CustomerProfileCitedString

@typing.type_check_only
class CustomerProfileWebPresence(typing_extensions.TypedDict, total=False):
    citationIds: _list[str]
    domain: str

@typing.type_check_only
class DataLeakAlertDetail(typing_extensions.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class DataLeakFindingDetail(typing_extensions.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class DomainMonitoringConfig(typing_extensions.TypedDict, total=False):
    domains: _list[DomainMonitoringDomain]

@typing.type_check_only
class DomainMonitoringDomain(typing_extensions.TypedDict, total=False):
    domain: str

@typing.type_check_only
class EntityProfile(typing_extensions.TypedDict, total=False):
    countries: _list[str]
    domains: _list[str]
    industries: _list[str]
    name: str
    operationalAreas: _list[str]
    profileSummary: str
    regions: _list[str]
    subIndustries: _list[str]

@typing.type_check_only
class EnumerateAlertFacetsResponse(typing_extensions.TypedDict, total=False):
    facets: _list[Facet]

@typing.type_check_only
class Evidence(typing_extensions.TypedDict, total=False):
    commonThemes: _list[str]
    distinctThemes: _list[str]

@typing.type_check_only
class Facet(typing_extensions.TypedDict, total=False):
    facet: str
    facetCounts: _list[FacetCount]
    facetType: str
    maxValue: str
    minValue: str
    totalCount: str

@typing.type_check_only
class FacetCount(typing_extensions.TypedDict, total=False):
    count: int
    value: str

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    aiSummary: str
    alert: str
    asset: str
    audit: Audit
    configurations: _list[str]
    detail: FindingDetail
    displayName: str
    issue: str
    name: str
    provider: str
    relevanceAnalysis: RelevanceAnalysis
    reoccurrenceTimes: _list[str]
    severity: float
    severityAnalysis: SeverityAnalysis

@typing.type_check_only
class FindingDetail(typing_extensions.TypedDict, total=False):
    compromisedCredentials: CompromisedCredentialsFindingDetail
    dataLeak: DataLeakFindingDetail
    detailType: str
    inbandVulnerability: InbandVulnerabilityFindingDetail
    initialAccessBroker: InitialAccessBrokerFindingDetail
    insiderThreat: InsiderThreatFindingDetail
    misconfiguration: MisconfigurationFindingDetail
    suspiciousDomain: SuspiciousDomainFindingDetail
    targetTechnology: TargetTechnologyFindingDetail

@typing.type_check_only
class GenerateOrgProfileConfigurationRequest(typing_extensions.TypedDict, total=False):
    displayName: str
    domain: str

@typing.type_check_only
class InbandVulnerability(typing_extensions.TypedDict, total=False):
    affectedSoftware: _list[AffectedSoftware]
    authors: _list[str]
    cveId: str
    cvssV31Score: float
    cvssV31ScoreTemporal: float
    description: str
    disclosureTime: str
    exploitationState: str
    externalVulnerabilityId: str
    isExploitedWild: bool
    referenceUrls: _list[str]
    remediation: str
    riskRating: str
    title: str

@typing.type_check_only
class InbandVulnerabilityFindingDetail(typing_extensions.TypedDict, total=False):
    formattedProofDetails: str
    requestUri: str
    vulnerability: InbandVulnerability

@typing.type_check_only
class InitialAccessBrokerAlertDetail(typing_extensions.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class InitialAccessBrokerConfig(typing_extensions.TypedDict, total=False):
    entityProfile: EntityProfile

@typing.type_check_only
class InitialAccessBrokerFindingDetail(typing_extensions.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class InsiderThreatAlertDetail(typing_extensions.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class InsiderThreatFindingDetail(typing_extensions.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    alerts: _list[Alert]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[ConfigurationRevision]

@typing.type_check_only
class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    configurations: _list[Configuration]
    nextPageToken: str

@typing.type_check_only
class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class MarkAlertAsBenignRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsDuplicateRequest(typing_extensions.TypedDict, total=False):
    duplicateOf: str

@typing.type_check_only
class MarkAlertAsEscalatedRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsFalsePositiveRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsNotActionableRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsReadRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsResolvedRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsTrackedExternallyRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsTriagedRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class MisconfigurationFindingDetail(typing_extensions.TypedDict, total=False):
    misconfigurationMetadata: MisconfigurationMetadata

@typing.type_check_only
class MisconfigurationMetadata(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    misconfigurationId: str
    references: _list[MisconfigurationReference]
    remediation: str
    vulnerableUri: str

@typing.type_check_only
class MisconfigurationReference(typing_extensions.TypedDict, total=False):
    type: str
    uri: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PriorityAnalysis(typing_extensions.TypedDict, total=False):
    confidence: typing_extensions.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    priorityLevel: typing_extensions.Literal[
        "PRIORITY_LEVEL_UNSPECIFIED",
        "PRIORITY_LEVEL_LOW",
        "PRIORITY_LEVEL_MEDIUM",
        "PRIORITY_LEVEL_HIGH",
        "PRIORITY_LEVEL_CRITICAL",
    ]
    reasoning: str

@typing.type_check_only
class RefreshAlertUriStatusRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RefreshAlertUriStatusResponse(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_UNSPECIFIED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_NOT_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_PROCESSING",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_ADDED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_REJECTED",
    ]

@typing.type_check_only
class RelevanceAnalysis(typing_extensions.TypedDict, total=False):
    confidence: typing_extensions.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    evidence: Evidence
    reasoning: str
    relevanceLevel: typing_extensions.Literal[
        "RELEVANCE_LEVEL_UNSPECIFIED",
        "RELEVANCE_LEVEL_LOW",
        "RELEVANCE_LEVEL_MEDIUM",
        "RELEVANCE_LEVEL_HIGH",
    ]
    relevant: bool

@typing.type_check_only
class ReportAlertUriRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReportAlertUriResponse(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_UNSPECIFIED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_NOT_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_PROCESSING",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_ADDED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_REJECTED",
    ]

@typing.type_check_only
class SearchFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class SeverityAnalysis(typing_extensions.TypedDict, total=False):
    confidence: typing_extensions.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    reasoning: str
    severityLevel: typing_extensions.Literal[
        "SEVERITY_LEVEL_UNSPECIFIED",
        "SEVERITY_LEVEL_LOW",
        "SEVERITY_LEVEL_MEDIUM",
        "SEVERITY_LEVEL_HIGH",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SuspiciousDomainAlertDetail(typing_extensions.TypedDict, total=False):
    dns: SuspiciousDomainDnsDetails
    domain: str
    gtiDetails: SuspiciousDomainGtiDetails
    webRiskOperation: str
    webRiskState: typing_extensions.Literal[
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_UNSPECIFIED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_NOT_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_SUBMITTED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_PROCESSING",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_ADDED",
        "SUSPICIOUS_DOMAIN_WEB_RISK_STATE_REJECTED",
    ]
    whois: SuspiciousDomainWhoIsDetails

@typing.type_check_only
class SuspiciousDomainDnsDetails(typing_extensions.TypedDict, total=False):
    dnsRecords: _list[SuspiciousDomainDnsRecord]
    retrievalTime: str

@typing.type_check_only
class SuspiciousDomainDnsRecord(typing_extensions.TypedDict, total=False):
    record: str
    ttl: int
    type: str
    value: str

@typing.type_check_only
class SuspiciousDomainFindingDetail(typing_extensions.TypedDict, total=False):
    dns: SuspiciousDomainDnsDetails
    domain: str
    gtiDetails: SuspiciousDomainGtiDetails
    matchScore: float
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]
    whois: SuspiciousDomainWhoIsDetails

@typing.type_check_only
class SuspiciousDomainGtiDetails(typing_extensions.TypedDict, total=False):
    threatScore: int
    verdict: typing_extensions.Literal[
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_UNSPECIFIED",
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_BENIGN",
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_UNDETECTED",
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_SUSPICIOUS",
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_MALICIOUS",
        "SUSPICIOUS_DOMAIN_GTI_VERDICT_UNKNOWN",
    ]
    virustotalUri: str

@typing.type_check_only
class SuspiciousDomainWhoIsDetails(typing_extensions.TypedDict, total=False):
    retrievalTime: str
    whois: str

@typing.type_check_only
class TargetTechnologyAlertDetail(typing_extensions.TypedDict, total=False):
    vulnerabilityMatch: VulnerabilityMatch

@typing.type_check_only
class TargetTechnologyFindingDetail(typing_extensions.TypedDict, total=False):
    vulnerabilityMatch: VulnerabilityMatch

@typing.type_check_only
class TechnologyWatchListAlertThreshold(typing_extensions.TypedDict, total=False):
    cvssScoreMinimum: float
    epssScoreMinimum: float
    exploitationStates: _list[
        typing_extensions.Literal[
            "EXPLOITATION_STATE_UNSPECIFIED",
            "EXPLOITATION_STATE_NO_KNOWN",
            "EXPLOITATION_STATE_REPORTED",
            "EXPLOITATION_STATE_SUSPECTED",
            "EXPLOITATION_STATE_CONFIRMED",
            "EXPLOITATION_STATE_WIDESPREAD",
        ]
    ]
    priorityMinimum: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "P0", "P1", "P2", "P3", "P4"
    ]

@typing.type_check_only
class TechnologyWatchListConfig(typing_extensions.TypedDict, total=False):
    alertThreshold: TechnologyWatchListAlertThreshold
    technologies: _list[str]

@typing.type_check_only
class UpsertConfigurationResponse(typing_extensions.TypedDict, total=False):
    configuration: str

@typing.type_check_only
class VulnerabilityMatch(typing_extensions.TypedDict, total=False):
    associations: _list[Association]
    collectionId: str
    cveId: str
    cvss3Score: float
    description: str
    exploitationState: typing_extensions.Literal[
        "EXPLOITATION_STATE_UNSPECIFIED",
        "EXPLOITATION_STATE_NO_KNOWN",
        "EXPLOITATION_STATE_REPORTED",
        "EXPLOITATION_STATE_SUSPECTED",
        "EXPLOITATION_STATE_CONFIRMED",
        "EXPLOITATION_STATE_WIDESPREAD",
    ]
    riskRating: typing_extensions.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNRATED"
    ]
    technologies: _list[str]
