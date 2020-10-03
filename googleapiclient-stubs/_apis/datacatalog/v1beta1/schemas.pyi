import typing

import typing_extensions

class GoogleCloudDatacatalogV1beta1ListTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1beta1Taxonomy]
    nextPageToken: str

class GoogleCloudDatacatalogV1beta1SerializedPolicyTag(
    typing.Dict[str, typing.Any]
): ...

class GoogleCloudDatacatalogV1beta1SystemTimestamps(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    updateTime: str
    createTime: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int

class GoogleCloudDatacatalogV1beta1ListEntryGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    entryGroups: typing.List[GoogleCloudDatacatalogV1beta1EntryGroup]

class GoogleCloudDatacatalogV1beta1ListTagsResponse(
    typing_extensions.TypedDict, total=False
):
    tags: typing.List[GoogleCloudDatacatalogV1beta1Tag]
    nextPageToken: str

class GoogleCloudDatacatalogV1beta1PolicyTag(typing_extensions.TypedDict, total=False):
    displayName: str
    parentPolicyTag: str
    description: str
    childPolicyTags: typing.List[str]
    name: str

class GoogleCloudDatacatalogV1beta1ListEntriesResponse(
    typing_extensions.TypedDict, total=False
):
    entries: typing.List[GoogleCloudDatacatalogV1beta1Entry]
    nextPageToken: str

class GoogleCloudDatacatalogV1beta1SearchCatalogResponse(
    typing_extensions.TypedDict, total=False
):
    unreachable: typing.List[str]
    nextPageToken: str
    results: typing.List[GoogleCloudDatacatalogV1beta1SearchCatalogResult]

class GoogleCloudDatacatalogV1beta1SearchCatalogResult(
    typing_extensions.TypedDict, total=False
):
    linkedResource: str
    searchResultType: typing_extensions.Literal[
        "SEARCH_RESULT_TYPE_UNSPECIFIED", "ENTRY", "TAG_TEMPLATE", "ENTRY_GROUP"
    ]
    searchResultSubtype: str
    relativeResourceName: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudDatacatalogV1beta1ExportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1beta1SerializedTaxonomy]

class GoogleCloudDatacatalogV1beta1ImportTaxonomiesResponse(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1beta1Taxonomy]

class GoogleCloudDatacatalogV1beta1GcsFileSpec(
    typing_extensions.TypedDict, total=False
):
    sizeBytes: str
    gcsTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps
    filePath: str

class GoogleCloudDatacatalogV1beta1Tag(typing_extensions.TypedDict, total=False):
    templateDisplayName: str
    name: str
    column: str
    fields: typing.Dict[str, typing.Any]
    template: str

class Binding(typing_extensions.TypedDict, total=False):
    bindingId: str
    condition: Expr
    role: str
    members: typing.List[str]

class GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldRequest(
    typing_extensions.TypedDict, total=False
):
    newTagTemplateFieldId: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GoogleCloudDatacatalogV1beta1Schema(typing_extensions.TypedDict, total=False):
    columns: typing.List[GoogleCloudDatacatalogV1beta1ColumnSchema]

class GoogleCloudDatacatalogV1beta1ListPolicyTagsResponse(
    typing_extensions.TypedDict, total=False
):
    policyTags: typing.List[GoogleCloudDatacatalogV1beta1PolicyTag]
    nextPageToken: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope(
    typing_extensions.TypedDict, total=False
):
    restrictedLocations: typing.List[str]
    includeOrgIds: typing.List[str]
    includeGcpPublicDatasets: bool
    includeProjectIds: typing.List[str]

class GoogleCloudDatacatalogV1beta1SerializedTaxonomy(typing.Dict[str, typing.Any]): ...

