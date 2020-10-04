import typing

import typing_extensions
@typing.type_check_only
class AppEngineHttpTarget(typing_extensions.TypedDict, total=False):
    appEngineRouting: AppEngineRouting
    body: str
    headers: typing.Dict[str, typing.Any]
    httpMethod: typing_extensions.Literal[
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
class AppEngineRouting(typing_extensions.TypedDict, total=False):
    host: str
    instance: str
    service: str
    version: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class HttpTarget(typing_extensions.TypedDict, total=False):
    body: str
    headers: typing.Dict[str, typing.Any]
    httpMethod: typing_extensions.Literal[
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
class Job(typing_extensions.TypedDict, total=False):
    appEngineHttpTarget: AppEngineHttpTarget
    attemptDeadline: str
    description: str
    httpTarget: HttpTarget
    lastAttemptTime: str
    name: str
    pubsubTarget: PubsubTarget
    retryConfig: RetryConfig
    schedule: str
    scheduleTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "PAUSED", "DISABLED", "UPDATE_FAILED"
    ]
    status: Status
    timeZone: str
    userUpdateTime: str

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class OAuthToken(typing_extensions.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

@typing.type_check_only
class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

@typing.type_check_only
class PauseJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PubsubMessage(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    data: str
    messageId: str
    orderingKey: str
    publishTime: str

@typing.type_check_only
class PubsubTarget(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    data: str
    topicName: str

@typing.type_check_only
class ResumeJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RetryConfig(typing_extensions.TypedDict, total=False):
    maxBackoffDuration: str
    maxDoublings: int
    maxRetryDuration: str
    minBackoffDuration: str
    retryCount: int

@typing.type_check_only
class RunJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
