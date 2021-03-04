import typing

import typing_extensions
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
    parameters: typing.List[DataSourceParameter]
    scopes: typing.List[str]
    supportsCustomSchedule: bool
    supportsMultipleTransfers: bool
    transferType: typing_extensions.Literal[
        "TRANSFER_TYPE_UNSPECIFIED", "BATCH", "STREAMING"
    ]
    updateDeadlineSeconds: int

@typing.type_check_only
class DataSourceParameter(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class EmailPreferences(typing_extensions.TypedDict, total=False):
    enableFailureEmail: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSources: typing.List[DataSource]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListTransferConfigsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferConfigs: typing.List[TransferConfig]

@typing.type_check_only
class ListTransferLogsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferMessages: typing.List[TransferMessage]

@typing.type_check_only
class ListTransferRunsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    transferRuns: typing.List[TransferRun]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class ScheduleOptions(typing_extensions.TypedDict, total=False):
    disableAutoScheduling: bool
    endTime: str
    startTime: str

@typing.type_check_only
class ScheduleTransferRunsRequest(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ScheduleTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: typing.List[TransferRun]

@typing.type_check_only
class StartManualTransferRunsRequest(typing_extensions.TypedDict, total=False):
    requestedRunTime: str
    requestedTimeRange: TimeRange

@typing.type_check_only
class StartManualTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: typing.List[TransferRun]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

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
    name: str
    nextRunTime: str
    notificationPubsubTopic: str
    params: typing.Dict[str, typing.Any]
    schedule: str
    scheduleOptions: ScheduleOptions
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
class TransferRun(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    destinationDatasetId: str
    emailPreferences: EmailPreferences
    endTime: str
    errorStatus: Status
    name: str
    notificationPubsubTopic: str
    params: typing.Dict[str, typing.Any]
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
