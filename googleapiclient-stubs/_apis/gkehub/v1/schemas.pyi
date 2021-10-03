import typing

import typing_extensions

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Authority(typing_extensions.TypedDict, total=False):
    identityProvider: str
    issuer: str
    oidcJwks: str
    workloadIdentityPool: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CommonFeatureSpec(typing_extensions.TypedDict, total=False):
    multiclusteringress: MultiClusterIngressFeatureSpec

@typing.type_check_only
class CommonFeatureState(typing_extensions.TypedDict, total=False):
    state: FeatureState

@typing.type_check_only
class ConfigManagementConfigSync(typing_extensions.TypedDict, total=False):
    git: ConfigManagementGitConfig
    resourceRequirements: typing.Dict[str, typing.Any]
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
class ConfigManagementContainerResourceRequirements(
    typing_extensions.TypedDict, total=False
):
    containerName: str
    cpuLimit: ConfigManagementQuantity
    memoryLimit: ConfigManagementQuantity

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

@typing.type_check_only
class ConfigManagementGitConfig(typing_extensions.TypedDict, total=False):
    gcpServiceAccountEmail: str
    httpsProxy: str
    noSslVerify: bool
    policyDir: str
    secretType: str
    syncBranch: str
    syncDepth: str
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
    configSync: ConfigManagementConfigSync
    hierarchyController: ConfigManagementHierarchyControllerConfig
    policyController: ConfigManagementPolicyController
    version: str

@typing.type_check_only
class ConfigManagementMembershipState(typing_extensions.TypedDict, total=False):
    clusterName: str
    configSyncState: ConfigManagementConfigSyncState
    hierarchyControllerState: ConfigManagementHierarchyControllerState
    membershipSpec: ConfigManagementMembershipSpec
    operatorState: ConfigManagementOperatorState
    policyControllerState: ConfigManagementPolicyControllerState

@typing.type_check_only
class ConfigManagementOperatorState(typing_extensions.TypedDict, total=False):
    deploymentState: typing_extensions.Literal[
        "DEPLOYMENT_STATE_UNSPECIFIED", "NOT_INSTALLED", "INSTALLED", "ERROR"
    ]
    errors: typing.List[ConfigManagementInstallError]
    version: str

@typing.type_check_only
class ConfigManagementPolicyController(typing_extensions.TypedDict, total=False):
    auditIntervalSeconds: str
    enabled: bool
    exemptableNamespaces: typing.List[str]
    logDeniesEnabled: bool
    referentialRulesEnabled: bool
    templateLibraryInstalled: bool

@typing.type_check_only
class ConfigManagementPolicyControllerState(typing_extensions.TypedDict, total=False):
    deploymentState: ConfigManagementGatekeeperDeploymentState
    version: ConfigManagementPolicyControllerVersion

@typing.type_check_only
class ConfigManagementPolicyControllerVersion(typing_extensions.TypedDict, total=False):
    version: str

@typing.type_check_only
class ConfigManagementQuantity(typing_extensions.TypedDict, total=False):
    string: str

@typing.type_check_only
class ConfigManagementSyncError(typing_extensions.TypedDict, total=False):
    code: str
    errorMessage: str
    errorResources: typing.List[ConfigManagementErrorResource]

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
    errors: typing.List[ConfigManagementSyncError]
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
    labels: typing.Dict[str, typing.Any]
    membershipSpecs: typing.Dict[str, typing.Any]
    membershipStates: typing.Dict[str, typing.Any]
    name: str
    resourceState: FeatureResourceState
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
class GenerateConnectManifestResponse(typing_extensions.TypedDict, total=False):
    manifest: typing.List[ConnectAgentResource]

@typing.type_check_only
class GkeCluster(typing_extensions.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class KubernetesMetadata(typing_extensions.TypedDict, total=False):
    kubernetesApiServerVersion: str
    memoryMb: int
    nodeCount: int
    nodeProviderId: str
    updateTime: str
    vcpuCount: int

@typing.type_check_only
class ListFeaturesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Feature]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Membership]
    unreachable: typing.List[str]

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    authority: Authority
    createTime: str
    deleteTime: str
    description: str
    endpoint: MembershipEndpoint
    externalId: str
    labels: typing.Dict[str, typing.Any]
    lastConnectionTime: str
    name: str
    state: MembershipState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MembershipEndpoint(typing_extensions.TypedDict, total=False):
    gkeCluster: GkeCluster
    kubernetesMetadata: KubernetesMetadata
    multiCloudCluster: MultiCloudCluster
    onPremCluster: OnPremCluster

@typing.type_check_only
class MembershipFeatureSpec(typing_extensions.TypedDict, total=False):
    configmanagement: ConfigManagementMembershipSpec

@typing.type_check_only
class MembershipFeatureState(typing_extensions.TypedDict, total=False):
    configmanagement: ConfigManagementMembershipState
    state: FeatureState

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
class MultiCloudCluster(typing_extensions.TypedDict, total=False):
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class MultiClusterIngressFeatureSpec(typing_extensions.TypedDict, total=False):
    configMembership: str

@typing.type_check_only
class OnPremCluster(typing_extensions.TypedDict, total=False):
    adminCluster: bool
    clusterMissing: bool
    resourceLink: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

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
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TypeMeta(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
