import typing

import typing_extensions

_list = list

@typing.type_check_only
class AppDevExperienceState(typing_extensions.TypedDict, total=False):
    networkingInstallSucceeded: AppDevExperienceStatus

@typing.type_check_only
class AppDevExperienceStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "OK", "FAILED", "UNKNOWN"]
    description: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudBuildSpec(typing_extensions.TypedDict, total=False):
    securityPolicy: typing_extensions.Literal[
        "SECURITY_POLICY_UNSPECIFIED", "NON_PRIVILEGED", "PRIVILEGED"
    ]
    version: str

@typing.type_check_only
class ClusterUpgradeGKEUpgrade(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ClusterUpgradeIgnoredMembership(typing_extensions.TypedDict, total=False):
    ignoredTime: str
    reason: str

@typing.type_check_only
class ClusterUpgradeMembershipGKEUpgradeState(typing_extensions.TypedDict, total=False):
    status: ClusterUpgradeUpgradeStatus
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeState(typing_extensions.TypedDict, total=False):
    ignored: ClusterUpgradeIgnoredMembership
    upgrades: _list[ClusterUpgradeMembershipGKEUpgradeState]

@typing.type_check_only
class ClusterUpgradeUpgradeStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "INELIGIBLE",
        "PENDING",
        "IN_PROGRESS",
        "SOAKING",
        "FORCED_SOAKING",
        "COMPLETE",
    ]
    reason: str
    updateTime: str

@typing.type_check_only
class ConfigManagementBinauthzConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ConfigManagementBinauthzState(typing_extensions.TypedDict, total=False):
    version: ConfigManagementBinauthzVersion
    webhook: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementBinauthzVersion(typing_extensions.TypedDict, total=False):
    webhookVersion: str

@typing.type_check_only
class ConfigManagementConfigSync(typing_extensions.TypedDict, total=False):
    enabled: bool
    git: ConfigManagementGitConfig
    metricsGcpServiceAccountEmail: str
    oci: ConfigManagementOciConfig
    preventDrift: bool
    sourceFormat: str
    stopSyncing: bool

@typing.type_check_only
class ConfigManagementConfigSyncDeploymentState(
    typing_extensions.TypedDict, total=False
):
    admissionWebhook: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gitSync: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    importer: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    monitor: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    otelCollector: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    reconcilerManager: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    resourceGroupControllerManager: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    rootReconciler: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    syncer: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementConfigSyncError(typing_extensions.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class ConfigManagementConfigSyncState(typing_extensions.TypedDict, total=False):
    clusterLevelStopSyncingState: typing_extensions.Literal[
        "STOP_SYNCING_STATE_UNSPECIFIED", "NOT_STOPPED", "PENDING", "STOPPED"
    ]
    crCount: int
    deploymentState: ConfigManagementConfigSyncDeploymentState
    errors: _list[ConfigManagementConfigSyncError]
    reposyncCrd: typing_extensions.Literal[
        "CRD_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLED",
        "TERMINATING",
        "INSTALLING",
    ]
    rootsyncCrd: typing_extensions.Literal[
        "CRD_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLED",
        "TERMINATING",
        "INSTALLING",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CONFIG_SYNC_NOT_INSTALLED",
        "CONFIG_SYNC_INSTALLED",
        "CONFIG_SYNC_ERROR",
        "CONFIG_SYNC_PENDING",
    ]
    syncState: ConfigManagementSyncState
    version: ConfigManagementConfigSyncVersion

@typing.type_check_only
class ConfigManagementConfigSyncVersion(typing_extensions.TypedDict, total=False):
    admissionWebhook: str
    gitSync: str
    importer: str
    monitor: str
    otelCollector: str
    reconcilerManager: str
    resourceGroupControllerManager: str
    rootReconciler: str
    syncer: str

@typing.type_check_only
class ConfigManagementErrorResource(typing_extensions.TypedDict, total=False):
    resourceGvk: ConfigManagementGroupVersionKind
    resourceName: str
    resourceNamespace: str
    sourcePath: str

@typing.type_check_only
class ConfigManagementGatekeeperDeploymentState(
    typing_extensions.TypedDict, total=False
):
    gatekeeperAudit: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gatekeeperControllerManagerState: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gatekeeperMutation: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementGitConfig(typing_extensions.TypedDict, total=False):
    gcpServiceAccountEmail: str
    httpsProxy: str
    policyDir: str
    secretType: str
    syncBranch: str
    syncRepo: str
    syncRev: str
    syncWaitSecs: str

@typing.type_check_only
class ConfigManagementGroupVersionKind(typing_extensions.TypedDict, total=False):
    group: str
    kind: str
    version: str

@typing.type_check_only
class ConfigManagementHierarchyControllerConfig(
    typing_extensions.TypedDict, total=False
):
    enableHierarchicalResourceQuota: bool
    enablePodTreeLabels: bool
    enabled: bool

@typing.type_check_only
class ConfigManagementHierarchyControllerDeploymentState(
    typing_extensions.TypedDict, total=False
):
    extension: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    hnc: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementHierarchyControllerState(
    typing_extensions.TypedDict, total=False
):
    state: ConfigManagementHierarchyControllerDeploymentState
    version: ConfigManagementHierarchyControllerVersion

@typing.type_check_only
class ConfigManagementHierarchyControllerVersion(
    typing_extensions.TypedDict, total=False
):
    extension: str
    hnc: str

@typing.type_check_only
class ConfigManagementInstallError(typing_extensions.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class ConfigManagementOciConfig(typing_extensions.TypedDict, total=False):
    gcpServiceAccountEmail: str
    policyDir: str
    secretType: str
    syncRepo: str
    syncWaitSecs: str

@typing.type_check_only
class ConfigManagementOperatorState(typing_extensions.TypedDict, total=False):
    deploymentState: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    errors: _list[ConfigManagementInstallError]
    version: str

@typing.type_check_only
class ConfigManagementPolicyController(typing_extensions.TypedDict, total=False):
    auditIntervalSeconds: str
    enabled: bool
    exemptableNamespaces: _list[str]
    logDeniesEnabled: bool
    monitoring: ConfigManagementPolicyControllerMonitoring
    mutationEnabled: bool
    referentialRulesEnabled: bool
    templateLibraryInstalled: bool
    updateTime: str

@typing.type_check_only
class ConfigManagementPolicyControllerMigration(
    typing_extensions.TypedDict, total=False
):
    copyTime: str
    stage: typing_extensions.Literal["STAGE_UNSPECIFIED", "ACM_MANAGED", "POCO_MANAGED"]

@typing.type_check_only
class ConfigManagementPolicyControllerMonitoring(
    typing_extensions.TypedDict, total=False
):
    backends: _list[
        typing_extensions.Literal[
            "MONITORING_BACKEND_UNSPECIFIED", "PROMETHEUS", "CLOUD_MONITORING"
        ]
    ]

@typing.type_check_only
class ConfigManagementPolicyControllerState(typing_extensions.TypedDict, total=False):
    deploymentState: ConfigManagementGatekeeperDeploymentState
    migration: ConfigManagementPolicyControllerMigration
    version: ConfigManagementPolicyControllerVersion

@typing.type_check_only
class ConfigManagementPolicyControllerVersion(typing_extensions.TypedDict, total=False):
    version: str

@typing.type_check_only
class ConfigManagementSpec(typing_extensions.TypedDict, total=False):
    binauthz: ConfigManagementBinauthzConfig
    cluster: str
    configSync: ConfigManagementConfigSync
    hierarchyController: ConfigManagementHierarchyControllerConfig
    management: typing_extensions.Literal[
        "MANAGEMENT_UNSPECIFIED", "MANAGEMENT_AUTOMATIC", "MANAGEMENT_MANUAL"
    ]
    policyController: ConfigManagementPolicyController
    version: str

@typing.type_check_only
class ConfigManagementState(typing_extensions.TypedDict, total=False):
    binauthzState: ConfigManagementBinauthzState
    clusterName: str
    configSyncState: ConfigManagementConfigSyncState
    hierarchyControllerState: ConfigManagementHierarchyControllerState
    membershipSpec: ConfigManagementSpec
    operatorState: ConfigManagementOperatorState
    policyControllerState: ConfigManagementPolicyControllerState

@typing.type_check_only
class ConfigManagementSyncError(typing_extensions.TypedDict, total=False):
    code: str
    errorMessage: str
    errorResources: _list[ConfigManagementErrorResource]

@typing.type_check_only
class ConfigManagementSyncState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "SYNC_CODE_UNSPECIFIED",
        "SYNCED",
        "PENDING",
        "ERROR",
        "NOT_CONFIGURED",
        "NOT_INSTALLED",
        "UNAUTHORIZED",
        "UNREACHABLE",
    ]
    errors: _list[ConfigManagementSyncError]
    importToken: str
    lastSync: str
    lastSyncTime: str
    sourceToken: str
    syncToken: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FeatureSpec(typing_extensions.TypedDict, total=False):
    cloudbuild: CloudBuildSpec
    configmanagement: ConfigManagementSpec
    identityservice: IdentityServiceSpec
    origin: Origin
    policycontroller: PolicyControllerSpec
    servicemesh: ServiceMeshSpec
    workloadcertificate: WorkloadCertificateSpec

@typing.type_check_only
class FeatureState(typing_extensions.TypedDict, total=False):
    appdevexperience: AppDevExperienceState
    clusterupgrade: ClusterUpgradeState
    configmanagement: ConfigManagementState
    identityservice: IdentityServiceState
    metering: MeteringState
    policycontroller: PolicyControllerState
    servicemesh: ServiceMeshState
    state: State

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class IdentityServiceAuthMethod(typing_extensions.TypedDict, total=False):
    azureadConfig: IdentityServiceAzureADConfig
    googleConfig: IdentityServiceGoogleConfig
    ldapConfig: IdentityServiceLdapConfig
    name: str
    oidcConfig: IdentityServiceOidcConfig
    proxy: str
    samlConfig: IdentityServiceSamlConfig

@typing.type_check_only
class IdentityServiceAzureADConfig(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str
    encryptedClientSecret: str
    groupFormat: str
    kubectlRedirectUri: str
    tenant: str
    userClaim: str

@typing.type_check_only
class IdentityServiceDiagnosticInterface(typing_extensions.TypedDict, total=False):
    enabled: bool
    expirationTime: str

@typing.type_check_only
class IdentityServiceGoogleConfig(typing_extensions.TypedDict, total=False):
    disable: bool

@typing.type_check_only
class IdentityServiceGroupConfig(typing_extensions.TypedDict, total=False):
    baseDn: str
    filter: str
    idAttribute: str

@typing.type_check_only
class IdentityServiceIdentityServiceOptions(typing_extensions.TypedDict, total=False):
    diagnosticInterface: IdentityServiceDiagnosticInterface
    sessionDuration: str

@typing.type_check_only
class IdentityServiceLdapConfig(typing_extensions.TypedDict, total=False):
    group: IdentityServiceGroupConfig
    server: IdentityServiceServerConfig
    serviceAccount: IdentityServiceServiceAccountConfig
    user: IdentityServiceUserConfig

@typing.type_check_only
class IdentityServiceOidcConfig(typing_extensions.TypedDict, total=False):
    certificateAuthorityData: str
    clientId: str
    clientSecret: str
    deployCloudConsoleProxy: bool
    enableAccessToken: bool
    encryptedClientSecret: str
    extraParams: str
    groupPrefix: str
    groupsClaim: str
    issuerUri: str
    kubectlRedirectUri: str
    scopes: str
    userClaim: str
    userPrefix: str

@typing.type_check_only
class IdentityServiceSamlConfig(typing_extensions.TypedDict, total=False):
    attributeMapping: dict[str, typing.Any]
    groupPrefix: str
    groupsAttribute: str
    identityProviderCertificates: _list[str]
    identityProviderId: str
    identityProviderSsoUri: str
    userAttribute: str
    userPrefix: str

@typing.type_check_only
class IdentityServiceServerConfig(typing_extensions.TypedDict, total=False):
    certificateAuthorityData: str
    connectionType: str
    host: str

@typing.type_check_only
class IdentityServiceServiceAccountConfig(typing_extensions.TypedDict, total=False):
    simpleBindCredentials: IdentityServiceSimpleBindCredentials

@typing.type_check_only
class IdentityServiceSimpleBindCredentials(typing_extensions.TypedDict, total=False):
    dn: str
    encryptedPassword: str
    password: str

@typing.type_check_only
class IdentityServiceSpec(typing_extensions.TypedDict, total=False):
    authMethods: _list[IdentityServiceAuthMethod]
    identityServiceOptions: IdentityServiceIdentityServiceOptions

@typing.type_check_only
class IdentityServiceState(typing_extensions.TypedDict, total=False):
    failureReason: str
    installedVersion: str
    memberConfig: IdentityServiceSpec
    state: typing_extensions.Literal["DEPLOYMENT_STATE_UNSPECIFIED", "OK", "ERROR"]

@typing.type_check_only
class IdentityServiceUserConfig(typing_extensions.TypedDict, total=False):
    baseDn: str
    filter: str
    idAttribute: str
    loginAttribute: str

@typing.type_check_only
class LifecycleState(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ENABLING",
        "ACTIVE",
        "DISABLING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipFeaturesResponse(typing_extensions.TypedDict, total=False):
    membershipFeatures: _list[MembershipFeature]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class MembershipFeature(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    lifecycleState: LifecycleState
    name: str
    spec: FeatureSpec
    state: FeatureState
    updateTime: str

@typing.type_check_only
class MeteringState(typing_extensions.TypedDict, total=False):
    lastMeasurementTime: str
    preciseLastMeasuredClusterVcpuCapacity: float

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Origin(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "FLEET", "FLEET_OUT_OF_SYNC", "USER"
    ]

@typing.type_check_only
class PolicyControllerBundleInstallSpec(typing_extensions.TypedDict, total=False):
    exemptedNamespaces: _list[str]

@typing.type_check_only
class PolicyControllerHubConfig(typing_extensions.TypedDict, total=False):
    auditIntervalSeconds: str
    constraintViolationLimit: str
    deploymentConfigs: dict[str, typing.Any]
    exemptableNamespaces: _list[str]
    installSpec: typing_extensions.Literal[
        "INSTALL_SPEC_UNSPECIFIED",
        "INSTALL_SPEC_NOT_INSTALLED",
        "INSTALL_SPEC_ENABLED",
        "INSTALL_SPEC_SUSPENDED",
        "INSTALL_SPEC_DETACHED",
    ]
    logDeniesEnabled: bool
    monitoring: PolicyControllerMonitoringConfig
    mutationEnabled: bool
    policyContent: PolicyControllerPolicyContentSpec
    referentialRulesEnabled: bool

@typing.type_check_only
class PolicyControllerMonitoringConfig(typing_extensions.TypedDict, total=False):
    backends: _list[
        typing_extensions.Literal[
            "MONITORING_BACKEND_UNSPECIFIED", "PROMETHEUS", "CLOUD_MONITORING"
        ]
    ]

@typing.type_check_only
class PolicyControllerOnClusterState(typing_extensions.TypedDict, total=False):
    details: str
    state: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLING",
        "ACTIVE",
        "UPDATING",
        "DECOMMISSIONING",
        "CLUSTER_ERROR",
        "HUB_ERROR",
        "SUSPENDED",
        "DETACHED",
    ]

@typing.type_check_only
class PolicyControllerPolicyContentSpec(typing_extensions.TypedDict, total=False):
    bundles: dict[str, typing.Any]
    templateLibrary: PolicyControllerTemplateLibraryConfig

@typing.type_check_only
class PolicyControllerPolicyContentState(typing_extensions.TypedDict, total=False):
    bundleStates: dict[str, typing.Any]
    referentialSyncConfigState: PolicyControllerOnClusterState
    templateLibraryState: PolicyControllerOnClusterState

@typing.type_check_only
class PolicyControllerPolicyControllerDeploymentConfig(
    typing_extensions.TypedDict, total=False
):
    containerResources: PolicyControllerResourceRequirements
    podAffinity: typing_extensions.Literal[
        "AFFINITY_UNSPECIFIED", "NO_AFFINITY", "ANTI_AFFINITY"
    ]
    podAntiAffinity: bool
    podTolerations: _list[PolicyControllerToleration]
    replicaCount: str

@typing.type_check_only
class PolicyControllerResourceList(typing_extensions.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class PolicyControllerResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: PolicyControllerResourceList
    requests: PolicyControllerResourceList

@typing.type_check_only
class PolicyControllerSpec(typing_extensions.TypedDict, total=False):
    policyControllerHubConfig: PolicyControllerHubConfig
    version: str

@typing.type_check_only
class PolicyControllerState(typing_extensions.TypedDict, total=False):
    componentStates: dict[str, typing.Any]
    policyContentState: PolicyControllerPolicyContentState
    state: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLING",
        "ACTIVE",
        "UPDATING",
        "DECOMMISSIONING",
        "CLUSTER_ERROR",
        "HUB_ERROR",
        "SUSPENDED",
        "DETACHED",
    ]

@typing.type_check_only
class PolicyControllerTemplateLibraryConfig(typing_extensions.TypedDict, total=False):
    installation: typing_extensions.Literal[
        "INSTALLATION_UNSPECIFIED", "NOT_INSTALLED", "ALL"
    ]

@typing.type_check_only
class PolicyControllerToleration(typing_extensions.TypedDict, total=False):
    effect: str
    key: str
    operator: str
    value: str

@typing.type_check_only
class ServiceMeshAnalysisMessage(typing_extensions.TypedDict, total=False):
    args: dict[str, typing.Any]
    description: str
    messageBase: ServiceMeshAnalysisMessageBase
    resourcePaths: _list[str]

@typing.type_check_only
class ServiceMeshAnalysisMessageBase(typing_extensions.TypedDict, total=False):
    documentationUrl: str
    level: typing_extensions.Literal["LEVEL_UNSPECIFIED", "ERROR", "WARNING", "INFO"]
    type: ServiceMeshType

@typing.type_check_only
class ServiceMeshCondition(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "MESH_IAM_PERMISSION_DENIED",
        "MESH_IAM_CROSS_PROJECT_PERMISSION_DENIED",
        "CNI_CONFIG_UNSUPPORTED",
        "GKE_SANDBOX_UNSUPPORTED",
        "NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED",
        "CNI_INSTALLATION_FAILED",
        "CNI_POD_UNSCHEDULABLE",
        "CLUSTER_HAS_ZERO_NODES",
        "UNSUPPORTED_MULTIPLE_CONTROL_PLANES",
        "VPCSC_GA_SUPPORTED",
        "DEPRECATED_SPEC_CONTROL_PLANE_MANAGEMENT",
        "DEPRECATED_SPEC_CONTROL_PLANE_MANAGEMENT_SAFE",
        "CONFIG_APPLY_INTERNAL_ERROR",
        "CONFIG_VALIDATION_ERROR",
        "CONFIG_VALIDATION_WARNING",
        "QUOTA_EXCEEDED_BACKEND_SERVICES",
        "QUOTA_EXCEEDED_HEALTH_CHECKS",
        "QUOTA_EXCEEDED_HTTP_ROUTES",
        "QUOTA_EXCEEDED_TCP_ROUTES",
        "QUOTA_EXCEEDED_TLS_ROUTES",
        "QUOTA_EXCEEDED_TRAFFIC_POLICIES",
        "QUOTA_EXCEEDED_ENDPOINT_POLICIES",
        "QUOTA_EXCEEDED_GATEWAYS",
        "QUOTA_EXCEEDED_MESHES",
        "QUOTA_EXCEEDED_SERVER_TLS_POLICIES",
        "QUOTA_EXCEEDED_CLIENT_TLS_POLICIES",
        "QUOTA_EXCEEDED_SERVICE_LB_POLICIES",
        "QUOTA_EXCEEDED_HTTP_FILTERS",
        "QUOTA_EXCEEDED_TCP_FILTERS",
        "QUOTA_EXCEEDED_NETWORK_ENDPOINT_GROUPS",
        "MODERNIZATION_SCHEDULED",
        "MODERNIZATION_IN_PROGRESS",
        "MODERNIZATION_COMPLETED",
        "MODERNIZATION_ABORTED",
    ]
    details: str
    documentationLink: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"
    ]

@typing.type_check_only
class ServiceMeshControlPlaneManagement(typing_extensions.TypedDict, total=False):
    details: _list[ServiceMeshStatusDetails]
    implementation: typing_extensions.Literal[
        "IMPLEMENTATION_UNSPECIFIED", "ISTIOD", "TRAFFIC_DIRECTOR", "UPDATING"
    ]
    state: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "DISABLED",
        "FAILED_PRECONDITION",
        "PROVISIONING",
        "ACTIVE",
        "STALLED",
        "NEEDS_ATTENTION",
        "DEGRADED",
    ]

@typing.type_check_only
class ServiceMeshDataPlaneManagement(typing_extensions.TypedDict, total=False):
    details: _list[ServiceMeshStatusDetails]
    state: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "DISABLED",
        "FAILED_PRECONDITION",
        "PROVISIONING",
        "ACTIVE",
        "STALLED",
        "NEEDS_ATTENTION",
        "DEGRADED",
    ]

