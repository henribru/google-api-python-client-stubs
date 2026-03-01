import typing

import typing_extensions

_list = list

@typing.type_check_only
class ActiveDirectory(typing_extensions.TypedDict, total=False):
    dnsAddress: str
    domain: str
    domainUsername: str
    secretManagerSecret: str
    type: typing_extensions.Literal[
        "ACTIVE_DIRECTORY_TYPE_UNSPECIFIED", "GCP_MANAGED", "SELF_MANAGED"
    ]

@typing.type_check_only
class Actuation(typing_extensions.TypedDict, total=False):
    actuationOutput: ActuationOutput
    deploymentOutput: _list[DeploymentOutput]
    endTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INFRA_CREATING",
        "SUCCEEDED",
        "FAILED",
        "POST_INFRA_CONFIGURING",
        "INFRA_DESTROYING",
        "TIMEOUT",
    ]

@typing.type_check_only
class ActuationOutput(typing_extensions.TypedDict, total=False):
    actuateLogs: str
    ansibleError: str
    ansibleFailedTask: _list[str]
    blueprintId: str
    cloudbuildId: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "TERRAFORM_FAILED",
        "PERMISSION_DENIED_IN_TERRAFORM",
        "QUOTA_EXCEED_IN_TERRAFORM",
        "ANSIBLE_FAILED",
        "CONSTRAINT_VIOLATION_IN_TERRAFORM",
        "RESOURCE_ALREADY_EXISTS_IN_TERRAFORM",
        "RESOURCE_UNAVAILABLE_IN_TERRAFORM",
        "PERMISSION_DENIED_IN_ANSIBLE",
        "INVALID_SECRET_IN_ANSIBLE",
        "TERRAFORM_DELETION_FAILED",
        "RESOURCE_IN_USE_IN_TERRAFORM_DELETION",
        "ANSIBLE_START_FAILED",
    ]
    errorLogs: str
    hasUserFacingErrorMsg: bool
    terraformError: str
    terraformTemplate: str

@typing.type_check_only
class AgentCommand(typing_extensions.TypedDict, total=False):
    command: str
    parameters: dict[str, typing.Any]

@typing.type_check_only
class AgentStates(typing_extensions.TypedDict, total=False):
    availableVersion: str
    hanaMonitoring: ServiceStates
    installedVersion: str
    isFullyEnabled: bool
    processMetrics: ServiceStates
    systemDiscovery: ServiceStates

@typing.type_check_only
class AgentStatus(typing_extensions.TypedDict, total=False):
    agentName: str
    availableVersion: str
    cloudApiAccessFullScopesGranted: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    configurationErrorMessage: str
    configurationFilePath: str
    configurationValid: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    installedVersion: str
    instanceUri: str
    kernelVersion: SapDiscoveryResourceInstancePropertiesKernelVersion
    references: _list[AgentStatusReference]
    services: _list[AgentStatusServiceStatus]
    systemdServiceEnabled: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    systemdServiceRunning: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]

@typing.type_check_only
class AgentStatusConfigValue(typing_extensions.TypedDict, total=False):
    isDefault: bool
    name: str
    value: str

@typing.type_check_only
class AgentStatusIAMPermission(typing_extensions.TypedDict, total=False):
    granted: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    name: str

@typing.type_check_only
class AgentStatusReference(typing_extensions.TypedDict, total=False):
    name: str
    url: str

@typing.type_check_only
class AgentStatusServiceStatus(typing_extensions.TypedDict, total=False):
    configValues: _list[AgentStatusConfigValue]
    errorMessage: str
    fullyFunctional: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    iamPermissions: _list[AgentStatusIAMPermission]
    name: str
    state: typing_extensions.Literal[
        "UNSPECIFIED_STATE", "SUCCESS_STATE", "FAILURE_STATE", "ERROR_STATE"
    ]
    unspecifiedStateMessage: str

