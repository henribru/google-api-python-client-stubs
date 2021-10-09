import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditLoggingSettings(typing_extensions.TypedDict, total=False):
    logAdminReadActions: bool
    logDataReadActions: bool
    logDataWriteActions: bool
    project: str

@typing.type_check_only
class BooleanOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class BooleanPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: BooleanOperatorOptions

@typing.type_check_only
class CheckAccessResponse(typing_extensions.TypedDict, total=False):
    hasAccess: bool

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    logicOperator: typing_extensions.Literal["AND", "OR", "NOT"]
    subFilters: _list[Filter]

@typing.type_check_only
class ContextAttribute(typing_extensions.TypedDict, total=False):
    name: str
    values: _list[str]

@typing.type_check_only
class CustomerIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class CustomerQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class CustomerSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class CustomerSettings(typing_extensions.TypedDict, total=False):
    auditLoggingSettings: AuditLoggingSettings
    vpcSettings: VPCSettings

@typing.type_check_only
class CustomerUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    disableModifications: bool
    disableServing: bool
    displayName: str
    indexingServiceAccounts: _list[str]
    itemsVisibility: _list[GSuitePrincipal]
    name: str
    operationIds: _list[str]
    shortName: str

@typing.type_check_only
class DataSourceIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class DataSourceRestriction(typing_extensions.TypedDict, total=False):
    filterOptions: _list[FilterOptions]
    source: Source

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class DatePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DateOperatorOptions

@typing.type_check_only
class DateValues(typing_extensions.TypedDict, total=False):
    values: _list[Date]

@typing.type_check_only
class DebugOptions(typing_extensions.TypedDict, total=False):
    enableDebugging: bool

@typing.type_check_only
class DeleteQueueItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class DisplayedProperty(typing_extensions.TypedDict, total=False):
    propertyName: str

@typing.type_check_only
class DoubleOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class DoublePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DoubleOperatorOptions

@typing.type_check_only
class DoubleValues(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class DriveFollowUpRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "FOLLOWUP_SUGGESTIONS", "FOLLOWUP_ACTION_ITEMS"
    ]

@typing.type_check_only
class DriveLocationRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "TRASHED", "STARRED"]

@typing.type_check_only
class DriveMimeTypeRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "PDF",
        "DOCUMENT",
        "PRESENTATION",
        "SPREADSHEET",
        "FORM",
        "DRAWING",
        "SCRIPT",
        "MAP",
        "IMAGE",
        "AUDIO",
        "VIDEO",
        "FOLDER",
        "ARCHIVE",
        "SITE",
    ]

@typing.type_check_only
class DriveTimeSpanRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
    ]

@typing.type_check_only
class EmailAddress(typing_extensions.TypedDict, total=False):
    emailAddress: str

@typing.type_check_only
class EnumOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class EnumPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: EnumOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    possibleValues: _list[EnumValuePair]

@typing.type_check_only
class EnumValuePair(typing_extensions.TypedDict, total=False):
    integerValue: int
    stringValue: str

@typing.type_check_only
class EnumValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ErrorInfo(typing_extensions.TypedDict, total=False):
    errorMessages: _list[ErrorMessage]

@typing.type_check_only
class ErrorMessage(typing_extensions.TypedDict, total=False):
    errorMessage: str
    source: Source

@typing.type_check_only
class FacetBucket(typing_extensions.TypedDict, total=False):
    count: int
    percentage: int
    value: Value

@typing.type_check_only
class FacetOptions(typing_extensions.TypedDict, total=False):
    numFacetBuckets: int
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FacetResult(typing_extensions.TypedDict, total=False):
    buckets: _list[FacetBucket]
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FieldViolation(typing_extensions.TypedDict, total=False):
    description: str
    field: str

@typing.type_check_only
class Filter(dict[str, typing.Any]): ...

@typing.type_check_only
class FilterOptions(dict[str, typing.Any]): ...

@typing.type_check_only
class FreshnessOptions(typing_extensions.TypedDict, total=False):
    freshnessDuration: str
    freshnessProperty: str

@typing.type_check_only
class GSuitePrincipal(typing_extensions.TypedDict, total=False):
    gsuiteDomain: bool
    gsuiteGroupEmail: str
    gsuiteUserEmail: str

@typing.type_check_only
class GetCustomerIndexStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerIndexStats]

@typing.type_check_only
class GetCustomerQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerQueryStats]

@typing.type_check_only
class GetCustomerSessionStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerSessionStats]

@typing.type_check_only
class GetCustomerUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerUserStats]

@typing.type_check_only
class GetDataSourceIndexStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[DataSourceIndexStats]

@typing.type_check_only
class GetSearchApplicationQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationQueryStats]

