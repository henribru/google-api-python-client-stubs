import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1Action(typing.TypedDict, total=False):
    asset: str
    category: typing.Literal[
        "CATEGORY_UNSPECIFIED",
        "RESOURCE_MANAGEMENT",
        "SECURITY_POLICY",
        "DATA_DISCOVERY",
    ]
    dataLocations: _list[str]
    detectTime: str
    failedSecurityPolicyApply: GoogleCloudDataplexV1ActionFailedSecurityPolicyApply
    incompatibleDataSchema: GoogleCloudDataplexV1ActionIncompatibleDataSchema
    invalidDataFormat: GoogleCloudDataplexV1ActionInvalidDataFormat
    invalidDataOrganization: GoogleCloudDataplexV1ActionInvalidDataOrganization
    invalidDataPartition: GoogleCloudDataplexV1ActionInvalidDataPartition
    issue: str
    lake: str
    missingData: GoogleCloudDataplexV1ActionMissingData
    missingResource: GoogleCloudDataplexV1ActionMissingResource
    name: str
    unauthorizedResource: GoogleCloudDataplexV1ActionUnauthorizedResource
    zone: str

@typing.type_check_only
class GoogleCloudDataplexV1ActionFailedSecurityPolicyApply(
    typing.TypedDict, total=False
):
    asset: str