@typing.type_check_only
class AppDetails(typing_extensions.TypedDict, total=False):
    appInstanceId: str
    appServiceAccount: str
    appVmNames: _list[str]
    ascsImage: str
    ascsInstanceId: str
    ascsMachineType: str
    ascsServiceAccount: str
    ascsVm: str
    ersInstanceId: str
    ersVm: str
    image: str
    machineType: str
    secretManagerSecret: str
    sharedStorage: str
    sid: str
    vmsMultiplier: int

@typing.type_check_only
class BackupProperties(typing_extensions.TypedDict, total=False):
    latestBackupStatus: typing_extensions.Literal[
        "BACKUP_STATE_UNSPECIFIED", "BACKUP_STATE_SUCCESS", "BACKUP_STATE_FAILURE"
    ]
    latestBackupTime: str

@typing.type_check_only
class BigQueryDestination(typing_extensions.TypedDict, total=False):
    createNewResultsTable: bool
    destinationDataset: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudResource(typing_extensions.TypedDict, total=False):
    instanceProperties: InstanceProperties
    kind: typing_extensions.Literal[
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
    name: str

@typing.type_check_only
class Command(typing_extensions.TypedDict, total=False):
    agentCommand: AgentCommand
    shellCommand: ShellCommand

@typing.type_check_only
class ComponentHealth(typing_extensions.TypedDict, total=False):
    component: str
    componentHealthChecks: _list[HealthCheck]
    componentHealthType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_REQUIRED", "TYPE_OPTIONAL", "TYPE_SPECIAL"
    ]
    state: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY", "CRITICAL", "UNSUPPORTED"
    ]
    subComponentsHealth: _list[ComponentHealth]

@typing.type_check_only
class Database(typing_extensions.TypedDict, total=False):
    diskType: str
    floatingIpAddress: str
    machineType: str
    secondarySoleTenantNode: str
    secondarySoleTenantNodeType: str
    secretManagerSecret: str
    smt: bool
    soleTenantNode: str
    soleTenantNodeType: str
    tempdbOnSsd: bool
    tenancyModel: typing_extensions.Literal[
        "TENANCY_MODEL_UNSPECIFIED", "SHARED", "SOLE_TENANT"
    ]

@typing.type_check_only
class DatabaseDetails(typing_extensions.TypedDict, total=False):
    databaseServiceAccount: str
    diskType: str
    image: str
    instanceId: str
    machineType: str
    primaryDbVm: str
    secondaryDbVm: str
    secretManagerSecret: str
    sid: str

@typing.type_check_only
class DatabaseProperties(typing_extensions.TypedDict, total=False):
    backupProperties: BackupProperties
    databaseType: typing_extensions.Literal[
        "DATABASE_TYPE_UNSPECIFIED",
        "HANA",
        "MAX_DB",
        "DB2",
        "ORACLE",
        "SQLSERVER",
        "ASE",
    ]

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    sapSystemS4Config: SapSystemS4Config
    serviceAccount: str
    sqlServerWorkload: SqlServerWorkload
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "UPDATING", "DELETING", "FAILED"
    ]
    terraformVariables: dict[str, typing.Any]
    updateTime: str
    workerPool: str
    workloadType: typing_extensions.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "SAP_S4", "SQL_SERVER", "ORACLE"
    ]

@typing.type_check_only
class DeploymentOutput(typing_extensions.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Evaluation(typing_extensions.TypedDict, total=False):
    bigQueryDestination: BigQueryDestination
    createTime: str
    customRulesBucket: str
    description: str
    evaluationType: typing_extensions.Literal[
        "EVALUATION_TYPE_UNSPECIFIED", "SAP", "SQL_SERVER", "OTHER", "SCC_IAC"
    ]
    kmsKey: str
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
    engine: typing_extensions.Literal["ENGINE_UNSPECIFIED", "ENGINE_SCANNER", "V2"]
    evaluationId: str
    externalDataSources: _list[ExternalDataSources]
    inventoryTime: str
    labels: dict[str, typing.Any]
    name: str
    notices: _list[Notice]
    resultSummary: Summary
    ruleResults: _list[RuleExecutionResult]
    runType: typing_extensions.Literal["TYPE_UNSPECIFIED", "ONE_TIME", "SCHEDULED"]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class ExecutionResult(typing_extensions.TypedDict, total=False):
    commands: _list[Command]
    documentationUrl: str
    resource: Resource
    rule: str
    severity: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TYPE_PASSED", "TYPE_VIOLATED"]
    violationDetails: ViolationDetails
    violationMessage: str

@typing.type_check_only
class ExternalDataSources(typing_extensions.TypedDict, total=False):
    assetType: str
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "BIG_QUERY_TABLE"]
    uri: str

