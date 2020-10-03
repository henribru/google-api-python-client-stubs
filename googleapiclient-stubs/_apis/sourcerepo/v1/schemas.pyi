import typing

import typing_extensions

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class UpdateRepoRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    repo: Repo

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str

class Repo(typing_extensions.TypedDict, total=False):
    pubsubConfigs: typing.Dict[str, typing.Any]
    mirrorConfig: MirrorConfig
    name: str
    size: str
    url: str

class PubsubConfig(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    topic: str
    messageFormat: typing_extensions.Literal[
        "MESSAGE_FORMAT_UNSPECIFIED", "PROTOBUF", "JSON"
    ]

class UpdateProjectConfigRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    projectConfig: ProjectConfig

class Empty(typing_extensions.TypedDict, total=False): ...

class ProjectConfig(typing_extensions.TypedDict, total=False):
    enablePrivateKeyCheck: bool
    name: str
    pubsubConfigs: typing.Dict[str, typing.Any]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int

class SyncRepoMetadata(typing_extensions.TypedDict, total=False):
    updateTime: str
    name: str
    startTime: str
    statusMessage: str

class ListReposResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repos: typing.List[Repo]

class SyncRepoRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr

class MirrorConfig(typing_extensions.TypedDict, total=False):
    webhookId: str
    deployKeyId: str
    url: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool
    name: str
    response: typing.Dict[str, typing.Any]
