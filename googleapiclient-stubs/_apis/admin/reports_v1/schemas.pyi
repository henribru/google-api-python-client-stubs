import typing

_list = list

@typing.type_check_only
class Activities(typing.TypedDict, total=False):
    etag: str
    items: _list[Activity]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Activity(typing.TypedDict, total=False):
    actor: dict[str, typing.Any]
    etag: str
    events: _list[dict[str, typing.Any]]
    id: dict[str, typing.Any]
    ipAddress: str
    isAgenticAction: bool
    kind: str
    networkInfo: ActivityNetworkInfo
    ownerDomain: str
    resourceDetails: _list[ResourceDetails]
    userDeviceInfo: ActivityUserDeviceInfo

@typing.type_check_only
class ActivityEventsStatus(typing.TypedDict, total=False):
    errorCode: str
    errorMessage: str
    eventStatus: str
    httpStatusCode: int

@typing.type_check_only
class ActivityNetworkInfo(typing.TypedDict, total=False):
    ipAsn: _list[int]
    regionCode: str
    subdivisionCode: str

@typing.type_check_only
class ActivityUserDeviceInfo(typing.TypedDict, total=False):
    deviceId: str
    deviceOsVersion: str
    deviceType: str

@typing.type_check_only
class AgentAttributionInfo(typing.TypedDict, total=False):
    agentId: str
    agentName: str
    agentOwner: AgentAttributionInfoAgentOwner
    agentType: str

@typing.type_check_only
class AgentAttributionInfoAgentOwner(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class AppliedLabel(typing.TypedDict, total=False):
    fieldValues: _list[FieldValue]
    id: str
    reason: Reason
    title: str

@typing.type_check_only
class Channel(typing.TypedDict, total=False):
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
class CustomerIdentity(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class FieldValue(typing.TypedDict, total=False):
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
class FieldValueSelectionListValue(typing.TypedDict, total=False):
    values: _list[FieldValueSelectionValue]

@typing.type_check_only
class FieldValueSelectionValue(typing.TypedDict, total=False):
    badged: bool
    displayName: str
    id: str

@typing.type_check_only
class FieldValueTextListValue(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class FieldValueUserListValue(typing.TypedDict, total=False):
    values: _list[FieldValueUserValue]

@typing.type_check_only
class FieldValueUserValue(typing.TypedDict, total=False):
    email: str

@typing.type_check_only
class GroupIdentity(typing.TypedDict, total=False):
    groupEmail: str
    id: str

@typing.type_check_only
class NestedParameter(typing.TypedDict, total=False):
    boolValue: bool
    intValue: str
    multiBoolValue: _list[bool]
    multiIntValue: _list[str]
    multiValue: _list[str]
    name: str
    value: str

@typing.type_check_only
class OwnerDetails(typing.TypedDict, total=False):
    ownerIdentity: _list[OwnerIdentity]
    ownerType: str

@typing.type_check_only
class OwnerIdentity(typing.TypedDict, total=False):
    customerIdentity: CustomerIdentity
    groupIdentity: GroupIdentity
    sharedDriveIdentity: SharedDriveIdentity
    userIdentity: UserIdentity

@typing.type_check_only
class Reason(typing.TypedDict, total=False):
    reasonType: str

@typing.type_check_only
class ResourceDetails(typing.TypedDict, total=False):
    appliedLabels: _list[AppliedLabel]
    id: str
    ownerDetails: OwnerDetails
    relation: str
    title: str
    type: str

@typing.type_check_only
class SharedDriveIdentity(typing.TypedDict, total=False):
    id: str
    sharedDriveName: str

@typing.type_check_only
class UsageReport(typing.TypedDict, total=False):
    date: str
    entity: dict[str, typing.Any]
    etag: str
    kind: str
    parameters: _list[dict[str, typing.Any]]

@typing.type_check_only
class UsageReports(typing.TypedDict, total=False):
    etag: str
    kind: str
    nextPageToken: str
    usageReports: _list[UsageReport]
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class UserIdentity(typing.TypedDict, total=False):
    id: str
    userEmail: str
