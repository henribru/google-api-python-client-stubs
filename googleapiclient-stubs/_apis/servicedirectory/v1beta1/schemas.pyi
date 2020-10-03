import typing

import typing_extensions

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class Empty(typing_extensions.TypedDict, total=False): ...

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    name: str

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    services: typing.List[Service]

class ListEndpointsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    endpoints: typing.List[Endpoint]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    location: str
    title: str
    description: str

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    bindingId: str
    condition: Expr

class Endpoint(typing_extensions.TypedDict, total=False):
    address: str
    name: str
    port: int
    metadata: typing.Dict[str, typing.Any]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class ResolveServiceRequest(typing_extensions.TypedDict, total=False):
    maxEndpoints: int
    endpointFilter: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Service(typing_extensions.TypedDict, total=False):
    name: str
    endpoints: typing.List[Endpoint]
    metadata: typing.Dict[str, typing.Any]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Namespace(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str

class ListNamespacesResponse(typing_extensions.TypedDict, total=False):
    namespaces: typing.List[Namespace]
    nextPageToken: str

class ResolveServiceResponse(typing_extensions.TypedDict, total=False):
    service: Service