@typing.type_check_only
class GceInstanceFilter(typing_extensions.TypedDict, total=False):
    serviceAccounts: _list[str]

@typing.type_check_only
class HealthCheck(typing_extensions.TypedDict, total=False):
    message: str
    metric: str
    resource: CloudResource
    source: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PASSED", "FAILED", "DEGRADED", "SKIPPED", "UNSUPPORTED"
    ]

@typing.type_check_only
class IAMPermission(typing_extensions.TypedDict, total=False):
    granted: bool
    name: str

@typing.type_check_only
class Insight(typing_extensions.TypedDict, total=False):
    agentStatus: AgentStatus
    instanceId: str
    openShiftValidation: OpenShiftValidation
    sapDiscovery: SapDiscovery
    sapValidation: SapValidation
    sentTime: str
    sqlserverValidation: SqlserverValidation
    torsoValidation: TorsoValidation

@typing.type_check_only
class InstanceProperties(typing_extensions.TypedDict, total=False):
    instanceNumber: str
    machineType: str
    roles: _list[
        typing_extensions.Literal[
            "INSTANCE_ROLE_UNSPECIFIED",
            "INSTANCE_ROLE_ASCS",
            "INSTANCE_ROLE_ERS",
            "INSTANCE_ROLE_APP_SERVER",
            "INSTANCE_ROLE_HANA_PRIMARY",
            "INSTANCE_ROLE_HANA_SECONDARY",
        ]
    ]
    sapInstanceProperties: SapInstanceProperties
    status: str
    upcomingMaintenanceEvent: UpcomingMaintenanceEvent

@typing.type_check_only
class InvalidRule(typing_extensions.TypedDict, total=False):
    displayName: str
    gcsUri: str
    name: str
    valiadtionError: str

@typing.type_check_only
class InvalidRulesWrapper(typing_extensions.TypedDict, total=False):
    invalidRules: _list[InvalidRule]

@typing.type_check_only
class ListActuationsResponse(typing_extensions.TypedDict, total=False):
    actuations: _list[Actuation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredProfilesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workloadProfiles: _list[WorkloadProfile]

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
    unreachable: _list[str]

@typing.type_check_only
class ListRulesResponse(typing_extensions.TypedDict, total=False):
    invalidRulesWrapper: InvalidRulesWrapper
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
class LocationDetails(typing_extensions.TypedDict, total=False):
    createCommsFirewall: bool
    customTags: _list[str]
    deploymentDnsEnabled: bool
    dnsZone: str
    dnsZoneNameSuffix: str
    internetAccess: typing_extensions.Literal[
        "INTERNETACCESS_UNSPECIFIED", "ALLOW_EXTERNAL_IP", "CONFIGURE_NAT"
    ]
    networkProject: str
    regionName: str
    subnetName: str
    vpcName: str
    zone1Name: str
    zone2Name: str

@typing.type_check_only
class Notice(typing_extensions.TypedDict, total=False):
    message: str

@typing.type_check_only
class OpenShiftValidation(typing_extensions.TypedDict, total=False):
    clusterId: str
    validationDetails: dict[str, typing.Any]

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
class Pacemaker(typing_extensions.TypedDict, total=False):
    bucketNameNodeCertificates: str
    pacemakerCluster: str
    pacemakerClusterSecret: str
    pacemakerClusterUsername: str
    sqlPacemakerSecret: str
    sqlPacemakerUsername: str

@typing.type_check_only
class Product(typing_extensions.TypedDict, total=False):
    name: str
    version: str

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
    assetType: str
    description: str
    displayName: str
    errorMessage: str
    name: str
    primaryCategory: str
    remediation: str
    revisionId: str
    ruleType: typing_extensions.Literal["RULE_TYPE_UNSPECIFIED", "BASELINE", "CUSTOM"]
    secondaryCategory: str
    severity: str
    tags: _list[str]
    uri: str

@typing.type_check_only
class RuleExecutionResult(typing_extensions.TypedDict, total=False):
    message: str
    resultCount: str
    rule: str
    scannedResourceCount: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "STATE_SUCCESS", "STATE_FAILURE", "STATE_SKIPPED"
    ]

