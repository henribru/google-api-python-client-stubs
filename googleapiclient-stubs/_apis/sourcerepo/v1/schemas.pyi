import typing

_list = list

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ListReposResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repos: _list[Repo]

@typing.type_check_only
class MirrorConfig(typing.TypedDict, total=False):
    deployKeyId: str
    url: str
    webhookId: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProjectConfig(typing.TypedDict, total=False):
    enablePrivateKeyCheck: bool
    name: str
    pubsubConfigs: dict[str, typing.Any]

@typing.type_check_only
class PubsubConfig(typing.TypedDict, total=False):
    messageFormat: typing.Literal["MESSAGE_FORMAT_UNSPECIFIED", "PROTOBUF", "JSON"]
    serviceAccountEmail: str
    topic: str

@typing.type_check_only
class Repo(typing.TypedDict, total=False):
    mirrorConfig: MirrorConfig
    name: str
    pubsubConfigs: dict[str, typing.Any]
    size: str
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SyncRepoMetadata(typing.TypedDict, total=False):
    name: str
    startTime: str
    statusMessage: str
    updateTime: str

@typing.type_check_only
class SyncRepoRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UpdateProjectConfigRequest(typing.TypedDict, total=False):
    projectConfig: ProjectConfig
    updateMask: str

@typing.type_check_only
class UpdateRepoRequest(typing.TypedDict, total=False):
    repo: Repo
    updateMask: str