@typing.type_check_only
class ServiceMeshSpec(typing_extensions.TypedDict, total=False):
    configApi: typing_extensions.Literal[
        "CONFIG_API_UNSPECIFIED", "CONFIG_API_ISTIO", "CONFIG_API_GATEWAY"
    ]
    controlPlane: typing_extensions.Literal[
        "CONTROL_PLANE_MANAGEMENT_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    defaultChannel: typing_extensions.Literal[
        "CHANNEL_UNSPECIFIED", "RAPID", "REGULAR", "STABLE"
    ]
    management: typing_extensions.Literal[
        "MANAGEMENT_UNSPECIFIED", "MANAGEMENT_AUTOMATIC", "MANAGEMENT_MANUAL"
    ]

@typing.type_check_only
class ServiceMeshState(typing_extensions.TypedDict, total=False):
    analysisMessages: _list[ServiceMeshAnalysisMessage]
    conditions: _list[ServiceMeshCondition]
    configApiVersion: str
    controlPlaneManagement: ServiceMeshControlPlaneManagement
    dataPlaneManagement: ServiceMeshDataPlaneManagement

@typing.type_check_only
class ServiceMeshStatusDetails(typing_extensions.TypedDict, total=False):
    code: str
    details: str

@typing.type_check_only
class ServiceMeshType(typing_extensions.TypedDict, total=False):
    code: str
    displayName: str

@typing.type_check_only
class State(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "OK", "WARNING", "ERROR"]
    description: str
    updateTime: str

@typing.type_check_only
class WorkloadCertificateSpec(typing_extensions.TypedDict, total=False):
    certificateManagement: typing_extensions.Literal[
        "CERTIFICATE_MANAGEMENT_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
