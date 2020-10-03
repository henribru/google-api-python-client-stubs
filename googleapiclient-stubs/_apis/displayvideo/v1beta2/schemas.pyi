import typing

import typing_extensions

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    response: typing.Dict[str, typing.Any]
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]

class GoogleBytestreamMedia(typing_extensions.TypedDict, total=False):
    resourceName: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
