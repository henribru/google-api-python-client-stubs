import typing

import typing_extensions

class ItemMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    hash: str
    keywords: typing.List[str]
    objectType: str
    containerName: str
    searchQualityMetadata: SearchQualityMetadata
    contentLanguage: str
    interactions: typing.List[Interaction]
    updateTime: str
    mimeType: str
    sourceRepositoryUrl: str
    title: str

class Metaline(typing_extensions.TypedDict, total=False):
    properties: typing.List[DisplayedProperty]

class StartUploadItemRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    connectorName: str

class GetDataSourceIndexStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[DataSourceIndexStats]

class PeopleSuggestion(typing_extensions.TypedDict, total=False):
    person: Person

class SourceResultCount(typing_extensions.TypedDict, total=False):
    resultCountEstimate: str
    resultCountExact: str
    source: Source
    hasMoreResults: bool

class ObjectOptions(typing_extensions.TypedDict, total=False):
    displayOptions: ObjectDisplayOptions
    freshnessOptions: FreshnessOptions

class DataSource(typing_extensions.TypedDict, total=False):
    disableServing: bool
    shortName: str
    operationIds: typing.List[str]
    itemsVisibility: typing.List[GSuitePrincipal]
    disableModifications: bool
    displayName: str
    name: str
    indexingServiceAccounts: typing.List[str]

class TimestampValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class ItemAcl(typing_extensions.TypedDict, total=False):
    deniedReaders: typing.List[Principal]
    inheritAclFrom: str
    owners: typing.List[Principal]
    aclInheritanceType: typing_extensions.Literal[
        "NOT_APPLICABLE", "CHILD_OVERRIDE", "PARENT_OVERRIDE", "BOTH_PERMIT"
    ]
    readers: typing.List[Principal]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class ItemStructuredData(typing_extensions.TypedDict, total=False):
    object: StructuredDataObject
    hash: str

class SourceCrowdingConfig(typing_extensions.TypedDict, total=False):
    numSuggestions: int
    numResults: int

class SearchResponse(typing_extensions.TypedDict, total=False):
    hasMoreResults: bool
    errorInfo: ErrorInfo
    results: typing.List[SearchResult]
    resultCountExact: str
    resultCounts: ResultCounts
    resultCountEstimate: str
    spellResults: typing.List[SpellResult]
    queryInterpretation: QueryInterpretation
    debugInfo: ResponseDebugInfo
    structuredResults: typing.List[StructuredResult]
    facetResults: typing.List[FacetResult]

class TimestampOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    operatorName: str
    lessThanOperatorName: str

class CustomerQueryStats(typing_extensions.TypedDict, total=False):
    queryCountByStatus: typing.List[QueryCountByStatus]
    date: Date

class PropertyDefinition(typing_extensions.TypedDict, total=False):
    booleanPropertyOptions: BooleanPropertyOptions
    displayOptions: PropertyDisplayOptions
    htmlPropertyOptions: HtmlPropertyOptions
    enumPropertyOptions: EnumPropertyOptions
    integerPropertyOptions: IntegerPropertyOptions
    objectPropertyOptions: ObjectPropertyOptions
    isSortable: bool
    isReturnable: bool
    isRepeatable: bool
    textPropertyOptions: TextPropertyOptions
    isSuggestable: bool
    doublePropertyOptions: DoublePropertyOptions
    isFacetable: bool
    isWildcardSearchable: bool
    name: str
    datePropertyOptions: DatePropertyOptions
    timestampPropertyOptions: TimestampPropertyOptions

class StructuredResult(typing_extensions.TypedDict, total=False):
    person: Person

class IndexItemOptions(typing_extensions.TypedDict, total=False):
    allowUnknownGsuitePrincipals: bool

class PushItem(typing_extensions.TypedDict, total=False):
    structuredDataHash: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MODIFIED", "NOT_MODIFIED", "REPOSITORY_ERROR", "REQUEUE"
    ]
    metadataHash: str
    repositoryError: RepositoryError
    queue: str
    contentHash: str
    payload: str

class SuggestResponse(typing_extensions.TypedDict, total=False):
    suggestResults: typing.List[SuggestResult]

class QueryOperator(typing_extensions.TypedDict, total=False):
    objectType: str
    isSuggestable: bool
    enumValues: typing.List[str]
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
    isSortable: bool
    isRepeatable: bool
    greaterThanOperatorName: str
    isReturnable: bool
    displayName: str
    isFacetable: bool
    lessThanOperatorName: str

class EmailAddress(typing_extensions.TypedDict, total=False):
    emailAddress: str

class ResultDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

class StructuredDataObject(typing.Dict[str, typing.Any]): ...

class PushItemRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    connectorName: str
    item: PushItem

class SearchApplicationSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

class HtmlPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: HtmlOperatorOptions
    retrievalImportance: RetrievalImportance

class SearchApplicationUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

class DoubleValues(typing_extensions.TypedDict, total=False):
    values: typing.List[float]

class FacetBucket(typing_extensions.TypedDict, total=False):
    value: Value
    percentage: int
    count: int

class BooleanOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

class UpdateSchemaRequest(typing_extensions.TypedDict, total=False):
    schema: Schema
    debugOptions: DebugOptions
    validateOnly: bool

class DateValues(typing_extensions.TypedDict, total=False):
    values: typing.List[Date]

class UploadItemRef(typing_extensions.TypedDict, total=False):
    name: str

class DoubleOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

class DataSourceIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: typing.List[ItemCountByStatus]

class IndexItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    indexItemOptions: IndexItemOptions
    item: Item
    mode: typing_extensions.Literal["UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"]
    debugOptions: DebugOptions

class RetrievalImportance(typing_extensions.TypedDict, total=False):
    importance: typing_extensions.Literal["DEFAULT", "HIGHEST", "HIGH", "LOW", "NONE"]

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

class RestrictItem(typing_extensions.TypedDict, total=False):
    searchOperator: str
    driveLocationRestrict: DriveLocationRestrict
    driveFollowUpRestrict: DriveFollowUpRestrict
    driveTimeSpanRestrict: DriveTimeSpanRestrict
    driveMimeTypeRestrict: DriveMimeTypeRestrict

class SourceScoringConfig(typing_extensions.TypedDict, total=False):
    sourceImportance: typing_extensions.Literal["DEFAULT", "LOW", "HIGH"]

class IntegerValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class ObjectDisplayOptions(typing_extensions.TypedDict, total=False):
    metalines: typing.List[Metaline]
    objectDisplayLabel: str

class SearchApplication(typing_extensions.TypedDict, total=False):
    defaultSortOptions: SortOptions
    dataSourceRestrictions: typing.List[DataSourceRestriction]
    displayName: str
    sourceConfig: typing.List[SourceConfig]
    operationIds: typing.List[str]
    name: str
    scoringConfig: ScoringConfig
    defaultFacetOptions: typing.List[FacetOptions]

class QuerySuggestion(typing_extensions.TypedDict, total=False): ...
class Schema(typing.Dict[str, typing.Any]): ...

class GSuitePrincipal(typing_extensions.TypedDict, total=False):
    gsuiteGroupEmail: str
    gsuiteDomain: bool
    gsuiteUserEmail: str

class DriveFollowUpRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "FOLLOWUP_SUGGESTIONS", "FOLLOWUP_ACTION_ITEMS"
    ]

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

class QueryItem(typing_extensions.TypedDict, total=False):
    isSynthetic: bool

class DoublePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DoubleOperatorOptions

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class Photo(typing_extensions.TypedDict, total=False):
    url: str

class GetCustomerQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[CustomerQueryStats]

class SearchApplicationQueryStats(typing_extensions.TypedDict, total=False):
    queryCountByStatus: typing.List[QueryCountByStatus]
    date: Date

class DebugOptions(typing_extensions.TypedDict, total=False):
    enableDebugging: bool

class Person(typing_extensions.TypedDict, total=False):
    name: str
    emailAddresses: typing.List[EmailAddress]
    photos: typing.List[Photo]
    obfuscatedId: str
    personNames: typing.List[Name]

class PollItemsRequest(typing_extensions.TypedDict, total=False):
    statusCodes: typing.List[str]
    debugOptions: DebugOptions
    connectorName: str
    limit: int
    queue: str

class SearchItemsByViewUrlResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Item]

class ProcessingError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "PROCESSING_ERROR_CODE_UNSPECIFIED",
        "MALFORMED_REQUEST",
        "UNSUPPORTED_CONTENT_FORMAT",
        "INDIRECT_BROKEN_ACL",
        "ACL_CYCLE",
    ]
    errorMessage: str
    fieldViolations: typing.List[FieldViolation]

class ListItemsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    items: typing.List[Item]

class EnumValuePair(typing_extensions.TypedDict, total=False):
    stringValue: str
    integerValue: int

class CheckAccessResponse(typing_extensions.TypedDict, total=False):
    hasAccess: bool

class GetCustomerSessionStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[CustomerSessionStats]

