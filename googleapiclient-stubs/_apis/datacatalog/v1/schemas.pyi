import typing

import typing_extensions

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryConnectionSpec(
    typing_extensions.TypedDict, total=False
):
    cloudSql: GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec
    connectionType: typing_extensions.Literal[
        "CONNECTION_TYPE_UNSPECIFIED", "CLOUD_SQL"
    ]
    hasCredential: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryDateShardedSpec(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    shardCount: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryRoutineSpec(
    typing_extensions.TypedDict, total=False
):
    importedLibraries: typing.List[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryTableSpec(
    typing_extensions.TypedDict, total=False
):
    tableSourceType: typing_extensions.Literal[
        "TABLE_SOURCE_TYPE_UNSPECIFIED",
        "BIGQUERY_VIEW",
        "BIGQUERY_TABLE",
        "BIGQUERY_MATERIALIZED_VIEW",
    ]
    tableSpec: GoogleCloudDatacatalogV1TableSpec
    viewSpec: GoogleCloudDatacatalogV1ViewSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec(
    typing_extensions.TypedDict, total=False
):
    database: str
    instanceId: str
    type: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchema(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1CrossRegionalSource(
    typing_extensions.TypedDict, total=False
):
    taxonomy: str

@typing.type_check_only
class GoogleCloudDatacatalogV1DataSource(typing_extensions.TypedDict, total=False):
    resource: str
    service: typing_extensions.Literal[
        "SERVICE_UNSPECIFIED", "CLOUD_STORAGE", "BIGQUERY"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1DataSourceConnectionSpec(
    typing_extensions.TypedDict, total=False
):
    bigqueryConnectionSpec: GoogleCloudDatacatalogV1BigQueryConnectionSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DatabaseTableSpec(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TABLE_TYPE_UNSPECIFIED", "NATIVE", "EXTERNAL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1Entry(typing_extensions.TypedDict, total=False):
    bigqueryDateShardedSpec: GoogleCloudDatacatalogV1BigQueryDateShardedSpec
    bigqueryTableSpec: GoogleCloudDatacatalogV1BigQueryTableSpec
    dataSource: GoogleCloudDatacatalogV1DataSource
    dataSourceConnectionSpec: GoogleCloudDatacatalogV1DataSourceConnectionSpec
    databaseTableSpec: GoogleCloudDatacatalogV1DatabaseTableSpec
    description: str
    displayName: str
    fullyQualifiedName: str
    gcsFilesetSpec: GoogleCloudDatacatalogV1GcsFilesetSpec
    integratedSystem: typing_extensions.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED",
        "BIGQUERY",
        "CLOUD_PUBSUB",
        "DATAPROC_METASTORE",
    ]
    labels: typing.Dict[str, typing.Any]
    linkedResource: str
    name: str
    routineSpec: GoogleCloudDatacatalogV1RoutineSpec
    schema: GoogleCloudDatacatalogV1Schema
    sourceSystemTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    type: typing_extensions.Literal[
        "ENTRY_TYPE_UNSPECIFIED",
        "TABLE",
        "MODEL",
        "DATA_STREAM",
        "FILESET",
        "CLUSTER",
        "DATABASE",
        "DATA_SOURCE_CONNECTION",
        "ROUTINE",
        "SERVICE",
    ]
    usageSignal: GoogleCloudDatacatalogV1UsageSignal
    userSpecifiedSystem: str
    userSpecifiedType: str

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryGroup(typing_extensions.TypedDict, total=False):
    dataCatalogTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ExportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldType(typing_extensions.TypedDict, total=False):
    enumType: GoogleCloudDatacatalogV1FieldTypeEnumType
    primitiveType: typing_extensions.Literal[
        "PRIMITIVE_TYPE_UNSPECIFIED",
        "DOUBLE",
        "STRING",
        "BOOL",
        "TIMESTAMP",
        "RICHTEXT",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldTypeEnumType(
    typing_extensions.TypedDict, total=False
):
    allowedValues: typing.List[GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFileSpec(typing_extensions.TypedDict, total=False):
    filePath: str
    gcsTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    sizeBytes: str

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFilesetSpec(typing_extensions.TypedDict, total=False):
    filePatterns: typing.List[str]
    sampleGcsFileSpecs: typing.List[GoogleCloudDatacatalogV1GcsFileSpec]

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesRequest(
    typing_extensions.TypedDict, total=False
):
    crossRegionalSource: GoogleCloudDatacatalogV1CrossRegionalSource
    inlineSource: GoogleCloudDatacatalogV1InlineSource

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1InlineSource(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    entries: typing.List[GoogleCloudDatacatalogV1Entry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntryGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    entryGroups: typing.List[GoogleCloudDatacatalogV1EntryGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListPolicyTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policyTags: typing.List[GoogleCloudDatacatalogV1PolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tags: typing.List[GoogleCloudDatacatalogV1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    taxonomies: typing.List[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1PolicyTag(typing_extensions.TypedDict, total=False):
    childPolicyTags: typing.List[str]
    description: str
    displayName: str
    name: str
    parentPolicyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequest(
    typing_extensions.TypedDict, total=False
):
    newEnumValueDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1RenameTagTemplateFieldRequest(
    typing_extensions.TypedDict, total=False
):
    newTagTemplateFieldId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ReplaceTaxonomyRequest(
    typing_extensions.TypedDict, total=False
):
    serializedTaxonomy: GoogleCloudDatacatalogV1SerializedTaxonomy

@typing.type_check_only
class GoogleCloudDatacatalogV1RoutineSpec(typing_extensions.TypedDict, total=False):
    bigqueryRoutineSpec: GoogleCloudDatacatalogV1BigQueryRoutineSpec
    definitionBody: str
    language: str
    returnType: str
    routineArguments: typing.List[GoogleCloudDatacatalogV1RoutineSpecArgument]
    routineType: typing_extensions.Literal[
        "ROUTINE_TYPE_UNSPECIFIED", "SCALAR_FUNCTION", "PROCEDURE"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1RoutineSpecArgument(
    typing_extensions.TypedDict, total=False
):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]
    name: str
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Schema(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogRequest(
    typing_extensions.TypedDict, total=False
):
    orderBy: str
    pageSize: int
    pageToken: str
    query: str
    scope: GoogleCloudDatacatalogV1SearchCatalogRequestScope

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogRequestScope(
    typing_extensions.TypedDict, total=False
):
    includeGcpPublicDatasets: bool
    includeOrgIds: typing.List[str]
    includeProjectIds: typing.List[str]
    includePublicTagTemplates: bool
    restrictedLocations: typing.List[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    results: typing.List[GoogleCloudDatacatalogV1SearchCatalogResult]
    unreachable: typing.List[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResult(
    typing_extensions.TypedDict, total=False
):
    fullyQualifiedName: str
    integratedSystem: typing_extensions.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED",
        "BIGQUERY",
        "CLOUD_PUBSUB",
        "DATAPROC_METASTORE",
    ]
    linkedResource: str
    modifyTime: str
    relativeResourceName: str
    searchResultSubtype: str
    searchResultType: typing_extensions.Literal[
        "SEARCH_RESULT_TYPE_UNSPECIFIED", "ENTRY", "TAG_TEMPLATE", "ENTRY_GROUP"
    ]
    userSpecifiedSystem: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedPolicyTag(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedTaxonomy(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1SystemTimestamps(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    expireTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TableSpec(typing_extensions.TypedDict, total=False):
    groupedEntry: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Tag(typing_extensions.TypedDict, total=False):
    column: str
    fields: typing.Dict[str, typing.Any]
    name: str
    template: str
    templateDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagField(typing_extensions.TypedDict, total=False):
    boolValue: bool
    displayName: str
    doubleValue: float
    enumValue: GoogleCloudDatacatalogV1TagFieldEnumValue
    order: int
    richtextValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagFieldEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplate(typing_extensions.TypedDict, total=False):
    displayName: str
    fields: typing.Dict[str, typing.Any]
    isPubliclyReadable: bool
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplateField(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    isRequired: bool
    name: str
    order: int
    type: GoogleCloudDatacatalogV1FieldType

@typing.type_check_only
class GoogleCloudDatacatalogV1Taxonomy(typing_extensions.TypedDict, total=False):
    activatedPolicyTypes: typing.List[str]
    description: str
    displayName: str
    name: str
    policyTagCount: int
    taxonomyTimestamps: GoogleCloudDatacatalogV1SystemTimestamps

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageSignal(typing_extensions.TypedDict, total=False):
    updateTime: str
    usageWithinTimeRange: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageStats(typing_extensions.TypedDict, total=False):
    totalCancellations: float
    totalCompletions: float
    totalExecutionTimeForCompletionsMillis: float
    totalFailures: float

@typing.type_check_only
class GoogleCloudDatacatalogV1ViewSpec(typing_extensions.TypedDict, total=False):
    viewQuery: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
