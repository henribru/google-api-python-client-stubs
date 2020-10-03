import typing

import typing_extensions

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    error: Status
    name: str
    done: bool
