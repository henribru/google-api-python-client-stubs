import typing

_list = list

@typing.type_check_only
class ClaimDeviceRequest(typing.TypedDict, total=False):
    configurationId: str
    customerId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    googleWorkspaceCustomerId: str
    preProvisioningToken: str
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    simlockProfileId: str

@typing.type_check_only
class ClaimDeviceResponse(typing.TypedDict, total=False):
    deviceId: str
    deviceName: str

@typing.type_check_only
class ClaimDevicesRequest(typing.TypedDict, total=False):
    claims: _list[PartnerClaim]

@typing.type_check_only
class Company(typing.TypedDict, total=False):
    adminEmails: _list[str]
    companyId: str
    companyName: str
    googleWorkspaceAccount: GoogleWorkspaceAccount
    languageCode: str
    name: str
    ownerEmails: _list[str]
    skipWelcomeEmail: bool
    termsStatus: typing.Literal[
        "TERMS_STATUS_UNSPECIFIED",
        "TERMS_STATUS_NOT_ACCEPTED",
        "TERMS_STATUS_ACCEPTED",
        "TERMS_STATUS_STALE",
    ]

@typing.type_check_only
class Configuration(typing.TypedDict, total=False):
    companyName: str
    configurationId: str
    configurationName: str
    contactEmail: str
    contactPhone: str
    customMessage: str
    dpcExtras: str
    dpcResourcePath: str
    forcedResetTime: str
    isDefault: bool
    name: str

@typing.type_check_only
class CreateCustomerRequest(typing.TypedDict, total=False):
    customer: Company

@typing.type_check_only
class CustomerApplyConfigurationRequest(typing.TypedDict, total=False):
    configuration: str
    device: DeviceReference

@typing.type_check_only
class CustomerListConfigurationsResponse(typing.TypedDict, total=False):
    configurations: _list[Configuration]

@typing.type_check_only
class CustomerListCustomersResponse(typing.TypedDict, total=False):
    customers: _list[Company]
    nextPageToken: str

@typing.type_check_only
class CustomerListDevicesResponse(typing.TypedDict, total=False):
    devices: _list[Device]
    nextPageToken: str

@typing.type_check_only
class CustomerListDpcsResponse(typing.TypedDict, total=False):
    dpcs: _list[Dpc]

@typing.type_check_only
class CustomerRemoveConfigurationRequest(typing.TypedDict, total=False):
    device: DeviceReference

@typing.type_check_only
class CustomerUnclaimDeviceRequest(typing.TypedDict, total=False):
    device: DeviceReference

@typing.type_check_only
class Device(typing.TypedDict, total=False):
    claims: _list[DeviceClaim]
    configuration: str
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    name: str

@typing.type_check_only
class DeviceClaim(typing.TypedDict, total=False):
    additionalService: typing.Literal[
        "ADDITIONAL_SERVICE_UNSPECIFIED", "DEVICE_PROTECTION"
    ]
    googleWorkspaceCustomerId: str
    ownerCompanyId: str
    resellerId: str
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeExpireTime: str
    vacationModeStartTime: str

@typing.type_check_only
class DeviceIdentifier(typing.TypedDict, total=False):
    chromeOsAttestedDeviceId: str
    deviceType: typing.Literal[
        "DEVICE_TYPE_UNSPECIFIED", "DEVICE_TYPE_ANDROID", "DEVICE_TYPE_CHROME_OS"
    ]
    imei: str
    imei2: str
    manufacturer: str
    meid: str
    meid2: str
    model: str
    serialNumber: str

@typing.type_check_only
class DeviceMetadata(typing.TypedDict, total=False):
    entries: dict[str, typing.Any]

