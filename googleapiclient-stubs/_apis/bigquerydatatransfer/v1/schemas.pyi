import typing

import typing_extensions

_list = list

@typing.type_check_only
class CheckValidCredsRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckValidCredsResponse(typing_extensions.TypedDict, total=False):
    hasValidCreds: bool

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    authorizationType: typing_extensions.Literal[
        "AUTHORIZATION_TYPE_UNSPECIFIED",
        "AUTHORIZATION_CODE",
        "GOOGLE_PLUS_AUTHORIZATION_CODE",
        "FIRST_PARTY_OAUTH",
    ]
    clientId: str
    dataRefreshType: typing_extensions.Literal[
        "DATA_REFRESH_TYPE_UNSPECIFIED", "SLIDING_WINDOW", "CUSTOM_SLIDING_WINDOW"
    ]
    dataSourceId: str
    defaultDataRefreshWindowDays: int
    defaultSchedule: str
    description: str
    displayName: str
    helpUrl: str
    manualRunsDisabled: bool
    minimumScheduleInterval: str
    name: str
    parameters: _list[DataSourceParameter]
    scopes: _list[str]
    supportsCustomSchedule: bool
    supportsMultipleTransfers: bool
    transferType: typing_extensions.Literal[
        "TRANSFER_TYPE_UNSPECIFIED", "BATCH", "STREAMING"
    ]
    updateDeadlineSeconds: int

@typing.type_check_only
class DataSourceParameter(typing_extensions.TypedDict, total=False):
    allowedValues: _list[str]
    deprecated: bool
    description: str
    displayName: str
    fields: _list[DataSourceParameter]
    immutable: bool
    maxListSize: str
    maxValue: float
    minValue: float
    paramId: str
    recurse: bool
    repeated: bool
    required: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "STRING",
        "INTEGER",
        "DOUBLE",
        "BOOLEAN",
        "RECORD",
        "PLUS_PAGE",
        "LIST",
    ]
    validationDescription: str
    validationHelpUrl: str
    validationRegex: str

@typing.type_check_only
class EmailPreferences(typing_extensions.TypedDict, total=False):
    enableFailureEmail: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionConfiguration(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class EnrollDataSourcesRequest(typing_extensions.TypedDict, total=False):
    dataSourceIds: _list[str]

@typing.type_check_only
class EventDrivenSchedule(typing_extensions.TypedDict, total=False):
    pubsubSubscription: str

@typing.type_check_only
class HierarchyDetail(typing_extensions.TypedDict, total=False):
    partitionDetail: PartitionDetail
    tableDetail: TableDetail

@typing.type_check_only
class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSources: _list[DataSource]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListTransferConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferConfigs: _list[TransferConfig]

@typing.type_check_only
class ListTransferLogsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferMessages: _list[TransferMessage]

@typing.type_check_only
class ListTransferResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferResources: _list[TransferResource]

@typing.type_check_only
class ListTransferRunsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferRuns: _list[TransferRun]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ManualSchedule(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class PartitionDetail(typing_extensions.TypedDict, total=False):
    table: str

@typing.type_check_only
class ScheduleOptions(typing_extensions.TypedDict, total=False):
    disableAutoScheduling: bool
    endTime: str
    startTime: str

@typing.type_check_only
class ScheduleOptionsV2(typing_extensions.TypedDict, total=False):
    eventDrivenSchedule: EventDrivenSchedule
    manualSchedule: ManualSchedule
    timeBasedSchedule: TimeBasedSchedule

@typing.type_check_only
class ScheduleTransferRunsRequest(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ScheduleTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: _list[TransferRun]

@typing.type_check_only
class StartManualTransferRunsRequest(typing_extensions.TypedDict, total=False):
    requestedRunTime: str
    requestedTimeRange: TimeRange

@typing.type_check_only
class StartManualTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: _list[TransferRun]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TableDetail(typing_extensions.TypedDict, total=False):
    partitionCount: str

@typing.type_check_only
class TimeBasedSchedule(typing_extensions.TypedDict, total=False):
    endTime: str
    schedule: str
    startTime: str

@typing.type_check_only
class TimeRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class TransferConfig(typing_extensions.TypedDict, total=False):
    dataRefreshWindowDays: int
    dataSourceId: str
    datasetRegion: str
    destinationDatasetId: str
    disabled: bool
    displayName: str
    emailPreferences: EmailPreferences
    encryptionConfiguration: EncryptionConfiguration
    error: Status
    managedTableType: typing_extensions.Literal[
        "MANAGED_TABLE_TYPE_UNSPECIFIED", "NATIVE", "BIGLAKE"
    ]
    name: str
    nextRunTime: str
    notificationPubsubTopic: str
    ownerInfo: UserInfo
    params: dict[str, typing.Any]
    schedule: str
    scheduleOptions: ScheduleOptions
    scheduleOptionsV2: ScheduleOptionsV2
    state: typing_extensions.Literal[
        "TRANSFER_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    ]
    updateTime: str
    userId: str

@typing.type_check_only
class TransferMessage(typing_extensions.TypedDict, total=False):
    messageText: str
    messageTime: str
    severity: typing_extensions.Literal[
        "MESSAGE_SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR"
    ]

@typing.type_check_only
class TransferResource(typing_extensions.TypedDict, total=False):
    destination: typing_extensions.Literal[
        "RESOURCE_DESTINATION_UNSPECIFIED",
        "RESOURCE_DESTINATION_BIGQUERY",
        "RESOURCE_DESTINATION_DATAPROC_METASTORE",
        "RESOURCE_DESTINATION_BIGLAKE_METASTORE",
        "RESOURCE_DESTINATION_BIGLAKE_REST_CATALOG",
        "RESOURCE_DESTINATION_BIGLAKE_HIVE_CATALOG",
    ]
    hierarchyDetail: HierarchyDetail
    lastSuccessfulRun: TransferRunBrief
    latestRun: TransferRunBrief
    latestStatusDetail: TransferResourceStatusDetail
    name: str
    type: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "RESOURCE_TYPE_TABLE", "RESOURCE_TYPE_PARTITION"
    ]
    updateTime: str

@typing.type_check_only
class TransferResourceStatusDetail(typing_extensions.TypedDict, total=False):
    completedPercentage: float
    error: Status
    state: typing_extensions.Literal[
        "RESOURCE_TRANSFER_STATE_UNSPECIFIED",
        "RESOURCE_TRANSFER_PENDING",
        "RESOURCE_TRANSFER_RUNNING",
        "RESOURCE_TRANSFER_SUCCEEDED",
        "RESOURCE_TRANSFER_FAILED",
        "RESOURCE_TRANSFER_CANCELLED",
    ]
    summary: TransferStatusSummary

@typing.type_check_only
class TransferRun(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    destinationDatasetId: str
    emailPreferences: EmailPreferences
    endTime: str
    errorStatus: Status
    name: str
    notificationPubsubTopic: str
    params: dict[str, typing.Any]
    runTime: str
    schedule: str
    scheduleTime: str
    startTime: str
    state: typing_extensions.Literal[
        "TRANSFER_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    ]
    updateTime: str
    userId: str

@typing.type_check_only
class TransferRunBrief(typing_extensions.TypedDict, total=False):
    run: str
    startTime: str

@typing.type_check_only
class TransferStatusMetric(typing_extensions.TypedDict, total=False):
    completed: str
    failed: str
    pending: str
    total: str
    unit: typing_extensions.Literal[
        "TRANSFER_STATUS_UNIT_UNSPECIFIED",
        "TRANSFER_STATUS_UNIT_BYTES",
        "TRANSFER_STATUS_UNIT_OBJECTS",
    ]

@typing.type_check_only
class TransferStatusSummary(typing_extensions.TypedDict, total=False):
    metrics: _list[TransferStatusMetric]
    progressUnit: typing_extensions.Literal[
        "TRANSFER_STATUS_UNIT_UNSPECIFIED",
        "TRANSFER_STATUS_UNIT_BYTES",
        "TRANSFER_STATUS_UNIT_OBJECTS",
    ]

@typing.type_check_only
class UnenrollDataSourcesRequest(typing_extensions.TypedDict, total=False):
    dataSourceIds: _list[str]

@typing.type_check_only
class UserInfo(typing_extensions.TypedDict, total=False):
    email: str