@typing.type_check_only
class RuleOutput(typing_extensions.TypedDict, total=False):
    details: dict[str, typing.Any]
    message: str

@typing.type_check_only
class RunEvaluationRequest(typing_extensions.TypedDict, total=False):
    execution: Execution
    executionId: str
    requestId: str

@typing.type_check_only
class SapComponent(typing_extensions.TypedDict, total=False):
    databaseProperties: DatabaseProperties
    haHosts: _list[str]
    resources: _list[CloudResource]
    sid: str
    topologyType: typing_extensions.Literal[
        "TOPOLOGY_TYPE_UNSPECIFIED", "TOPOLOGY_SCALE_UP", "TOPOLOGY_SCALE_OUT"
    ]

@typing.type_check_only
class SapDiscovery(typing_extensions.TypedDict, total=False):
    applicationLayer: SapDiscoveryComponent
    databaseLayer: SapDiscoveryComponent
    metadata: SapDiscoveryMetadata
    projectNumber: str
    systemId: str
    updateTime: str
    useDrReconciliation: bool
    workloadProperties: SapDiscoveryWorkloadProperties

@typing.type_check_only
class SapDiscoveryComponent(typing_extensions.TypedDict, total=False):
    applicationProperties: SapDiscoveryComponentApplicationProperties
    databaseProperties: SapDiscoveryComponentDatabaseProperties
    haHosts: _list[str]
    hostProject: str
    region: str
    replicationSites: _list[SapDiscoveryComponentReplicationSite]
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
        "APPLICATION_TYPE_UNSPECIFIED", "NETWEAVER", "NETWEAVER_ABAP", "NETWEAVER_JAVA"
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
        "DATABASE_TYPE_UNSPECIFIED",
        "HANA",
        "MAX_DB",
        "DB2",
        "ORACLE",
        "SQLSERVER",
        "ASE",
    ]
    databaseVersion: str
    instanceNumber: str
    landscapeId: str
    primaryInstanceUri: str
    sharedNfsUri: str

@typing.type_check_only
class SapDiscoveryComponentReplicationSite(typing_extensions.TypedDict, total=False):
    component: SapDiscoveryComponent
    sourceSite: str

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
    diskMounts: _list[SapDiscoveryResourceInstancePropertiesDiskMount]
    instanceNumber: str
    instanceRole: typing_extensions.Literal[
        "INSTANCE_ROLE_UNSPECIFIED",
        "INSTANCE_ROLE_ASCS",
        "INSTANCE_ROLE_ERS",
        "INSTANCE_ROLE_APP_SERVER",
        "INSTANCE_ROLE_DATABASE",
        "INSTANCE_ROLE_ASCS_ERS",
        "INSTANCE_ROLE_ASCS_APP_SERVER",
        "INSTANCE_ROLE_ASCS_DATABASE",
        "INSTANCE_ROLE_ERS_APP_SERVER",
        "INSTANCE_ROLE_ERS_DATABASE",
        "INSTANCE_ROLE_APP_SERVER_DATABASE",
        "INSTANCE_ROLE_ASCS_ERS_APP_SERVER",
        "INSTANCE_ROLE_ASCS_ERS_DATABASE",
        "INSTANCE_ROLE_ASCS_APP_SERVER_DATABASE",
        "INSTANCE_ROLE_ERS_APP_SERVER_DATABASE",
        "INSTANCE_ROLE_ASCS_ERS_APP_SERVER_DATABASE",
    ]
    isDrSite: bool
    osKernelVersion: SapDiscoveryResourceInstancePropertiesKernelVersion
    virtualHostname: str

