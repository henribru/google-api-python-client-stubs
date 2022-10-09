import typing

import typing_extensions

_list = list

@typing.type_check_only
class AgentPool(typing_extensions.TypedDict, total=False):
    bandwidthLimit: BandwidthLimit
    displayName: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "DELETING"
    ]

@typing.type_check_only
class AwsAccessKey(typing_extensions.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str

@typing.type_check_only
class AwsS3CompatibleData(typing_extensions.TypedDict, total=False):
    bucketName: str
    endpoint: str
    path: str
    region: str
    s3Metadata: S3CompatibleMetadata

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
class BandwidthLimit(typing_extensions.TypedDict, total=False):
    limitMbps: str

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
class ListAgentPoolsResponse(typing_extensions.TypedDict, total=False):
    agentPools: _list[AgentPool]
    nextPageToken: str

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
    logActionStates: _list[str]
    logActions: _list[str]

@typing.type_check_only
class MetadataOptions(typing_extensions.TypedDict, total=False):
    acl: typing_extensions.Literal[
        "ACL_UNSPECIFIED", "ACL_DESTINATION_BUCKET_DEFAULT", "ACL_PRESERVE"
    ]
    gid: typing_extensions.Literal["GID_UNSPECIFIED", "GID_SKIP", "GID_NUMBER"]
    kmsKey: typing_extensions.Literal[
        "KMS_KEY_UNSPECIFIED", "KMS_KEY_DESTINATION_BUCKET_DEFAULT", "KMS_KEY_PRESERVE"
    ]
    mode: typing_extensions.Literal["MODE_UNSPECIFIED", "MODE_SKIP", "MODE_PRESERVE"]
    storageClass: typing_extensions.Literal[
        "STORAGE_CLASS_UNSPECIFIED",
        "STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT",
        "STORAGE_CLASS_PRESERVE",
        "STORAGE_CLASS_STANDARD",
        "STORAGE_CLASS_NEARLINE",
        "STORAGE_CLASS_COLDLINE",
        "STORAGE_CLASS_ARCHIVE",
    ]
    symlink: typing_extensions.Literal[
        "SYMLINK_UNSPECIFIED", "SYMLINK_SKIP", "SYMLINK_PRESERVE"
    ]
    temporaryHold: typing_extensions.Literal[
        "TEMPORARY_HOLD_UNSPECIFIED", "TEMPORARY_HOLD_SKIP", "TEMPORARY_HOLD_PRESERVE"
    ]
    timeCreated: typing_extensions.Literal[
        "TIME_CREATED_UNSPECIFIED",
        "TIME_CREATED_SKIP",
        "TIME_CREATED_PRESERVE_AS_CUSTOM_TIME",
    ]
    uid: typing_extensions.Literal["UID_UNSPECIFIED", "UID_SKIP", "UID_NUMBER"]

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
class S3CompatibleMetadata(typing_extensions.TypedDict, total=False):
    authMethod: typing_extensions.Literal[
        "AUTH_METHOD_UNSPECIFIED",
        "AUTH_METHOD_AWS_SIGNATURE_V4",
        "AUTH_METHOD_AWS_SIGNATURE_V2",
    ]
    listApi: typing_extensions.Literal[
        "LIST_API_UNSPECIFIED", "LIST_OBJECTS_V2", "LIST_OBJECTS"
    ]
    protocol: typing_extensions.Literal[
        "NETWORK_PROTOCOL_UNSPECIFIED",
        "NETWORK_PROTOCOL_HTTPS",
        "NETWORK_PROTOCOL_HTTP",
    ]
    requestModel: typing_extensions.Literal[
        "REQUEST_MODEL_UNSPECIFIED",
        "REQUEST_MODEL_VIRTUAL_HOSTED_STYLE",
        "REQUEST_MODEL_PATH_STYLE",
    ]

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
    intermediateObjectsCleanedUp: str
    intermediateObjectsFailedCleanedUp: str
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
class TransferManifest(typing_extensions.TypedDict, total=False):
    location: str

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
    metadataOptions: MetadataOptions
    overwriteObjectsAlreadyExistingInSink: bool
    overwriteWhen: typing_extensions.Literal[
        "OVERWRITE_WHEN_UNSPECIFIED", "DIFFERENT", "NEVER", "ALWAYS"
    ]

@typing.type_check_only
class TransferSpec(typing_extensions.TypedDict, total=False):
    awsS3CompatibleDataSource: AwsS3CompatibleData
    awsS3DataSource: AwsS3Data
    azureBlobStorageDataSource: AzureBlobStorageData
    gcsDataSink: GcsData
    gcsDataSource: GcsData
    gcsIntermediateDataLocation: GcsData
    httpDataSource: HttpData
    objectConditions: ObjectConditions
    posixDataSink: PosixFilesystem
    posixDataSource: PosixFilesystem
    sinkAgentPoolName: str
    sourceAgentPoolName: str
    transferManifest: TransferManifest
    transferOptions: TransferOptions

@typing.type_check_only
class UpdateTransferJobRequest(typing_extensions.TypedDict, total=False):
    projectId: str
    transferJob: TransferJob
    updateTransferJobFieldMask: str
