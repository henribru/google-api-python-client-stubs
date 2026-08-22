import typing

_list = list

@typing.type_check_only
class AccessConfig(typing.TypedDict, total=False):
    networkConfigs: _list[NetworkConfig]

@typing.type_check_only
class Acl(typing.TypedDict, total=False):
    aclEntries: _list[AclEntry]
    etag: str
    name: str
    patternType: str
    resourceName: str
    resourceType: str

@typing.type_check_only
class AclEntry(typing.TypedDict, total=False):
    host: str
    operation: str
    permissionType: str
    principal: str

@typing.type_check_only
class AddAclEntryResponse(typing.TypedDict, total=False):
    acl: Acl
    aclCreated: bool

@typing.type_check_only
class BrokerDetails(typing.TypedDict, total=False):
    brokerIndex: str
    nodeId: str
    rack: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CapacityConfig(typing.TypedDict, total=False):
    memoryBytes: str
    vcpuCount: str

@typing.type_check_only
class CertificateAuthorityServiceConfig(typing.TypedDict, total=False):
    caPool: str

@typing.type_check_only
class CheckCompatibilityRequest(typing.TypedDict, total=False):
    references: _list[SchemaReference]
    schema: str
    schemaType: typing.Literal["SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"]
    verbose: bool

@typing.type_check_only
class CheckCompatibilityResponse(typing.TypedDict, total=False):
    is_compatible: bool
    messages: _list[str]

@typing.type_check_only
class Cluster(typing.TypedDict, total=False):
    brokerDetails: _list[BrokerDetails]
    capacityConfig: CapacityConfig
    createTime: str
    gcpConfig: GcpConfig
    kafkaVersion: str
    labels: dict[str, typing.Any]
    name: str
    rebalanceConfig: RebalanceConfig
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING"
    ]
    tlsConfig: TlsConfig
    updateOptions: UpdateOptions
    updateTime: str

@typing.type_check_only
class ConnectAccessConfig(typing.TypedDict, total=False):
    networkConfigs: _list[ConnectNetworkConfig]

@typing.type_check_only
class ConnectCluster(typing.TypedDict, total=False):
    capacityConfig: CapacityConfig
    config: dict[str, typing.Any]
    createTime: str
    gcpConfig: ConnectGcpConfig
    kafkaCluster: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "DETACHED"
    ]
    updateTime: str

@typing.type_check_only
class ConnectGcpConfig(typing.TypedDict, total=False):
    accessConfig: ConnectAccessConfig
    secretPaths: _list[str]

@typing.type_check_only
class ConnectNetworkConfig(typing.TypedDict, total=False):
    additionalSubnets: _list[str]
    dnsDomainNames: _list[str]
    primarySubnet: str

