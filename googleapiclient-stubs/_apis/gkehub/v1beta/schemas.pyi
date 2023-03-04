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
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CommonFeatureSpec(typing_extensions.TypedDict, total=False):
    anthosobservability: AnthosObservabilityFeatureSpec
    appdevexperience: AppDevExperienceFeatureSpec
    fleetobservability: FleetObservabilityFeatureSpec
    multiclusteringress: MultiClusterIngressFeatureSpec

@typing.type_check_only
class CommonFeatureState(typing_extensions.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
    fleetobservability: FleetObservabilityFeatureState
    state: FeatureState

@typing.type_check_only
class CommonFleetDefaultMemberConfigSpec(typing_extensions.TypedDict, total=False):
    identityservice: IdentityServiceMembershipSpec

@typing.type_check_only
class ConfigManagementBinauthzConfig(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class ConfigManagementBinauthzState(typing_extensions.TypedDict, total=False):
    version: ConfigManagementBinauthzVersion
    webhook: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]

@typing.type_check_only
class ConfigManagementBinauthzVersion(typing_extensions.TypedDict, total=False):
    webhookVersion: str

@typing.type_check_only
class ConfigManagementConfigSync(typing_extensions.TypedDict, total=False):
    allowVerticalScale: bool
    enabled: bool
    git: ConfigManagementGitConfig
    oci: ConfigManagementOciConfig
    preventDrift: bool
    sourceFormat: str

@typing.type_check_only
class ConfigManagementConfigSyncDeploymentState(
    typing_extensions.TypedDict, total=False
):
    admissionWebhook: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    gitSync: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    importer: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    monitor: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    reconcilerManager: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    rootReconciler: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    syncer: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]

@typing.type_check_only
class ConfigManagementConfigSyncState(typing_extensions.TypedDict, total=False):
    deploymentState: ConfigManagementConfigSyncDeploymentState
    syncState: ConfigManagementSyncState
    version: ConfigManagementConfigSyncVersion

@typing.type_check_only
class ConfigManagementConfigSyncVersion(typing_extensions.TypedDict, total=False):
    admissionWebhook: str
    gitSync: str
    importer: str
    monitor: str
    reconcilerManager: str
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
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    gatekeeperControllerManagerState: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    gatekeeperMutation: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
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
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    hnc: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
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
    configSync: ConfigManagementConfigSync
    hierarchyController: ConfigManagementHierarchyControllerConfig
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
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
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

@typing.type_check_only
class ConfigManagementPolicyControllerMigration(
    typing_extensions.TypedDict, total=False
):
    stage: typing_extensions.Literal["STAGE_UNSPECIFIED", "ACM_MANAGED", "POCO_MANAGED"]

@typing.type_check_only
class ConfigManagementPolicyControllerMonitoring(
    typing_extensions.TypedDict, total=False
):
    backends: _list[str]

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
class FleetObservabilityFeatureSpec(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityFeatureState(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityMembershipSpec(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FleetObservabilityMembershipState(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class IdentityServiceAuthMethod(typing_extensions.TypedDict, total=False):
    azureadConfig: IdentityServiceAzureADConfig
    googleConfig: IdentityServiceGoogleConfig
    name: str
    oidcConfig: IdentityServiceOidcConfig
    proxy: str

@typing.type_check_only
class IdentityServiceAzureADConfig(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: str
    encryptedClientSecret: str
    kubectlRedirectUri: str
    tenant: str

@typing.type_check_only
class IdentityServiceGoogleConfig(typing_extensions.TypedDict, total=False):
    disable: bool

@typing.type_check_only
class IdentityServiceMembershipSpec(typing_extensions.TypedDict, total=False):
    authMethods: _list[IdentityServiceAuthMethod]

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
class ListFeaturesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Feature]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipBindingsResponse(typing_extensions.TypedDict, total=False):
    membershipBindings: _list[MembershipBinding]
    nextPageToken: str

@typing.type_check_only
class ListNamespacesResponse(typing_extensions.TypedDict, total=False):
    namespaces: _list[Namespace]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListRBACRoleBindingsResponse(typing_extensions.TypedDict, total=False):
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
class MembershipBinding(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    fleet: bool
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
class MembershipFeatureSpec(typing_extensions.TypedDict, total=False):
    anthosobservability: AnthosObservabilityMembershipSpec
    cloudbuild: MembershipSpec
    configmanagement: ConfigManagementMembershipSpec
    fleetInherited: bool
    fleetobservability: FleetObservabilityMembershipSpec
    identityservice: IdentityServiceMembershipSpec
    mesh: ServiceMeshMembershipSpec
    policycontroller: PolicyControllerMembershipSpec

@typing.type_check_only
class MembershipFeatureState(typing_extensions.TypedDict, total=False):
    appdevexperience: AppDevExperienceFeatureState
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
class MeteringMembershipState(typing_extensions.TypedDict, total=False):
    lastMeasurementTime: str
    preciseLastMeasuredClusterVcpuCapacity: float

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
    name: str
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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PolicyControllerBundleInstallSpec(typing_extensions.TypedDict, total=False):
    exemptedNamespaces: _list[str]
    management: typing_extensions.Literal["MANAGEMENT_UNSPECIFIED", "INSTALLED"]

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
    ]
    logDeniesEnabled: bool
    monitoring: PolicyControllerMonitoringConfig
    mutationEnabled: bool
    policyContent: PolicyControllerPolicyContentSpec
    referentialRulesEnabled: bool
    templateLibraryConfig: PolicyControllerTemplateLibraryConfig

@typing.type_check_only
class PolicyControllerMembershipSpec(typing_extensions.TypedDict, total=False):
    policyControllerHubConfig: PolicyControllerHubConfig
    version: str

@typing.type_check_only
class PolicyControllerMembershipState(typing_extensions.TypedDict, total=False):
    componentStates: dict[str, typing.Any]
    contentStates: dict[str, typing.Any]
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
    ]

@typing.type_check_only
class PolicyControllerMonitoringConfig(typing_extensions.TypedDict, total=False):
    backends: _list[str]

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
    ]

@typing.type_check_only
class PolicyControllerPolicyContentSpec(typing_extensions.TypedDict, total=False):
    bundles: dict[str, typing.Any]

@typing.type_check_only
class PolicyControllerPolicyControllerDeploymentConfig(
    typing_extensions.TypedDict, total=False
):
    containerResources: PolicyControllerResourceRequirements
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
    included: bool

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
class Role(typing_extensions.TypedDict, total=False):
    predefinedRole: typing_extensions.Literal["UNKNOWN", "ADMIN", "EDIT", "VIEW"]

@typing.type_check_only
class Scope(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    name: str
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
class ServiceMeshControlPlaneManagement(typing_extensions.TypedDict, total=False):
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
    controlPlane: typing_extensions.Literal[
        "CONTROL_PLANE_MANAGEMENT_UNSPECIFIED", "AUTOMATIC", "MANUAL"
    ]
    management: typing_extensions.Literal[
        "MANAGEMENT_UNSPECIFIED", "MANAGEMENT_AUTOMATIC", "MANAGEMENT_MANUAL"
    ]

@typing.type_check_only
class ServiceMeshMembershipState(typing_extensions.TypedDict, total=False):
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
