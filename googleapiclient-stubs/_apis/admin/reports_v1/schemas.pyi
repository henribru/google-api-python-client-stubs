import typing

import typing_extensions

_list = list

@typing.type_check_only
class Activities(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[Activity]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Activity(typing_extensions.TypedDict, total=False):
    actor: dict[str, typing.Any]
    etag: str
    events: _list[dict[str, typing.Any]]
    id: dict[str, typing.Any]
    ipAddress: str
    kind: str
    ownerDomain: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class NestedParameter(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    multiBoolValue: _list[bool]
    multiIntValue: _list[str]
    multiValue: _list[str]
    name: str
    value: str

@typing.type_check_only
class UsageReport(typing_extensions.TypedDict, total=False):
    date: str
    entity: dict[str, typing.Any]
    etag: str
    kind: str
    parameters: _list[dict[str, typing.Any]]

@typing.type_check_only
class UsageReports(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    usageReports: _list[UsageReport]
    warnings: _list[dict[str, typing.Any]]
