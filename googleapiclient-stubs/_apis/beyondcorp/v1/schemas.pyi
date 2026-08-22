import typing

_list = list

@typing.type_check_only
class AllocatedConnection(typing.TypedDict, total=False):
    ingressPort: int
    pscUri: str

@typing.type_check_only
class AppGateway(typing.TypedDict, total=False):
    allocatedConnections: _list[AllocatedConnection]
    createTime: str
    displayName: str
    hostType: typing.Literal["HOST_TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str
    uri: str

@typing.type_check_only
class AppGatewayOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class CloudSecurityZerotrustApplinkAppConnectorProtoConnectionConfig(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class CloudSecurityZerotrustApplinkAppConnectorProtoGateway(
    typing.TypedDict, total=False
):
    interface: str
    name: str
    port: int
    project: str
    selfLink: str
    zone: str

@typing.type_check_only
class CloudSecurityZerotrustApplinkLogagentProtoLogAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnection(typing.TypedDict, total=False):
    applicationEndpoint: (
        GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint
    )
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionApplicationEndpoint(
    typing.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionGateway(
    typing.TypedDict, total=False
):
    appGateway: str
    ingressPort: int
    l7psc: str
    type: typing.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1AppConnectionOperationMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    appConnections: _list[GoogleCloudBeyondcorpAppconnectionsV1AppConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponse(
    typing.TypedDict, total=False
):
    appConnectionDetails: _list[
        GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails
    ]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1ResolveAppConnectionsResponseAppConnectionDetails(
    typing.TypedDict, total=False
):
    appConnection: GoogleCloudBeyondcorpAppconnectionsV1AppConnection
    recentMigVms: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionOperationMetadata(
    typing.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnector(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfo
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig(
    typing.TypedDict, total=False
):
    imageConfig: GoogleCloudBeyondcorpAppconnectorsV1ImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig
    sequenceNumber: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorOperationMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    serviceAccount: (
        GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount
    )

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1AppConnectorPrincipalInfoServiceAccount(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails(
    typing.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ImageConfig(typing.TypedDict, total=False):
    stableImage: str
    targetImage: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ListAppConnectorsResponse(
    typing.TypedDict, total=False
):
    appConnectors: _list[GoogleCloudBeyondcorpAppconnectorsV1AppConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1NotificationConfig(
    typing.TypedDict, total=False
):
    pubsubNotification: GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1NotificationConfigCloudPubSubNotificationConfig(
    typing.TypedDict, total=False
):
    pubsubSubscription: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ReportStatusRequest(
    typing.TypedDict, total=False
):
    requestId: str
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo
    validateOnly: bool

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ResolveInstanceConfigResponse(
    typing.TypedDict, total=False
):
    instanceConfig: GoogleCloudBeyondcorpAppconnectorsV1AppConnectorInstanceConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo(typing.TypedDict, total=False):
    id: str
    resource: dict[str, typing.Any]
    status: typing.Literal[
        "HEALTH_STATUS_UNSPECIFIED", "HEALTHY", "UNHEALTHY", "UNRESPONSIVE", "DEGRADED"
    ]
    sub: _list[GoogleCloudBeyondcorpAppconnectorsV1ResourceInfo]
    time: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorOperationMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppgatewaysV1alphaAppGatewayOperationMetadata(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpConnectorsV1alphaRemoteAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerServiceOperationMetadata(
    typing.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpPartnerservicesV1mainPartnerServiceOperationMetadata(
    typing.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1Application(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    endpointMatchers: _list[GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher]
    name: str
    schema: typing.Literal["SCHEMA_UNSPECIFIED", "PROXY_GATEWAY", "API_GATEWAY"]
    updateTime: str
    upstreams: _list[GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstream(
    typing.TypedDict, total=False
):
    egressPolicy: GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy
    external: GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal
    network: GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork
    proxyProtocol: GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamExternal(
    typing.TypedDict, total=False
):
    endpoints: _list[GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ApplicationUpstreamNetwork(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders(
    typing.TypedDict, total=False
):
    deviceInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo
    )
    dispatchInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDispatchInfo
    )
    groupInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo
    )
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]
    userInfo: GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDeviceInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedDispatchInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedGroupInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeadersDelegatedUserInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1EgressPolicy(
    typing.TypedDict, total=False
):
    regions: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1Endpoint(typing.TypedDict, total=False):
    hostname: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1EndpointMatcher(
    typing.TypedDict, total=False
):
    hostname: str
    ports: _list[int]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1Hub(typing.TypedDict, total=False):
    internetGateway: GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1InternetGateway(
    typing.TypedDict, total=False
):
    assignedIps: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ListApplicationsResponse(
    typing.TypedDict, total=False
):
    applications: _list[GoogleCloudBeyondcorpSecuritygatewaysV1Application]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ListSecurityGatewaysResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securityGateways: _list[GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1LoggingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig(
    typing.TypedDict, total=False
):
    allowedClientHeaders: _list[str]
    clientIp: bool
    contextualHeaders: GoogleCloudBeyondcorpSecuritygatewaysV1ContextualHeaders
    gatewayIdentity: typing.Literal["GATEWAY_IDENTITY_UNSPECIFIED", "RESOURCE_NAME"]
    metadataHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGateway(
    typing.TypedDict, total=False
):
    createTime: str
    delegatingServiceAccount: str
    displayName: str
    externalIps: _list[str]
    hubs: dict[str, typing.Any]
    logging: GoogleCloudBeyondcorpSecuritygatewaysV1LoggingConfig
    name: str
    proxyProtocolConfig: GoogleCloudBeyondcorpSecuritygatewaysV1ProxyProtocolConfig
    serviceDiscovery: GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery
    state: typing.Literal[
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
class GoogleCloudBeyondcorpSecuritygatewaysV1SecurityGatewayOperationMetadata(
    typing.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscovery(
    typing.TypedDict, total=False
):
    apiGateway: GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGateway(
    typing.TypedDict, total=False
):
    resourceOverride: GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1ServiceDiscoveryApiGatewayOperationDescriptor(
    typing.TypedDict, total=False
):
    path: str

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGatewayOperationMetadata(
    typing.TypedDict, total=False
):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleCloudLocationListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[GoogleCloudLocationLocation]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudLocationLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleIamV1SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: GoogleIamV1Policy
    updateMask: str

@typing.type_check_only
class GoogleIamV1TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListAppGatewaysResponse(typing.TypedDict, total=False):
    appGateways: _list[AppGateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class Tunnelv1ProtoTunnelerError(typing.TypedDict, total=False):
    err: str
    retryable: bool

@typing.type_check_only
class Tunnelv1ProtoTunnelerInfo(typing.TypedDict, total=False):
    backoffRetryCount: int
    id: str
    latestErr: Tunnelv1ProtoTunnelerError
    latestRetryTime: str
    totalRetryCount: int
