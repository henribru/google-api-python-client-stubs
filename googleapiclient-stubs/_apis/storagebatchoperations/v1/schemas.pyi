import typing

_list = list

@typing.type_check_only
class AccessControlsUpdates(typing.TypedDict, total=False):
    grants: _list[ObjectAccessControl]
    removeEntities: _list[str]

@typing.type_check_only
class Bucket(typing.TypedDict, total=False):
    bucket: str
    manifest: Manifest
    prefixList: PrefixList

@typing.type_check_only
class BucketList(typing.TypedDict, total=False):
    buckets: _list[Bucket]

@typing.type_check_only
class BucketOperation(typing.TypedDict, total=False):
    bucketName: str
    completeTime: str
    counters: Counters
    createTime: str
    deleteObject: DeleteObject
    errorSummaries: _list[ErrorSummary]
    manifest: Manifest
    name: str
    prefixList: PrefixList
    projectSource: ProjectSource
    putMetadata: PutMetadata
    putObjectHold: PutObjectHold
    rewriteObject: RewriteObject
    setObjectAcls: SetObjectAcls
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "QUEUED", "RUNNING", "SUCCEEDED", "CANCELED", "FAILED"
    ]
    updateObjectCustomContext: UpdateObjectCustomContext

@typing.type_check_only
class CancelJobRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class CancelJobResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Counters(typing.TypedDict, total=False):
    failedObjectCount: str
    objectCustomContextsCreated: str
    objectCustomContextsDeleted: str
    objectCustomContextsUpdated: str
    succeededObjectCount: str
    totalBytesFound: str
    totalBytesTransformed: str
    totalObjectCount: str

@typing.type_check_only
class CustomContextUpdates(typing.TypedDict, total=False):
    keysToClear: _list[str]
    updates: dict[str, typing.Any]

@typing.type_check_only
class DeleteObject(typing.TypedDict, total=False):
    permanentObjectDeletionEnabled: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorLogEntry(typing.TypedDict, total=False):
    errorDetails: _list[str]
    objectUri: str

@typing.type_check_only
class ErrorSummary(typing.TypedDict, total=False):
    errorCode: typing.Literal[
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
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    bucketList: BucketList
    completeTime: str
    counters: Counters
    createTime: str
    deleteObject: DeleteObject
    description: str
    dryRun: bool
    errorSummaries: _list[ErrorSummary]
    isMultiBucketJob: bool
    loggingConfig: LoggingConfig
    name: str
    projectSource: ProjectSource
    putMetadata: PutMetadata
    putObjectHold: PutObjectHold
    rewriteObject: RewriteObject
    scheduleTime: str
    setObjectAcls: SetObjectAcls
    state: typing.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "CANCELED", "FAILED", "QUEUED"
    ]
    updateObjectCustomContext: UpdateObjectCustomContext

@typing.type_check_only
class ListBucketOperationsResponse(typing.TypedDict, total=False):
    bucketOperations: _list[BucketOperation]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str
    unreachable: _list[str]

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
class LoggingConfig(typing.TypedDict, total=False):
    logActionStates: _list[
        typing.Literal["LOGGABLE_ACTION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED"]
    ]
    logActions: _list[typing.Literal["LOGGABLE_ACTION_UNSPECIFIED", "TRANSFORM"]]

@typing.type_check_only
class Manifest(typing.TypedDict, total=False):
    manifestLocation: str

@typing.type_check_only
class ObjectAccessControl(typing.TypedDict, total=False):
    entity: str
    role: str

@typing.type_check_only
class ObjectCustomContextPayload(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class ObjectRetention(typing.TypedDict, total=False):
    retainUntilTime: str
    retentionMode: typing.Literal["RETENTION_MODE_UNSPECIFIED", "LOCKED", "UNLOCKED"]

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
    createTime: str
    endTime: str
    job: Job
    operation: str
    requestedCancellation: bool

@typing.type_check_only
class PrefixList(typing.TypedDict, total=False):
    includedObjectPrefixes: _list[str]

@typing.type_check_only
class ProjectSource(typing.TypedDict, total=False):
    bucketFilters: Expr
    dryRunJobId: str
    insightsDatasetConfig: str
    objectFilters: Expr
    project: str
    snapshotTime: str
    targetLocations: TargetLocations

@typing.type_check_only
class PutMetadata(typing.TypedDict, total=False):
    cacheControl: str
    contentDisposition: str
    contentEncoding: str
    contentLanguage: str
    contentType: str
    customMetadata: dict[str, typing.Any]
    customTime: str
    objectRetention: ObjectRetention

@typing.type_check_only
class PutObjectHold(typing.TypedDict, total=False):
    eventBasedHold: typing.Literal["HOLD_STATUS_UNSPECIFIED", "SET", "UNSET"]
    temporaryHold: typing.Literal["HOLD_STATUS_UNSPECIFIED", "SET", "UNSET"]

@typing.type_check_only
class RewriteObject(typing.TypedDict, total=False):
    kmsKey: str
    storageClass: typing.Literal[
        "STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]

@typing.type_check_only
class SetObjectAcls(typing.TypedDict, total=False):
    accessControlsUpdates: AccessControlsUpdates

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TargetLocations(typing.TypedDict, total=False):
    locations: _list[str]
    snapshotTime: str

@typing.type_check_only
class UpdateObjectCustomContext(typing.TypedDict, total=False):
    clearAll: bool
    customContextUpdates: CustomContextUpdates
