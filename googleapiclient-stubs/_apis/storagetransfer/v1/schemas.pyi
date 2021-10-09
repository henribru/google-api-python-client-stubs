import typing

import typing_extensions

_list = list

@typing.type_check_only
class AwsAccessKey(typing_extensions.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str

@typing.type_check_only
class AwsS3Data(typing_extensions.TypedDict, total=False):
    awsAccessKey: AwsAccessKey
    bucketName: str
    path: str
    roleArn: str

@typing.type_check_only
class AzureBlobStorageData(typing_extensions.TypedDict, total=False):
    azureCredentials: AzureCredentials
    container: str
    path: str
    storageAccount: str

@typing.type_check_only
class AzureCredentials(typing_extensions.TypedDict, total=False):
    sasToken: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ErrorLogEntry(typing_extensions.TypedDict, total=False):
    errorDetails: _list[str]
    url: str

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
class GcsData(typing_extensions.TypedDict, total=False):
    bucketName: str
    path: str

@typing.type_check_only
class GoogleServiceAccount(typing_extensions.TypedDict, total=False):
    accountEmail: str
    subjectId: str

@typing.type_check_only
class HttpData(typing_extensions.TypedDict, total=False):
    listUrl: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListTransferJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferJobs: _list[TransferJob]

@typing.type_check_only
class LoggingConfig(typing_extensions.TypedDict, total=False):
    enableOnpremGcsTransferLogs: bool

@typing.type_check_only
class NotificationConfig(typing_extensions.TypedDict, total=False):
    eventTypes: _list[str]
    payloadFormat: typing_extensions.Literal[
        "PAYLOAD_FORMAT_UNSPECIFIED", "NONE", "JSON"
    ]
    pubsubTopic: str

@typing.type_check_only
class ObjectConditions(typing_extensions.TypedDict, total=False):
    excludePrefixes: _list[str]
    includePrefixes: _list[str]
    lastModifiedBefore: str
    lastModifiedSince: str
    maxTimeElapsedSinceLastModification: str
    minTimeElapsedSinceLastModification: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PauseTransferOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PosixFilesystem(typing_extensions.TypedDict, total=False):
    rootDirectory: str

@typing.type_check_only
class ResumeTransferOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RunTransferJobRequest(typing_extensions.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class Schedule(typing_extensions.TypedDict, total=False):
    endTimeOfDay: TimeOfDay
    repeatInterval: str
    scheduleEndDate: Date
    scheduleStartDate: Date
    startTimeOfDay: TimeOfDay

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TransferCounters(typing_extensions.TypedDict, total=False):
    bytesCopiedToSink: str
    bytesDeletedFromSink: str
    bytesDeletedFromSource: str
    bytesFailedToDeleteFromSink: str
    bytesFoundFromSource: str
    bytesFoundOnlyFromSink: str
    bytesFromSourceFailed: str
    bytesFromSourceSkippedBySync: str
    directoriesFailedToListFromSource: str
    directoriesFoundFromSource: str
    directoriesSuccessfullyListedFromSource: str
    objectsCopiedToSink: str
    objectsDeletedFromSink: str
    objectsDeletedFromSource: str
    objectsFailedToDeleteFromSink: str
    objectsFoundFromSource: str
    objectsFoundOnlyFromSink: str
    objectsFromSourceFailed: str
    objectsFromSourceSkippedBySync: str

@typing.type_check_only
class TransferJob(typing_extensions.TypedDict, total=False):
    creationTime: str
    deletionTime: str
    description: str
    lastModificationTime: str
    latestOperationName: str
    loggingConfig: LoggingConfig
    name: str
    notificationConfig: NotificationConfig
    projectId: str
    schedule: Schedule
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "ENABLED", "DISABLED", "DELETED"
    ]
    transferSpec: TransferSpec

@typing.type_check_only
class TransferOperation(typing_extensions.TypedDict, total=False):
    counters: TransferCounters
    endTime: str
    errorBreakdowns: _list[ErrorSummary]
    name: str
    notificationConfig: NotificationConfig
    projectId: str
    startTime: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "IN_PROGRESS",
        "PAUSED",
        "SUCCESS",
        "FAILED",
        "ABORTED",
        "QUEUED",
    ]
    transferJobName: str
    transferSpec: TransferSpec

@typing.type_check_only
class TransferOptions(typing_extensions.TypedDict, total=False):
    deleteObjectsFromSourceAfterTransfer: bool
    deleteObjectsUniqueInSink: bool
    overwriteObjectsAlreadyExistingInSink: bool

@typing.type_check_only
class TransferSpec(typing_extensions.TypedDict, total=False):
    awsS3DataSource: AwsS3Data
    azureBlobStorageDataSource: AzureBlobStorageData
    gcsDataSink: GcsData
    gcsDataSource: GcsData
    httpDataSource: HttpData
    objectConditions: ObjectConditions
    posixDataSource: PosixFilesystem
    transferOptions: TransferOptions

@typing.type_check_only
class UpdateTransferJobRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    transferJob: TransferJob
    updateTransferJobFieldMask: str
