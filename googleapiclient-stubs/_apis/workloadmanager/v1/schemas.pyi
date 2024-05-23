import typing

import typing_extensions

_list = list

@typing.type_check_only
class AssetLocation(typing_extensions.TypedDict, total=False):
    expected: IsolationExpectations
    extraParameters: _list[ExtraParameter]
    locationData: _list[LocationData]
    parentAsset: _list[CloudAsset]

@typing.type_check_only
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    createNewResultsTable: bool
    destinationDataset: str

@typing.type_check_only
class BlobstoreLocation(typing_extensions.TypedDict, total=False):
    policyId: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudAsset(typing_extensions.TypedDict, total=False):
    assetName: str
    assetType: str

@typing.type_check_only
class CloudAssetComposition(typing_extensions.TypedDict, total=False):
    childAsset: _list[CloudAsset]

@typing.type_check_only
class DirectLocationAssignment(typing_extensions.TypedDict, total=False):
    location: _list[LocationAssignment]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Evaluation(typing_extensions.TypedDict, total=False):
    bigQueryDestination: BigQueryDestination
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
    externalDataSources: _list[ExternalDataSources]
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
class ExternalDataSources(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "BIG_QUERY_TABLE"]
    uri: str

@typing.type_check_only
class ExtraParameter(typing_extensions.TypedDict, total=False):
    regionalMigDistributionPolicy: RegionalMigDistributionPolicy

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
class IsolationExpectations(typing_extensions.TypedDict, total=False):
    ziOrgPolicy: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    ziRegionPolicy: typing_extensions.Literal[
        "ZI_REGION_POLICY_UNSPECIFIED",
        "ZI_REGION_POLICY_UNKNOWN",
        "ZI_REGION_POLICY_NOT_SET",
        "ZI_REGION_POLICY_FAIL_OPEN",
        "ZI_REGION_POLICY_FAIL_CLOSED",
    ]
    ziRegionState: typing_extensions.Literal[
        "ZI_REGION_UNSPECIFIED",
        "ZI_REGION_UNKNOWN",
        "ZI_REGION_NOT_ENABLED",
        "ZI_REGION_ENABLED",
    ]
    zoneIsolation: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    zoneSeparation: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsOrgPolicy: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsRegionState: typing_extensions.Literal[
        "ZS_REGION_UNSPECIFIED",
        "ZS_REGION_UNKNOWN",
        "ZS_REGION_NOT_ENABLED",
        "ZS_REGION_ENABLED",
    ]

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
class LocationAssignment(typing_extensions.TypedDict, total=False):
    location: str
    locationType: typing_extensions.Literal[
        "UNSPECIFIED",
        "CLUSTER",
        "POP",
        "CLOUD_ZONE",
        "CLOUD_REGION",
        "MULTI_REGION_GEO",
        "MULTI_REGION_JURISDICTION",
        "GLOBAL",
        "OTHER",
    ]

@typing.type_check_only
class LocationData(typing_extensions.TypedDict, total=False):
    blobstoreLocation: BlobstoreLocation
    childAssetLocation: CloudAssetComposition
    directLocation: DirectLocationAssignment
    gcpProjectProxy: TenantProjectProxy
    spannerLocation: SpannerLocation

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
class RegionalMigDistributionPolicy(typing_extensions.TypedDict, total=False):
    targetShape: int
    zones: _list[ZoneConfiguration]

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
    tags: _list[str]
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
    projectNumber: str
    systemId: str
    updateTime: str
    workloadProperties: SapDiscoveryWorkloadProperties

@typing.type_check_only
class SapDiscoveryComponent(typing_extensions.TypedDict, total=False):
    applicationProperties: SapDiscoveryComponentApplicationProperties
    databaseProperties: SapDiscoveryComponentDatabaseProperties
    haHosts: _list[str]
    hostProject: str
    resources: _list[SapDiscoveryResource]
    sid: str
    topologyType: typing_extensions.Literal[
        "TOPOLOGY_TYPE_UNSPECIFIED", "TOPOLOGY_SCALE_UP", "TOPOLOGY_SCALE_OUT"
    ]

@typing.type_check_only
class SapDiscoveryComponentApplicationProperties(
    typing_extensions.TypedDict, total=False
):
    abap: bool
    appInstanceNumber: str
    applicationType: typing_extensions.Literal[
        "APPLICATION_TYPE_UNSPECIFIED", "NETWEAVER"
    ]
    ascsInstanceNumber: str
    ascsUri: str
    ersInstanceNumber: str
    kernelVersion: str
    nfsUri: str

@typing.type_check_only
class SapDiscoveryComponentDatabaseProperties(typing_extensions.TypedDict, total=False):
    databaseSid: str
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED", "HANA", "MAX_DB", "DB2"
    ]
    databaseVersion: str
    instanceNumber: str
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
    instanceProperties: SapDiscoveryResourceInstanceProperties
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
class SapDiscoveryResourceInstanceProperties(typing_extensions.TypedDict, total=False):
    appInstances: _list[SapDiscoveryResourceInstancePropertiesAppInstance]
    clusterInstances: _list[str]
    instanceNumber: str
    instanceRole: typing_extensions.Literal[
        "INSTANCE_ROLE_UNSPECIFIED",
        "INSTANCE_ROLE_ASCS",
        "INSTANCE_ROLE_ERS",
        "INSTANCE_ROLE_APP_SERVER",
        "INSTANCE_ROLE_DATABASE",
    ]
    virtualHostname: str

@typing.type_check_only
class SapDiscoveryResourceInstancePropertiesAppInstance(
    typing_extensions.TypedDict, total=False
):
    name: str
    number: str

@typing.type_check_only
class SapDiscoveryWorkloadProperties(typing_extensions.TypedDict, total=False):
    productVersions: _list[SapDiscoveryWorkloadPropertiesProductVersion]
    softwareComponentVersions: _list[
        SapDiscoveryWorkloadPropertiesSoftwareComponentProperties
    ]

@typing.type_check_only
class SapDiscoveryWorkloadPropertiesProductVersion(
    typing_extensions.TypedDict, total=False
):
    name: str
    version: str

@typing.type_check_only
class SapDiscoveryWorkloadPropertiesSoftwareComponentProperties(
    typing_extensions.TypedDict, total=False
):
    extVersion: str
    name: str
    type: str
    version: str

@typing.type_check_only
class SapValidation(typing_extensions.TypedDict, total=False):
    projectId: str
    validationDetails: _list[SapValidationValidationDetail]
    zone: str

@typing.type_check_only
class SapValidationValidationDetail(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    isPresent: bool
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
    type: str

@typing.type_check_only
class SpannerLocation(typing_extensions.TypedDict, total=False):
    dbName: _list[str]

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
class TenantProjectProxy(typing_extensions.TypedDict, total=False):
    projectNumbers: _list[str]

@typing.type_check_only
class ViolationDetails(typing_extensions.TypedDict, total=False):
    asset: str
    observed: dict[str, typing.Any]
    serviceAccount: str

@typing.type_check_only
class WriteInsightRequest(typing_extensions.TypedDict, total=False):
    agentVersion: str
    insight: Insight
    requestId: str

@typing.type_check_only
class WriteInsightResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str
