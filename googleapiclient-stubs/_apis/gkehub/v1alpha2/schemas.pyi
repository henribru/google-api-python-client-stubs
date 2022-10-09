import typing

import typing_extensions

_list = list

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
    workloadIdentityPool: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConnectAgentResource(typing_extensions.TypedDict, total=False):
    manifest: str
    type: TypeMeta

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
class GenerateConnectManifestResponse(typing_extensions.TypedDict, total=False):
    manifest: _list[ConnectAgentResource]

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
class InitializeHubRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InitializeHubResponse(typing_extensions.TypedDict, total=False):
    serviceIdentity: str
    workloadIdentityPool: str

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
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

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
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    authority: Authority
    createTime: str
    deleteTime: str
    description: str
    endpoint: MembershipEndpoint
    externalId: str
    infrastructureType: typing_extensions.Literal[
        "INFRASTRUCTURE_TYPE_UNSPECIFIED", "ON_PREM", "MULTI_CLOUD"
    ]
    labels: dict[str, typing.Any]
    lastConnectionTime: str
    name: str
    state: MembershipState
    uniqueId: str
    updateTime: str

@typing.type_check_only
class MembershipEndpoint(typing_extensions.TypedDict, total=False):
    applianceCluster: ApplianceCluster
    edgeCluster: EdgeCluster
    gkeCluster: GkeCluster
    kubernetesMetadata: KubernetesMetadata
    kubernetesResource: KubernetesResource
    multiCloudCluster: MultiCloudCluster
    onPremCluster: OnPremCluster

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
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

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
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

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
