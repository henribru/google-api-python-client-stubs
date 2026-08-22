import typing

_list = list

@typing.type_check_only
class AgentDeviceId(typing.TypedDict, total=False):
    id: str

@typing.type_check_only
class AgentOtherDeviceId(typing.TypedDict, total=False):
    agentId: str
    deviceId: str

@typing.type_check_only
class CameraEventStreamTrait(typing.TypedDict, total=False): ...

@typing.type_check_only
class CommonEventDataStruct(typing.TypedDict, total=False):
    mediaUrls: MediaUrlsStruct
    sessionId: str
    trackId: str

@typing.type_check_only
class Component(typing.TypedDict, total=False):
    childComponents: _list[Component]
    deviceTypes: _list[str]
    id: str
    traitData: _list[TraitData]

@typing.type_check_only
class ComponentTraitUpdates(typing.TypedDict, total=False):
    componentId: str
    traitData: _list[TraitData]

@typing.type_check_only
class Device(typing.TypedDict, total=False):
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
class DeviceBlameStruct(typing.TypedDict, total=False):
    blameType: typing.Literal[
        "DEVICE_BLAME_TYPE_ENUM_UNSPECIFIED",
        "LOCK",
        "UNLOCK",
        "MOTION_DETECTION",
        "TOUCH_INTERACTION",
        "VOICE_INTERACTION",
    ]

@typing.type_check_only
class DeviceInfo(typing.TypedDict, total=False):
    hwVersion: str
    manufacturer: str
    model: str
    swVersion: str

@typing.type_check_only
class DeviceMetadata(typing.TypedDict, total=False):
    traitCommitTimestamps: dict[str, typing.Any]

@typing.type_check_only
class DeviceNames(typing.TypedDict, total=False):
    defaultNames: _list[str]
    name: str
    nicknames: _list[str]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EveUtilityTrait(typing.TypedDict, total=False):
    acceptedCommandList: _list[typing.Literal["COMMANDS_UNSPECIFIED"]]
    accumulatedControlPoint: str
    airPressure: float
    altitude: float
    childLock: bool
    current: float
    getConfig: str
    holdPosition: bool
    lastEventTime: str
    loggingControlPoint: str
    loggingData: str
    loggingMetadata: str
    loggingTime: str
    motionSensitivity: int
    obstructionDetected: bool
    openCount: str
    rloc16: int
    setConfig: str
    statusFault: int
    voltage: float
    watt: float
    wattAccumulated: float
    weatherTrend: int

@typing.type_check_only
class EventData(typing.TypedDict, total=False):
    event: dict[str, typing.Any]
    eventId: str
    eventTime: str

@typing.type_check_only
class Events(typing.TypedDict, total=False):
    componentId: str
    events: _list[EventData]

@typing.type_check_only
class HomeEvents(typing.TypedDict, total=False):
    deviceId: str
    events: _list[Events]

@typing.type_check_only
class HomeTraitPayload(typing.TypedDict, total=False):
    rootComponent: Component

@typing.type_check_only
class HomeTraitUpdates(typing.TypedDict, total=False):
    components: _list[ComponentTraitUpdates]
    deviceId: str

@typing.type_check_only
class MediaUrlsStruct(typing.TypedDict, total=False):
    dashManifestUrl: str
    hlsMasterPlaylistUrl: str
    previewUrl: str
    thumbnailUrl: str

@typing.type_check_only
class MotionEvent(typing.TypedDict, total=False):
    commonEventData: CommonEventDataStruct
    zones: _list[ZoneStruct]
    zonesIsEmpty: bool

@typing.type_check_only
class PartnerPresenceSignalTrait(typing.TypedDict, total=False): ...

@typing.type_check_only
class PersonEvent(typing.TypedDict, total=False):
    commonEventData: CommonEventDataStruct
    zones: _list[ZoneStruct]
    zonesIsEmpty: bool

