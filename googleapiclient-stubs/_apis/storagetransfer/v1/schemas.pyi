import typing

import typing_extensions

class ErrorLogEntry(typing_extensions.TypedDict, total=False):
    url: str
    errorDetails: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class AzureBlobStorageData(typing_extensions.TypedDict, total=False):
    azureCredentials: AzureCredentials
    container: str
    storageAccount: str

class Schedule(typing_extensions.TypedDict, total=False):
    startTimeOfDay: TimeOfDay
    scheduleStartDate: Date
    scheduleEndDate: Date

class ErrorSummary(typing_extensions.TypedDict, total=False):
    errorLogEntries: typing.List[ErrorLogEntry]
    errorCount: str
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

class TransferJob(typing_extensions.TypedDict, total=False):
    deletionTime: str
    transferSpec: TransferSpec
    description: str
    creationTime: str
    name: str
    notificationConfig: NotificationConfig
    lastModificationTime: str
    schedule: Schedule
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "ENABLED", "DISABLED", "DELETED"
    ]
    projectId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class ResumeTransferOperationRequest(typing_extensions.TypedDict, total=False): ...

class TransferOptions(typing_extensions.TypedDict, total=False):
    overwriteObjectsAlreadyExistingInSink: bool
    deleteObjectsFromSourceAfterTransfer: bool
    deleteObjectsUniqueInSink: bool

class GoogleServiceAccount(typing_extensions.TypedDict, total=False):
    accountEmail: str

class TransferCounters(typing_extensions.TypedDict, total=False):
    objectsFoundOnlyFromSink: str
    objectsCopiedToSink: str
    bytesDeletedFromSink: str
    objectsFoundFromSource: str
    bytesFromSourceFailed: str
    objectsDeletedFromSink: str
    bytesFoundOnlyFromSink: str
    objectsFailedToDeleteFromSink: str
    bytesFoundFromSource: str
    objectsDeletedFromSource: str
    bytesCopiedToSink: str
    bytesFromSourceSkippedBySync: str
    bytesDeletedFromSource: str
    bytesFailedToDeleteFromSink: str
    objectsFromSourceSkippedBySync: str
    objectsFromSourceFailed: str

class TimeOfDay(typing_extensions.TypedDict, total=False):
    minutes: int
    hours: int
    seconds: int
    nanos: int

class GcsData(typing_extensions.TypedDict, total=False):
    bucketName: str

class AwsS3Data(typing_extensions.TypedDict, total=False):
    awsAccessKey: AwsAccessKey
    bucketName: str

class UpdateTransferJobRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    updateTransferJobFieldMask: str
    transferJob: TransferJob

class AwsAccessKey(typing_extensions.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str

class HttpData(typing_extensions.TypedDict, total=False):
    listUrl: str

class AzureCredentials(typing_extensions.TypedDict, total=False):
    sasToken: str

class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

class PauseTransferOperationRequest(typing_extensions.TypedDict, total=False): ...

class TransferOperation(typing_extensions.TypedDict, total=False):
    startTime: str
    notificationConfig: NotificationConfig
    transferSpec: TransferSpec
    projectId: str
    errorBreakdowns: typing.List[ErrorSummary]
    transferJobName: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "IN_PROGRESS",
        "PAUSED",
        "SUCCESS",
        "FAILED",
        "ABORTED",
        "QUEUED",
    ]
    counters: TransferCounters
    name: str
    endTime: str

class ObjectConditions(typing_extensions.TypedDict, total=False):
    excludePrefixes: typing.List[str]
    lastModifiedBefore: str
    lastModifiedSince: str
    minTimeElapsedSinceLastModification: str
    includePrefixes: typing.List[str]
    maxTimeElapsedSinceLastModification: str

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    error: Status
    response: typing.Dict[str, typing.Any]

class NotificationConfig(typing_extensions.TypedDict, total=False):
    eventTypes: typing.List[str]
    payloadFormat: typing_extensions.Literal[
        "PAYLOAD_FORMAT_UNSPECIFIED", "NONE", "JSON"
    ]
    pubsubTopic: str

class TransferSpec(typing_extensions.TypedDict, total=False):
    gcsDataSource: GcsData
    awsS3DataSource: AwsS3Data
    gcsDataSink: GcsData
    httpDataSource: HttpData
    objectConditions: ObjectConditions
    transferOptions: TransferOptions
    azureBlobStorageDataSource: AzureBlobStorageData

class ListTransferJobsResponse(typing_extensions.TypedDict, total=False):
    transferJobs: typing.List[TransferJob]
    nextPageToken: str
