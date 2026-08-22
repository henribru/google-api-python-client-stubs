import typing

_list = list

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class AwsAccessRole(typing.TypedDict, total=False):
    iamRoleId: str
    identity: str

@typing.type_check_only
class AwsProperties(typing.TypedDict, total=False):
    accessRole: AwsAccessRole

@typing.type_check_only
class AzureProperties(typing.TypedDict, total=False):
    application: str
    clientId: str
    customerTenantId: str
    federatedApplicationClientId: str
    identity: str
    objectId: str
    redirectUri: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudResourceProperties(typing.TypedDict, total=False):
    serviceAccountId: str

@typing.type_check_only
class CloudSpannerProperties(typing.TypedDict, total=False):
    database: str
    databaseRole: str
    maxParallelism: int
    useDataBoost: bool
    useParallelism: bool
    useServerlessAnalytics: bool

@typing.type_check_only
class CloudSqlCredential(typing.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class CloudSqlProperties(typing.TypedDict, total=False):
    credential: CloudSqlCredential
    database: str
    instanceId: str
    serviceAccountId: str
    type: typing.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class Connection(typing.TypedDict, total=False):
    aws: AwsProperties
    azure: AzureProperties
    cloudResource: CloudResourceProperties
    cloudSpanner: CloudSpannerProperties
    cloudSql: CloudSqlProperties
    configuration: ConnectorConfiguration
    creationTime: str
    description: str
    friendlyName: str
    hasCredential: bool
    kmsKeyName: str
    lastModifiedTime: str
    name: str
    salesforceDataCloud: SalesforceDataCloudProperties
    spark: SparkProperties

@typing.type_check_only
class ConnectorConfiguration(typing.TypedDict, total=False):
    asset: ConnectorConfigurationAsset
    authentication: ConnectorConfigurationAuthentication
    connectorId: str
    endpoint: ConnectorConfigurationEndpoint
    network: ConnectorConfigurationNetwork
    parameters: dict[str, typing.Any]
    tls: ConnectorConfigurationTls

@typing.type_check_only
class ConnectorConfigurationAsset(typing.TypedDict, total=False):
    database: str
    googleCloudResource: str

@typing.type_check_only
class ConnectorConfigurationAuthentication(typing.TypedDict, total=False):
    parameters: dict[str, typing.Any]
    serviceAccount: str
    usernamePassword: ConnectorConfigurationUsernamePassword

@typing.type_check_only
class ConnectorConfigurationEndpoint(typing.TypedDict, total=False):
    hostPort: str

@typing.type_check_only
class ConnectorConfigurationNetwork(typing.TypedDict, total=False):
    privateServiceConnect: ConnectorConfigurationPrivateServiceConnect

@typing.type_check_only
class ConnectorConfigurationParameterValue(typing.TypedDict, total=False):
    boolValue: bool
    doubleValue: float
    int32Value: int
    secretValue: ConnectorConfigurationSecret
    stringValue: str

@typing.type_check_only
class ConnectorConfigurationPrivateServiceConnect(typing.TypedDict, total=False):
    networkAttachment: str

@typing.type_check_only
class ConnectorConfigurationSecret(typing.TypedDict, total=False):
    plaintext: str
    secretType: typing.Literal["SECRET_TYPE_UNSPECIFIED", "PLAINTEXT"]

@typing.type_check_only
class ConnectorConfigurationTls(typing.TypedDict, total=False):
    mode: typing.Literal[
        "MODE_UNSPECIFIED",
        "DISABLE",
        "ENCRYPT_VERIFY_NONE",
        "ENCRYPT_VERIFY_CA",
        "ENCRYPT_VERIFY_CA_AND_HOST",
    ]
    privatePki: ConnectorConfigurationTlsPrivatePki
    webPki: ConnectorConfigurationTlsWebPki

@typing.type_check_only
class ConnectorConfigurationTlsPrivatePki(typing.TypedDict, total=False):
    trustedCertificatesPem: str

@typing.type_check_only
class ConnectorConfigurationTlsWebPki(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConnectorConfigurationUsernamePassword(typing.TypedDict, total=False):
    password: ConnectorConfigurationSecret
    username: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListConnectionsResponse(typing.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str

@typing.type_check_only
class MetastoreServiceConfig(typing.TypedDict, total=False):
    metastoreService: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SalesforceDataCloudProperties(typing.TypedDict, total=False):
    identity: str
    instanceUri: str
    tenantId: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SparkHistoryServerConfig(typing.TypedDict, total=False):
    dataprocCluster: str

@typing.type_check_only
class SparkProperties(typing.TypedDict, total=False):
    metastoreServiceConfig: MetastoreServiceConfig
    serviceAccountId: str
    sparkHistoryServerConfig: SparkHistoryServerConfig

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
