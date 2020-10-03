import typing

import typing_extensions

class GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings(
    typing_extensions.TypedDict, total=False
):
    nextRotationTime: str
    rotationPeriod: str

class GoogleCloudAssuredworkloadsV1beta1Workload(
    typing_extensions.TypedDict, total=False
):
    il4Settings: GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings
    name: str
    cjisSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings
    etag: str
    displayName: str
    createTime: str
    resources: typing.List[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo]
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings
    billingAccount: str
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
    ]
    fedrampModerateSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings
    labels: typing.Dict[str, typing.Any]

class GoogleCloudAssuredworkloadsV1WorkloadResourceInfo(
    typing_extensions.TypedDict, total=False
):
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "CONSUMER_PROJECT", "ENCRYPTION_KEYS_PROJECT"
    ]

class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class GoogleCloudAssuredworkloadsV1WorkloadKMSSettings(
    typing_extensions.TypedDict, total=False
):
    rotationPeriod: str
    nextRotationTime: str

class GoogleCloudAssuredworkloadsV1WorkloadCJISSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]
    name: str
    done: bool
    error: GoogleRpcStatus

class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

class GoogleCloudAssuredworkloadsV1beta1CreateWorkloadOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    displayName: str
    parent: str
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
    ]
    createTime: str

class GoogleCloudAssuredworkloadsV1CreateWorkloadOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    parent: str
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
    ]
    createTime: str
    displayName: str

class GoogleCloudAssuredworkloadsV1WorkloadFedrampModerateSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings

class GoogleCloudAssuredworkloadsV1WorkloadIL4Settings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings

class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[GoogleLongrunningOperation]

class GoogleCloudAssuredworkloadsV1WorkloadFedrampHighSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings

class GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: typing.List[GoogleCloudAssuredworkloadsV1beta1Workload]

class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo(
    typing_extensions.TypedDict, total=False
):
    resourceId: str
    resourceType: typing_extensions.Literal[
        "RESOURCE_TYPE_UNSPECIFIED", "CONSUMER_PROJECT", "ENCRYPTION_KEYS_PROJECT"
    ]

class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

class GoogleCloudAssuredworkloadsV1Workload(typing_extensions.TypedDict, total=False):
    complianceRegime: typing_extensions.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "IL4",
        "CJIS",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
    ]
    billingAccount: str
    name: str
    resources: typing.List[GoogleCloudAssuredworkloadsV1WorkloadResourceInfo]
    cjisSettings: GoogleCloudAssuredworkloadsV1WorkloadCJISSettings
    etag: str
    fedrampModerateSettings: GoogleCloudAssuredworkloadsV1WorkloadFedrampModerateSettings
    displayName: str
    il4Settings: GoogleCloudAssuredworkloadsV1WorkloadIL4Settings
    labels: typing.Dict[str, typing.Any]
    createTime: str
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1WorkloadFedrampHighSettings
