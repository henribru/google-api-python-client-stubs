import typing

import typing_extensions

_list = list

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
class AuthConfig(typing_extensions.TypedDict, total=False):
    additionalVariables: _list[ConfigVariable]
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
    ]
    oauth2ClientCredentials: Oauth2ClientCredentials
    oauth2JwtBearer: Oauth2JwtBearer
    sshPublicKey: SshPublicKey
    userPassword: UserPassword

@typing.type_check_only
class AuthConfigTemplate(typing_extensions.TypedDict, total=False):
    authType: typing_extensions.Literal[
        "AUTH_TYPE_UNSPECIFIED",
        "USER_PASSWORD",
        "OAUTH2_JWT_BEARER",
        "OAUTH2_CLIENT_CREDENTIALS",
        "SSH_PUBLIC_KEY",
        "OAUTH2_AUTH_CODE_FLOW",
    ]
    configVariableTemplates: _list[ConfigVariableTemplate]

@typing.type_check_only
class AuthorizationCodeLink(typing_extensions.TypedDict, total=False):
    clientId: str
    enablePkce: bool
    scopes: _list[str]
    uri: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConfigVariable(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    key: str
    secretValue: Secret
    stringValue: str

@typing.type_check_only
class ConfigVariableTemplate(typing_extensions.TypedDict, total=False):
    authorizationCodeLink: AuthorizationCodeLink
    description: str
    displayName: str
    enumOptions: _list[EnumOption]
    key: str
    required: bool
    roleGrant: RoleGrant
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DEPRECATED"]
    validationRegex: str
    valueType: typing_extensions.Literal[
        "VALUE_TYPE_UNSPECIFIED",
        "STRING",
        "INT",
        "BOOL",
        "SECRET",
        "ENUM",
        "AUTHORIZATION_CODE",
    ]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
    authConfig: AuthConfig
    configVariables: _list[ConfigVariable]
    connectorVersion: str
    createTime: str
    description: str
    destinationConfigs: _list[DestinationConfig]
    envoyImageLocation: str
    imageLocation: str
    labels: dict[str, typing.Any]
    lockConfig: LockConfig
    name: str
    nodeConfig: NodeConfig
    serviceAccount: str
    serviceDirectory: str
    status: ConnectionStatus
    suspended: bool
    updateTime: str

@typing.type_check_only
class ConnectionSchemaMetadata(typing_extensions.TypedDict, total=False):
    actions: _list[str]
    entities: _list[str]

@typing.type_check_only
class ConnectionStatus(typing_extensions.TypedDict, total=False):
    description: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ACTIVE",
        "INACTIVE",
        "DELETING",
        "UPDATING",
        "ERROR",
    ]
    status: str

@typing.type_check_only
class Connector(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED"
    ]
    name: str
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class ConnectorVersion(typing_extensions.TypedDict, total=False):
    authConfigTemplates: _list[AuthConfigTemplate]
    configVariableTemplates: _list[ConfigVariableTemplate]
    createTime: str
    displayName: str
    egressControlConfig: EgressControlConfig
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED"
    ]
    name: str
    releaseVersion: str
    roleGrant: RoleGrant
    roleGrants: _list[RoleGrant]
    supportedRuntimeFeatures: SupportedRuntimeFeatures
    updateTime: str

@typing.type_check_only
class Destination(typing_extensions.TypedDict, total=False):
    host: str
    port: int
    serviceAttachment: str

@typing.type_check_only
class DestinationConfig(typing_extensions.TypedDict, total=False):
    destinations: _list[Destination]
    key: str

