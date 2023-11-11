import typing

import typing_extensions

_list = list

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    envoyInternalAddress: EnvoyInternalAddress
    pipe: Pipe
    socketAddress: SocketAddress

@typing.type_check_only
class BuildVersion(typing_extensions.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    version: SemanticVersion

@typing.type_check_only
class ClientConfig(typing_extensions.TypedDict, total=False):
    genericXdsConfigs: _list[GenericXdsConfig]
    node: Node
    xdsConfig: _list[PerXdsConfig]

@typing.type_check_only
class ClientStatusRequest(typing_extensions.TypedDict, total=False):
    excludeResourceContents: bool
    node: Node
    nodeMatchers: _list[NodeMatcher]

@typing.type_check_only
class ClientStatusResponse(typing_extensions.TypedDict, total=False):
    config: _list[ClientConfig]

@typing.type_check_only
class ClustersConfigDump(typing_extensions.TypedDict, total=False):
    dynamicActiveClusters: _list[DynamicCluster]
    dynamicWarmingClusters: _list[DynamicCluster]
    staticClusters: _list[StaticCluster]
    versionInfo: str

@typing.type_check_only
class ContextParams(typing_extensions.TypedDict, total=False):
    params: dict[str, typing.Any]

@typing.type_check_only
class DoubleMatcher(typing_extensions.TypedDict, total=False):
    exact: float
    range: DoubleRange

@typing.type_check_only
class DoubleRange(typing_extensions.TypedDict, total=False):
    end: float
    start: float

@typing.type_check_only
class DynamicCluster(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    cluster: dict[str, typing.Any]
    errorState: UpdateFailureState
    lastUpdated: str
    versionInfo: str

@typing.type_check_only
class DynamicEndpointConfig(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    endpointConfig: dict[str, typing.Any]
    errorState: UpdateFailureState
    lastUpdated: str
    versionInfo: str

@typing.type_check_only
class DynamicListener(typing_extensions.TypedDict, total=False):
    activeState: DynamicListenerState
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    drainingState: DynamicListenerState
    errorState: UpdateFailureState
    name: str
    warmingState: DynamicListenerState

@typing.type_check_only
class DynamicListenerState(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    listener: dict[str, typing.Any]
    versionInfo: str

@typing.type_check_only
class DynamicRouteConfig(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    errorState: UpdateFailureState
    lastUpdated: str
    routeConfig: dict[str, typing.Any]
    versionInfo: str

@typing.type_check_only
class DynamicScopedRouteConfigs(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    errorState: UpdateFailureState
    lastUpdated: str
    name: str
    scopedRouteConfigs: _list[dict[str, typing.Any]]
    versionInfo: str

@typing.type_check_only
class EndpointsConfigDump(typing_extensions.TypedDict, total=False):
    dynamicEndpointConfigs: _list[DynamicEndpointConfig]
    staticEndpointConfigs: _list[StaticEndpointConfig]

@typing.type_check_only
class EnvoyInternalAddress(typing_extensions.TypedDict, total=False):
    endpointId: str
    serverListenerName: str

@typing.type_check_only
class Extension(typing_extensions.TypedDict, total=False):
    category: str
    disabled: bool
    name: str
    typeDescriptor: str
    typeUrls: _list[str]
    version: BuildVersion

@typing.type_check_only
class GenericXdsConfig(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "UNKNOWN", "REQUESTED", "DOES_NOT_EXIST", "ACKED", "NACKED"
    ]
    configStatus: typing_extensions.Literal[
        "UNKNOWN", "SYNCED", "NOT_SENT", "STALE", "ERROR"
    ]
    errorState: UpdateFailureState
    isStaticResource: bool
    lastUpdated: str
    name: str
    typeUrl: str
    versionInfo: str
    xdsConfig: dict[str, typing.Any]

@typing.type_check_only
class GoogleRE2(typing_extensions.TypedDict, total=False):
    maxProgramSize: int

@typing.type_check_only
class InlineScopedRouteConfigs(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    name: str
    scopedRouteConfigs: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListMatcher(typing_extensions.TypedDict, total=False):
    oneOf: ValueMatcher

@typing.type_check_only
class ListenersConfigDump(typing_extensions.TypedDict, total=False):
    dynamicListeners: _list[DynamicListener]
    staticListeners: _list[StaticListener]
    versionInfo: str

@typing.type_check_only
class Locality(typing_extensions.TypedDict, total=False):
    region: str
    subZone: str
    zone: str

@typing.type_check_only
class Node(typing_extensions.TypedDict, total=False):
    clientFeatures: _list[str]
    cluster: str
    dynamicParameters: dict[str, typing.Any]
    extensions: _list[Extension]
    id: str
    listeningAddresses: _list[Address]
    locality: Locality
    metadata: dict[str, typing.Any]
    userAgentBuildVersion: BuildVersion
    userAgentName: str
    userAgentVersion: str

@typing.type_check_only
class NodeMatcher(typing_extensions.TypedDict, total=False):
    nodeId: StringMatcher
    nodeMetadatas: _list[StructMatcher]

@typing.type_check_only
class NullMatch(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PathSegment(typing_extensions.TypedDict, total=False):
    key: str

@typing.type_check_only
class PerXdsConfig(typing_extensions.TypedDict, total=False):
    clientStatus: typing_extensions.Literal[
        "CLIENT_UNKNOWN", "CLIENT_REQUESTED", "CLIENT_ACKED", "CLIENT_NACKED"
    ]
    clusterConfig: ClustersConfigDump
    endpointConfig: EndpointsConfigDump
    listenerConfig: ListenersConfigDump
    routeConfig: RoutesConfigDump
    scopedRouteConfig: ScopedRoutesConfigDump
    status: typing_extensions.Literal["UNKNOWN", "SYNCED", "NOT_SENT", "STALE", "ERROR"]

@typing.type_check_only
class Pipe(typing_extensions.TypedDict, total=False):
    mode: int
    path: str

@typing.type_check_only
class RegexMatcher(typing_extensions.TypedDict, total=False):
    googleRe2: GoogleRE2
    regex: str

@typing.type_check_only
class RoutesConfigDump(typing_extensions.TypedDict, total=False):
    dynamicRouteConfigs: _list[DynamicRouteConfig]
    staticRouteConfigs: _list[StaticRouteConfig]

@typing.type_check_only
class ScopedRoutesConfigDump(typing_extensions.TypedDict, total=False):
    dynamicScopedRouteConfigs: _list[DynamicScopedRouteConfigs]
    inlineScopedRouteConfigs: _list[InlineScopedRouteConfigs]

@typing.type_check_only
class SemanticVersion(typing_extensions.TypedDict, total=False):
    majorNumber: int
    minorNumber: int
    patch: int

@typing.type_check_only
class SocketAddress(typing_extensions.TypedDict, total=False):
    address: str
    ipv4Compat: bool
    namedPort: str
    portValue: int
    protocol: typing_extensions.Literal["TCP", "UDP"]
    resolverName: str

@typing.type_check_only
class StaticCluster(typing_extensions.TypedDict, total=False):
    cluster: dict[str, typing.Any]
    lastUpdated: str

@typing.type_check_only
class StaticEndpointConfig(typing_extensions.TypedDict, total=False):
    endpointConfig: dict[str, typing.Any]
    lastUpdated: str

@typing.type_check_only
class StaticListener(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    listener: dict[str, typing.Any]

@typing.type_check_only
class StaticRouteConfig(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    routeConfig: dict[str, typing.Any]

@typing.type_check_only
class StringMatcher(typing_extensions.TypedDict, total=False):
    contains: str
    exact: str
    ignoreCase: bool
    prefix: str
    safeRegex: RegexMatcher
    suffix: str

@typing.type_check_only
class StructMatcher(typing_extensions.TypedDict, total=False):
    path: _list[PathSegment]
    value: ValueMatcher

@typing.type_check_only
class UpdateFailureState(typing_extensions.TypedDict, total=False):
    details: str
    failedConfiguration: dict[str, typing.Any]
    lastUpdateAttempt: str
    versionInfo: str

@typing.type_check_only
class ValueMatcher(typing_extensions.TypedDict, total=False):
    boolMatch: bool
    doubleMatch: DoubleMatcher
    listMatch: ListMatcher
    nullMatch: NullMatch
    presentMatch: bool
    stringMatch: StringMatcher
