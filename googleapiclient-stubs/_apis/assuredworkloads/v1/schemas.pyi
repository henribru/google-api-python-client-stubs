import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AcknowledgeViolationRequest(
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
class GoogleCloudAssuredworkloadsV1AcknowledgeViolationResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AnalyzeWorkloadMoveResponse(
    typing_extensions.TypedDict, total=False
):
    assetMoveAnalyses: _list[GoogleCloudAssuredworkloadsV1AssetMoveAnalysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1AssetMoveAnalysis(
    typing_extensions.TypedDict, total=False
):
    analysisGroups: _list[GoogleCloudAssuredworkloadsV1MoveAnalysisGroup]
    asset: str
    assetType: str

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

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1EnableResourceMonitoringResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListViolationsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    violations: _list[GoogleCloudAssuredworkloadsV1Violation]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ListWorkloadsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    workloads: _list[GoogleCloudAssuredworkloadsV1Workload]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1MoveAnalysisGroup(
    typing_extensions.TypedDict, total=False
):
    analysisResult: GoogleCloudAssuredworkloadsV1MoveAnalysisResult
    displayName: str
    error: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1MoveAnalysisResult(
    typing_extensions.TypedDict, total=False
):
    blockers: _list[GoogleCloudAssuredworkloadsV1MoveImpact]
    warnings: _list[GoogleCloudAssuredworkloadsV1MoveImpact]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1MoveImpact(typing_extensions.TypedDict, total=False):
    detail: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1MutatePartnerPermissionsRequest(
    typing_extensions.TypedDict, total=False
):
    etag: str
    partnerPermissions: GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissions
    updateMask: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesRequest(
    typing_extensions.TypedDict, total=False
):
    restrictionType: typing_extensions.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED",
        "ALLOW_ALL_GCP_RESOURCES",
        "ALLOW_COMPLIANT_RESOURCES",
        "APPEND_COMPLIANT_RESOURCES",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1RestrictAllowedResourcesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1Violation(typing_extensions.TypedDict, total=False):
    acknowledged: bool
    acknowledgementTime: str
    associatedOrgPolicyViolationId: str
    auditLogLink: str
    beginTime: str
    category: str
    description: str
    exceptionAuditLogLink: str
    exceptionContexts: _list[GoogleCloudAssuredworkloadsV1ViolationExceptionContext]
    name: str
    nonCompliantOrgPolicy: str
    orgPolicyConstraint: str
    parentProjectNumber: str
    remediation: GoogleCloudAssuredworkloadsV1ViolationRemediation
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
class GoogleCloudAssuredworkloadsV1ViolationExceptionContext(
    typing_extensions.TypedDict, total=False
):
    acknowledgementTime: str
    comment: str
    userName: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ViolationRemediation(
    typing_extensions.TypedDict, total=False
):
    compliantValues: _list[str]
    instructions: GoogleCloudAssuredworkloadsV1ViolationRemediationInstructions
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
class GoogleCloudAssuredworkloadsV1ViolationRemediationInstructions(
    typing_extensions.TypedDict, total=False
):
    consoleInstructions: (
        GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsole
    )
    gcloudInstructions: (
        GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloud
    )

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsConsole(
    typing_extensions.TypedDict, total=False
):
    additionalLinks: _list[str]
    consoleUris: _list[str]
    steps: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1ViolationRemediationInstructionsGcloud(
    typing_extensions.TypedDict, total=False
):
    additionalLinks: _list[str]
    gcloudCommands: _list[str]
    steps: _list[str]

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
    complianceStatus: GoogleCloudAssuredworkloadsV1WorkloadComplianceStatus
    compliantButDisallowedServices: _list[str]
    createTime: str
    displayName: str
    ekmProvisioningResponse: (
        GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponse
    )
    enableSovereignControls: bool
    etag: str
    kajEnrollmentState: typing_extensions.Literal[
        "KAJ_ENROLLMENT_STATE_UNSPECIFIED",
        "KAJ_ENROLLMENT_STATE_PENDING",
        "KAJ_ENROLLMENT_STATE_COMPLETE",
    ]
    kmsSettings: GoogleCloudAssuredworkloadsV1WorkloadKMSSettings
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
    partnerPermissions: GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissions
    partnerServicesBillingAccount: str
    provisionedResourcesParent: str
    resourceMonitoringEnabled: bool
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1WorkloadResourceSettings]
    resources: _list[GoogleCloudAssuredworkloadsV1WorkloadResourceInfo]
    saaEnrollmentResponse: GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponse
    violationNotificationsEnabled: bool
    workloadOptions: GoogleCloudAssuredworkloadsV1WorkloadWorkloadOptions

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadComplianceStatus(
    typing_extensions.TypedDict, total=False
):
    acknowledgedResourceViolationCount: int
    acknowledgedViolationCount: int
    activeResourceViolationCount: int
    activeViolationCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadEkmProvisioningResponse(
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
class GoogleCloudAssuredworkloadsV1WorkloadKMSSettings(
    typing_extensions.TypedDict, total=False
):
    nextRotationTime: str
    rotationPeriod: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadPartnerPermissions(
    typing_extensions.TypedDict, total=False
):
    accessTransparencyLogsSupportCaseViewer: bool
    assuredWorkloadsMonitoring: bool
    dataLogsViewer: bool
    serviceAccessApprover: bool

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1WorkloadResourceInfo(
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
class GoogleCloudAssuredworkloadsV1WorkloadResourceSettings(
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
class GoogleCloudAssuredworkloadsV1WorkloadSaaEnrollmentResponse(
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
class GoogleCloudAssuredworkloadsV1WorkloadWorkloadOptions(
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
