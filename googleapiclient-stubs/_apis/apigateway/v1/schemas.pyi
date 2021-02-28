import typing

import typing_extensions
@typing.type_check_only
class ApigatewayApi(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    managedService: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class ApigatewayApiConfig(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    gatewayServiceAccount: str
    grpcServices: typing.List[ApigatewayApiConfigGrpcServiceDefinition]
    labels: typing.Dict[str, typing.Any]
    managedServiceConfigs: typing.List[ApigatewayApiConfigFile]
    name: str
    openapiDocuments: typing.List[ApigatewayApiConfigOpenApiDocument]
    serviceConfigId: str
    state: typing_extensions.Literal[
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
class ApigatewayApiConfigFile(typing_extensions.TypedDict, total=False):
    contents: str
    path: str

@typing.type_check_only
class ApigatewayApiConfigGrpcServiceDefinition(
    typing_extensions.TypedDict, total=False
):
    fileDescriptorSet: ApigatewayApiConfigFile
    source: typing.List[ApigatewayApiConfigFile]

@typing.type_check_only
class ApigatewayApiConfigOpenApiDocument(typing_extensions.TypedDict, total=False):
    document: ApigatewayApiConfigFile

@typing.type_check_only
class ApigatewayAuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[ApigatewayAuditLogConfig]
    service: str

@typing.type_check_only
class ApigatewayAuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class ApigatewayBinding(typing_extensions.TypedDict, total=False):
    condition: ApigatewayExpr
    members: typing.List[str]
    role: str

@typing.type_check_only
class ApigatewayCancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ApigatewayExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ApigatewayGateway(typing_extensions.TypedDict, total=False):
    apiConfig: str
    createTime: str
    defaultHostname: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "FAILED", "DELETING", "UPDATING"
    ]
    updateTime: str

@typing.type_check_only
class ApigatewayListApiConfigsResponse(typing_extensions.TypedDict, total=False):
    apiConfigs: typing.List[ApigatewayApiConfig]
    nextPageToken: str
    unreachableLocations: typing.List[str]

@typing.type_check_only
class ApigatewayListApisResponse(typing_extensions.TypedDict, total=False):
    apis: typing.List[ApigatewayApi]
    nextPageToken: str
    unreachableLocations: typing.List[str]

@typing.type_check_only
class ApigatewayListGatewaysResponse(typing_extensions.TypedDict, total=False):
    gateways: typing.List[ApigatewayGateway]
    nextPageToken: str
    unreachableLocations: typing.List[str]

@typing.type_check_only
class ApigatewayListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[ApigatewayLocation]
    nextPageToken: str

@typing.type_check_only
class ApigatewayListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[ApigatewayOperation]

@typing.type_check_only
class ApigatewayLocation(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class ApigatewayOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: ApigatewayStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class ApigatewayOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    diagnostics: typing.List[ApigatewayOperationMetadataDiagnostic]
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class ApigatewayOperationMetadataDiagnostic(typing_extensions.TypedDict, total=False):
    location: str
    message: str

@typing.type_check_only
class ApigatewayPolicy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[ApigatewayAuditConfig]
    bindings: typing.List[ApigatewayBinding]
    etag: str
    version: int

@typing.type_check_only
class ApigatewaySetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: ApigatewayPolicy
    updateMask: str

@typing.type_check_only
class ApigatewayStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ApigatewayTestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class ApigatewayTestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...
