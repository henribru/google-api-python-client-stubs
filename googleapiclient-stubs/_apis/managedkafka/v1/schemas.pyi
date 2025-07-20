import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessConfig(typing_extensions.TypedDict, total=False):
    networkConfigs: _list[NetworkConfig]

@typing.type_check_only
class Acl(typing_extensions.TypedDict, total=False):
    aclEntries: _list[AclEntry]
    etag: str
    name: str
    patternType: str
    resourceName: str
    resourceType: str

@typing.type_check_only
class AclEntry(typing_extensions.TypedDict, total=False):
    host: str
    operation: str
    permissionType: str
    principal: str

@typing.type_check_only
class AddAclEntryResponse(typing_extensions.TypedDict, total=False):
    acl: Acl
    aclCreated: bool

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CapacityConfig(typing_extensions.TypedDict, total=False):
    memoryBytes: str
    vcpuCount: str

@typing.type_check_only
class CertificateAuthorityServiceConfig(typing_extensions.TypedDict, total=False):
    caPool: str

@typing.type_check_only
class CheckCompatibilityRequest(typing_extensions.TypedDict, total=False):
    references: _list[SchemaReference]
    schema: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"
    ]
    verbose: bool

@typing.type_check_only
class CheckCompatibilityResponse(typing_extensions.TypedDict, total=False):
    is_compatible: bool
    messages: _list[str]

@typing.type_check_only
class Cluster(typing_extensions.TypedDict, total=False):
    capacityConfig: CapacityConfig
    createTime: str
    gcpConfig: GcpConfig
    labels: dict[str, typing.Any]
    name: str
    rebalanceConfig: RebalanceConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    tlsConfig: TlsConfig
    updateTime: str

@typing.type_check_only
class ConnectAccessConfig(typing_extensions.TypedDict, total=False):
    networkConfigs: _list[ConnectNetworkConfig]

@typing.type_check_only
class ConnectCluster(typing_extensions.TypedDict, total=False):
    capacityConfig: CapacityConfig
    config: dict[str, typing.Any]
    createTime: str
    gcpConfig: ConnectGcpConfig
    kafkaCluster: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING"
    ]
    updateTime: str

@typing.type_check_only
class ConnectGcpConfig(typing_extensions.TypedDict, total=False):
    accessConfig: ConnectAccessConfig
    secretPaths: _list[str]

@typing.type_check_only
class ConnectNetworkConfig(typing_extensions.TypedDict, total=False):
    additionalSubnets: _list[str]
    dnsDomainNames: _list[str]
    primarySubnet: str

@typing.type_check_only
class Connector(typing_extensions.TypedDict, total=False):
    configs: dict[str, typing.Any]
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "UNASSIGNED",
        "RUNNING",
        "PAUSED",
        "FAILED",
        "RESTARTING",
        "STOPPED",
    ]
    taskRestartPolicy: TaskRetryPolicy

@typing.type_check_only
class ConsumerGroup(typing_extensions.TypedDict, total=False):
    name: str
    topics: dict[str, typing.Any]

@typing.type_check_only
class ConsumerPartitionMetadata(typing_extensions.TypedDict, total=False):
    metadata: str
    offset: str

@typing.type_check_only
class ConsumerTopicMetadata(typing_extensions.TypedDict, total=False):
    partitions: dict[str, typing.Any]

@typing.type_check_only
class Context(typing_extensions.TypedDict, total=False):
    name: str
    subjects: _list[str]

@typing.type_check_only
class CreateSchemaRegistryRequest(typing_extensions.TypedDict, total=False):
    schemaRegistry: SchemaRegistry
    schemaRegistryId: str

@typing.type_check_only
class CreateVersionRequest(typing_extensions.TypedDict, total=False):
    id: int
    normalize: bool
    references: _list[SchemaReference]
    schema: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"
    ]
    version: int

@typing.type_check_only
class CreateVersionResponse(typing_extensions.TypedDict, total=False):
    id: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GcpConfig(typing_extensions.TypedDict, total=False):
    accessConfig: AccessConfig
    kmsKey: str

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListAclsResponse(typing_extensions.TypedDict, total=False):
    acls: _list[Acl]
    nextPageToken: str

@typing.type_check_only
class ListClustersResponse(typing_extensions.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectClustersResponse(typing_extensions.TypedDict, total=False):
    connectClusters: _list[ConnectCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing_extensions.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str

@typing.type_check_only
class ListConsumerGroupsResponse(typing_extensions.TypedDict, total=False):
    consumerGroups: _list[ConsumerGroup]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSchemaRegistriesResponse(typing_extensions.TypedDict, total=False):
    schemaRegistries: _list[SchemaRegistry]

@typing.type_check_only
class ListTopicsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LookupVersionRequest(typing_extensions.TypedDict, total=False):
    deleted: bool
    normalize: bool
    references: _list[SchemaReference]
    schema: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"
    ]

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    subnet: str

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
class PauseConnectorRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PauseConnectorResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RebalanceConfig(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal[
        "MODE_UNSPECIFIED", "NO_REBALANCE", "AUTO_REBALANCE_ON_SCALE_UP"
    ]

@typing.type_check_only
class RemoveAclEntryResponse(typing_extensions.TypedDict, total=False):
    acl: Acl
    aclDeleted: bool

@typing.type_check_only
class RestartConnectorRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestartConnectorResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResumeConnectorRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResumeConnectorResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    references: _list[SchemaReference]
    schema: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"
    ]

@typing.type_check_only
class SchemaConfig(typing_extensions.TypedDict, total=False):
    alias: str
    compatibility: typing_extensions.Literal[
        "NONE",
        "BACKWARD",
        "BACKWARD_TRANSITIVE",
        "FORWARD",
        "FORWARD_TRANSITIVE",
        "FULL",
        "FULL_TRANSITIVE",
    ]
    normalize: bool

@typing.type_check_only
class SchemaMode(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["NONE", "READONLY", "READWRITE", "IMPORT"]

@typing.type_check_only
class SchemaReference(typing_extensions.TypedDict, total=False):
    name: str
    subject: str
    version: int

@typing.type_check_only
class SchemaRegistry(typing_extensions.TypedDict, total=False):
    contexts: _list[str]
    name: str

@typing.type_check_only
class SchemaVersion(typing_extensions.TypedDict, total=False):
    id: int
    references: _list[SchemaReference]
    schema: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"
    ]
    subject: str
    version: int

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopConnectorRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StopConnectorResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TaskRetryPolicy(typing_extensions.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str

@typing.type_check_only
class TlsConfig(typing_extensions.TypedDict, total=False):
    sslPrincipalMappingRules: str
    trustConfig: TrustConfig

@typing.type_check_only
class Topic(typing_extensions.TypedDict, total=False):
    configs: dict[str, typing.Any]
    name: str
    partitionCount: int
    replicationFactor: int

@typing.type_check_only
class TrustConfig(typing_extensions.TypedDict, total=False):
    casConfigs: _list[CertificateAuthorityServiceConfig]

@typing.type_check_only
class UpdateSchemaConfigRequest(typing_extensions.TypedDict, total=False):
    compatibility: typing_extensions.Literal[
        "NONE",
        "BACKWARD",
        "BACKWARD_TRANSITIVE",
        "FORWARD",
        "FORWARD_TRANSITIVE",
        "FULL",
        "FULL_TRANSITIVE",
    ]
    normalize: bool

@typing.type_check_only
class UpdateSchemaModeRequest(typing_extensions.TypedDict, total=False):
    mode: typing_extensions.Literal["NONE", "READONLY", "READWRITE", "IMPORT"]