class ResultCounts(typing_extensions.TypedDict, total=False):
    sourceResultCounts: typing.List[SourceResultCount]

class QueryInterpretation(typing_extensions.TypedDict, total=False):
    interpretedQuery: str
    reason: typing_extensions.Literal[
        "UNSPECIFIED",
        "QUERY_HAS_NATURAL_LANGUAGE_INTENT",
        "NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY",
    ]
    interpretationType: typing_extensions.Literal["NONE", "BLEND", "REPLACE"]

class FieldViolation(typing_extensions.TypedDict, total=False):
    description: str
    field: str

class ResultDisplayMetadata(typing_extensions.TypedDict, total=False):
    metalines: typing.List[ResultDisplayLine]
    objectTypeLabel: str

class ObjectDefinition(typing.Dict[str, typing.Any]): ...

class ItemStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]
    processingErrors: typing.List[ProcessingError]
    repositoryErrors: typing.List[RepositoryError]

class UpdateDataSourceRequest(typing_extensions.TypedDict, total=False):
    source: DataSource
    debugOptions: DebugOptions

class FacetResult(typing_extensions.TypedDict, total=False):
    objectType: str
    buckets: typing.List[FacetBucket]
    operatorName: str
    sourceName: str

class EnumValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class SearchResult(typing.Dict[str, typing.Any]): ...

class Date(typing_extensions.TypedDict, total=False):
    year: int
    month: int
    day: int

class Filter(typing_extensions.TypedDict, total=False):
    valueFilter: ValueFilter
    compositeFilter: CompositeFilter

class GetSearchApplicationSessionStatsResponse(
    typing_extensions.TypedDict, total=False
):
    stats: typing.List[SearchApplicationSessionStats]

class ListDataSourceResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: typing.List[DataSource]

class CustomerUserStats(typing_extensions.TypedDict, total=False):
    thirtyDaysActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    date: Date
    oneDayActiveUsersCount: str

class SuggestRequest(typing_extensions.TypedDict, total=False):
    query: str
    requestOptions: RequestOptions
    dataSourceRestrictions: typing.List[DataSourceRestriction]

class ValueFilter(typing_extensions.TypedDict, total=False):
    operatorName: str
    value: Value

class ListUnmappedIdentitiesResponse(typing_extensions.TypedDict, total=False):
    unmappedIdentities: typing.List[UnmappedIdentity]
    nextPageToken: str

class FacetOptions(typing_extensions.TypedDict, total=False):
    sourceName: str
    objectType: str
    numFacetBuckets: int
    operatorName: str

class GetCustomerIndexStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[CustomerIndexStats]

class GetCustomerUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[CustomerUserStats]

class TimestampPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TimestampOperatorOptions

class HtmlOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

class SearchItemsByViewUrlRequest(typing_extensions.TypedDict, total=False):
    viewUrl: str
    pageToken: str
    debugOptions: DebugOptions

class TextOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str
    exactMatchWithOperator: bool

class DatePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DateOperatorOptions

class ObjectValues(typing_extensions.TypedDict, total=False):
    values: typing.List[StructuredDataObject]

class CompositeFilter(typing.Dict[str, typing.Any]): ...

class DateOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str
    lessThanOperatorName: str
    greaterThanOperatorName: str

class ErrorMessage(typing_extensions.TypedDict, total=False):
    source: Source
    errorMessage: str

class PropertyDisplayOptions(typing_extensions.TypedDict, total=False):
    displayLabel: str

class IntegerOperatorOptions(typing_extensions.TypedDict, total=False):
    lessThanOperatorName: str
    greaterThanOperatorName: str
    operatorName: str

class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

class NamedProperty(typing.Dict[str, typing.Any]): ...

class Value(typing_extensions.TypedDict, total=False):
    dateValue: Date
    booleanValue: bool
    integerValue: str
    timestampValue: str
    doubleValue: float
    stringValue: str

class ListItemNamesForUnmappedIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    itemNames: typing.List[str]

class DisplayedProperty(typing_extensions.TypedDict, total=False):
    propertyName: str

class UnreserveItemsRequest(typing_extensions.TypedDict, total=False):
    queue: str
    connectorName: str
    debugOptions: DebugOptions

class SuggestResult(typing_extensions.TypedDict, total=False):
    suggestedQuery: str
    source: Source
    peopleSuggestion: PeopleSuggestion
    querySuggestion: QuerySuggestion

class ListSearchApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    searchApplications: typing.List[SearchApplication]

class Snippet(typing_extensions.TypedDict, total=False):
    snippet: str
    matchRanges: typing.List[MatchRange]

class GetSearchApplicationQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[SearchApplicationQueryStats]

class Item(typing.Dict[str, typing.Any]): ...

class CustomerIndexStats(typing_extensions.TypedDict, total=False):
    itemCountByStatus: typing.List[ItemCountByStatus]
    date: Date

class ListQuerySourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: typing.List[QuerySource]

class ItemCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    statusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]

class SpellResult(typing_extensions.TypedDict, total=False):
    suggestedQuery: str

class DeleteQueueItemsRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    queue: str
    connectorName: str

class MatchRange(typing_extensions.TypedDict, total=False):
    end: int
    start: int

class TextPropertyOptions(typing_extensions.TypedDict, total=False):
    retrievalImportance: RetrievalImportance
    operatorOptions: TextOperatorOptions

class HtmlValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class QueryInterpretationOptions(typing_extensions.TypedDict, total=False):
    disableNlInterpretation: bool
    enableVerbatimMode: bool

class CustomerSessionStats(typing_extensions.TypedDict, total=False):
    searchSessionsCount: str
    date: Date

class EnumPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: EnumOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    possibleValues: typing.List[EnumValuePair]

class SearchQualityMetadata(typing_extensions.TypedDict, total=False):
    quality: float

class DriveTimeSpanRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
    ]

class DataSourceRestriction(typing.Dict[str, typing.Any]): ...

class RepositoryError(typing_extensions.TypedDict, total=False):
    httpStatusCode: int
    errorMessage: str
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

class Source(typing_extensions.TypedDict, total=False):
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
    name: str

class ScoringConfig(typing_extensions.TypedDict, total=False):
    disablePersonalization: bool
    disableFreshness: bool

class Name(typing_extensions.TypedDict, total=False):
    displayName: str

class Principal(typing_extensions.TypedDict, total=False):
    gsuitePrincipal: GSuitePrincipal
    groupResourceName: str
    userResourceName: str

class ResponseDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

class Metadata(typing.Dict[str, typing.Any]): ...
class ObjectPropertyOptions(typing.Dict[str, typing.Any]): ...

class SortOptions(typing_extensions.TypedDict, total=False):
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]
    operatorName: str

class ResultDisplayField(typing_extensions.TypedDict, total=False):
    property: NamedProperty
    label: str
    operatorName: str

class DriveLocationRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "TRASHED", "STARRED"]

class RequestOptions(typing_extensions.TypedDict, total=False):
    languageCode: str
    searchApplicationId: str
    timeZone: str
    debugOptions: DebugOptions

class Interaction(typing_extensions.TypedDict, total=False):
    principal: Principal
    interactionTime: str
    type: typing_extensions.Literal["UNSPECIFIED", "VIEW", "EDIT"]

class EnumOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

class FreshnessOptions(typing_extensions.TypedDict, total=False):
    freshnessDuration: str
    freshnessProperty: str

class SourceConfig(typing_extensions.TypedDict, total=False):
    crowdingConfig: SourceCrowdingConfig
    scoringConfig: SourceScoringConfig
    source: Source

class QuerySource(typing_extensions.TypedDict, total=False):
    displayName: str
    operators: typing.List[QueryOperator]
    source: Source
    shortName: str

class ResetSearchApplicationRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions

class IntegerPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: IntegerOperatorOptions
    maximumValue: str
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    minimumValue: str

class GetSearchApplicationUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: typing.List[SearchApplicationUserStats]

class SearchRequest(typing_extensions.TypedDict, total=False):
    queryInterpretationOptions: QueryInterpretationOptions
    facetOptions: typing.List[FacetOptions]
    sortOptions: SortOptions
    requestOptions: RequestOptions
    start: int
    query: str
    dataSourceRestrictions: typing.List[DataSourceRestriction]
    pageSize: int

class TextValues(typing_extensions.TypedDict, total=False):
    values: typing.List[str]

class ErrorInfo(typing_extensions.TypedDict, total=False):
    errorMessages: typing.List[ErrorMessage]

class ResultDisplayLine(typing.Dict[str, typing.Any]): ...

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class QueryCountByStatus(typing_extensions.TypedDict, total=False):
    statusCode: int
    count: str

class PollItemsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Item]

class ItemContent(typing_extensions.TypedDict, total=False):
    contentFormat: typing_extensions.Literal["UNSPECIFIED", "HTML", "TEXT", "RAW"]
    hash: str
    contentDataRef: UploadItemRef
    inlineContent: str

class FilterOptions(typing.Dict[str, typing.Any]): ...

class BooleanPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: BooleanOperatorOptions
