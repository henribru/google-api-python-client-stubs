import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListReposResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repos: _list[Repo]

@typing.type_check_only
class MirrorConfig(typing_extensions.TypedDict, total=False):
    deployKeyId: str
    url: str
    webhookId: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectConfig(typing_extensions.TypedDict, total=False):
    enablePrivateKeyCheck: bool
    name: str
    pubsubConfigs: dict[str, typing.Any]

@typing.type_check_only
class PubsubConfig(typing_extensions.TypedDict, total=False):
    messageFormat: typing_extensions.Literal[
        "MESSAGE_FORMAT_UNSPECIFIED", "PROTOBUF", "JSON"
    ]
    serviceAccountEmail: str
    topic: str

@typing.type_check_only
class Repo(typing_extensions.TypedDict, total=False):
    mirrorConfig: MirrorConfig
    name: str
    pubsubConfigs: dict[str, typing.Any]
    size: str
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SyncRepoMetadata(typing_extensions.TypedDict, total=False):
    name: str
    startTime: str
    statusMessage: str
    updateTime: str

@typing.type_check_only
class SyncRepoRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpdateProjectConfigRequest(typing_extensions.TypedDict, total=False):
    projectConfig: ProjectConfig
    updateMask: str

@typing.type_check_only
class UpdateRepoRequest(typing_extensions.TypedDict, total=False):
    repo: Repo
    updateMask: str
