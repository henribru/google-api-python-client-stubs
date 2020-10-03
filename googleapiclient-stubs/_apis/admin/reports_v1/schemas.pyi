import typing

import typing_extensions

class Activity(typing_extensions.TypedDict, total=False):
    id: typing.Dict[str, typing.Any]
    events: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    actor: typing.Dict[str, typing.Any]
    ownerDomain: str
    etag: str
    ipAddress: str

class Activities(typing_extensions.TypedDict, total=False):
    items: typing.List[Activity]
    etag: str
    kind: str
    nextPageToken: str

class UsageReports(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    nextPageToken: str
    usageReports: typing.List[UsageReport]

class UsageReport(typing_extensions.TypedDict, total=False):
    parameters: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    date: str
    entity: typing.Dict[str, typing.Any]
    etag: str

class NestedParameter(typing_extensions.TypedDict, total=False):
    value: str
    multiIntValue: typing.List[str]
    name: str
    boolValue: bool
    multiBoolValue: typing.List[bool]
    intValue: str
    multiValue: typing.List[str]

class Channel(typing_extensions.TypedDict, total=False):
    address: str
    token: str
    kind: str
    params: typing.Dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    expiration: str
    type: str
    id: str
