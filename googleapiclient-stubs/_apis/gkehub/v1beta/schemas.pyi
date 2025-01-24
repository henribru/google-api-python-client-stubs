import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnthosObservabilityFeatureSpec(typing_extensions.TypedDict, total=False):
    defaultMembershipSpec: AnthosObservabilityMembershipSpec

@typing.type_check_only
class AnthosObservabilityMembershipSpec(typing_extensions.TypedDict, total=False):
    doNotOptimizeMetrics: bool
    enableStackdriverOnApplications: bool
    version: str

@typing.type_check_only
class AppDevExperienceFeatureSpec(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AppDevExperienceFeatureState(typing_extensions.TypedDict, total=False):
    networkingInstallSucceeded: Status

@typing.type_check_only
class ApplianceCluster(typing_extensions.TypedDict, total=False):
    resourceLink: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Authority(typing_extensions.TypedDict, total=False):
    identityProvider: str
    issuer: str
    oidcJwks: str
    scopeTenancyIdentityProvider: str
    scopeTenancyWorkloadIdentityPool: str
    workloadIdentityPool: str

@typing.type_check_only
class BinaryAuthorizationConfig(typing_extensions.TypedDict, total=False):
    evaluationMode: typing_extensions.Literal[
        "EVALUATION_MODE_UNSPECIFIED", "DISABLED", "POLICY_BINDINGS"
    ]
    policyBindings: _list[PolicyBinding]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClusterUpgradeFleetSpec(typing_extensions.TypedDict, total=False):
    gkeUpgradeOverrides: _list[ClusterUpgradeGKEUpgradeOverride]
    postConditions: ClusterUpgradePostConditions
    upstreamFleets: _list[str]

@typing.type_check_only
class ClusterUpgradeFleetState(typing_extensions.TypedDict, total=False):
    downstreamFleets: _list[str]
    gkeState: ClusterUpgradeGKEUpgradeFeatureState
    ignored: dict[str, typing.Any]

@typing.type_check_only
class ClusterUpgradeGKEUpgrade(typing_extensions.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class ClusterUpgradeGKEUpgradeFeatureCondition(
    typing_extensions.TypedDict, total=False
):
    reason: str
    status: str
    type: str
    updateTime: str

@typing.type_check_only
class ClusterUpgradeGKEUpgradeFeatureState(typing_extensions.TypedDict, total=False):
    conditions: _list[ClusterUpgradeGKEUpgradeFeatureCondition]
    upgradeState: _list[ClusterUpgradeGKEUpgradeState]

@typing.type_check_only
class ClusterUpgradeGKEUpgradeOverride(typing_extensions.TypedDict, total=False):
    postConditions: ClusterUpgradePostConditions
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeGKEUpgradeState(typing_extensions.TypedDict, total=False):
    stats: dict[str, typing.Any]
    status: ClusterUpgradeUpgradeStatus
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeIgnoredMembership(typing_extensions.TypedDict, total=False):
    ignoredTime: str
    reason: str

@typing.type_check_only
class ClusterUpgradeMembershipGKEUpgradeState(typing_extensions.TypedDict, total=False):
    status: ClusterUpgradeUpgradeStatus
    upgrade: ClusterUpgradeGKEUpgrade

@typing.type_check_only
class ClusterUpgradeMembershipState(typing_extensions.TypedDict, total=False):
    ignored: ClusterUpgradeIgnoredMembership
    upgrades: _list[ClusterUpgradeMembershipGKEUpgradeState]

@typing.type_check_only
class ClusterUpgradePostConditions(typing_extensions.TypedDict, total=False):
    soaking: str

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
class CommonFeatureSpec(typing_extensions.TypedDict, total=False):
    anthosobservability: AnthosObservabilityFeatureSpec
    appdevexperience: AppDevExperienceFeatureSpec
    clusterupgrade: ClusterUpgradeFleetSpec
    dataplanev2: DataplaneV2FeatureSpec
    fleetobservability: FleetObservabilityFeatureSpec
    multiclusteringress: MultiClusterIngressFeatureSpec

@typing.type_check_only
class CommonFeatureState(typing_extensions.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
    clusterupgrade: ClusterUpgradeFleetState
    fleetobservability: FleetObservabilityFeatureState
    state: FeatureState

@typing.type_check_only
class CommonFleetDefaultMemberConfigSpec(typing_extensions.TypedDict, total=False):
    configmanagement: ConfigManagementMembershipSpec
    identityservice: IdentityServiceMembershipSpec
    mesh: ServiceMeshMembershipSpec
    policycontroller: PolicyControllerMembershipSpec

@typing.type_check_only
class CompliancePostureConfig(typing_extensions.TypedDict, total=False):
    complianceStandards: _list[ComplianceStandard]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "DISABLED", "ENABLED"]

@typing.type_check_only
class ComplianceStandard(typing_extensions.TypedDict, total=False):
    standard: str

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
class ConfigManagementMembershipSpec(typing_extensions.TypedDict, total=False):
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
class ConfigManagementMembershipState(typing_extensions.TypedDict, total=False):
    binauthzState: ConfigManagementBinauthzState
    clusterName: str
    configSyncState: ConfigManagementConfigSyncState
    hierarchyControllerState: ConfigManagementHierarchyControllerState
    membershipSpec: ConfigManagementMembershipSpec
    operatorState: ConfigManagementOperatorState
    policyControllerState: ConfigManagementPolicyControllerState

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
class ConnectAgentResource(typing_extensions.TypedDict, total=False):
    manifest: str
    type: TypeMeta

@typing.type_check_only
class DataplaneV2FeatureSpec(typing_extensions.TypedDict, total=False):
    enableEncryption: bool

@typing.type_check_only
class DefaultClusterConfig(typing_extensions.TypedDict, total=False):
    binaryAuthorizationConfig: BinaryAuthorizationConfig
    compliancePostureConfig: CompliancePostureConfig
    securityPostureConfig: SecurityPostureConfig

@typing.type_check_only
class EdgeCluster(typing_extensions.TypedDict, total=False):
    resourceLink: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feature(typing_extensions.TypedDict, total=False):
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
class FeatureResourceState(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "ENABLING",
        "ACTIVE",
        "DISABLING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class FeatureState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "OK", "WARNING", "ERROR"]
    description: str
    updateTime: str

@typing.type_check_only
class Fleet(typing_extensions.TypedDict, total=False):
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
class FleetLifecycleState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class FleetObservabilityFeatureError(typing_extensions.TypedDict, total=False):
    code: str
    description: str

@typing.type_check_only
class FleetObservabilityFeatureSpec(typing_extensions.TypedDict, total=False):
    loggingConfig: FleetObservabilityLoggingConfig

@typing.type_check_only
class FleetObservabilityFeatureState(typing_extensions.TypedDict, total=False):
    logging: FleetObservabilityFleetObservabilityLoggingState
    monitoring: FleetObservabilityFleetObservabilityMonitoringState

@typing.type_check_only
class FleetObservabilityFleetObservabilityBaseFeatureState(
    typing_extensions.TypedDict, total=False
):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "OK", "ERROR"]
    errors: _list[FleetObservabilityFeatureError]

@typing.type_check_only
class FleetObservabilityFleetObservabilityLoggingState(
    typing_extensions.TypedDict, total=False
):
    defaultLog: FleetObservabilityFleetObservabilityBaseFeatureState
    scopeLog: FleetObservabilityFleetObservabilityBaseFeatureState

@typing.type_check_only
class FleetObservabilityFleetObservabilityMonitoringState(
    typing_extensions.TypedDict, total=False
):
    state: FleetObservabilityFleetObservabilityBaseFeatureState

@typing.type_check_only
class FleetObservabilityLoggingConfig(typing_extensions.TypedDict, total=False):
    defaultConfig: FleetObservabilityRoutingConfig
    fleetScopeLogsConfig: FleetObservabilityRoutingConfig

@typing.type_check_only
class FleetObservabilityMembershipSpec(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityMembershipState(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityRoutingConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "COPY", "MOVE"]

@typing.type_check_only
class GenerateConnectManifestResponse(typing_extensions.TypedDict, total=False):
    manifest: _list[ConnectAgentResource]

@typing.type_check_only
class GenerateMembershipRBACRoleBindingYAMLResponse(
    typing_extensions.TypedDict, total=False
):
    roleBindingsYaml: str

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

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
class IdentityServiceMembershipSpec(typing_extensions.TypedDict, total=False):
    authMethods: _list[IdentityServiceAuthMethod]
    identityServiceOptions: IdentityServiceIdentityServiceOptions

@typing.type_check_only
class IdentityServiceMembershipState(typing_extensions.TypedDict, total=False):
    failureReason: str
    installedVersion: str
    memberConfig: IdentityServiceMembershipSpec
    state: typing_extensions.Literal["DEPLOYMENT_STATE_UNSPECIFIED", "OK", "ERROR"]

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
class IdentityServiceUserConfig(typing_extensions.TypedDict, total=False):
    baseDn: str
    filter: str
    idAttribute: str
    loginAttribute: str

@typing.type_check_only
class KubernetesMetadata(typing_extensions.TypedDict, total=False):
    kubernetesApiServerVersion: str
    memoryMb: int
    nodeCount: int
    nodeProviderId: str
    updateTime: str
    vcpuCount: int

@typing.type_check_only
class KubernetesResource(typing_extensions.TypedDict, total=False):
    connectResources: _list[ResourceManifest]
    membershipCrManifest: str
    membershipResources: _list[ResourceManifest]
    resourceOptions: ResourceOptions

@typing.type_check_only
class ListBoundMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListFeaturesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Feature]

@typing.type_check_only
class ListFleetsResponse(typing_extensions.TypedDict, total=False):
    fleets: _list[Fleet]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipBindingsResponse(typing_extensions.TypedDict, total=False):
    membershipBindings: _list[MembershipBinding]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListMembershipRBACRoleBindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rbacrolebindings: _list[RBACRoleBinding]
    unreachable: _list[str]

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Membership]
    unreachable: _list[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListPermittedScopesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scopes: _list[Scope]

@typing.type_check_only
class ListScopeNamespacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scopeNamespaces: _list[Namespace]

@typing.type_check_only
class ListScopeRBACRoleBindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rbacrolebindings: _list[RBACRoleBinding]

@typing.type_check_only
class ListScopesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    scopes: _list[Scope]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    authority: Authority
    clusterTier: typing_extensions.Literal[
        "CLUSTER_TIER_UNSPECIFIED", "STANDARD", "ENTERPRISE"
    ]
    createTime: str
    deleteTime: str
    description: str
    endpoint: MembershipEndpoint
    externalId: str
    labels: dict[str, typing.Any]
    lastConnectionTime: str
    monitoringConfig: MonitoringConfig
    name: str
    state: MembershipState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MembershipBinding(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    name: str
    scope: str
    state: MembershipBindingLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class MembershipBindingLifecycleState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class MembershipEndpoint(typing_extensions.TypedDict, total=False):
    applianceCluster: ApplianceCluster
    edgeCluster: EdgeCluster
    gkeCluster: GkeCluster
    googleManaged: bool
    kubernetesMetadata: KubernetesMetadata
    kubernetesResource: KubernetesResource
    multiCloudCluster: MultiCloudCluster
    onPremCluster: OnPremCluster

@typing.type_check_only
class MembershipFeatureSpec(typing_extensions.TypedDict, total=False):
    anthosobservability: AnthosObservabilityMembershipSpec
    cloudbuild: MembershipSpec
    configmanagement: ConfigManagementMembershipSpec
    fleetobservability: FleetObservabilityMembershipSpec
    identityservice: IdentityServiceMembershipSpec
    mesh: ServiceMeshMembershipSpec
    origin: Origin
    policycontroller: PolicyControllerMembershipSpec

@typing.type_check_only
class MembershipFeatureState(typing_extensions.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
    clusterupgrade: ClusterUpgradeMembershipState
    configmanagement: ConfigManagementMembershipState
    fleetobservability: FleetObservabilityMembershipState
    identityservice: IdentityServiceMembershipState
    metering: MeteringMembershipState
    policycontroller: PolicyControllerMembershipState
    servicemesh: ServiceMeshMembershipState
    state: FeatureState

@typing.type_check_only
class MembershipSpec(typing_extensions.TypedDict, total=False):
    securityPolicy: typing_extensions.Literal[
        "SECURITY_POLICY_UNSPECIFIED", "NON_PRIVILEGED", "PRIVILEGED"
    ]
    version: str

@typing.type_check_only
class MembershipState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "CREATING",
        "READY",
        "DELETING",
        "UPDATING",
        "SERVICE_UPDATING",
    ]

@typing.type_check_only
class MeteringMembershipState(typing_extensions.TypedDict, total=False):
    lastMeasurementTime: str
    preciseLastMeasuredClusterVcpuCapacity: float

@typing.type_check_only
class MonitoringConfig(typing_extensions.TypedDict, total=False):
    cluster: str
    clusterHash: str
    kubernetesMetricsPrefix: str
    location: str
    projectId: str

@typing.type_check_only
class MultiCloudCluster(typing_extensions.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class MultiClusterIngressFeatureSpec(typing_extensions.TypedDict, total=False):
    billing: typing_extensions.Literal[
        "BILLING_UNSPECIFIED", "PAY_AS_YOU_GO", "ANTHOS_LICENSE"
    ]
    configMembership: str

@typing.type_check_only
class Namespace(typing_extensions.TypedDict, total=False):
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
class NamespaceLifecycleState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class OnPremCluster(typing_extensions.TypedDict, total=False):
    adminCluster: bool
    clusterMissing: bool
    clusterType: typing_extensions.Literal[
        "CLUSTERTYPE_UNSPECIFIED", "BOOTSTRAP", "HYBRID", "STANDALONE", "USER"
    ]
    resourceLink: str

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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyBinding(typing_extensions.TypedDict, total=False):
    name: str

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
class PolicyControllerMembershipSpec(typing_extensions.TypedDict, total=False):
    policyControllerHubConfig: PolicyControllerHubConfig
    version: str

@typing.type_check_only
class PolicyControllerMembershipState(typing_extensions.TypedDict, total=False):
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
class RBACRoleBinding(typing_extensions.TypedDict, total=False):
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
class RBACRoleBindingLifecycleState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class ResourceManifest(typing_extensions.TypedDict, total=False):
    clusterScoped: bool
    manifest: str

@typing.type_check_only
class ResourceOptions(typing_extensions.TypedDict, total=False):
    connectVersion: str
    k8sVersion: str
    v1beta1Crd: bool

@typing.type_check_only
class Role(typing_extensions.TypedDict, total=False):
    predefinedRole: typing_extensions.Literal[
        "UNKNOWN", "ADMIN", "EDIT", "VIEW", "ANTHOS_SUPPORT"
    ]

@typing.type_check_only
class Scope(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    labels: dict[str, typing.Any]
    name: str
    namespaceLabels: dict[str, typing.Any]
    state: ScopeLifecycleState
    uid: str
    updateTime: str

@typing.type_check_only
class ScopeFeatureSpec(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ScopeFeatureState(typing_extensions.TypedDict, total=False):
    state: FeatureState

@typing.type_check_only
class ScopeLifecycleState(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "CREATING", "READY", "DELETING", "UPDATING"
    ]

@typing.type_check_only
class SecurityPostureConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "DISABLED", "BASIC", "ENTERPRISE"
    ]
    vulnerabilityMode: typing_extensions.Literal[
        "VULNERABILITY_MODE_UNSPECIFIED",
        "VULNERABILITY_DISABLED",
        "VULNERABILITY_BASIC",
        "VULNERABILITY_ENTERPRISE",
    ]

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
class ServiceMeshMembershipSpec(typing_extensions.TypedDict, total=False):
    configApi: typing_extensions.Literal[
        "CONFIG_API_UNSPECIFIED", "CONFIG_API_ISTIO", "CONFIG_API_GATEWAY"
    ]
    controlPlane: typing_extensions.Literal[
        "CONTROL_PLANE_MANAGEMENT_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    management: typing_extensions.Literal[
        "MANAGEMENT_UNSPECIFIED", "MANAGEMENT_AUTOMATIC", "MANAGEMENT_MANUAL"
    ]

@typing.type_check_only
class ServiceMeshMembershipState(typing_extensions.TypedDict, total=False):
    conditions: _list[ServiceMeshCondition]
    controlPlaneManagement: ServiceMeshControlPlaneManagement
    dataPlaneManagement: ServiceMeshDataPlaneManagement

@typing.type_check_only
class ServiceMeshStatusDetails(typing_extensions.TypedDict, total=False):
    code: str
    details: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal["CODE_UNSPECIFIED", "OK", "FAILED", "UNKNOWN"]
    description: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TypeMeta(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