@typing.type_check_only
class GetSearchApplicationSessionStatsResponse(
    typing_extensions.TypedDict, total=False
):
    stats: _list[SearchApplicationSessionStats]

@typing.type_check_only
class GetSearchApplicationUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationUserStats]

@typing.type_check_only
class HtmlOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class HtmlPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: HtmlOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class HtmlValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class IndexItemOptions(typing_extensions.TypedDict, total=False):
    allowUnknownGsuitePrincipals: bool

@typing.type_check_only
class IndexItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    indexItemOptions: IndexItemOptions
    item: Item
    mode: typing_extensions.Literal["UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"]

@typing.type_check_only
class IntegerOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class IntegerPropertyOptions(typing_extensions.TypedDict, total=False):
    maximumValue: str
    minimumValue: str
    operatorOptions: IntegerOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class IntegerValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class Interaction(typing_extensions.TypedDict, total=False):
    interactionTime: str
    principal: Principal
    type: typing_extensions.Literal["UNSPECIFIED", "VIEW", "EDIT"]

@typing.type_check_only
class Item(dict[str, typing.Any]): ...

@typing.type_check_only
class ItemAcl(typing_extensions.TypedDict, total=False):
    aclInheritanceType: typing_extensions.Literal[
        "NOT_APPLICABLE", "CHILD_OVERRIDE", "PARENT_OVERRIDE", "BOTH_PERMIT"
    ]
    deniedReaders: _list[Principal]
    inheritAclFrom: str
    owners: _list[Principal]
    readers: _list[Principal]

@typing.type_check_only
class ItemContent(typing_extensions.TypedDict, total=False):
    contentDataRef: UploadItemRef
    contentFormat: typing_extensions.Literal["UNSPECIFIED", "HTML", "TEXT", "RAW"]
    hash: str
    inlineContent: str

@typing.type_check_only
class ItemCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    statusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]

@typing.type_check_only
class ItemMetadata(typing_extensions.TypedDict, total=False):
    containerName: str
    contentLanguage: str
    contextAttributes: _list[ContextAttribute]
    createTime: str
    hash: str
    interactions: _list[Interaction]
    keywords: _list[str]
    mimeType: str
    objectType: str
    searchQualityMetadata: SearchQualityMetadata
    sourceRepositoryUrl: str
    title: str
    updateTime: str

@typing.type_check_only
class ItemStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]
    processingErrors: _list[ProcessingError]
    repositoryErrors: _list[RepositoryError]

@typing.type_check_only
class ItemStructuredData(dict[str, typing.Any]): ...

@typing.type_check_only
class ListDataSourceResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[DataSource]

@typing.type_check_only
class ListItemNamesForUnmappedIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    itemNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListQuerySourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[QuerySource]

@typing.type_check_only
class ListSearchApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    searchApplications: _list[SearchApplication]

@typing.type_check_only
class ListUnmappedIdentitiesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unmappedIdentities: _list[UnmappedIdentity]

