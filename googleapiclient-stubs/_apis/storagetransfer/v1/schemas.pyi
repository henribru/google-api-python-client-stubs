import typing

_list = list

@typing.type_check_only
class AgentPool(typing.TypedDict, total=False):
    bandwidthLimit: BandwidthLimit
    displayName: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "CREATING", "CREATED", "DELETING"]

@typing.type_check_only
class AwsAccessKey(typing.TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str

@typing.type_check_only
class AwsS3CompatibleData(typing.TypedDict, total=False):
    bucketName: str
    endpoint: str
    path: str
    region: str
    s3Metadata: S3CompatibleMetadata

@typing.type_check_only
class AwsS3Data(typing.TypedDict, total=False):
    awsAccessKey: AwsAccessKey
    bucketName: str
    cloudfrontDomain: str
    credentialsSecret: str
    managedPrivateNetwork: bool
    path: str
    privateNetworkService: str
    roleArn: str

@typing.type_check_only
class AzureBlobStorageData(typing.TypedDict, total=False):
    azureCredentials: AzureCredentials
    container: str
    credentialsSecret: str
    federatedIdentityConfig: FederatedIdentityConfig
    path: str
    privateNetworkService: str
    storageAccount: str

@typing.type_check_only
class AzureCredentials(typing.TypedDict, total=False):
    sasToken: str

@typing.type_check_only
class BandwidthLimit(typing.TypedDict, total=False):
    limitMbps: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ErrorLogEntry(typing.TypedDict, total=False):
    errorDetails: _list[str]
    url: str

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
class EventStream(typing.TypedDict, total=False):
    eventStreamExpirationTime: str
    eventStreamStartTime: str
    name: str

@typing.type_check_only
class FederatedIdentityConfig(typing.TypedDict, total=False):
    clientId: str
    tenantId: str

@typing.type_check_only
class GcsData(typing.TypedDict, total=False):
    bucketName: str
    managedFolderTransferEnabled: bool
    path: str

@typing.type_check_only
class GoogleServiceAccount(typing.TypedDict, total=False):
    accountEmail: str
    subjectId: str

@typing.type_check_only
class HdfsData(typing.TypedDict, total=False):
    path: str

@typing.type_check_only
class HttpData(typing.TypedDict, total=False):
    listUrl: str

@typing.type_check_only
class ListAgentPoolsResponse(typing.TypedDict, total=False):
    agentPools: _list[AgentPool]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListTransferJobsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    transferJobs: _list[TransferJob]

@typing.type_check_only
class LoggingConfig(typing.TypedDict, total=False):
    enableOnpremGcsTransferLogs: bool
    logActionStates: _list[
        typing.Literal[
            "LOGGABLE_ACTION_STATE_UNSPECIFIED", "SUCCEEDED", "FAILED", "SKIPPED"
        ]
    ]
    logActions: _list[
        typing.Literal["LOGGABLE_ACTION_UNSPECIFIED", "FIND", "DELETE", "COPY"]
    ]

@typing.type_check_only
class MetadataOptions(typing.TypedDict, total=False):
    acl: typing.Literal[
        "ACL_UNSPECIFIED", "ACL_DESTINATION_BUCKET_DEFAULT", "ACL_PRESERVE"
    ]
    gid: typing.Literal["GID_UNSPECIFIED", "GID_SKIP", "GID_NUMBER"]
    kmsKey: typing.Literal[
        "KMS_KEY_UNSPECIFIED", "KMS_KEY_DESTINATION_BUCKET_DEFAULT", "KMS_KEY_PRESERVE"
    ]
    mode: typing.Literal["MODE_UNSPECIFIED", "MODE_SKIP", "MODE_PRESERVE"]
    storageClass: typing.Literal[
        "STORAGE_CLASS_UNSPECIFIED",
        "STORAGE_CLASS_DESTINATION_BUCKET_DEFAULT",
        "STORAGE_CLASS_PRESERVE",
        "STORAGE_CLASS_STANDARD",
        "STORAGE_CLASS_NEARLINE",
        "STORAGE_CLASS_COLDLINE",
        "STORAGE_CLASS_ARCHIVE",
    ]
    symlink: typing.Literal["SYMLINK_UNSPECIFIED", "SYMLINK_SKIP", "SYMLINK_PRESERVE"]
    temporaryHold: typing.Literal[
        "TEMPORARY_HOLD_UNSPECIFIED", "TEMPORARY_HOLD_SKIP", "TEMPORARY_HOLD_PRESERVE"
    ]
    timeCreated: typing.Literal[
        "TIME_CREATED_UNSPECIFIED",
        "TIME_CREATED_SKIP",
        "TIME_CREATED_PRESERVE_AS_CUSTOM_TIME",
    ]
    uid: typing.Literal["UID_UNSPECIFIED", "UID_SKIP", "UID_NUMBER"]

@typing.type_check_only
class NotificationConfig(typing.TypedDict, total=False):
    eventTypes: _list[
        typing.Literal[
            "EVENT_TYPE_UNSPECIFIED",
            "TRANSFER_OPERATION_SUCCESS",
            "TRANSFER_OPERATION_FAILED",
            "TRANSFER_OPERATION_ABORTED",
        ]
    ]
    payloadFormat: typing.Literal["PAYLOAD_FORMAT_UNSPECIFIED", "NONE", "JSON"]
    pubsubTopic: str

@typing.type_check_only
class ObjectConditions(typing.TypedDict, total=False):
    excludePrefixes: _list[str]
    includePrefixes: _list[str]
    includeStorageClasses: _list[str]
    lastModifiedBefore: str
    lastModifiedSince: str
    matchGlob: str
    maxTimeElapsedSinceLastModification: str
    minTimeElapsedSinceLastModification: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PauseTransferOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class PosixFilesystem(typing.TypedDict, total=False):
    rootDirectory: str

@typing.type_check_only
class ReplicationSpec(typing.TypedDict, total=False):
    gcsDataSink: GcsData
    gcsDataSource: GcsData
    objectConditions: ObjectConditions
    transferOptions: TransferOptions

@typing.type_check_only
class ResumeTransferOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class RunTransferJobRequest(typing.TypedDict, total=False):
    projectId: str

@typing.type_check_only
class S3CompatibleMetadata(typing.TypedDict, total=False):
    authMethod: typing.Literal[
        "AUTH_METHOD_UNSPECIFIED",
        "AUTH_METHOD_AWS_SIGNATURE_V4",
        "AUTH_METHOD_AWS_SIGNATURE_V2",
    ]
    listApi: typing.Literal["LIST_API_UNSPECIFIED", "LIST_OBJECTS_V2", "LIST_OBJECTS"]
    protocol: typing.Literal[
        "NETWORK_PROTOCOL_UNSPECIFIED",
        "NETWORK_PROTOCOL_HTTPS",
        "NETWORK_PROTOCOL_HTTP",
    ]
    requestModel: typing.Literal[
        "REQUEST_MODEL_UNSPECIFIED",
        "REQUEST_MODEL_VIRTUAL_HOSTED_STYLE",
        "REQUEST_MODEL_PATH_STYLE",
    ]

@typing.type_check_only
class Schedule(typing.TypedDict, total=False):
    endTimeOfDay: TimeOfDay
    repeatInterval: str
    scheduleEndDate: Date
    scheduleStartDate: Date
    startTimeOfDay: TimeOfDay

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class TransferCounters(typing.TypedDict, total=False):
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
    unrestoredDeepArchiveObjectsSkippedCount: str
    unsupportedS3GlacierObjectsSkippedCount: str

@typing.type_check_only
class TransferJob(typing.TypedDict, total=False):
    creationTime: str
    deletionTime: str
    description: str
    eventStream: EventStream
    lastModificationTime: str
    latestOperationName: str
    loggingConfig: LoggingConfig
    name: str
    notificationConfig: NotificationConfig
    projectId: str
    replicationSpec: ReplicationSpec
    schedule: Schedule
    serviceAccount: str
    status: typing.Literal["STATUS_UNSPECIFIED", "ENABLED", "DISABLED", "DELETED"]
    transferSpec: TransferSpec

@typing.type_check_only
class TransferManifest(typing.TypedDict, total=False):
    location: str

@typing.type_check_only
class TransferOperation(typing.TypedDict, total=False):
    counters: TransferCounters
    endTime: str
    errorBreakdowns: _list[ErrorSummary]
    loggingConfig: LoggingConfig
    name: str
    notificationConfig: NotificationConfig
    projectId: str
    startTime: str
    status: typing.Literal[
        "STATUS_UNSPECIFIED",
        "IN_PROGRESS",
        "PAUSED",
        "SUCCESS",
        "FAILED",
        "ABORTED",
        "QUEUED",
        "SUSPENDING",
    ]
    transferJobName: str
    transferSpec: TransferSpec

@typing.type_check_only
class TransferOptions(typing.TypedDict, total=False):
    deleteObjectsFromSourceAfterTransfer: bool
    deleteObjectsUniqueInSink: bool
    metadataOptions: MetadataOptions
    overwriteObjectsAlreadyExistingInSink: bool
    overwriteWhen: typing.Literal[
        "OVERWRITE_WHEN_UNSPECIFIED", "DIFFERENT", "NEVER", "ALWAYS"
    ]

@typing.type_check_only
class TransferSpec(typing.TypedDict, total=False):
    awsS3CompatibleDataSource: AwsS3CompatibleData
    awsS3DataSource: AwsS3Data
    azureBlobStorageDataSource: AzureBlobStorageData
    gcsDataSink: GcsData
    gcsDataSource: GcsData
    gcsIntermediateDataLocation: GcsData
    hdfsDataSource: HdfsData
    httpDataSource: HttpData
    objectConditions: ObjectConditions
    posixDataSink: PosixFilesystem
    posixDataSource: PosixFilesystem
    sinkAgentPoolName: str
    sourceAgentPoolName: str
    transferManifest: TransferManifest
    transferOptions: TransferOptions

@typing.type_check_only
class UpdateTransferJobRequest(typing.TypedDict, total=False):
    projectId: str
    transferJob: TransferJob
    updateTransferJobFieldMask: str
