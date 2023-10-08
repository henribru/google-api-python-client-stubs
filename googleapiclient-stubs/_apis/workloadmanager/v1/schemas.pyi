import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Evaluation(typing_extensions.TypedDict, total=False):
    createTime: str
    customRulesBucket: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    resourceFilter: ResourceFilter
    resourceStatus: ResourceStatus
    ruleNames: _list[str]
    ruleVersions: _list[str]
    schedule: str
    updateTime: str

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    endTime: str
    evaluationId: str
    inventoryTime: str
    labels: dict[str, typing.Any]
    name: str
    runType: typing_extensions.Literal["TYPE_UNSPECIFIED", "ONE_TIME", "SCHEDULED"]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class ExecutionResult(typing_extensions.TypedDict, total=False):
    documentationUrl: str
    resource: Resource
    rule: str
    severity: str
    violationDetails: ViolationDetails
    violationMessage: str

@typing.type_check_only
class GceInstanceFilter(typing_extensions.TypedDict, total=False):
    serviceAccounts: _list[str]

@typing.type_check_only
class Insight(typing_extensions.TypedDict, total=False):
    instanceId: str
    sapDiscovery: SapDiscovery
    sapValidation: SapValidation
    sentTime: str
    sqlserverValidation: SqlserverValidation

@typing.type_check_only
class ListEvaluationsResponse(typing_extensions.TypedDict, total=False):
    evaluations: _list[Evaluation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionResultsResponse(typing_extensions.TypedDict, total=False):
    executionResults: _list[ExecutionResult]
    nextPageToken: str

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    executions: _list[Execution]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListRulesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rules: _list[Rule]

@typing.type_check_only
class ListScannedResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scannedResources: _list[ScannedResource]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    name: str
    serviceAccount: str
    type: str

@typing.type_check_only
class ResourceFilter(typing_extensions.TypedDict, total=False):
    gceInstanceFilter: GceInstanceFilter
    inclusionLabels: dict[str, typing.Any]
    resourceIdPatterns: _list[str]
    scopes: _list[str]

@typing.type_check_only
class ResourceStatus(typing_extensions.TypedDict, total=False):
    rulesNewerVersions: _list[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]

@typing.type_check_only
class Rule(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    errorMessage: str
    name: str
    primaryCategory: str
    remediation: str
    revisionId: str
    secondaryCategory: str
    severity: str
    uri: str

@typing.type_check_only
class RunEvaluationRequest(typing_extensions.TypedDict, total=False):
    execution: Execution
    executionId: str
    requestId: str

@typing.type_check_only
class SapDiscovery(typing_extensions.TypedDict, total=False):
    applicationLayer: SapDiscoveryComponent
    databaseLayer: SapDiscoveryComponent
    metadata: SapDiscoveryMetadata
    systemId: str
    updateTime: str

@typing.type_check_only
class SapDiscoveryComponent(typing_extensions.TypedDict, total=False):
    applicationProperties: SapDiscoveryComponentApplicationProperties
    databaseProperties: SapDiscoveryComponentDatabaseProperties
    hostProject: str
    resources: _list[SapDiscoveryResource]
    sid: str

@typing.type_check_only
class SapDiscoveryComponentApplicationProperties(
    typing_extensions.TypedDict, total=False
):
    applicationType: typing_extensions.Literal[
        "APPLICATION_TYPE_UNSPECIFIED", "NETWEAVER"
    ]
    ascsUri: str
    nfsUri: str

@typing.type_check_only
class SapDiscoveryComponentDatabaseProperties(typing_extensions.TypedDict, total=False):
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "HANA", "MAX_DB", "DB2"
    ]
    primaryInstanceUri: str
    sharedNfsUri: str

@typing.type_check_only
class SapDiscoveryMetadata(typing_extensions.TypedDict, total=False):
    customerRegion: str
    definedSystem: str
    environmentType: str
    sapProduct: str

@typing.type_check_only
class SapDiscoveryResource(typing_extensions.TypedDict, total=False):
    relatedResources: _list[str]
    resourceKind: typing_extensions.Literal[
        "RESOURCE_KIND_UNSPECIFIED",
        "RESOURCE_KIND_INSTANCE",
        "RESOURCE_KIND_DISK",
        "RESOURCE_KIND_ADDRESS",
        "RESOURCE_KIND_FILESTORE",
        "RESOURCE_KIND_HEALTH_CHECK",
        "RESOURCE_KIND_FORWARDING_RULE",
        "RESOURCE_KIND_BACKEND_SERVICE",
        "RESOURCE_KIND_SUBNETWORK",
        "RESOURCE_KIND_NETWORK",
        "RESOURCE_KIND_PUBLIC_ADDRESS",
        "RESOURCE_KIND_INSTANCE_GROUP",
    ]
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "RESOURCE_TYPE_COMPUTE",
        "RESOURCE_TYPE_STORAGE",
        "RESOURCE_TYPE_NETWORK",
    ]
    resourceUri: str
    updateTime: str

@typing.type_check_only
class SapValidation(typing_extensions.TypedDict, total=False):
    validationDetails: _list[SapValidationValidationDetail]

@typing.type_check_only
class SapValidationValidationDetail(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    sapValidationType: typing_extensions.Literal[
        "SAP_VALIDATION_TYPE_UNSPECIFIED",
        "SYSTEM",
        "COROSYNC",
        "PACEMAKER",
        "HANA",
        "NETWEAVER",
        "HANA_SECURITY",
        "CUSTOM",
    ]

@typing.type_check_only
class ScannedResource(typing_extensions.TypedDict, total=False):
    resource: str

@typing.type_check_only
class SqlserverValidation(typing_extensions.TypedDict, total=False):
    agentVersion: str
    instance: str
    projectId: str
    validationDetails: _list[SqlserverValidationValidationDetail]

@typing.type_check_only
class SqlserverValidationDetails(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class SqlserverValidationValidationDetail(typing_extensions.TypedDict, total=False):
    details: _list[SqlserverValidationDetails]
    type: typing_extensions.Literal[
        "SQLSERVER_VALIDATION_TYPE_UNSPECIFIED",
        "OS",
        "DB_LOG_DISK_SEPARATION",
        "DB_MAX_PARALLELISM",
        "DB_CXPACKET_WAITS",
        "DB_TRANSACTION_LOG_HANDLING",
        "DB_VIRTUAL_LOG_FILE_COUNT",
        "DB_BUFFER_POOL_EXTENSION",
        "DB_MAX_SERVER_MEMORY",
        "INSTANCE_METRICS",
        "DB_INDEX_FRAGMENTATION",
        "DB_TABLE_INDEX_COMPRESSION",
        "DB_BACKUP_POLICY",
    ]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ViolationDetails(typing_extensions.TypedDict, total=False):
    asset: str
    observed: dict[str, typing.Any]
    serviceAccount: str

@typing.type_check_only
class WriteInsightRequest(typing_extensions.TypedDict, total=False):
    insight: Insight
    requestId: str

@typing.type_check_only
class WriteInsightResponse(typing_extensions.TypedDict, total=False): ...
