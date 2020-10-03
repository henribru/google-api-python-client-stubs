import typing

import typing_extensions

class PubsubTarget(typing_extensions.TypedDict, total=False):
    data: str
    attributes: typing.Dict[str, typing.Any]
    topicName: str

class RetryConfig(typing_extensions.TypedDict, total=False):
    retryCount: int
    minBackoffDuration: str
    maxRetryDuration: str
    maxBackoffDuration: str
    maxDoublings: int

class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    nextPageToken: str

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class HttpTarget(typing_extensions.TypedDict, total=False):
    oauthToken: OAuthToken
    headers: typing.Dict[str, typing.Any]
    body: str
    uri: str
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
    oidcToken: OidcToken

class ResumeJobRequest(typing_extensions.TypedDict, total=False): ...

class Job(typing_extensions.TypedDict, total=False):
    scheduleTime: str
    timeZone: str
    name: str
    description: str
    status: Status
    appEngineHttpTarget: AppEngineHttpTarget
    httpTarget: HttpTarget
    userUpdateTime: str
    attemptDeadline: str
    schedule: str
    pubsubTarget: PubsubTarget
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "PAUSED", "DISABLED", "UPDATE_FAILED"
    ]
    lastAttemptTime: str
    retryConfig: RetryConfig

class Empty(typing_extensions.TypedDict, total=False): ...

class AppEngineRouting(typing_extensions.TypedDict, total=False):
    service: str
    version: str
    instance: str
    host: str

class AppEngineHttpTarget(typing_extensions.TypedDict, total=False):
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
    appEngineRouting: AppEngineRouting
    relativeUri: str
    body: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class PauseJobRequest(typing_extensions.TypedDict, total=False): ...

class PubsubMessage(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    messageId: str
    orderingKey: str
    data: str
    publishTime: str

class OAuthToken(typing_extensions.TypedDict, total=False):
    scope: str
    serviceAccountEmail: str

class RunJobRequest(typing_extensions.TypedDict, total=False): ...
