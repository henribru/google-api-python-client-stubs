import typing

_list = list

@typing.type_check_only
class ApigatewayApi(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: dict[str, typing.Any]
    managedService: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class ApigatewayApiConfig(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    gatewayServiceAccount: str
    grpcServices: _list[ApigatewayApiConfigGrpcServiceDefinition]
    labels: dict[str, typing.Any]
    managedServiceConfigs: _list[ApigatewayApiConfigFile]
    name: str
    openapiDocuments: _list[ApigatewayApiConfigOpenApiDocument]
    serviceConfigId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "FAILED",
        "DELETING",
        "UPDATING",
        "ACTIVATING",
    ]
    updateTime: str

@typing.type_check_only
class ApigatewayApiConfigFile(typing.TypedDict, total=False):
    contents: str
    path: str

@typing.type_check_only
class ApigatewayApiConfigGrpcServiceDefinition(typing.TypedDict, total=False):
    fileDescriptorSet: ApigatewayApiConfigFile
    source: _list[ApigatewayApiConfigFile]

@typing.type_check_only
class ApigatewayApiConfigOpenApiDocument(typing.TypedDict, total=False):
    document: ApigatewayApiConfigFile

@typing.type_check_only
class ApigatewayAuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[ApigatewayAuditLogConfig]
    service: str

@typing.type_check_only
class ApigatewayAuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class ApigatewayBinding(typing.TypedDict, total=False):
    condition: ApigatewayExpr
    members: _list[str]
    role: str

@typing.type_check_only
class ApigatewayCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ApigatewayExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ApigatewayGateway(typing.TypedDict, total=False):
    apiConfig: str
    createTime: str
    defaultHostname: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class ApigatewayListApiConfigsResponse(typing.TypedDict, total=False):
    apiConfigs: _list[ApigatewayApiConfig]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class ApigatewayListApisResponse(typing.TypedDict, total=False):
    apis: _list[ApigatewayApi]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class ApigatewayListGatewaysResponse(typing.TypedDict, total=False):
    gateways: _list[ApigatewayGateway]
    nextPageToken: str
    unreachableLocations: _list[str]

@typing.type_check_only
class ApigatewayListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[ApigatewayLocation]
    nextPageToken: str

@typing.type_check_only
class ApigatewayListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[ApigatewayOperation]
    unreachable: _list[str]

@typing.type_check_only
class ApigatewayLocation(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ApigatewayOperation(typing.TypedDict, total=False):
    done: bool
    error: ApigatewayStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class ApigatewayOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    diagnostics: _list[ApigatewayOperationMetadataDiagnostic]
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ApigatewayOperationMetadataDiagnostic(typing.TypedDict, total=False):
    location: str
    message: str

@typing.type_check_only
class ApigatewayPolicy(typing.TypedDict, total=False):
    auditConfigs: _list[ApigatewayAuditConfig]
    bindings: _list[ApigatewayBinding]
    etag: str
    version: int

@typing.type_check_only
class ApigatewaySetIamPolicyRequest(typing.TypedDict, total=False):
    policy: ApigatewayPolicy
    updateMask: str

@typing.type_check_only
class ApigatewayStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ApigatewayTestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class ApigatewayTestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...
