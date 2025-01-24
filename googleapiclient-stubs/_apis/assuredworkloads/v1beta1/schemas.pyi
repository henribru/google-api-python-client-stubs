import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationRequest(
    typing_extensions.TypedDict, total=False
):
    acknowledgeType: typing_extensions.Literal[
        "ACKNOWLEDGE_TYPE_UNSPECIFIED",
        "SINGLE_VIOLATION",
        "EXISTING_CHILD_RESOURCE_VIOLATIONS",
    ]
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
    assetMoveAnalyses: _list[GoogleCloudAssuredworkloadsV1beta1AssetMoveAnalysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal["WORKLOAD_UPDATE_ACTION_UNSPECIFIED", "APPLY"]
    createTime: str
    updateName: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateRequest(
    typing_extensions.TypedDict, total=False
):
    action: typing_extensions.Literal["WORKLOAD_UPDATE_ACTION_UNSPECIFIED", "APPLY"]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateResponse(
    typing_extensions.TypedDict, total=False
):
    appliedUpdate: GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AssetMoveAnalysis(
    typing_extensions.TypedDict, total=False
):
    analysisGroups: _list[GoogleCloudAssuredworkloadsV1beta1MoveAnalysisGroup]
    asset: str
    assetType: str

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
        "ITAR",
        "AU_REGIONS_AND_US_SUPPORT",
        "ASSURED_WORKLOADS_FOR_PARTNERS",
        "ISR_REGIONS",
        "ISR_REGIONS_AND_SUPPORT",
        "CA_PROTECTED_B",
        "IL5",
        "IL2",
        "JP_REGIONS_AND_SUPPORT",
        "KSA_REGIONS_AND_SUPPORT_WITH_SOVEREIGNTY_CONTROLS",
        "REGIONAL_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS_US_SUPPORT",
        "IRS_1075",
        "CANADA_CONTROLLED_GOODS",
    ]
    createTime: str
    displayName: str
    parent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableComplianceUpdatesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableResourceMonitoringResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListViolationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    violations: _list[GoogleCloudAssuredworkloadsV1beta1Violation]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloadUpdates: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: _list[GoogleCloudAssuredworkloadsV1beta1Workload]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveAnalysisGroup(
    typing_extensions.TypedDict, total=False
):
    analysisResult: GoogleCloudAssuredworkloadsV1beta1MoveAnalysisResult
    displayName: str
    error: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    blockers: _list[GoogleCloudAssuredworkloadsV1beta1MoveImpact]
    warnings: _list[GoogleCloudAssuredworkloadsV1beta1MoveImpact]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveImpact(
    typing_extensions.TypedDict, total=False
):
    detail: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicy(
    typing_extensions.TypedDict, total=False
):
    constraint: str
    inherit: bool
    reset: bool
    resource: str
    rule: GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRule

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRule(
    typing_extensions.TypedDict, total=False
):
    allowAll: bool
    denyAll: bool
    enforce: bool
    values: GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRuleStringValues(
    typing_extensions.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyUpdate(
    typing_extensions.TypedDict, total=False
):
    appliedPolicy: GoogleCloudAssuredworkloadsV1beta1OrgPolicy
    suggestedPolicy: GoogleCloudAssuredworkloadsV1beta1OrgPolicy

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    restrictionType: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED",
        "ALLOW_ALL_GCP_RESOURCES",
        "ALLOW_COMPLIANT_RESOURCES",
        "APPEND_COMPLIANT_RESOURCES",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1UpdateDetails(
    typing_extensions.TypedDict, total=False
):
    orgPolicyUpdate: GoogleCloudAssuredworkloadsV1beta1OrgPolicyUpdate

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Violation(
    typing_extensions.TypedDict, total=False
):
    acknowledged: bool
    acknowledgementTime: str
    associatedOrgPolicyViolationId: str
    auditLogLink: str
    beginTime: str
    category: str
    description: str
    exceptionAuditLogLink: str
    exceptionContexts: _list[
        GoogleCloudAssuredworkloadsV1beta1ViolationExceptionContext
    ]
    name: str
    nonCompliantOrgPolicy: str
    orgPolicyConstraint: str
    parentProjectNumber: str
    remediation: GoogleCloudAssuredworkloadsV1beta1ViolationRemediation
    resolveTime: str
    resourceName: str
    resourceType: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RESOLVED", "UNRESOLVED", "EXCEPTION"
    ]
    updateTime: str
    violationType: typing_extensions.Literal[
        "VIOLATION_TYPE_UNSPECIFIED", "ORG_POLICY", "RESOURCE"
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationExceptionContext(
    typing_extensions.TypedDict, total=False
):
    acknowledgementTime: str
    comment: str
    userName: str

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
        "REMEDIATION_RESOURCE_VIOLATION",
        "REMEDIATION_RESOURCE_VIOLATION_NON_CMEK_SERVICES",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructions(
    typing_extensions.TypedDict, total=False
):
    consoleInstructions: (
        GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsConsole
    )
    gcloudInstructions: (
        GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsGcloud
    )

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
    availableUpdates: int
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
        "AU_REGIONS_AND_US_SUPPORT",
        "ASSURED_WORKLOADS_FOR_PARTNERS",
        "ISR_REGIONS",
        "ISR_REGIONS_AND_SUPPORT",
        "CA_PROTECTED_B",
        "IL5",
        "IL2",
        "JP_REGIONS_AND_SUPPORT",
        "KSA_REGIONS_AND_SUPPORT_WITH_SOVEREIGNTY_CONTROLS",
        "REGIONAL_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS_US_SUPPORT",
        "IRS_1075",
        "CANADA_CONTROLLED_GOODS",
    ]
    complianceStatus: GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatus
    complianceUpdatesEnabled: bool
    compliantButDisallowedServices: _list[str]
    createTime: str
    displayName: str
    ekmProvisioningResponse: (
        GoogleCloudAssuredworkloadsV1beta1WorkloadEkmProvisioningResponse
    )
    enableSovereignControls: bool
    etag: str
    fedrampHighSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings
    fedrampModerateSettings: (
        GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings
    )
    il4Settings: GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings
    kajEnrollmentState: typing_extensions.Literal[
        "KAJ_ENROLLMENT_STATE_UNSPECIFIED",
        "KAJ_ENROLLMENT_STATE_PENDING",
        "KAJ_ENROLLMENT_STATE_COMPLETE",
    ]
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings
    labels: dict[str, typing.Any]
    name: str
    partner: typing_extensions.Literal[
        "PARTNER_UNSPECIFIED",
        "LOCAL_CONTROLS_BY_S3NS",
        "SOVEREIGN_CONTROLS_BY_T_SYSTEMS",
        "SOVEREIGN_CONTROLS_BY_SIA_MINSAIT",
        "SOVEREIGN_CONTROLS_BY_PSN",
        "SOVEREIGN_CONTROLS_BY_CNTXT",
        "SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM",
    ]
    partnerPermissions: GoogleCloudAssuredworkloadsV1beta1WorkloadPartnerPermissions
    partnerServicesBillingAccount: str
    provisionedResourcesParent: str
    resourceMonitoringEnabled: bool
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]
    resources: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo]
    saaEnrollmentResponse: (
        GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponse
    )
    violationNotificationsEnabled: bool
    workloadOptions: GoogleCloudAssuredworkloadsV1beta1WorkloadWorkloadOptions

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings(
    typing_extensions.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatus(
    typing_extensions.TypedDict, total=False
):
    acknowledgedResourceViolationCount: int
    acknowledgedViolationCount: int
    activeResourceViolationCount: int
    activeViolationCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadEkmProvisioningResponse(
    typing_extensions.TypedDict, total=False
):
    ekmProvisioningErrorDomain: typing_extensions.Literal[
        "EKM_PROVISIONING_ERROR_DOMAIN_UNSPECIFIED",
        "UNSPECIFIED_ERROR",
        "GOOGLE_SERVER_ERROR",
        "EXTERNAL_USER_ERROR",
        "EXTERNAL_PARTNER_ERROR",
        "TIMEOUT_ERROR",
    ]
    ekmProvisioningErrorMapping: typing_extensions.Literal[
        "EKM_PROVISIONING_ERROR_MAPPING_UNSPECIFIED",
        "INVALID_SERVICE_ACCOUNT",
        "MISSING_METRICS_SCOPE_ADMIN_PERMISSION",
        "MISSING_EKM_CONNECTION_ADMIN_PERMISSION",
    ]
    ekmProvisioningState: typing_extensions.Literal[
        "EKM_PROVISIONING_STATE_UNSPECIFIED",
        "EKM_PROVISIONING_STATE_PENDING",
        "EKM_PROVISIONING_STATE_FAILED",
        "EKM_PROVISIONING_STATE_COMPLETED",
    ]

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
class GoogleCloudAssuredworkloadsV1beta1WorkloadPartnerPermissions(
    typing_extensions.TypedDict, total=False
):
    accessTransparencyLogsSupportCaseViewer: bool
    assuredWorkloadsMonitoring: bool
    dataLogsViewer: bool
    serviceAccessApprover: bool

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
    setupErrors: _list[
        typing_extensions.Literal[
            "SETUP_ERROR_UNSPECIFIED",
            "ERROR_INVALID_BASE_SETUP",
            "ERROR_MISSING_EXTERNAL_SIGNING_KEY",
            "ERROR_NOT_ALL_SERVICES_ENROLLED",
            "ERROR_SETUP_CHECK_FAILED",
        ]
    ]
    setupStatus: typing_extensions.Literal[
        "SETUP_STATE_UNSPECIFIED", "STATUS_PENDING", "STATUS_COMPLETE"
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    details: GoogleCloudAssuredworkloadsV1beta1UpdateDetails
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "AVAILABLE", "APPLIED", "WITHDRAWN"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadWorkloadOptions(
    typing_extensions.TypedDict, total=False
):
    kajEnrollmentType: typing_extensions.Literal[
        "KAJ_ENROLLMENT_TYPE_UNSPECIFIED", "KEY_ACCESS_TRANSPARENCY_OFF"
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
