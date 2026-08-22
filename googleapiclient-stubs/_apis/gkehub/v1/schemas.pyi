import typing

_list = list

@typing.type_check_only
class AppDevExperienceFeatureSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class AppDevExperienceFeatureState(typing.TypedDict, total=False):
    networkingInstallSucceeded: Status

@typing.type_check_only
class ApplianceCluster(typing.TypedDict, total=False):
    resourceLink: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Authority(typing.TypedDict, total=False):
    identityProvider: str
    issuer: str
    oidcJwks: str
    scopeTenancyIdentityProvider: str
    scopeTenancyWorkloadIdentityPool: str
    workloadIdentityPool: str

@typing.type_check_only
class AutoUpgradeConfig(typing.TypedDict, total=False):
    enforcedRollouts: dict[str, typing.Any]
    rolloutCreationScope: RolloutCreationScope

@typing.type_check_only
class BinaryAuthorizationConfig(typing.TypedDict, total=False):
    evaluationMode: typing.Literal[
        "EVALUATION_MODE_UNSPECIFIED", "DISABLED", "POLICY_BINDINGS"
    ]
    policyBindings: _list[PolicyBinding]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelRolloutRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClusterSelector(typing.TypedDict, total=False):
    labelSelector: str

@typing.type_check_only
class ClusterUpgradeFleetSpec(typing.TypedDict, total=False):
    gkeUpgradeOverrides: _list[ClusterUpgradeGKEUpgradeOverride]
    postConditions: ClusterUpgradePostConditions
    upstreamFleets: _list[str]

@typing.type_check_only
class ClusterUpgradeFleetState(typing.TypedDict, total=False):
    downstreamFleets: _list[str]
    gkeState: ClusterUpgradeGKEUpgradeFeatureState
    ignored: dict[str, typing.Any]