class GoogleCloudDatacatalogV1beta1Taxonomy(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    activatedPolicyTypes: typing.List[str]
    displayName: str

class GoogleCloudDatacatalogV1beta1FieldTypeEnumType(
    typing_extensions.TypedDict, total=False
):
    allowedValues: typing.List[GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValue]

class Empty(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class GoogleCloudDatacatalogV1beta1RenameTagTemplateFieldEnumValueRequest(
    typing_extensions.TypedDict, total=False
):
    newEnumValueDisplayName: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class GoogleCloudDatacatalogV1beta1BigQueryTableSpec(
    typing_extensions.TypedDict, total=False
):
    tableSpec: GoogleCloudDatacatalogV1beta1TableSpec
    tableSourceType: typing_extensions.Literal[
        "TABLE_SOURCE_TYPE_UNSPECIFIED",
        "BIGQUERY_VIEW",
        "BIGQUERY_TABLE",
        "BIGQUERY_MATERIALIZED_VIEW",
    ]
    viewSpec: GoogleCloudDatacatalogV1beta1ViewSpec

class GoogleCloudDatacatalogV1beta1InlineSource(
    typing_extensions.TypedDict, total=False
):
    taxonomies: typing.List[GoogleCloudDatacatalogV1beta1SerializedTaxonomy]

class GoogleCloudDatacatalogV1beta1TagFieldEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

class GoogleCloudDatacatalogV1beta1TableSpec(typing_extensions.TypedDict, total=False):
    groupedEntry: str

class GoogleCloudDatacatalogV1beta1EntryGroup(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    dataCatalogTimestamps: GoogleCloudDatacatalogV1beta1SystemTimestamps
    name: str

class GoogleCloudDatacatalogV1beta1TagTemplate(
    typing_extensions.TypedDict, total=False
):
    fields: typing.Dict[str, typing.Any]
    name: str
    displayName: str

class GoogleCloudDatacatalogV1beta1Entry(typing.Dict[str, typing.Any]): ...

class GoogleCloudDatacatalogV1beta1FieldTypeEnumTypeEnumValue(
    typing_extensions.TypedDict, total=False
):
    displayName: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str

class GoogleCloudDatacatalogV1beta1SearchCatalogRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    orderBy: str
    query: str
    scope: GoogleCloudDatacatalogV1beta1SearchCatalogRequestScope
    pageToken: str

class GoogleCloudDatacatalogV1beta1ImportTaxonomiesRequest(
    typing_extensions.TypedDict, total=False
):
    inlineSource: GoogleCloudDatacatalogV1beta1InlineSource

class GoogleCloudDatacatalogV1beta1ColumnSchema(typing.Dict[str, typing.Any]): ...

class GoogleCloudDatacatalogV1beta1TagTemplateField(
    typing_extensions.TypedDict, total=False
):
    name: str
    isRequired: bool
    type: GoogleCloudDatacatalogV1beta1FieldType
    order: int
    displayName: str

class GoogleCloudDatacatalogV1beta1TagField(typing_extensions.TypedDict, total=False):
    doubleValue: float
    displayName: str
    timestampValue: str
    order: int
    boolValue: bool
    enumValue: GoogleCloudDatacatalogV1beta1TagFieldEnumValue
    stringValue: str

class GoogleCloudDatacatalogV1beta1ViewSpec(typing_extensions.TypedDict, total=False):
    viewQuery: str

class GoogleCloudDatacatalogV1beta1GcsFilesetSpec(
    typing_extensions.TypedDict, total=False
):
    sampleGcsFileSpecs: typing.List[GoogleCloudDatacatalogV1beta1GcsFileSpec]
    filePatterns: typing.List[str]

class GoogleCloudDatacatalogV1beta1FieldType(typing_extensions.TypedDict, total=False):
    enumType: GoogleCloudDatacatalogV1beta1FieldTypeEnumType
    primitiveType: typing_extensions.Literal[
        "PRIMITIVE_TYPE_UNSPECIFIED", "DOUBLE", "STRING", "BOOL", "TIMESTAMP"
    ]

class GoogleCloudDatacatalogV1beta1BigQueryDateShardedSpec(
    typing_extensions.TypedDict, total=False
):
    dataset: str
    shardCount: str
    tablePrefix: str
