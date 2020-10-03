import typing

import typing_extensions

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    name: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]

class ScheduleTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: typing.List[TransferRun]

class CheckValidCredsResponse(typing_extensions.TypedDict, total=False):
    hasValidCreds: bool

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class StartManualTransferRunsResponse(typing_extensions.TypedDict, total=False):
    runs: typing.List[TransferRun]

class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    dataSources: typing.List[DataSource]

class TimeRange(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

class TransferRun(typing_extensions.TypedDict, total=False):
    dataSourceId: str
    scheduleTime: str
    destinationDatasetId: str
    endTime: str
    notificationPubsubTopic: str
    schedule: str
    name: str
    state: typing_extensions.Literal[
        "TRANSFER_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    ]
    errorStatus: Status
    startTime: str
    emailPreferences: EmailPreferences
    updateTime: str
    runTime: str
    userId: str
    params: typing.Dict[str, typing.Any]

class ScheduleTransferRunsRequest(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class DataSourceParameter(typing.Dict[str, typing.Any]): ...

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class StartManualTransferRunsRequest(typing_extensions.TypedDict, total=False):
    requestedTimeRange: TimeRange
    requestedRunTime: str

class TransferConfig(typing_extensions.TypedDict, total=False):
    nextRunTime: str
    destinationDatasetId: str
    params: typing.Dict[str, typing.Any]
    dataRefreshWindowDays: int
    updateTime: str
    name: str
    dataSourceId: str
    disabled: bool
    state: typing_extensions.Literal[
        "TRANSFER_STATE_UNSPECIFIED",
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    ]
    notificationPubsubTopic: str
    schedule: str
    userId: str
    emailPreferences: EmailPreferences
    datasetRegion: str
    scheduleOptions: ScheduleOptions
    displayName: str

class ListTransferRunsResponse(typing_extensions.TypedDict, total=False):
    transferRuns: typing.List[TransferRun]
    nextPageToken: str

class ListTransferConfigsResponse(typing_extensions.TypedDict, total=False):
    transferConfigs: typing.List[TransferConfig]
    nextPageToken: str

class ScheduleOptions(typing_extensions.TypedDict, total=False):
    endTime: str
    disableAutoScheduling: bool
    startTime: str

class ListTransferLogsResponse(typing_extensions.TypedDict, total=False):
    transferMessages: typing.List[TransferMessage]
    nextPageToken: str

class EmailPreferences(typing_extensions.TypedDict, total=False):
    enableFailureEmail: bool

class CheckValidCredsRequest(typing_extensions.TypedDict, total=False): ...

class TransferMessage(typing_extensions.TypedDict, total=False):
    severity: typing_extensions.Literal[
        "MESSAGE_SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR"
    ]
    messageText: str
    messageTime: str

class DataSource(typing.Dict[str, typing.Any]): ...
class Empty(typing_extensions.TypedDict, total=False): ...
