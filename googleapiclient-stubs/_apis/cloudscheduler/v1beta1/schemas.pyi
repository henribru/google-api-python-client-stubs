import typing

_list = list

@typing.type_check_only
class AppEngineHttpTarget(typing.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    body: str
    headers: dict[str, typing.Any]
    httpMethod: typing.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    relativeUri: str

@typing.type_check_only
class AppEngineRouting(typing.TypedDict, total=False):
    host: str
    instance: str
    service: str
    version: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class HttpTarget(typing.TypedDict, total=False):
    body: str
    headers: dict[str, typing.Any]
    httpMethod: typing.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "POST",
        "GET",
        "HEAD",
        "PUT",
        "DELETE",
        "PATCH",
        "OPTIONS",
    ]
    oauthToken: OAuthToken
    oidcToken: OidcToken
    uri: str

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    appEngineHttpTarget: AppEngineHttpTarget
    attemptDeadline: str
    description: str
    httpTarget: HttpTarget
    lastAttemptTime: str
    legacyAppEngineCron: bool
    name: str
    pubsubTarget: PubsubTarget
    retryConfig: RetryConfig
    satisfiesPzs: bool
    schedule: str
    scheduleTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "PAUSED", "DISABLED", "UPDATE_FAILED"
    ]
    status: Status
    timeZone: str
    userUpdateTime: str

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthToken(typing.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

@typing.type_check_only
class OidcToken(typing.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class PauseJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PubsubMessage(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    data: str
    messageId: str
    orderingKey: str
    publishTime: str

@typing.type_check_only
class PubsubTarget(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    data: str
    topicName: str

@typing.type_check_only
class ResumeJobRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RetryConfig(typing.TypedDict, total=False):
    maxBackoffDuration: str
    maxDoublings: int
    maxRetryDuration: str
    minBackoffDuration: str
    retryCount: int

@typing.type_check_only
class RunJobRequest(typing.TypedDict, total=False):
    legacyAppEngineCron: bool

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