@typing.type_check_only
class ClusterUpgradeGKEUpgrade(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ClusterUpgradeGKEUpgradeFeatureCondition(typing.TypedDict, total=False):
    reason: str
    status: str
    type: str
    updateTime: str

@typing.type_check_only
class ClusterUpgradeGKEUpgradeFeatureState(typing.TypedDict, total=False):
    conditions: _list[ClusterUpgradeGKEUpgradeFeatureCondition]
    upgradeState: _list[ClusterUpgradeGKEUpgradeState]

@typing.type_check_only
class ClusterUpgradeGKEUpgradeOverride(typing.TypedDict, total=False):
    postConditions: ClusterUpgradePostConditions
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeGKEUpgradeState(typing.TypedDict, total=False):
    stats: dict[str, typing.Any]
    status: ClusterUpgradeUpgradeStatus
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeIgnoredMembership(typing.TypedDict, total=False):
    ignoredTime: str
    reason: str

@typing.type_check_only
class ClusterUpgradeMembershipGKEUpgradeState(typing.TypedDict, total=False):
    status: ClusterUpgradeUpgradeStatus
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeMembershipState(typing.TypedDict, total=False):
    ignored: ClusterUpgradeIgnoredMembership
    upgrades: _list[ClusterUpgradeMembershipGKEUpgradeState]

@typing.type_check_only
class ClusterUpgradePostConditions(typing.TypedDict, total=False):
    soaking: str

@typing.type_check_only
class ClusterUpgradeUpgradeStatus(typing.TypedDict, total=False):
    code: typing.Literal[
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
class CommonFeatureSpec(typing.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureSpec
    clusterupgrade: ClusterUpgradeFleetSpec
    dataplanev2: DataplaneV2FeatureSpec
    fleetobservability: FleetObservabilityFeatureSpec
    mesh: ServiceMeshFeatureSpec
    multiclusteringress: MultiClusterIngressFeatureSpec
    rbacrolebindingactuation: RBACRoleBindingActuationFeatureSpec
    workloadidentity: WorkloadIdentityFeatureSpec

@typing.type_check_only
class CommonFeatureState(typing.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
    clusterupgrade: ClusterUpgradeFleetState
    fleetobservability: FleetObservabilityFeatureState
    rbacrolebindingactuation: RBACRoleBindingActuationFeatureState
    servicemesh: ServiceMeshFeatureState
    state: FeatureState
    workloadidentity: WorkloadIdentityFeatureState

@typing.type_check_only
class CommonFleetDefaultMemberConfigSpec(typing.TypedDict, total=False):
    configmanagement: ConfigManagementMembershipSpec
    identityservice: IdentityServiceMembershipSpec
    mesh: ServiceMeshMembershipSpec
    policycontroller: PolicyControllerMembershipSpec

@typing.type_check_only
class CompliancePostureConfig(typing.TypedDict, total=False):
    complianceStandards: _list[ComplianceStandard]
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class ComplianceStandard(typing.TypedDict, total=False):
    standard: str

@typing.type_check_only
class ConfigManagementConfigSync(typing.TypedDict, total=False):
    deploymentOverrides: _list[ConfigManagementDeploymentOverride]
    enabled: bool
    git: ConfigManagementGitConfig
    metricsGcpServiceAccountEmail: str
    oci: ConfigManagementOciConfig
    preventDrift: bool
    sourceFormat: str
    stopSyncing: bool

@typing.type_check_only
class ConfigManagementConfigSyncDeploymentState(typing.TypedDict, total=False):
    admissionWebhook: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gitSync: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    importer: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    monitor: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    otelCollector: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    reconcilerManager: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    resourceGroupControllerManager: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    rootReconciler: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    syncer: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementConfigSyncError(typing.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class ConfigManagementConfigSyncState(typing.TypedDict, total=False):
    clusterLevelStopSyncingState: typing.Literal[
        "STOP_SYNCING_STATE_UNSPECIFIED", "NOT_STOPPED", "PENDING", "STOPPED"
    ]
    crCount: int
    deploymentState: ConfigManagementConfigSyncDeploymentState
    errors: _list[ConfigManagementConfigSyncError]
    reposyncCrd: typing.Literal[
        "CRD_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLED",
        "TERMINATING",
        "INSTALLING",
    ]
    rootsyncCrd: typing.Literal[
        "CRD_STATE_UNSPECIFIED",
        "NOT_INSTALLED",
        "INSTALLED",
        "TERMINATING",
        "INSTALLING",
    ]
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CONFIG_SYNC_NOT_INSTALLED",
        "CONFIG_SYNC_INSTALLED",
        "CONFIG_SYNC_ERROR",
        "CONFIG_SYNC_PENDING",
    ]
    syncState: ConfigManagementSyncState
    version: ConfigManagementConfigSyncVersion

@typing.type_check_only
class ConfigManagementConfigSyncVersion(typing.TypedDict, total=False):
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
class ConfigManagementContainerOverride(typing.TypedDict, total=False):
    containerName: str
    cpuLimit: str
    cpuRequest: str
    memoryLimit: str
    memoryRequest: str

@typing.type_check_only
class ConfigManagementDeploymentOverride(typing.TypedDict, total=False):
    containers: _list[ConfigManagementContainerOverride]
    deploymentName: str
    deploymentNamespace: str

@typing.type_check_only
class ConfigManagementErrorResource(typing.TypedDict, total=False):
    resourceGvk: ConfigManagementGroupVersionKind
    resourceName: str
    resourceNamespace: str
    sourcePath: str

@typing.type_check_only
class ConfigManagementGatekeeperDeploymentState(typing.TypedDict, total=False):
    gatekeeperAudit: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gatekeeperControllerManagerState: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    gatekeeperMutation: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementGitConfig(typing.TypedDict, total=False):
    gcpServiceAccountEmail: str
    httpsProxy: str
    policyDir: str
    secretType: str
    syncBranch: str
    syncRepo: str
    syncRev: str
    syncWaitSecs: str

@typing.type_check_only
class ConfigManagementGroupVersionKind(typing.TypedDict, total=False):
    group: str
    kind: str
    version: str

@typing.type_check_only
class ConfigManagementHierarchyControllerConfig(typing.TypedDict, total=False):
    enableHierarchicalResourceQuota: bool
    enablePodTreeLabels: bool
    enabled: bool

@typing.type_check_only
class ConfigManagementHierarchyControllerDeploymentState(typing.TypedDict, total=False):
    extension: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    hnc: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]

@typing.type_check_only
class ConfigManagementHierarchyControllerState(typing.TypedDict, total=False):
    state: ConfigManagementHierarchyControllerDeploymentState
    version: ConfigManagementHierarchyControllerVersion

@typing.type_check_only
class ConfigManagementHierarchyControllerVersion(typing.TypedDict, total=False):
    extension: str
    hnc: str

@typing.type_check_only
class ConfigManagementInstallError(typing.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class ConfigManagementMembershipSpec(typing.TypedDict, total=False):
    cluster: str
    configSync: ConfigManagementConfigSync
    hierarchyController: ConfigManagementHierarchyControllerConfig
    management: typing.Literal[
        "MANAGEMENT_UNSPECIFIED", "MANAGEMENT_AUTOMATIC", "MANAGEMENT_MANUAL"
    ]
    policyController: ConfigManagementPolicyController
    version: str

@typing.type_check_only
class ConfigManagementMembershipState(typing.TypedDict, total=False):
    clusterName: str
    configSyncState: ConfigManagementConfigSyncState
    hierarchyControllerState: ConfigManagementHierarchyControllerState
    kubernetesApiServerVersion: str
    membershipSpec: ConfigManagementMembershipSpec
    operatorState: ConfigManagementOperatorState
    policyControllerState: ConfigManagementPolicyControllerState

@typing.type_check_only
class ConfigManagementOciConfig(typing.TypedDict, total=False):
    gcpServiceAccountEmail: str
    policyDir: str
    secretType: str
    syncRepo: str
    syncWaitSecs: str

@typing.type_check_only
class ConfigManagementOperatorState(typing.TypedDict, total=False):
    deploymentState: typing.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR", "PENDING"
    ]
    errors: _list[ConfigManagementInstallError]
    version: str

@typing.type_check_only
class ConfigManagementPolicyController(typing.TypedDict, total=False):
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
class ConfigManagementPolicyControllerMigration(typing.TypedDict, total=False):
    copyTime: str
    stage: typing.Literal["STAGE_UNSPECIFIED", "ACM_MANAGED", "POCO_MANAGED"]

@typing.type_check_only
class ConfigManagementPolicyControllerMonitoring(typing.TypedDict, total=False):
    backends: _list[
        typing.Literal[
            "MONITORING_BACKEND_UNSPECIFIED", "PROMETHEUS", "CLOUD_MONITORING"
        ]
    ]

@typing.type_check_only
class ConfigManagementPolicyControllerState(typing.TypedDict, total=False):
    deploymentState: ConfigManagementGatekeeperDeploymentState
    migration: ConfigManagementPolicyControllerMigration
    version: ConfigManagementPolicyControllerVersion

@typing.type_check_only
class ConfigManagementPolicyControllerVersion(typing.TypedDict, total=False):
    version: str

@typing.type_check_only
class ConfigManagementSyncError(typing.TypedDict, total=False):
    code: str
    errorMessage: str
    errorResources: _list[ConfigManagementErrorResource]

@typing.type_check_only
class ConfigManagementSyncState(typing.TypedDict, total=False):
    code: typing.Literal[
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
class ConnectAgentResource(typing.TypedDict, total=False):
    manifest: str
    type: TypeMeta

@typing.type_check_only
class DataplaneV2FeatureSpec(typing.TypedDict, total=False):
    enableEncryption: bool

@typing.type_check_only
class DefaultClusterConfig(typing.TypedDict, total=False):
    binaryAuthorizationConfig: BinaryAuthorizationConfig
    compliancePostureConfig: CompliancePostureConfig
    securityPostureConfig: SecurityPostureConfig

@typing.type_check_only
class EdgeCluster(typing.TypedDict, total=False):
    resourceLink: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feature(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    fleetDefaultMemberConfig: CommonFleetDefaultMemberConfigSpec
    labels: dict[str, typing.Any]
    membershipSpecs: dict[str, typing.Any]
    membershipStates: dict[str, typing.Any]
    name: str
    resourceState: FeatureResourceState
    scopeSpecs: dict[str, typing.Any]
    scopeStates: dict[str, typing.Any]
    spec: CommonFeatureSpec
    state: CommonFeatureState
    unreachable: _list[str]
    updateTime: str

@typing.type_check_only
class FeatureResourceState(typing.TypedDict, total=False):
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "ENABLING",
        "ACTIVE",
        "DISABLING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class FeatureState(typing.TypedDict, total=False):
    code: typing.Literal["CODE_UNSPECIFIED", "OK", "WARNING", "ERROR"]
    description: str
    updateTime: str

@typing.type_check_only
class Fleet(typing.TypedDict, total=False):
    createTime: str
    defaultClusterConfig: DefaultClusterConfig
    deleteTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    state: FleetLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class FleetLifecycleState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class FleetObservabilityFeatureError(typing.TypedDict, total=False):
    code: str
    description: str

@typing.type_check_only
class FleetObservabilityFeatureSpec(typing.TypedDict, total=False):
    loggingConfig: FleetObservabilityLoggingConfig

@typing.type_check_only
class FleetObservabilityFeatureState(typing.TypedDict, total=False):
    logging: FleetObservabilityFleetObservabilityLoggingState
    monitoring: FleetObservabilityFleetObservabilityMonitoringState

@typing.type_check_only
class FleetObservabilityFleetObservabilityBaseFeatureState(
    typing.TypedDict, total=False
):
    code: typing.Literal["CODE_UNSPECIFIED", "OK", "ERROR"]
    errors: _list[FleetObservabilityFeatureError]

@typing.type_check_only
class FleetObservabilityFleetObservabilityLoggingState(typing.TypedDict, total=False):
    defaultLog: FleetObservabilityFleetObservabilityBaseFeatureState
    scopeLog: FleetObservabilityFleetObservabilityBaseFeatureState

@typing.type_check_only
class FleetObservabilityFleetObservabilityMonitoringState(
    typing.TypedDict, total=False
):
    state: FleetObservabilityFleetObservabilityBaseFeatureState

@typing.type_check_only
class FleetObservabilityLoggingConfig(typing.TypedDict, total=False):
    defaultConfig: FleetObservabilityRoutingConfig
    fleetScopeLogsConfig: FleetObservabilityRoutingConfig

@typing.type_check_only
class FleetObservabilityMembershipSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityMembershipState(typing.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityRoutingConfig(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "COPY", "MOVE"]

@typing.type_check_only
class ForceCompleteRolloutStageRequest(typing.TypedDict, total=False):
    stageNumber: int

@typing.type_check_only
class GenerateConnectManifestResponse(typing.TypedDict, total=False):
    manifest: _list[ConnectAgentResource]

@typing.type_check_only
class GenerateMembershipRBACRoleBindingYAMLResponse(typing.TypedDict, total=False):
    roleBindingsYaml: str

@typing.type_check_only
class GkeCluster(typing.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class IdentityServiceAuthMethod(typing.TypedDict, total=False):
    azureadConfig: IdentityServiceAzureADConfig
    googleConfig: IdentityServiceGoogleConfig
    ldapConfig: IdentityServiceLdapConfig
    name: str
    oidcConfig: IdentityServiceOidcConfig
    proxy: str
    samlConfig: IdentityServiceSamlConfig

@typing.type_check_only
class IdentityServiceAzureADConfig(typing.TypedDict, total=False):
    clientId: str
    clientSecret: str
    encryptedClientSecret: str
    groupFormat: str
    kubectlRedirectUri: str
    tenant: str
    userClaim: str

@typing.type_check_only
class IdentityServiceDiagnosticInterface(typing.TypedDict, total=False):
    enabled: bool
    expirationTime: str

@typing.type_check_only
class IdentityServiceGoogleConfig(typing.TypedDict, total=False):
    disable: bool

@typing.type_check_only
class IdentityServiceGroupConfig(typing.TypedDict, total=False):
    baseDn: str
    filter: str
    idAttribute: str

@typing.type_check_only
class IdentityServiceIdentityServiceOptions(typing.TypedDict, total=False):
    diagnosticInterface: IdentityServiceDiagnosticInterface
    sessionDuration: str

@typing.type_check_only
class IdentityServiceLdapConfig(typing.TypedDict, total=False):
    group: IdentityServiceGroupConfig
    server: IdentityServiceServerConfig
    serviceAccount: IdentityServiceServiceAccountConfig
    user: IdentityServiceUserConfig

@typing.type_check_only
class IdentityServiceMembershipSpec(typing.TypedDict, total=False):
    authMethods: _list[IdentityServiceAuthMethod]
    identityServiceOptions: IdentityServiceIdentityServiceOptions

@typing.type_check_only
class IdentityServiceMembershipState(typing.TypedDict, total=False):
    failureReason: str
    installedVersion: str
    memberConfig: IdentityServiceMembershipSpec
    state: typing.Literal["DEPLOYMENT_STATE_UNSPECIFIED", "OK", "ERROR"]

@typing.type_check_only
class IdentityServiceOidcConfig(typing.TypedDict, total=False):
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
class IdentityServiceSamlConfig(typing.TypedDict, total=False):
    attributeMapping: dict[str, typing.Any]
    groupPrefix: str
    groupsAttribute: str
    identityProviderCertificates: _list[str]
    identityProviderId: str
    identityProviderSsoUri: str
    userAttribute: str
    userPrefix: str

@typing.type_check_only
class IdentityServiceServerConfig(typing.TypedDict, total=False):
    certificateAuthorityData: str
    connectionType: str
    host: str

@typing.type_check_only
class IdentityServiceServiceAccountConfig(typing.TypedDict, total=False):
    simpleBindCredentials: IdentityServiceSimpleBindCredentials

@typing.type_check_only
class IdentityServiceSimpleBindCredentials(typing.TypedDict, total=False):
    dn: str
    encryptedPassword: str
    password: str

@typing.type_check_only
class IdentityServiceUserConfig(typing.TypedDict, total=False):
    baseDn: str
    filter: str
    idAttribute: str
    loginAttribute: str

@typing.type_check_only
class KubernetesMetadata(typing.TypedDict, total=False):
    kubernetesApiServerVersion: str
    memoryMb: int
    nodeCount: int
    nodeProviderId: str
    updateTime: str
    vcpuCount: int

@typing.type_check_only
class KubernetesResource(typing.TypedDict, total=False):
    connectResources: _list[ResourceManifest]
    membershipCrManifest: str
    membershipResources: _list[ResourceManifest]
    resourceOptions: ResourceOptions

@typing.type_check_only
class ListBoundMembershipsResponse(typing.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFeaturesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Feature]

@typing.type_check_only
class ListFleetsResponse(typing.TypedDict, total=False):
    fleets: _list[Fleet]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipBindingsResponse(typing.TypedDict, total=False):
    membershipBindings: _list[MembershipBinding]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMembershipRBACRoleBindingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rbacrolebindings: _list[RBACRoleBinding]
    unreachable: _list[str]

@typing.type_check_only
class ListMembershipsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Membership]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListPermittedScopesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scopes: _list[Scope]

@typing.type_check_only
class ListRolloutSequencesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rolloutSequences: _list[RolloutSequence]

@typing.type_check_only
class ListRolloutsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rollouts: _list[Rollout]

@typing.type_check_only
class ListScopeNamespacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scopeNamespaces: _list[Namespace]

@typing.type_check_only
class ListScopeRBACRoleBindingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rbacrolebindings: _list[RBACRoleBinding]

@typing.type_check_only
class ListScopesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    scopes: _list[Scope]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Membership(typing.TypedDict, total=False):
    authority: Authority
    clusterTier: typing.Literal["CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"]
    createTime: str
    deleteTime: str
    description: str
    endpoint: MembershipEndpoint
    externalId: str
    labels: dict[str, typing.Any]
    lastConnectionTime: str
    membershipType: typing.Literal["MEMBERSHIP_TYPE_UNSPECIFIED", "LIGHTWEIGHT"]
    monitoringConfig: MonitoringConfig
    name: str
    state: MembershipState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MembershipBinding(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    name: str
    scope: str
    state: MembershipBindingLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class MembershipBindingLifecycleState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class MembershipEndpoint(typing.TypedDict, total=False):
    applianceCluster: ApplianceCluster
    edgeCluster: EdgeCluster
    gkeCluster: GkeCluster
    googleManaged: bool
    kubernetesMetadata: KubernetesMetadata
    kubernetesResource: KubernetesResource
    multiCloudCluster: MultiCloudCluster
    onPremCluster: OnPremCluster

@typing.type_check_only
class MembershipFeatureSpec(typing.TypedDict, total=False):
    configmanagement: ConfigManagementMembershipSpec
    fleetobservability: FleetObservabilityMembershipSpec
    identityservice: IdentityServiceMembershipSpec
    mesh: ServiceMeshMembershipSpec
    origin: Origin
    policycontroller: PolicyControllerMembershipSpec

@typing.type_check_only
class MembershipFeatureState(typing.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
    clusterupgrade: ClusterUpgradeMembershipState
    configmanagement: ConfigManagementMembershipState
    fleetobservability: FleetObservabilityMembershipState
    identityservice: IdentityServiceMembershipState
    policycontroller: PolicyControllerMembershipState
    servicemesh: ServiceMeshMembershipState
    state: FeatureState
    workloadidentity: WorkloadIdentityMembershipState

@typing.type_check_only
class MembershipState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "CREATING",
        "READY",
        "DELETING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class MonitoringConfig(typing.TypedDict, total=False):
    cluster: str
    clusterHash: str
    kubernetesMetricsPrefix: str
    location: str
    projectId: str

@typing.type_check_only
class MultiCloudCluster(typing.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class MultiClusterIngressFeatureSpec(typing.TypedDict, total=False):
    configMembership: str

@typing.type_check_only
class Namespace(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    name: str
    namespaceLabels: dict[str, typing.Any]
    scope: str
    state: NamespaceLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class NamespaceLifecycleState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class OnPremCluster(typing.TypedDict, total=False):
    adminCluster: bool
    clusterMissing: bool
    clusterType: typing.Literal[
        "CLUSTERTYPE_UNSPECIFIED", "BOOTSTRAP", "HYBRID", "STANDALONE", "USER"
    ]
    resourceLink: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class OperationalState(typing.TypedDict, total=False):
    reasons: _list[
        typing.Literal[
            "REASON_UNSPECIFIED",
            "FLEET_FEATURE_DELETED_ERROR",
            "FLEET_DELETED_ERROR",
            "EMPTY_STAGE_WARNING",
            "MIXED_RELEASE_CHANNELS_WARNING",
            "INTERNAL_ERROR",
            "NO_CLUSTERS_IN_SEQUENCE",
        ]
    ]
    state: typing.Literal[
        "STATE_CODE_UNSPECIFIED", "ACTIVE", "WARNING", "ERROR", "INITIALIZING"
    ]
    stateChangeTime: str

@typing.type_check_only
class Origin(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "FLEET", "FLEET_OUT_OF_SYNC", "USER"]

@typing.type_check_only
class PauseRolloutRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyBinding(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class PolicyControllerBundleInstallSpec(typing.TypedDict, total=False):
    exemptedNamespaces: _list[str]

@typing.type_check_only
class PolicyControllerHubConfig(typing.TypedDict, total=False):
    auditIntervalSeconds: str
    constraintViolationLimit: str
    deploymentConfigs: dict[str, typing.Any]
    exemptableNamespaces: _list[str]
    installSpec: typing.Literal[
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
class PolicyControllerMembershipSpec(typing.TypedDict, total=False):
    policyControllerHubConfig: PolicyControllerHubConfig
    version: str

@typing.type_check_only
class PolicyControllerMembershipState(typing.TypedDict, total=False):
    componentStates: dict[str, typing.Any]
    policyContentState: PolicyControllerPolicyContentState
    state: typing.Literal[
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
class PolicyControllerMonitoringConfig(typing.TypedDict, total=False):
    backends: _list[
        typing.Literal[
            "MONITORING_BACKEND_UNSPECIFIED", "PROMETHEUS", "CLOUD_MONITORING"
        ]
    ]

@typing.type_check_only
class PolicyControllerOnClusterState(typing.TypedDict, total=False):
    details: str
    state: typing.Literal[
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
class PolicyControllerPolicyContentSpec(typing.TypedDict, total=False):
    bundles: dict[str, typing.Any]
    templateLibrary: PolicyControllerTemplateLibraryConfig

@typing.type_check_only
class PolicyControllerPolicyContentState(typing.TypedDict, total=False):
    bundleStates: dict[str, typing.Any]
    referentialSyncConfigState: PolicyControllerOnClusterState
    templateLibraryState: PolicyControllerOnClusterState

@typing.type_check_only
class PolicyControllerPolicyControllerDeploymentConfig(typing.TypedDict, total=False):
    containerResources: PolicyControllerResourceRequirements
    podAffinity: typing.Literal["AFFINITY_UNSPECIFIED", "NO_AFFINITY", "ANTI_AFFINITY"]
    podAntiAffinity: bool
    podTolerations: _list[PolicyControllerToleration]
    replicaCount: str

@typing.type_check_only
class PolicyControllerResourceList(typing.TypedDict, total=False):
    cpu: str
    memory: str

@typing.type_check_only
class PolicyControllerResourceRequirements(typing.TypedDict, total=False):
    limits: PolicyControllerResourceList
    requests: PolicyControllerResourceList

@typing.type_check_only
class PolicyControllerTemplateLibraryConfig(typing.TypedDict, total=False):
    installation: typing.Literal["INSTALLATION_UNSPECIFIED", "NOT_INSTALLED", "ALL"]

@typing.type_check_only
class PolicyControllerToleration(typing.TypedDict, total=False):
    effect: str
    key: str
    operator: str
    value: str

@typing.type_check_only
class RBACRoleBinding(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    group: str
    labels: dict[str, typing.Any]
    name: str
    role: Role
    state: RBACRoleBindingLifecycleState
    uid: str
    updateTime: str
    user: str

@typing.type_check_only
class RBACRoleBindingActuationFeatureSpec(typing.TypedDict, total=False):
    allowedCustomRoles: _list[str]

@typing.type_check_only
class RBACRoleBindingActuationFeatureState(typing.TypedDict, total=False): ...

@typing.type_check_only
class RBACRoleBindingLifecycleState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class ResourceManifest(typing.TypedDict, total=False):
    clusterScoped: bool
    manifest: str

@typing.type_check_only
class ResourceOptions(typing.TypedDict, total=False):
    connectVersion: str
    k8sGitVersion: str
    k8sVersion: str
    v1beta1Crd: bool

@typing.type_check_only
class ResumeRolloutRequest(typing.TypedDict, total=False):
    scheduleOffset: str
    validateOnly: bool

@typing.type_check_only
class Role(typing.TypedDict, total=False):
    customRole: str
    predefinedRole: typing.Literal["UNKNOWN", "ADMIN", "EDIT", "VIEW", "ANTHOS_SUPPORT"]

@typing.type_check_only
class Rollout(typing.TypedDict, total=False):
    completeTime: str
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    intent: typing.Literal[
        "ROLLOUT_INTENT_UNSPECIFIED",
        "REGULAR_UPGRADE",
        "CONTROL_PLANE_PATCH_ENFORCEMENT",
        "END_OF_SUPPORT_ENFORCEMENT",
    ]
    labels: dict[str, typing.Any]
    membershipStates: dict[str, typing.Any]
    name: str
    rolloutSequence: str
    stages: _list[RolloutStage]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "PAUSED", "CANCELLED", "COMPLETED"
    ]
    stateReason: str
    stateReasonType: typing.Literal[
        "STATE_REASON_TYPE_UNSPECIFIED",
        "PAUSED_BY_USER",
        "PAUSED_BY_SYSTEM_CONFIG",
        "PAUSED_WAITING_FOR_NEXT_STAGE",
        "CANCELLED_BY_USER",
        "CANCELLED_PAUSED_TOO_LONG",
        "CANCELLED_SUPERSEDED",
        "CANCELLED_INCOMPATIBLE_ROLLOUT_SEQUENCE",
        "CANCELLED_SUPERSEDED_BY_USER_ROLLOUT",
    ]
    trigger: typing.Literal["ROLLOUT_TRIGGER_UNSPECIFIED", "USER", "GKE"]
    uid: str
    updateTime: str
    versionUpgrade: VersionUpgrade

@typing.type_check_only
class RolloutCreationScope(typing.TypedDict, total=False):
    upgradeTypes: _list[
        typing.Literal[
            "UPGRADE_TYPE_UNSPECIFIED",
            "CONTROL_PLANE_MINOR",
            "CONTROL_PLANE_PATCH",
            "NODE_MINOR",
            "NODE_PATCH",
        ]
    ]

@typing.type_check_only
class RolloutMembershipState(typing.TypedDict, total=False):
    lastUpdateTime: str
    stageAssignment: int
    targets: _list[RolloutTarget]

@typing.type_check_only
class RolloutSequence(typing.TypedDict, total=False):
    autoUpgradeConfig: AutoUpgradeConfig
    computedReleaseChannel: typing.Literal[
        "GKE_RELEASE_CHANNEL_UNSPECIFIED",
        "RAPID",
        "REGULAR",
        "STABLE",
        "EXTENDED",
        "NO_CHANNEL",
    ]
    createTime: str
    deleteTime: str
    displayName: str
    effectiveAutoUpgradeConfig: AutoUpgradeConfig
    etag: str
    ignoredClustersSelector: ClusterSelector
    labels: dict[str, typing.Any]
    lastQualifiedControlPlaneVersion: str
    lastQualifiedNodeVersion: str
    name: str
    operationalState: OperationalState
    stages: _list[Stage]
    targetControlPlaneVersion: str
    targetNodeVersion: str
    uid: str
    updateTime: str

@typing.type_check_only
class RolloutStage(typing.TypedDict, total=False):
    clusterSelector: ClusterSelector
    endTime: str
    fleetProjects: _list[str]
    soakDuration: str
    stageNumber: int
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SOAKING", "COMPLETED", "PAUSED"
    ]

@typing.type_check_only
class RolloutTarget(typing.TypedDict, total=False):
    cluster: str
    nodePool: str
    operation: str
    reason: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "FAILED",
        "SUCCEEDED",
        "PAUSED",
        "REMOVED",
        "INELIGIBLE",
        "SKIPPED",
    ]

@typing.type_check_only
class Scope(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    name: str
    namespaceLabels: dict[str, typing.Any]
    state: ScopeLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class ScopeFeatureSpec(typing.TypedDict, total=False): ...

@typing.type_check_only
class ScopeFeatureState(typing.TypedDict, total=False):
    state: FeatureState

@typing.type_check_only
class ScopeLifecycleState(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class SecurityPostureConfig(typing.TypedDict, total=False):
    mode: typing.Literal["MODE_UNSPECIFIED", "DISABLED", "BASIC", "ENTERPRISE"]
    vulnerabilityMode: typing.Literal[
        "VULNERABILITY_MODE_UNSPECIFIED",
        "VULNERABILITY_DISABLED",
        "VULNERABILITY_BASIC",
        "VULNERABILITY_ENTERPRISE",
    ]

@typing.type_check_only
class ServiceMeshCondition(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "MESH_IAM_PERMISSION_DENIED",
        "MESH_IAM_CROSS_PROJECT_PERMISSION_DENIED",
        "CNI_CONFIG_UNSUPPORTED",
        "GKE_SANDBOX_UNSUPPORTED",
        "NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED",
        "CNI_INSTALLATION_FAILED",
        "CNI_POD_UNSCHEDULABLE",
        "CLUSTER_HAS_ZERO_NODES",
        "CANONICAL_SERVICE_ERROR",
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
        "CONFIG_APPLY_BLOCKED",
        "LEGACY_MC_SECRETS",
        "WORKLOAD_IDENTITY_REQUIRED",
        "NON_STANDARD_BINARY_USAGE",
        "UNSUPPORTED_GATEWAY_CLASS",
        "MANAGED_CNI_NOT_ENABLED",
        "MISSING_CONTROL_PLANE_CONFIG",
        "SHARED_VPC_MISSING_PERMISSIONS",
        "REQUIRED_ORG_POLICY_DISABLED",
        "MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION",
        "MODERNIZATION_INCOMPATIBLE_CONFIG",
        "MODERNIZATION_INCOMPATIBLE_GATEWAY_POD_SCALE",
        "MODERNIZATION_SCHEDULED",
        "MODERNIZATION_IN_PROGRESS",
        "MODERNIZATION_COMPLETED",
        "MODERNIZATION_ABORTED",
        "MODERNIZATION_PREPARING",
        "MODERNIZATION_STALLED",
        "MODERNIZATION_PREPARED",
        "MODERNIZATION_MIGRATING_WORKLOADS",
        "MODERNIZATION_ROLLING_BACK_CLUSTER",
        "MODERNIZATION_WILL_BE_SCHEDULED",
        "MODERNIZATION_MANUAL",
        "MODERNIZATION_ELIGIBLE",
        "MODERNIZATION_MODERNIZING",
        "MODERNIZATION_MODERNIZED_SOAKING",
        "MODERNIZATION_FINALIZED",
        "MODERNIZATION_ROLLING_BACK_FLEET",
        "MODERNIZATION_MODERNIZED",
        "MODERNIZATION_COMPATIBLE",
        "MODERNIZATION_INCOMPATIBLE",
        "MODERNIZATION_INCOMPATIBLE_FLEET_SCALE",
        "MODERNIZATION_INCOMPATIBLE_FLEET_QUOTA",
    ]
    details: str
    documentationLink: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"]

@typing.type_check_only
class ServiceMeshControlPlaneManagement(typing.TypedDict, total=False):
    details: _list[ServiceMeshStatusDetails]
    implementation: typing.Literal[
        "IMPLEMENTATION_UNSPECIFIED", "ISTIOD", "TRAFFIC_DIRECTOR", "UPDATING"
    ]
    state: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "DISABLED",
        "FAILED_PRECONDITION",
        "PROVISIONING",
        "ACTIVE",
        "STALLED",
        "NEEDS_ATTENTION",
        "DEGRADED",
        "DEPROVISIONING",
    ]

@typing.type_check_only
class ServiceMeshDataPlaneManagement(typing.TypedDict, total=False):
    details: _list[ServiceMeshStatusDetails]
    state: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED",
        "DISABLED",
        "FAILED_PRECONDITION",
        "PROVISIONING",
        "ACTIVE",
        "STALLED",
        "NEEDS_ATTENTION",
        "DEGRADED",
        "DEPROVISIONING",
    ]

@typing.type_check_only
class ServiceMeshFeatureCondition(typing.TypedDict, total=False):
    code: typing.Literal[
        "CODE_UNSPECIFIED",
        "MESH_IAM_PERMISSION_DENIED",
        "MESH_IAM_CROSS_PROJECT_PERMISSION_DENIED",
        "CNI_CONFIG_UNSUPPORTED",
        "GKE_SANDBOX_UNSUPPORTED",
        "NODEPOOL_WORKLOAD_IDENTITY_FEDERATION_REQUIRED",
        "CNI_INSTALLATION_FAILED",
        "CNI_POD_UNSCHEDULABLE",
        "CLUSTER_HAS_ZERO_NODES",
        "CANONICAL_SERVICE_ERROR",
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
        "CONFIG_APPLY_BLOCKED",
        "LEGACY_MC_SECRETS",
        "WORKLOAD_IDENTITY_REQUIRED",
        "NON_STANDARD_BINARY_USAGE",
        "UNSUPPORTED_GATEWAY_CLASS",
        "MANAGED_CNI_NOT_ENABLED",
        "MISSING_CONTROL_PLANE_CONFIG",
        "SHARED_VPC_MISSING_PERMISSIONS",
        "REQUIRED_ORG_POLICY_DISABLED",
        "MODERNIZATION_INCOMPATIBLE_POD_ANNOTATION",
        "MODERNIZATION_INCOMPATIBLE_CONFIG",
        "MODERNIZATION_INCOMPATIBLE_GATEWAY_POD_SCALE",
        "MODERNIZATION_SCHEDULED",
        "MODERNIZATION_IN_PROGRESS",
        "MODERNIZATION_COMPLETED",
        "MODERNIZATION_ABORTED",
        "MODERNIZATION_PREPARING",
        "MODERNIZATION_STALLED",
        "MODERNIZATION_PREPARED",
        "MODERNIZATION_MIGRATING_WORKLOADS",
        "MODERNIZATION_ROLLING_BACK_CLUSTER",
        "MODERNIZATION_WILL_BE_SCHEDULED",
        "MODERNIZATION_MANUAL",
        "MODERNIZATION_ELIGIBLE",
        "MODERNIZATION_MODERNIZING",
        "MODERNIZATION_MODERNIZED_SOAKING",
        "MODERNIZATION_FINALIZED",
        "MODERNIZATION_ROLLING_BACK_FLEET",
        "MODERNIZATION_MODERNIZED",
        "MODERNIZATION_COMPATIBLE",
        "MODERNIZATION_INCOMPATIBLE",
        "MODERNIZATION_INCOMPATIBLE_FLEET_SCALE",
        "MODERNIZATION_INCOMPATIBLE_FLEET_QUOTA",
    ]
    details: str
    documentationLink: str
    severity: typing.Literal["SEVERITY_UNSPECIFIED", "ERROR", "WARNING", "INFO"]

@typing.type_check_only
class ServiceMeshFeatureSpec(typing.TypedDict, total=False):
    modernizationCompatibility: typing.Literal[
        "MODERNIZATION_COMPATIBILITY_UNSPECIFIED",
        "VALIDATION_ENABLED",
        "VALIDATION_DISABLED",
    ]
    modernizationStrategy: typing.Literal[
        "MODERNIZATION_STRATEGY_UNSPECIFIED", "AUTOMATIC", "DEFERRED"
    ]

@typing.type_check_only
class ServiceMeshFeatureState(typing.TypedDict, total=False):
    conditions: _list[ServiceMeshFeatureCondition]

@typing.type_check_only
class ServiceMeshMembershipSpec(typing.TypedDict, total=False):
    configApi: typing.Literal[
        "CONFIG_API_UNSPECIFIED", "CONFIG_API_ISTIO", "CONFIG_API_GATEWAY"
    ]
    controlPlane: typing.Literal[
        "CONTROL_PLANE_MANAGEMENT_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    management: typing.Literal[
        "MANAGEMENT_UNSPECIFIED",
        "MANAGEMENT_AUTOMATIC",
        "MANAGEMENT_MANUAL",
        "MANAGEMENT_NOT_INSTALLED",
    ]

@typing.type_check_only
class ServiceMeshMembershipState(typing.TypedDict, total=False):
    conditions: _list[ServiceMeshCondition]
    controlPlaneManagement: ServiceMeshControlPlaneManagement
    dataPlaneManagement: ServiceMeshDataPlaneManagement

@typing.type_check_only
class ServiceMeshStatusDetails(typing.TypedDict, total=False):
    code: str
    details: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Stage(typing.TypedDict, total=False):
    clusterSelector: ClusterSelector
    fleetProjects: _list[str]
    soakDuration: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: typing.Literal["CODE_UNSPECIFIED", "OK", "FAILED", "UNKNOWN"]
    description: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TypeMeta(typing.TypedDict, total=False):
    apiVersion: str
    kind: str

@typing.type_check_only
class UpgradeRolloutSequenceRequest(typing.TypedDict, total=False):
    force: bool
    upgradeType: typing.Literal["UPGRADE_TYPE_UNSPECIFIED", "CONTROL_PLANE", "NODE"]
    version: str

@typing.type_check_only
class VersionUpgrade(typing.TypedDict, total=False):
    desiredVersion: str
    type: typing.Literal["TYPE_UNSPECIFIED", "TYPE_CONTROL_PLANE", "TYPE_NODE_POOL"]

@typing.type_check_only
class WorkloadIdentityFeatureSpec(typing.TypedDict, total=False):
    scopeTenancyPool: str

@typing.type_check_only
class WorkloadIdentityFeatureState(typing.TypedDict, total=False):
    namespaceStateDetails: dict[str, typing.Any]
    namespaceStates: dict[str, typing.Any]
    scopeTenancyWorkloadIdentityPool: str
    workloadIdentityPool: str
    workloadIdentityPoolStateDetails: dict[str, typing.Any]

@typing.type_check_only
class WorkloadIdentityIdentityProviderStateDetail(typing.TypedDict, total=False):
    code: typing.Literal[
        "IDENTITY_PROVIDER_STATE_UNSPECIFIED",
        "IDENTITY_PROVIDER_STATE_OK",
        "IDENTITY_PROVIDER_STATE_ERROR",
    ]
    description: str

@typing.type_check_only
class WorkloadIdentityMembershipState(typing.TypedDict, total=False):
    description: str
    identityProviderStateDetails: dict[str, typing.Any]

@typing.type_check_only
class WorkloadIdentityNamespaceStateDetail(typing.TypedDict, total=False):
    code: typing.Literal[
        "NAMESPACE_STATE_UNSPECIFIED", "NAMESPACE_STATE_OK", "NAMESPACE_STATE_ERROR"
    ]
    description: str

@typing.type_check_only
class WorkloadIdentityWorkloadIdentityPoolStateDetail(typing.TypedDict, total=False):
    code: typing.Literal[
        "WORKLOAD_IDENTITY_POOL_STATE_UNSPECIFIED",
        "WORKLOAD_IDENTITY_POOL_STATE_OK",
        "WORKLOAD_IDENTITY_POOL_STATE_ERROR",
    ]
    description: str
