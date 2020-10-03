import typing

import typing_extensions

class ValueMatcher(typing_extensions.TypedDict, total=False):
    nullMatch: NullMatch
    doubleMatch: DoubleMatcher
    boolMatch: bool
    stringMatch: StringMatcher
    presentMatch: bool
    listMatch: ListMatcher

class DynamicListenerState(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    versionInfo: str
    listener: typing.Dict[str, typing.Any]

class StructMatcher(typing_extensions.TypedDict, total=False):
    path: typing.List[PathSegment]
    value: ValueMatcher

class Address(typing_extensions.TypedDict, total=False):
    pipe: Pipe
    socketAddress: SocketAddress

class BuildVersion(typing_extensions.TypedDict, total=False):
    version: SemanticVersion
    metadata: typing.Dict[str, typing.Any]

class StringMatcher(typing_extensions.TypedDict, total=False):
    safeRegex: RegexMatcher
    suffix: str
    prefix: str
    exact: str
    regex: str
    ignoreCase: bool

class InlineScopedRouteConfigs(typing_extensions.TypedDict, total=False):
    scopedRouteConfigs: typing.List[typing.Dict[str, typing.Any]]
    lastUpdated: str
    name: str

class ListenersConfigDump(typing_extensions.TypedDict, total=False):
    dynamicListeners: typing.List[DynamicListener]
    staticListeners: typing.List[StaticListener]
    versionInfo: str

class StaticRouteConfig(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    routeConfig: typing.Dict[str, typing.Any]

class ClientStatusResponse(typing_extensions.TypedDict, total=False):
    config: typing.List[ClientConfig]

class SemanticVersion(typing_extensions.TypedDict, total=False):
    patch: int
    minorNumber: int
    majorNumber: int

class Node(typing_extensions.TypedDict, total=False):
    locality: Locality
    extensions: typing.List[Extension]
    buildVersion: str
    userAgentVersion: str
    clientFeatures: typing.List[str]
    id: str
    metadata: typing.Dict[str, typing.Any]
    userAgentBuildVersion: BuildVersion
    cluster: str
    listeningAddresses: typing.List[Address]
    userAgentName: str

class PathSegment(typing_extensions.TypedDict, total=False):
    key: str

class ListMatcher(typing.Dict[str, typing.Any]): ...

class UpdateFailureState(typing_extensions.TypedDict, total=False):
    details: str
    failedConfiguration: typing.Dict[str, typing.Any]
    lastUpdateAttempt: str

class Extension(typing_extensions.TypedDict, total=False):
    typeDescriptor: str
    version: BuildVersion
    disabled: bool
    name: str
    category: str

class DoubleMatcher(typing_extensions.TypedDict, total=False):
    range: DoubleRange
    exact: float

class NodeMatcher(typing_extensions.TypedDict, total=False):
    nodeId: StringMatcher
    nodeMetadatas: typing.List[StructMatcher]

class ScopedRoutesConfigDump(typing_extensions.TypedDict, total=False):
    inlineScopedRouteConfigs: typing.List[InlineScopedRouteConfigs]
    dynamicScopedRouteConfigs: typing.List[DynamicScopedRouteConfigs]

class Pipe(typing_extensions.TypedDict, total=False):
    mode: int
    path: str

class StaticCluster(typing_extensions.TypedDict, total=False):
    cluster: typing.Dict[str, typing.Any]
    lastUpdated: str

class ClientConfig(typing_extensions.TypedDict, total=False):
    node: Node
    xdsConfig: typing.List[PerXdsConfig]

class StaticListener(typing_extensions.TypedDict, total=False):
    listener: typing.Dict[str, typing.Any]
    lastUpdated: str

class RoutesConfigDump(typing_extensions.TypedDict, total=False):
    staticRouteConfigs: typing.List[StaticRouteConfig]
    dynamicRouteConfigs: typing.List[DynamicRouteConfig]

class NullMatch(typing_extensions.TypedDict, total=False): ...

class ClientStatusRequest(typing_extensions.TypedDict, total=False):
    nodeMatchers: typing.List[NodeMatcher]

class RegexMatcher(typing_extensions.TypedDict, total=False):
    regex: str
    googleRe2: GoogleRE2

class SocketAddress(typing_extensions.TypedDict, total=False):
    protocol: typing_extensions.Literal["TCP", "UDP"]
    ipv4Compat: bool
    address: str
    namedPort: str
    portValue: int
    resolverName: str

class DoubleRange(typing_extensions.TypedDict, total=False):
    end: float
    start: float

class GoogleRE2(typing_extensions.TypedDict, total=False):
    maxProgramSize: int

class PerXdsConfig(typing_extensions.TypedDict, total=False):
    listenerConfig: ListenersConfigDump
    scopedRouteConfig: ScopedRoutesConfigDump
    routeConfig: RoutesConfigDump
    status: typing_extensions.Literal["UNKNOWN", "SYNCED", "NOT_SENT", "STALE", "ERROR"]
    clusterConfig: ClustersConfigDump

class DynamicScopedRouteConfigs(typing_extensions.TypedDict, total=False):
    versionInfo: str
    lastUpdated: str
    scopedRouteConfigs: typing.List[typing.Dict[str, typing.Any]]
    name: str

class Locality(typing_extensions.TypedDict, total=False):
    region: str
    subZone: str
    zone: str

class DynamicRouteConfig(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    routeConfig: typing.Dict[str, typing.Any]
    versionInfo: str

class DynamicListener(typing_extensions.TypedDict, total=False):
    warmingState: DynamicListenerState
    name: str
    activeState: DynamicListenerState
    drainingState: DynamicListenerState
    errorState: UpdateFailureState

class ClustersConfigDump(typing_extensions.TypedDict, total=False):
    staticClusters: typing.List[StaticCluster]
    dynamicWarmingClusters: typing.List[DynamicCluster]
    versionInfo: str
    dynamicActiveClusters: typing.List[DynamicCluster]

class DynamicCluster(typing_extensions.TypedDict, total=False):
    lastUpdated: str
    cluster: typing.Dict[str, typing.Any]
    versionInfo: str
