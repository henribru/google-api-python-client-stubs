import typing

import typing_extensions

_list = list

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
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
    latestShardResource: str
    shardCount: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudDatacatalogV1BigQueryRoutineSpec(
    typing_extensions.TypedDict, total=False
):
    importedLibraries: _list[str]

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
class GoogleCloudDatacatalogV1BusinessContext(typing_extensions.TypedDict, total=False):
    contacts: GoogleCloudDatacatalogV1Contacts
    entryOverview: GoogleCloudDatacatalogV1EntryOverview

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableInstanceSpec(
    typing_extensions.TypedDict, total=False
):
    cloudBigtableClusterSpecs: _list[
        GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpec
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableInstanceSpecCloudBigtableClusterSpec(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    linkedResource: str
    location: str
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudBigtableSystemSpec(
    typing_extensions.TypedDict, total=False
):
    instanceDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1CloudSqlBigQueryConnectionSpec(
    typing_extensions.TypedDict, total=False
):
    database: str
    instanceId: str
    type: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchema(typing_extensions.TypedDict, total=False):
    column: str
    defaultValue: str
    description: str
    gcRule: str
    highestIndexingType: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    type: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpec(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal[
        "LOOKER_COLUMN_TYPE_UNSPECIFIED",
        "DIMENSION",
        "DIMENSION_GROUP",
        "FILTER",
        "MEASURE",
        "PARAMETER",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1CommonUsageStats(
    typing_extensions.TypedDict, total=False
):
    viewCount: str

@typing.type_check_only
class GoogleCloudDatacatalogV1Contacts(typing_extensions.TypedDict, total=False):
    people: _list[GoogleCloudDatacatalogV1ContactsPerson]

@typing.type_check_only
class GoogleCloudDatacatalogV1ContactsPerson(typing_extensions.TypedDict, total=False):
    designation: str
    email: str

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
    sourceEntry: str
    storageProperties: GoogleCloudDatacatalogV1StorageProperties

@typing.type_check_only
class GoogleCloudDatacatalogV1DataSourceConnectionSpec(
    typing_extensions.TypedDict, total=False
):
    bigqueryConnectionSpec: GoogleCloudDatacatalogV1BigQueryConnectionSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DatabaseTableSpec(
    typing_extensions.TypedDict, total=False
):
    databaseViewSpec: GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec
    dataplexTable: GoogleCloudDatacatalogV1DataplexTableSpec
    type: typing_extensions.Literal["TABLE_TYPE_UNSPECIFIED", "NATIVE", "EXTERNAL"]

@typing.type_check_only
class GoogleCloudDatacatalogV1DatabaseTableSpecDatabaseViewSpec(
    typing_extensions.TypedDict, total=False
):
    baseTable: str
    sqlQuery: str
    viewType: typing_extensions.Literal[
        "VIEW_TYPE_UNSPECIFIED", "STANDARD_VIEW", "MATERIALIZED_VIEW"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexExternalTable(
    typing_extensions.TypedDict, total=False
):
    dataCatalogEntry: str
    fullyQualifiedName: str
    googleCloudResource: str
    system: typing_extensions.Literal[
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
class GoogleCloudDatacatalogV1DataplexFilesetSpec(
    typing_extensions.TypedDict, total=False
):
    dataplexSpec: GoogleCloudDatacatalogV1DataplexSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexSpec(typing_extensions.TypedDict, total=False):
    asset: str
    compressionFormat: str
    dataFormat: GoogleCloudDatacatalogV1PhysicalSchema
    projectId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1DataplexTableSpec(
    typing_extensions.TypedDict, total=False
):
    dataplexSpec: GoogleCloudDatacatalogV1DataplexSpec
    externalTables: _list[GoogleCloudDatacatalogV1DataplexExternalTable]
    userManaged: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1DatasetSpec(typing_extensions.TypedDict, total=False):
    vertexDatasetSpec: GoogleCloudDatacatalogV1VertexDatasetSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1DumpItem(typing_extensions.TypedDict, total=False):
    taggedEntry: GoogleCloudDatacatalogV1TaggedEntry

@typing.type_check_only
class GoogleCloudDatacatalogV1Entry(typing_extensions.TypedDict, total=False):
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
    integratedSystem: typing_extensions.Literal[
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
    sqlDatabaseSystemSpec: GoogleCloudDatacatalogV1SqlDatabaseSystemSpec
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
    transferredToDataplex: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1EntryOverview(typing_extensions.TypedDict, total=False):
    overview: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ExportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: _list[GoogleCloudDatacatalogV1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1FeatureOnlineStoreSpec(
    typing_extensions.TypedDict, total=False
):
    storageType: typing_extensions.Literal[
        "STORAGE_TYPE_UNSPECIFIED", "BIGTABLE", "OPTIMIZED"
    ]

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
    allowedValues: _list[GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue]

@typing.type_check_only
class GoogleCloudDatacatalogV1FieldTypeEnumTypeEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1FilesetSpec(typing_extensions.TypedDict, total=False):
    dataplexFileset: GoogleCloudDatacatalogV1DataplexFilesetSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFileSpec(typing_extensions.TypedDict, total=False):
    filePath: str
    gcsTimestamps: GoogleCloudDatacatalogV1SystemTimestamps
    sizeBytes: str

@typing.type_check_only
class GoogleCloudDatacatalogV1GcsFilesetSpec(typing_extensions.TypedDict, total=False):
    filePatterns: _list[str]
    sampleGcsFileSpecs: _list[GoogleCloudDatacatalogV1GcsFileSpec]

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: _list[Status]
    state: typing_extensions.Literal[
        "IMPORT_STATE_UNSPECIFIED",
        "IMPORT_QUEUED",
        "IMPORT_IN_PROGRESS",
        "IMPORT_DONE",
        "IMPORT_OBSOLETE",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesRequest(
    typing_extensions.TypedDict, total=False
):
    gcsBucketPath: str
    jobId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ImportEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    deletedEntriesCount: str
    upsertedEntriesCount: str

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
    taxonomies: _list[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1InlineSource(typing_extensions.TypedDict, total=False):
    taxonomies: _list[GoogleCloudDatacatalogV1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDatacatalogV1Entry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListEntryGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    entryGroups: _list[GoogleCloudDatacatalogV1EntryGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ListPolicyTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policyTags: _list[GoogleCloudDatacatalogV1PolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tags: _list[GoogleCloudDatacatalogV1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ListTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    taxonomies: _list[GoogleCloudDatacatalogV1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1LookerSystemSpec(
    typing_extensions.TypedDict, total=False
):
    parentInstanceDisplayName: str
    parentInstanceId: str
    parentModelDisplayName: str
    parentModelId: str
    parentViewDisplayName: str
    parentViewId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1MigrationConfig(typing_extensions.TypedDict, total=False):
    catalogUiExperience: typing_extensions.Literal[
        "CATALOG_UI_EXPERIENCE_UNSPECIFIED",
        "CATALOG_UI_EXPERIENCE_ENABLED",
        "CATALOG_UI_EXPERIENCE_DISABLED",
    ]
    tagTemplateMigration: typing_extensions.Literal[
        "TAG_TEMPLATE_MIGRATION_UNSPECIFIED",
        "TAG_TEMPLATE_MIGRATION_ENABLED",
        "TAG_TEMPLATE_MIGRATION_DISABLED",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1ModelSpec(typing_extensions.TypedDict, total=False):
    vertexModelSpec: GoogleCloudDatacatalogV1VertexModelSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1ModifyEntryContactsRequest(
    typing_extensions.TypedDict, total=False
):
    contacts: GoogleCloudDatacatalogV1Contacts

@typing.type_check_only
class GoogleCloudDatacatalogV1ModifyEntryOverviewRequest(
    typing_extensions.TypedDict, total=False
):
    entryOverview: GoogleCloudDatacatalogV1EntryOverview

@typing.type_check_only
class GoogleCloudDatacatalogV1OrganizationConfig(
    typing_extensions.TypedDict, total=False
):
    config: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1PersonalDetails(typing_extensions.TypedDict, total=False):
    starTime: str
    starred: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchema(typing_extensions.TypedDict, total=False):
    avro: GoogleCloudDatacatalogV1PhysicalSchemaAvroSchema
    csv: GoogleCloudDatacatalogV1PhysicalSchemaCsvSchema
    orc: GoogleCloudDatacatalogV1PhysicalSchemaOrcSchema
    parquet: GoogleCloudDatacatalogV1PhysicalSchemaParquetSchema
    protobuf: GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchema
    thrift: GoogleCloudDatacatalogV1PhysicalSchemaThriftSchema

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaAvroSchema(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaCsvSchema(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaOrcSchema(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaParquetSchema(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaProtobufSchema(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PhysicalSchemaThriftSchema(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class GoogleCloudDatacatalogV1PolicyTag(typing_extensions.TypedDict, total=False):
    childPolicyTags: _list[str]
    description: str
    displayName: str
    name: str
    parentPolicyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsMetadata(
    typing_extensions.TypedDict, total=False
):
    errors: dict[str, typing.Any]
    state: typing_extensions.Literal[
        "RECONCILIATION_STATE_UNSPECIFIED",
        "RECONCILIATION_QUEUED",
        "RECONCILIATION_IN_PROGRESS",
        "RECONCILIATION_DONE",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsRequest(
    typing_extensions.TypedDict, total=False
):
    forceDeleteMissing: bool
    tagTemplate: str
    tags: _list[GoogleCloudDatacatalogV1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ReconcileTagsResponse(
    typing_extensions.TypedDict, total=False
):
    createdTagsCount: str
    deletedTagsCount: str
    updatedTagsCount: str

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
    routineArguments: _list[GoogleCloudDatacatalogV1RoutineSpecArgument]
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
class GoogleCloudDatacatalogV1Schema(typing_extensions.TypedDict, total=False):
    columns: _list[GoogleCloudDatacatalogV1ColumnSchema]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogRequest(
    typing_extensions.TypedDict, total=False
):
    adminSearch: bool
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
    includeOrgIds: _list[str]
    includeProjectIds: _list[str]
    includePublicTagTemplates: bool
    restrictedLocations: _list[str]
    starredOnly: bool

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    results: _list[GoogleCloudDatacatalogV1SearchCatalogResult]
    totalSize: int
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1SearchCatalogResult(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    fullyQualifiedName: str
    integratedSystem: typing_extensions.Literal[
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
    searchResultType: typing_extensions.Literal[
        "SEARCH_RESULT_TYPE_UNSPECIFIED", "ENTRY", "TAG_TEMPLATE", "ENTRY_GROUP"
    ]
    userSpecifiedSystem: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedPolicyTag(
    typing_extensions.TypedDict, total=False
):
    childPolicyTags: _list[GoogleCloudDatacatalogV1SerializedPolicyTag]
    description: str
    displayName: str
    policyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1SerializedTaxonomy(
    typing_extensions.TypedDict, total=False
):
    activatedPolicyTypes: _list[
        typing_extensions.Literal[
            "POLICY_TYPE_UNSPECIFIED", "FINE_GRAINED_ACCESS_CONTROL"
        ]
    ]
    description: str
    displayName: str
    policyTags: _list[GoogleCloudDatacatalogV1SerializedPolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1ServiceSpec(typing_extensions.TypedDict, total=False):
    cloudBigtableInstanceSpec: GoogleCloudDatacatalogV1CloudBigtableInstanceSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1SetConfigRequest(
    typing_extensions.TypedDict, total=False
):
    catalogUiExperience: typing_extensions.Literal[
        "CATALOG_UI_EXPERIENCE_UNSPECIFIED",
        "CATALOG_UI_EXPERIENCE_ENABLED",
        "CATALOG_UI_EXPERIENCE_DISABLED",
    ]
    tagTemplateMigration: typing_extensions.Literal[
        "TAG_TEMPLATE_MIGRATION_UNSPECIFIED",
        "TAG_TEMPLATE_MIGRATION_ENABLED",
        "TAG_TEMPLATE_MIGRATION_DISABLED",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1SqlDatabaseSystemSpec(
    typing_extensions.TypedDict, total=False
):
    databaseVersion: str
    instanceHost: str
    sqlEngine: str

@typing.type_check_only
class GoogleCloudDatacatalogV1StarEntryRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1StarEntryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1StorageProperties(
    typing_extensions.TypedDict, total=False
):
    filePattern: _list[str]
    fileType: str

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
    dataplexTransferStatus: typing_extensions.Literal[
        "DATAPLEX_TRANSFER_STATUS_UNSPECIFIED", "MIGRATED", "TRANSFERRED"
    ]
    fields: dict[str, typing.Any]
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
    dataplexTransferStatus: typing_extensions.Literal[
        "DATAPLEX_TRANSFER_STATUS_UNSPECIFIED", "MIGRATED", "TRANSFERRED"
    ]
    displayName: str
    fields: dict[str, typing.Any]
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
class GoogleCloudDatacatalogV1TaggedEntry(typing_extensions.TypedDict, total=False):
    absentTags: _list[GoogleCloudDatacatalogV1Tag]
    presentTags: _list[GoogleCloudDatacatalogV1Tag]
    v1Entry: GoogleCloudDatacatalogV1Entry

@typing.type_check_only
class GoogleCloudDatacatalogV1Taxonomy(typing_extensions.TypedDict, total=False):
    activatedPolicyTypes: _list[
        typing_extensions.Literal[
            "POLICY_TYPE_UNSPECIFIED", "FINE_GRAINED_ACCESS_CONTROL"
        ]
    ]
    description: str
    displayName: str
    name: str
    policyTagCount: int
    service: GoogleCloudDatacatalogV1TaxonomyService
    taxonomyTimestamps: GoogleCloudDatacatalogV1SystemTimestamps

@typing.type_check_only
class GoogleCloudDatacatalogV1TaxonomyService(typing_extensions.TypedDict, total=False):
    identity: str
    name: typing_extensions.Literal[
        "MANAGING_SYSTEM_UNSPECIFIED",
        "MANAGING_SYSTEM_DATAPLEX",
        "MANAGING_SYSTEM_OTHER",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1UnstarEntryRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1UnstarEntryResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageSignal(typing_extensions.TypedDict, total=False):
    commonUsageWithinTimeRange: dict[str, typing.Any]
    favoriteCount: str
    updateTime: str
    usageWithinTimeRange: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1UsageStats(typing_extensions.TypedDict, total=False):
    totalCancellations: float
    totalCompletions: float
    totalExecutionTimeForCompletionsMillis: float
    totalFailures: float

@typing.type_check_only
class GoogleCloudDatacatalogV1VertexDatasetSpec(
    typing_extensions.TypedDict, total=False
):
    dataItemCount: str
    dataType: typing_extensions.Literal[
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
class GoogleCloudDatacatalogV1VertexModelSourceInfo(
    typing_extensions.TypedDict, total=False
):
    copy: bool
    sourceType: typing_extensions.Literal[
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
class GoogleCloudDatacatalogV1VertexModelSpec(typing_extensions.TypedDict, total=False):
    containerImageUri: str
    versionAliases: _list[str]
    versionDescription: str
    versionId: str
    vertexModelSourceInfo: GoogleCloudDatacatalogV1VertexModelSourceInfo

@typing.type_check_only
class GoogleCloudDatacatalogV1ViewSpec(typing_extensions.TypedDict, total=False):
    viewQuery: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

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
