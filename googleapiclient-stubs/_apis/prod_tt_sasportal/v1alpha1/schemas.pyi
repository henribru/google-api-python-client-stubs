import typing

import typing_extensions

class SasPortalDeviceGrant(typing_extensions.TypedDict, total=False):
    grantId: str
    moveList: typing.List[SasPortalDpaMoveList]
    suspensionReason: typing.List[str]
    state: typing_extensions.Literal[
        "GRANT_STATE_UNSPECIFIED",
        "GRANT_STATE_GRANTED",
        "GRANT_STATE_TERMINATED",
        "GRANT_STATE_SUSPENDED",
        "GRANT_STATE_AUTHORIZED",
        "GRANT_STATE_EXPIRED",
    ]
    maxEirp: float
    expireTime: str
    frequencyRange: SasPortalFrequencyRange
    channelType: typing_extensions.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "CHANNEL_TYPE_GAA", "CHANNEL_TYPE_PAL"
    ]

class SasPortalDeviceConfig(typing_extensions.TypedDict, total=False):
    model: SasPortalDeviceModel
    measurementCapabilities: typing.List[str]
    airInterface: SasPortalDeviceAirInterface
    installationParams: SasPortalInstallationParams
    callSign: str
    userId: str
    isSigned: bool
    updateTime: str
    category: typing_extensions.Literal[
        "DEVICE_CATEGORY_UNSPECIFIED", "DEVICE_CATEGORY_A", "DEVICE_CATEGORY_B"
    ]
    state: typing_extensions.Literal[
        "DEVICE_CONFIG_STATE_UNSPECIFIED", "DRAFT", "FINAL"
    ]

class SasPortalBulkCreateDeviceRequest(typing_extensions.TypedDict, total=False):
    csv: str

class SasPortalBulkCreateDeviceResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[SasPortalDevice]

class SasPortalStatus(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class SasPortalGetPolicyRequest(typing_extensions.TypedDict, total=False):
    resource: str

class SasPortalValidateInstallerResponse(typing_extensions.TypedDict, total=False): ...

class SasPortalGenerateSecretResponse(typing_extensions.TypedDict, total=False):
    secret: str

class SasPortalGenerateSecretRequest(typing_extensions.TypedDict, total=False): ...

class SasPortalMoveDeviceRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalEmpty(typing_extensions.TypedDict, total=False): ...

class SasPortalDpaMoveList(typing_extensions.TypedDict, total=False):
    frequencyRange: SasPortalFrequencyRange
    dpaId: str

class SasPortalUpdateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    encodedDevice: str
    installerId: str

class SasPortalTestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SasPortalTestPermissionsRequest(typing_extensions.TypedDict, total=False):
    resource: str
    permissions: typing.List[str]

class SasPortalPolicy(typing_extensions.TypedDict, total=False):
    etag: str
    assignments: typing.List[SasPortalAssignment]

class SasPortalListCustomersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    customers: typing.List[SasPortalCustomer]

class SasPortalSignDeviceRequest(typing_extensions.TypedDict, total=False):
    device: SasPortalDevice

class SasPortalCustomer(typing_extensions.TypedDict, total=False):
    sasUserIds: typing.List[str]
    name: str
    displayName: str

class SasPortalInstallationParams(typing_extensions.TypedDict, total=False):
    antennaDowntilt: int
    height: float
    latitude: float
    indoorDeployment: bool
    cpeCbsdIndication: bool
    antennaAzimuth: int
    antennaModel: str
    heightType: typing_extensions.Literal[
        "HEIGHT_TYPE_UNSPECIFIED", "HEIGHT_TYPE_AGL", "HEIGHT_TYPE_AMSL"
    ]
    verticalAccuracy: float
    horizontalAccuracy: float
    antennaBeamwidth: int
    eirpCapability: int
    longitude: float
    antennaGain: int

class SasPortalMoveNodeRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalDeviceModel(typing_extensions.TypedDict, total=False):
    hardwareVersion: str
    vendor: str
    softwareVersion: str
    firmwareVersion: str
    name: str

class SasPortalValidateInstallerRequest(typing_extensions.TypedDict, total=False):
    secret: str
    encodedSecret: str
    installerId: str

class SasPortalListDevicesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    devices: typing.List[SasPortalDevice]

class SasPortalDevice(typing_extensions.TypedDict, total=False):
    serialNumber: str
    grants: typing.List[SasPortalDeviceGrant]
    activeConfig: SasPortalDeviceConfig
    preloadedConfig: SasPortalDeviceConfig
    name: str
    fccId: str
    state: typing_extensions.Literal[
        "DEVICE_STATE_UNSPECIFIED", "RESERVED", "REGISTERED", "DEREGISTERED"
    ]
    displayName: str
    deviceMetadata: SasPortalDeviceMetadata

class SasPortalCreateSignedDeviceRequest(typing_extensions.TypedDict, total=False):
    installerId: str
    encodedDevice: str

class SasPortalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: SasPortalPolicy
    resource: str

class SasPortalListNodesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    nodes: typing.List[SasPortalNode]

class SasPortalOperation(typing_extensions.TypedDict, total=False):
    error: SasPortalStatus
    response: typing.Dict[str, typing.Any]
    name: str
    done: bool
    metadata: typing.Dict[str, typing.Any]

class SasPortalNode(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: typing.List[str]

class SasPortalDeviceAirInterface(typing_extensions.TypedDict, total=False):
    supportedSpec: str
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

class SasPortalMoveDeploymentRequest(typing_extensions.TypedDict, total=False):
    destination: str

class SasPortalAssignment(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str

class SasPortalDeviceMetadata(typing_extensions.TypedDict, total=False): ...

class SasPortalFrequencyRange(typing_extensions.TypedDict, total=False):
    highFrequencyMhz: float
    lowFrequencyMhz: float
