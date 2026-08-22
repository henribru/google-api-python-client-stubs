import typing

_list = list

@typing.type_check_only
class AccessApprovalRequest(typing.TypedDict, total=False):
    name: str
    requestTime: str
    requestedExpirationTime: str
    requestedReason: AccessReason

@typing.type_check_only
class AccessReason(typing.TypedDict, total=False):
    detail: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "CUSTOMER_INITIATED_SUPPORT",
        "GOOGLE_INITIATED_SERVICE",
        "GOOGLE_INITIATED_REVIEW",
        "THIRD_PARTY_DATA_REQUEST",
        "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
        "CLOUD_INITIATED_ACCESS",
    ]

@typing.type_check_only
class ConnectionError(typing.TypedDict, total=False):
    errorDomain: str
    errorMessage: str

@typing.type_check_only
class Console(typing.TypedDict, total=False):
    additionalLinks: _list[str]
    consoleUris: _list[str]
    steps: _list[str]

@typing.type_check_only
class Customer(typing.TypedDict, total=False):
    customerOnboardingState: CustomerOnboardingState
    displayName: str
    isOnboarded: bool
    name: str
    organizationDomain: str

@typing.type_check_only
class CustomerOnboardingState(typing.TypedDict, total=False):
    onboardingSteps: _list[CustomerOnboardingStep]

@typing.type_check_only
class CustomerOnboardingStep(typing.TypedDict, total=False):
    completionState: typing.Literal[
        "COMPLETION_STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "NOT_APPLICABLE",
    ]
    completionTime: str
    startTime: str
    step: typing.Literal["STEP_UNSPECIFIED", "KAJ_ENROLLMENT", "CUSTOMER_ENVIRONMENT"]

@typing.type_check_only
class EkmConnection(typing.TypedDict, total=False):
    connectionError: ConnectionError
    connectionName: str
    connectionState: typing.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "AVAILABLE",
        "NOT_AVAILABLE",
        "ERROR",
        "PERMISSION_DENIED",
    ]

@typing.type_check_only
class EkmConnections(typing.TypedDict, total=False):
    ekmConnections: _list[EkmConnection]
    name: str

@typing.type_check_only
class EkmMetadata(typing.TypedDict, total=False):
    ekmEndpointUri: str
    ekmSolution: typing.Literal[
        "EKM_SOLUTION_UNSPECIFIED", "FORTANIX", "FUTUREX", "THALES", "VIRTRU"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Gcloud(typing.TypedDict, total=False):
    additionalLinks: _list[str]
    gcloudCommands: _list[str]
    steps: _list[str]

@typing.type_check_only
class Instructions(typing.TypedDict, total=False):
    consoleInstructions: Console
    gcloudInstructions: Gcloud

@typing.type_check_only
class ListAccessApprovalRequestsResponse(typing.TypedDict, total=False):
    accessApprovalRequests: _list[AccessApprovalRequest]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCustomersResponse(typing.TypedDict, total=False):
    customers: _list[Customer]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListViolationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    violations: _list[Violation]

@typing.type_check_only
class ListWorkloadsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workloads: _list[Workload]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Partner(typing.TypedDict, total=False):
    createTime: str
    ekmSolutions: _list[EkmMetadata]
    name: str
    operatedCloudRegions: _list[str]
    partnerProjectId: str
    skus: _list[Sku]
    updateTime: str

@typing.type_check_only
class PartnerPermissions(typing.TypedDict, total=False):
    name: str
    partnerPermissions: _list[
        typing.Literal[
            "PERMISSION_UNSPECIFIED",
            "ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS",
            "ASSURED_WORKLOADS_MONITORING",
            "ACCESS_APPROVAL_REQUESTS",
            "ASSURED_WORKLOADS_EKM_CONNECTION_STATUS",
            "ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER",
        ]
    ]

@typing.type_check_only
class Remediation(typing.TypedDict, total=False):
    compliantValues: _list[str]
    instructions: Instructions
    remediationType: typing.Literal[
        "REMEDIATION_TYPE_UNSPECIFIED",
        "REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION",
        "REMEDIATION_RESOURCE_VIOLATION",
    ]

@typing.type_check_only
class Sku(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class Violation(typing.TypedDict, total=False):
    beginTime: str
    category: str
    description: str
    folderId: str
    name: str
    nonCompliantOrgPolicy: str
    remediation: Remediation
    resolveTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "RESOLVED", "UNRESOLVED", "EXCEPTION"]
    updateTime: str

@typing.type_check_only
class Workload(typing.TypedDict, total=False):
    createTime: str
    folder: str
    folderId: str
    isOnboarded: bool
    keyManagementProjectId: str
    location: str
    name: str
    partner: typing.Literal[
        "PARTNER_UNSPECIFIED",
        "PARTNER_LOCAL_CONTROLS_BY_S3NS",
        "PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS",
        "PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT",
        "PARTNER_SOVEREIGN_CONTROLS_BY_PSN",
        "PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT",
        "PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM",
        "PARTNER_SPAIN_DATA_BOUNDARY_BY_TELEFONICA",
    ]
    workloadOnboardingState: WorkloadOnboardingState

@typing.type_check_only
class WorkloadOnboardingState(typing.TypedDict, total=False):
    onboardingSteps: _list[WorkloadOnboardingStep]

@typing.type_check_only
class WorkloadOnboardingStep(typing.TypedDict, total=False):
    completionState: typing.Literal[
        "COMPLETION_STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "NOT_APPLICABLE",
    ]
    completionTime: str
    startTime: str
    step: typing.Literal[
        "STEP_UNSPECIFIED", "EKM_PROVISIONED", "SIGNED_ACCESS_APPROVAL_CONFIGURED"
    ]
