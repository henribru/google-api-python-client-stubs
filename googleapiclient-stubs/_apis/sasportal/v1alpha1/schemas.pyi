import typing

import typing_extensions

class SasPortalValidateInstallerResponse(typing_extensions.TypedDict, total=False): ...

class SasPortalStatus(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class SasPortalDeviceModel(typing_extensions.TypedDict, total=False):
    softwareVersion: str
    hardwareVersion: str
    vendor: str
    name: str
    firmwareVersion: str

class SasPortalPolicy(typing_extensions.TypedDict, total=False):
    etag: str
    assignments: typing.List[SasPortalAssignment]

class SasPortalDeviceMetadata(typing_extensions.TypedDict, total=False): ...

class SasPortalDevice(typing_extensions.TypedDict, total=False):
    preloadedConfig: SasPortalDeviceConfig
    serialNumber: str
    deviceMetadata: SasPortalDeviceMetadata
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "RESERVED", "REGISTERED", "DEREGISTERED"
    ]
    name: str
    activeConfig: SasPortalDeviceConfig
    fccId: str
    grants: typing.List[SasPortalDeviceGrant]
    displayName: str

class SasPortalDpaMoveList(typing_extensions.TypedDict, total=False):
    frequencyRange: SasPortalFrequencyRange
    dpaId: str

class SasPortalAssignment(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str

class SasPortalBulkCreateDeviceRequest(typing_extensions.TypedDict, total=False):
    csv: str

class SasPortalNode(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    sasUserIds: typing.List[str]

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

class SasPortalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: SasPortalPolicy
    resource: str

class SasPortalGetPolicyRequest(typing_extensions.TypedDict, total=False):
    resource: str

class SasPortalCustomer(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: typing.List[str]

class SasPortalInstallationParams(typing_extensions.TypedDict, total=False):
    antennaAzimuth: int
    antennaModel: str
    horizontalAccuracy: float
    cpeCbsdIndication: bool
    antennaGain: int
    heightType: typing_extensions.Literal[
        "HEIGHT_TYPE_UNSPECIFIED", "HEIGHT_TYPE_AGL", "HEIGHT_TYPE_AMSL"
    ]
    antennaDowntilt: int
    latitude: float
    longitude: float
    antennaBeamwidth: int
    height: float
    verticalAccuracy: float
    eirpCapability: int
    indoorDeployment: bool

class SasPortalDeviceConfig(typing_extensions.TypedDict, total=False):
    isSigned: bool
    airInterface: SasPortalDeviceAirInterface
    state: typing_extensions.Literal[
        "DEVICE_CONFIG_STATE_UNSPECIFIED", "DRAFT", "FINAL"
    ]
    category: typing_extensions.Literal[
        "DEVICE_CATEGORY_UNSPECIFIED", "DEVICE_CATEGORY_A", "DEVICE_CATEGORY_B"
    ]
    updateTime: str
    installationParams: SasPortalInstallationParams
    measurementCapabilities: typing.List[str]
    userId: str
    callSign: str
    model: SasPortalDeviceModel

class SasPortalListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: typing.List[SasPortalNode]

class SasPortalMoveNodeRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalDeviceGrant(typing_extensions.TypedDict, total=False):
    frequencyRange: SasPortalFrequencyRange
    suspensionReason: typing.List[str]
    grantId: str
    channelType: typing_extensions.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "CHANNEL_TYPE_GAA", "CHANNEL_TYPE_PAL"
    ]
    maxEirp: float
    expireTime: str
    state: typing_extensions.Literal[
        "GRANT_STATE_UNSPECIFIED",
        "GRANT_STATE_GRANTED",
        "GRANT_STATE_TERMINATED",
        "GRANT_STATE_SUSPENDED",
        "GRANT_STATE_AUTHORIZED",
        "GRANT_STATE_EXPIRED",
    ]
    moveList: typing.List[SasPortalDpaMoveList]

class SasPortalGenerateSecretRequest(typing_extensions.TypedDict, total=False): ...

class SasPortalFrequencyRange(typing_extensions.TypedDict, total=False):
    lowFrequencyMhz: float
    highFrequencyMhz: float

class SasPortalMoveDeviceRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalCreateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    installerId: str
    encodedDevice: str

class SasPortalUpdateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    encodedDevice: str
    installerId: str

class SasPortalListCustomersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    customers: typing.List[SasPortalCustomer]

class SasPortalBulkCreateDeviceResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[SasPortalDevice]

class SasPortalEmpty(typing_extensions.TypedDict, total=False): ...

class SasPortalValidateInstallerRequest(typing_extensions.TypedDict, total=False):
    installerId: str
    secret: str
    encodedSecret: str

class SasPortalSignDeviceRequest(typing_extensions.TypedDict, total=False):
    device: SasPortalDevice

class SasPortalListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[SasPortalDevice]
    nextPageToken: str

class SasPortalMoveDeploymentRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalOperation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    error: SasPortalStatus
    name: str
    metadata: typing.Dict[str, typing.Any]

class SasPortalGenerateSecretResponse(typing_extensions.TypedDict, total=False):
    secret: str

class SasPortalTestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SasPortalTestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
    resource: str
