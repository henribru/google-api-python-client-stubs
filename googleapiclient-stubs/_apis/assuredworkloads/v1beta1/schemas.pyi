import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationRequest(
    typing_extensions.TypedDict, total=False
):
    comment: str
    nonCompliantOrgPolicy: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponse(
    typing_extensions.TypedDict, total=False
):
    blockers: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListViolationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    violations: _list[GoogleCloudAssuredworkloadsV1beta1Violation]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: _list[GoogleCloudAssuredworkloadsV1beta1Workload]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    restrictionType: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED",
        "ALLOW_ALL_GCP_RESOURCES",
        "ALLOW_COMPLIANT_RESOURCES",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Violation(
    typing_extensions.TypedDict, total=False
):
    acknowledged: bool
    acknowledgementTime: str
    auditLogLink: str
    beginTime: str
    category: str
    description: str
    name: str
    nonCompliantOrgPolicy: str
    orgPolicyConstraint: str
    remediation: GoogleCloudAssuredworkloadsV1beta1ViolationRemediation
    resolveTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RESOLVED", "UNRESOLVED", "EXCEPTION"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediation(
    typing_extensions.TypedDict, total=False
):
    compliantValues: _list[str]
    instructions: GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructions
    remediationType: typing_extensions.Literal[
        "REMEDIATION_TYPE_UNSPECIFIED",
        "REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructions(
    typing_extensions.TypedDict, total=False
):
    consoleInstructions: GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsConsole
    gcloudInstructions: GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsGcloud

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsConsole(
    typing_extensions.TypedDict, total=False
):
    additionalLinks: _list[str]
    consoleUris: _list[str]
    steps: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsGcloud(
    typing_extensions.TypedDict, total=False
):
    additionalLinks: _list[str]
    gcloudCommands: _list[str]
    steps: _list[str]

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
        "ITAR",
        "ASSURED_WORKLOADS_FOR_PARTNERS",
    ]
    complianceStatus: GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatus
    compliantButDisallowedServices: _list[str]
    createTime: str
    displayName: str
    enableSovereignControls: bool
    etag: str
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings
    fedrampModerateSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings
    il4Settings: GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings
    kajEnrollmentState: typing_extensions.Literal[
        "KAJ_ENROLLMENT_STATE_UNSPECIFIED",
        "KAJ_ENROLLMENT_STATE_PENDING",
        "KAJ_ENROLLMENT_STATE_COMPLETE",
    ]
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings
    labels: dict[str, typing.Any]
    name: str
    partner: typing_extensions.Literal["PARTNER_UNSPECIFIED", "LOCAL_CONTROLS_BY_S3NS"]
    provisionedResourcesParent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]
    resources: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo]
    saaEnrollmentResponse: GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponse

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatus(
    typing_extensions.TypedDict, total=False
):
    acknowledgedViolationCount: int
    activeViolationCount: int

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
class GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponse(
    typing_extensions.TypedDict, total=False
):
    setupErrors: _list[str]
    setupStatus: typing_extensions.Literal[
        "SETUP_STATE_UNSPECIFIED", "STATUS_PENDING", "STATUS_COMPLETE"
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
