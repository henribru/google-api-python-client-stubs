import typing

import typing_extensions

class Bin(typing_extensions.TypedDict, total=False):
    density: float
    end: typing.Any
    start: typing.Any

class UrlNormalization(typing_extensions.TypedDict, total=False):
    normalizedUrl: str
    originalUrl: str

class Percentiles(typing_extensions.TypedDict, total=False):
    p75: typing.Any

class QueryRequest(typing_extensions.TypedDict, total=False):
    url: str
    effectiveConnectionType: str
    formFactor: typing_extensions.Literal[
        "ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"
    ]
    origin: str
    metrics: typing.List[str]

class Metric(typing_extensions.TypedDict, total=False):
    percentiles: Percentiles
    histogram: typing.List[Bin]

class QueryResponse(typing_extensions.TypedDict, total=False):
    record: Record
    urlNormalizationDetails: UrlNormalization

class Key(typing_extensions.TypedDict, total=False):
    effectiveConnectionType: str
    origin: str
    url: str
    formFactor: typing_extensions.Literal[
        "ALL_FORM_FACTORS", "PHONE", "DESKTOP", "TABLET"
    ]

class Record(typing_extensions.TypedDict, total=False):
    key: Key
    metrics: typing.Dict[str, typing.Any]