@typing.type_check_only
class QueryRequest(typing.TypedDict, total=False):
    agentUserId: str
    deviceView: typing.Literal[
        "DEVICE_VIEW_UNSPECIFIED",
        "SMART_HOME_TRAIT_ONLY",
        "HOME_TRAIT_ONLY",
        "HOME_TRAIT_AND_SMART_HOME_TRAIT",
    ]
    includeDeviceMetadata: bool
    inputs: _list[QueryRequestInput]
    requestId: str

@typing.type_check_only
class QueryRequestInput(typing.TypedDict, total=False):
    payload: QueryRequestPayload

@typing.type_check_only
class QueryRequestPayload(typing.TypedDict, total=False):
    devices: _list[AgentDeviceId]

@typing.type_check_only
class QueryResponse(typing.TypedDict, total=False):
    payload: QueryResponsePayload
    requestId: str

@typing.type_check_only
class QueryResponsePayload(typing.TypedDict, total=False):
    deviceMetadata: dict[str, typing.Any]
    devices: dict[str, typing.Any]
    homeTraitPayload: dict[str, typing.Any]

@typing.type_check_only
class ReportStateAndNotificationDevice(typing.TypedDict, total=False):
    homeEvents: _list[HomeEvents]
    homeTraits: _list[HomeTraitUpdates]
    notifications: dict[str, typing.Any]
    states: dict[str, typing.Any]

@typing.type_check_only
class ReportStateAndNotificationRequest(typing.TypedDict, total=False):
    agentUserId: str
    eventId: str
    followUpToken: str
    payload: StateAndNotificationPayload
    requestId: str

@typing.type_check_only
class ReportStateAndNotificationResponse(typing.TypedDict, total=False):
    deviceResults: dict[str, typing.Any]
    requestId: str

AlternativeRequestSyncDevicesRequest = typing.TypedDict(
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
class RequestSyncDevicesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Result(typing.TypedDict, total=False):
    homeTraitCommitTime: str

@typing.type_check_only
class StateAndNotificationPayload(typing.TypedDict, total=False):
    devices: ReportStateAndNotificationDevice

@typing.type_check_only
class StructurePresenceStateChangeEvent(typing.TypedDict, total=False):
    presenceState: typing.Literal[
        "STRUCTURE_PRESENCE_STATE_ENUM_UNSPECIFIED", "HOME", "AWAY"
    ]
    reason: StructurePresenceStateChangeReasonStruct

@typing.type_check_only
class StructurePresenceStateChangeReasonStruct(typing.TypedDict, total=False):
    deviceBlame: DeviceBlameStruct
    userBlame: UserBlameStruct

@typing.type_check_only
class SyncRequest(typing.TypedDict, total=False):
    agentUserId: str
    requestId: str

@typing.type_check_only
class SyncResponse(typing.TypedDict, total=False):
    payload: SyncResponsePayload
    requestId: str

@typing.type_check_only
class SyncResponsePayload(typing.TypedDict, total=False):
    agentUserId: str
    devices: _list[Device]

@typing.type_check_only
class ThermostatFanControlTrait(typing.TypedDict, total=False):
    timerDuration: str
    timerEnd: str
    timerSpeed: typing.Literal[
        "FAN_SPEED_SETTING_ENUM_UNSPECIFIED",
        "FAN_SPEED_SETTING_OFF",
        "FAN_SPEED_SETTING_STAGE1",
        "FAN_SPEED_SETTING_STAGE2",
        "FAN_SPEED_SETTING_STAGE3",
        "FAN_SPEED_SETTING_AUTO",
    ]

@typing.type_check_only
class TraitData(typing.TypedDict, total=False):
    commitTime: str
    providerVersionTime: str
    trait: dict[str, typing.Any]

@typing.type_check_only
class UserBlameStruct(typing.TypedDict, total=False):
    blameType: typing.Literal[
        "USER_BLAME_TYPE_ENUM_UNSPECIFIED", "PHONE_LOCATION", "MANUAL_CHANGE"
    ]
    userEmail: str

@typing.type_check_only
class ZoneStruct(typing.TypedDict, total=False):
    label: str
    zoneId: str
