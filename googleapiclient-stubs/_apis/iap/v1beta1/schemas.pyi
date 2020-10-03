import typing

import typing_extensions

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    expression: str
    description: str
    title: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str
    bindingId: str

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    bindings: typing.List[Binding]
    etag: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions
