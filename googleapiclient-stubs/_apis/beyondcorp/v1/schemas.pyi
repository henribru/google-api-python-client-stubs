import typing

import typing_extensions

_list = list

@typing.type_check_only
class AllocatedConnection(typing_extensions.TypedDict, total=False):
    ingressPort: int
    pscUri: str

@typing.type_check_only
class AppGateway(typing_extensions.TypedDict, total=False):
    allocatedConnections: _list[AllocatedConnection]
    createTime: str
    displayName: str
    hostType: typing_extensions.Literal["HOST_TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str
    uri: str

@typing.type_check_only
class AppGatewayOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ClientConnectorService(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    egress: Egress
    ingress: Ingress
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "RUNNING",
        "DOWN",
        "ERROR",
    ]
    updateTime: str

@typing.type_check_only
class ClientConnectorServiceOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ClientGateway(typing_extensions.TypedDict, total=False):
    clientConnectorService: str
    createTime: str
    id: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "UPDATING",
        "DELETING",
        "RUNNING",
        "DOWN",
        "ERROR",
    ]
    updateTime: str

@typing.type_check_only
class ClientGatewayOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig(
    typing_extensions.TypedDict, total=False
):
    applicationEndpoint: str
    applicationName: str
    gateway: _list[CloudSecurityZerotrustApplinkAppConnectorProtoGateway]
    name: str
    project: str
    tunnelsPerGateway: int
    userPort: int

@typing.type_check_only
class CloudSecurityZerotrustApplinkAppConnectorProtoConnectorDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class CloudSecurityZerotrustApplinkAppConnectorProtoGateway(
    typing_extensions.TypedDict, total=False
):
    interface: str
    name: str
    port: int
    project: str
    selfLink: str
    zone: str

@typing.type_check_only
class CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class Config(typing_extensions.TypedDict, total=False):
    destinationRoutes: _list[DestinationRoute]
    transportProtocol: typing_extensions.Literal[
        "TRANSPORT_PROTOCOL_UNSPECIFIED", "TCP"
    ]

@typing.type_check_only
class DestinationRoute(typing_extensions.TypedDict, total=False):
    address: str
    netmask: str

@typing.type_check_only
class Egress(typing_extensions.TypedDict, total=False):
    peeredVpc: PeeredVpc

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnection(
    typing_extensions.TypedDict, total=False
):
    applicationEndpoint: GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint(
    typing_extensions.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway(
    typing_extensions.TypedDict, total=False
):
    appGateway: str
    ingressPort: int
    l7psc: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ListAppConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnections: _list[GoogleCloudBeyondcorpAppconnectionsV1AppConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnectionDetails: _list[
        GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails
    ]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails(
    typing_extensions.TypedDict, total=False
):
    appConnection: GoogleCloudBeyondcorpAppconnectionsV1AppConnection
    recentMigVms: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnector(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig(
    typing_extensions.TypedDict, total=False
):
    imageConfig: GoogleCloudBeyondcorpAppconnectorsV1ImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig
    sequenceNumber: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo(
    typing_extensions.TypedDict, total=False
):
    serviceAccount: GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount(
    typing_extensions.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails(
    typing_extensions.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ImageConfig(
    typing_extensions.TypedDict, total=False
):
    stableImage: str
    targetImage: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnectors: _list[GoogleCloudBeyondcorpAppconnectorsV1AppConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig(
    typing_extensions.TypedDict, total=False
):
    pubsubNotification: GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig(
    typing_extensions.TypedDict, total=False
):
    pubsubSubscription: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo
    validateOnly: bool

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse(
    typing_extensions.TypedDict, total=False
):
    instanceConfig: GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails(
    typing_extensions.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpApplicationsV1alphaApplicationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpClientconnectorservicesV1alphaClientConnectorServiceOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpClientgatewaysV1alphaClientGatewayOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpConnectionsV1alphaConnectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpConnectorsV1alphaConnectorOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpConnectorsV1alphaContainerHealthDetails(
    typing_extensions.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnectionOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

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

@typing.type_check_only
class Ingress(typing_extensions.TypedDict, total=False):
    config: Config

@typing.type_check_only
class ListAppGatewaysResponse(typing_extensions.TypedDict, total=False):
    appGateways: _list[AppGateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClientConnectorServicesResponse(typing_extensions.TypedDict, total=False):
    clientConnectorServices: _list[ClientConnectorService]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListClientGatewaysResponse(typing_extensions.TypedDict, total=False):
    clientGateways: _list[ClientGateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class PeeredVpc(typing_extensions.TypedDict, total=False):
    networkVpc: str

@typing.type_check_only
class Tunnelv1ProtoTunnelerError(typing_extensions.TypedDict, total=False):
    err: str
    retryable: bool

@typing.type_check_only
class Tunnelv1ProtoTunnelerInfo(typing_extensions.TypedDict, total=False):
    backoffRetryCount: int
    id: str
    latestErr: Tunnelv1ProtoTunnelerError
    latestRetryTime: str
    totalRetryCount: int
