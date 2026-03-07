import typing

import typing_extensions

_list = list

@typing.type_check_only
class Alert(typing_extensions.TypedDict, total=False):
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
class Audit(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: str
    updateTime: str
    updater: str

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
    customerProfile: CustomerProfileConfig
    detailType: str

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
class FindingDetail(typing_extensions.TypedDict, total=False):
    dataLeak: DataLeakFindingDetail
    detailType: str
    initialAccessBroker: InitialAccessBrokerFindingDetail
    insiderThreat: InsiderThreatFindingDetail

@typing.type_check_only
class GenerateOrgProfileConfigurationRequest(typing_extensions.TypedDict, total=False):
    displayName: str
    domain: str

@typing.type_check_only
class InitialAccessBrokerAlertDetail(typing_extensions.TypedDict, total=False):
    discoveryDocumentIds: _list[str]
    severity: str

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
class UpsertConfigurationResponse(typing_extensions.TypedDict, total=False):
    configuration: str
