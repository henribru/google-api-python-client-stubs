import typing

_list = list

@typing.type_check_only
class DriveOptions(typing.TypedDict, total=False):
    includeDescendants: bool

@typing.type_check_only
class ListSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    subscriptions: _list[Subscription]

@typing.type_check_only
class NotificationEndpoint(typing.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PayloadOptions(typing.TypedDict, total=False):
    fieldMask: str
    includeResource: bool

@typing.type_check_only
class ReactivateSubscriptionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Subscription(typing.TypedDict, total=False):
    authority: str
    createTime: str
    driveOptions: DriveOptions
    etag: str
    eventTypes: _list[str]
    expireTime: str
    name: str
    notificationEndpoint: NotificationEndpoint
    payloadOptions: PayloadOptions
    reconciling: bool
    serviceAccountAuthority: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED", "DELETED"]
    suspensionReason: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "USER_SCOPE_REVOKED",
        "APP_SCOPE_REVOKED",
        "RESOURCE_DELETED",
        "USER_AUTHORIZATION_FAILURE",
        "APP_AUTHORIZATION_FAILURE",
        "ENDPOINT_PERMISSION_DENIED",
        "ENDPOINT_NOT_FOUND",
        "ENDPOINT_RESOURCE_EXHAUSTED",
        "OTHER",
    ]
    targetResource: str
    ttl: str
    uid: str
    updateTime: str
    userAuthority: str