@typing.type_check_only
class SapDiscoveryResourceInstancePropertiesAppInstance(
    typing_extensions.TypedDict, total=False
):
    name: str
    number: str

@typing.type_check_only
class SapDiscoveryResourceInstancePropertiesDiskMount(
    typing_extensions.TypedDict, total=False
):
    diskNames: _list[str]
    mountPoint: str
    name: str

@typing.type_check_only
class SapDiscoveryResourceInstancePropertiesKernelVersion(
    typing_extensions.TypedDict, total=False
):
    distroKernel: SapDiscoveryResourceInstancePropertiesKernelVersionVersion
    osKernel: SapDiscoveryResourceInstancePropertiesKernelVersionVersion
    rawString: str

@typing.type_check_only
class SapDiscoveryResourceInstancePropertiesKernelVersionVersion(
    typing_extensions.TypedDict, total=False
):
    build: int
    major: int
    minor: int
    patch: int
    remainder: str

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
class SapInstanceProperties(typing_extensions.TypedDict, total=False):
    agentStates: AgentStates
    numbers: _list[str]

@typing.type_check_only
class SapSystemS4Config(typing_extensions.TypedDict, total=False):
    allowStoppingForUpdate: bool
    ansibleRunnerServiceAccount: str
    app: AppDetails
    database: DatabaseDetails
    deploymentModel: typing_extensions.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "DISTRIBUTED", "DISTRIBUTED_HA"
    ]
    environmentType: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "NON_PRODUCTION", "PRODUCTION"
    ]
    gcpProjectId: str
    location: LocationDetails
    mediaBucketName: str
    sapBootDiskImage: str
    scalingMethod: typing_extensions.Literal[
        "SCALE_METHOD_UNSPECIFIED", "SCALE_UP", "SCALE_OUT"
    ]
    version: typing_extensions.Literal[
        "VERSION_UNSPECIFIED", "S4_HANA_2021", "S4_HANA_2022", "S4_HANA_2023"
    ]
    vmPrefix: str

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
class SapWorkload(typing_extensions.TypedDict, total=False):
    application: SapComponent
    architecture: typing_extensions.Literal[
        "ARCHITECTURE_UNSPECIFIED",
        "INVALID",
        "CENTRALIZED",
        "DISTRIBUTED",
        "DISTRIBUTED_HA",
        "STANDALONE_DATABASE",
        "STANDALONE_DATABASE_HA",
    ]
    database: SapComponent
    metadata: dict[str, typing.Any]
    products: _list[Product]

@typing.type_check_only
class ScannedResource(typing_extensions.TypedDict, total=False):
    resource: str
    type: str

@typing.type_check_only
class ServiceStates(typing_extensions.TypedDict, total=False):
    iamPermissions: _list[IAMPermission]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CONFIG_FAILURE",
        "IAM_FAILURE",
        "FUNCTIONALITY_FAILURE",
        "ENABLED",
        "DISABLED",
    ]

@typing.type_check_only
class ShellCommand(typing_extensions.TypedDict, total=False):
    args: str
    command: str
    timeoutSeconds: int

@typing.type_check_only
class SqlLocationDetails(typing_extensions.TypedDict, total=False):
    dnsZone: str
    gcpProjectId: str
    internetAccess: typing_extensions.Literal[
        "INTERNET_ACCESS_UNSPECIFIED", "ALLOW_EXTERNAL_IP", "CONFIGURE_NAT"
    ]
    network: str
    primaryZone: str
    region: str
    secondaryZone: str
    subnetwork: str
    tertiaryZone: str

