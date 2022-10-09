import typing

import typing_extensions

_list = list

@typing.type_check_only
class Bin(typing_extensions.TypedDict, total=False):
    density: float
    end: typing.Any
    start: typing.Any

@typing.type_check_only
class CollectionPeriod(typing_extensions.TypedDict, total=False):
    firstDate: Date
    lastDate: Date

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Key(typing_extensions.TypedDict, total=False):
    effectiveConnectionType: str
    formFactor: typing_extensions.Literal[
        "ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"
    ]
    origin: str
    url: str

@typing.type_check_only
class Metric(typing_extensions.TypedDict, total=False):
    histogram: _list[Bin]
    percentiles: Percentiles

@typing.type_check_only
class Percentiles(typing_extensions.TypedDict, total=False):
    p75: typing.Any

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    effectiveConnectionType: str
    formFactor: typing_extensions.Literal[
        "ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"
    ]
    metrics: _list[str]
    origin: str
    url: str

@typing.type_check_only
class QueryResponse(typing_extensions.TypedDict, total=False):
    record: Record
    urlNormalizationDetails: UrlNormalization

@typing.type_check_only
class Record(typing_extensions.TypedDict, total=False):
    collectionPeriod: CollectionPeriod
    key: Key
    metrics: dict[str, typing.Any]

@typing.type_check_only
class UrlNormalization(typing_extensions.TypedDict, total=False):
    normalizedUrl: str
    originalUrl: str
