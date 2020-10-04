import typing

import typing_extensions
@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Explanation(typing_extensions.TypedDict, total=False):
    matchedPermissions: typing.Dict[str, typing.Any]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class IamPolicySearchResult(typing_extensions.TypedDict, total=False):
    explanation: Explanation
    policy: Policy
    project: str
    resource: str

@typing.type_check_only
class Permissions(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class SearchAllIamPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[IamPolicySearchResult]

@typing.type_check_only
class SearchAllResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[StandardResourceMetadata]

@typing.type_check_only
class StandardResourceMetadata(typing_extensions.TypedDict, total=False):
    additionalAttributes: typing.List[str]
    assetType: str
    description: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    location: str
    name: str
    networkTags: typing.List[str]
    project: str
