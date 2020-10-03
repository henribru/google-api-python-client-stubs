import typing

import typing_extensions

class ReportStateAndNotificationResponse(typing_extensions.TypedDict, total=False):
    requestId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Device(typing_extensions.TypedDict, total=False):
    traits: typing.List[str]
    customData: typing.Dict[str, typing.Any]
    notificationSupportedByAgent: bool
    id: str
    structureHint: str
    attributes: typing.Dict[str, typing.Any]
    deviceInfo: DeviceInfo
    willReportState: bool
    otherDeviceIds: typing.List[AgentOtherDeviceId]
    name: DeviceNames
    type: str
    roomHint: str

class SyncRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    requestId: str

RequestSyncDevicesRequest = typing_extensions.TypedDict(
    "RequestSyncDevicesRequest",
    {
        "async": bool,
        "agentUserId": str,
    },
    total=False,
)

class RequestSyncDevicesResponse(typing_extensions.TypedDict, total=False): ...

class DeviceInfo(typing_extensions.TypedDict, total=False):
    hwVersion: str
    swVersion: str
    manufacturer: str
    model: str

class QueryRequestInput(typing_extensions.TypedDict, total=False):
    payload: QueryRequestPayload

class QueryRequest(typing_extensions.TypedDict, total=False):
    inputs: typing.List[QueryRequestInput]
    agentUserId: str
    requestId: str

class SyncResponse(typing_extensions.TypedDict, total=False):
    requestId: str
    payload: SyncResponsePayload

class QueryResponse(typing_extensions.TypedDict, total=False):
    payload: QueryResponsePayload
    requestId: str

class AgentOtherDeviceId(typing_extensions.TypedDict, total=False):
    deviceId: str
    agentId: str

class ReportStateAndNotificationDevice(typing_extensions.TypedDict, total=False):
    states: typing.Dict[str, typing.Any]
    notifications: typing.Dict[str, typing.Any]

class QueryRequestPayload(typing_extensions.TypedDict, total=False):
    devices: typing.List[AgentDeviceId]

class QueryResponsePayload(typing_extensions.TypedDict, total=False):
    devices: typing.Dict[str, typing.Any]

class SyncResponsePayload(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    agentUserId: str

class DeviceNames(typing_extensions.TypedDict, total=False):
    defaultNames: typing.List[str]
    name: str
    nicknames: typing.List[str]

class AgentDeviceId(typing_extensions.TypedDict, total=False):
    id: str

class StateAndNotificationPayload(typing_extensions.TypedDict, total=False):
    devices: ReportStateAndNotificationDevice

class ReportStateAndNotificationRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    payload: StateAndNotificationPayload
    requestId: str
    eventId: str
    followUpToken: str