@typing.type_check_only
class Connector(typing.TypedDict, total=False):
    configs: dict[str, typing.Any]
    name: str
    state: typing.Literal[
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
class ConsumerGroup(typing.TypedDict, total=False):
    name: str
    topics: dict[str, typing.Any]

@typing.type_check_only
class ConsumerPartitionMetadata(typing.TypedDict, total=False):
    metadata: str
    offset: str

@typing.type_check_only
class ConsumerTopicMetadata(typing.TypedDict, total=False):
    partitions: dict[str, typing.Any]

@typing.type_check_only
class Context(typing.TypedDict, total=False):
    name: str
    subjects: _list[str]

@typing.type_check_only
class CreateSchemaRegistryRequest(typing.TypedDict, total=False):
    schemaRegistry: SchemaRegistry
    schemaRegistryId: str

@typing.type_check_only
class CreateVersionRequest(typing.TypedDict, total=False):
    id: int
    normalize: bool
    references: _list[SchemaReference]
    schema: str
    schemaType: typing.Literal["SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"]
    version: int

@typing.type_check_only
class CreateVersionResponse(typing.TypedDict, total=False):
    id: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GcpConfig(typing.TypedDict, total=False):
    accessConfig: AccessConfig
    kmsKey: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListAclsResponse(typing.TypedDict, total=False):
    acls: _list[Acl]
    nextPageToken: str

@typing.type_check_only
class ListClustersResponse(typing.TypedDict, total=False):
    clusters: _list[Cluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectClustersResponse(typing.TypedDict, total=False):
    connectClusters: _list[ConnectCluster]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListConnectorsResponse(typing.TypedDict, total=False):
    connectors: _list[Connector]
    nextPageToken: str

@typing.type_check_only
class ListConsumerGroupsResponse(typing.TypedDict, total=False):
    consumerGroups: _list[ConsumerGroup]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSchemaRegistriesResponse(typing.TypedDict, total=False):
    schemaRegistries: _list[SchemaRegistry]

@typing.type_check_only
class ListTopicsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    topics: _list[Topic]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LookupVersionRequest(typing.TypedDict, total=False):
    deleted: bool
    normalize: bool
    references: _list[SchemaReference]
    schema: str
    schemaType: typing.Literal["SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"]

@typing.type_check_only
class NetworkConfig(typing.TypedDict, total=False):
    subnet: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PauseConnectorRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PauseConnectorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class RebalanceConfig(typing.TypedDict, total=False):
    mode: typing.Literal[
        "MODE_UNSPECIFIED", "NO_REBALANCE", "AUTO_REBALANCE_ON_SCALE_UP"
    ]

@typing.type_check_only
class RemoveAclEntryResponse(typing.TypedDict, total=False):
    acl: Acl
    aclDeleted: bool

@typing.type_check_only
class RestartConnectorRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RestartConnectorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResumeConnectorRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResumeConnectorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Schema(typing.TypedDict, total=False):
    references: _list[SchemaReference]
    schema: str
    schemaType: typing.Literal["SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"]

@typing.type_check_only
class SchemaConfig(typing.TypedDict, total=False):
    alias: str
    compatibility: typing.Literal[
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
class SchemaMode(typing.TypedDict, total=False):
    mode: typing.Literal["NONE", "READONLY", "READWRITE", "IMPORT"]

@typing.type_check_only
class SchemaReference(typing.TypedDict, total=False):
    name: str
    subject: str
    version: int

@typing.type_check_only
class SchemaRegistry(typing.TypedDict, total=False):
    contexts: _list[str]
    name: str

@typing.type_check_only
class SchemaSubject(typing.TypedDict, total=False):
    name: str
    versions: _list[str]

@typing.type_check_only
class SchemaVersion(typing.TypedDict, total=False):
    id: int
    references: _list[SchemaReference]
    schema: str
    schemaType: typing.Literal["SCHEMA_TYPE_UNSPECIFIED", "AVRO", "JSON", "PROTOBUF"]
    subject: str
    version: int

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StopConnectorRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class StopConnectorResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class TaskRetryPolicy(typing.TypedDict, total=False):
    maximumBackoff: str
    minimumBackoff: str
    taskRetryDisabled: bool

@typing.type_check_only
class TlsConfig(typing.TypedDict, total=False):
    sslPrincipalMappingRules: str
    trustConfig: TrustConfig

@typing.type_check_only
class Topic(typing.TypedDict, total=False):
    configs: dict[str, typing.Any]
    name: str
    partitionCount: int
    replicationFactor: int

@typing.type_check_only
class TrustConfig(typing.TypedDict, total=False):
    casConfigs: _list[CertificateAuthorityServiceConfig]

@typing.type_check_only
class UpdateOptions(typing.TypedDict, total=False):
    allowBrokerDownscaleOnClusterUpscale: bool

@typing.type_check_only
class UpdateSchemaConfigRequest(typing.TypedDict, total=False):
    compatibility: typing.Literal[
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
class UpdateSchemaModeRequest(typing.TypedDict, total=False):
    mode: typing.Literal["NONE", "READONLY", "READWRITE", "IMPORT"]
