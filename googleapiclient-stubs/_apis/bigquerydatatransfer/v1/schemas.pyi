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
class DataSourceParameter(dict[str, typing.Any]): ...

@typing.type_check_only
class EmailPreferences(typing_extensions.TypedDict, total=False):
    enableFailureEmail: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnrollDataSourcesRequest(typing_extensions.TypedDict, total=False):
    dataSourceIds: _list[str]

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
    ownerInfo: UserInfo
    params: dict[str, typing.Any]
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
class UserInfo(typing_extensions.TypedDict, total=False):
    email: str
