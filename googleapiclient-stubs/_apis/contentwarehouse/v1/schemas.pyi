import typing

_list = list

@typing.type_check_only
class CloudAiPlatformTenantresourceCloudSqlInstanceConfig(
    typing.TypedDict, total=False
):
    cloudSqlInstanceConnectionName: str
    cloudSqlInstanceName: str
    kmsKeyReference: str
    mdbRolesForCorpAccess: _list[str]
    slmInstanceName: str
    slmInstanceTemplate: str
    slmInstanceType: str

@typing.type_check_only
class CloudAiPlatformTenantresourceGcsBucketConfig(typing.TypedDict, total=False):
    admins: _list[str]
    bucketName: str
    entityName: str
    kmsKeyReference: str
    ttlDays: int
    viewers: _list[str]

@typing.type_check_only
class CloudAiPlatformTenantresourceIamPolicyBinding(typing.TypedDict, total=False):
    members: _list[str]
    resource: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "PROJECT",
        "SERVICE_ACCOUNT",
        "GCS_BUCKET",
        "SERVICE_CONSUMER",
        "AR_REPO",
    ]
    role: str

@typing.type_check_only
class CloudAiPlatformTenantresourceInfraSpannerConfig(typing.TypedDict, total=False):
    createDatabaseOptions: (
        CloudAiPlatformTenantresourceInfraSpannerConfigCreateDatabaseOptions
    )
    kmsKeyReference: str
    sdlBundlePath: str
    spannerBorgServiceAccount: str
    spannerLocalNamePrefix: str
    spannerNamespace: str
    spannerUniverse: str

@typing.type_check_only
class CloudAiPlatformTenantresourceInfraSpannerConfigCreateDatabaseOptions(
    typing.TypedDict, total=False
):
    cmekCloudResourceName: str
    cmekCloudResourceType: str
    cmekServiceName: str

@typing.type_check_only
class CloudAiPlatformTenantresourceServiceAccountIdentity(
    typing.TypedDict, total=False
):
    serviceAccountEmail: str
    tag: str

@typing.type_check_only
class CloudAiPlatformTenantresourceTenantProjectConfig(typing.TypedDict, total=False):
    billingConfig: GoogleApiServiceconsumermanagementV1BillingConfig
    folder: str
    policyBindings: _list[GoogleApiServiceconsumermanagementV1PolicyBinding]
    services: _list[str]

@typing.type_check_only
class CloudAiPlatformTenantresourceTenantProjectResource(typing.TypedDict, total=False):
    cloudSqlInstances: _list[CloudAiPlatformTenantresourceCloudSqlInstanceConfig]
    gcsBuckets: _list[CloudAiPlatformTenantresourceGcsBucketConfig]
    iamPolicyBindings: _list[CloudAiPlatformTenantresourceIamPolicyBinding]
    infraSpannerConfigs: _list[CloudAiPlatformTenantresourceInfraSpannerConfig]
    tag: str
    tenantProjectConfig: CloudAiPlatformTenantresourceTenantProjectConfig
    tenantProjectId: str
    tenantProjectNumber: str
    tenantServiceAccounts: _list[
        CloudAiPlatformTenantresourceTenantServiceAccountIdentity
    ]

@typing.type_check_only
class CloudAiPlatformTenantresourceTenantResource(typing.TypedDict, total=False):
    p4ServiceAccounts: _list[CloudAiPlatformTenantresourceServiceAccountIdentity]
    tenantProjectResources: _list[CloudAiPlatformTenantresourceTenantProjectResource]

@typing.type_check_only
class CloudAiPlatformTenantresourceTenantServiceAccountIdentity(
    typing.TypedDict, total=False
):
    serviceAccountEmail: str
    serviceName: str

@typing.type_check_only
class GoogleApiServiceconsumermanagementV1BillingConfig(typing.TypedDict, total=False):
    billingAccount: str

@typing.type_check_only
class GoogleApiServiceconsumermanagementV1PolicyBinding(typing.TypedDict, total=False):
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1AccessControlAction(typing.TypedDict, total=False):
    operationType: typing.Literal[
        "UNKNOWN",
        "ADD_POLICY_BINDING",
        "REMOVE_POLICY_BINDING",
        "REPLACE_POLICY_BINDING",
    ]
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleCloudContentwarehouseV1Action(typing.TypedDict, total=False):
    accessControl: GoogleCloudContentwarehouseV1AccessControlAction
    actionId: str
    addToFolder: GoogleCloudContentwarehouseV1AddToFolderAction
    dataUpdate: GoogleCloudContentwarehouseV1DataUpdateAction
    dataValidation: GoogleCloudContentwarehouseV1DataValidationAction
    deleteDocumentAction: GoogleCloudContentwarehouseV1DeleteDocumentAction
    publishToPubSub: GoogleCloudContentwarehouseV1PublishAction
    removeFromFolderAction: GoogleCloudContentwarehouseV1RemoveFromFolderAction

@typing.type_check_only
class GoogleCloudContentwarehouseV1ActionExecutorOutput(typing.TypedDict, total=False):
    ruleActionsPairs: _list[GoogleCloudContentwarehouseV1RuleActionsPair]

@typing.type_check_only
class GoogleCloudContentwarehouseV1ActionOutput(typing.TypedDict, total=False):
    actionId: str
    actionState: typing.Literal[
        "UNKNOWN",
        "ACTION_SUCCEEDED",
        "ACTION_FAILED",
        "ACTION_TIMED_OUT",
        "ACTION_PENDING",
    ]
    outputMessage: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1AddToFolderAction(typing.TypedDict, total=False):
    folders: _list[str]

@typing.type_check_only
class GoogleCloudContentwarehouseV1CloudAIDocumentOption(typing.TypedDict, total=False):
    customizedEntitiesPropertiesConversions: dict[str, typing.Any]
    enableEntitiesConversions: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1CreateDocumentLinkRequest(
    typing.TypedDict, total=False
):
    documentLink: GoogleCloudContentwarehouseV1DocumentLink
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1CreateDocumentMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1CreateDocumentRequest(typing.TypedDict, total=False):
    cloudAiDocumentOption: GoogleCloudContentwarehouseV1CloudAIDocumentOption
    createMask: str
    document: GoogleCloudContentwarehouseV1Document
    policy: GoogleIamV1Policy
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1CreateDocumentResponse(
    typing.TypedDict, total=False
):
    document: GoogleCloudContentwarehouseV1Document
    longRunningOperations: _list[GoogleLongrunningOperation]
    metadata: GoogleCloudContentwarehouseV1ResponseMetadata
    ruleEngineOutput: GoogleCloudContentwarehouseV1RuleEngineOutput

@typing.type_check_only
class GoogleCloudContentwarehouseV1CustomWeightsMetadata(typing.TypedDict, total=False):
    weightedSchemaProperties: _list[GoogleCloudContentwarehouseV1WeightedSchemaProperty]

@typing.type_check_only
class GoogleCloudContentwarehouseV1DataUpdateAction(typing.TypedDict, total=False):
    entries: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContentwarehouseV1DataValidationAction(typing.TypedDict, total=False):
    conditions: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContentwarehouseV1DateTimeArray(typing.TypedDict, total=False):
    values: _list[GoogleTypeDateTime]

