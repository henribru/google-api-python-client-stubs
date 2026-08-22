import typing

_list = list

@typing.type_check_only
class AggregateBucket(typing.TypedDict, total=False):
    activity: int
    dataset: _list[Dataset]
    endTimeMillis: str
    session: Session
    startTimeMillis: str
    type: typing.Literal[
        "unknown", "time", "session", "activityType", "activitySegment"
    ]

@typing.type_check_only
class AggregateBy(typing.TypedDict, total=False):
    dataSourceId: str
    dataTypeName: str

@typing.type_check_only
class AggregateRequest(typing.TypedDict, total=False):
    aggregateBy: _list[AggregateBy]
    bucketByActivitySegment: BucketByActivity
    bucketByActivityType: BucketByActivity
    bucketBySession: BucketBySession
    bucketByTime: BucketByTime
    endTimeMillis: str
    filteredDataQualityStandard: _list[
        typing.Literal[
            "dataQualityUnknown",
            "dataQualityBloodPressureEsh2002",
            "dataQualityBloodPressureEsh2010",
            "dataQualityBloodPressureAami",
            "dataQualityBloodPressureBhsAA",
            "dataQualityBloodPressureBhsAB",
            "dataQualityBloodPressureBhsBA",
            "dataQualityBloodPressureBhsBB",
            "dataQualityBloodGlucoseIso151972003",
            "dataQualityBloodGlucoseIso151972013",
        ]
    ]
    startTimeMillis: str

@typing.type_check_only
class AggregateResponse(typing.TypedDict, total=False):
    bucket: _list[AggregateBucket]

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    detailsUrl: str
    name: str
    packageName: str
    version: str

@typing.type_check_only
class BucketByActivity(typing.TypedDict, total=False):
    activityDataSourceId: str
    minDurationMillis: str

@typing.type_check_only
class BucketBySession(typing.TypedDict, total=False):
    minDurationMillis: str

@typing.type_check_only
class BucketByTime(typing.TypedDict, total=False):
    durationMillis: str
    period: BucketByTimePeriod

@typing.type_check_only
class BucketByTimePeriod(typing.TypedDict, total=False):
    timeZoneId: str
    type: typing.Literal["day", "week", "month"]
    value: int

@typing.type_check_only
class DataPoint(typing.TypedDict, total=False):
    computationTimeMillis: str
    dataTypeName: str
    endTimeNanos: str
    modifiedTimeMillis: str
    originDataSourceId: str
    rawTimestampNanos: str
    startTimeNanos: str
    value: _list[Value]

@typing.type_check_only
class DataSource(typing.TypedDict, total=False):
    application: Application
    dataQualityStandard: _list[
        typing.Literal[
            "dataQualityUnknown",
            "dataQualityBloodPressureEsh2002",
            "dataQualityBloodPressureEsh2010",
            "dataQualityBloodPressureAami",
            "dataQualityBloodPressureBhsAA",
            "dataQualityBloodPressureBhsAB",
            "dataQualityBloodPressureBhsBA",
            "dataQualityBloodPressureBhsBB",
            "dataQualityBloodGlucoseIso151972003",
            "dataQualityBloodGlucoseIso151972013",
        ]
    ]
    dataStreamId: str
    dataStreamName: str
    dataType: DataType
    device: Device
    name: str
    type: typing.Literal["raw", "derived"]

@typing.type_check_only
class DataType(typing.TypedDict, total=False):
    field: _list[DataTypeField]
    name: str

@typing.type_check_only
class DataTypeField(typing.TypedDict, total=False):
    format: typing.Literal[
        "integer", "floatPoint", "string", "map", "integerList", "floatList", "blob"
    ]
    name: str
    optional: bool

@typing.type_check_only
class Dataset(typing.TypedDict, total=False):
    dataSourceId: str
    maxEndTimeNs: str
    minStartTimeNs: str
    nextPageToken: str
    point: _list[DataPoint]

@typing.type_check_only
class Device(typing.TypedDict, total=False):
    manufacturer: str
    model: str
    type: typing.Literal[
        "unknown",
        "phone",
        "tablet",
        "watch",
        "chestStrap",
        "scale",
        "headMounted",
        "smartDisplay",
    ]
    uid: str
    version: str

@typing.type_check_only
class ListDataPointChangesResponse(typing.TypedDict, total=False):
    dataSourceId: str
    deletedDataPoint: _list[DataPoint]
    insertedDataPoint: _list[DataPoint]
    nextPageToken: str

@typing.type_check_only
class ListDataSourcesResponse(typing.TypedDict, total=False):
    dataSource: _list[DataSource]

@typing.type_check_only
class ListSessionsResponse(typing.TypedDict, total=False):
    deletedSession: _list[Session]
    hasMoreData: bool
    nextPageToken: str
    session: _list[Session]

@typing.type_check_only
class MapValue(typing.TypedDict, total=False):
    fpVal: float

@typing.type_check_only
class Session(typing.TypedDict, total=False):
    activeTimeMillis: str
    activityType: int
    application: Application
    description: str
    endTimeMillis: str
    id: str
    modifiedTimeMillis: str
    name: str
    startTimeMillis: str

@typing.type_check_only
class Value(typing.TypedDict, total=False):
    fpVal: float
    intVal: int
    mapVal: _list[ValueMapValEntry]
    stringVal: str

@typing.type_check_only
class ValueMapValEntry(typing.TypedDict, total=False):
    key: str
    value: MapValue
