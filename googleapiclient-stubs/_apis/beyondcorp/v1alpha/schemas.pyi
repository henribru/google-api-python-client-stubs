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
class ApplicationEndpoint(typing_extensions.TypedDict, total=False):
    host: str
    port: int

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
class CloudPubSubNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubSubscription: str

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
class Connection(typing_extensions.TypedDict, total=False):
    applicationEndpoint: ApplicationEndpoint
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: Gateway
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str

@typing.type_check_only
class ConnectionDetails(typing_extensions.TypedDict, total=False):
    connection: Connection
    recentMigVms: _list[str]

@typing.type_check_only
class ConnectionOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Connector(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: PrincipalInfo
    resourceInfo: ResourceInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ConnectorInstanceConfig(typing_extensions.TypedDict, total=False):
    imageConfig: ImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: NotificationConfig
    sequenceNumber: str

@typing.type_check_only
class ConnectorOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ContainerHealthDetails(typing_extensions.TypedDict, total=False):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

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
class Gateway(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str
    userPort: int

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
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection(
    typing_extensions.TypedDict, total=False
):
    applicationEndpoint: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway
    labels: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint(
    typing_extensions.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway(
    typing_extensions.TypedDict, total=False
):
    appGateway: str
    ingressPort: int
    l7psc: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str

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
class GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnections: _list[GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnectionDetails: _list[
        GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails
    ]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails(
    typing_extensions.TypedDict, total=False
):
    appConnection: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection
    recentMigVms: _list[str]

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
class GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails(
    typing_extensions.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig(
    typing_extensions.TypedDict, total=False
):
    imageConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig
    sequenceNumber: str

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
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo(
    typing_extensions.TypedDict, total=False
):
    serviceAccount: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount(
    typing_extensions.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails(
    typing_extensions.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig(
    typing_extensions.TypedDict, total=False
):
    stableImage: str
    targetImage: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse(
    typing_extensions.TypedDict, total=False
):
    appConnectors: _list[GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig(
    typing_extensions.TypedDict, total=False
):
    pubsubNotification: GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig(
    typing_extensions.TypedDict, total=False
):
    pubsubSubscription: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest(
    typing_extensions.TypedDict, total=False
):
    requestId: str
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo
    validateOnly: bool

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse(
    typing_extensions.TypedDict, total=False
):
    instanceConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata(
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
class GoogleCloudBeyondcorpClientconnectorservicesV1ClientConnectorServiceOperationMetadata(
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
class GoogleCloudBeyondcorpClientgatewaysV1ClientGatewayOperationMetadata(
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
class GoogleCloudBeyondcorpNetconnectionsV1alphaListNetConnectionsResponse(
    typing_extensions.TypedDict, total=False
):
    netConnections: _list[GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpNetconnectionsV1alphaNetConnection(
    typing_extensions.TypedDict, total=False
):
    connectors: _list[str]
    createTime: str
    destinationCidrs: _list[str]
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    networkVpc: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

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
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig(
    typing_extensions.TypedDict, total=False
):
    aggregation: typing_extensions.Literal[
        "AGGREGATION_UNSPECIFIED",
        "HOURLY",
        "DAILY",
        "WEEKLY",
        "MONTHLY",
        "CUSTOM_DATE_RANGE",
    ]
    customGrouping: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping
    endTime: str
    fieldFilter: str
    group: str
    startTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaConfiguredInsightResponse(
    typing_extensions.TypedDict, total=False
):
    appliedConfig: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig
    nextPageToken: str
    rows: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping(
    typing_extensions.TypedDict, total=False
):
    fieldFilter: str
    groupFields: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight(
    typing_extensions.TypedDict, total=False
):
    appliedConfig: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig
    metadata: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata
    name: str
    rows: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata(
    typing_extensions.TypedDict, total=False
):
    aggregations: _list[str]
    category: str
    displayName: str
    fields: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField]
    groups: _list[str]
    subCategory: str
    type: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField(
    typing_extensions.TypedDict, total=False
):
    description: str
    displayName: str
    filterAlias: str
    filterable: bool
    groupable: bool
    id: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse(
    typing_extensions.TypedDict, total=False
):
    insights: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow(
    typing_extensions.TypedDict, total=False
):
    fieldValues: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    filterAlias: str
    id: str
    value: str

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
class ImageConfig(typing_extensions.TypedDict, total=False):
    stableImage: str
    targetImage: str

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
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing_extensions.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubNotification: CloudPubSubNotificationConfig

@typing.type_check_only
class PeeredVpc(typing_extensions.TypedDict, total=False):
    networkVpc: str

@typing.type_check_only
class PrincipalInfo(typing_extensions.TypedDict, total=False):
    serviceAccount: ServiceAccount

@typing.type_check_only
class RemoteAgentDetails(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReportStatusRequest(typing_extensions.TypedDict, total=False):
    requestId: str
    resourceInfo: ResourceInfo
    validateOnly: bool

@typing.type_check_only
class ResolveConnectionsResponse(typing_extensions.TypedDict, total=False):
    connectionDetails: _list[ConnectionDetails]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ResolveInstanceConfigResponse(typing_extensions.TypedDict, total=False):
    instanceConfig: ConnectorInstanceConfig

@typing.type_check_only
class ResourceInfo(dict[str, typing.Any]): ...

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

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
