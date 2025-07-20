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
    networkInfo: ActivityNetworkInfo
    ownerDomain: str
    resourceDetails: _list[ResourceDetails]

@typing.type_check_only
class ActivityNetworkInfo(typing_extensions.TypedDict, total=False):
    ipAsn: _list[int]
    regionCode: str
    subdivisionCode: str

@typing.type_check_only
class AppliedLabel(typing_extensions.TypedDict, total=False):
    fieldValues: _list[FieldValue]
    id: str
    reason: Reason
    title: str

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
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FieldValue(typing_extensions.TypedDict, total=False):
    dateValue: Date
    displayName: str
    id: str
    integerValue: str
    longTextValue: str
    reason: Reason
    selectionListValue: FieldValueSelectionListValue
    selectionValue: FieldValueSelectionValue
    textListValue: FieldValueTextListValue
    textValue: str
    type: str
    unsetValue: bool
    userListValue: FieldValueUserListValue
    userValue: FieldValueUserValue

@typing.type_check_only
class FieldValueSelectionListValue(typing_extensions.TypedDict, total=False):
    values: _list[FieldValueSelectionValue]

@typing.type_check_only
class FieldValueSelectionValue(typing_extensions.TypedDict, total=False):
    badged: bool
    displayName: str
    id: str

@typing.type_check_only
class FieldValueTextListValue(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class FieldValueUserListValue(typing_extensions.TypedDict, total=False):
    values: _list[FieldValueUserValue]

@typing.type_check_only
class FieldValueUserValue(typing_extensions.TypedDict, total=False):
    email: str

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
class Reason(typing_extensions.TypedDict, total=False):
    reasonType: str

@typing.type_check_only
class ResourceDetails(typing_extensions.TypedDict, total=False):
    appliedLabels: _list[AppliedLabel]
    id: str
    relation: str
    title: str
    type: str

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
