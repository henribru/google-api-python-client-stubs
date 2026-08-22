import typing

_list = list

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryConnectionSpec(typing.TypedDict, total=False):
    cloudSql: GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec
    connectionType: typing.Literal["CONNECTION_TYPE_UNSPECIFIED", "CLOUD_SQL"]
    hasCredential: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryDateShardedSpec(typing.TypedDict, total=False):
    dataset: str
    latestShardResource: str
    shardCount: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryRoutineSpec(typing.TypedDict, total=False):
    importedLibraries: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryTableSpec(typing.TypedDict, total=False):
    tableSourceType: typing.Literal[
        "TABLE_SOURCE_TYPE_UNSPECIFIED",
        "BIGQUERY_VIEW",
        "BIGQUERY_TABLE",
        "BIGQUERY_MATERIALIZED_VIEW",
    ]
    tableSpec: GoogleCloudDatacatalogV1TableSpec
    viewSpec: GoogleCloudDatacatalogV1ViewSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1BusinessContext(typing.TypedDict, total=False):
    contacts: GoogleCloudDatacatalogV1Contacts
    entryOverview: GoogleCloudDatacatalogV1EntryOverview

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableInstanceSpec(typing.TypedDict, total=False):
    cloudBigtableClusterSpecs: _list[
        GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpec
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpec(
    typing.TypedDict, total=False
):
    displayName: str
    linkedResource: str
    location: str
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableSystemSpec(typing.TypedDict, total=False):
    instanceDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec(
    typing.TypedDict, total=False
):
    database: str
    instanceId: str
    type: typing.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchema(typing.TypedDict, total=False):
    column: str
    defaultValue: str
    description: str
    gcRule: str
    highestIndexingType: typing.Literal[
        "INDEXING_TYPE_UNSPECIFIED",
        "INDEXING_TYPE_NONE",
        "INDEXING_TYPE_NON_UNIQUE",
        "INDEXING_TYPE_UNIQUE",
        "INDEXING_TYPE_PRIMARY_KEY",
    ]
    lookerColumnSpec: GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpec
    mode: str
    ordinalPosition: int
    rangeElementType: GoogleCloudDatacatalogV1ColumnSchemaFieldElementType
    subcolumns: _list[GoogleCloudDatacatalogV1ColumnSchema]
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchemaFieldElementType(
    typing.TypedDict, total=False
):
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpec(
    typing.TypedDict, total=False
):
    type: typing.Literal[
        "LOOKER_COLUMN_TYPE_UNSPECIFIED",
        "DIMENSION",
        "DIMENSION_GROUP",
        "FILTER",
        "MEASURE",
        "PARAMETER",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1CommonUsageStats(typing.TypedDict, total=False):
    viewCount: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Contacts(typing.TypedDict, total=False):
    people: _list[GoogleCloudDatacatalogV1ContactsPerson]

@typing.type_check_only
class GoogleCloudDatacatalogV1ContactsPerson(typing.TypedDict, total=False):
    designation: str
    email: str

@typing.type_check_only
class GoogleCloudDatacatalogV1CrossRegionalSource(typing.TypedDict, total=False):
    taxonomy: str

@typing.type_check_only
class GoogleCloudDatacatalogV1DataSource(typing.TypedDict, total=False):
    resource: str
    service: typing.Literal["SERVICE_UNSPECIFIED", "CLOUD_STORAGE", "BIGQUERY"]
    sourceEntry: str
    storageProperties: GoogleCloudDatacatalogV1StorageProperties

@typing.type_check_only
class GoogleCloudDatacatalogV1DataSourceConnectionSpec(typing.TypedDict, total=False):
    bigqueryConnectionSpec: GoogleCloudDatacatalogV1BigQueryConnectionSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DatabaseTableSpec(typing.TypedDict, total=False):
    databaseViewSpec: GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec
    dataplexTable: GoogleCloudDatacatalogV1DataplexTableSpec
    type: typing.Literal["TABLE_TYPE_UNSPECIFIED", "NATIVE", "EXTERNAL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec(
    typing.TypedDict, total=False
):
    baseTable: str
    sqlQuery: str
    viewType: typing.Literal[
        "VIEW_TYPE_UNSPECIFIED", "STANDARD_VIEW", "MATERIALIZED_VIEW"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexExternalTable(typing.TypedDict, total=False):
    dataCatalogEntry: str
    fullyQualifiedName: str
    googleCloudResource: str
    system: typing.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED",
        "BIGQUERY",
        "CLOUD_PUBSUB",
        "DATAPROC_METASTORE",
        "DATAPLEX",
        "CLOUD_SPANNER",
        "CLOUD_BIGTABLE",
        "CLOUD_SQL",
        "LOOKER",
        "VERTEX_AI",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexFilesetSpec(typing.TypedDict, total=False):
    dataplexSpec: GoogleCloudDatacatalogV1DataplexSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexSpec(typing.TypedDict, total=False):
    asset: str
    compressionFormat: str
    dataFormat: GoogleCloudDatacatalogV1PhysicalSchema
    projectId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexTableSpec(typing.TypedDict, total=False):
    dataplexSpec: GoogleCloudDatacatalogV1DataplexSpec
    externalTables: _list[GoogleCloudDatacatalogV1DataplexExternalTable]
    userManaged: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1DatasetSpec(typing.TypedDict, total=False):
    vertexDatasetSpec: GoogleCloudDatacatalogV1VertexDatasetSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DumpItem(typing.TypedDict, total=False):
    taggedEntry: GoogleCloudDatacatalogV1TaggedEntry

@typing.type_check_only
class GoogleCloudDatacatalogV1Entry(typing.TypedDict, total=False):
    bigqueryDateShardedSpec: GoogleCloudDatacatalogV1BigQueryDateShardedSpec
    bigqueryTableSpec: GoogleCloudDatacatalogV1BigQueryTableSpec
    businessContext: GoogleCloudDatacatalogV1BusinessContext
    cloudBigtableSystemSpec: GoogleCloudDatacatalogV1CloudBigtableSystemSpec
    dataSource: GoogleCloudDatacatalogV1DataSource
    dataSourceConnectionSpec: GoogleCloudDatacatalogV1DataSourceConnectionSpec
    databaseTableSpec: GoogleCloudDatacatalogV1DatabaseTableSpec
    datasetSpec: GoogleCloudDatacatalogV1DatasetSpec
    description: str
    displayName: str
    featureOnlineStoreSpec: GoogleCloudDatacatalogV1FeatureOnlineStoreSpec
    filesetSpec: GoogleCloudDatacatalogV1FilesetSpec
    fullyQualifiedName: str
    gcsFilesetSpec: GoogleCloudDatacatalogV1GcsFilesetSpec
    graphSpec: GoogleCloudDatacatalogV1GraphSpec
    integratedSystem: typing.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED",
        "BIGQUERY",
        "CLOUD_PUBSUB",
        "DATAPROC_METASTORE",
        "DATAPLEX",
        "CLOUD_SPANNER",
        "CLOUD_BIGTABLE",
        "CLOUD_SQL",
        "LOOKER",
        "VERTEX_AI",
    ]
    labels: dict[str, typing.Any]
    linkedResource: str
    lookerSystemSpec: GoogleCloudDatacatalogV1LookerSystemSpec
    modelSpec: GoogleCloudDatacatalogV1ModelSpec
    name: str
    personalDetails: GoogleCloudDatacatalogV1PersonalDetails
    routineSpec: GoogleCloudDatacatalogV1RoutineSpec
    schema: GoogleCloudDatacatalogV1Schema
    serviceSpec: GoogleCloudDatacatalogV1ServiceSpec
    sourceSystemTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    spannerTableSpec: GoogleCloudDatacatalogV1SpannerTableSpec
    sqlDatabaseSystemSpec: GoogleCloudDatacatalogV1SqlDatabaseSystemSpec
    type: typing.Literal[
        "ENTRY_TYPE_UNSPECIFIED",
        "TABLE",
        "MODEL",
        "DATA_STREAM",
        "FILESET",
        "CLUSTER",
        "DATABASE",
        "DATA_SOURCE_CONNECTION",
        "ROUTINE",
        "LAKE",
        "ZONE",
        "SERVICE",
        "DATABASE_SCHEMA",
        "DASHBOARD",
        "EXPLORE",
        "LOOK",
        "FEATURE_ONLINE_STORE",
        "FEATURE_VIEW",
        "FEATURE_GROUP",
        "GRAPH",
    ]
    usageSignal: GoogleCloudDatacatalogV1UsageSignal
    userSpecifiedSystem: str
    userSpecifiedType: str

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryGroup(typing.TypedDict, total=False):
    dataCatalogTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    description: str
    displayName: str
    name: str
    transferredToDataplex: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryOverview(typing.TypedDict, total=False):
    overview: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ExportTaxonomiesResponse(typing.TypedDict, total=False):
    taxonomies: _list[GoogleCloudDatacatalogV1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1FeatureOnlineStoreSpec(typing.TypedDict, total=False):
    storageType: typing.Literal["STORAGE_TYPE_UNSPECIFIED", "BIGTABLE", "OPTIMIZED"]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldType(typing.TypedDict, total=False):
    enumType: GoogleCloudDatacatalogV1FieldTypeEnumType
    primitiveType: typing.Literal[
        "PRIMITIVE_TYPE_UNSPECIFIED",
        "DOUBLE",
        "STRING",
        "BOOL",
        "TIMESTAMP",
        "RICHTEXT",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldTypeEnumType(typing.TypedDict, total=False):
    allowedValues: _list[GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1FilesetSpec(typing.TypedDict, total=False):
    dataplexFileset: GoogleCloudDatacatalogV1DataplexFilesetSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFileSpec(typing.TypedDict, total=False):
    filePath: str
    gcsTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    sizeBytes: str

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFilesetSpec(typing.TypedDict, total=False):
    filePatterns: _list[str]
    sampleGcsFileSpecs: _list[GoogleCloudDatacatalogV1GcsFileSpec]

@typing.type_check_only
class GoogleCloudDatacatalogV1GraphSpec(typing.TypedDict, total=False):
    edgeTables: _list[GoogleCloudDatacatalogV1GraphSpecGraphElementTable]
    name: str
    nodeTables: _list[GoogleCloudDatacatalogV1GraphSpecGraphElementTable]

@typing.type_check_only
class GoogleCloudDatacatalogV1GraphSpecGraphElementTable(typing.TypedDict, total=False):
    alias: str
    dataSource: str
    destinationNodeReference: (
        GoogleCloudDatacatalogV1GraphSpecGraphElementTableGraphNodeReference
    )
    dynamicLabelColumn: str
    dynamicPropertiesColumn: str
    elementKeys: _list[str]
    inputSource: typing.Literal["INPUT_SOURCE_UNSPECIFIED", "TABLE", "VIEW"]
    kind: typing.Literal["KIND_UNSPECIFIED", "NODE", "EDGE"]
    labelAndProperties: _list[
        GoogleCloudDatacatalogV1GraphSpecGraphElementTableLabelAndProperties
    ]
    sourceNodeReference: (
        GoogleCloudDatacatalogV1GraphSpecGraphElementTableGraphNodeReference
    )

@typing.type_check_only
class GoogleCloudDatacatalogV1GraphSpecGraphElementTableGraphNodeReference(
    typing.TypedDict, total=False
):
    edgeTableColumns: _list[str]
    nodeAlias: str
    nodeTableColumns: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1GraphSpecGraphElementTableLabelAndProperties(
    typing.TypedDict, total=False
):
    label: str
    properties: _list[GoogleCloudDatacatalogV1GraphSpecGraphElementTableProperty]

@typing.type_check_only
class GoogleCloudDatacatalogV1GraphSpecGraphElementTableProperty(
    typing.TypedDict, total=False
):
    name: str
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesMetadata(typing.TypedDict, total=False):
    errors: _list[Status]
    state: typing.Literal[
        "IMPORT_STATE_UNSPECIFIED",
        "IMPORT_QUEUED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_DONE",
        "IMPORT_OBSOLETE",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesRequest(typing.TypedDict, total=False):
    gcsBucketPath: str
    jobId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesResponse(typing.TypedDict, total=False):
    deletedEntriesCount: str
    upsertedEntriesCount: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesRequest(typing.TypedDict, total=False):
    crossRegionalSource: GoogleCloudDatacatalogV1CrossRegionalSource
    inlineSource: GoogleCloudDatacatalogV1InlineSource

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportTaxonomiesResponse(typing.TypedDict, total=False):
    taxonomies: _list[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1InlineSource(typing.TypedDict, total=False):
    taxonomies: _list[GoogleCloudDatacatalogV1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntriesResponse(typing.TypedDict, total=False):
    entries: _list[GoogleCloudDatacatalogV1Entry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntryGroupsResponse(typing.TypedDict, total=False):
    entryGroups: _list[GoogleCloudDatacatalogV1EntryGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListPolicyTagsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policyTags: _list[GoogleCloudDatacatalogV1PolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTagsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tags: _list[GoogleCloudDatacatalogV1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTaxonomiesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    taxonomies: _list[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1LookerSystemSpec(typing.TypedDict, total=False):
    parentInstanceDisplayName: str
    parentInstanceId: str
    parentModelDisplayName: str
    parentModelId: str
    parentViewDisplayName: str
    parentViewId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1MigrationConfig(typing.TypedDict, total=False):
    catalogUiExperience: typing.Literal[
        "CATALOG_UI_EXPERIENCE_UNSPECIFIED",
        "CATALOG_UI_EXPERIENCE_ENABLED",
        "CATALOG_UI_EXPERIENCE_DISABLED",
    ]
    tagTemplateMigration: typing.Literal[
        "TAG_TEMPLATE_MIGRATION_UNSPECIFIED",
        "TAG_TEMPLATE_MIGRATION_ENABLED",
        "TAG_TEMPLATE_MIGRATION_DISABLED",
    ]
    templateMigrationEnabledTime: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ModelSpec(typing.TypedDict, total=False):
    vertexModelSpec: GoogleCloudDatacatalogV1VertexModelSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1ModifyEntryContactsRequest(typing.TypedDict, total=False):
    contacts: GoogleCloudDatacatalogV1Contacts

@typing.type_check_only
class GoogleCloudDatacatalogV1ModifyEntryOverviewRequest(typing.TypedDict, total=False):
    entryOverview: GoogleCloudDatacatalogV1EntryOverview

@typing.type_check_only
class GoogleCloudDatacatalogV1OrganizationConfig(typing.TypedDict, total=False):
    config: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1PersonalDetails(typing.TypedDict, total=False):
    starTime: str
    starred: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchema(typing.TypedDict, total=False):
    avro: GoogleCloudDatacatalogV1PhysicalSchemaAvroSchema
    csv: GoogleCloudDatacatalogV1PhysicalSchemaCsvSchema
    orc: GoogleCloudDatacatalogV1PhysicalSchemaOrcSchema
    parquet: GoogleCloudDatacatalogV1PhysicalSchemaParquetSchema
    protobuf: GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchema
    thrift: GoogleCloudDatacatalogV1PhysicalSchemaThriftSchema

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaAvroSchema(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaCsvSchema(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaOrcSchema(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaParquetSchema(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchema(
    typing.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaThriftSchema(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PolicyTag(typing.TypedDict, total=False):
    childPolicyTags: _list[str]
    description: str
    displayName: str
    name: str
    parentPolicyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsMetadata(typing.TypedDict, total=False):
    errors: dict[str, typing.Any]
    state: typing.Literal[
        "RECONCILIATION_STATE_UNSPECIFIED",
        "RECONCILIATION_QUEUED",
        "RECONCILIATION_IN_PROGRESS",
        "RECONCILIATION_DONE",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsRequest(typing.TypedDict, total=False):
    forceDeleteMissing: bool
    tagTemplate: str
    tags: _list[GoogleCloudDatacatalogV1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsResponse(typing.TypedDict, total=False):
    createdTagsCount: str
    deletedTagsCount: str
    updatedTagsCount: str

@typing.type_check_only
class GoogleCloudDatacatalogV1RenameTagTemplateFieldEnumValueRequest(
    typing.TypedDict, total=False
):
    newEnumValueDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1RenameTagTemplateFieldRequest(
    typing.TypedDict, total=False
):
    newTagTemplateFieldId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ReplaceTaxonomyRequest(typing.TypedDict, total=False):
    serializedTaxonomy: GoogleCloudDatacatalogV1SerializedTaxonomy

@typing.type_check_only
class GoogleCloudDatacatalogV1RoutineSpec(typing.TypedDict, total=False):
    bigqueryRoutineSpec: GoogleCloudDatacatalogV1BigQueryRoutineSpec
    definitionBody: str
    language: str
    returnType: str
    routineArguments: _list[GoogleCloudDatacatalogV1RoutineSpecArgument]
    routineType: typing.Literal[
        "ROUTINE_TYPE_UNSPECIFIED", "SCALAR_FUNCTION", "PROCEDURE"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1RoutineSpecArgument(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "IN", "OUT", "INOUT"]
    name: str
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Schema(typing.TypedDict, total=False):
    columns: _list[GoogleCloudDatacatalogV1ColumnSchema]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogRequest(typing.TypedDict, total=False):
    adminSearch: bool
    orderBy: str
    pageSize: int
    pageToken: str
    query: str
    scope: GoogleCloudDatacatalogV1SearchCatalogRequestScope

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogRequestScope(typing.TypedDict, total=False):
    includeGcpPublicDatasets: bool
    includeOrgIds: _list[str]
    includeProjectIds: _list[str]
    includePublicTagTemplates: bool
    restrictedLocations: _list[str]
    starredOnly: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[GoogleCloudDatacatalogV1SearchCatalogResult]
    totalSize: int
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResult(typing.TypedDict, total=False):
    description: str
    displayName: str
    fullyQualifiedName: str
    integratedSystem: typing.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED",
        "BIGQUERY",
        "CLOUD_PUBSUB",
        "DATAPROC_METASTORE",
        "DATAPLEX",
        "CLOUD_SPANNER",
        "CLOUD_BIGTABLE",
        "CLOUD_SQL",
        "LOOKER",
        "VERTEX_AI",
    ]
    linkedResource: str
    modifyTime: str
    relativeResourceName: str
    searchResultSubtype: str
    searchResultType: typing.Literal[
        "SEARCH_RESULT_TYPE_UNSPECIFIED", "ENTRY", "TAG_TEMPLATE", "ENTRY_GROUP"
    ]
    userSpecifiedSystem: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedPolicyTag(typing.TypedDict, total=False):
    childPolicyTags: _list[GoogleCloudDatacatalogV1SerializedPolicyTag]
    description: str
    displayName: str
    policyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedTaxonomy(typing.TypedDict, total=False):
    activatedPolicyTypes: _list[
        typing.Literal["POLICY_TYPE_UNSPECIFIED", "FINE_GRAINED_ACCESS_CONTROL"]
    ]
    description: str
    displayName: str
    policyTags: _list[GoogleCloudDatacatalogV1SerializedPolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ServiceSpec(typing.TypedDict, total=False):
    cloudBigtableInstanceSpec: GoogleCloudDatacatalogV1CloudBigtableInstanceSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1SetConfigRequest(typing.TypedDict, total=False):
    catalogUiExperience: typing.Literal[
        "CATALOG_UI_EXPERIENCE_UNSPECIFIED",
        "CATALOG_UI_EXPERIENCE_ENABLED",
        "CATALOG_UI_EXPERIENCE_DISABLED",
    ]
    tagTemplateMigration: typing.Literal[
        "TAG_TEMPLATE_MIGRATION_UNSPECIFIED",
        "TAG_TEMPLATE_MIGRATION_ENABLED",
        "TAG_TEMPLATE_MIGRATION_DISABLED",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1SpannerTableSpec(typing.TypedDict, total=False):
    foreignKeys: _list[GoogleCloudDatacatalogV1SpannerTableSpecSpannerForeignKey]
    primaryKey: GoogleCloudDatacatalogV1SpannerTableSpecSpannerPrimaryKey

@typing.type_check_only
class GoogleCloudDatacatalogV1SpannerTableSpecSpannerForeignKey(
    typing.TypedDict, total=False
):
    columnMappings: _list[
        GoogleCloudDatacatalogV1SpannerTableSpecSpannerForeignKeyForeignKeyColumnMapping
    ]
    entry: str
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SpannerTableSpecSpannerForeignKeyForeignKeyColumnMapping(
    typing.TypedDict, total=False
):
    column: str
    referenceColumn: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SpannerTableSpecSpannerPrimaryKey(
    typing.TypedDict, total=False
):
    columns: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1SqlDatabaseSystemSpec(typing.TypedDict, total=False):
    databaseVersion: str
    instanceHost: str
    sqlEngine: str

@typing.type_check_only
class GoogleCloudDatacatalogV1StarEntryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1StarEntryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1StorageProperties(typing.TypedDict, total=False):
    filePattern: _list[str]
    fileType: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SystemTimestamps(typing.TypedDict, total=False):
    createTime: str
    expireTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TableSpec(typing.TypedDict, total=False):
    groupedEntry: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Tag(typing.TypedDict, total=False):
    column: str
    dataplexTransferStatus: typing.Literal[
        "DATAPLEX_TRANSFER_STATUS_UNSPECIFIED", "MIGRATED", "TRANSFERRED"
    ]
    fields: dict[str, typing.Any]
    name: str
    template: str
    templateDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagField(typing.TypedDict, total=False):
    boolValue: bool
    displayName: str
    doubleValue: float
    enumValue: GoogleCloudDatacatalogV1TagFieldEnumValue
    order: int
    richtextValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagFieldEnumValue(typing.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplate(typing.TypedDict, total=False):
    dataplexTransferStatus: typing.Literal[
        "DATAPLEX_TRANSFER_STATUS_UNSPECIFIED", "MIGRATED", "TRANSFERRED"
    ]
    displayName: str
    fields: dict[str, typing.Any]
    isPubliclyReadable: bool
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1TagTemplateField(typing.TypedDict, total=False):
    description: str
    displayName: str
    isRequired: bool
    name: str
    order: int
    type: GoogleCloudDatacatalogV1FieldType

@typing.type_check_only
class GoogleCloudDatacatalogV1TaggedEntry(typing.TypedDict, total=False):
    absentTags: _list[GoogleCloudDatacatalogV1Tag]
    presentTags: _list[GoogleCloudDatacatalogV1Tag]
    v1Entry: GoogleCloudDatacatalogV1Entry

@typing.type_check_only
class GoogleCloudDatacatalogV1Taxonomy(typing.TypedDict, total=False):
    activatedPolicyTypes: _list[
        typing.Literal["POLICY_TYPE_UNSPECIFIED", "FINE_GRAINED_ACCESS_CONTROL"]
    ]
    description: str
    displayName: str
    name: str
    policyTagCount: int
    service: GoogleCloudDatacatalogV1TaxonomyService
    taxonomyTimestamps: GoogleCloudDatacatalogV1SystemTimestamps

@typing.type_check_only
class GoogleCloudDatacatalogV1TaxonomyService(typing.TypedDict, total=False):
    identity: str
    name: typing.Literal[
        "MANAGING_SYSTEM_UNSPECIFIED",
        "MANAGING_SYSTEM_DATAPLEX",
        "MANAGING_SYSTEM_OTHER",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1UnstarEntryRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1UnstarEntryResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageSignal(typing.TypedDict, total=False):
    commonUsageWithinTimeRange: dict[str, typing.Any]
    favoriteCount: str
    updateTime: str
    usageWithinTimeRange: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageStats(typing.TypedDict, total=False):
    totalCancellations: float
    totalCompletions: float
    totalExecutionTimeForCompletionsMillis: float
    totalFailures: float

@typing.type_check_only
class GoogleCloudDatacatalogV1VertexDatasetSpec(typing.TypedDict, total=False):
    dataItemCount: str
    dataType: typing.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "TABLE",
        "IMAGE",
        "TEXT",
        "VIDEO",
        "CONVERSATION",
        "TIME_SERIES",
        "DOCUMENT",
        "TEXT_TO_SPEECH",
        "TRANSLATION",
        "STORE_VISION",
        "ENTERPRISE_KNOWLEDGE_GRAPH",
        "TEXT_PROMPT",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1VertexModelSourceInfo(typing.TypedDict, total=False):
    copy: bool
    sourceType: typing.Literal[
        "MODEL_SOURCE_TYPE_UNSPECIFIED",
        "AUTOML",
        "CUSTOM",
        "BQML",
        "MODEL_GARDEN",
        "GENIE",
        "CUSTOM_TEXT_EMBEDDING",
        "MARKETPLACE",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1VertexModelSpec(typing.TypedDict, total=False):
    containerImageUri: str
    versionAliases: _list[str]
    versionDescription: str
    versionId: str
    vertexModelSourceInfo: GoogleCloudDatacatalogV1VertexModelSourceInfo

@typing.type_check_only
class GoogleCloudDatacatalogV1ViewSpec(typing.TypedDict, total=False):
    viewQuery: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

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
