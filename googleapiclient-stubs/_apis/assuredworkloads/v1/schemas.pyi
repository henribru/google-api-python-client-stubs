import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "US_REGIONAL_ACCESS",
        "HIPAA",
        "HITRUST",
        "EU_REGIONS_AND_SUPPORT",
        "CA_REGIONS_AND_SUPPORT",
    ]
    createTime: str
    displayName: str
    parent: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: _list[GoogleCloudAssuredworkloadsV1Workload]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1Workload(typing_extensions.TypedDict, total=False):
    billingAccount: str
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "US_REGIONAL_ACCESS",
        "HIPAA",
        "HITRUST",
        "EU_REGIONS_AND_SUPPORT",
        "CA_REGIONS_AND_SUPPORT",
    ]
    createTime: str
    displayName: str
    etag: str
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings
    labels: dict[str, typing.Any]
    name: str
    provisionedResourcesParent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1WorkloadResourceSettings]
    resources: _list[GoogleCloudAssuredworkloadsV1WorkloadResourceInfo]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadKMSSettings(
    typing_extensions.TypedDict, total=False
):
    nextRotationTime: str
    rotationPeriod: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadResourceInfo(
    typing_extensions.TypedDict, total=False
):
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadResourceSettings(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1CreateWorkloadOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "US_REGIONAL_ACCESS",
        "HIPAA",
        "HITRUST",
        "EU_REGIONS_AND_SUPPORT",
        "CA_REGIONS_AND_SUPPORT",
    ]
    createTime: str
    displayName: str
    parent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Workload(
    typing_extensions.TypedDict, total=False
):
    billingAccount: str
    cjisSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "US_REGIONAL_ACCESS",
        "HIPAA",
        "HITRUST",
        "EU_REGIONS_AND_SUPPORT",
        "CA_REGIONS_AND_SUPPORT",
    ]
    createTime: str
    displayName: str
    etag: str
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings
    fedrampModerateSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings
    il4Settings: GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings
    labels: dict[str, typing.Any]
    name: str
    provisionedResourcesParent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]
    resources: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings(
    typing_extensions.TypedDict, total=False
):
    nextRotationTime: str
    rotationPeriod: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo(
    typing_extensions.TypedDict, total=False
):
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "CONSUMER_FOLDER",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "CONSUMER_FOLDER",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
