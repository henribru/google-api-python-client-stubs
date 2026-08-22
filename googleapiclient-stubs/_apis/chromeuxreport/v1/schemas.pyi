import typing

_list = list

@typing.type_check_only
class Bin(typing.TypedDict, total=False):
    density: typing.Any
    end: typing.Any
    start: typing.Any

@typing.type_check_only
class CollectionPeriod(typing.TypedDict, total=False):
    firstDate: Date
    lastDate: Date

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FractionTimeseries(typing.TypedDict, total=False):
    fractions: _list[float]

@typing.type_check_only
class HistoryKey(typing.TypedDict, total=False):
    formFactor: typing.Literal["ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"]
    origin: str
    url: str

@typing.type_check_only
class HistoryRecord(typing.TypedDict, total=False):
    collectionPeriods: _list[CollectionPeriod]
    key: HistoryKey
    metrics: dict[str, typing.Any]

@typing.type_check_only
class Key(typing.TypedDict, total=False):
    effectiveConnectionType: str
    formFactor: typing.Literal["ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"]
    origin: str
    url: str

@typing.type_check_only
class Metric(typing.TypedDict, total=False):
    fractions: dict[str, typing.Any]
    histogram: _list[Bin]
    percentiles: Percentiles

@typing.type_check_only
class MetricTimeseries(typing.TypedDict, total=False):
    fractionTimeseries: dict[str, typing.Any]
    histogramTimeseries: _list[TimeseriesBin]
    percentilesTimeseries: TimeseriesPercentiles

@typing.type_check_only
class Percentiles(typing.TypedDict, total=False):
    p75: typing.Any

@typing.type_check_only
class QueryHistoryRequest(typing.TypedDict, total=False):
    collectionPeriodCount: int
    formFactor: typing.Literal["ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"]
    metrics: _list[str]
    origin: str
    url: str

@typing.type_check_only
class QueryHistoryResponse(typing.TypedDict, total=False):
    record: HistoryRecord
    urlNormalizationDetails: UrlNormalization

@typing.type_check_only
class QueryRequest(typing.TypedDict, total=False):
    effectiveConnectionType: str
    formFactor: typing.Literal["ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"]
    metrics: _list[str]
    origin: str
    url: str

@typing.type_check_only
class QueryResponse(typing.TypedDict, total=False):
    record: Record
    urlNormalizationDetails: UrlNormalization

@typing.type_check_only
class Record(typing.TypedDict, total=False):
    collectionPeriod: CollectionPeriod
    key: Key
    metrics: dict[str, typing.Any]

@typing.type_check_only
class TimeseriesBin(typing.TypedDict, total=False):
    densities: _list[float]
    end: typing.Any
    start: typing.Any

@typing.type_check_only
class TimeseriesPercentiles(typing.TypedDict, total=False):
    p75s: _list[typing.Any]

@typing.type_check_only
class UrlNormalization(typing.TypedDict, total=False):
    normalizedUrl: str
    originalUrl: str
