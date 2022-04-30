import typing

import typing_extensions

_list = list

@typing.type_check_only
class SasPortalAssignment(typing_extensions.TypedDict, total=False):
    members: _list[str]
    role: str

@typing.type_check_only
class SasPortalChannelWithScore(typing_extensions.TypedDict, total=False):
    frequencyRange: SasPortalFrequencyRange
    score: float

@typing.type_check_only
class SasPortalCreateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    encodedDevice: str
    installerId: str

@typing.type_check_only
class SasPortalCustomer(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalDeployment(typing_extensions.TypedDict, total=False):
    displayName: str
    frns: _list[str]
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalDevice(typing_extensions.TypedDict, total=False):
    activeConfig: SasPortalDeviceConfig
    currentChannels: _list[SasPortalChannelWithScore]
    deviceMetadata: SasPortalDeviceMetadata
    displayName: str
    fccId: str
    grantRangeAllowlists: _list[SasPortalFrequencyRange]
    grants: _list[SasPortalDeviceGrant]
    name: str
    preloadedConfig: SasPortalDeviceConfig
    serialNumber: str
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "RESERVED", "REGISTERED", "DEREGISTERED"
    ]

@typing.type_check_only
class SasPortalDeviceAirInterface(typing_extensions.TypedDict, total=False):
    radioTechnology: typing_extensions.Literal[
        "RADIO_TECHNOLOGY_UNSPECIFIED",
        "E_UTRA",
        "CAMBIUM_NETWORKS",
        "FOUR_G_BBW_SAA_1",
        "NR",
        "DOODLE_CBRS",
        "CW",
        "REDLINE",
        "TARANA_WIRELESS",
    ]
    supportedSpec: str

@typing.type_check_only
class SasPortalDeviceConfig(typing_extensions.TypedDict, total=False):
    airInterface: SasPortalDeviceAirInterface
    callSign: str
    category: typing_extensions.Literal[
        "DEVICE_CATEGORY_UNSPECIFIED", "DEVICE_CATEGORY_A", "DEVICE_CATEGORY_B"
    ]
    installationParams: SasPortalInstallationParams
    isSigned: bool
    measurementCapabilities: _list[str]
    model: SasPortalDeviceModel
    state: typing_extensions.Literal[
        "DEVICE_CONFIG_STATE_UNSPECIFIED", "DRAFT", "FINAL"
    ]
    updateTime: str
    userId: str

@typing.type_check_only
class SasPortalDeviceGrant(typing_extensions.TypedDict, total=False):
    channelType: typing_extensions.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "CHANNEL_TYPE_GAA", "CHANNEL_TYPE_PAL"
    ]
    expireTime: str
    frequencyRange: SasPortalFrequencyRange
    grantId: str
    lastHeartbeatTransmitExpireTime: str
    maxEirp: float
    moveList: _list[SasPortalDpaMoveList]
    state: typing_extensions.Literal[
        "GRANT_STATE_UNSPECIFIED",
        "GRANT_STATE_GRANTED",
        "GRANT_STATE_TERMINATED",
        "GRANT_STATE_SUSPENDED",
        "GRANT_STATE_AUTHORIZED",
        "GRANT_STATE_EXPIRED",
    ]
    suspensionReason: _list[str]

@typing.type_check_only
class SasPortalDeviceMetadata(typing_extensions.TypedDict, total=False):
    antennaModel: str
    commonChannelGroup: str
    interferenceCoordinationGroup: str
    nrqzValidated: bool
    nrqzValidation: SasPortalNrqzValidation

@typing.type_check_only
class SasPortalDeviceModel(typing_extensions.TypedDict, total=False):
    firmwareVersion: str
    hardwareVersion: str
    name: str
    softwareVersion: str
    vendor: str

@typing.type_check_only
class SasPortalDpaMoveList(typing_extensions.TypedDict, total=False):
    dpaId: str
    frequencyRange: SasPortalFrequencyRange

@typing.type_check_only
class SasPortalEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalFrequencyRange(typing_extensions.TypedDict, total=False):
    highFrequencyMhz: float
    lowFrequencyMhz: float

@typing.type_check_only
class SasPortalGenerateSecretRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalGenerateSecretResponse(typing_extensions.TypedDict, total=False):
    secret: str

@typing.type_check_only
class SasPortalGetPolicyRequest(typing_extensions.TypedDict, total=False):
    resource: str

@typing.type_check_only
class SasPortalInstallationParams(typing_extensions.TypedDict, total=False):
    antennaAzimuth: int
    antennaBeamwidth: int
    antennaDowntilt: int
    antennaGain: int
    antennaModel: str
    cpeCbsdIndication: bool
    eirpCapability: int
    height: float
    heightType: typing_extensions.Literal[
        "HEIGHT_TYPE_UNSPECIFIED", "HEIGHT_TYPE_AGL", "HEIGHT_TYPE_AMSL"
    ]
    horizontalAccuracy: float
    indoorDeployment: bool
    latitude: float
    longitude: float
    verticalAccuracy: float

@typing.type_check_only
class SasPortalListCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: _list[SasPortalCustomer]
    nextPageToken: str

@typing.type_check_only
class SasPortalListDeploymentsResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[SasPortalDeployment]
    nextPageToken: str

@typing.type_check_only
class SasPortalListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: _list[SasPortalDevice]
    nextPageToken: str

@typing.type_check_only
class SasPortalListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: _list[SasPortalNode]

@typing.type_check_only
class SasPortalMoveDeploymentRequest(typing_extensions.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalMoveDeviceRequest(typing_extensions.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalMoveNodeRequest(typing_extensions.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalNode(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalNrqzValidation(typing_extensions.TypedDict, total=False):
    caseId: str
    cpiId: str
    latitude: float
    longitude: float
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "DRAFT", "FINAL"]

@typing.type_check_only
class SasPortalOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: SasPortalStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class SasPortalPolicy(typing_extensions.TypedDict, total=False):
    assignments: _list[SasPortalAssignment]
    etag: str

@typing.type_check_only
class SasPortalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    disableNotification: bool
    policy: SasPortalPolicy
    resource: str

@typing.type_check_only
class SasPortalSignDeviceRequest(typing_extensions.TypedDict, total=False):
    device: SasPortalDevice

@typing.type_check_only
class SasPortalStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SasPortalTestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
    resource: str

@typing.type_check_only
class SasPortalTestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class SasPortalUpdateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    encodedDevice: str
    installerId: str

@typing.type_check_only
class SasPortalValidateInstallerRequest(typing_extensions.TypedDict, total=False):
    encodedSecret: str
    installerId: str
    secret: str

@typing.type_check_only
class SasPortalValidateInstallerResponse(typing_extensions.TypedDict, total=False): ...
