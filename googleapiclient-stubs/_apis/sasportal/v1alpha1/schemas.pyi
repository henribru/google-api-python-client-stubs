import typing

_list = list

@typing.type_check_only
class SasPortalAssignment(typing.TypedDict, total=False):
    members: _list[str]
    role: str

@typing.type_check_only
class SasPortalChannelWithScore(typing.TypedDict, total=False):
    frequencyRange: SasPortalFrequencyRange
    score: float

@typing.type_check_only
class SasPortalCreateSignedDeviceRequest(typing.TypedDict, total=False):
    encodedDevice: str
    installerId: str

@typing.type_check_only
class SasPortalCustomer(typing.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalDeployment(typing.TypedDict, total=False):
    displayName: str
    frns: _list[str]
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalDeploymentAssociation(typing.TypedDict, total=False):
    gcpProjectId: str
    userId: str

@typing.type_check_only
class SasPortalDevice(typing.TypedDict, total=False):
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
    state: typing.Literal[
        "DEVICE_STATE_UNSPECIFIED", "RESERVED", "REGISTERED", "DEREGISTERED"
    ]

@typing.type_check_only
class SasPortalDeviceAirInterface(typing.TypedDict, total=False):
    radioTechnology: typing.Literal[
        "RADIO_TECHNOLOGY_UNSPECIFIED",
        "E_UTRA",
        "CAMBIUM_NETWORKS",
        "FOUR_G_BBW_SAA_1",
        "NR",
        "DOODLE_CBRS",
        "CW",
        "REDLINE",
        "TARANA_WIRELESS",
        "FAROS",
    ]
    supportedSpec: str

@typing.type_check_only
class SasPortalDeviceConfig(typing.TypedDict, total=False):
    airInterface: SasPortalDeviceAirInterface
    callSign: str
    category: typing.Literal[
        "DEVICE_CATEGORY_UNSPECIFIED", "DEVICE_CATEGORY_A", "DEVICE_CATEGORY_B"
    ]
    installationParams: SasPortalInstallationParams
    isSigned: bool
    measurementCapabilities: _list[
        typing.Literal[
            "MEASUREMENT_CAPABILITY_UNSPECIFIED",
            "MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITH_GRANT",
            "MEASUREMENT_CAPABILITY_RECEIVED_POWER_WITHOUT_GRANT",
        ]
    ]
    model: SasPortalDeviceModel
    state: typing.Literal["DEVICE_CONFIG_STATE_UNSPECIFIED", "DRAFT", "FINAL"]
    updateTime: str
    userId: str

@typing.type_check_only
class SasPortalDeviceGrant(typing.TypedDict, total=False):
    channelType: typing.Literal[
        "CHANNEL_TYPE_UNSPECIFIED", "CHANNEL_TYPE_GAA", "CHANNEL_TYPE_PAL"
    ]
    expireTime: str
    frequencyRange: SasPortalFrequencyRange
    grantId: str
    lastHeartbeatTransmitExpireTime: str
    maxEirp: float
    moveList: _list[SasPortalDpaMoveList]
    state: typing.Literal[
        "GRANT_STATE_UNSPECIFIED",
        "GRANT_STATE_GRANTED",
        "GRANT_STATE_TERMINATED",
        "GRANT_STATE_SUSPENDED",
        "GRANT_STATE_AUTHORIZED",
        "GRANT_STATE_EXPIRED",
    ]
    suspensionReason: _list[str]

@typing.type_check_only
class SasPortalDeviceMetadata(typing.TypedDict, total=False):
    antennaModel: str
    commonChannelGroup: str
    interferenceCoordinationGroup: str
    nrqzValidated: bool
    nrqzValidation: SasPortalNrqzValidation

@typing.type_check_only
class SasPortalDeviceModel(typing.TypedDict, total=False):
    firmwareVersion: str
    hardwareVersion: str
    name: str
    softwareVersion: str
    vendor: str

@typing.type_check_only
class SasPortalDpaMoveList(typing.TypedDict, total=False):
    dpaId: str
    frequencyRange: SasPortalFrequencyRange

@typing.type_check_only
class SasPortalEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalFrequencyRange(typing.TypedDict, total=False):
    highFrequencyMhz: float
    lowFrequencyMhz: float

@typing.type_check_only
class SasPortalGcpProjectDeployment(typing.TypedDict, total=False):
    deployment: SasPortalDeployment
    hasEnabledAnalytics: bool

@typing.type_check_only
class SasPortalGenerateSecretRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalGenerateSecretResponse(typing.TypedDict, total=False):
    secret: str

@typing.type_check_only
class SasPortalGetPolicyRequest(typing.TypedDict, total=False):
    resource: str

@typing.type_check_only
class SasPortalInstallationParams(typing.TypedDict, total=False):
    antennaAzimuth: int
    antennaBeamwidth: int
    antennaDowntilt: int
    antennaGain: float
    antennaModel: str
    cpeCbsdIndication: bool
    eirpCapability: int
    height: float
    heightType: typing.Literal[
        "HEIGHT_TYPE_UNSPECIFIED", "HEIGHT_TYPE_AGL", "HEIGHT_TYPE_AMSL"
    ]
    horizontalAccuracy: float
    indoorDeployment: bool
    latitude: float
    longitude: float
    verticalAccuracy: float

@typing.type_check_only
class SasPortalListCustomersResponse(typing.TypedDict, total=False):
    customers: _list[SasPortalCustomer]
    nextPageToken: str

@typing.type_check_only
class SasPortalListDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[SasPortalDeployment]
    nextPageToken: str

@typing.type_check_only
class SasPortalListDevicesResponse(typing.TypedDict, total=False):
    devices: _list[SasPortalDevice]
    nextPageToken: str

@typing.type_check_only
class SasPortalListGcpProjectDeploymentsResponse(typing.TypedDict, total=False):
    deployments: _list[SasPortalGcpProjectDeployment]

@typing.type_check_only
class SasPortalListLegacyOrganizationsResponse(typing.TypedDict, total=False):
    organizations: _list[SasPortalOrganization]

@typing.type_check_only
class SasPortalListNodesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    nodes: _list[SasPortalNode]

@typing.type_check_only
class SasPortalMigrateOrganizationMetadata(typing.TypedDict, total=False):
    operationState: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_PENDING",
        "OPERATION_STATE_RUNNING",
        "OPERATION_STATE_SUCCEEDED",
        "OPERATION_STATE_FAILED",
    ]