@typing.type_check_only
class SqlServerWorkload(typing_extensions.TypedDict, total=False):
    activeDirectory: ActiveDirectory
    computeEngineServiceAccount: str
    database: Database
    deploymentModel: typing_extensions.Literal[
        "DEPLOYMENT_MODEL_UNSPECIFIED", "HIGH_AVAILABILITY", "SINGLE_INSTANCE"
    ]
    environmentType: typing_extensions.Literal[
        "ENVIRONMENT_TYPE_UNSPECIFIED", "NON_PRODUCTION", "PRODUCTION"
    ]
    fciType: typing_extensions.Literal["FCI_TYPE_UNSPECIFIED", "SHARED_DISK", "S2D"]
    haType: typing_extensions.Literal["HA_TYPE_UNSPECIFIED", "AOAG", "FCI"]
    isSqlPayg: bool
    location: SqlLocationDetails
    mediaBucket: str
    operatingSystemType: typing_extensions.Literal[
        "OPERATING_SYSTEM_TYPE_UNSPECIFIED",
        "WINDOWS",
        "UBUNTU",
        "RED_HAT_ENTERPRISE_LINUX",
        "SUSE",
    ]
    osImage: str
    osImageType: typing_extensions.Literal[
        "OS_IMAGE_TYPE_UNSPECIFIED", "PUBLIC_IMAGE", "CUSTOM_IMAGE"
    ]
    pacemaker: Pacemaker
    sqlServerEdition: typing_extensions.Literal[
        "SQL_SERVER_EDITION_TYPE_UNSPECIFIED",
        "SQL_SERVER_EDITION_TYPE_DEVELOPER",
        "SQL_SERVER_EDITION_TYPE_ENTERPRISE",
        "SQL_SERVER_EDITION_TYPE_STANDARD",
        "SQL_SERVER_EDITION_TYPE_WEB",
    ]
    sqlServerVersion: typing_extensions.Literal[
        "SQL_SERVER_VERSION_TYPE_UNSPECIFIED",
        "SQL_SERVER_VERSION_TYPE_2017",
        "SQL_SERVER_VERSION_TYPE_2019",
        "SQL_SERVER_VERSION_TYPE_2022",
    ]
    vmPrefix: str

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
class Summary(typing_extensions.TypedDict, total=False):
    failures: str
    newFailures: str
    newFixes: str

@typing.type_check_only
class TerraformVariable(typing_extensions.TypedDict, total=False):
    inputValue: typing.Any

@typing.type_check_only
class TorsoValidation(typing_extensions.TypedDict, total=False):
    agentVersion: str
    instanceName: str
    projectId: str
    validationDetails: dict[str, typing.Any]
    workloadType: typing_extensions.Literal[
        "WORKLOAD_TYPE_UNSPECIFIED", "MYSQL", "ORACLE", "REDIS"
    ]

@typing.type_check_only
class UpcomingMaintenanceEvent(typing_extensions.TypedDict, total=False):
    endTime: str
    maintenanceStatus: str
    onHostMaintenance: str
    startTime: str
    type: str

@typing.type_check_only
class ViolationDetails(typing_extensions.TypedDict, total=False):
    asset: str
    observed: dict[str, typing.Any]
    ruleOutput: _list[RuleOutput]
    serviceAccount: str

@typing.type_check_only
class WorkloadProfile(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    refreshedTime: str
    sapWorkload: SapWorkload
    workloadType: typing_extensions.Literal["WORKLOAD_TYPE_UNSPECIFIED", "S4_HANA"]

@typing.type_check_only
class WorkloadProfileHealth(typing_extensions.TypedDict, total=False):
    checkTime: str
    componentsHealth: _list[ComponentHealth]
    state: typing_extensions.Literal[
        "HEALTH_STATE_UNSPECIFIED", "HEALTHY", "UNHEALTHY", "CRITICAL", "UNSUPPORTED"
    ]

@typing.type_check_only
class WriteInsightRequest(typing_extensions.TypedDict, total=False):
    agentVersion: str
    insight: Insight
    requestId: str

@typing.type_check_only
class WriteInsightResponse(typing_extensions.TypedDict, total=False): ...
