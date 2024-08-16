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
class AwsAccessRole(typing_extensions.TypedDict, total=False):
    iamRoleId: str
    identity: str

@typing.type_check_only
class AwsProperties(typing_extensions.TypedDict, total=False):
    accessRole: AwsAccessRole

@typing.type_check_only
class AzureProperties(typing_extensions.TypedDict, total=False):
    application: str
    clientId: str
    customerTenantId: str
    federatedApplicationClientId: str
    identity: str
    objectId: str
    redirectUri: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CloudResourceProperties(typing_extensions.TypedDict, total=False):
    serviceAccountId: str

@typing.type_check_only
class CloudSpannerProperties(typing_extensions.TypedDict, total=False):
    database: str
    databaseRole: str
    maxParallelism: int
    useDataBoost: bool
    useParallelism: bool
    useServerlessAnalytics: bool

@typing.type_check_only
class CloudSqlCredential(typing_extensions.TypedDict, total=False):
    password: str
    username: str

@typing.type_check_only
class CloudSqlProperties(typing_extensions.TypedDict, total=False):
    credential: CloudSqlCredential
    database: str
    instanceId: str
    serviceAccountId: str
    type: typing_extensions.Literal["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]

@typing.type_check_only
class Connection(typing_extensions.TypedDict, total=False):
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
class ConnectorConfiguration(typing_extensions.TypedDict, total=False):
    asset: ConnectorConfigurationAsset
    authentication: ConnectorConfigurationAuthentication
    connectorId: str
    endpoint: ConnectorConfigurationEndpoint
    network: ConnectorConfigurationNetwork

@typing.type_check_only
class ConnectorConfigurationAsset(typing_extensions.TypedDict, total=False):
    database: str
    googleCloudResource: str

@typing.type_check_only
class ConnectorConfigurationAuthentication(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    usernamePassword: ConnectorConfigurationUsernamePassword

@typing.type_check_only
class ConnectorConfigurationEndpoint(typing_extensions.TypedDict, total=False):
    hostPort: str

@typing.type_check_only
class ConnectorConfigurationNetwork(typing_extensions.TypedDict, total=False):
    privateServiceConnect: ConnectorConfigurationPrivateServiceConnect

@typing.type_check_only
class ConnectorConfigurationPrivateServiceConnect(
    typing_extensions.TypedDict, total=False
):
    networkAttachment: str

@typing.type_check_only
class ConnectorConfigurationSecret(typing_extensions.TypedDict, total=False):
    plaintext: str
    secretType: typing_extensions.Literal["SECRET_TYPE_UNSPECIFIED", "PLAINTEXT"]

@typing.type_check_only
class ConnectorConfigurationUsernamePassword(typing_extensions.TypedDict, total=False):
    password: ConnectorConfigurationSecret
    username: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListConnectionsResponse(typing_extensions.TypedDict, total=False):
    connections: _list[Connection]
    nextPageToken: str

@typing.type_check_only
class MetastoreServiceConfig(typing_extensions.TypedDict, total=False):
    metastoreService: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class SalesforceDataCloudProperties(typing_extensions.TypedDict, total=False):
    identity: str
    instanceUri: str
    tenantId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SparkHistoryServerConfig(typing_extensions.TypedDict, total=False):
    dataprocCluster: str

@typing.type_check_only
class SparkProperties(typing_extensions.TypedDict, total=False):
    metastoreServiceConfig: MetastoreServiceConfig
    serviceAccountId: str
    sparkHistoryServerConfig: SparkHistoryServerConfig

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
