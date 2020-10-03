import typing

import typing_extensions

class ApigatewaySetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: ApigatewayPolicy

class ApigatewayExpr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class ApigatewayOperationMetadataDiagnostic(typing_extensions.TypedDict, total=False):
    message: str
    location: str

class ApigatewayApiConfigFile(typing_extensions.TypedDict, total=False):
    path: str
    contents: str

class ApigatewayGatewayConfig(typing_extensions.TypedDict, total=False):
    backendConfig: ApigatewayBackendConfig

class ApigatewayGateway(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    createTime: str
    name: str
    apiConfig: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    updateTime: str
    defaultHostname: str

class ApigatewayListApiConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachableLocations: typing.List[str]
    apiConfigs: typing.List[ApigatewayApiConfig]

class ApigatewayListApisResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    apis: typing.List[ApigatewayApi]
    unreachableLocations: typing.List[str]

class ApigatewayTestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class ApigatewayAuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class ApigatewayBackendConfig(typing_extensions.TypedDict, total=False):
    googleServiceAccount: str

class ApigatewayCancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ApigatewayBinding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: ApigatewayExpr
    role: str

class ApigatewayApiConfigOpenApiDocument(typing_extensions.TypedDict, total=False):
    document: ApigatewayApiConfigFile

class ApigatewayListGatewaysResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachableLocations: typing.List[str]
    gateways: typing.List[ApigatewayGateway]

class ApigatewayLocation(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    locationId: str
    name: str
    displayName: str
    metadata: typing.Dict[str, typing.Any]

class ApigatewayStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class ApigatewayAuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[ApigatewayAuditLogConfig]

class ApigatewayPolicy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[ApigatewayAuditConfig]
    version: int
    bindings: typing.List[ApigatewayBinding]

class ApigatewayApi(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    updateTime: str
    createTime: str
    labels: typing.Dict[str, typing.Any]
    managedService: str
    name: str
    displayName: str

class ApigatewayApiConfigGrpcServiceDefinition(
    typing_extensions.TypedDict, total=False
):
    fileDescriptorSet: ApigatewayApiConfigFile
    source: typing.List[ApigatewayApiConfigFile]

class ApigatewayOperationMetadata(typing_extensions.TypedDict, total=False):
    statusMessage: str
    diagnostics: typing.List[ApigatewayOperationMetadataDiagnostic]
    createTime: str
    apiVersion: str
    target: str
    requestedCancellation: bool
    endTime: str
    verb: str

class ApigatewayListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[ApigatewayOperation]
    nextPageToken: str

class ApigatewayTestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ApigatewayListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[ApigatewayLocation]
    nextPageToken: str

class ApigatewayApiConfig(typing_extensions.TypedDict, total=False):
    displayName: str
    gatewayConfig: ApigatewayGatewayConfig
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "DELETING",
        "UPDATING",
        "ACTIVATING",
    ]
    name: str
    labels: typing.Dict[str, typing.Any]
    serviceConfigId: str
    openapiDocuments: typing.List[ApigatewayApiConfigOpenApiDocument]
    createTime: str
    managedServiceConfigs: typing.List[ApigatewayApiConfigFile]
    grpcServices: typing.List[ApigatewayApiConfigGrpcServiceDefinition]
    updateTime: str

class ApigatewayOperation(typing_extensions.TypedDict, total=False):
    name: str
    error: ApigatewayStatus
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
