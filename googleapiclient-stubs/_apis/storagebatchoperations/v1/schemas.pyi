import typing

import typing_extensions

_list = list

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    bucket: str
    manifest: Manifest
    prefixList: PrefixList

@typing.type_check_only
class BucketList(typing_extensions.TypedDict, total=False):
    buckets: _list[Bucket]

@typing.type_check_only
class CancelJobRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class CancelJobResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Counters(typing_extensions.TypedDict, total=False):
    failedObjectCount: str
    succeededObjectCount: str
    totalObjectCount: str

@typing.type_check_only
class DeleteObject(typing_extensions.TypedDict, total=False):
    permanentObjectDeletionEnabled: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorLogEntry(typing_extensions.TypedDict, total=False):
    errorDetails: _list[str]
    objectUri: str

@typing.type_check_only
class ErrorSummary(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    errorCount: str
    errorLogEntries: _list[ErrorLogEntry]

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    bucketList: BucketList
    completeTime: str
    counters: Counters
    createTime: str
    deleteObject: DeleteObject
    description: str
    errorSummaries: _list[ErrorSummary]
    loggingConfig: LoggingConfig
    name: str
    putMetadata: PutMetadata
    putObjectHold: PutObjectHold
    rewriteObject: RewriteObject
    scheduleTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "CANCELED", "FAILED"
    ]

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    logActionStates: _list[
        typing_extensions.Literal[
            "LOGGABLE_ACTION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"
        ]
    ]
    logActions: _list[
        typing_extensions.Literal["LOGGABLE_ACTION_UNSPECIFIED", "TRANSFORM"]
    ]

@typing.type_check_only
class Manifest(typing_extensions.TypedDict, total=False):
    manifestLocation: str

@typing.type_check_only
class ObjectRetention(typing_extensions.TypedDict, total=False):
    retainUntilTime: str
    retentionMode: typing_extensions.Literal[
        "RETENTION_MODE_UNSPECIFIED", "LOCKED", "UNLOCKED"
    ]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    job: Job
    operation: str
    requestedCancellation: bool

@typing.type_check_only
class PrefixList(typing_extensions.TypedDict, total=False):
    includedObjectPrefixes: _list[str]

@typing.type_check_only
class PutMetadata(typing_extensions.TypedDict, total=False):
    cacheControl: str
    contentDisposition: str
    contentEncoding: str
    contentLanguage: str
    contentType: str
    customMetadata: dict[str, typing.Any]
    customTime: str
    objectRetention: ObjectRetention

@typing.type_check_only
class PutObjectHold(typing_extensions.TypedDict, total=False):
    eventBasedHold: typing_extensions.Literal["HOLD_STATUS_UNSPECIFIED", "SET", "UNSET"]
    temporaryHold: typing_extensions.Literal["HOLD_STATUS_UNSPECIFIED", "SET", "UNSET"]

@typing.type_check_only
class RewriteObject(typing_extensions.TypedDict, total=False):
    kmsKey: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
