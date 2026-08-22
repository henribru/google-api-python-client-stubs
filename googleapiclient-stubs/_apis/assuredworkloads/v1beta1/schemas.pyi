import typing

_list = list

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationRequest(
    typing.TypedDict, total=False
):
    acknowledgeType: typing.Literal[
        "ACKNOWLEDGE_TYPE_UNSPECIFIED",
        "SINGLE_VIOLATION",
        "EXISTING_CHILD_RESOURCE_VIOLATIONS",
    ]
    comment: str
    nonCompliantOrgPolicy: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AcknowledgeViolationResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AggregateDbFrameworkComplianceReportResponse(
    typing.TypedDict, total=False
):
    aggregatedComplianceReports: _list[
        GoogleCloudAssuredworkloadsV1beta1AggregatedComplianceReport
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AggregatedComplianceReport(
    typing.TypedDict, total=False
):
    controlAssessmentDetails: GoogleCloudAssuredworkloadsV1beta1ControlAssessmentDetails
    reportTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AnalyzeWorkloadMoveResponse(
    typing.TypedDict, total=False
):
    assetMoveAnalyses: _list[GoogleCloudAssuredworkloadsV1beta1AssetMoveAnalysis]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateOperationMetadata(
    typing.TypedDict, total=False
):
    action: typing.Literal["WORKLOAD_UPDATE_ACTION_UNSPECIFIED", "APPLY"]
    createTime: str
    updateName: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateRequest(
    typing.TypedDict, total=False
):
    action: typing.Literal["WORKLOAD_UPDATE_ACTION_UNSPECIFIED", "APPLY"]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ApplyWorkloadUpdateResponse(
    typing.TypedDict, total=False
):
    appliedUpdate: GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ArchiveResourceEventsRequest(
    typing.TypedDict, total=False
):
    archiveTime: str
    batchSize: int
    eventCutoffTime: str
    maxEventsMove: int
    organizationId: str
    region: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ArchiveResourceEventsResponse(
    typing.TypedDict, total=False
):
    movedEventsCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1AssetMoveAnalysis(
    typing.TypedDict, total=False
):
    analysisGroups: _list[GoogleCloudAssuredworkloadsV1beta1MoveAnalysisGroup]
    asset: str
    assetType: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1CELExpression(typing.TypedDict, total=False):
    expression: str
    resourceTypesValues: GoogleCloudAssuredworkloadsV1beta1StringList

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1CloudControlAssessmentDetails(
    typing.TypedDict, total=False
):
    evaluationState: typing.Literal[
        "EVALUATION_STATE_UNSPECIFIED",
        "EVALUATION_STATE_PASSED",
        "EVALUATION_STATE_FAILED",
        "EVALUATION_STATE_NOT_ASSESSED",
    ]
    findingsCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1CloudControlReport(
    typing.TypedDict, total=False
):
    categories: _list[str]
    cloudControl: str
    cloudControlAssessmentDetails: (
        GoogleCloudAssuredworkloadsV1beta1CloudControlAssessmentDetails
    )
    cloudControlDeployment: str
    cloudControlType: typing.Literal["TYPE_UNSPECIFIED", "CUSTOM", "BUILT_IN"]
    description: str
    displayName: str
    enforcementMode: typing.Literal[
        "ENFORCEMENT_MODE_UNSPECIFIED", "PREVENTIVE", "DETECTIVE", "AUDIT"
    ]
    findingCategory: str
    findingSeverity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    frameworkMajorRevisionIds: _list[str]
    majorRevisionId: str
    manualCloudControlAssessmentDetails: (
        GoogleCloudAssuredworkloadsV1beta1ManualCloudControlAssessmentDetails
    )
    minorRevisionId: str
    rules: _list[GoogleCloudAssuredworkloadsV1beta1Rule]
    similarControls: _list[GoogleCloudAssuredworkloadsV1beta1SimilarControls]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ControlAssessmentDetails(
    typing.TypedDict, total=False
):
    assessedPassingControlIds: _list[str]
    assessedPassingControls: int
    failingControlIds: _list[str]
    failingControls: int
    notAssessedControlIds: _list[str]
    notAssessedControls: int
    passingControlIds: _list[str]
    passingControls: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1CreateWorkloadOperationMetadata(
    typing.TypedDict, total=False
):
    complianceRegime: typing.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "ASSURED_WORKLOADS_FOR_PARTNERS",
        "AUSTRALIA_DATA_BOUNDARY_AND_SUPPORT",
        "CANADA_DATA_BOUNDARY_AND_SUPPORT",
        "DATA_BOUNDARY_FOR_CANADA_CONTROLLED_GOODS",
        "DATA_BOUNDARY_FOR_CANADA_PROTECTED_B",
        "DATA_BOUNDARY_FOR_CJIS",
        "DATA_BOUNDARY_FOR_FEDRAMP_HIGH",
        "DATA_BOUNDARY_FOR_FEDRAMP_MODERATE",
        "DATA_BOUNDARY_FOR_IL2",
        "DATA_BOUNDARY_FOR_IL4",
        "DATA_BOUNDARY_FOR_IL5",
        "DATA_BOUNDARY_FOR_IRS_PUBLICATION_1075",
        "DATA_BOUNDARY_FOR_ITAR",
        "EU_DATA_BOUNDARY_AND_SUPPORT",
        "ISRAEL_DATA_BOUNDARY_AND_SUPPORT",
        "JAPAN_DATA_BOUNDARY",
        "SWITZERLAND_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS",
        "KSA_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS",
        "REGIONAL_DATA_BOUNDARY",
        "US_DATA_BOUNDARY_AND_SUPPORT",
        "US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES",
        "US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES_WITH_SUPPORT",
        "AU_REGIONS_AND_US_SUPPORT",
        "CA_PROTECTED_B",
        "CA_REGIONS_AND_SUPPORT",
        "CANADA_CONTROLLED_GOODS",
        "CJIS",
        "EU_REGIONS_AND_SUPPORT",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS_US_SUPPORT",
        "HIPAA",
        "HITRUST",
        "IL2",
        "IL4",
        "IL5",
        "IRS_1075",
        "ISR_REGIONS",
        "ISR_REGIONS_AND_SUPPORT",
        "ITAR",
        "JP_REGIONS_AND_SUPPORT",
        "KSA_REGIONS_AND_SUPPORT_WITH_SOVEREIGNTY_CONTROLS",
        "REGIONAL_CONTROLS",
        "US_REGIONAL_ACCESS",
    ]
    createTime: str
    displayName: str
    parent: str
    resourceSettings: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1DbControlComplianceSummary(
    typing.TypedDict, total=False
):
    cloudControlReports: _list[GoogleCloudAssuredworkloadsV1beta1CloudControlReport]
    complianceFrameworks: _list[str]
    control: str
    controlResponsibilityType: typing.Literal[
        "REGULATORY_CONTROL_RESPONSIBILITY_TYPE_UNSPECIFIED",
        "GOOGLE",
        "CUSTOMER",
        "SHARED",
    ]
    description: str
    displayName: str
    isFakeControl: bool
    name: str
    overallEvaluationState: typing.Literal[
        "EVALUATION_STATE_UNSPECIFIED",
        "EVALUATION_STATE_PASSED",
        "EVALUATION_STATE_FAILED",
        "EVALUATION_STATE_NOT_ASSESSED",
    ]
    similarControls: _list[GoogleCloudAssuredworkloadsV1beta1SimilarControls]
    totalFindingsCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1DbFindingSummary(typing.TypedDict, total=False):
    findingCategory: str
    findingClass: typing.Literal[
        "FINDING_CLASS_UNSPECIFIED",
        "THREAT",
        "VULNERABILITY",
        "MISCONFIGURATION",
        "OBSERVATION",
        "SCC_ERROR",
        "POSTURE_VIOLATION",
        "TOXIC_COMBINATION",
        "SENSITIVE_DATA_RISK",
        "CHOKEPOINT",
    ]
    findingCount: str
    name: str
    organizationPolicyFindingCount: str
    relatedFrameworks: _list[str]
    resourceFindingCount: str
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1DbFrameworkComplianceSummary(
    typing.TypedDict, total=False
):
    controlAssessmentDetails: GoogleCloudAssuredworkloadsV1beta1ControlAssessmentDetails
    controlsPassingTrend: GoogleCloudAssuredworkloadsV1beta1Trend
    findingCount: str
    framework: str
    frameworkCategories: _list[
        typing.Literal[
            "FRAMEWORK_CATEGORY_UNSPECIFIED",
            "INDUSTRY_DEFINED_STANDARD",
            "ASSURED_WORKLOADS",
            "DATA_SECURITY",
            "GOOGLE_BEST_PRACTICES",
            "CUSTOM_FRAMEWORK",
        ]
    ]
    frameworkDisplayName: str
    frameworkType: typing.Literal["FRAMEWORK_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"]
    majorRevisionId: str
    minorRevisionId: str
    name: str
    supportedCloudProviders: _list[
        typing.Literal["CLOUD_PROVIDER_UNSPECIFIED", "AWS", "AZURE", "GCP"]
    ]
    targetResourceDetails: _list[
        GoogleCloudAssuredworkloadsV1beta1TargetResourceDetails
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableComplianceUpdatesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1EnableResourceMonitoringResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1FetchDbFrameworkComplianceReportResponse(
    typing.TypedDict, total=False
):
    controlAssessmentDetails: GoogleCloudAssuredworkloadsV1beta1ControlAssessmentDetails
    framework: str
    frameworkCategories: _list[
        typing.Literal[
            "FRAMEWORK_CATEGORY_UNSPECIFIED",
            "INDUSTRY_DEFINED_STANDARD",
            "ASSURED_WORKLOADS",
            "DATA_SECURITY",
            "GOOGLE_BEST_PRACTICES",
            "CUSTOM_FRAMEWORK",
        ]
    ]
    frameworkDescription: str
    frameworkDisplayName: str
    frameworkType: typing.Literal["FRAMEWORK_TYPE_UNSPECIFIED", "BUILT_IN", "CUSTOM"]
    majorRevisionId: str
    minorRevisionId: str
    name: str
    supportedCloudProviders: _list[
        typing.Literal["CLOUD_PROVIDER_UNSPECIFIED", "AWS", "AZURE", "GCP"]
    ]
    targetResourceDetails: _list[
        GoogleCloudAssuredworkloadsV1beta1TargetResourceDetails
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListDbControlComplianceSummariesResponse(
    typing.TypedDict, total=False
):
    dbControlComplianceSummaries: _list[
        GoogleCloudAssuredworkloadsV1beta1DbControlComplianceSummary
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListDbFindingSummariesResponse(
    typing.TypedDict, total=False
):
    dbFindingSummaries: _list[GoogleCloudAssuredworkloadsV1beta1DbFindingSummary]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListDbFrameworkComplianceSummariesResponse(
    typing.TypedDict, total=False
):
    dbFrameworkComplianceSummaries: _list[
        GoogleCloudAssuredworkloadsV1beta1DbFrameworkComplianceSummary
    ]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListViolationsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    totalSize: int
    violations: _list[GoogleCloudAssuredworkloadsV1beta1Violation]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadUpdatesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    workloadUpdates: _list[GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ListWorkloadsResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    workloads: _list[GoogleCloudAssuredworkloadsV1beta1Workload]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ManualCloudControlAssessmentDetails(
    typing.TypedDict, total=False
):
    manualCloudControlGuide: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveAnalysisGroup(
    typing.TypedDict, total=False
):
    analysisResult: GoogleCloudAssuredworkloadsV1beta1MoveAnalysisResult
    displayName: str
    error: GoogleRpcStatus

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveAnalysisResult(
    typing.TypedDict, total=False
):
    blockers: _list[GoogleCloudAssuredworkloadsV1beta1MoveImpact]
    warnings: _list[GoogleCloudAssuredworkloadsV1beta1MoveImpact]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1MoveImpact(typing.TypedDict, total=False):
    detail: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicy(typing.TypedDict, total=False):
    constraint: str
    inherit: bool
    reset: bool
    resource: str
    rule: GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRule

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRule(
    typing.TypedDict, total=False
):
    allowAll: bool
    denyAll: bool
    enforce: bool
    values: GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyPolicyRuleStringValues(
    typing.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1OrgPolicyUpdate(typing.TypedDict, total=False):
    appliedPolicy: GoogleCloudAssuredworkloadsV1beta1OrgPolicy
    suggestedPolicy: GoogleCloudAssuredworkloadsV1beta1OrgPolicy

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesRequest(
    typing.TypedDict, total=False
):
    restrictionType: typing.Literal[
        "RESTRICTION_TYPE_UNSPECIFIED",
        "ALLOW_ALL_GCP_RESOURCES",
        "ALLOW_COMPLIANT_RESOURCES",
        "APPEND_COMPLIANT_RESOURCES",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RestrictAllowedResourcesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RevertArchivedResourceEventsRequest(
    typing.TypedDict, total=False
):
    archiveEndTime: str
    archiveStartTime: str
    batchSize: int
    maxEventsMove: int
    organizationId: str
    region: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1RevertArchivedResourceEventsResponse(
    typing.TypedDict, total=False
):
    movedEventsCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Rule(typing.TypedDict, total=False):
    celExpression: GoogleCloudAssuredworkloadsV1beta1CELExpression
    description: str
    ruleActionTypes: _list[
        typing.Literal[
            "RULE_ACTION_TYPE_UNSPECIFIED",
            "RULE_ACTION_TYPE_PREVENTIVE",
            "RULE_ACTION_TYPE_DETECTIVE",
            "RULE_ACTION_TYPE_AUDIT",
        ]
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1SimilarControls(typing.TypedDict, total=False):
    controlId: str
    framework: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1StringList(typing.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1TargetResourceDetails(
    typing.TypedDict, total=False
):
    createTime: str
    frameworkDeployment: str
    majorRevisionId: str
    minorRevisionId: str
    targetResource: str
    targetResourceDisplayName: str
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Trend(typing.TypedDict, total=False):
    duration: str
    valuePercent: float

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1UpdateDetails(typing.TypedDict, total=False):
    orgPolicyUpdate: GoogleCloudAssuredworkloadsV1beta1OrgPolicyUpdate

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Violation(typing.TypedDict, total=False):
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
    state: typing.Literal["STATE_UNSPECIFIED", "RESOLVED", "UNRESOLVED", "EXCEPTION"]
    updateTime: str
    violationType: typing.Literal[
        "VIOLATION_TYPE_UNSPECIFIED", "ORG_POLICY", "RESOURCE"
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationExceptionContext(
    typing.TypedDict, total=False
):
    acknowledgementTime: str
    comment: str
    userName: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediation(
    typing.TypedDict, total=False
):
    compliantValues: _list[str]
    instructions: GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructions
    remediationType: typing.Literal[
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
    typing.TypedDict, total=False
):
    consoleInstructions: (
        GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsConsole
    )
    gcloudInstructions: (
        GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsGcloud
    )

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsConsole(
    typing.TypedDict, total=False
):
    additionalLinks: _list[str]
    consoleUris: _list[str]
    steps: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1ViolationRemediationInstructionsGcloud(
    typing.TypedDict, total=False
):
    additionalLinks: _list[str]
    gcloudCommands: _list[str]
    steps: _list[str]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1Workload(typing.TypedDict, total=False):
    availableUpdates: int
    billingAccount: str
    cjisSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadCJISSettings
    complianceRegime: typing.Literal[
        "COMPLIANCE_REGIME_UNSPECIFIED",
        "ASSURED_WORKLOADS_FOR_PARTNERS",
        "AUSTRALIA_DATA_BOUNDARY_AND_SUPPORT",
        "CANADA_DATA_BOUNDARY_AND_SUPPORT",
        "DATA_BOUNDARY_FOR_CANADA_CONTROLLED_GOODS",
        "DATA_BOUNDARY_FOR_CANADA_PROTECTED_B",
        "DATA_BOUNDARY_FOR_CJIS",
        "DATA_BOUNDARY_FOR_FEDRAMP_HIGH",
        "DATA_BOUNDARY_FOR_FEDRAMP_MODERATE",
        "DATA_BOUNDARY_FOR_IL2",
        "DATA_BOUNDARY_FOR_IL4",
        "DATA_BOUNDARY_FOR_IL5",
        "DATA_BOUNDARY_FOR_IRS_PUBLICATION_1075",
        "DATA_BOUNDARY_FOR_ITAR",
        "EU_DATA_BOUNDARY_AND_SUPPORT",
        "ISRAEL_DATA_BOUNDARY_AND_SUPPORT",
        "JAPAN_DATA_BOUNDARY",
        "SWITZERLAND_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS",
        "KSA_DATA_BOUNDARY_WITH_ACCESS_JUSTIFICATIONS",
        "REGIONAL_DATA_BOUNDARY",
        "US_DATA_BOUNDARY_AND_SUPPORT",
        "US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES",
        "US_DATA_BOUNDARY_FOR_HEALTHCARE_AND_LIFE_SCIENCES_WITH_SUPPORT",
        "AU_REGIONS_AND_US_SUPPORT",
        "CA_PROTECTED_B",
        "CA_REGIONS_AND_SUPPORT",
        "CANADA_CONTROLLED_GOODS",
        "CJIS",
        "EU_REGIONS_AND_SUPPORT",
        "FEDRAMP_HIGH",
        "FEDRAMP_MODERATE",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS",
        "HEALTHCARE_AND_LIFE_SCIENCES_CONTROLS_US_SUPPORT",
        "HIPAA",
        "HITRUST",
        "IL2",
        "IL4",
        "IL5",
        "IRS_1075",
        "ISR_REGIONS",
        "ISR_REGIONS_AND_SUPPORT",
        "ITAR",
        "JP_REGIONS_AND_SUPPORT",
        "KSA_REGIONS_AND_SUPPORT_WITH_SOVEREIGNTY_CONTROLS",
        "REGIONAL_CONTROLS",
        "US_REGIONAL_ACCESS",
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
    kajEnrollmentState: typing.Literal[
        "KAJ_ENROLLMENT_STATE_UNSPECIFIED",
        "KAJ_ENROLLMENT_STATE_PENDING",
        "KAJ_ENROLLMENT_STATE_COMPLETE",
    ]
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings
    labels: dict[str, typing.Any]
    name: str
    partner: typing.Literal[
        "PARTNER_UNSPECIFIED",
        "LOCAL_CONTROLS_BY_S3NS",
        "SOVEREIGN_CONTROLS_BY_T_SYSTEMS",
        "SOVEREIGN_CONTROLS_BY_SIA_MINSAIT",
        "SOVEREIGN_CONTROLS_BY_PSN",
        "SOVEREIGN_CONTROLS_BY_CNTXT",
        "SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM",
        "SPAIN_DATA_BOUNDARY_BY_TELEFONICA",
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
    typing.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadComplianceStatus(
    typing.TypedDict, total=False
):
    acknowledgedResourceViolationCount: int
    acknowledgedViolationCount: int
    activeResourceViolationCount: int
    activeViolationCount: int

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadEkmProvisioningResponse(
    typing.TypedDict, total=False
):
    ekmProvisioningErrorDomain: typing.Literal[
        "EKM_PROVISIONING_ERROR_DOMAIN_UNSPECIFIED",
        "UNSPECIFIED_ERROR",
        "GOOGLE_SERVER_ERROR",
        "EXTERNAL_USER_ERROR",
        "EXTERNAL_PARTNER_ERROR",
        "TIMEOUT_ERROR",
    ]
    ekmProvisioningErrorMapping: typing.Literal[
        "EKM_PROVISIONING_ERROR_MAPPING_UNSPECIFIED",
        "INVALID_SERVICE_ACCOUNT",
        "MISSING_METRICS_SCOPE_ADMIN_PERMISSION",
        "MISSING_EKM_CONNECTION_ADMIN_PERMISSION",
    ]
    ekmProvisioningState: typing.Literal[
        "EKM_PROVISIONING_STATE_UNSPECIFIED",
        "EKM_PROVISIONING_STATE_PENDING",
        "EKM_PROVISIONING_STATE_FAILED",
        "EKM_PROVISIONING_STATE_COMPLETED",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampHighSettings(
    typing.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadFedrampModerateSettings(
    typing.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadIL4Settings(
    typing.TypedDict, total=False
):
    kmsSettings: GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadKMSSettings(
    typing.TypedDict, total=False
):
    nextRotationTime: str
    rotationPeriod: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadPartnerPermissions(
    typing.TypedDict, total=False
):
    accessTransparencyLogsSupportCaseViewer: bool
    assuredWorkloadsMonitoring: bool
    dataLogsViewer: bool
    serviceAccessApprover: bool

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceInfo(
    typing.TypedDict, total=False
):
    resourceId: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "CONSUMER_FOLDER",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadResourceSettings(
    typing.TypedDict, total=False
):
    displayName: str
    resourceId: str
    resourceType: typing.Literal[
        "RESOURCE_TYPE_UNSPECIFIED",
        "CONSUMER_PROJECT",
        "CONSUMER_FOLDER",
        "ENCRYPTION_KEYS_PROJECT",
        "KEYRING",
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadSaaEnrollmentResponse(
    typing.TypedDict, total=False
):
    setupErrors: _list[
        typing.Literal[
            "SETUP_ERROR_UNSPECIFIED",
            "ERROR_INVALID_BASE_SETUP",
            "ERROR_MISSING_EXTERNAL_SIGNING_KEY",
            "ERROR_NOT_ALL_SERVICES_ENROLLED",
            "ERROR_SETUP_CHECK_FAILED",
        ]
    ]
    setupStatus: typing.Literal[
        "SETUP_STATE_UNSPECIFIED", "STATUS_PENDING", "STATUS_COMPLETE"
    ]

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadUpdate(typing.TypedDict, total=False):
    createTime: str
    details: GoogleCloudAssuredworkloadsV1beta1UpdateDetails
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "AVAILABLE", "APPLIED", "WITHDRAWN"]
    updateTime: str

@typing.type_check_only
class GoogleCloudAssuredworkloadsV1beta1WorkloadWorkloadOptions(
    typing.TypedDict, total=False
):
    kajEnrollmentType: typing.Literal[
        "KAJ_ENROLLMENT_TYPE_UNSPECIFIED", "KEY_ACCESS_TRANSPARENCY_OFF"
    ]

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
