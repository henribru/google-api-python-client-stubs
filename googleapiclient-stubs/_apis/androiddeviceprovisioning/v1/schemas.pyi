import typing

import typing_extensions

class UnclaimDeviceRequest(typing_extensions.TypedDict, total=False):
    vacationModeExpireTime: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    deviceIdentifier: DeviceIdentifier
    vacationModeDays: int
    deviceId: str

class Configuration(typing_extensions.TypedDict, total=False):
    contactEmail: str
    companyName: str
    isDefault: bool
    configurationId: str
    contactPhone: str
    name: str
    dpcExtras: str
    dpcResourcePath: str
    customMessage: str
    configurationName: str

class DeviceMetadata(typing_extensions.TypedDict, total=False):
    entries: typing.Dict[str, typing.Any]

class PartnerUnclaim(typing_extensions.TypedDict, total=False):
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    deviceIdentifier: DeviceIdentifier
    vacationModeExpireTime: str
    vacationModeDays: int
    deviceId: str

class ListCustomersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    customers: typing.List[Company]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class UpdateDeviceMetadataInBatchRequest(typing_extensions.TypedDict, total=False):
    updates: typing.List[UpdateMetadataArguments]

class ListVendorCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: typing.List[Company]
    totalSize: int
    nextPageToken: str

class FindDevicesByOwnerRequest(typing_extensions.TypedDict, total=False):
    customerId: typing.List[str]
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    limit: str
    pageToken: str

class CreateCustomerRequest(typing_extensions.TypedDict, total=False):
    customer: Company

class DeviceReference(typing_extensions.TypedDict, total=False):
    deviceIdentifier: DeviceIdentifier
    deviceId: str

class DevicesLongRunningOperationMetadata(typing_extensions.TypedDict, total=False):
    devicesCount: int
    progress: int
    processingStatus: typing_extensions.Literal[
        "BATCH_PROCESS_STATUS_UNSPECIFIED",
        "BATCH_PROCESS_PENDING",
        "BATCH_PROCESS_IN_PROGRESS",
        "BATCH_PROCESS_PROCESSED",
    ]

class ClaimDeviceResponse(typing_extensions.TypedDict, total=False):
    deviceName: str
    deviceId: str

class Empty(typing_extensions.TypedDict, total=False): ...

class DeviceIdentifier(typing_extensions.TypedDict, total=False):
    meid: str
    model: str
    imei: str
    serialNumber: str
    manufacturer: str

class Company(typing_extensions.TypedDict, total=False):
    ownerEmails: typing.List[str]
    name: str
    companyId: str
    companyName: str
    termsStatus: typing_extensions.Literal[
        "TERMS_STATUS_UNSPECIFIED",
        "TERMS_STATUS_NOT_ACCEPTED",
        "TERMS_STATUS_ACCEPTED",
        "TERMS_STATUS_STALE",
    ]
    adminEmails: typing.List[str]

class PartnerClaim(typing_extensions.TypedDict, total=False):
    deviceIdentifier: DeviceIdentifier
    customerId: str
    deviceMetadata: DeviceMetadata
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]

class UpdateMetadataArguments(typing_extensions.TypedDict, total=False):
    deviceMetadata: DeviceMetadata
    deviceId: str
    deviceIdentifier: DeviceIdentifier

class FindDevicesByDeviceIdentifierResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    devices: typing.List[Device]

class ClaimDevicesRequest(typing_extensions.TypedDict, total=False):
    claims: typing.List[PartnerClaim]

class CustomerUnclaimDeviceRequest(typing_extensions.TypedDict, total=False):
    device: DeviceReference

class OperationPerDevice(typing_extensions.TypedDict, total=False):
    claim: PartnerClaim
    updateMetadata: UpdateMetadataArguments
    result: PerDeviceStatusInBatch
    unclaim: PartnerUnclaim

class DevicesLongRunningOperationResponse(typing_extensions.TypedDict, total=False):
    perDeviceStatus: typing.List[OperationPerDevice]
    successCount: int

class FindDevicesByOwnerResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    devices: typing.List[Device]

class Dpc(typing_extensions.TypedDict, total=False):
    name: str
    packageName: str
    dpcName: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str

class CustomerRemoveConfigurationRequest(typing_extensions.TypedDict, total=False):
    device: DeviceReference

class CustomerListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    configurations: typing.List[Configuration]

class CustomerListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str

class CustomerApplyConfigurationRequest(typing_extensions.TypedDict, total=False):
    configuration: str
    device: DeviceReference

class Device(typing_extensions.TypedDict, total=False):
    deviceMetadata: DeviceMetadata
    configuration: str
    deviceId: str
    name: str
    claims: typing.List[DeviceClaim]
    deviceIdentifier: DeviceIdentifier

class CustomerListCustomersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    customers: typing.List[Company]

class PerDeviceStatusInBatch(typing_extensions.TypedDict, total=False):
    deviceId: str
    status: typing_extensions.Literal[
        "SINGLE_DEVICE_STATUS_UNSPECIFIED",
        "SINGLE_DEVICE_STATUS_UNKNOWN_ERROR",
        "SINGLE_DEVICE_STATUS_OTHER_ERROR",
        "SINGLE_DEVICE_STATUS_SUCCESS",
        "SINGLE_DEVICE_STATUS_PERMISSION_DENIED",
        "SINGLE_DEVICE_STATUS_INVALID_DEVICE_IDENTIFIER",
        "SINGLE_DEVICE_STATUS_INVALID_SECTION_TYPE",
        "SINGLE_DEVICE_STATUS_SECTION_NOT_YOURS",
    ]
    errorIdentifier: str
    errorMessage: str

class ClaimDeviceRequest(typing_extensions.TypedDict, total=False):
    customerId: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    deviceIdentifier: DeviceIdentifier
    deviceMetadata: DeviceMetadata

class UpdateDeviceMetadataRequest(typing_extensions.TypedDict, total=False):
    deviceMetadata: DeviceMetadata

class FindDevicesByDeviceIdentifierRequest(typing_extensions.TypedDict, total=False):
    limit: str
    pageToken: str
    deviceIdentifier: DeviceIdentifier

class UnclaimDevicesRequest(typing_extensions.TypedDict, total=False):
    unclaims: typing.List[PartnerUnclaim]

class CustomerListDpcsResponse(typing_extensions.TypedDict, total=False):
    dpcs: typing.List[Dpc]

class ListVendorsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    vendors: typing.List[Company]
    totalSize: int

class DeviceClaim(typing_extensions.TypedDict, total=False):
    resellerId: str
    sectionType: typing_extensions.Literal[
        "SECTION_TYPE_UNSPECIFIED", "SECTION_TYPE_SIM_LOCK", "SECTION_TYPE_ZERO_TOUCH"
    ]
    vacationModeExpireTime: str
    vacationModeStartTime: str
    ownerCompanyId: str
