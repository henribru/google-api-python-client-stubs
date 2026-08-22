import typing

_list = list

@typing.type_check_only
class Address(typing.TypedDict, total=False):
    pipe: Pipe
    socketAddress: SocketAddress

@typing.type_check_only
class BuildVersion(typing.TypedDict, total=False):
    metadata: dict[str, typing.Any]
    version: SemanticVersion

@typing.type_check_only
class ClientConfig(typing.TypedDict, total=False):
    node: Node
    xdsConfig: _list[PerXdsConfig]

@typing.type_check_only
class ClientStatusRequest(typing.TypedDict, total=False):
    nodeMatchers: _list[NodeMatcher]

@typing.type_check_only
class ClientStatusResponse(typing.TypedDict, total=False):
    config: _list[ClientConfig]

@typing.type_check_only
class ClustersConfigDump(typing.TypedDict, total=False):
    dynamicActiveClusters: _list[DynamicCluster]
    dynamicWarmingClusters: _list[DynamicCluster]
    staticClusters: _list[StaticCluster]
    versionInfo: str

@typing.type_check_only
class DoubleMatcher(typing.TypedDict, total=False):
    exact: float
    range: DoubleRange

@typing.type_check_only
class DoubleRange(typing.TypedDict, total=False):
    end: float
    start: float

@typing.type_check_only
class DynamicCluster(typing.TypedDict, total=False):
    cluster: dict[str, typing.Any]
    lastUpdated: str
    versionInfo: str

@typing.type_check_only
class DynamicListener(typing.TypedDict, total=False):
    activeState: DynamicListenerState
    drainingState: DynamicListenerState
    errorState: UpdateFailureState
    name: str
    warmingState: DynamicListenerState

@typing.type_check_only
class DynamicListenerState(typing.TypedDict, total=False):
    lastUpdated: str
    listener: dict[str, typing.Any]
    versionInfo: str

@typing.type_check_only
class DynamicRouteConfig(typing.TypedDict, total=False):
    lastUpdated: str
    routeConfig: dict[str, typing.Any]
    versionInfo: str

@typing.type_check_only
class DynamicScopedRouteConfigs(typing.TypedDict, total=False):
    lastUpdated: str
    name: str
    scopedRouteConfigs: _list[dict[str, typing.Any]]
    versionInfo: str

@typing.type_check_only
class Extension(typing.TypedDict, total=False):
    category: str
    disabled: bool
    name: str
    typeDescriptor: str
    version: BuildVersion

@typing.type_check_only
class GoogleRE2(typing.TypedDict, total=False):
    maxProgramSize: int

@typing.type_check_only
class InlineScopedRouteConfigs(typing.TypedDict, total=False):
    lastUpdated: str
    name: str
    scopedRouteConfigs: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListMatcher(typing.TypedDict, total=False):
    oneOf: ValueMatcher

@typing.type_check_only
class ListenersConfigDump(typing.TypedDict, total=False):
    dynamicListeners: _list[DynamicListener]
    staticListeners: _list[StaticListener]
    versionInfo: str

@typing.type_check_only
class Locality(typing.TypedDict, total=False):
    region: str
    subZone: str
    zone: str

@typing.type_check_only
class Node(typing.TypedDict, total=False):
    buildVersion: str
    clientFeatures: _list[str]
    cluster: str
    extensions: _list[Extension]
    id: str
    listeningAddresses: _list[Address]
    locality: Locality
    metadata: dict[str, typing.Any]
    userAgentBuildVersion: BuildVersion
    userAgentName: str
    userAgentVersion: str

@typing.type_check_only
class NodeMatcher(typing.TypedDict, total=False):
    nodeId: StringMatcher
    nodeMetadatas: _list[StructMatcher]

@typing.type_check_only
class NullMatch(typing.TypedDict, total=False): ...

@typing.type_check_only
class PathSegment(typing.TypedDict, total=False):
    key: str

@typing.type_check_only
class PerXdsConfig(typing.TypedDict, total=False):
    clusterConfig: ClustersConfigDump
    listenerConfig: ListenersConfigDump
    routeConfig: RoutesConfigDump
    scopedRouteConfig: ScopedRoutesConfigDump
    status: typing.Literal["UNKNOWN", "SYNCED", "NOT_SENT", "STALE", "ERROR"]

@typing.type_check_only
class Pipe(typing.TypedDict, total=False):
    mode: int
    path: str

@typing.type_check_only
class RegexMatcher(typing.TypedDict, total=False):
    googleRe2: GoogleRE2
    regex: str

@typing.type_check_only
class RoutesConfigDump(typing.TypedDict, total=False):
    dynamicRouteConfigs: _list[DynamicRouteConfig]
    staticRouteConfigs: _list[StaticRouteConfig]

@typing.type_check_only
class ScopedRoutesConfigDump(typing.TypedDict, total=False):
    dynamicScopedRouteConfigs: _list[DynamicScopedRouteConfigs]
    inlineScopedRouteConfigs: _list[InlineScopedRouteConfigs]

@typing.type_check_only
class SemanticVersion(typing.TypedDict, total=False):
    majorNumber: int
    minorNumber: int
    patch: int

@typing.type_check_only
class SocketAddress(typing.TypedDict, total=False):
    address: str
    ipv4Compat: bool
    namedPort: str
    portValue: int
    protocol: typing.Literal["TCP", "UDP"]
    resolverName: str

@typing.type_check_only
class StaticCluster(typing.TypedDict, total=False):
    cluster: dict[str, typing.Any]
    lastUpdated: str

@typing.type_check_only
class StaticListener(typing.TypedDict, total=False):
    lastUpdated: str
    listener: dict[str, typing.Any]

@typing.type_check_only
class StaticRouteConfig(typing.TypedDict, total=False):
    lastUpdated: str
    routeConfig: dict[str, typing.Any]

@typing.type_check_only
class StringMatcher(typing.TypedDict, total=False):
    exact: str
    ignoreCase: bool
    prefix: str
    regex: str
    safeRegex: RegexMatcher
    suffix: str

@typing.type_check_only
class StructMatcher(typing.TypedDict, total=False):
    path: _list[PathSegment]
    value: ValueMatcher

@typing.type_check_only
class UpdateFailureState(typing.TypedDict, total=False):
    details: str
    failedConfiguration: dict[str, typing.Any]
    lastUpdateAttempt: str

@typing.type_check_only
class ValueMatcher(typing.TypedDict, total=False):
    boolMatch: bool
    doubleMatch: DoubleMatcher
    listMatch: ListMatcher
    nullMatch: NullMatch
    presentMatch: bool
    stringMatch: StringMatcher