@typing.type_check_only
class DeviceReference(typing.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier

@typing.type_check_only
class DevicesLongRunningOperationMetadata(typing.TypedDict, total=False):
    devicesCount: int
    processingStatus: typing.Literal[
        "BATCH_PROCESS_STATUS_UNSPECIFIED",
        "BATCH_PROCESS_PENDING",
        "BATCH_PROCESS_IN_PROGRESS",
        "BATCH_PROCESS_PROCESSED",
    ]
    progress: int

@typing.type_check_only
class DevicesLongRunningOperationResponse(typing.TypedDict, total=False):
    perDeviceStatus: _list[OperationPerDevice]
    successCount: int

@typing.type_check_only
class Dpc(typing.TypedDict, total=False):
    dpcName: str
    name: str
    packageName: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FindDevicesByDeviceIdentifierRequest(typing.TypedDict, total=False):
    deviceIdentifier: DeviceIdentifier
    limit: str
    pageToken: str

@typing.type_check_only
class FindDevicesByDeviceIdentifierResponse(typing.TypedDict, total=False):
    devices: _list[Device]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class FindDevicesByOwnerRequest(typing.TypedDict, total=False):
    customerId: _list[str]
    googleWorkspaceCustomerId: _list[str]
    limit: str
    pageToken: str
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]

@typing.type_check_only
class FindDevicesByOwnerResponse(typing.TypedDict, total=False):
    devices: _list[Device]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class GetDeviceSimLockStateRequest(typing.TypedDict, total=False):
    deviceIdentifier: DeviceIdentifier

@typing.type_check_only
class GetDeviceSimLockStateResponse(typing.TypedDict, total=False):
    simLockState: typing.Literal[
        "SIM_LOCK_STATE_UNSPECIFIED",
        "UNLOCKED",
        "LOCKED_TO_PARTNER",
        "LOCKED_TO_OTHER_PARTNER",
    ]

@typing.type_check_only
class GoogleWorkspaceAccount(typing.TypedDict, total=False):
    customerId: str
    preProvisioningTokens: _list[str]

@typing.type_check_only
class ListCustomersResponse(typing.TypedDict, total=False):
    customers: _list[Company]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListVendorCustomersResponse(typing.TypedDict, total=False):
    customers: _list[Company]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListVendorsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    vendors: _list[Company]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationPerDevice(typing.TypedDict, total=False):
    claim: PartnerClaim
    result: PerDeviceStatusInBatch
    unclaim: PartnerUnclaim
    updateMetadata: UpdateMetadataArguments

@typing.type_check_only
class PartnerClaim(typing.TypedDict, total=False):
    configurationId: str
    customerId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
    googleWorkspaceCustomerId: str
    preProvisioningToken: str
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    simlockProfileId: str

@typing.type_check_only
class PartnerUnclaim(typing.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeDays: int
    vacationModeExpireTime: str

@typing.type_check_only
class PerDeviceStatusInBatch(typing.TypedDict, total=False):
    deviceId: str
    errorIdentifier: str
    errorMessage: str
    status: typing.Literal[
        "SINGLE_DEVICE_STATUS_UNSPECIFIED",
        "SINGLE_DEVICE_STATUS_UNKNOWN_ERROR",
        "SINGLE_DEVICE_STATUS_OTHER_ERROR",
        "SINGLE_DEVICE_STATUS_SUCCESS",
        "SINGLE_DEVICE_STATUS_PERMISSION_DENIED",
        "SINGLE_DEVICE_STATUS_INVALID_DEVICE_IDENTIFIER",
        "SINGLE_DEVICE_STATUS_INVALID_SECTION_TYPE",
        "SINGLE_DEVICE_STATUS_SECTION_NOT_YOURS",
        "SINGLE_DEVICE_STATUS_INVALID_TOKEN",
        "SINGLE_DEVICE_STATUS_REVOKED_TOKEN",
        "SINGLE_DEVICE_STATUS_DEVICE_LIMIT_EXCEEDED",
    ]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class UnclaimDeviceRequest(typing.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    sectionType: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeDays: int
    vacationModeExpireTime: str

@typing.type_check_only
class UnclaimDevicesRequest(typing.TypedDict, total=False):
    unclaims: _list[PartnerUnclaim]

@typing.type_check_only
class UpdateDeviceMetadataInBatchRequest(typing.TypedDict, total=False):
    updates: _list[UpdateMetadataArguments]

@typing.type_check_only
class UpdateDeviceMetadataRequest(typing.TypedDict, total=False):
    deviceMetadata: DeviceMetadata

@typing.type_check_only
class UpdateMetadataArguments(typing.TypedDict, total=False):
    deviceId: str
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata
