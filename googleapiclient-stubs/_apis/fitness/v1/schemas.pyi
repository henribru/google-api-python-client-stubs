import typing

import typing_extensions

class Application(typing_extensions.TypedDict, total=False):
    version: str
    packageName: str
    name: str
    detailsUrl: str

class BucketBySession(typing_extensions.TypedDict, total=False):
    minDurationMillis: str

class DataSource(typing_extensions.TypedDict, total=False):
    device: Device
    dataStreamName: str
    application: Application
    dataStreamId: str
    dataType: DataType
    name: str
    dataQualityStandard: typing.List[str]
    type: typing_extensions.Literal["raw", "derived"]

class MapValue(typing_extensions.TypedDict, total=False):
    fpVal: float

class AggregateBy(typing_extensions.TypedDict, total=False):
    dataTypeName: str
    dataSourceId: str

class DataPoint(typing_extensions.TypedDict, total=False):
    rawTimestampNanos: str
    value: typing.List[Value]
    dataTypeName: str
    originDataSourceId: str
    computationTimeMillis: str
    modifiedTimeMillis: str
    startTimeNanos: str
    endTimeNanos: str

class BucketByActivity(typing_extensions.TypedDict, total=False):
    minDurationMillis: str
    activityDataSourceId: str

class ListDataPointChangesResponse(typing_extensions.TypedDict, total=False):
    deletedDataPoint: typing.List[DataPoint]
    insertedDataPoint: typing.List[DataPoint]
    nextPageToken: str
    dataSourceId: str

class Value(typing_extensions.TypedDict, total=False):
    fpVal: float
    stringVal: str
    intVal: int
    mapVal: typing.List[ValueMapValEntry]

class ValueMapValEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: MapValue

class Device(typing_extensions.TypedDict, total=False):
    uid: str
    model: str
    manufacturer: str
    type: typing_extensions.Literal[
        "unknown",
        "phone",
        "tablet",
        "watch",
        "chestStrap",
        "scale",
        "headMounted",
        "smartDisplay",
    ]
    version: str

class DataType(typing_extensions.TypedDict, total=False):
    name: str
    field: typing.List[DataTypeField]

class AggregateResponse(typing_extensions.TypedDict, total=False):
    bucket: typing.List[AggregateBucket]

class DataTypeField(typing_extensions.TypedDict, total=False):
    name: str
    optional: bool
    format: typing_extensions.Literal[
        "integer", "floatPoint", "string", "map", "integerList", "floatList", "blob"
    ]

class BucketByTimePeriod(typing_extensions.TypedDict, total=False):
    timeZoneId: str
    value: int
    type: typing_extensions.Literal["day", "week", "month"]

class BucketByTime(typing_extensions.TypedDict, total=False):
    durationMillis: str
    period: BucketByTimePeriod

class ListSessionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    session: typing.List[Session]
    hasMoreData: bool
    deletedSession: typing.List[Session]

class Dataset(typing_extensions.TypedDict, total=False):
    point: typing.List[DataPoint]
    maxEndTimeNs: str
    nextPageToken: str
    dataSourceId: str
    minStartTimeNs: str

class ListDataSourcesResponse(typing_extensions.TypedDict, total=False):
    dataSource: typing.List[DataSource]

class AggregateBucket(typing_extensions.TypedDict, total=False):
    dataset: typing.List[Dataset]
    session: Session
    endTimeMillis: str
    startTimeMillis: str
    type: typing_extensions.Literal[
        "unknown", "time", "session", "activityType", "activitySegment"
    ]
    activity: int

class Session(typing_extensions.TypedDict, total=False):
    name: str
    application: Application
    endTimeMillis: str
    startTimeMillis: str
    activeTimeMillis: str
    modifiedTimeMillis: str
    id: str
    description: str
    activityType: int

class AggregateRequest(typing_extensions.TypedDict, total=False):
    bucketByActivitySegment: BucketByActivity
    filteredDataQualityStandard: typing.List[str]
    bucketBySession: BucketBySession
    startTimeMillis: str
    endTimeMillis: str
    bucketByActivityType: BucketByActivity
    bucketByTime: BucketByTime
    aggregateBy: typing.List[AggregateBy]
