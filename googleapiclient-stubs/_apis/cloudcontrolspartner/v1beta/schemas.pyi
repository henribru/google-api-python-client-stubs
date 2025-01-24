import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessApprovalRequest(typing_extensions.TypedDict, total=False):
    name: str
    requestTime: str
    requestedExpirationTime: str
    requestedReason: AccessReason

@typing.type_check_only
class AccessReason(typing_extensions.TypedDict, total=False):
    detail: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "CUSTOMER_INITIATED_SUPPORT",
        "GOOGLE_INITIATED_SERVICE",
        "GOOGLE_INITIATED_REVIEW",
        "THIRD_PARTY_DATA_REQUEST",
        "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
        "CLOUD_INITIATED_ACCESS",
    ]

@typing.type_check_only
class ConnectionError(typing_extensions.TypedDict, total=False):
    errorDomain: str
    errorMessage: str

@typing.type_check_only
class Console(typing_extensions.TypedDict, total=False):
    additionalLinks: _list[str]
    consoleUris: _list[str]
    steps: _list[str]

@typing.type_check_only
class Customer(typing_extensions.TypedDict, total=False):
    customerOnboardingState: CustomerOnboardingState
    displayName: str
    isOnboarded: bool
    name: str
    organizationDomain: str

@typing.type_check_only
class CustomerOnboardingState(typing_extensions.TypedDict, total=False):
    onboardingSteps: _list[CustomerOnboardingStep]

@typing.type_check_only
class CustomerOnboardingStep(typing_extensions.TypedDict, total=False):
    completionState: typing_extensions.Literal[
        "COMPLETION_STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "NOT_APPLICABLE",
    ]
    completionTime: str
    startTime: str
    step: typing_extensions.Literal[
        "STEP_UNSPECIFIED", "KAJ_ENROLLMENT", "CUSTOMER_ENVIRONMENT"
    ]

@typing.type_check_only
class EkmConnection(typing_extensions.TypedDict, total=False):
    connectionError: ConnectionError
    connectionName: str
    connectionState: typing_extensions.Literal[
        "CONNECTION_STATE_UNSPECIFIED",
        "AVAILABLE",
        "NOT_AVAILABLE",
        "ERROR",
        "PERMISSION_DENIED",
    ]

@typing.type_check_only
class EkmConnections(typing_extensions.TypedDict, total=False):
    ekmConnections: _list[EkmConnection]
    name: str

@typing.type_check_only
class EkmMetadata(typing_extensions.TypedDict, total=False):
    ekmEndpointUri: str
    ekmSolution: typing_extensions.Literal[
        "EKM_SOLUTION_UNSPECIFIED", "FORTANIX", "FUTUREX", "THALES", "VIRTRU"
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Gcloud(typing_extensions.TypedDict, total=False):
    additionalLinks: _list[str]
    gcloudCommands: _list[str]
    steps: _list[str]

@typing.type_check_only
class Instructions(typing_extensions.TypedDict, total=False):
    consoleInstructions: Console
    gcloudInstructions: Gcloud

@typing.type_check_only
class ListAccessApprovalRequestsResponse(typing_extensions.TypedDict, total=False):
    accessApprovalRequests: _list[AccessApprovalRequest]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListCustomersResponse(typing_extensions.TypedDict, total=False):
    customers: _list[Customer]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListViolationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    violations: _list[Violation]

@typing.type_check_only
class ListWorkloadsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unreachable: _list[str]
    workloads: _list[Workload]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Partner(typing_extensions.TypedDict, total=False):
    createTime: str
    ekmSolutions: _list[EkmMetadata]
    name: str
    operatedCloudRegions: _list[str]
    partnerProjectId: str
    skus: _list[Sku]
    updateTime: str

@typing.type_check_only
class PartnerPermissions(typing_extensions.TypedDict, total=False):
    name: str
    partnerPermissions: _list[
        typing_extensions.Literal[
            "PERMISSION_UNSPECIFIED",
            "ACCESS_TRANSPARENCY_AND_EMERGENCY_ACCESS_LOGS",
            "ASSURED_WORKLOADS_MONITORING",
            "ACCESS_APPROVAL_REQUESTS",
            "ASSURED_WORKLOADS_EKM_CONNECTION_STATUS",
            "ACCESS_TRANSPARENCY_LOGS_SUPPORT_CASE_VIEWER",
        ]
    ]

@typing.type_check_only
class Remediation(typing_extensions.TypedDict, total=False):
    compliantValues: _list[str]
    instructions: Instructions
    remediationType: typing_extensions.Literal[
        "REMEDIATION_TYPE_UNSPECIFIED",
        "REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION",
        "REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION",
        "REMEDIATION_RESOURCE_VIOLATION",
    ]

@typing.type_check_only
class Sku(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class Violation(typing_extensions.TypedDict, total=False):
    beginTime: str
    category: str
    description: str
    folderId: str
    name: str
    nonCompliantOrgPolicy: str
    remediation: Remediation
    resolveTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RESOLVED", "UNRESOLVED", "EXCEPTION"
    ]
    updateTime: str

@typing.type_check_only
class Workload(typing_extensions.TypedDict, total=False):
    createTime: str
    folder: str
    folderId: str
    isOnboarded: bool
    keyManagementProjectId: str
    location: str
    name: str
    partner: typing_extensions.Literal[
        "PARTNER_UNSPECIFIED",
        "PARTNER_LOCAL_CONTROLS_BY_S3NS",
        "PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS",
        "PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT",
        "PARTNER_SOVEREIGN_CONTROLS_BY_PSN",
        "PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT",
        "PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM",
    ]
    workloadOnboardingState: WorkloadOnboardingState

@typing.type_check_only
class WorkloadOnboardingState(typing_extensions.TypedDict, total=False):
    onboardingSteps: _list[WorkloadOnboardingStep]

@typing.type_check_only
class WorkloadOnboardingStep(typing_extensions.TypedDict, total=False):
    completionState: typing_extensions.Literal[
        "COMPLETION_STATE_UNSPECIFIED",
        "PENDING",
        "SUCCEEDED",
        "FAILED",
        "NOT_APPLICABLE",
    ]
    completionTime: str
    startTime: str
    step: typing_extensions.Literal[
        "STEP_UNSPECIFIED", "EKM_PROVISIONED", "SIGNED_ACCESS_APPROVAL_CONFIGURED"
    ]