@typing.type_check_only
class MatchRange(typing_extensions.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    createTime: str
    displayOptions: ResultDisplayMetadata
    fields: _list[NamedProperty]
    mimeType: str
    objectType: str
    owner: Person
    source: Source
    updateTime: str

@typing.type_check_only
class Metaline(typing_extensions.TypedDict, total=False):
    properties: _list[DisplayedProperty]

@typing.type_check_only
class Name(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class NamedProperty(dict[str, typing.Any]): ...

@typing.type_check_only
class ObjectDefinition(typing_extensions.TypedDict, total=False):
    name: str
    options: ObjectOptions
    propertyDefinitions: _list[PropertyDefinition]

@typing.type_check_only
class ObjectDisplayOptions(typing_extensions.TypedDict, total=False):
    metalines: _list[Metaline]
    objectDisplayLabel: str

@typing.type_check_only
class ObjectOptions(typing_extensions.TypedDict, total=False):
    displayOptions: ObjectDisplayOptions
    freshnessOptions: FreshnessOptions

@typing.type_check_only
class ObjectPropertyOptions(typing_extensions.TypedDict, total=False):
    subobjectProperties: _list[PropertyDefinition]

@typing.type_check_only
class ObjectValues(dict[str, typing.Any]): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PeopleSuggestion(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Person(typing_extensions.TypedDict, total=False):
    emailAddresses: _list[EmailAddress]
    name: str
    obfuscatedId: str
    personNames: _list[Name]
    photos: _list[Photo]

@typing.type_check_only
class Photo(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class PollItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    limit: int
    queue: str
    statusCodes: _list[str]

@typing.type_check_only
class PollItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]

@typing.type_check_only
class Principal(typing_extensions.TypedDict, total=False):
    groupResourceName: str
    gsuitePrincipal: GSuitePrincipal
    userResourceName: str

@typing.type_check_only
class ProcessingError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "PROCESSING_ERROR_CODE_UNSPECIFIED",
        "MALFORMED_REQUEST",
        "UNSUPPORTED_CONTENT_FORMAT",
        "INDIRECT_BROKEN_ACL",
        "ACL_CYCLE",
    ]
    errorMessage: str
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class PropertyDefinition(dict[str, typing.Any]): ...

@typing.type_check_only
class PropertyDisplayOptions(typing_extensions.TypedDict, total=False):
    displayLabel: str

@typing.type_check_only
class PushItem(typing_extensions.TypedDict, total=False):
    contentHash: str
    metadataHash: str
    payload: str
    queue: str
    repositoryError: RepositoryError
    structuredDataHash: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MODIFIED", "NOT_MODIFIED", "REPOSITORY_ERROR", "REQUEUE"
    ]

@typing.type_check_only
class PushItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    item: PushItem

@typing.type_check_only
class QueryCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    statusCode: int

@typing.type_check_only
class QueryInterpretation(typing_extensions.TypedDict, total=False):
    interpretationType: typing_extensions.Literal["NONE", "BLEND", "REPLACE"]
    interpretedQuery: str
    reason: typing_extensions.Literal[
        "UNSPECIFIED",
        "QUERY_HAS_NATURAL_LANGUAGE_INTENT",
        "NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY",
    ]

@typing.type_check_only
class QueryInterpretationConfig(typing_extensions.TypedDict, total=False):
    forceDisableSupplementalResults: bool
    forceVerbatimMode: bool

@typing.type_check_only
class QueryInterpretationOptions(typing_extensions.TypedDict, total=False):
    disableNlInterpretation: bool
    disableSupplementalResults: bool
    enableVerbatimMode: bool

@typing.type_check_only
class QueryItem(typing_extensions.TypedDict, total=False):
    isSynthetic: bool

@typing.type_check_only
class QueryOperator(typing_extensions.TypedDict, total=False):
    displayName: str
    enumValues: _list[str]
    greaterThanOperatorName: str
    isFacetable: bool
    isRepeatable: bool
    isReturnable: bool
    isSortable: bool
    isSuggestable: bool
    lessThanOperatorName: str
    objectType: str
    operatorName: str
    type: typing_extensions.Literal[
        "UNKNOWN",
        "INTEGER",
        "DOUBLE",
        "TIMESTAMP",
        "BOOLEAN",
        "ENUM",
        "DATE",
        "TEXT",
        "HTML",
    ]

@typing.type_check_only
class QuerySource(typing_extensions.TypedDict, total=False):
    displayName: str
    operators: _list[QueryOperator]
    shortName: str
    source: Source

@typing.type_check_only
class QuerySuggestion(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RepositoryError(typing_extensions.TypedDict, total=False):
    errorMessage: str
    httpStatusCode: int
    type: typing_extensions.Literal[
        "UNKNOWN",
        "NETWORK_ERROR",
        "DNS_ERROR",
        "CONNECTION_ERROR",
        "AUTHENTICATION_ERROR",
        "AUTHORIZATION_ERROR",
        "SERVER_ERROR",
        "QUOTA_EXCEEDED",
        "SERVICE_UNAVAILABLE",
        "CLIENT_ERROR",
    ]

@typing.type_check_only
class RequestOptions(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    languageCode: str
    searchApplicationId: str
    timeZone: str

@typing.type_check_only
class ResetSearchApplicationRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions

@typing.type_check_only
class ResponseDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class RestrictItem(typing_extensions.TypedDict, total=False):
    driveFollowUpRestrict: DriveFollowUpRestrict
    driveLocationRestrict: DriveLocationRestrict
    driveMimeTypeRestrict: DriveMimeTypeRestrict
    driveTimeSpanRestrict: DriveTimeSpanRestrict
    searchOperator: str

@typing.type_check_only
class ResultCounts(typing_extensions.TypedDict, total=False):
    sourceResultCounts: _list[SourceResultCount]

@typing.type_check_only
class ResultDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class ResultDisplayField(typing_extensions.TypedDict, total=False):
    label: str
    operatorName: str
    property: NamedProperty

@typing.type_check_only
class ResultDisplayLine(typing_extensions.TypedDict, total=False):
    fields: _list[ResultDisplayField]

@typing.type_check_only
class ResultDisplayMetadata(dict[str, typing.Any]): ...

@typing.type_check_only
class RetrievalImportance(typing_extensions.TypedDict, total=False):
    importance: typing_extensions.Literal["DEFAULT", "HIGHEST", "HIGH", "LOW", "NONE"]

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    objectDefinitions: _list[ObjectDefinition]
    operationIds: _list[str]

@typing.type_check_only
class ScoringConfig(typing_extensions.TypedDict, total=False):
    disableFreshness: bool
    disablePersonalization: bool

@typing.type_check_only
class SearchApplication(dict[str, typing.Any]): ...

@typing.type_check_only
class SearchApplicationQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class SearchApplicationSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class SearchApplicationUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class SearchItemsByViewUrlRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    pageToken: str
    viewUrl: str

@typing.type_check_only
class SearchItemsByViewUrlResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class SearchQualityMetadata(typing_extensions.TypedDict, total=False):
    quality: float

@typing.type_check_only
class SearchRequest(typing_extensions.TypedDict, total=False):
    contextAttributes: _list[ContextAttribute]
    dataSourceRestrictions: _list[DataSourceRestriction]
    facetOptions: _list[FacetOptions]
    pageSize: int
    query: str
    queryInterpretationOptions: QueryInterpretationOptions
    requestOptions: RequestOptions
    sortOptions: SortOptions
    start: int

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    debugInfo: ResponseDebugInfo
    errorInfo: ErrorInfo
    facetResults: _list[FacetResult]
    hasMoreResults: bool
    queryInterpretation: QueryInterpretation
    resultCountEstimate: str
    resultCountExact: str
    resultCounts: ResultCounts
    results: _list[SearchResult]
    spellResults: _list[SpellResult]
    structuredResults: _list[StructuredResult]

@typing.type_check_only
class SearchResult(dict[str, typing.Any]): ...

@typing.type_check_only
class Snippet(typing_extensions.TypedDict, total=False):
    matchRanges: _list[MatchRange]
    snippet: str

@typing.type_check_only
class SortOptions(typing_extensions.TypedDict, total=False):
    operatorName: str
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    name: str
    predefinedSource: typing_extensions.Literal[
        "NONE",
        "QUERY_HISTORY",
        "PERSON",
        "GOOGLE_DRIVE",
        "GOOGLE_GMAIL",
        "GOOGLE_SITES",
        "GOOGLE_GROUPS",
        "GOOGLE_CALENDAR",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class SourceConfig(typing_extensions.TypedDict, total=False):
    crowdingConfig: SourceCrowdingConfig
    scoringConfig: SourceScoringConfig
    source: Source

@typing.type_check_only
class SourceCrowdingConfig(typing_extensions.TypedDict, total=False):
    numResults: int
    numSuggestions: int

@typing.type_check_only
class SourceResultCount(typing_extensions.TypedDict, total=False):
    hasMoreResults: bool
    resultCountEstimate: str
    resultCountExact: str
    source: Source

@typing.type_check_only
class SourceScoringConfig(typing_extensions.TypedDict, total=False):
    sourceImportance: typing_extensions.Literal["DEFAULT", "LOW", "HIGH"]

@typing.type_check_only
class SpellResult(typing_extensions.TypedDict, total=False):
    suggestedQuery: str

@typing.type_check_only
class StartUploadItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StructuredDataObject(dict[str, typing.Any]): ...

@typing.type_check_only
class StructuredResult(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SuggestRequest(typing_extensions.TypedDict, total=False):
    dataSourceRestrictions: _list[DataSourceRestriction]
    query: str
    requestOptions: RequestOptions

@typing.type_check_only
class SuggestResponse(typing_extensions.TypedDict, total=False):
    suggestResults: _list[SuggestResult]

@typing.type_check_only
class SuggestResult(typing_extensions.TypedDict, total=False):
    peopleSuggestion: PeopleSuggestion
    querySuggestion: QuerySuggestion
    source: Source
    suggestedQuery: str

@typing.type_check_only
class TextOperatorOptions(typing_extensions.TypedDict, total=False):
    exactMatchWithOperator: bool
    operatorName: str

@typing.type_check_only
class TextPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TextOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class TextValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TimestampOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class TimestampPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TimestampOperatorOptions

@typing.type_check_only
class TimestampValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class UnmappedIdentity(typing_extensions.TypedDict, total=False):
    externalIdentity: Principal
    resolutionStatusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "NOT_FOUND",
        "IDENTITY_SOURCE_NOT_FOUND",
        "IDENTITY_SOURCE_MISCONFIGURED",
        "TOO_MANY_MAPPINGS_FOUND",
        "INTERNAL_ERROR",
    ]

@typing.type_check_only
class UnreserveItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class UpdateDataSourceRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    source: DataSource

@typing.type_check_only
class UpdateSchemaRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    schema: Schema
    validateOnly: bool

@typing.type_check_only
class UploadItemRef(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class VPCSettings(typing_extensions.TypedDict, total=False):
    project: str

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    dateValue: Date
    doubleValue: float
    integerValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class ValueFilter(typing_extensions.TypedDict, total=False):
    operatorName: str
    value: Value