@typing.type_check_only
class EgressControlConfig(typing_extensions.TypedDict, total=False):
    backends: str
    extractionRules: ExtractionRules

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnumOption(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtractionRule(typing_extensions.TypedDict, total=False):
    extractionRegex: str
    source: Source

@typing.type_check_only
class ExtractionRules(typing_extensions.TypedDict, total=False):
    extractionRule: _list[ExtractionRule]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    field: str
    key: bool
    nullable: bool
    readonly: bool

@typing.type_check_only
class InputParameter(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    nullable: bool
    parameter: str

@typing.type_check_only
class JwtClaims(typing_extensions.TypedDict, total=False):
    audience: str
    issuer: str
    subject: str

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorVersionsResponse(typing_extensions.TypedDict, total=False):
    connectorVersions: _list[ConnectorVersion]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing_extensions.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListProvidersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    providers: _list[Provider]
    unreachable: _list[str]

@typing.type_check_only
class ListRuntimeActionSchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimeActionSchemas: _list[RuntimeActionSchema]

@typing.type_check_only
class ListRuntimeEntitySchemasResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    runtimeEntitySchemas: _list[RuntimeEntitySchema]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LockConfig(typing_extensions.TypedDict, total=False):
    locked: bool
    reason: str

@typing.type_check_only
class NodeConfig(typing_extensions.TypedDict, total=False):
    maxNodeCount: int
    minNodeCount: int

@typing.type_check_only
class Oauth2ClientCredentials(typing_extensions.TypedDict, total=False):
    clientId: str
    clientSecret: Secret

@typing.type_check_only
class Oauth2JwtBearer(typing_extensions.TypedDict, total=False):
    clientKey: Secret
    jwtClaims: JwtClaims

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Provider(typing_extensions.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    documentationUri: str
    externalUri: str
    labels: dict[str, typing.Any]
    launchStage: typing_extensions.Literal[
        "LAUNCH_STAGE_UNSPECIFIED", "PREVIEW", "GA", "DEPRECATED"
    ]
    name: str
    updateTime: str
    webAssetsLocation: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    pathTemplate: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "GCP_PROJECT",
        "GCP_RESOURCE",
        "GCP_SECRETMANAGER_SECRET",
        "GCP_SECRETMANAGER_SECRET_VERSION",
    ]

@typing.type_check_only
class ResultMetadata(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_INT",
        "DATA_TYPE_SMALLINT",
        "DATA_TYPE_DOUBLE",
        "DATA_TYPE_DATE",
        "DATA_TYPE_DATETIME",
        "DATA_TYPE_TIME",
        "DATA_TYPE_STRING",
        "DATA_TYPE_LONG",
        "DATA_TYPE_BOOLEAN",
        "DATA_TYPE_DECIMAL",
        "DATA_TYPE_UUID",
        "DATA_TYPE_BLOB",
        "DATA_TYPE_BIT",
        "DATA_TYPE_TINYINT",
        "DATA_TYPE_INTEGER",
        "DATA_TYPE_BIGINT",
        "DATA_TYPE_FLOAT",
        "DATA_TYPE_REAL",
        "DATA_TYPE_NUMERIC",
        "DATA_TYPE_CHAR",
        "DATA_TYPE_VARCHAR",
        "DATA_TYPE_LONGVARCHAR",
        "DATA_TYPE_TIMESTAMP",
        "DATA_TYPE_NCHAR",
        "DATA_TYPE_NVARCHAR",
        "DATA_TYPE_LONGNVARCHAR",
        "DATA_TYPE_NULL",
        "DATA_TYPE_OTHER",
        "DATA_TYPE_JAVA_OBJECT",
        "DATA_TYPE_DISTINCT",
        "DATA_TYPE_STRUCT",
        "DATA_TYPE_ARRAY",
        "DATA_TYPE_CLOB",
        "DATA_TYPE_REF",
        "DATA_TYPE_DATALINK",
        "DATA_TYPE_ROWID",
        "DATA_TYPE_BINARY",
        "DATA_TYPE_VARBINARY",
        "DATA_TYPE_LONGVARBINARY",
        "DATA_TYPE_NCLOB",
        "DATA_TYPE_SQLXML",
        "DATA_TYPE_REF_CURSOR",
        "DATA_TYPE_TIME_WITH_TIMEZONE",
        "DATA_TYPE_TIMESTAMP_WITH_TIMEZONE",
    ]
    description: str
    field: str

@typing.type_check_only
class RoleGrant(typing_extensions.TypedDict, total=False):
    helperTextTemplate: str
    principal: typing_extensions.Literal["PRINCIPAL_UNSPECIFIED", "CONNECTOR_SA"]
    resource: Resource
    roles: _list[str]

@typing.type_check_only
class RuntimeActionSchema(typing_extensions.TypedDict, total=False):
    action: str
    inputParameters: _list[InputParameter]
    resultMetadata: _list[ResultMetadata]

@typing.type_check_only
class RuntimeConfig(typing_extensions.TypedDict, total=False):
    conndSubscription: str
    conndTopic: str
    controlPlaneSubscription: str
    controlPlaneTopic: str
    locationId: str
    name: str
    runtimeEndpoint: str
    schemaGcsBucket: str
    serviceDirectory: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INACTIVE",
        "ACTIVATING",
        "ACTIVE",
        "CREATING",
        "DELETING",
        "UPDATING",
    ]

@typing.type_check_only
class RuntimeEntitySchema(typing_extensions.TypedDict, total=False):
    entity: str
    fields: _list[Field]

@typing.type_check_only
class Secret(typing_extensions.TypedDict, total=False):
    secretVersion: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    fieldId: str
    sourceType: typing_extensions.Literal["SOURCE_TYPE_UNSPECIFIED", "CONFIG_VARIABLE"]

@typing.type_check_only
class SshPublicKey(typing_extensions.TypedDict, total=False):
    certType: str
    password: Secret
    sshClientCert: Secret
    sshClientCertPass: Secret
    username: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedRuntimeFeatures(typing_extensions.TypedDict, total=False):
    actionApis: bool
    entityApis: bool
    sqlQuery: bool

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UserPassword(typing_extensions.TypedDict, total=False):
    password: Secret
    username: str
