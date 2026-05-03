import typing

import typing_extensions

_list = list

@typing.type_check_only
class AgentDeviceId(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class AgentOtherDeviceId(typing_extensions.TypedDict, total=False):
    agentId: str
    deviceId: str

@typing.type_check_only
class ComponentTraitUpdates(typing_extensions.TypedDict, total=False):
    componentId: str
    traitData: _list[TraitData]

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    customData: dict[str, typing.Any]
    deviceInfo: DeviceInfo
    id: str
    name: DeviceNames
    notificationSupportedByAgent: bool
    otherDeviceIds: _list[AgentOtherDeviceId]
    roomHint: str
    structureHint: str
    traits: _list[str]
    type: str
    willReportState: bool

@typing.type_check_only
class DeviceInfo(typing_extensions.TypedDict, total=False):
    hwVersion: str
    manufacturer: str
    model: str
    swVersion: str

@typing.type_check_only
class DeviceNames(typing_extensions.TypedDict, total=False):
    defaultNames: _list[str]
    name: str
    nicknames: _list[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EventData(typing_extensions.TypedDict, total=False):
    event: dict[str, typing.Any]
    eventId: str
    eventTime: str

@typing.type_check_only
class Events(typing_extensions.TypedDict, total=False):
    componentId: str
    events: _list[EventData]

@typing.type_check_only
class HomeEvents(typing_extensions.TypedDict, total=False):
    deviceId: str
    events: _list[Events]

@typing.type_check_only
class HomeTraitUpdates(typing_extensions.TypedDict, total=False):
    components: _list[ComponentTraitUpdates]
    deviceId: str

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    inputs: _list[QueryRequestInput]
    requestId: str

@typing.type_check_only
class QueryRequestInput(typing_extensions.TypedDict, total=False):
    payload: QueryRequestPayload

@typing.type_check_only
class QueryRequestPayload(typing_extensions.TypedDict, total=False):
    devices: _list[AgentDeviceId]

@typing.type_check_only
class QueryResponse(typing_extensions.TypedDict, total=False):
    payload: QueryResponsePayload
    requestId: str

@typing.type_check_only
class QueryResponsePayload(typing_extensions.TypedDict, total=False):
    devices: dict[str, typing.Any]

@typing.type_check_only
class ReportStateAndNotificationDevice(typing_extensions.TypedDict, total=False):
    homeEvents: _list[HomeEvents]
    homeTraits: _list[HomeTraitUpdates]
    notifications: dict[str, typing.Any]
    states: dict[str, typing.Any]

@typing.type_check_only
class ReportStateAndNotificationRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    eventId: str
    followUpToken: str
    payload: StateAndNotificationPayload
    requestId: str

@typing.type_check_only
class ReportStateAndNotificationResponse(typing_extensions.TypedDict, total=False):
    requestId: str

AlternativeRequestSyncDevicesRequest = typing_extensions.TypedDict(
    "AlternativeRequestSyncDevicesRequest",
    {
        "agentUserId": str,
        "async": bool,
    },
    total=False,
)

@typing.type_check_only
class RequestSyncDevicesRequest(AlternativeRequestSyncDevicesRequest): ...

@typing.type_check_only
class RequestSyncDevicesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class StateAndNotificationPayload(typing_extensions.TypedDict, total=False):
    devices: ReportStateAndNotificationDevice

@typing.type_check_only
class SyncRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    requestId: str

@typing.type_check_only
class SyncResponse(typing_extensions.TypedDict, total=False):
    payload: SyncResponsePayload
    requestId: str

@typing.type_check_only
class SyncResponsePayload(typing_extensions.TypedDict, total=False):
    agentUserId: str
    devices: _list[Device]

@typing.type_check_only
class TraitData(typing_extensions.TypedDict, total=False):
    trait: dict[str, typing.Any]
