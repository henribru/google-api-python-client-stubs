import typing

import typing_extensions

class Empty(typing_extensions.TypedDict, total=False): ...

class OutputConfig(typing_extensions.TypedDict, total=False):
    destination: str

class TraceSink(typing_extensions.TypedDict, total=False):
    outputConfig: OutputConfig
    writerIdentity: str
    name: str

class ListTraceSinksResponse(typing_extensions.TypedDict, total=False):
    sinks: typing.List[TraceSink]
    nextPageToken: str
