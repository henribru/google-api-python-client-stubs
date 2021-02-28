import typing

import typing_extensions
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
    ]
    createTime: str
    displayName: str
    parent: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: typing.List[GoogleCloudAssuredworkloadsV1Workload]

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
    ]
    createTime: str
    displayName: str
    etag: str
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings
    labels: typing.Dict[str, typing.Any]
    name: str
    provisionedResourcesParent: str
    resources: typing.List[GoogleCloudAssuredworkloadsV1WorkloadResourceInfo]

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
        "RESOURCE_TYPE_UNSPECIFIED", "CONSUMER_PROJECT", "ENCRYPTION_KEYS_PROJECT"
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
    ]
    createTime: str
    displayName: str
    parent: str

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
    ]
    createTime: str
    displayName: str
    etag: str
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings
    fedrampModerateSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings
    il4Settings: GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings
    labels: typing.Dict[str, typing.Any]
    name: str
    provisionedResourcesParent: str
    resources: typing.List[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo]

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
        "RESOURCE_TYPE_UNSPECIFIED", "CONSUMER_PROJECT", "ENCRYPTION_KEYS_PROJECT"
    ]

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
