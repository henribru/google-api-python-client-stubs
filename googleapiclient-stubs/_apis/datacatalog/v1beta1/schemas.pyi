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
class GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    shardCount: str
    tablePrefix: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1BigQueryTableSpec(
    typing_extensions.TypedDict, total=False
):
    tableSourceType: typing_extensions.Literal[
        "TABLE_SOURCE_TYPE_UNSPECIFIED",
        "BIGQUERY_VIEW",
        "BIGQUERY_TABLE",
        "BIGQUERY_MATERIALIZED_VIEW",
    ]
    tableSpec: GoogleCloudDatacatalogV1beta1TableSpec
    viewSpec: GoogleCloudDatacatalogV1beta1ViewSpec

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ColumnSchema(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1Entry(typing_extensions.TypedDict, total=False):
    bigqueryDateShardedSpec: GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec
    bigqueryTableSpec: GoogleCloudDatacatalogV1beta1BigQueryTableSpec
    description: str
    displayName: str
    gcsFilesetSpec: GoogleCloudDatacatalogV1beta1GcsFilesetSpec
    integratedSystem: typing_extensions.Literal[
        "INTEGRATED_SYSTEM_UNSPECIFIED", "BIGQUERY", "CLOUD_PUBSUB"
    ]
    linkedResource: str
    name: str
    schema: GoogleCloudDatacatalogV1beta1Schema
    sourceSystemTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps
    type: typing_extensions.Literal[
        "ENTRY_TYPE_UNSPECIFIED", "TABLE", "MODEL", "DATA_STREAM", "FILESET"
    ]
    usageSignal: GoogleCloudDatacatalogV1beta1UsageSignal
    userSpecifiedSystem: str
    userSpecifiedType: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1EntryGroup(typing_extensions.TypedDict, total=False):
    dataCatalogTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps
    description: str
    displayName: str
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: _list[GoogleCloudDatacatalogV1beta1SerializedTaxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1FieldType(typing_extensions.TypedDict, total=False):
    enumType: GoogleCloudDatacatalogV1beta1FieldTypeEnumType
    primitiveType: typing_extensions.Literal[
        "PRIMITIVE_TYPE_UNSPECIFIED", "DOUBLE", "STRING", "BOOL", "TIMESTAMP"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1FieldTypeEnumType(
    typing_extensions.TypedDict, total=False
):
    allowedValues: _list[GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValue]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1GcsFileSpec(
    typing_extensions.TypedDict, total=False
):
    filePath: str
    gcsTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps
    sizeBytes: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1GcsFilesetSpec(
    typing_extensions.TypedDict, total=False
):
    filePatterns: _list[str]
    sampleGcsFileSpecs: _list[GoogleCloudDatacatalogV1beta1GcsFileSpec]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest(
    typing_extensions.TypedDict, total=False
):
    inlineSource: GoogleCloudDatacatalogV1beta1InlineSource

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: _list[GoogleCloudDatacatalogV1beta1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1InlineSource(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    entries: _list[GoogleCloudDatacatalogV1beta1Entry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    entryGroups: _list[GoogleCloudDatacatalogV1beta1EntryGroup]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policyTags: _list[GoogleCloudDatacatalogV1beta1PolicyTag]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListTagsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    tags: _list[GoogleCloudDatacatalogV1beta1Tag]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    taxonomies: _list[GoogleCloudDatacatalogV1beta1Taxonomy]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1PolicyTag(typing_extensions.TypedDict, total=False):
    childPolicyTags: _list[str]
    description: str
    displayName: str
    name: str
    parentPolicyTag: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest(
    typing_extensions.TypedDict, total=False
):
    newEnumValueDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldRequest(
    typing_extensions.TypedDict, total=False
):
    newTagTemplateFieldId: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1Schema(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogRequest(
    typing_extensions.TypedDict, total=False
):
    orderBy: str
    pageSize: int
    pageToken: str
    query: str
    scope: GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope(
    typing_extensions.TypedDict, total=False
):
    includeGcpPublicDatasets: bool
    includeOrgIds: _list[str]
    includeProjectIds: _list[str]
    restrictedLocations: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    results: _list[GoogleCloudDatacatalogV1beta1SearchCatalogResult]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SearchCatalogResult(
    typing_extensions.TypedDict, total=False
):
    linkedResource: str
    modifyTime: str
    relativeResourceName: str
    searchResultSubtype: str
    searchResultType: typing_extensions.Literal[
        "SEARCH_RESULT_TYPE_UNSPECIFIED", "ENTRY", "TAG_TEMPLATE", "ENTRY_GROUP"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SerializedPolicyTag(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SerializedTaxonomy(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1SystemTimestamps(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    expireTime: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TableSpec(typing_extensions.TypedDict, total=False):
    groupedEntry: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1Tag(typing_extensions.TypedDict, total=False):
    column: str
    fields: dict[str, typing.Any]
    name: str
    template: str
    templateDisplayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagField(typing_extensions.TypedDict, total=False):
    boolValue: bool
    displayName: str
    doubleValue: float
    enumValue: GoogleCloudDatacatalogV1beta1TagFieldEnumValue
    order: int
    stringValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagFieldEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagTemplate(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    fields: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1TagTemplateField(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    isRequired: bool
    name: str
    order: int
    type: GoogleCloudDatacatalogV1beta1FieldType

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1Taxonomy(typing_extensions.TypedDict, total=False):
    activatedPolicyTypes: _list[str]
    description: str
    displayName: str
    name: str
    policyTagCount: int
    taxonomyTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1UsageSignal(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    usageWithinTimeRange: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1UsageStats(typing_extensions.TypedDict, total=False):
    totalCancellations: float
    totalCompletions: float
    totalExecutionTimeForCompletionsMillis: float
    totalFailures: float

@typing.type_check_only
class GoogleCloudDatacatalogV1beta1ViewSpec(typing_extensions.TypedDict, total=False):
    viewQuery: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
