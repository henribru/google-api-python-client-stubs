import typing

import typing_extensions

class IamPolicySearchResult(typing_extensions.TypedDict, total=False):
    policy: Policy
    resource: str
    project: str
    explanation: Explanation

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    title: str
    location: str

class SearchAllIamPoliciesResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[IamPolicySearchResult]
    nextPageToken: str

class StandardResourceMetadata(typing_extensions.TypedDict, total=False):
    networkTags: typing.List[str]
    project: str
    additionalAttributes: typing.List[str]
    assetType: str
    name: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    location: str
    description: str

class Permissions(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    auditConfigs: typing.List[AuditConfig]
    etag: str
    version: int

class Explanation(typing_extensions.TypedDict, total=False):
    matchedPermissions: typing.Dict[str, typing.Any]

class SearchAllResourcesResponse(typing_extensions.TypedDict, total=False):
    results: typing.List[StandardResourceMetadata]
    nextPageToken: str