@typing.type_check_only
class GoogleCloudContentwarehouseV1DateTimeTypeOptions(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1DeleteDocumentAction(typing.TypedDict, total=False):
    enableHardDelete: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1DeleteDocumentLinkRequest(
    typing.TypedDict, total=False
):
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1DeleteDocumentRequest(typing.TypedDict, total=False):
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1Document(typing.TypedDict, total=False):
    cloudAiDocument: GoogleCloudDocumentaiV1Document
    contentCategory: typing.Literal[
        "CONTENT_CATEGORY_UNSPECIFIED",
        "CONTENT_CATEGORY_IMAGE",
        "CONTENT_CATEGORY_AUDIO",
        "CONTENT_CATEGORY_VIDEO",
    ]
    createTime: str
    creator: str
    displayName: str
    displayUri: str
    dispositionTime: str
    documentSchemaName: str
    inlineRawDocument: str
    legalHold: bool
    name: str
    plainText: str
    properties: _list[GoogleCloudContentwarehouseV1Property]
    rawDocumentFileType: typing.Literal[
        "RAW_DOCUMENT_FILE_TYPE_UNSPECIFIED",
        "RAW_DOCUMENT_FILE_TYPE_PDF",
        "RAW_DOCUMENT_FILE_TYPE_DOCX",
        "RAW_DOCUMENT_FILE_TYPE_XLSX",
        "RAW_DOCUMENT_FILE_TYPE_PPTX",
        "RAW_DOCUMENT_FILE_TYPE_TEXT",
        "RAW_DOCUMENT_FILE_TYPE_TIFF",
    ]
    rawDocumentPath: str
    referenceId: str
    textExtractionDisabled: bool
    textExtractionEnabled: bool
    title: str
    updateTime: str
    updater: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentLink(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    sourceDocumentReference: GoogleCloudContentwarehouseV1DocumentReference
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "SOFT_DELETED"]
    targetDocumentReference: GoogleCloudContentwarehouseV1DocumentReference
    updateTime: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentQuery(typing.TypedDict, total=False):
    customPropertyFilter: str
    customWeightsMetadata: GoogleCloudContentwarehouseV1CustomWeightsMetadata
    documentCreatorFilter: _list[str]
    documentNameFilter: _list[str]
    documentSchemaNames: _list[str]
    fileTypeFilter: GoogleCloudContentwarehouseV1FileTypeFilter
    folderNameFilter: str
    isNlQuery: bool
    propertyFilter: _list[GoogleCloudContentwarehouseV1PropertyFilter]
    query: str
    queryContext: _list[str]
    timeFilters: _list[GoogleCloudContentwarehouseV1TimeFilter]

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentReference(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    displayName: str
    documentIsFolder: bool
    documentIsLegalHoldFolder: bool
    documentIsRetentionFolder: bool
    documentName: str
    snippet: str
    updateTime: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1DocumentSchema(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentIsFolder: bool
    name: str
    propertyDefinitions: _list[GoogleCloudContentwarehouseV1PropertyDefinition]
    updateTime: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1EnumArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudContentwarehouseV1EnumTypeOptions(typing.TypedDict, total=False):
    possibleValues: _list[str]
    validationCheckDisabled: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1EnumValue(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ExportToCdwPipeline(typing.TypedDict, total=False):
    docAiDataset: str
    documents: _list[str]
    exportFolderPath: str
    trainingSplitRatio: float

@typing.type_check_only
class GoogleCloudContentwarehouseV1FetchAclRequest(typing.TypedDict, total=False):
    projectOwner: bool
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1FetchAclResponse(typing.TypedDict, total=False):
    metadata: GoogleCloudContentwarehouseV1ResponseMetadata
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleCloudContentwarehouseV1FileTypeFilter(typing.TypedDict, total=False):
    fileType: typing.Literal[
        "FILE_TYPE_UNSPECIFIED", "ALL", "FOLDER", "DOCUMENT", "ROOT_FOLDER"
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1FloatArray(typing.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class GoogleCloudContentwarehouseV1FloatTypeOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1GcsIngestPipeline(typing.TypedDict, total=False):
    inputPath: str
    pipelineConfig: GoogleCloudContentwarehouseV1IngestPipelineConfig
    processorType: str
    schemaName: str
    skipIngestedDocuments: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1GcsIngestWithDocAiProcessorsPipeline(
    typing.TypedDict, total=False
):
    extractProcessorInfos: _list[GoogleCloudContentwarehouseV1ProcessorInfo]
    inputPath: str
    pipelineConfig: GoogleCloudContentwarehouseV1IngestPipelineConfig
    processorResultsFolderPath: str
    skipIngestedDocuments: bool
    splitClassifyProcessorInfo: GoogleCloudContentwarehouseV1ProcessorInfo

@typing.type_check_only
class GoogleCloudContentwarehouseV1GetDocumentRequest(typing.TypedDict, total=False):
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1HistogramQuery(typing.TypedDict, total=False):
    filters: GoogleCloudContentwarehouseV1HistogramQueryPropertyNameFilter
    histogramQuery: str
    requirePreciseResultSize: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1HistogramQueryPropertyNameFilter(
    typing.TypedDict, total=False
):
    documentSchemas: _list[str]
    propertyNames: _list[str]
    yAxis: typing.Literal["HISTOGRAM_YAXIS_DOCUMENT", "HISTOGRAM_YAXIS_PROPERTY"]

@typing.type_check_only
class GoogleCloudContentwarehouseV1HistogramQueryResult(typing.TypedDict, total=False):
    histogram: dict[str, typing.Any]
    histogramQuery: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1IngestPipelineConfig(typing.TypedDict, total=False):
    cloudFunction: str
    documentAclPolicy: GoogleIamV1Policy
    enableDocumentTextExtraction: bool
    folder: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1InitializeProjectRequest(
    typing.TypedDict, total=False
):
    accessControlMode: typing.Literal[
        "ACL_MODE_UNKNOWN",
        "ACL_MODE_UNIVERSAL_ACCESS",
        "ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID",
        "ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI",
    ]
    databaseType: typing.Literal[
        "DB_UNKNOWN", "DB_INFRA_SPANNER", "DB_CLOUD_SQL_POSTGRES"
    ]
    documentCreatorDefaultRole: typing.Literal[
        "DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED",
        "DOCUMENT_ADMIN",
        "DOCUMENT_EDITOR",
        "DOCUMENT_VIEWER",
    ]
    enableCalUserEmailLogging: bool
    kmsKey: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1InitializeProjectResponse(
    typing.TypedDict, total=False
):
    message: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "CANCELLED", "RUNNING"
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1IntegerArray(typing.TypedDict, total=False):
    values: _list[int]

@typing.type_check_only
class GoogleCloudContentwarehouseV1IntegerTypeOptions(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1InvalidRule(typing.TypedDict, total=False):
    error: str
    rule: GoogleCloudContentwarehouseV1Rule

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListDocumentSchemasResponse(
    typing.TypedDict, total=False
):
    documentSchemas: _list[GoogleCloudContentwarehouseV1DocumentSchema]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedSourcesRequest(
    typing.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedSourcesResponse(
    typing.TypedDict, total=False
):
    documentLinks: _list[GoogleCloudContentwarehouseV1DocumentLink]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedTargetsRequest(
    typing.TypedDict, total=False
):
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListLinkedTargetsResponse(
    typing.TypedDict, total=False
):
    documentLinks: _list[GoogleCloudContentwarehouseV1DocumentLink]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListRuleSetsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ruleSets: _list[GoogleCloudContentwarehouseV1RuleSet]

@typing.type_check_only
class GoogleCloudContentwarehouseV1ListSynonymSetsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    synonymSets: _list[GoogleCloudContentwarehouseV1SynonymSet]

@typing.type_check_only
class GoogleCloudContentwarehouseV1LockDocumentRequest(typing.TypedDict, total=False):
    collectionId: str
    lockingUser: GoogleCloudContentwarehouseV1UserInfo

@typing.type_check_only
class GoogleCloudContentwarehouseV1MapProperty(typing.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudContentwarehouseV1MapTypeOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1MergeFieldsOptions(typing.TypedDict, total=False):
    replaceMessageFields: bool
    replaceRepeatedFields: bool

@typing.type_check_only
class GoogleCloudContentwarehouseV1ProcessWithDocAiPipeline(
    typing.TypedDict, total=False
):
    documents: _list[str]
    exportFolderPath: str
    processorInfo: GoogleCloudContentwarehouseV1ProcessorInfo
    processorResultsFolderPath: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ProcessorInfo(typing.TypedDict, total=False):
    documentType: str
    processorName: str
    schemaName: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1ProjectStatus(typing.TypedDict, total=False):
    accessControlMode: typing.Literal[
        "ACL_MODE_UNKNOWN",
        "ACL_MODE_UNIVERSAL_ACCESS",
        "ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID",
        "ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI",
    ]
    databaseType: typing.Literal[
        "DB_UNKNOWN", "DB_INFRA_SPANNER", "DB_CLOUD_SQL_POSTGRES"
    ]
    documentCreatorDefaultRole: str
    location: str
    qaEnabled: bool
    state: typing.Literal[
        "PROJECT_STATE_UNSPECIFIED",
        "PROJECT_STATE_PENDING",
        "PROJECT_STATE_COMPLETED",
        "PROJECT_STATE_FAILED",
        "PROJECT_STATE_DELETING",
        "PROJECT_STATE_DELETING_FAILED",
        "PROJECT_STATE_DELETED",
        "PROJECT_STATE_NOT_FOUND",
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1Property(typing.TypedDict, total=False):
    dateTimeValues: GoogleCloudContentwarehouseV1DateTimeArray
    enumValues: GoogleCloudContentwarehouseV1EnumArray
    floatValues: GoogleCloudContentwarehouseV1FloatArray
    integerValues: GoogleCloudContentwarehouseV1IntegerArray
    mapProperty: GoogleCloudContentwarehouseV1MapProperty
    name: str
    propertyValues: GoogleCloudContentwarehouseV1PropertyArray
    textValues: GoogleCloudContentwarehouseV1TextArray
    timestampValues: GoogleCloudContentwarehouseV1TimestampArray

@typing.type_check_only
class GoogleCloudContentwarehouseV1PropertyArray(typing.TypedDict, total=False):
    properties: _list[GoogleCloudContentwarehouseV1Property]

@typing.type_check_only
class GoogleCloudContentwarehouseV1PropertyDefinition(typing.TypedDict, total=False):
    dateTimeTypeOptions: GoogleCloudContentwarehouseV1DateTimeTypeOptions
    displayName: str
    enumTypeOptions: GoogleCloudContentwarehouseV1EnumTypeOptions
    floatTypeOptions: GoogleCloudContentwarehouseV1FloatTypeOptions
    integerTypeOptions: GoogleCloudContentwarehouseV1IntegerTypeOptions
    isFilterable: bool
    isMetadata: bool
    isRepeatable: bool
    isRequired: bool
    isSearchable: bool
    mapTypeOptions: GoogleCloudContentwarehouseV1MapTypeOptions
    name: str
    propertyTypeOptions: GoogleCloudContentwarehouseV1PropertyTypeOptions
    retrievalImportance: typing.Literal[
        "RETRIEVAL_IMPORTANCE_UNSPECIFIED",
        "HIGHEST",
        "HIGHER",
        "HIGH",
        "MEDIUM",
        "LOW",
        "LOWEST",
    ]
    schemaSources: _list[GoogleCloudContentwarehouseV1PropertyDefinitionSchemaSource]
    textTypeOptions: GoogleCloudContentwarehouseV1TextTypeOptions
    timestampTypeOptions: GoogleCloudContentwarehouseV1TimestampTypeOptions

@typing.type_check_only
class GoogleCloudContentwarehouseV1PropertyDefinitionSchemaSource(
    typing.TypedDict, total=False
):
    name: str
    processorType: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1PropertyFilter(typing.TypedDict, total=False):
    condition: str
    documentSchemaName: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1PropertyTypeOptions(typing.TypedDict, total=False):
    propertyDefinitions: _list[GoogleCloudContentwarehouseV1PropertyDefinition]

@typing.type_check_only
class GoogleCloudContentwarehouseV1PublishAction(typing.TypedDict, total=False):
    messages: _list[str]
    topicId: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1QAResult(typing.TypedDict, total=False):
    confidenceScore: float
    highlights: _list[GoogleCloudContentwarehouseV1QAResultHighlight]

@typing.type_check_only
class GoogleCloudContentwarehouseV1QAResultHighlight(typing.TypedDict, total=False):
    endIndex: int
    startIndex: int

@typing.type_check_only
class GoogleCloudContentwarehouseV1RemoveFromFolderAction(
    typing.TypedDict, total=False
):
    condition: str
    folder: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1RequestMetadata(typing.TypedDict, total=False):
    userInfo: GoogleCloudContentwarehouseV1UserInfo

@typing.type_check_only
class GoogleCloudContentwarehouseV1ResponseMetadata(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1Rule(typing.TypedDict, total=False):
    actions: _list[GoogleCloudContentwarehouseV1Action]
    condition: str
    description: str
    ruleId: str
    triggerType: typing.Literal[
        "UNKNOWN", "ON_CREATE", "ON_UPDATE", "ON_CREATE_LINK", "ON_DELETE_LINK"
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1RuleActionsPair(typing.TypedDict, total=False):
    actionOutputs: _list[GoogleCloudContentwarehouseV1ActionOutput]
    rule: GoogleCloudContentwarehouseV1Rule

@typing.type_check_only
class GoogleCloudContentwarehouseV1RuleEngineOutput(typing.TypedDict, total=False):
    actionExecutorOutput: GoogleCloudContentwarehouseV1ActionExecutorOutput
    documentName: str
    ruleEvaluatorOutput: GoogleCloudContentwarehouseV1RuleEvaluatorOutput

@typing.type_check_only
class GoogleCloudContentwarehouseV1RuleEvaluatorOutput(typing.TypedDict, total=False):
    invalidRules: _list[GoogleCloudContentwarehouseV1InvalidRule]
    matchedRules: _list[GoogleCloudContentwarehouseV1Rule]
    triggeredRules: _list[GoogleCloudContentwarehouseV1Rule]

@typing.type_check_only
class GoogleCloudContentwarehouseV1RuleSet(typing.TypedDict, total=False):
    description: str
    name: str
    rules: _list[GoogleCloudContentwarehouseV1Rule]
    source: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineMetadata(typing.TypedDict, total=False):
    exportToCdwPipelineMetadata: (
        GoogleCloudContentwarehouseV1RunPipelineMetadataExportToCdwPipelineMetadata
    )
    failedFileCount: int
    gcsIngestPipelineMetadata: (
        GoogleCloudContentwarehouseV1RunPipelineMetadataGcsIngestPipelineMetadata
    )
    individualDocumentStatuses: _list[
        GoogleCloudContentwarehouseV1RunPipelineMetadataIndividualDocumentStatus
    ]
    processWithDocAiPipelineMetadata: (
        GoogleCloudContentwarehouseV1RunPipelineMetadataProcessWithDocAiPipelineMetadata
    )
    totalFileCount: int
    userInfo: GoogleCloudContentwarehouseV1UserInfo

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineMetadataExportToCdwPipelineMetadata(
    typing.TypedDict, total=False
):
    docAiDataset: str
    documents: _list[str]
    outputPath: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineMetadataGcsIngestPipelineMetadata(
    typing.TypedDict, total=False
):
    inputPath: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineMetadataIndividualDocumentStatus(
    typing.TypedDict, total=False
):
    documentId: str
    status: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineMetadataProcessWithDocAiPipelineMetadata(
    typing.TypedDict, total=False
):
    documents: _list[str]
    processorInfo: GoogleCloudContentwarehouseV1ProcessorInfo

@typing.type_check_only
class GoogleCloudContentwarehouseV1RunPipelineRequest(typing.TypedDict, total=False):
    exportCdwPipeline: GoogleCloudContentwarehouseV1ExportToCdwPipeline
    gcsIngestPipeline: GoogleCloudContentwarehouseV1GcsIngestPipeline
    gcsIngestWithDocAiProcessorsPipeline: (
        GoogleCloudContentwarehouseV1GcsIngestWithDocAiProcessorsPipeline
    )
    processWithDocAiPipeline: GoogleCloudContentwarehouseV1ProcessWithDocAiPipeline
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1SearchDocumentsRequest(
    typing.TypedDict, total=False
):
    documentQuery: GoogleCloudContentwarehouseV1DocumentQuery
    histogramQueries: _list[GoogleCloudContentwarehouseV1HistogramQuery]
    offset: int
    orderBy: str
    pageSize: int
    pageToken: str
    qaSizeLimit: int
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata
    requireTotalSize: bool
    totalResultSize: typing.Literal[
        "TOTAL_RESULT_SIZE_UNSPECIFIED", "ESTIMATED_SIZE", "ACTUAL_SIZE"
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1SearchDocumentsResponse(
    typing.TypedDict, total=False
):
    histogramQueryResults: _list[GoogleCloudContentwarehouseV1HistogramQueryResult]
    matchingDocuments: _list[
        GoogleCloudContentwarehouseV1SearchDocumentsResponseMatchingDocument
    ]
    metadata: GoogleCloudContentwarehouseV1ResponseMetadata
    nextPageToken: str
    questionAnswer: str
    totalSize: int

@typing.type_check_only
class GoogleCloudContentwarehouseV1SearchDocumentsResponseMatchingDocument(
    typing.TypedDict, total=False
):
    document: GoogleCloudContentwarehouseV1Document
    matchedTokenPageIndices: _list[str]
    qaResult: GoogleCloudContentwarehouseV1QAResult
    searchTextSnippet: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1SetAclRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    projectOwner: bool
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata

@typing.type_check_only
class GoogleCloudContentwarehouseV1SetAclResponse(typing.TypedDict, total=False):
    metadata: GoogleCloudContentwarehouseV1ResponseMetadata
    policy: GoogleIamV1Policy

@typing.type_check_only
class GoogleCloudContentwarehouseV1SynonymSet(typing.TypedDict, total=False):
    context: str
    name: str
    synonyms: _list[GoogleCloudContentwarehouseV1SynonymSetSynonym]

@typing.type_check_only
class GoogleCloudContentwarehouseV1SynonymSetSynonym(typing.TypedDict, total=False):
    words: _list[str]

@typing.type_check_only
class GoogleCloudContentwarehouseV1TextArray(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudContentwarehouseV1TextTypeOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1TimeFilter(typing.TypedDict, total=False):
    timeField: typing.Literal[
        "TIME_FIELD_UNSPECIFIED", "CREATE_TIME", "UPDATE_TIME", "DISPOSITION_TIME"
    ]
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudContentwarehouseV1TimestampArray(typing.TypedDict, total=False):
    values: _list[GoogleCloudContentwarehouseV1TimestampValue]

@typing.type_check_only
class GoogleCloudContentwarehouseV1TimestampTypeOptions(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1TimestampValue(typing.TypedDict, total=False):
    textValue: str
    timestampValue: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateDocumentMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateDocumentRequest(typing.TypedDict, total=False):
    cloudAiDocumentOption: GoogleCloudContentwarehouseV1CloudAIDocumentOption
    document: GoogleCloudContentwarehouseV1Document
    requestMetadata: GoogleCloudContentwarehouseV1RequestMetadata
    updateOptions: GoogleCloudContentwarehouseV1UpdateOptions

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateDocumentResponse(
    typing.TypedDict, total=False
):
    document: GoogleCloudContentwarehouseV1Document
    metadata: GoogleCloudContentwarehouseV1ResponseMetadata
    ruleEngineOutput: GoogleCloudContentwarehouseV1RuleEngineOutput

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateDocumentSchemaRequest(
    typing.TypedDict, total=False
):
    documentSchema: GoogleCloudContentwarehouseV1DocumentSchema

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateOptions(typing.TypedDict, total=False):
    mergeFieldsOptions: GoogleCloudContentwarehouseV1MergeFieldsOptions
    updateMask: str
    updateType: typing.Literal[
        "UPDATE_TYPE_UNSPECIFIED",
        "UPDATE_TYPE_REPLACE",
        "UPDATE_TYPE_MERGE",
        "UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES",
        "UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES",
        "UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES",
        "UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES",
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1UpdateRuleSetRequest(typing.TypedDict, total=False):
    ruleSet: GoogleCloudContentwarehouseV1RuleSet

@typing.type_check_only
class GoogleCloudContentwarehouseV1UserInfo(typing.TypedDict, total=False):
    groupIds: _list[str]
    id: str

@typing.type_check_only
class GoogleCloudContentwarehouseV1Value(typing.TypedDict, total=False):
    booleanValue: bool
    datetimeValue: GoogleTypeDateTime
    enumValue: GoogleCloudContentwarehouseV1EnumValue
    floatValue: float
    intValue: int
    stringValue: str
    timestampValue: GoogleCloudContentwarehouseV1TimestampValue

@typing.type_check_only
class GoogleCloudContentwarehouseV1WeightedSchemaProperty(
    typing.TypedDict, total=False
):
    documentSchemaName: str
    propertyNames: _list[str]

@typing.type_check_only
class GoogleCloudContentwarehouseV1beta1CreateDocumentMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudContentwarehouseV1beta1InitializeProjectResponse(
    typing.TypedDict, total=False
):
    message: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "CANCELLED", "RUNNING"
    ]

@typing.type_check_only
class GoogleCloudContentwarehouseV1beta1UpdateDocumentMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDocumentaiV1Barcode(typing.TypedDict, total=False):
    format: str
    rawValue: str
    valueFormat: str

@typing.type_check_only
class GoogleCloudDocumentaiV1BoundingPoly(typing.TypedDict, total=False):
    normalizedVertices: _list[GoogleCloudDocumentaiV1NormalizedVertex]
    vertices: _list[GoogleCloudDocumentaiV1Vertex]

@typing.type_check_only
class GoogleCloudDocumentaiV1Document(typing.TypedDict, total=False):
    chunkedDocument: GoogleCloudDocumentaiV1DocumentChunkedDocument
    content: str
    documentLayout: GoogleCloudDocumentaiV1DocumentDocumentLayout
    entities: _list[GoogleCloudDocumentaiV1DocumentEntity]
    entityRelations: _list[GoogleCloudDocumentaiV1DocumentEntityRelation]
    error: GoogleRpcStatus
    mimeType: str
    pages: _list[GoogleCloudDocumentaiV1DocumentPage]
    revisions: _list[GoogleCloudDocumentaiV1DocumentRevision]
    shardInfo: GoogleCloudDocumentaiV1DocumentShardInfo
    text: str
    textChanges: _list[GoogleCloudDocumentaiV1DocumentTextChange]
    textStyles: _list[GoogleCloudDocumentaiV1DocumentStyle]
    uri: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentChunkedDocument(typing.TypedDict, total=False):
    chunks: _list[GoogleCloudDocumentaiV1DocumentChunkedDocumentChunk]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentChunkedDocumentChunk(
    typing.TypedDict, total=False
):
    chunkId: str
    content: str
    pageFooters: _list[
        GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageFooter
    ]
    pageHeaders: _list[
        GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageHeader
    ]
    pageSpan: GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageSpan
    sourceBlockIds: _list[str]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageFooter(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageHeader(
    typing.TypedDict, total=False
):
    pageSpan: GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageSpan
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentChunkedDocumentChunkChunkPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayout(typing.TypedDict, total=False):
    blocks: _list[GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlock(
    typing.TypedDict, total=False
):
    blockId: str
    listBlock: (
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock
    )
    pageSpan: (
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan
    )
    tableBlock: (
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock
    )
    textBlock: (
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock
    )

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutListBlock(
    typing.TypedDict, total=False
):
    listEntries: _list[
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry
    ]
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutListEntry(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlock]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutPageSpan(
    typing.TypedDict, total=False
):
    pageEnd: int
    pageStart: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableBlock(
    typing.TypedDict, total=False
):
    bodyRows: _list[
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]
    caption: str
    headerRows: _list[
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlock]
    colSpan: int
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableRow(
    typing.TypedDict, total=False
):
    cells: _list[
        GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTableCell
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlockLayoutTextBlock(
    typing.TypedDict, total=False
):
    blocks: _list[GoogleCloudDocumentaiV1DocumentDocumentLayoutDocumentLayoutBlock]
    text: str
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentEntity(typing.TypedDict, total=False):
    confidence: float
    id: str
    mentionId: str
    mentionText: str
    normalizedValue: GoogleCloudDocumentaiV1DocumentEntityNormalizedValue
    pageAnchor: GoogleCloudDocumentaiV1DocumentPageAnchor
    properties: _list[GoogleCloudDocumentaiV1DocumentEntity]
    provenance: GoogleCloudDocumentaiV1DocumentProvenance
    redacted: bool
    textAnchor: GoogleCloudDocumentaiV1DocumentTextAnchor
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentEntityNormalizedValue(
    typing.TypedDict, total=False
):
    addressValue: GoogleTypePostalAddress
    booleanValue: bool
    dateValue: GoogleTypeDate
    datetimeValue: GoogleTypeDateTime
    floatValue: float
    integerValue: int
    moneyValue: GoogleTypeMoney
    text: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentEntityRelation(typing.TypedDict, total=False):
    objectId: str
    relation: str
    subjectId: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPage(typing.TypedDict, total=False):
    blocks: _list[GoogleCloudDocumentaiV1DocumentPageBlock]
    detectedBarcodes: _list[GoogleCloudDocumentaiV1DocumentPageDetectedBarcode]
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    dimension: GoogleCloudDocumentaiV1DocumentPageDimension
    formFields: _list[GoogleCloudDocumentaiV1DocumentPageFormField]
    image: GoogleCloudDocumentaiV1DocumentPageImage
    imageQualityScores: GoogleCloudDocumentaiV1DocumentPageImageQualityScores
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    lines: _list[GoogleCloudDocumentaiV1DocumentPageLine]
    pageNumber: int
    paragraphs: _list[GoogleCloudDocumentaiV1DocumentPageParagraph]
    provenance: GoogleCloudDocumentaiV1DocumentProvenance
    symbols: _list[GoogleCloudDocumentaiV1DocumentPageSymbol]
    tables: _list[GoogleCloudDocumentaiV1DocumentPageTable]
    tokens: _list[GoogleCloudDocumentaiV1DocumentPageToken]
    transforms: _list[GoogleCloudDocumentaiV1DocumentPageMatrix]
    visualElements: _list[GoogleCloudDocumentaiV1DocumentPageVisualElement]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageAnchor(typing.TypedDict, total=False):
    pageRefs: _list[GoogleCloudDocumentaiV1DocumentPageAnchorPageRef]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageAnchorPageRef(typing.TypedDict, total=False):
    boundingPoly: GoogleCloudDocumentaiV1BoundingPoly
    confidence: float
    layoutId: str
    layoutType: typing.Literal[
        "LAYOUT_TYPE_UNSPECIFIED",
        "BLOCK",
        "PARAGRAPH",
        "LINE",
        "TOKEN",
        "VISUAL_ELEMENT",
        "TABLE",
        "FORM_FIELD",
    ]
    page: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageBlock(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageDetectedBarcode(typing.TypedDict, total=False):
    barcode: GoogleCloudDocumentaiV1Barcode
    layout: GoogleCloudDocumentaiV1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageDetectedLanguage(
    typing.TypedDict, total=False
):
    confidence: float
    languageCode: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageDimension(typing.TypedDict, total=False):
    height: float
    unit: str
    width: float

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageFormField(typing.TypedDict, total=False):
    correctedKeyText: str
    correctedValueText: str
    fieldName: GoogleCloudDocumentaiV1DocumentPageLayout
    fieldValue: GoogleCloudDocumentaiV1DocumentPageLayout
    nameDetectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    provenance: GoogleCloudDocumentaiV1DocumentProvenance
    valueDetectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    valueType: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageImage(typing.TypedDict, total=False):
    content: str
    height: int
    mimeType: str
    width: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageImageQualityScores(
    typing.TypedDict, total=False
):
    detectedDefects: _list[
        GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefect
    ]
    qualityScore: float

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageImageQualityScoresDetectedDefect(
    typing.TypedDict, total=False
):
    confidence: float
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageLayout(typing.TypedDict, total=False):
    boundingPoly: GoogleCloudDocumentaiV1BoundingPoly
    confidence: float
    orientation: typing.Literal[
        "ORIENTATION_UNSPECIFIED", "PAGE_UP", "PAGE_RIGHT", "PAGE_DOWN", "PAGE_LEFT"
    ]
    textAnchor: GoogleCloudDocumentaiV1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageLine(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageMatrix(typing.TypedDict, total=False):
    cols: int
    data: str
    rows: int
    type: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageParagraph(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageSymbol(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageTable(typing.TypedDict, total=False):
    bodyRows: _list[GoogleCloudDocumentaiV1DocumentPageTableTableRow]
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    headerRows: _list[GoogleCloudDocumentaiV1DocumentPageTableTableRow]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1DocumentProvenance

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageTableTableCell(typing.TypedDict, total=False):
    colSpan: int
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    rowSpan: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageTableTableRow(typing.TypedDict, total=False):
    cells: _list[GoogleCloudDocumentaiV1DocumentPageTableTableCell]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageToken(typing.TypedDict, total=False):
    detectedBreak: GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreak
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    provenance: GoogleCloudDocumentaiV1DocumentProvenance
    styleInfo: GoogleCloudDocumentaiV1DocumentPageTokenStyleInfo

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageTokenDetectedBreak(
    typing.TypedDict, total=False
):
    type: typing.Literal["TYPE_UNSPECIFIED", "SPACE", "WIDE_SPACE", "HYPHEN"]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageTokenStyleInfo(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    bold: bool
    fontSize: int
    fontType: str
    fontWeight: int
    handwritten: bool
    italic: bool
    letterSpacing: float
    pixelFontSize: float
    smallcaps: bool
    strikeout: bool
    subscript: bool
    superscript: bool
    textColor: GoogleTypeColor
    underlined: bool

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentPageVisualElement(typing.TypedDict, total=False):
    detectedLanguages: _list[GoogleCloudDocumentaiV1DocumentPageDetectedLanguage]
    layout: GoogleCloudDocumentaiV1DocumentPageLayout
    type: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentProvenance(typing.TypedDict, total=False):
    id: int
    parents: _list[GoogleCloudDocumentaiV1DocumentProvenanceParent]
    revision: int
    type: typing.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "ADD",
        "REMOVE",
        "UPDATE",
        "REPLACE",
        "EVAL_REQUESTED",
        "EVAL_APPROVED",
        "EVAL_SKIPPED",
    ]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentProvenanceParent(typing.TypedDict, total=False):
    id: int
    index: int
    revision: int

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentRevision(typing.TypedDict, total=False):
    agent: str
    createTime: str
    humanReview: GoogleCloudDocumentaiV1DocumentRevisionHumanReview
    id: str
    parent: _list[int]
    parentIds: _list[str]
    processor: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentRevisionHumanReview(typing.TypedDict, total=False):
    state: str
    stateMessage: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentShardInfo(typing.TypedDict, total=False):
    shardCount: str
    shardIndex: str
    textOffset: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentStyle(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    color: GoogleTypeColor
    fontFamily: str
    fontSize: GoogleCloudDocumentaiV1DocumentStyleFontSize
    fontWeight: str
    textAnchor: GoogleCloudDocumentaiV1DocumentTextAnchor
    textDecoration: str
    textStyle: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentStyleFontSize(typing.TypedDict, total=False):
    size: float
    unit: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentTextAnchor(typing.TypedDict, total=False):
    content: str
    textSegments: _list[GoogleCloudDocumentaiV1DocumentTextAnchorTextSegment]

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentTextAnchorTextSegment(
    typing.TypedDict, total=False
):
    endIndex: str
    startIndex: str

@typing.type_check_only
class GoogleCloudDocumentaiV1DocumentTextChange(typing.TypedDict, total=False):
    changedText: str
    provenance: _list[GoogleCloudDocumentaiV1DocumentProvenance]
    textAnchor: GoogleCloudDocumentaiV1DocumentTextAnchor

@typing.type_check_only
class GoogleCloudDocumentaiV1NormalizedVertex(typing.TypedDict, total=False):
    x: float
    y: float

@typing.type_check_only
class GoogleCloudDocumentaiV1Vertex(typing.TypedDict, total=False):
    x: int
    y: int

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
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeColor(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeDateTime(typing.TypedDict, total=False):
    day: int
    hours: int
    minutes: int
    month: int
    nanos: int
    seconds: int
    timeZone: GoogleTypeTimeZone
    utcOffset: str
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleTypeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleTypeMoney(typing.TypedDict, total=False):
    currencyCode: str
    nanos: int
    units: str

@typing.type_check_only
class GoogleTypePostalAddress(typing.TypedDict, total=False):
    addressLines: _list[str]
    administrativeArea: str
    languageCode: str
    locality: str
    organization: str
    postalCode: str
    recipients: _list[str]
    regionCode: str
    revision: int
    sortingCode: str
    sublocality: str

@typing.type_check_only
class GoogleTypeTimeZone(typing.TypedDict, total=False):
    id: str
    version: str
