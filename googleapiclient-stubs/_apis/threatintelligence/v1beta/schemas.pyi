import typing

_list = list

@typing.type_check_only
class Alert(typing.TypedDict, total=False):
    aiSummary: str
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
    state: typing.Literal[
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
class AlertDetail(typing.TypedDict, total=False):
    dataLeak: DataLeakAlertDetail
    detailType: str
    initialAccessBroker: InitialAccessBrokerAlertDetail
    insiderThreat: InsiderThreatAlertDetail
    targetTechnology: TargetTechnologyAlertDetail

@typing.type_check_only
class AlertDocument(typing.TypedDict, total=False):
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
class AlertDocumentTranslation(typing.TypedDict, total=False):
    translatedContent: str
    translatedTitle: str

@typing.type_check_only
class Association(typing.TypedDict, total=False):
    id: str
    type: typing.Literal[
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
class Audit(typing.TypedDict, total=False):
    createTime: str
    creator: str
    updateTime: str
    updater: str

@typing.type_check_only
class Configuration(typing.TypedDict, total=False):
    audit: Audit
    description: str
    detail: ConfigurationDetail
    displayName: str
    etag: str
    name: str
    provider: str
    state: typing.Literal["STATE_UNSPECIFIED", "ENABLED", "DISABLED", "DEPRECATED"]
    version: str

@typing.type_check_only
class ConfigurationDetail(typing.TypedDict, total=False):
    customThreatScenario: CustomThreatScenarioConfig
    customerProfile: CustomerProfileConfig
    detailType: str
    technologyWatchlist: TechnologyWatchListConfig

@typing.type_check_only
class ConfigurationRevision(typing.TypedDict, total=False):
    createTime: str
    name: str
    snapshot: Configuration

@typing.type_check_only
class CustomThreatScenarioConfig(typing.TypedDict, total=False):
    documentCondition: str

@typing.type_check_only
class CustomerProfileCitation(typing.TypedDict, total=False):
    citationId: str
    document: str
    retrievalTime: str
    source: str
    uri: str

@typing.type_check_only
class CustomerProfileCitedString(typing.TypedDict, total=False):
    citationIds: _list[str]
    value: str

@typing.type_check_only
class CustomerProfileCompany(typing.TypedDict, total=False):
    citationIds: _list[str]
    company: str

@typing.type_check_only
class CustomerProfileConfig(typing.TypedDict, total=False):
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
class CustomerProfileContactInfo(typing.TypedDict, total=False):
    address: str
    citationIds: _list[str]
    email: str
    label: str
    other: str
    phone: str

@typing.type_check_only
class CustomerProfileIndustry(typing.TypedDict, total=False):
    citationIds: _list[str]
    industry: str

@typing.type_check_only
class CustomerProfileLocation(typing.TypedDict, total=False):
    address: str
    brand: str
    citationIds: _list[str]
    facilityType: str

@typing.type_check_only
class CustomerProfilePerson(typing.TypedDict, total=False):
    citationIds: _list[str]
    name: str
    title: str

@typing.type_check_only
class CustomerProfileProduct(typing.TypedDict, total=False):
    brand: str
    citationIds: _list[str]
    product: str

@typing.type_check_only
class CustomerProfileSecurityConsiderations(typing.TypedDict, total=False):
    considerations: _list[str]
    note: str

@typing.type_check_only
class CustomerProfileSummary(typing.TypedDict, total=False):
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
class CustomerProfileWebPresence(typing.TypedDict, total=False):
    citationIds: _list[str]
    domain: str

@typing.type_check_only
class DataLeakAlertDetail(typing.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class DataLeakFindingDetail(typing.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class EnumerateAlertFacetsResponse(typing.TypedDict, total=False):
    facets: _list[Facet]

@typing.type_check_only
class Evidence(typing.TypedDict, total=False):
    commonThemes: _list[str]
    distinctThemes: _list[str]

@typing.type_check_only
class Facet(typing.TypedDict, total=False):
    facet: str
    facetCounts: _list[FacetCount]
    facetType: str
    maxValue: str
    minValue: str
    totalCount: str

@typing.type_check_only
class FacetCount(typing.TypedDict, total=False):
    count: int
    value: str

@typing.type_check_only
class Finding(typing.TypedDict, total=False):
    aiSummary: str
    alert: str
    audit: Audit
    configurations: _list[str]
    detail: FindingDetail
    displayName: str
    name: str
    provider: str
    relevanceAnalysis: RelevanceAnalysis
    reoccurrenceTimes: _list[str]
    severity: float
    severityAnalysis: SeverityAnalysis

@typing.type_check_only
class FindingDetail(typing.TypedDict, total=False):
    dataLeak: DataLeakFindingDetail
    detailType: str
    initialAccessBroker: InitialAccessBrokerFindingDetail
    insiderThreat: InsiderThreatFindingDetail
    targetTechnology: TargetTechnologyFindingDetail

@typing.type_check_only
class GenerateOrgProfileConfigurationRequest(typing.TypedDict, total=False):
    displayName: str
    domain: str

@typing.type_check_only
class GetPasswordResponse(typing.TypedDict, total=False):
    password: str

@typing.type_check_only
class InitialAccessBrokerAlertDetail(typing.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class InitialAccessBrokerFindingDetail(typing.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class InsiderThreatAlertDetail(typing.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

@typing.type_check_only
class InsiderThreatFindingDetail(typing.TypedDict, total=False):
    documentId: str
    matchScore: float
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"
    ]

@typing.type_check_only
class ListAlertsResponse(typing.TypedDict, total=False):
    alerts: _list[Alert]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationRevisionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    revisions: _list[ConfigurationRevision]

@typing.type_check_only
class ListConfigurationsResponse(typing.TypedDict, total=False):
    configurations: _list[Configuration]
    nextPageToken: str

@typing.type_check_only
class ListFindingsResponse(typing.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class MarkAlertAsBenignRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsDuplicateRequest(typing.TypedDict, total=False):
    duplicateOf: str

@typing.type_check_only
class MarkAlertAsEscalatedRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsFalsePositiveRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsNotActionableRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsReadRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsResolvedRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsTrackedExternallyRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAlertAsTriagedRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PriorityAnalysis(typing.TypedDict, total=False):
    confidence: typing.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    priorityLevel: typing.Literal[
        "PRIORITY_LEVEL_UNSPECIFIED",
        "PRIORITY_LEVEL_LOW",
        "PRIORITY_LEVEL_MEDIUM",
        "PRIORITY_LEVEL_HIGH",
        "PRIORITY_LEVEL_CRITICAL",
    ]
    reasoning: str

@typing.type_check_only
class ProductFix(typing.TypedDict, total=False):
    displayName: str
    publishTime: str
    sourceId: str
    uri: str

@typing.type_check_only
class PublicExploit(typing.TypedDict, total=False):
    exploitGrade: typing.Literal[
        "EXPLOIT_GRADE_UNSPECIFIED",
        "UNEVALUATED",
        "PROOF_OF_CONCEPT",
        "NON_WEAPONIZED",
        "WEAPONIZED",
        "SCANNER",
        "FAKE",
    ]
    exploitName: str
    exploitReliability: typing.Literal[
        "EXPLOIT_RELIABILITY_UNSPECIFIED", "UNREVIEWED", "REVIEWED", "TESTED"
    ]
    releaseTime: str
    sizeBytes: str
    uri: str

@typing.type_check_only
class RelevanceAnalysis(typing.TypedDict, total=False):
    confidence: typing.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    evidence: Evidence
    reasoning: str
    relevanceLevel: typing.Literal[
        "RELEVANCE_LEVEL_UNSPECIFIED",
        "RELEVANCE_LEVEL_LOW",
        "RELEVANCE_LEVEL_MEDIUM",
        "RELEVANCE_LEVEL_HIGH",
    ]
    relevant: bool

@typing.type_check_only
class SearchFindingsResponse(typing.TypedDict, total=False):
    findings: _list[Finding]
    nextPageToken: str

@typing.type_check_only
class SeverityAnalysis(typing.TypedDict, total=False):
    confidence: typing.Literal[
        "CONFIDENCE_LEVEL_UNSPECIFIED",
        "CONFIDENCE_LEVEL_LOW",
        "CONFIDENCE_LEVEL_MEDIUM",
        "CONFIDENCE_LEVEL_HIGH",
    ]
    reasoning: str
    severityLevel: typing.Literal[
        "SEVERITY_LEVEL_UNSPECIFIED",
        "SEVERITY_LEVEL_LOW",
        "SEVERITY_LEVEL_MEDIUM",
        "SEVERITY_LEVEL_HIGH",
    ]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetTechnologyAlertDetail(typing.TypedDict, total=False):
    vulnerabilityMatch: VulnerabilityMatch

@typing.type_check_only
class TargetTechnologyFindingDetail(typing.TypedDict, total=False):
    vulnerabilityMatch: VulnerabilityMatch

@typing.type_check_only
class TechnologyWatchListAlertThreshold(typing.TypedDict, total=False):
    cvssScoreMinimum: float
    epssScoreMinimum: float
    exploitationStates: _list[
        typing.Literal[
            "EXPLOITATION_STATE_UNSPECIFIED",
            "EXPLOITATION_STATE_NO_KNOWN",
            "EXPLOITATION_STATE_REPORTED",
            "EXPLOITATION_STATE_SUSPECTED",
            "EXPLOITATION_STATE_CONFIRMED",
            "EXPLOITATION_STATE_WIDESPREAD",
        ]
    ]
    priorityMinimum: typing.Literal[
        "PRIORITY_UNSPECIFIED", "P0", "P1", "P2", "P3", "P4"
    ]
    riskRatingMinimum: typing.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNRATED"
    ]

@typing.type_check_only
class TechnologyWatchListConfig(typing.TypedDict, total=False):
    alertThreshold: TechnologyWatchListAlertThreshold
    technologies: _list[str]

@typing.type_check_only
class UpsertConfigurationResponse(typing.TypedDict, total=False):
    configuration: str

@typing.type_check_only
class VulnerabilityMatch(typing.TypedDict, total=False):
    associations: _list[Association]
    collectionId: str
    cveId: str
    cvss3Score: float
    description: str
    disclosureTime: str
    epssScore: float
    exploitationConsequences: _list[
        typing.Literal[
            "EXPLOITATION_CONSEQUENCE_UNSPECIFIED",
            "CODE_EXECUTION",
            "COMMAND_EXECUTION",
            "DATA_LOSS",
            "DATA_MANIPULATION",
            "DENIAL_OF_SERVICE",
            "INFORMATION_DISCLOSURE",
            "UNAUTHORIZED_ACCESS",
            "PRIVILEGE_ESCALATION",
            "SANDBOX_ESCAPE",
            "SECURITY_BYPASS",
            "CONTAINER_ESCAPE",
            "SPOOFING",
        ]
    ]
    exploitationState: typing.Literal[
        "EXPLOITATION_STATE_UNSPECIFIED",
        "EXPLOITATION_STATE_NO_KNOWN",
        "EXPLOITATION_STATE_REPORTED",
        "EXPLOITATION_STATE_SUSPECTED",
        "EXPLOITATION_STATE_CONFIRMED",
        "EXPLOITATION_STATE_WIDESPREAD",
    ]
    exploitationVectors: _list[
        typing.Literal[
            "EXPLOITATION_VECTOR_UNSPECIFIED",
            "ADMINISTRATIVE_INTERFACE",
            "BLUETOOTH_ACCESS",
            "BROWSER",
            "COMPROMISED_COMMUNICATION_CHANNEL",
            "EMAIL",
            "EXPOSED_WEB_APPLICATION",
            "LOCAL_NETWORK_ACCESS",
            "MALICIOUS_APPLICATION",
            "MALICIOUS_FILE",
            "MALICIOUS_SERVER",
            "OPEN_PORT",
            "PHYSICAL_ACCESS",
            "SHORT_RANGE_RADIO",
            "UNSPECIFIED_LOCAL_VECTOR",
            "UNSPECIFIED_REMOTE_VECTOR",
            "VPN_ACCESS",
            "WIFI_ACCESS",
        ]
    ]
    matchedTechnologies: _list[str]
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "P0", "P1", "P2", "P3", "P4"]
    productFixes: _list[ProductFix]
    publicExploits: _list[PublicExploit]
    publiclyAvailableExploit: bool
    riskRating: typing.Literal[
        "RISK_RATING_UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNRATED"
    ]
    technologies: _list[str]
