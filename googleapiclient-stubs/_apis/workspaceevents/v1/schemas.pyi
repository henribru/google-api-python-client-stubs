import typing

import typing_extensions

_list = list

@typing.type_check_only
class Artifact(typing_extensions.TypedDict, total=False):
    artifactId: str
    description: str
    extensions: _list[str]
    metadata: dict[str, typing.Any]
    name: str
    parts: _list[Part]

@typing.type_check_only
class AuthenticationInfo(typing_extensions.TypedDict, total=False):
    credentials: str
    schemes: _list[str]

@typing.type_check_only
class CancelTaskRequest(typing_extensions.TypedDict, total=False):
    tenant: str

@typing.type_check_only
class DataPart(typing_extensions.TypedDict, total=False):
    data: dict[str, typing.Any]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FilePart(typing_extensions.TypedDict, total=False):
    fileWithBytes: str
    fileWithUri: str
    mimeType: str
    name: str

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class ListTaskPushNotificationConfigResponse(typing_extensions.TypedDict, total=False):
    configs: _list[TaskPushNotificationConfig]
    nextPageToken: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    content: _list[Part]
    contextId: str
    extensions: _list[str]
    messageId: str
    metadata: dict[str, typing.Any]
    role: typing_extensions.Literal["ROLE_UNSPECIFIED", "ROLE_USER", "ROLE_AGENT"]
    taskId: str

@typing.type_check_only
class NotificationEndpoint(typing_extensions.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Part(typing_extensions.TypedDict, total=False):
    data: DataPart
    file: FilePart
    metadata: dict[str, typing.Any]
    text: str

@typing.type_check_only
class PayloadOptions(typing_extensions.TypedDict, total=False):
    fieldMask: str
    includeResource: bool

@typing.type_check_only
class PushNotificationConfig(typing_extensions.TypedDict, total=False):
    authentication: AuthenticationInfo
    id: str
    token: str
    url: str

@typing.type_check_only
class ReactivateSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SendMessageConfiguration(typing_extensions.TypedDict, total=False):
    acceptedOutputModes: _list[str]
    blocking: bool
    historyLength: int
    pushNotification: PushNotificationConfig

@typing.type_check_only
class SendMessageRequest(typing_extensions.TypedDict, total=False):
    configuration: SendMessageConfiguration
    message: Message
    metadata: dict[str, typing.Any]
    tenant: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StreamResponse(typing_extensions.TypedDict, total=False):
    artifactUpdate: TaskArtifactUpdateEvent
    message: Message
    statusUpdate: TaskStatusUpdateEvent
    task: Task

@typing.type_check_only
class Subscription(typing_extensions.TypedDict, total=False):
    authority: str
    createTime: str
    etag: str
    eventTypes: _list[str]
    expireTime: str
    name: str
    notificationEndpoint: NotificationEndpoint
    payloadOptions: PayloadOptions
    reconciling: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED", "DELETED"
    ]
    suspensionReason: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "USER_SCOPE_REVOKED",
        "RESOURCE_DELETED",
        "USER_AUTHORIZATION_FAILURE",
        "ENDPOINT_PERMISSION_DENIED",
        "ENDPOINT_NOT_FOUND",
        "ENDPOINT_RESOURCE_EXHAUSTED",
        "OTHER",
    ]
    targetResource: str
    ttl: str
    uid: str
    updateTime: str

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    artifacts: _list[Artifact]
    contextId: str
    history: _list[Message]
    id: str
    metadata: dict[str, typing.Any]
    status: TaskStatus

@typing.type_check_only
class TaskArtifactUpdateEvent(typing_extensions.TypedDict, total=False):
    append: bool
    artifact: Artifact
    contextId: str
    lastChunk: bool
    metadata: dict[str, typing.Any]
    taskId: str

@typing.type_check_only
class TaskPushNotificationConfig(typing_extensions.TypedDict, total=False):
    name: str
    pushNotificationConfig: PushNotificationConfig

@typing.type_check_only
class TaskStatus(typing_extensions.TypedDict, total=False):
    message: Message
    state: typing_extensions.Literal[
        "TASK_STATE_UNSPECIFIED",
        "TASK_STATE_SUBMITTED",
        "TASK_STATE_WORKING",
        "TASK_STATE_COMPLETED",
        "TASK_STATE_FAILED",
        "TASK_STATE_CANCELLED",
        "TASK_STATE_INPUT_REQUIRED",
        "TASK_STATE_REJECTED",
        "TASK_STATE_AUTH_REQUIRED",
    ]
    timestamp: str

@typing.type_check_only
class TaskStatusUpdateEvent(typing_extensions.TypedDict, total=False):
    contextId: str
    final: bool
    metadata: dict[str, typing.Any]
    status: TaskStatus
    taskId: str