@typing.type_check_only
class GoogleCloudDataplexV1ActionIncompatibleDataSchema(typing.TypedDict, total=False):
    existingSchema: str
    newSchema: str
    sampledDataLocations: _list[str]
    schemaChange: typing.Literal[
        "SCHEMA_CHANGE_UNSPECIFIED", "INCOMPATIBLE", "MODIFIED"
    ]
    table: str

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataFormat(typing.TypedDict, total=False):
    expectedFormat: str
    newFormat: str
    sampledDataLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataOrganization(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataPartition(typing.TypedDict, total=False):
    expectedStructure: typing.Literal[
        "PARTITION_STRUCTURE_UNSPECIFIED", "CONSISTENT_KEYS", "HIVE_STYLE_KEYS"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1ActionMissingData(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionMissingResource(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionUnauthorizedResource(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ApproveChangeRequestRequest(typing.TypedDict, total=False):
    comment: str
    etag: str

@typing.type_check_only
class GoogleCloudDataplexV1Aspect(typing.TypedDict, total=False):
    aspectSource: GoogleCloudDataplexV1AspectSource
    aspectType: str
    createTime: str
    data: dict[str, typing.Any]
    path: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AspectSource(typing.TypedDict, total=False):
    createTime: str
    dataVersion: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AspectType(typing.TypedDict, total=False):
    authorization: GoogleCloudDataplexV1AspectTypeAuthorization
    createTime: str
    dataClassification: typing.Literal[
        "DATA_CLASSIFICATION_UNSPECIFIED", "METADATA_AND_DATA"
    ]
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    metadataTemplate: GoogleCloudDataplexV1AspectTypeMetadataTemplate
    name: str
    transferStatus: typing.Literal[
        "TRANSFER_STATUS_UNSPECIFIED",
        "TRANSFER_STATUS_MIGRATED",
        "TRANSFER_STATUS_TRANSFERRED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AspectTypeAuthorization(typing.TypedDict, total=False):
    alternateUsePermission: str

@typing.type_check_only
class GoogleCloudDataplexV1AspectTypeMetadataTemplate(typing.TypedDict, total=False):
    annotations: GoogleCloudDataplexV1AspectTypeMetadataTemplateAnnotations
    arrayItems: GoogleCloudDataplexV1AspectTypeMetadataTemplate
    constraints: GoogleCloudDataplexV1AspectTypeMetadataTemplateConstraints
    enumValues: _list[GoogleCloudDataplexV1AspectTypeMetadataTemplateEnumValue]
    index: int
    mapItems: GoogleCloudDataplexV1AspectTypeMetadataTemplate
    name: str
    recordFields: _list[GoogleCloudDataplexV1AspectTypeMetadataTemplate]
    type: str
    typeId: str
    typeRef: str

@typing.type_check_only
class GoogleCloudDataplexV1AspectTypeMetadataTemplateAnnotations(
    typing.TypedDict, total=False
):
    deprecated: str
    description: str
    displayName: str
    displayOrder: int
    stringType: str
    stringValues: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1AspectTypeMetadataTemplateConstraints(
    typing.TypedDict, total=False
):
    required: bool

@typing.type_check_only
class GoogleCloudDataplexV1AspectTypeMetadataTemplateEnumValue(
    typing.TypedDict, total=False
):
    deprecated: str
    index: int
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1Asset(typing.TypedDict, total=False):
    createTime: str
    description: str
    discoverySpec: GoogleCloudDataplexV1AssetDiscoverySpec
    discoveryStatus: GoogleCloudDataplexV1AssetDiscoveryStatus
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    resourceSpec: GoogleCloudDataplexV1AssetResourceSpec
    resourceStatus: GoogleCloudDataplexV1AssetResourceStatus
    securityStatus: GoogleCloudDataplexV1AssetSecurityStatus
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpec(typing.TypedDict, total=False):
    csvOptions: GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions
    enabled: bool
    excludePatterns: _list[str]
    includePatterns: _list[str]
    jsonOptions: GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions
    schedule: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions(typing.TypedDict, total=False):
    delimiter: str
    disableTypeInference: bool
    encoding: str
    headerRows: int

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions(typing.TypedDict, total=False):
    disableTypeInference: bool
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoveryStatus(typing.TypedDict, total=False):
    lastRunDuration: str
    lastRunTime: str
    message: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SCHEDULED", "IN_PROGRESS", "PAUSED", "DISABLED"
    ]
    stats: GoogleCloudDataplexV1AssetDiscoveryStatusStats
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoveryStatusStats(typing.TypedDict, total=False):
    dataItems: str
    dataSize: str
    filesets: str
    tables: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetResourceSpec(typing.TypedDict, total=False):
    name: str
    readAccessMode: typing.Literal["ACCESS_MODE_UNSPECIFIED", "DIRECT", "MANAGED"]
    type: typing.Literal["TYPE_UNSPECIFIED", "STORAGE_BUCKET", "BIGQUERY_DATASET"]

@typing.type_check_only
class GoogleCloudDataplexV1AssetResourceStatus(typing.TypedDict, total=False):
    managedAccessIdentity: str
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "ERROR"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetSecurityStatus(typing.TypedDict, total=False):
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "READY", "APPLYING", "ERROR"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetStatus(typing.TypedDict, total=False):
    activeAssets: int
    securityPolicyApplyingAssets: int
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1BusinessGlossaryEvent(typing.TypedDict, total=False):
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "GLOSSARY_CREATE",
        "GLOSSARY_UPDATE",
        "GLOSSARY_DELETE",
        "GLOSSARY_CATEGORY_CREATE",
        "GLOSSARY_CATEGORY_UPDATE",
        "GLOSSARY_CATEGORY_DELETE",
        "GLOSSARY_TERM_CREATE",
        "GLOSSARY_TERM_UPDATE",
        "GLOSSARY_TERM_DELETE",
    ]
    message: str
    resource: str

@typing.type_check_only
class GoogleCloudDataplexV1CancelDataScanJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1CancelDataScanJobResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1CancelJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1CancelMetadataJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1ChangeRequest(typing.TypedDict, total=False):
    approver: str
    author: str
    changeType: typing.Literal[
        "CHANGE_TYPE_UNSPECIFIED",
        "CREATE_ENTRY",
        "UPDATE_ENTRY",
        "DELETE_ENTRY",
        "CREATE_ENTRY_LINK",
        "DELETE_ENTRY_LINK",
        "CREATE_GLOSSARY",
        "UPDATE_GLOSSARY",
        "DELETE_GLOSSARY",
        "CREATE_GLOSSARY_CATEGORY",
        "UPDATE_GLOSSARY_CATEGORY",
        "DELETE_GLOSSARY_CATEGORY",
        "CREATE_GLOSSARY_TERM",
        "UPDATE_GLOSSARY_TERM",
        "DELETE_GLOSSARY_TERM",
        "REQUEST_DATA_PRODUCT_ACCESS",
    ]
    createEntry: GoogleCloudDataplexV1CreateEntryRequest
    createEntryLink: GoogleCloudDataplexV1CreateEntryLinkRequest
    createGlossary: GoogleCloudDataplexV1CreateGlossaryRequest
    createGlossaryCategory: GoogleCloudDataplexV1CreateGlossaryCategoryRequest
    createGlossaryTerm: GoogleCloudDataplexV1CreateGlossaryTermRequest
    createTime: str
    dataProductAccessRequest: GoogleCloudDataplexV1DataProductAccessRequest
    deleteEntry: GoogleCloudDataplexV1DeleteEntryRequest
    deleteEntryLink: GoogleCloudDataplexV1DeleteEntryLinkRequest
    deleteGlossary: GoogleCloudDataplexV1DeleteGlossaryRequest
    deleteGlossaryCategory: GoogleCloudDataplexV1DeleteGlossaryCategoryRequest
    deleteGlossaryTerm: GoogleCloudDataplexV1DeleteGlossaryTermRequest
    etag: str
    justification: str
    labels: dict[str, typing.Any]
    name: str
    rejectionComment: str
    resource: str
    reviewerComment: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "NEW", "APPROVED", "REJECTED", "EXPIRED", "REVOKED"
    ]
    uid: str
    updateEntry: GoogleCloudDataplexV1UpdateEntryRequest
    updateGlossary: GoogleCloudDataplexV1UpdateGlossaryRequest
    updateGlossaryCategory: GoogleCloudDataplexV1UpdateGlossaryCategoryRequest
    updateGlossaryTerm: GoogleCloudDataplexV1UpdateGlossaryTermRequest
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ContactIdentity(typing.TypedDict, total=False):
    contactId: str
    contactName: str
    contactRole: str

@typing.type_check_only
class GoogleCloudDataplexV1Contacts(typing.TypedDict, total=False):
    identities: _list[GoogleCloudDataplexV1ContactIdentity]

@typing.type_check_only
class GoogleCloudDataplexV1CreateEntryLinkRequest(typing.TypedDict, total=False):
    entryLink: GoogleCloudDataplexV1EntryLink
    entryLinkId: str
    parent: str

@typing.type_check_only
class GoogleCloudDataplexV1CreateEntryRequest(typing.TypedDict, total=False):
    entry: GoogleCloudDataplexV1Entry
    entryId: str
    parent: str

@typing.type_check_only
class GoogleCloudDataplexV1CreateGlossaryCategoryRequest(typing.TypedDict, total=False):
    category: GoogleCloudDataplexV1GlossaryCategory
    categoryId: str
    parent: str

@typing.type_check_only
class GoogleCloudDataplexV1CreateGlossaryRequest(typing.TypedDict, total=False):
    glossary: GoogleCloudDataplexV1Glossary
    glossaryId: str
    parent: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDataplexV1CreateGlossaryTermRequest(typing.TypedDict, total=False):
    parent: str
    term: GoogleCloudDataplexV1GlossaryTerm
    termId: str

@typing.type_check_only
class GoogleCloudDataplexV1DataAccessSpec(typing.TypedDict, total=False):
    readers: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataAsset(typing.TypedDict, total=False):
    accessGroupConfigs: dict[str, typing.Any]
    createTime: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    resource: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataAssetAccessGroupConfig(typing.TypedDict, total=False):
    iamRoles: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataAttribute(typing.TypedDict, total=False):
    attributeCount: int
    createTime: str
    dataAccessSpec: GoogleCloudDataplexV1DataAccessSpec
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    parentId: str
    resourceAccessSpec: GoogleCloudDataplexV1ResourceAccessSpec
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataAttributeBinding(typing.TypedDict, total=False):
    attributes: _list[str]
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    paths: _list[GoogleCloudDataplexV1DataAttributeBindingPath]
    resource: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataAttributeBindingPath(typing.TypedDict, total=False):
    attributes: _list[str]
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoveryResult(typing.TypedDict, total=False):
    bigqueryPublishing: GoogleCloudDataplexV1DataDiscoveryResultBigQueryPublishing
    scanStatistics: GoogleCloudDataplexV1DataDiscoveryResultScanStatistics

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoveryResultBigQueryPublishing(
    typing.TypedDict, total=False
):
    dataset: str
    location: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoveryResultScanStatistics(
    typing.TypedDict, total=False
):
    dataProcessedBytes: str
    filesExcluded: int
    filesetsCreated: int
    filesetsDeleted: int
    filesetsUpdated: int
    scannedFileCount: int
    tablesCreated: int
    tablesDeleted: int
    tablesUpdated: int

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpec(typing.TypedDict, total=False):
    bigqueryPublishingConfig: (
        GoogleCloudDataplexV1DataDiscoverySpecBigQueryPublishingConfig
    )
    storageConfig: GoogleCloudDataplexV1DataDiscoverySpecStorageConfig

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpecBigQueryPublishingConfig(
    typing.TypedDict, total=False
):
    connection: str
    location: str
    project: str
    tableType: typing.Literal["TABLE_TYPE_UNSPECIFIED", "EXTERNAL", "BIGLAKE"]

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpecStorageConfig(
    typing.TypedDict, total=False
):
    csvOptions: GoogleCloudDataplexV1DataDiscoverySpecStorageConfigCsvOptions
    excludePatterns: _list[str]
    includePatterns: _list[str]
    jsonOptions: GoogleCloudDataplexV1DataDiscoverySpecStorageConfigJsonOptions
    unstructuredDataOptions: (
        GoogleCloudDataplexV1DataDiscoverySpecStorageConfigUnstructuredDataOptions
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpecStorageConfigCsvOptions(
    typing.TypedDict, total=False
):
    delimiter: str
    encoding: str
    headerRows: int
    quote: str
    typeInferenceDisabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpecStorageConfigJsonOptions(
    typing.TypedDict, total=False
):
    encoding: str
    typeInferenceDisabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataDiscoverySpecStorageConfigUnstructuredDataOptions(
    typing.TypedDict, total=False
):
    globalEndpointEnabled: bool
    semanticInferenceEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResult(typing.TypedDict, total=False):
    datasetResult: GoogleCloudDataplexV1DataDocumentationResultDatasetResult
    tableResult: GoogleCloudDataplexV1DataDocumentationResultTableResult

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultDatasetResult(
    typing.TypedDict, total=False
):
    overview: str
    queries: _list[GoogleCloudDataplexV1DataDocumentationResultQuery]
    schemaRelationships: _list[
        GoogleCloudDataplexV1DataDocumentationResultSchemaRelationship
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultField(typing.TypedDict, total=False):
    description: str
    fields: _list[GoogleCloudDataplexV1DataDocumentationResultField]
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultQuery(typing.TypedDict, total=False):
    description: str
    sql: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultSchema(typing.TypedDict, total=False):
    fields: _list[GoogleCloudDataplexV1DataDocumentationResultField]

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultSchemaRelationship(
    typing.TypedDict, total=False
):
    leftSchemaPaths: (
        GoogleCloudDataplexV1DataDocumentationResultSchemaRelationshipSchemaPaths
    )
    rightSchemaPaths: (
        GoogleCloudDataplexV1DataDocumentationResultSchemaRelationshipSchemaPaths
    )
    sources: _list[
        typing.Literal[
            "SOURCE_UNSPECIFIED", "AGENT", "QUERY_HISTORY", "TABLE_CONSTRAINTS"
        ]
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "SCHEMA_JOIN"]

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultSchemaRelationshipSchemaPaths(
    typing.TypedDict, total=False
):
    paths: _list[str]
    tableFqn: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationResultTableResult(
    typing.TypedDict, total=False
):
    name: str
    overview: str
    queries: _list[GoogleCloudDataplexV1DataDocumentationResultQuery]
    schema: GoogleCloudDataplexV1DataDocumentationResultSchema

@typing.type_check_only
class GoogleCloudDataplexV1DataDocumentationSpec(typing.TypedDict, total=False):
    catalogPublishingEnabled: bool
    generationScopes: _list[
        typing.Literal[
            "GENERATION_SCOPE_UNSPECIFIED",
            "ALL",
            "TABLE_AND_COLUMN_DESCRIPTIONS",
            "SQL_QUERIES",
            "BUSINESS_GLOSSARY_TERM_ASSOCIATIONS",
        ]
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataDomain(typing.TypedDict, total=False):
    contacts: GoogleCloudDataplexV1Contacts
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    parentDataDomain: str
    policyMember: GoogleIamV1ResourcePolicyMember
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataDomainBinding(typing.TypedDict, total=False):
    createTime: str
    name: str
    resource: str
    uid: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProduct(typing.TypedDict, total=False):
    accessApprovalConfig: GoogleCloudDataplexV1DataProductAccessApprovalConfig
    accessGroups: dict[str, typing.Any]
    assetCount: int
    createTime: str
    description: str
    displayName: str
    etag: str
    icon: str
    labels: dict[str, typing.Any]
    name: str
    ownerEmails: _list[str]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProductAccessApprovalConfig(
    typing.TypedDict, total=False
):
    approverEmails: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataProductAccessGroup(typing.TypedDict, total=False):
    description: str
    displayName: str
    id: str
    principal: GoogleCloudDataplexV1DataProductPrincipal

@typing.type_check_only
class GoogleCloudDataplexV1DataProductAccessRequest(typing.TypedDict, total=False):
    accessGroupDisplayName: str
    accessGroupId: str
    parent: str
    requestedPrincipal: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProductPrincipal(typing.TypedDict, total=False):
    googleGroup: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResult(typing.TypedDict, total=False):
    catalogPublishingStatus: GoogleCloudDataplexV1DataScanCatalogPublishingStatus
    postScanActionsResult: GoogleCloudDataplexV1DataProfileResultPostScanActionsResult
    profile: GoogleCloudDataplexV1DataProfileResultProfile
    rowCount: str
    scannedData: GoogleCloudDataplexV1ScannedData

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultPostScanActionsResult(
    typing.TypedDict, total=False
):
    bigqueryExportResult: (
        GoogleCloudDataplexV1DataProfileResultPostScanActionsResultBigQueryExportResult
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultPostScanActionsResultBigQueryExportResult(
    typing.TypedDict, total=False
):
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "SKIPPED"]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfile(typing.TypedDict, total=False):
    fields: _list[GoogleCloudDataplexV1DataProfileResultProfileField]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileField(typing.TypedDict, total=False):
    mode: str
    name: str
    profile: GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo(
    typing.TypedDict, total=False
):
    distinctRatio: float
    doubleProfile: (
        GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo
    )
    integerProfile: (
        GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo
    )
    nullRatio: float
    stringProfile: (
        GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo
    )
    topNValues: _list[
        GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo(
    typing.TypedDict, total=False
):
    average: float
    max: float
    min: float
    quartiles: _list[float]
    standardDeviation: float

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo(
    typing.TypedDict, total=False
):
    average: float
    max: str
    min: str
    quartiles: _list[str]
    standardDeviation: float

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo(
    typing.TypedDict, total=False
):
    averageLength: float
    maxLength: str
    minLength: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue(
    typing.TypedDict, total=False
):
    count: str
    ratio: float
    value: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileSpec(typing.TypedDict, total=False):
    catalogPublishingEnabled: bool
    excludeFields: GoogleCloudDataplexV1DataProfileSpecSelectedFields
    includeFields: GoogleCloudDataplexV1DataProfileSpecSelectedFields
    mode: typing.Literal["MODE_UNSPECIFIED", "STANDARD", "LIGHTWEIGHT"]
    postScanActions: GoogleCloudDataplexV1DataProfileSpecPostScanActions
    rowFilter: str
    samplingPercent: float

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileSpecPostScanActions(
    typing.TypedDict, total=False
):
    bigqueryExport: GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExport

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileSpecPostScanActionsBigQueryExport(
    typing.TypedDict, total=False
):
    resultsTable: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileSpecSelectedFields(typing.TypedDict, total=False):
    fieldNames: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityColumnResult(typing.TypedDict, total=False):
    column: str
    dimensions: _list[GoogleCloudDataplexV1DataQualityDimensionResult]
    passed: bool
    score: float

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityDimension(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityDimensionResult(typing.TypedDict, total=False):
    dimension: GoogleCloudDataplexV1DataQualityDimension
    passed: bool
    score: float

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityResult(typing.TypedDict, total=False):
    anomalyDetectionGeneratedAssets: (
        GoogleCloudDataplexV1DataQualityResultAnomalyDetectionGeneratedAssets
    )
    catalogPublishingStatus: GoogleCloudDataplexV1DataScanCatalogPublishingStatus
    columns: _list[GoogleCloudDataplexV1DataQualityColumnResult]
    dimensions: _list[GoogleCloudDataplexV1DataQualityDimensionResult]
    passed: bool
    postScanActionsResult: GoogleCloudDataplexV1DataQualityResultPostScanActionsResult
    rowCount: str
    rules: _list[GoogleCloudDataplexV1DataQualityRuleResult]
    scannedData: GoogleCloudDataplexV1ScannedData
    score: float

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityResultAnomalyDetectionGeneratedAssets(
    typing.TypedDict, total=False
):
    dataIntermediateTable: str
    freshnessIntermediateTable: str
    resultTable: str
    volumeIntermediateTable: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityResultPostScanActionsResult(
    typing.TypedDict, total=False
):
    bigqueryExportResult: (
        GoogleCloudDataplexV1DataQualityResultPostScanActionsResultBigQueryExportResult
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityResultPostScanActionsResultBigQueryExportResult(
    typing.TypedDict, total=False
):
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "SKIPPED"]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRule(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    column: str
    debugQueries: _list[GoogleCloudDataplexV1DataQualityRuleDebugQuery]
    description: str
    dimension: str
    ignoreNull: bool
    name: str
    nonNullExpectation: GoogleCloudDataplexV1DataQualityRuleNonNullExpectation
    rangeExpectation: GoogleCloudDataplexV1DataQualityRuleRangeExpectation
    regexExpectation: GoogleCloudDataplexV1DataQualityRuleRegexExpectation
    rowConditionExpectation: GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation
    ruleSource: GoogleCloudDataplexV1DataQualityRuleRuleSource
    setExpectation: GoogleCloudDataplexV1DataQualityRuleSetExpectation
    sqlAssertion: GoogleCloudDataplexV1DataQualityRuleSqlAssertion
    statisticRangeExpectation: (
        GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation
    )
    suspended: bool
    tableConditionExpectation: (
        GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation
    )
    templateReference: GoogleCloudDataplexV1DataQualityRuleTemplateReference
    threshold: float
    uniquenessExpectation: GoogleCloudDataplexV1DataQualityRuleUniquenessExpectation

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleDebugQuery(typing.TypedDict, total=False):
    description: str
    sqlStatement: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleNonNullExpectation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRangeExpectation(
    typing.TypedDict, total=False
):
    maxValue: str
    minValue: str
    strictMaxEnabled: bool
    strictMinEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRegexExpectation(
    typing.TypedDict, total=False
):
    regex: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleResult(typing.TypedDict, total=False):
    assertionRowCount: str
    debugQueriesResultSets: _list[
        GoogleCloudDataplexV1DataQualityRuleResultDebugQueryResultSet
    ]
    evaluatedCount: str
    failingRowsQuery: str
    nullCount: str
    passRatio: float
    passed: bool
    passedCount: str
    rule: GoogleCloudDataplexV1DataQualityRule

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleResultDebugQueryResult(
    typing.TypedDict, total=False
):
    name: str
    type: str
    value: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleResultDebugQueryResultSet(
    typing.TypedDict, total=False
):
    results: _list[GoogleCloudDataplexV1DataQualityRuleResultDebugQueryResult]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation(
    typing.TypedDict, total=False
):
    sqlExpression: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRuleSource(typing.TypedDict, total=False):
    rulePathElements: _list[
        GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElement
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElement(
    typing.TypedDict, total=False
):
    entryLinkSource: (
        GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElementEntryLinkSource
    )
    entrySource: (
        GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElementEntrySource
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElementEntryLinkSource(
    typing.TypedDict, total=False
):
    entryLink: str
    entryLinkType: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRuleSourceRulePathElementEntrySource(
    typing.TypedDict, total=False
):
    displayName: str
    entry: str
    entryType: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleSetExpectation(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleSqlAssertion(typing.TypedDict, total=False):
    sqlStatement: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation(
    typing.TypedDict, total=False
):
    maxValue: str
    minValue: str
    statistic: typing.Literal["STATISTIC_UNDEFINED", "MEAN", "MIN", "MAX"]
    strictMaxEnabled: bool
    strictMinEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation(
    typing.TypedDict, total=False
):
    sqlExpression: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTemplate(typing.TypedDict, total=False):
    capabilities: _list[str]
    dimension: str
    inputParameters: dict[str, typing.Any]
    name: str
    sqlCollection: _list[GoogleCloudDataplexV1DataQualityRuleTemplateSql]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTemplateParameterDescription(
    typing.TypedDict, total=False
):
    defaultValue: str
    description: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTemplateReference(
    typing.TypedDict, total=False
):
    name: str
    resolvedSql: str
    ruleTemplate: GoogleCloudDataplexV1DataQualityRuleTemplate
    values: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTemplateReferenceParameterValue(
    typing.TypedDict, total=False
):
    value: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTemplateSql(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleUniquenessExpectation(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityScanRuleResult(typing.TypedDict, total=False):
    assertionRowCount: str
    column: str
    dataSource: str
    evaluatedRowCount: str
    evalutionType: typing.Literal["EVALUATION_TYPE_UNSPECIFIED", "PER_ROW", "AGGREGATE"]
    jobId: str
    nullRowCount: str
    passedRowCount: str
    result: typing.Literal["RESULT_UNSPECIFIED", "PASSED", "FAILED"]
    ruleDimension: str
    ruleName: str
    ruleType: typing.Literal[
        "RULE_TYPE_UNSPECIFIED",
        "NON_NULL_EXPECTATION",
        "RANGE_EXPECTATION",
        "REGEX_EXPECTATION",
        "ROW_CONDITION_EXPECTATION",
        "SET_EXPECTATION",
        "STATISTIC_RANGE_EXPECTATION",
        "TABLE_CONDITION_EXPECTATION",
        "UNIQUENESS_EXPECTATION",
        "SQL_ASSERTION",
        "TEMPLATE_REFERENCE",
    ]
    thresholdPercent: float

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpec(typing.TypedDict, total=False):
    catalogPublishingEnabled: bool
    enableCatalogBasedRules: bool
    filter: str
    postScanActions: GoogleCloudDataplexV1DataQualitySpecPostScanActions
    rowFilter: str
    rules: _list[GoogleCloudDataplexV1DataQualityRule]
    samplingPercent: float

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActions(
    typing.TypedDict, total=False
):
    bigqueryExport: GoogleCloudDataplexV1DataQualitySpecPostScanActionsBigQueryExport
    notificationReport: (
        GoogleCloudDataplexV1DataQualitySpecPostScanActionsNotificationReport
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsBigQueryExport(
    typing.TypedDict, total=False
):
    resultsTable: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsJobEndTrigger(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsJobFailureTrigger(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsNotificationReport(
    typing.TypedDict, total=False
):
    jobEndTrigger: GoogleCloudDataplexV1DataQualitySpecPostScanActionsJobEndTrigger
    jobFailureTrigger: (
        GoogleCloudDataplexV1DataQualitySpecPostScanActionsJobFailureTrigger
    )
    recipients: GoogleCloudDataplexV1DataQualitySpecPostScanActionsRecipients
    scoreThresholdTrigger: (
        GoogleCloudDataplexV1DataQualitySpecPostScanActionsScoreThresholdTrigger
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsRecipients(
    typing.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpecPostScanActionsScoreThresholdTrigger(
    typing.TypedDict, total=False
):
    scoreThreshold: float

@typing.type_check_only
class GoogleCloudDataplexV1DataScan(typing.TypedDict, total=False):
    createTime: str
    data: GoogleCloudDataplexV1DataSource
    dataDiscoveryResult: GoogleCloudDataplexV1DataDiscoveryResult
    dataDiscoverySpec: GoogleCloudDataplexV1DataDiscoverySpec
    dataDocumentationResult: GoogleCloudDataplexV1DataDocumentationResult
    dataDocumentationSpec: GoogleCloudDataplexV1DataDocumentationSpec
    dataProfileResult: GoogleCloudDataplexV1DataProfileResult
    dataProfileSpec: GoogleCloudDataplexV1DataProfileSpec
    dataQualityResult: GoogleCloudDataplexV1DataQualityResult
    dataQualitySpec: GoogleCloudDataplexV1DataQualitySpec
    description: str
    displayName: str
    executionIdentity: GoogleCloudDataplexV1ExecutionIdentity
    executionSpec: GoogleCloudDataplexV1DataScanExecutionSpec
    executionStatus: GoogleCloudDataplexV1DataScanExecutionStatus
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    type: typing.Literal[
        "DATA_SCAN_TYPE_UNSPECIFIED",
        "DATA_QUALITY",
        "DATA_PROFILE",
        "DATA_DISCOVERY",
        "DATA_DOCUMENTATION",
        "UNSTRUCTURED_DATA_PROFILE",
    ]
    uid: str
    unstructuredDataProfileResult: GoogleCloudDataplexV1UnstructuredDataProfileResult
    unstructuredDataProfileSpec: GoogleCloudDataplexV1UnstructuredDataProfileSpec
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanCatalogPublishingStatus(
    typing.TypedDict, total=False
):
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "SKIPPED"]

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEvent(typing.TypedDict, total=False):
    catalogPublishingStatus: GoogleCloudDataplexV1DataScanCatalogPublishingStatus
    createTime: str
    dataProfile: GoogleCloudDataplexV1DataScanEventDataProfileResult
    dataProfileConfigs: GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs
    dataQuality: GoogleCloudDataplexV1DataScanEventDataQualityResult
    dataQualityConfigs: GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs
    dataSource: str
    endTime: str
    jobId: str
    message: str
    postScanActionsResult: GoogleCloudDataplexV1DataScanEventPostScanActionsResult
    scope: typing.Literal["SCOPE_UNSPECIFIED", "FULL", "INCREMENTAL"]
    specVersion: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED", "CANCELLED", "CREATED"
    ]
    trigger: typing.Literal["TRIGGER_UNSPECIFIED", "ON_DEMAND", "SCHEDULE", "ONE_TIME"]
    type: typing.Literal[
        "SCAN_TYPE_UNSPECIFIED", "DATA_PROFILE", "DATA_QUALITY", "DATA_DISCOVERY"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataProfileAppliedConfigs(
    typing.TypedDict, total=False
):
    columnFilterApplied: bool
    rowFilterApplied: bool
    samplingPercent: float

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataProfileResult(
    typing.TypedDict, total=False
):
    rowCount: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataQualityAppliedConfigs(
    typing.TypedDict, total=False
):
    rowFilterApplied: bool
    samplingPercent: float

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataQualityResult(
    typing.TypedDict, total=False
):
    columnScore: dict[str, typing.Any]
    dimensionPassed: dict[str, typing.Any]
    dimensionScore: dict[str, typing.Any]
    passed: bool
    rowCount: str
    score: float

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventPostScanActionsResult(
    typing.TypedDict, total=False
):
    bigqueryExportResult: (
        GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResult
    )

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventPostScanActionsResultBigQueryExportResult(
    typing.TypedDict, total=False
):
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "SKIPPED"]

@typing.type_check_only
class GoogleCloudDataplexV1DataScanExecutionSpec(typing.TypedDict, total=False):
    field: str
    trigger: GoogleCloudDataplexV1Trigger

@typing.type_check_only
class GoogleCloudDataplexV1DataScanExecutionStatus(typing.TypedDict, total=False):
    latestJobCreateTime: str
    latestJobEndTime: str
    latestJobStartTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanJob(typing.TypedDict, total=False):
    createTime: str
    dataDiscoveryResult: GoogleCloudDataplexV1DataDiscoveryResult
    dataDiscoverySpec: GoogleCloudDataplexV1DataDiscoverySpec
    dataDocumentationResult: GoogleCloudDataplexV1DataDocumentationResult
    dataDocumentationSpec: GoogleCloudDataplexV1DataDocumentationSpec
    dataProfileResult: GoogleCloudDataplexV1DataProfileResult
    dataProfileSpec: GoogleCloudDataplexV1DataProfileSpec
    dataQualityResult: GoogleCloudDataplexV1DataQualityResult
    dataQualitySpec: GoogleCloudDataplexV1DataQualitySpec
    endTime: str
    message: str
    name: str
    partialFailureMessage: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "CANCELING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
        "PENDING",
        "SUCCEEDED_WITH_ERRORS",
    ]
    type: typing.Literal[
        "DATA_SCAN_TYPE_UNSPECIFIED",
        "DATA_QUALITY",
        "DATA_PROFILE",
        "DATA_DISCOVERY",
        "DATA_DOCUMENTATION",
        "UNSTRUCTURED_DATA_PROFILE",
    ]
    uid: str
    unstructuredDataProfileResult: GoogleCloudDataplexV1UnstructuredDataProfileResult
    unstructuredDataProfileSpec: GoogleCloudDataplexV1UnstructuredDataProfileSpec

@typing.type_check_only
class GoogleCloudDataplexV1DataSource(typing.TypedDict, total=False):
    entity: str
    resource: str

@typing.type_check_only
class GoogleCloudDataplexV1DataTaxonomy(typing.TypedDict, total=False):
    attributeCount: int
    classCount: int
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DeleteEntryLinkRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DeleteEntryRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DeleteGlossaryCategoryRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DeleteGlossaryRequest(typing.TypedDict, total=False):
    etag: str
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DeleteGlossaryTermRequest(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEvent(typing.TypedDict, total=False):
    action: GoogleCloudDataplexV1DiscoveryEventActionDetails
    assetId: str
    config: GoogleCloudDataplexV1DiscoveryEventConfigDetails
    dataLocation: str
    datascanId: str
    entity: GoogleCloudDataplexV1DiscoveryEventEntityDetails
    lakeId: str
    message: str
    partition: GoogleCloudDataplexV1DiscoveryEventPartitionDetails
    table: GoogleCloudDataplexV1DiscoveryEventTableDetails
    type: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "CONFIG",
        "ENTITY_CREATED",
        "ENTITY_UPDATED",
        "ENTITY_DELETED",
        "PARTITION_CREATED",
        "PARTITION_UPDATED",
        "PARTITION_DELETED",
        "TABLE_PUBLISHED",
        "TABLE_UPDATED",
        "TABLE_IGNORED",
        "TABLE_DELETED",
    ]
    zoneId: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventActionDetails(typing.TypedDict, total=False):
    issue: str
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventConfigDetails(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventEntityDetails(typing.TypedDict, total=False):
    entity: str
    type: typing.Literal["ENTITY_TYPE_UNSPECIFIED", "TABLE", "FILESET"]

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventPartitionDetails(
    typing.TypedDict, total=False
):
    entity: str
    partition: str
    sampledDataLocations: _list[str]
    type: typing.Literal["ENTITY_TYPE_UNSPECIFIED", "TABLE", "FILESET"]

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventTableDetails(typing.TypedDict, total=False):
    table: str
    type: typing.Literal[
        "TABLE_TYPE_UNSPECIFIED", "EXTERNAL_TABLE", "BIGLAKE_TABLE", "OBJECT_TABLE"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1EncryptionConfig(typing.TypedDict, total=False):
    createTime: str
    enableMetastoreEncryption: bool
    encryptionState: typing.Literal[
        "ENCRYPTION_STATE_UNSPECIFIED", "ENCRYPTING", "COMPLETED", "FAILED"
    ]
    etag: str
    failureDetails: GoogleCloudDataplexV1EncryptionConfigFailureDetails
    key: str
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EncryptionConfigFailureDetails(
    typing.TypedDict, total=False
):
    errorCode: typing.Literal["UNKNOWN", "INTERNAL_ERROR", "REQUIRE_USER_ACTION"]
    errorMessage: str

@typing.type_check_only
class GoogleCloudDataplexV1Entity(typing.TypedDict, total=False):
    access: GoogleCloudDataplexV1StorageAccess
    asset: str
    catalogEntry: str
    compatibility: GoogleCloudDataplexV1EntityCompatibilityStatus
    createTime: str
    dataPath: str
    dataPathPattern: str
    description: str
    displayName: str
    etag: str
    format: GoogleCloudDataplexV1StorageFormat
    id: str
    name: str
    schema: GoogleCloudDataplexV1Schema
    system: typing.Literal["STORAGE_SYSTEM_UNSPECIFIED", "CLOUD_STORAGE", "BIGQUERY"]
    type: typing.Literal["TYPE_UNSPECIFIED", "TABLE", "FILESET"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntityCompatibilityStatus(typing.TypedDict, total=False):
    bigquery: GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility
    hiveMetastore: GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility

@typing.type_check_only
class GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility(
    typing.TypedDict, total=False
):
    compatible: bool
    reason: str

@typing.type_check_only
class GoogleCloudDataplexV1Entry(typing.TypedDict, total=False):
    aspects: dict[str, typing.Any]
    createTime: str
    entrySource: GoogleCloudDataplexV1EntrySource
    entryType: str
    fullyQualifiedName: str
    name: str
    parentEntry: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryGroup(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    transferStatus: typing.Literal[
        "TRANSFER_STATUS_UNSPECIFIED",
        "TRANSFER_STATUS_MIGRATED",
        "TRANSFER_STATUS_TRANSFERRED",
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryLink(typing.TypedDict, total=False):
    aspects: dict[str, typing.Any]
    createTime: str
    entryLinkType: str
    entryReferences: _list[GoogleCloudDataplexV1EntryLinkEntryReference]
    name: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryLinkEntryReference(typing.TypedDict, total=False):
    name: str
    path: str
    type: typing.Literal["UNSPECIFIED", "SOURCE", "TARGET"]

@typing.type_check_only
class GoogleCloudDataplexV1EntryLinkEvent(typing.TypedDict, total=False):
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED", "ENTRY_LINK_CREATE", "ENTRY_LINK_DELETE"
    ]
    message: str
    resource: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryLinkTypeEvent(typing.TypedDict, total=False):
    entryLinkTypeId: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "ENTRY_LINK_TYPE_CREATE",
        "ENTRY_LINK_TYPE_UPDATE",
        "ENTRY_LINK_TYPE_DELETE",
    ]
    message: str

@typing.type_check_only
class GoogleCloudDataplexV1EntrySource(typing.TypedDict, total=False):
    ancestors: _list[GoogleCloudDataplexV1EntrySourceAncestor]
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    location: str
    platform: str
    resource: str
    system: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntrySourceAncestor(typing.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryType(typing.TypedDict, total=False):
    authorization: GoogleCloudDataplexV1EntryTypeAuthorization
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    platform: str
    requiredAspects: _list[GoogleCloudDataplexV1EntryTypeAspectInfo]
    system: str
    typeAliases: _list[str]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryTypeAspectInfo(typing.TypedDict, total=False):
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1EntryTypeAuthorization(typing.TypedDict, total=False):
    alternateUsePermission: str

@typing.type_check_only
class GoogleCloudDataplexV1ExecutionIdentity(typing.TypedDict, total=False):
    dataplexServiceAgent: GoogleCloudDataplexV1ExecutionIdentityDataplexServiceAgent
    serviceAccount: GoogleCloudDataplexV1ExecutionIdentityServiceAccount
    userCredential: GoogleCloudDataplexV1ExecutionIdentityUserCredential

@typing.type_check_only
class GoogleCloudDataplexV1ExecutionIdentityDataplexServiceAgent(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ExecutionIdentityServiceAccount(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudDataplexV1ExecutionIdentityUserCredential(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1GenerateDataQualityRulesRequest(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1GenerateDataQualityRulesResponse(
    typing.TypedDict, total=False
):
    rule: _list[GoogleCloudDataplexV1DataQualityRule]

@typing.type_check_only
class GoogleCloudDataplexV1Glossary(typing.TypedDict, total=False):
    categoryCount: int
    createTime: str
    description: str
    displayName: str
    etag: str
    labels: dict[str, typing.Any]
    name: str
    termCount: int
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1GlossaryCategory(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    parent: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1GlossaryTerm(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    parent: str
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1GovernanceEvent(typing.TypedDict, total=False):
    entity: GoogleCloudDataplexV1GovernanceEventEntity
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "RESOURCE_IAM_POLICY_UPDATE",
        "BIGQUERY_TABLE_CREATE",
        "BIGQUERY_TABLE_UPDATE",
        "BIGQUERY_TABLE_DELETE",
        "BIGQUERY_CONNECTION_CREATE",
        "BIGQUERY_CONNECTION_UPDATE",
        "BIGQUERY_CONNECTION_DELETE",
        "BIGQUERY_TAXONOMY_CREATE",
        "BIGQUERY_POLICY_TAG_CREATE",
        "BIGQUERY_POLICY_TAG_DELETE",
        "BIGQUERY_POLICY_TAG_SET_IAM_POLICY",
        "ACCESS_POLICY_UPDATE",
        "GOVERNANCE_RULE_MATCHED_RESOURCES",
        "GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS",
        "GOVERNANCE_RULE_ERRORS",
        "GOVERNANCE_RULE_PROCESSING",
    ]
    message: str

@typing.type_check_only
class GoogleCloudDataplexV1GovernanceEventEntity(typing.TypedDict, total=False):
    entity: str
    entityType: typing.Literal["ENTITY_TYPE_UNSPECIFIED", "TABLE", "FILESET"]

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfile(typing.TypedDict, total=False):
    edgeTypes: _list[GoogleCloudDataplexV1GraphProfileEdgeType]
    nodeTypes: _list[GoogleCloudDataplexV1GraphProfileNodeType]

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileEdgeType(typing.TypedDict, total=False):
    description: str
    extractionHints: GoogleCloudDataplexV1GraphProfileEdgeTypeExtractionHints
    fields: _list[GoogleCloudDataplexV1GraphProfileField]
    foreignKeys: _list[GoogleCloudDataplexV1GraphProfileEdgeTypeForeignKey]
    name: str
    sourceNodeType: str
    targetNodeType: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileEdgeTypeExtractionHints(
    typing.TypedDict, total=False
):
    cardinality: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileEdgeTypeForeignKey(
    typing.TypedDict, total=False
):
    description: str
    fieldMappings: _list[
        GoogleCloudDataplexV1GraphProfileEdgeTypeForeignKeyFieldMapping
    ]
    name: str
    referencedNodeType: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileEdgeTypeForeignKeyFieldMapping(
    typing.TypedDict, total=False
):
    field: str
    referencedField: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileField(typing.TypedDict, total=False):
    dataType: str
    description: str
    extractionHints: GoogleCloudDataplexV1GraphProfileFieldExtractionHints
    fields: _list[GoogleCloudDataplexV1GraphProfileField]
    metadataType: typing.Literal[
        "METADATA_TYPE_UNSPECIFIED",
        "BOOLEAN",
        "NUMBER",
        "STRING",
        "BYTES",
        "DATETIME",
        "TIMESTAMP",
        "GEOSPATIAL",
        "STRUCT",
        "OTHER",
    ]
    mode: typing.Literal["MODE_UNSPECIFIED", "NULLABLE", "REPEATED", "REQUIRED"]
    name: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileFieldExtractionHints(
    typing.TypedDict, total=False
):
    normalization: str
    synthesis: str

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileNodeType(typing.TypedDict, total=False):
    description: str
    extractionHints: GoogleCloudDataplexV1GraphProfileNodeTypeExtractionHints
    fields: _list[GoogleCloudDataplexV1GraphProfileField]
    name: str
    primaryKeys: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1GraphProfileNodeTypeExtractionHints(
    typing.TypedDict, total=False
):
    cardinality: str

@typing.type_check_only
class GoogleCloudDataplexV1ImportItem(typing.TypedDict, total=False):
    aspectKeys: _list[str]
    entry: GoogleCloudDataplexV1Entry
    entryLink: GoogleCloudDataplexV1EntryLink
    updateMask: str

@typing.type_check_only
class GoogleCloudDataplexV1Job(typing.TypedDict, total=False):
    endTime: str
    executionSpec: GoogleCloudDataplexV1TaskExecutionSpec
    labels: dict[str, typing.Any]
    message: str
    name: str
    retryCount: int
    service: typing.Literal["SERVICE_UNSPECIFIED", "DATAPROC"]
    serviceJob: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
    ]
    trigger: typing.Literal["TRIGGER_UNSPECIFIED", "TASK_CONFIG", "RUN_REQUEST"]
    uid: str

@typing.type_check_only
class GoogleCloudDataplexV1JobEvent(typing.TypedDict, total=False):
    endTime: str
    executionTrigger: typing.Literal[
        "EXECUTION_TRIGGER_UNSPECIFIED", "TASK_CONFIG", "RUN_REQUEST"
    ]
    jobId: str
    message: str
    retries: int
    service: typing.Literal["SERVICE_UNSPECIFIED", "DATAPROC"]
    serviceJob: str
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "CANCELLED", "ABORTED"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "SPARK", "NOTEBOOK"]

@typing.type_check_only
class GoogleCloudDataplexV1Lake(typing.TypedDict, total=False):
    assetStatus: GoogleCloudDataplexV1AssetStatus
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    metastore: GoogleCloudDataplexV1LakeMetastore
    metastoreStatus: GoogleCloudDataplexV1LakeMetastoreStatus
    name: str
    serviceAccount: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1LakeMetastore(typing.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudDataplexV1LakeMetastoreStatus(typing.TypedDict, total=False):
    endpoint: str
    message: str
    state: typing.Literal["STATE_UNSPECIFIED", "NONE", "READY", "UPDATING", "ERROR"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ListActionsResponse(typing.TypedDict, total=False):
    actions: _list[GoogleCloudDataplexV1Action]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListAspectTypesResponse(typing.TypedDict, total=False):
    aspectTypes: _list[GoogleCloudDataplexV1AspectType]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListAssetsResponse(typing.TypedDict, total=False):
    assets: _list[GoogleCloudDataplexV1Asset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListChangeRequestsResponse(typing.TypedDict, total=False):
    changeRequests: _list[GoogleCloudDataplexV1ChangeRequest]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListDataAssetsResponse(typing.TypedDict, total=False):
    dataAssets: _list[GoogleCloudDataplexV1DataAsset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataAttributeBindingsResponse(
    typing.TypedDict, total=False
):
    dataAttributeBindings: _list[GoogleCloudDataplexV1DataAttributeBinding]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListDataAttributesResponse(typing.TypedDict, total=False):
    dataAttributes: _list[GoogleCloudDataplexV1DataAttribute]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListDataDomainBindingsResponse(
    typing.TypedDict, total=False
):
    dataDomainBindings: _list[GoogleCloudDataplexV1DataDomainBinding]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataDomainsResponse(typing.TypedDict, total=False):
    dataDomains: _list[GoogleCloudDataplexV1DataDomain]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataProductsResponse(typing.TypedDict, total=False):
    dataProducts: _list[GoogleCloudDataplexV1DataProduct]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScanJobsResponse(typing.TypedDict, total=False):
    dataScanJobs: _list[GoogleCloudDataplexV1DataScanJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScansResponse(typing.TypedDict, total=False):
    dataScans: _list[GoogleCloudDataplexV1DataScan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListDataTaxonomiesResponse(typing.TypedDict, total=False):
    dataTaxonomies: _list[GoogleCloudDataplexV1DataTaxonomy]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListEncryptionConfigsResponse(typing.TypedDict, total=False):
    encryptionConfigs: _list[GoogleCloudDataplexV1EncryptionConfig]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListEntitiesResponse(typing.TypedDict, total=False):
    entities: _list[GoogleCloudDataplexV1Entity]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListEntriesResponse(typing.TypedDict, total=False):
    entries: _list[GoogleCloudDataplexV1Entry]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListEntryGroupsResponse(typing.TypedDict, total=False):
    entryGroups: _list[GoogleCloudDataplexV1EntryGroup]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListEntryTypesResponse(typing.TypedDict, total=False):
    entryTypes: _list[GoogleCloudDataplexV1EntryType]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListGlossariesResponse(typing.TypedDict, total=False):
    glossaries: _list[GoogleCloudDataplexV1Glossary]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListGlossaryCategoriesResponse(
    typing.TypedDict, total=False
):
    categories: _list[GoogleCloudDataplexV1GlossaryCategory]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListGlossaryTermsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    terms: _list[GoogleCloudDataplexV1GlossaryTerm]
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[GoogleCloudDataplexV1Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListLakesResponse(typing.TypedDict, total=False):
    lakes: _list[GoogleCloudDataplexV1Lake]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListMetadataFeedsResponse(typing.TypedDict, total=False):
    metadataFeeds: _list[GoogleCloudDataplexV1MetadataFeed]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListMetadataJobsResponse(typing.TypedDict, total=False):
    metadataJobs: _list[GoogleCloudDataplexV1MetadataJob]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListPartitionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    partitions: _list[GoogleCloudDataplexV1Partition]

@typing.type_check_only
class GoogleCloudDataplexV1ListTasksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[GoogleCloudDataplexV1Task]
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListZonesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    zones: _list[GoogleCloudDataplexV1Zone]

@typing.type_check_only
class GoogleCloudDataplexV1LookupContextRequest(typing.TypedDict, total=False):
    options: dict[str, typing.Any]
    resources: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1LookupContextResponse(typing.TypedDict, total=False):
    context: str

@typing.type_check_only
class GoogleCloudDataplexV1LookupEntryLinksResponse(typing.TypedDict, total=False):
    entryLinks: _list[GoogleCloudDataplexV1EntryLink]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataFeed(typing.TypedDict, total=False):
    createTime: str
    filters: GoogleCloudDataplexV1MetadataFeedFilters
    labels: dict[str, typing.Any]
    name: str
    pubsubTopic: str
    scope: GoogleCloudDataplexV1MetadataFeedScope
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataFeedFilters(typing.TypedDict, total=False):
    aspectTypes: _list[str]
    changeTypes: _list[
        typing.Literal["CHANGE_TYPE_UNSPECIFIED", "CREATE", "UPDATE", "DELETE"]
    ]
    entryTypes: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1MetadataFeedScope(typing.TypedDict, total=False):
    entryGroups: _list[str]
    organizationLevel: bool
    projects: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJob(typing.TypedDict, total=False):
    createTime: str
    exportResult: GoogleCloudDataplexV1MetadataJobExportJobResult
    exportSpec: GoogleCloudDataplexV1MetadataJobExportJobSpec
    importResult: GoogleCloudDataplexV1MetadataJobImportJobResult
    importSpec: GoogleCloudDataplexV1MetadataJobImportJobSpec
    labels: dict[str, typing.Any]
    name: str
    status: GoogleCloudDataplexV1MetadataJobStatus
    type: typing.Literal["TYPE_UNSPECIFIED", "IMPORT", "EXPORT"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobExportJobResult(typing.TypedDict, total=False):
    errorMessage: str
    exportedEntries: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobExportJobSpec(typing.TypedDict, total=False):
    outputPath: str
    scope: GoogleCloudDataplexV1MetadataJobExportJobSpecExportJobScope

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobExportJobSpecExportJobScope(
    typing.TypedDict, total=False
):
    aspectTypes: _list[str]
    entryGroups: _list[str]
    entryTypes: _list[str]
    organizationLevel: bool
    projects: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobImportJobResult(typing.TypedDict, total=False):
    createdEntries: str
    createdEntryLinks: str
    deletedEntries: str
    deletedEntryLinks: str
    recreatedEntries: str
    unchangedEntries: str
    unchangedEntryLinks: str
    updateTime: str
    updatedEntries: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobImportJobSpec(typing.TypedDict, total=False):
    aspectSyncMode: typing.Literal[
        "SYNC_MODE_UNSPECIFIED", "FULL", "INCREMENTAL", "NONE"
    ]
    entrySyncMode: typing.Literal[
        "SYNC_MODE_UNSPECIFIED", "FULL", "INCREMENTAL", "NONE"
    ]
    logLevel: typing.Literal["LOG_LEVEL_UNSPECIFIED", "DEBUG", "INFO"]
    scope: GoogleCloudDataplexV1MetadataJobImportJobSpecImportJobScope
    sourceCreateTime: str
    sourceStorageUri: str

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobImportJobSpecImportJobScope(
    typing.TypedDict, total=False
):
    aspectTypes: _list[str]
    entryGroups: _list[str]
    entryLinkTypes: _list[str]
    entryTypes: _list[str]
    glossaries: _list[str]
    referencedEntryScopes: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1MetadataJobStatus(typing.TypedDict, total=False):
    completionPercent: int
    message: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "QUEUED",
        "RUNNING",
        "CANCELING",
        "CANCELED",
        "SUCCEEDED",
        "FAILED",
        "SUCCEEDED_WITH_ERRORS",
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ModifyEntryRequest(typing.TypedDict, total=False):
    aspectKeys: _list[str]
    deleteMissingAspects: bool
    entry: GoogleCloudDataplexV1Entry
    updateMask: str

@typing.type_check_only
class GoogleCloudDataplexV1OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudDataplexV1Partition(typing.TypedDict, total=False):
    etag: str
    location: str
    name: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1RejectChangeRequestRequest(typing.TypedDict, total=False):
    comment: str
    etag: str

@typing.type_check_only
class GoogleCloudDataplexV1RequestDataProductAccessRequest(
    typing.TypedDict, total=False
):
    changeRequest: GoogleCloudDataplexV1ChangeRequest
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDataplexV1RequestDataProductAccessResponse(
    typing.TypedDict, total=False
):
    changeRequestName: str

@typing.type_check_only
class GoogleCloudDataplexV1ResourceAccessSpec(typing.TypedDict, total=False):
    owners: _list[str]
    readers: _list[str]
    writers: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1RunDataScanRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1RunDataScanResponse(typing.TypedDict, total=False):
    job: GoogleCloudDataplexV1DataScanJob

@typing.type_check_only
class GoogleCloudDataplexV1RunTaskRequest(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    labels: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDataplexV1RunTaskResponse(typing.TypedDict, total=False):
    job: GoogleCloudDataplexV1Job

@typing.type_check_only
class GoogleCloudDataplexV1ScannedData(typing.TypedDict, total=False):
    incrementalField: GoogleCloudDataplexV1ScannedDataIncrementalField

@typing.type_check_only
class GoogleCloudDataplexV1ScannedDataIncrementalField(typing.TypedDict, total=False):
    end: str
    field: str
    start: str

@typing.type_check_only
class GoogleCloudDataplexV1Schema(typing.TypedDict, total=False):
    fields: _list[GoogleCloudDataplexV1SchemaSchemaField]
    partitionFields: _list[GoogleCloudDataplexV1SchemaPartitionField]
    partitionStyle: typing.Literal["PARTITION_STYLE_UNSPECIFIED", "HIVE_COMPATIBLE"]
    userManaged: bool

@typing.type_check_only
class GoogleCloudDataplexV1SchemaPartitionField(typing.TypedDict, total=False):
    name: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "BOOLEAN",
        "BYTE",
        "INT16",
        "INT32",
        "INT64",
        "FLOAT",
        "DOUBLE",
        "DECIMAL",
        "STRING",
        "BINARY",
        "TIMESTAMP",
        "DATE",
        "TIME",
        "RECORD",
        "NULL",
    ]

@typing.type_check_only
class GoogleCloudDataplexV1SchemaSchemaField(typing.TypedDict, total=False):
    description: str
    fields: _list[GoogleCloudDataplexV1SchemaSchemaField]
    mode: typing.Literal["MODE_UNSPECIFIED", "REQUIRED", "NULLABLE", "REPEATED"]
    name: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "BOOLEAN",
        "BYTE",
        "INT16",
        "INT32",
        "INT64",
        "FLOAT",
        "DOUBLE",
        "DECIMAL",
        "STRING",
        "BINARY",
        "TIMESTAMP",
        "DATE",
        "TIME",
        "RECORD",
        "NULL",
    ]

@typing.type_check_only
class GoogleCloudDataplexV1SearchEntriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[GoogleCloudDataplexV1SearchEntriesResult]
    totalSize: int
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1SearchEntriesResult(typing.TypedDict, total=False):
    dataplexEntry: GoogleCloudDataplexV1Entry
    linkedResource: str
    snippets: GoogleCloudDataplexV1SearchEntriesResultSnippets

@typing.type_check_only
class GoogleCloudDataplexV1SearchEntriesResultSnippets(typing.TypedDict, total=False):
    dataplexEntry: GoogleCloudDataplexV1Entry

@typing.type_check_only
class GoogleCloudDataplexV1SessionEvent(typing.TypedDict, total=False):
    eventSucceeded: bool
    fastStartupEnabled: bool
    message: str
    query: GoogleCloudDataplexV1SessionEventQueryDetail
    sessionId: str
    type: typing.Literal["EVENT_TYPE_UNSPECIFIED", "START", "STOP", "QUERY", "CREATE"]
    unassignedDuration: str
    userId: str

@typing.type_check_only
class GoogleCloudDataplexV1SessionEventQueryDetail(typing.TypedDict, total=False):
    dataProcessedBytes: str
    duration: str
    engine: typing.Literal["ENGINE_UNSPECIFIED", "SPARK_SQL", "BIGQUERY"]
    queryId: str
    queryText: str
    resultSizeBytes: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageAccess(typing.TypedDict, total=False):
    read: typing.Literal["ACCESS_MODE_UNSPECIFIED", "DIRECT", "MANAGED"]

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormat(typing.TypedDict, total=False):
    compressionFormat: typing.Literal["COMPRESSION_FORMAT_UNSPECIFIED", "GZIP", "BZIP2"]
    csv: GoogleCloudDataplexV1StorageFormatCsvOptions
    format: typing.Literal[
        "FORMAT_UNSPECIFIED",
        "PARQUET",
        "AVRO",
        "ORC",
        "CSV",
        "JSON",
        "IMAGE",
        "AUDIO",
        "VIDEO",
        "TEXT",
        "TFRECORD",
        "OTHER",
        "UNKNOWN",
    ]
    iceberg: GoogleCloudDataplexV1StorageFormatIcebergOptions
    json: GoogleCloudDataplexV1StorageFormatJsonOptions
    mimeType: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormatCsvOptions(typing.TypedDict, total=False):
    delimiter: str
    encoding: str
    headerRows: int
    quote: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormatIcebergOptions(typing.TypedDict, total=False):
    metadataLocation: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormatJsonOptions(typing.TypedDict, total=False):
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1Task(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    executionSpec: GoogleCloudDataplexV1TaskExecutionSpec
    executionStatus: GoogleCloudDataplexV1TaskExecutionStatus
    labels: dict[str, typing.Any]
    name: str
    notebook: GoogleCloudDataplexV1TaskNotebookTaskConfig
    spark: GoogleCloudDataplexV1TaskSparkTaskConfig
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    triggerSpec: GoogleCloudDataplexV1TaskTriggerSpec
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskExecutionSpec(typing.TypedDict, total=False):
    args: dict[str, typing.Any]
    kmsKey: str
    maxJobExecutionLifetime: str
    project: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskExecutionStatus(typing.TypedDict, total=False):
    latestJob: GoogleCloudDataplexV1Job
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpec(typing.TypedDict, total=False):
    batch: GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResources
    containerImage: GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntime
    vpcNetwork: GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetwork

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResources(
    typing.TypedDict, total=False
):
    executorsCount: int
    maxExecutorsCount: int

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntime(
    typing.TypedDict, total=False
):
    image: str
    javaJars: _list[str]
    properties: dict[str, typing.Any]
    pythonPackages: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetwork(
    typing.TypedDict, total=False
):
    network: str
    networkTags: _list[str]
    subNetwork: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskNotebookTaskConfig(typing.TypedDict, total=False):
    archiveUris: _list[str]
    fileUris: _list[str]
    infrastructureSpec: GoogleCloudDataplexV1TaskInfrastructureSpec
    notebook: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskSparkTaskConfig(typing.TypedDict, total=False):
    archiveUris: _list[str]
    fileUris: _list[str]
    infrastructureSpec: GoogleCloudDataplexV1TaskInfrastructureSpec
    mainClass: str
    mainJarFileUri: str
    pythonScriptFile: str
    sqlScript: str
    sqlScriptFile: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskTriggerSpec(typing.TypedDict, total=False):
    disabled: bool
    maxRetries: int
    schedule: str
    startTime: str
    type: typing.Literal["TYPE_UNSPECIFIED", "ON_DEMAND", "RECURRING"]

@typing.type_check_only
class GoogleCloudDataplexV1Trigger(typing.TypedDict, total=False):
    onDemand: GoogleCloudDataplexV1TriggerOnDemand
    oneTime: GoogleCloudDataplexV1TriggerOneTime
    schedule: GoogleCloudDataplexV1TriggerSchedule

@typing.type_check_only
class GoogleCloudDataplexV1TriggerOnDemand(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1TriggerOneTime(typing.TypedDict, total=False):
    ttlAfterScanCompletion: str

@typing.type_check_only
class GoogleCloudDataplexV1TriggerSchedule(typing.TypedDict, total=False):
    cron: str

@typing.type_check_only
class GoogleCloudDataplexV1UnstructuredDataProfileResult(typing.TypedDict, total=False):
    description: str
    graphProfile: GoogleCloudDataplexV1GraphProfile
    partialFailureMessage: str

@typing.type_check_only
class GoogleCloudDataplexV1UnstructuredDataProfileSpec(typing.TypedDict, total=False):
    customizedPrompt: str
    globalEndpointEnabled: bool
    graphProfilePublishingEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1UpdateEntryRequest(typing.TypedDict, total=False):
    allowMissing: bool
    aspectKeys: _list[str]
    deleteMissingAspects: bool
    entry: GoogleCloudDataplexV1Entry
    updateMask: str

@typing.type_check_only
class GoogleCloudDataplexV1UpdateGlossaryCategoryRequest(typing.TypedDict, total=False):
    category: GoogleCloudDataplexV1GlossaryCategory
    updateMask: str

@typing.type_check_only
class GoogleCloudDataplexV1UpdateGlossaryRequest(typing.TypedDict, total=False):
    glossary: GoogleCloudDataplexV1Glossary
    updateMask: str
    validateOnly: bool

@typing.type_check_only
class GoogleCloudDataplexV1UpdateGlossaryTermRequest(typing.TypedDict, total=False):
    term: GoogleCloudDataplexV1GlossaryTerm
    updateMask: str

@typing.type_check_only
class GoogleCloudDataplexV1Zone(typing.TypedDict, total=False):
    assetStatus: GoogleCloudDataplexV1AssetStatus
    createTime: str
    description: str
    discoverySpec: GoogleCloudDataplexV1ZoneDiscoverySpec
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    resourceSpec: GoogleCloudDataplexV1ZoneResourceSpec
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "RAW", "CURATED"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpec(typing.TypedDict, total=False):
    csvOptions: GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions
    enabled: bool
    excludePatterns: _list[str]
    includePatterns: _list[str]
    jsonOptions: GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions
    schedule: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions(typing.TypedDict, total=False):
    delimiter: str
    disableTypeInference: bool
    encoding: str
    headerRows: int

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions(typing.TypedDict, total=False):
    disableTypeInference: bool
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneResourceSpec(typing.TypedDict, total=False):
    locationType: typing.Literal[
        "LOCATION_TYPE_UNSPECIFIED", "SINGLE_REGION", "MULTI_REGION"
    ]

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1ResourcePolicyMember(typing.TypedDict, total=False):
    iamPolicyNamePrincipal: str
    iamPolicyUidPrincipal: str

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
