import typing

import typing_extensions

_list = list

@typing.type_check_only
class BlockchainNode(typing_extensions.TypedDict, total=False):
    blockchainType: typing_extensions.Literal["BLOCKCHAIN_TYPE_UNSPECIFIED", "ETHEREUM"]
    connectionInfo: ConnectionInfo
    createTime: str
    ethereumDetails: EthereumDetails
    labels: dict[str, typing.Any]
    name: str
    privateServiceConnectEnabled: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "DELETING",
        "RUNNING",
        "ERROR",
        "UPDATING",
        "REPAIRING",
        "RECONCILING",
        "SYNCING",
    ]
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConnectionInfo(typing_extensions.TypedDict, total=False):
    endpointInfo: EndpointInfo
    serviceAttachment: str

@typing.type_check_only
class EndpointInfo(typing_extensions.TypedDict, total=False):
    jsonRpcApiEndpoint: str
    websocketsApiEndpoint: str

@typing.type_check_only
class EthereumDetails(typing_extensions.TypedDict, total=False):
    additionalEndpoints: EthereumEndpoints
    apiEnableAdmin: bool
    apiEnableDebug: bool
    consensusClient: typing_extensions.Literal[
        "CONSENSUS_CLIENT_UNSPECIFIED", "LIGHTHOUSE", "ERIGON_EMBEDDED_CONSENSUS_LAYER"
    ]
    executionClient: typing_extensions.Literal[
        "EXECUTION_CLIENT_UNSPECIFIED", "GETH", "ERIGON"
    ]
    gethDetails: GethDetails
    network: typing_extensions.Literal[
        "NETWORK_UNSPECIFIED",
        "MAINNET",
        "TESTNET_GOERLI_PRATER",
        "TESTNET_SEPOLIA",
        "TESTNET_HOLESKY",
    ]
    nodeType: typing_extensions.Literal[
        "NODE_TYPE_UNSPECIFIED", "LIGHT", "FULL", "ARCHIVE"
    ]
    validatorConfig: ValidatorConfig

@typing.type_check_only
class EthereumEndpoints(typing_extensions.TypedDict, total=False):
    beaconApiEndpoint: str
    beaconPrometheusMetricsApiEndpoint: str
    executionClientPrometheusMetricsApiEndpoint: str

@typing.type_check_only
class GethDetails(typing_extensions.TypedDict, total=False):
    garbageCollectionMode: typing_extensions.Literal[
        "GARBAGE_COLLECTION_MODE_UNSPECIFIED", "FULL", "ARCHIVE"
    ]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListBlockchainNodesResponse(typing_extensions.TypedDict, total=False):
    blockchainNodes: _list[BlockchainNode]
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
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class ValidatorConfig(typing_extensions.TypedDict, total=False):
    beaconFeeRecipient: str
    managedValidatorClient: bool
    mevRelayUrls: _list[str]
