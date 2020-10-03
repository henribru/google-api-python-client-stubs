import typing

import typing_extensions

class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