@typing.type_check_only
class SasPortalMigrateOrganizationRequest(typing.TypedDict, total=False):
    organizationId: str

@typing.type_check_only
class SasPortalMigrateOrganizationResponse(typing.TypedDict, total=False):
    deploymentAssociation: _list[SasPortalDeploymentAssociation]

@typing.type_check_only
class SasPortalMoveDeploymentRequest(typing.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalMoveDeviceRequest(typing.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalMoveNodeRequest(typing.TypedDict, total=False):
    destination: str

@typing.type_check_only
class SasPortalNode(typing.TypedDict, total=False):
    displayName: str
    name: str
    sasUserIds: _list[str]

@typing.type_check_only
class SasPortalNrqzValidation(typing.TypedDict, total=False):
    caseId: str
    cpiId: str
    latitude: float
    longitude: float
    state: typing.Literal["STATE_UNSPECIFIED", "DRAFT", "FINAL"]

@typing.type_check_only
class SasPortalOperation(typing.TypedDict, total=False):
    done: bool
    error: SasPortalStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class SasPortalOrganization(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class SasPortalPolicy(typing.TypedDict, total=False):
    assignments: _list[SasPortalAssignment]
    etag: str

@typing.type_check_only
class SasPortalProvisionDeploymentRequest(typing.TypedDict, total=False):
    newDeploymentDisplayName: str
    newOrganizationDisplayName: str
    organizationId: str

@typing.type_check_only
class SasPortalProvisionDeploymentResponse(typing.TypedDict, total=False):
    errorMessage: str

@typing.type_check_only
class SasPortalSetPolicyRequest(typing.TypedDict, total=False):
    disableNotification: bool
    policy: SasPortalPolicy
    resource: str

@typing.type_check_only
class SasPortalSetupSasAnalyticsMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalSetupSasAnalyticsRequest(typing.TypedDict, total=False):
    userId: str

@typing.type_check_only
class SasPortalSetupSasAnalyticsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SasPortalSignDeviceRequest(typing.TypedDict, total=False):
    device: SasPortalDevice

@typing.type_check_only
class SasPortalStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SasPortalTestPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]
    resource: str

@typing.type_check_only
class SasPortalTestPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class SasPortalUpdateSignedDeviceRequest(typing.TypedDict, total=False):
    encodedDevice: str
    installerId: str

@typing.type_check_only
class SasPortalValidateInstallerRequest(typing.TypedDict, total=False):
    encodedSecret: str
    installerId: str
    secret: str

@typing.type_check_only
class SasPortalValidateInstallerResponse(typing.TypedDict, total=False): ...
