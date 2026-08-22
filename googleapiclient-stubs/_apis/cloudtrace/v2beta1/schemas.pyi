import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListTraceSinksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sinks: _list[TraceSink]

@typing.type_check_only
class OutputConfig(typing.TypedDict, total=False):
    destination: str

@typing.type_check_only
class TraceSink(typing.TypedDict, total=False):
    name: str
    outputConfig: OutputConfig
    writerIdentity: str
