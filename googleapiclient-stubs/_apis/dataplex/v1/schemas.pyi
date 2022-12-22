import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudDataplexV1Action(typing_extensions.TypedDict, total=False):
    asset: str
    category: typing_extensions.Literal[
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
    typing_extensions.TypedDict, total=False
):
    asset: str

@typing.type_check_only
class GoogleCloudDataplexV1ActionIncompatibleDataSchema(
    typing_extensions.TypedDict, total=False
):
    existingSchema: str
    newSchema: str
    sampledDataLocations: _list[str]
    schemaChange: typing_extensions.Literal[
        "SCHEMA_CHANGE_UNSPECIFIED", "INCOMPATIBLE", "MODIFIED"
    ]
    table: str

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataFormat(
    typing_extensions.TypedDict, total=False
):
    expectedFormat: str
    newFormat: str
    sampledDataLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataOrganization(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionInvalidDataPartition(
    typing_extensions.TypedDict, total=False
):
    expectedStructure: typing_extensions.Literal[
        "PARTITION_STRUCTURE_UNSPECIFIED", "CONSISTENT_KEYS", "HIVE_STYLE_KEYS"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1ActionMissingData(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionMissingResource(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1ActionUnauthorizedResource(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1Asset(typing_extensions.TypedDict, total=False):
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
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpec(typing_extensions.TypedDict, total=False):
    csvOptions: GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions
    enabled: bool
    excludePatterns: _list[str]
    includePatterns: _list[str]
    jsonOptions: GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions
    schedule: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpecCsvOptions(
    typing_extensions.TypedDict, total=False
):
    delimiter: str
    disableTypeInference: bool
    encoding: str
    headerRows: int

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoverySpecJsonOptions(
    typing_extensions.TypedDict, total=False
):
    disableTypeInference: bool
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoveryStatus(
    typing_extensions.TypedDict, total=False
):
    lastRunDuration: str
    lastRunTime: str
    message: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SCHEDULED", "IN_PROGRESS", "PAUSED", "DISABLED"
    ]
    stats: GoogleCloudDataplexV1AssetDiscoveryStatusStats
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetDiscoveryStatusStats(
    typing_extensions.TypedDict, total=False
):
    dataItems: str
    dataSize: str
    filesets: str
    tables: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetResourceSpec(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "STORAGE_BUCKET", "BIGQUERY_DATASET"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1AssetResourceStatus(
    typing_extensions.TypedDict, total=False
):
    message: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "READY", "ERROR"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetSecurityStatus(
    typing_extensions.TypedDict, total=False
):
    message: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "READY", "APPLYING", "ERROR"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1AssetStatus(typing_extensions.TypedDict, total=False):
    activeAssets: int
    securityPolicyApplyingAssets: int
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1CancelJobRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1Content(typing_extensions.TypedDict, total=False):
    createTime: str
    dataText: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    notebook: GoogleCloudDataplexV1ContentNotebook
    path: str
    sqlScript: GoogleCloudDataplexV1ContentSqlScript
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ContentNotebook(typing_extensions.TypedDict, total=False):
    kernelType: typing_extensions.Literal["KERNEL_TYPE_UNSPECIFIED", "PYTHON3"]

@typing.type_check_only
class GoogleCloudDataplexV1ContentSqlScript(typing_extensions.TypedDict, total=False):
    engine: typing_extensions.Literal["QUERY_ENGINE_UNSPECIFIED", "SPARK"]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResult(typing_extensions.TypedDict, total=False):
    profile: GoogleCloudDataplexV1DataProfileResultProfile
    rowCount: str
    scannedData: GoogleCloudDataplexV1ScannedData

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfile(
    typing_extensions.TypedDict, total=False
):
    fields: _list[GoogleCloudDataplexV1DataProfileResultProfileField]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileField(
    typing_extensions.TypedDict, total=False
):
    mode: str
    name: str
    profile: GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfo(
    typing_extensions.TypedDict, total=False
):
    distinctRatio: float
    doubleProfile: GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo
    integerProfile: GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo
    nullRatio: float
    stringProfile: GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo
    topNValues: _list[
        GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoDoubleFieldInfo(
    typing_extensions.TypedDict, total=False
):
    average: float
    max: float
    min: float
    quartiles: _list[float]
    standardDeviation: float

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoIntegerFieldInfo(
    typing_extensions.TypedDict, total=False
):
    average: float
    max: str
    min: str
    quartiles: _list[str]
    standardDeviation: float

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoStringFieldInfo(
    typing_extensions.TypedDict, total=False
):
    averageLength: float
    maxLength: str
    minLength: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileResultProfileFieldProfileInfoTopNValue(
    typing_extensions.TypedDict, total=False
):
    count: str
    value: str

@typing.type_check_only
class GoogleCloudDataplexV1DataProfileSpec(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityDimensionResult(
    typing_extensions.TypedDict, total=False
):
    passed: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityResult(typing_extensions.TypedDict, total=False):
    dimensions: _list[GoogleCloudDataplexV1DataQualityDimensionResult]
    passed: bool
    rowCount: str
    rules: _list[GoogleCloudDataplexV1DataQualityRuleResult]
    scannedData: GoogleCloudDataplexV1ScannedData

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRule(typing_extensions.TypedDict, total=False):
    column: str
    dimension: str
    ignoreNull: bool
    nonNullExpectation: GoogleCloudDataplexV1DataQualityRuleNonNullExpectation
    rangeExpectation: GoogleCloudDataplexV1DataQualityRuleRangeExpectation
    regexExpectation: GoogleCloudDataplexV1DataQualityRuleRegexExpectation
    rowConditionExpectation: GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation
    setExpectation: GoogleCloudDataplexV1DataQualityRuleSetExpectation
    statisticRangeExpectation: GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation
    tableConditionExpectation: GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation
    threshold: float
    uniquenessExpectation: GoogleCloudDataplexV1DataQualityRuleUniquenessExpectation

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleNonNullExpectation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRangeExpectation(
    typing_extensions.TypedDict, total=False
):
    maxValue: str
    minValue: str
    strictMaxEnabled: bool
    strictMinEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRegexExpectation(
    typing_extensions.TypedDict, total=False
):
    regex: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleResult(
    typing_extensions.TypedDict, total=False
):
    evaluatedCount: str
    failingRowsQuery: str
    nullCount: str
    passRatio: float
    passed: bool
    passedCount: str
    rule: GoogleCloudDataplexV1DataQualityRule

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleRowConditionExpectation(
    typing_extensions.TypedDict, total=False
):
    sqlExpression: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleSetExpectation(
    typing_extensions.TypedDict, total=False
):
    values: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleStatisticRangeExpectation(
    typing_extensions.TypedDict, total=False
):
    maxValue: str
    minValue: str
    statistic: typing_extensions.Literal["STATISTIC_UNDEFINED", "MEAN", "MIN", "MAX"]
    strictMaxEnabled: bool
    strictMinEnabled: bool

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleTableConditionExpectation(
    typing_extensions.TypedDict, total=False
):
    sqlExpression: str

@typing.type_check_only
class GoogleCloudDataplexV1DataQualityRuleUniquenessExpectation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1DataQualitySpec(typing_extensions.TypedDict, total=False):
    rules: _list[GoogleCloudDataplexV1DataQualityRule]

@typing.type_check_only
class GoogleCloudDataplexV1DataScan(typing_extensions.TypedDict, total=False):
    createTime: str
    data: GoogleCloudDataplexV1DataSource
    dataProfileResult: GoogleCloudDataplexV1DataProfileResult
    dataProfileSpec: GoogleCloudDataplexV1DataProfileSpec
    dataQualityResult: GoogleCloudDataplexV1DataQualityResult
    dataQualitySpec: GoogleCloudDataplexV1DataQualitySpec
    description: str
    displayName: str
    executionSpec: GoogleCloudDataplexV1DataScanExecutionSpec
    executionStatus: GoogleCloudDataplexV1DataScanExecutionStatus
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    type: typing_extensions.Literal[
        "DATA_SCAN_TYPE_UNSPECIFIED", "DATA_QUALITY", "DATA_PROFILE"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEvent(typing_extensions.TypedDict, total=False):
    dataProfile: GoogleCloudDataplexV1DataScanEventDataProfileResult
    dataQuality: GoogleCloudDataplexV1DataScanEventDataQualityResult
    dataSource: str
    endTime: str
    jobId: str
    message: str
    scope: typing_extensions.Literal["SCOPE_UNSPECIFIED", "FULL", "INCREMENTAL"]
    specVersion: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STARTED", "SUCCEEDED", "FAILED", "CANCELLED"
    ]
    trigger: typing_extensions.Literal["TRIGGER_UNSPECIFIED", "ON_DEMAND", "SCHEDULE"]
    type: typing_extensions.Literal[
        "SCAN_TYPE_UNSPECIFIED", "DATA_PROFILE", "DATA_QUALITY"
    ]

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataProfileResult(
    typing_extensions.TypedDict, total=False
):
    rowCount: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanEventDataQualityResult(
    typing_extensions.TypedDict, total=False
):
    dimensionPassed: dict[str, typing.Any]
    passed: bool
    rowCount: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanExecutionSpec(
    typing_extensions.TypedDict, total=False
):
    field: str
    trigger: GoogleCloudDataplexV1Trigger

@typing.type_check_only
class GoogleCloudDataplexV1DataScanExecutionStatus(
    typing_extensions.TypedDict, total=False
):
    latestJobEndTime: str
    latestJobStartTime: str

@typing.type_check_only
class GoogleCloudDataplexV1DataScanJob(typing_extensions.TypedDict, total=False):
    dataProfileResult: GoogleCloudDataplexV1DataProfileResult
    dataProfileSpec: GoogleCloudDataplexV1DataProfileSpec
    dataQualityResult: GoogleCloudDataplexV1DataQualityResult
    dataQualitySpec: GoogleCloudDataplexV1DataQualitySpec
    endTime: str
    message: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "CANCELING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
        "PENDING",
    ]
    type: typing_extensions.Literal[
        "DATA_SCAN_TYPE_UNSPECIFIED", "DATA_QUALITY", "DATA_PROFILE"
    ]
    uid: str

@typing.type_check_only
class GoogleCloudDataplexV1DataSource(typing_extensions.TypedDict, total=False):
    entity: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEvent(typing_extensions.TypedDict, total=False):
    action: GoogleCloudDataplexV1DiscoveryEventActionDetails
    assetId: str
    config: GoogleCloudDataplexV1DiscoveryEventConfigDetails
    dataLocation: str
    entity: GoogleCloudDataplexV1DiscoveryEventEntityDetails
    lakeId: str
    message: str
    partition: GoogleCloudDataplexV1DiscoveryEventPartitionDetails
    type: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED",
        "CONFIG",
        "ENTITY_CREATED",
        "ENTITY_UPDATED",
        "ENTITY_DELETED",
        "PARTITION_CREATED",
        "PARTITION_UPDATED",
        "PARTITION_DELETED",
    ]
    zoneId: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventActionDetails(
    typing_extensions.TypedDict, total=False
):
    type: str

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventConfigDetails(
    typing_extensions.TypedDict, total=False
):
    parameters: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventEntityDetails(
    typing_extensions.TypedDict, total=False
):
    entity: str
    type: typing_extensions.Literal["ENTITY_TYPE_UNSPECIFIED", "TABLE", "FILESET"]

@typing.type_check_only
class GoogleCloudDataplexV1DiscoveryEventPartitionDetails(
    typing_extensions.TypedDict, total=False
):
    entity: str
    partition: str
    sampledDataLocations: _list[str]
    type: typing_extensions.Literal["ENTITY_TYPE_UNSPECIFIED", "TABLE", "FILESET"]

@typing.type_check_only
class GoogleCloudDataplexV1Entity(typing_extensions.TypedDict, total=False):
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
    system: typing_extensions.Literal[
        "STORAGE_SYSTEM_UNSPECIFIED", "CLOUD_STORAGE", "BIGQUERY"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TABLE", "FILESET"]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EntityCompatibilityStatus(
    typing_extensions.TypedDict, total=False
):
    bigquery: GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility
    hiveMetastore: GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility

@typing.type_check_only
class GoogleCloudDataplexV1EntityCompatibilityStatusCompatibility(
    typing_extensions.TypedDict, total=False
):
    compatible: bool
    reason: str

@typing.type_check_only
class GoogleCloudDataplexV1Environment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    endpoints: GoogleCloudDataplexV1EnvironmentEndpoints
    infrastructureSpec: GoogleCloudDataplexV1EnvironmentInfrastructureSpec
    labels: dict[str, typing.Any]
    name: str
    sessionSpec: GoogleCloudDataplexV1EnvironmentSessionSpec
    sessionStatus: GoogleCloudDataplexV1EnvironmentSessionStatus
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentEndpoints(
    typing_extensions.TypedDict, total=False
):
    notebooks: str
    sql: str

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentInfrastructureSpec(
    typing_extensions.TypedDict, total=False
):
    compute: GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResources
    osImage: GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntime

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentInfrastructureSpecComputeResources(
    typing_extensions.TypedDict, total=False
):
    diskSizeGb: int
    maxNodeCount: int
    nodeCount: int

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentInfrastructureSpecOsImageRuntime(
    typing_extensions.TypedDict, total=False
):
    imageVersion: str
    javaLibraries: _list[str]
    properties: dict[str, typing.Any]
    pythonPackages: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentSessionSpec(
    typing_extensions.TypedDict, total=False
):
    enableFastStartup: bool
    maxIdleDuration: str

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentSessionStatus(
    typing_extensions.TypedDict, total=False
):
    active: bool

@typing.type_check_only
class GoogleCloudDataplexV1Job(typing_extensions.TypedDict, total=False):
    endTime: str
    message: str
    name: str
    retryCount: int
    service: typing_extensions.Literal["SERVICE_UNSPECIFIED", "DATAPROC"]
    serviceJob: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "RUNNING",
        "CANCELLING",
        "CANCELLED",
        "SUCCEEDED",
        "FAILED",
        "ABORTED",
    ]
    uid: str

@typing.type_check_only
class GoogleCloudDataplexV1JobEvent(typing_extensions.TypedDict, total=False):
    endTime: str
    jobId: str
    message: str
    retries: int
    service: typing_extensions.Literal["SERVICE_UNSPECIFIED", "DATAPROC"]
    serviceJob: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "CANCELLED", "ABORTED"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "SPARK", "NOTEBOOK"]

@typing.type_check_only
class GoogleCloudDataplexV1Lake(typing_extensions.TypedDict, total=False):
    assetStatus: GoogleCloudDataplexV1AssetStatus
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    metastore: GoogleCloudDataplexV1LakeMetastore
    metastoreStatus: GoogleCloudDataplexV1LakeMetastoreStatus
    name: str
    serviceAccount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1LakeMetastore(typing_extensions.TypedDict, total=False):
    service: str

@typing.type_check_only
class GoogleCloudDataplexV1LakeMetastoreStatus(
    typing_extensions.TypedDict, total=False
):
    endpoint: str
    message: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "NONE", "READY", "UPDATING", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ListActionsResponse(
    typing_extensions.TypedDict, total=False
):
    actions: _list[GoogleCloudDataplexV1Action]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[GoogleCloudDataplexV1Asset]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListContentResponse(
    typing_extensions.TypedDict, total=False
):
    content: _list[GoogleCloudDataplexV1Content]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScanJobsResponse(
    typing_extensions.TypedDict, total=False
):
    dataScanJobs: _list[GoogleCloudDataplexV1DataScanJob]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListDataScansResponse(
    typing_extensions.TypedDict, total=False
):
    dataScans: _list[GoogleCloudDataplexV1DataScan]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDataplexV1Entity]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListEnvironmentsResponse(
    typing_extensions.TypedDict, total=False
):
    environments: _list[GoogleCloudDataplexV1Environment]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[GoogleCloudDataplexV1Job]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDataplexV1ListLakesResponse(typing_extensions.TypedDict, total=False):
    lakes: _list[GoogleCloudDataplexV1Lake]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListPartitionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    partitions: _list[GoogleCloudDataplexV1Partition]

@typing.type_check_only
class GoogleCloudDataplexV1ListSessionsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    sessions: _list[GoogleCloudDataplexV1Session]

@typing.type_check_only
class GoogleCloudDataplexV1ListTasksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tasks: _list[GoogleCloudDataplexV1Task]
    unreachableLocations: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1ListZonesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    zones: _list[GoogleCloudDataplexV1Zone]

@typing.type_check_only
class GoogleCloudDataplexV1OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudDataplexV1Partition(typing_extensions.TypedDict, total=False):
    etag: str
    location: str
    name: str
    values: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1RunDataScanRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1RunDataScanResponse(
    typing_extensions.TypedDict, total=False
):
    job: GoogleCloudDataplexV1DataScanJob

@typing.type_check_only
class GoogleCloudDataplexV1ScannedData(typing_extensions.TypedDict, total=False):
    incrementalField: GoogleCloudDataplexV1ScannedDataIncrementalField

@typing.type_check_only
class GoogleCloudDataplexV1ScannedDataIncrementalField(
    typing_extensions.TypedDict, total=False
):
    end: str
    field: str
    start: str

@typing.type_check_only
class GoogleCloudDataplexV1Schema(typing_extensions.TypedDict, total=False):
    fields: _list[GoogleCloudDataplexV1SchemaSchemaField]
    partitionFields: _list[GoogleCloudDataplexV1SchemaPartitionField]
    partitionStyle: typing_extensions.Literal[
        "PARTITION_STYLE_UNSPECIFIED", "HIVE_COMPATIBLE"
    ]
    userManaged: bool

@typing.type_check_only
class GoogleCloudDataplexV1SchemaPartitionField(
    typing_extensions.TypedDict, total=False
):
    name: str
    type: typing_extensions.Literal[
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
class GoogleCloudDataplexV1SchemaSchemaField(typing_extensions.TypedDict, total=False):
    description: str
    fields: _list[GoogleCloudDataplexV1SchemaSchemaField]
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "REQUIRED", "NULLABLE", "REPEATED"
    ]
    name: str
    type: typing_extensions.Literal[
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
class GoogleCloudDataplexV1Session(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    userId: str

@typing.type_check_only
class GoogleCloudDataplexV1SessionEvent(typing_extensions.TypedDict, total=False):
    eventSucceeded: bool
    fastStartupEnabled: bool
    message: str
    query: GoogleCloudDataplexV1SessionEventQueryDetail
    sessionId: str
    type: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "START", "STOP", "QUERY", "CREATE"
    ]
    unassignedDuration: str
    userId: str

@typing.type_check_only
class GoogleCloudDataplexV1SessionEventQueryDetail(
    typing_extensions.TypedDict, total=False
):
    dataProcessedBytes: str
    duration: str
    engine: typing_extensions.Literal["ENGINE_UNSPECIFIED", "SPARK_SQL", "BIGQUERY"]
    queryId: str
    queryText: str
    resultSizeBytes: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormat(typing_extensions.TypedDict, total=False):
    compressionFormat: typing_extensions.Literal[
        "COMPRESSION_FORMAT_UNSPECIFIED", "GZIP", "BZIP2"
    ]
    csv: GoogleCloudDataplexV1StorageFormatCsvOptions
    format: typing_extensions.Literal[
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
class GoogleCloudDataplexV1StorageFormatCsvOptions(
    typing_extensions.TypedDict, total=False
):
    delimiter: str
    encoding: str
    headerRows: int
    quote: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormatIcebergOptions(
    typing_extensions.TypedDict, total=False
):
    metadataLocation: str

@typing.type_check_only
class GoogleCloudDataplexV1StorageFormatJsonOptions(
    typing_extensions.TypedDict, total=False
):
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1Task(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    executionSpec: GoogleCloudDataplexV1TaskExecutionSpec
    executionStatus: GoogleCloudDataplexV1TaskExecutionStatus
    labels: dict[str, typing.Any]
    name: str
    notebook: GoogleCloudDataplexV1TaskNotebookTaskConfig
    spark: GoogleCloudDataplexV1TaskSparkTaskConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    triggerSpec: GoogleCloudDataplexV1TaskTriggerSpec
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskExecutionSpec(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    kmsKey: str
    maxJobExecutionLifetime: str
    project: str
    serviceAccount: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskExecutionStatus(
    typing_extensions.TypedDict, total=False
):
    latestJob: GoogleCloudDataplexV1Job
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpec(
    typing_extensions.TypedDict, total=False
):
    batch: GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResources
    containerImage: GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntime
    vpcNetwork: GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetwork

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResources(
    typing_extensions.TypedDict, total=False
):
    executorsCount: int
    maxExecutorsCount: int

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecContainerImageRuntime(
    typing_extensions.TypedDict, total=False
):
    image: str
    javaJars: _list[str]
    properties: dict[str, typing.Any]
    pythonPackages: _list[str]

@typing.type_check_only
class GoogleCloudDataplexV1TaskInfrastructureSpecVpcNetwork(
    typing_extensions.TypedDict, total=False
):
    network: str
    networkTags: _list[str]
    subNetwork: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskNotebookTaskConfig(
    typing_extensions.TypedDict, total=False
):
    archiveUris: _list[str]
    fileUris: _list[str]
    infrastructureSpec: GoogleCloudDataplexV1TaskInfrastructureSpec
    notebook: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskSparkTaskConfig(
    typing_extensions.TypedDict, total=False
):
    archiveUris: _list[str]
    fileUris: _list[str]
    infrastructureSpec: GoogleCloudDataplexV1TaskInfrastructureSpec
    mainClass: str
    mainJarFileUri: str
    pythonScriptFile: str
    sqlScript: str
    sqlScriptFile: str

@typing.type_check_only
class GoogleCloudDataplexV1TaskTriggerSpec(typing_extensions.TypedDict, total=False):
    disabled: bool
    maxRetries: int
    schedule: str
    startTime: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ON_DEMAND", "RECURRING"]

@typing.type_check_only
class GoogleCloudDataplexV1Trigger(typing_extensions.TypedDict, total=False):
    onDemand: GoogleCloudDataplexV1TriggerOnDemand
    schedule: GoogleCloudDataplexV1TriggerSchedule

@typing.type_check_only
class GoogleCloudDataplexV1TriggerOnDemand(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudDataplexV1TriggerSchedule(typing_extensions.TypedDict, total=False):
    cron: str

@typing.type_check_only
class GoogleCloudDataplexV1Zone(typing_extensions.TypedDict, total=False):
    assetStatus: GoogleCloudDataplexV1AssetStatus
    createTime: str
    description: str
    discoverySpec: GoogleCloudDataplexV1ZoneDiscoverySpec
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    resourceSpec: GoogleCloudDataplexV1ZoneResourceSpec
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "CREATING", "DELETING", "ACTION_REQUIRED"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "RAW", "CURATED"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpec(typing_extensions.TypedDict, total=False):
    csvOptions: GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions
    enabled: bool
    excludePatterns: _list[str]
    includePatterns: _list[str]
    jsonOptions: GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions
    schedule: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpecCsvOptions(
    typing_extensions.TypedDict, total=False
):
    delimiter: str
    disableTypeInference: bool
    encoding: str
    headerRows: int

@typing.type_check_only
class GoogleCloudDataplexV1ZoneDiscoverySpecJsonOptions(
    typing_extensions.TypedDict, total=False
):
    disableTypeInference: bool
    encoding: str

@typing.type_check_only
class GoogleCloudDataplexV1ZoneResourceSpec(typing_extensions.TypedDict, total=False):
    locationType: typing_extensions.Literal[
        "LOCATION_TYPE_UNSPECIFIED", "SINGLE_REGION", "MULTI_REGION"
    ]

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(
    typing_extensions.TypedDict, total=False
):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
