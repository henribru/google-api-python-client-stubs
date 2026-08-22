import typing

_list = list

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing.TypedDict, total=False):
    address: str
    annotations: dict[str, typing.Any]
    name: str
    network: str
    port: int
    uid: str

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
class ListEndpointsResponse(typing.TypedDict, total=False):
    endpoints: _list[Endpoint]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNamespacesResponse(typing.TypedDict, total=False):
    namespaces: _list[Namespace]
    nextPageToken: str

@typing.type_check_only
class ListServicesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    services: _list[Service]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Namespace(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    uid: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ResolveServiceRequest(typing.TypedDict, total=False):
    endpointFilter: str
    maxEndpoints: int

@typing.type_check_only
class ResolveServiceResponse(typing.TypedDict, total=False):
    service: Service

@typing.type_check_only
class Service(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    endpoints: _list[Endpoint]
    name: str
    uid: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
