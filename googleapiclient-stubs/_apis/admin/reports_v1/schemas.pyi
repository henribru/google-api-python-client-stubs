import typing

import typing_extensions
@typing.type_check_only
class Activities(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Activity]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Activity(typing_extensions.TypedDict, total=False):
    actor: typing.Dict[str, typing.Any]
    etag: str
    events: typing.List[typing.Dict[str, typing.Any]]
    id: typing.Dict[str, typing.Any]
    ipAddress: str
    kind: str
    ownerDomain: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: typing.Dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class NestedParameter(typing_extensions.TypedDict, total=False):
    boolValue: bool
    intValue: str
    multiBoolValue: typing.List[bool]
    multiIntValue: typing.List[str]
    multiValue: typing.List[str]
    name: str
    value: str

@typing.type_check_only
class UsageReport(typing_extensions.TypedDict, total=False):
    date: str
    entity: typing.Dict[str, typing.Any]
    etag: str
    kind: str
    parameters: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class UsageReports(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    usageReports: typing.List[UsageReport]
    warnings: typing.List[typing.Dict[str, typing.Any]]
