import typing

import typing_extensions

_list = list

@typing.type_check_only
class ListSubscriptionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

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
class PayloadOptions(typing_extensions.TypedDict, total=False):
    fieldMask: str
    includeResource: bool

@typing.type_check_only
class ReactivateSubscriptionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

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
