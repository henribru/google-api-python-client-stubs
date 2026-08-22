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
class ApplicationEndpoint(typing.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class CloudPubSubNotificationConfig(typing.TypedDict, total=False):
    pubsubSubscription: str

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
class Connection(typing.TypedDict, total=False):
    applicationEndpoint: ApplicationEndpoint
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: Gateway
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "TCP_PROXY"]
    uid: str
    updateTime: str

@typing.type_check_only
class ConnectionDetails(typing.TypedDict, total=False):
    connection: Connection
    recentMigVms: _list[str]

@typing.type_check_only
class ConnectionOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Connector(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: PrincipalInfo
    resourceInfo: ResourceInfo
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class ConnectorInstanceConfig(typing.TypedDict, total=False):
    imageConfig: ImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: NotificationConfig
    sequenceNumber: str

@typing.type_check_only
class ConnectorOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ContainerHealthDetails(typing.TypedDict, total=False):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Gateway(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str
    userPort: int

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
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection(
    typing.TypedDict, total=False
):
    applicationEndpoint: (
        GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint
    )
    connectors: _list[str]
    createTime: str
    displayName: str
    gateway: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway
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
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionApplicationEndpoint(
    typing.TypedDict, total=False
):
    host: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnectionGateway(
    typing.TypedDict, total=False
):
    appGateway: str
    ingressPort: int
    l7psc: str
    type: typing.Literal["TYPE_UNSPECIFIED", "GCP_REGIONAL_MIG"]
    uri: str

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
class GoogleCloudBeyondcorpAppconnectionsV1alphaListAppConnectionsResponse(
    typing.TypedDict, total=False
):
    appConnections: _list[GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponse(
    typing.TypedDict, total=False
):
    appConnectionDetails: _list[
        GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails
    ]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectionsV1alphaResolveAppConnectionsResponseAppConnectionDetails(
    typing.TypedDict, total=False
):
    appConnection: GoogleCloudBeyondcorpAppconnectionsV1alphaAppConnection
    recentMigVms: _list[str]

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
class GoogleCloudBeyondcorpAppconnectorsV1ContainerHealthDetails(
    typing.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1RemoteAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector(
    typing.TypedDict, total=False
):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    principalInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "UPDATING", "DELETING", "DOWN"
    ]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig(
    typing.TypedDict, total=False
):
    imageConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig
    instanceConfig: dict[str, typing.Any]
    notificationConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig
    sequenceNumber: str

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
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfo(
    typing.TypedDict, total=False
):
    serviceAccount: (
        GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount
    )

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorPrincipalInfoServiceAccount(
    typing.TypedDict, total=False
):
    email: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaContainerHealthDetails(
    typing.TypedDict, total=False
):
    currentConfigVersion: str
    errorMsg: str
    expectedConfigVersion: str
    extendedStatus: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig(
    typing.TypedDict, total=False
):
    stableImage: str
    targetImage: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaListAppConnectorsResponse(
    typing.TypedDict, total=False
):
    appConnectors: _list[GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig(
    typing.TypedDict, total=False
):
    pubsubNotification: GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfigCloudPubSubNotificationConfig(
    typing.TypedDict, total=False
):
    pubsubSubscription: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaRemoteAgentDetails(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaReportStatusRequest(
    typing.TypedDict, total=False
):
    requestId: str
    resourceInfo: GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo
    validateOnly: bool

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResolveInstanceConfigResponse(
    typing.TypedDict, total=False
):
    instanceConfig: GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig

@typing.type_check_only
class GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo(
    typing.TypedDict, total=False
):
    id: str
    resource: dict[str, typing.Any]
    status: typing.Literal[
        "HEALTH_STATUS_UNSPECIFIED", "HEALTHY", "UNHEALTHY", "UNRESPONSIVE", "DEGRADED"
    ]
    sub: _list[GoogleCloudBeyondcorpAppconnectorsV1alphaResourceInfo]
    time: str

@typing.type_check_only
class GoogleCloudBeyondcorpAppgatewaysV1AppGatewayOperationMetadata(
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
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig(
    typing.TypedDict, total=False
):
    aggregation: typing.Literal[
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
    typing.TypedDict, total=False
):
    appliedConfig: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig
    nextPageToken: str
    rows: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping(
    typing.TypedDict, total=False
):
    fieldFilter: str
    groupFields: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight(
    typing.TypedDict, total=False
):
    appliedConfig: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaAppliedConfig
    metadata: GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata
    name: str
    rows: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadata(
    typing.TypedDict, total=False
):
    aggregations: _list[
        typing.Literal[
            "AGGREGATION_UNSPECIFIED",
            "HOURLY",
            "DAILY",
            "WEEKLY",
            "MONTHLY",
            "CUSTOM_DATE_RANGE",
        ]
    ]
    category: str
    displayName: str
    fields: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField]
    groups: _list[str]
    subCategory: str
    type: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsightMetadataField(
    typing.TypedDict, total=False
):
    description: str
    displayName: str
    filterAlias: str
    filterable: bool
    groupable: bool
    id: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaListInsightsResponse(
    typing.TypedDict, total=False
):
    insights: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaInsight]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRow(
    typing.TypedDict, total=False
):
    fieldValues: _list[GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformInsightsV1alphaRowFieldVal(
    typing.TypedDict, total=False
):
    displayName: str
    filterAlias: str
    id: str
    value: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaCancelSubscriptionResponse(
    typing.TypedDict, total=False
):
    effectiveCancellationTime: str

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    subscriptions: _list[
        GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription
    ]

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaRestartSubscriptionResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription(
    typing.TypedDict, total=False
):
    autoRenewEnabled: bool
    billingAccount: str
    createTime: str
    csgCustomer: bool
    endTime: str
    name: str
    seatCount: str
    signupSource: str
    sku: typing.Literal["SKU_UNSPECIFIED", "BCE_STANDARD_SKU"]
    startTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE", "COMPLETED"]
    subscriberType: typing.Literal[
        "SUBSCRIBER_TYPE_UNSPECIFIED", "ONLINE", "OFFLINE", "CEP_TRIAL"
    ]
    type: typing.Literal["TYPE_UNSPECIFIED", "TRIAL", "PAID", "ALLOWLIST"]

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
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication(
    typing.TypedDict, total=False
):
    createTime: str
    displayName: str
    endpointMatchers: _list[GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher]
    name: str
    schema: typing.Literal["SCHEMA_UNSPECIFIED", "PROXY_GATEWAY", "API_GATEWAY"]
    updateTime: str
    upstreams: _list[GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstream(
    typing.TypedDict, total=False
):
    egressPolicy: GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy
    external: GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal
    network: GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork
    proxyProtocol: GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamExternal(
    typing.TypedDict, total=False
):
    endpoints: _list[GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplicationUpstreamNetwork(
    typing.TypedDict, total=False
):
    name: str

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders(
    typing.TypedDict, total=False
):
    deviceInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo
    )
    dispatchInfo: GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDispatchInfo
    groupInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo
    )
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]
    userInfo: (
        GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo
    )

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDeviceInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedDispatchInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedGroupInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeadersDelegatedUserInfo(
    typing.TypedDict, total=False
):
    outputType: typing.Literal["OUTPUT_TYPE_UNSPECIFIED", "PROTOBUF", "JSON", "NONE"]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaEgressPolicy(
    typing.TypedDict, total=False
):
    regions: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpoint(
    typing.TypedDict, total=False
):
    hostname: str
    port: int

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaEndpointMatcher(
    typing.TypedDict, total=False
):
    hostname: str
    ports: _list[int]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaHub(typing.TypedDict, total=False):
    internetGateway: GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaInternetGateway(
    typing.TypedDict, total=False
):
    assignedIps: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaListApplicationsResponse(
    typing.TypedDict, total=False
):
    applications: _list[GoogleCloudBeyondcorpSecuritygatewaysV1alphaApplication]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaListSecurityGatewaysResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    securityGateways: _list[GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaLoggingConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig(
    typing.TypedDict, total=False
):
    allowedClientHeaders: _list[str]
    clientIp: bool
    contextualHeaders: GoogleCloudBeyondcorpSecuritygatewaysV1alphaContextualHeaders
    gatewayIdentity: typing.Literal["GATEWAY_IDENTITY_UNSPECIFIED", "RESOURCE_NAME"]
    metadataHeaders: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaSecurityGateway(
    typing.TypedDict, total=False
):
    createTime: str
    delegatingServiceAccount: str
    displayName: str
    externalIps: _list[str]
    hubs: dict[str, typing.Any]
    logging: GoogleCloudBeyondcorpSecuritygatewaysV1alphaLoggingConfig
    name: str
    proxyProtocolConfig: GoogleCloudBeyondcorpSecuritygatewaysV1alphaProxyProtocolConfig
    serviceDiscovery: GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery
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
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscovery(
    typing.TypedDict, total=False
):
    apiGateway: GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGateway(
    typing.TypedDict, total=False
):
    resourceOverride: GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor

@typing.type_check_only
class GoogleCloudBeyondcorpSecuritygatewaysV1alphaServiceDiscoveryApiGatewayOperationDescriptor(
    typing.TypedDict, total=False
):
    path: str

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
class ImageConfig(typing.TypedDict, total=False):
    stableImage: str
    targetImage: str

@typing.type_check_only
class ListAppGatewaysResponse(typing.TypedDict, total=False):
    appGateways: _list[AppGateway]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class NotificationConfig(typing.TypedDict, total=False):
    pubsubNotification: CloudPubSubNotificationConfig

@typing.type_check_only
class PrincipalInfo(typing.TypedDict, total=False):
    serviceAccount: ServiceAccount

@typing.type_check_only
class RemoteAgentDetails(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReportStatusRequest(typing.TypedDict, total=False):
    requestId: str
    resourceInfo: ResourceInfo
    validateOnly: bool

@typing.type_check_only
class ResolveConnectionsResponse(typing.TypedDict, total=False):
    connectionDetails: _list[ConnectionDetails]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ResolveInstanceConfigResponse(typing.TypedDict, total=False):
    instanceConfig: ConnectorInstanceConfig

@typing.type_check_only
class ResourceInfo(typing.TypedDict, total=False):
    id: str
    resource: dict[str, typing.Any]
    status: typing.Literal[
        "HEALTH_STATUS_UNSPECIFIED", "HEALTHY", "UNHEALTHY", "UNRESPONSIVE", "DEGRADED"
    ]
    sub: _list[ResourceInfo]
    time: str

@typing.type_check_only
class ServiceAccount(typing.TypedDict, total=False):
    email: str

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
