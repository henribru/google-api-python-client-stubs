import typing

import typing_extensions

_list = list

@typing.type_check_only
class Agent(typing_extensions.TypedDict, total=False):
    agentId: str
    attributes: dict[str, typing.Any]
    card: Card
    createTime: str
    description: str
    displayName: str
    location: str
    name: str
    protocols: _list[Protocol]
    skills: _list[Skill]
    uid: str
    updateTime: str
    version: str

@typing.type_check_only
class AgentSpec(typing_extensions.TypedDict, total=False):
    content: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "NO_SPEC", "A2A_AGENT_CARD"]

@typing.type_check_only
class Annotations(typing_extensions.TypedDict, total=False):
    destructiveHint: bool
    idempotentHint: bool
    openWorldHint: bool
    readOnlyHint: bool
    title: str

@typing.type_check_only
class AuthProviderBinding(typing_extensions.TypedDict, total=False):
    authProvider: str
    continueUri: str
    scopes: _list[str]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    authProviderBinding: AuthProviderBinding
    createTime: str
    description: str
    displayName: str
    name: str
    source: Source
    target: Target
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Card(typing_extensions.TypedDict, total=False):
    content: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "A2A_AGENT_CARD"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    description: str
    displayName: str
    endpointId: str
    interfaces: _list[Interface]
    name: str
    updateTime: str

@typing.type_check_only
class EndpointSpec(typing_extensions.TypedDict, total=False):
    content: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "NO_SPEC"]

@typing.type_check_only
class FetchAvailableBindingsResponse(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    nextPageToken: str

@typing.type_check_only
class Interface(typing_extensions.TypedDict, total=False):
    protocolBinding: typing_extensions.Literal[
        "PROTOCOL_BINDING_UNSPECIFIED", "JSONRPC", "GRPC", "HTTP_JSON"
    ]
    url: str

@typing.type_check_only
class ListAgentsResponse(typing_extensions.TypedDict, total=False):
    agents: _list[Agent]
    nextPageToken: str

@typing.type_check_only
class ListBindingsResponse(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    nextPageToken: str

@typing.type_check_only
class ListEndpointsResponse(typing_extensions.TypedDict, total=False):
    endpoints: _list[Endpoint]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMcpServersResponse(typing_extensions.TypedDict, total=False):
    mcpServers: _list[McpServer]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class McpServer(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    createTime: str
    description: str
    displayName: str
    interfaces: _list[Interface]
    mcpServerId: str
    name: str
    tools: _list[Tool]
    updateTime: str

@typing.type_check_only
class McpServerSpec(typing_extensions.TypedDict, total=False):
    content: dict[str, typing.Any]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "NO_SPEC", "TOOL_SPEC"]

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
class Protocol(typing_extensions.TypedDict, total=False):
    interfaces: _list[Interface]
    protocolVersion: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "A2A_AGENT", "CUSTOM"]

@typing.type_check_only
class SearchAgentsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    searchString: str

@typing.type_check_only
class SearchAgentsResponse(typing_extensions.TypedDict, total=False):
    agents: _list[Agent]
    nextPageToken: str

@typing.type_check_only
class SearchMcpServersRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    searchString: str

@typing.type_check_only
class SearchMcpServersResponse(typing_extensions.TypedDict, total=False):
    mcpServers: _list[McpServer]
    nextPageToken: str

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    agentSpec: AgentSpec
    createTime: str
    description: str
    displayName: str
    endpointSpec: EndpointSpec
    interfaces: _list[Interface]
    mcpServerSpec: McpServerSpec
    name: str
    registryResource: str
    updateTime: str

@typing.type_check_only
class Skill(typing_extensions.TypedDict, total=False):
    description: str
    examples: _list[str]
    id: str
    name: str
    tags: _list[str]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    identifier: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Target(typing_extensions.TypedDict, total=False):
    identifier: str

@typing.type_check_only
class Tool(typing_extensions.TypedDict, total=False):
    annotations: Annotations
    description: str
    name: str
