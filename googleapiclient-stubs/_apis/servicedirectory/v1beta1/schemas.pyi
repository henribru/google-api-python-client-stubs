import typing

import typing_extensions

_list = list

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Endpoint(typing_extensions.TypedDict, total=False):
    address: str
    createTime: str
    metadata: dict[str, typing.Any]
    name: str
    network: str
    port: int
    updateTime: str

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
class ListEndpointsResponse(typing_extensions.TypedDict, total=False):
    endpoints: _list[Endpoint]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNamespacesResponse(typing_extensions.TypedDict, total=False):
    namespaces: _list[Namespace]
    nextPageToken: str

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
class Namespace(typing_extensions.TypedDict, total=False):
    createTime: str
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ResolveServiceRequest(typing_extensions.TypedDict, total=False):
    endpointFilter: str
    maxEndpoints: int

@typing.type_check_only
class ResolveServiceResponse(typing_extensions.TypedDict, total=False):
    service: Service

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    createTime: str
    endpoints: _list[Endpoint]
    metadata: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
