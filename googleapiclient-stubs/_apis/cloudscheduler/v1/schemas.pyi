import typing

import typing_extensions

class AppEngineHttpTarget(typing_extensions.TypedDict, total=False):
    body: str
    headers: typing.Dict[str, typing.Any]
    appEngineRouting: AppEngineRouting
    relativeUri: str
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

class ResumeJobRequest(typing_extensions.TypedDict, total=False): ...

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    jobs: typing.List[Job]

class RunJobRequest(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class HttpTarget(typing_extensions.TypedDict, total=False):
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
    oauthToken: OAuthToken
    headers: typing.Dict[str, typing.Any]
    uri: str
    body: str

class OAuthToken(typing_extensions.TypedDict, total=False):
    serviceAccountEmail: str
    scope: str

class RetryConfig(typing_extensions.TypedDict, total=False):
    minBackoffDuration: str
    maxBackoffDuration: str
    retryCount: int
    maxRetryDuration: str
    maxDoublings: int

class PubsubTarget(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    topicName: str
    data: str

class PubsubMessage(typing_extensions.TypedDict, total=False):
    data: str
    orderingKey: str
    attributes: typing.Dict[str, typing.Any]
    publishTime: str
    messageId: str

class PauseJobRequest(typing_extensions.TypedDict, total=False): ...

class AppEngineRouting(typing_extensions.TypedDict, total=False):
    host: str
    service: str
    instance: str
    version: str

class OidcToken(typing_extensions.TypedDict, total=False):
    audience: str
    serviceAccountEmail: str

class Job(typing_extensions.TypedDict, total=False):
    schedule: str
    appEngineHttpTarget: AppEngineHttpTarget
    userUpdateTime: str
    description: str
    httpTarget: HttpTarget
    lastAttemptTime: str
    retryConfig: RetryConfig
    status: Status
    attemptDeadline: str
    name: str
    timeZone: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "PAUSED", "DISABLED", "UPDATE_FAILED"
    ]
    scheduleTime: str
    pubsubTarget: PubsubTarget

class Location(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    displayName: str
    locationId: str
    name: str
    labels: typing.Dict[str, typing.Any]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]
