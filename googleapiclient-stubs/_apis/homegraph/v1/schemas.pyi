import typing

import typing_extensions
@typing.type_check_only
class AgentDeviceId(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class AgentOtherDeviceId(typing_extensions.TypedDict, total=False):
    agentId: str
    deviceId: str

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]
    customData: typing.Dict[str, typing.Any]
    deviceInfo: DeviceInfo
    id: str
    name: DeviceNames
    nonLocalTraits: typing.List[NonLocalTrait]
    notificationSupportedByAgent: bool
    otherDeviceIds: typing.List[AgentOtherDeviceId]
    roomHint: str
    structureHint: str
    traits: typing.List[str]
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
    defaultNames: typing.List[str]
    name: str
    nicknames: typing.List[str]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class NonLocalTrait(typing_extensions.TypedDict, total=False):
    trait: str

@typing.type_check_only
class QueryRequest(typing_extensions.TypedDict, total=False):
    agentUserId: str
    inputs: typing.List[QueryRequestInput]
    requestId: str

@typing.type_check_only
class QueryRequestInput(typing_extensions.TypedDict, total=False):
    payload: QueryRequestPayload

@typing.type_check_only
class QueryRequestPayload(typing_extensions.TypedDict, total=False):
    devices: typing.List[AgentDeviceId]

@typing.type_check_only
class QueryResponse(typing_extensions.TypedDict, total=False):
    payload: QueryResponsePayload
    requestId: str

@typing.type_check_only
class QueryResponsePayload(typing_extensions.TypedDict, total=False):
    devices: typing.Dict[str, typing.Any]

@typing.type_check_only
class ReportStateAndNotificationDevice(typing_extensions.TypedDict, total=False):
    notifications: typing.Dict[str, typing.Any]
    states: typing.Dict[str, typing.Any]

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

@typing.type_check_only
class RequestLinkRequest(typing_extensions.TypedDict, total=False):
    payload: RequestLinkRequestPayload
    requestId: str

@typing.type_check_only
class RequestLinkRequestPayload(typing_extensions.TypedDict, total=False):
    detectionTime: str
    potentialCastDeviceIds: typing.List[str]

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
    devices: typing.List[Device]
