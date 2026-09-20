import typing

_list = list

@typing.type_check_only
class AuditReport(typing.TypedDict, total=False):
    complianceFramework: str
    complianceStandard: str
    controlDetails: _list[ControlDetails]
    createTime: str
    destinationDetails: DestinationDetails
    name: str
    operationId: str
    reportGenerationState: typing.Literal[
        "REPORT_GENERATION_STATE_UNSPECIFIED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "SUMMARY_UNKNOWN",
    ]
    reportSummary: ReportSummary
    scope: str
    scopeId: str

@typing.type_check_only
class AuditScopeReport(typing.TypedDict, total=False):
    name: str
    scopeReportContents: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Control(typing.TypedDict, total=False):
    controlFamily: ControlFamily
    customerResponsibilityDescription: str
    customerResponsibilityImplementation: str
    description: str
    displayName: str
    family: typing.Literal[
        "FAMILY_UNSPECIFIED",
        "AC",
        "AT",
        "AU",
        "CA",
        "CM",
        "CP",
        "IA",
        "IR",
        "MA",
        "MP",
        "PE",
        "PL",
        "PS",
        "RA",
        "SA",
        "SC",
        "SI",
        "SR",
    ]
    googleResponsibilityDescription: str
    googleResponsibilityImplementation: str
    id: str
    responsibilityType: str

@typing.type_check_only
class ControlDetails(typing.TypedDict, total=False):
    complianceState: typing.Literal[
        "COMPLIANCE_STATE_UNSPECIFIED",
        "COMPLIANT",
        "VIOLATION",
        "MANUAL_REVIEW_NEEDED",
        "ERROR",
        "AUDIT_NOT_SUPPORTED",
    ]
    control: Control
    controlReportSummary: ReportSummary

@typing.type_check_only
class ControlFamily(typing.TypedDict, total=False):
    displayName: str
    familyId: str

@typing.type_check_only
class DestinationDetails(typing.TypedDict, total=False):
    gcsBucketUri: str

@typing.type_check_only
class EligibleDestination(typing.TypedDict, total=False):
    eligibleGcsBucket: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnrollResourceRequest(typing.TypedDict, total=False):
    destinations: _list[EligibleDestination]
    validateOnly: bool

@typing.type_check_only
class Enrollment(typing.TypedDict, total=False):
    destinationDetails: _list[DestinationDetails]
    name: str

@typing.type_check_only
class GenerateAuditReportRequest(typing.TypedDict, total=False):
    complianceFramework: str
    complianceStandard: str
    gcsUri: str
    reportFormat: typing.Literal[
        "AUDIT_REPORT_FORMAT_UNSPECIFIED", "AUDIT_REPORT_FORMAT_ODF"
    ]
    validateOnly: bool

@typing.type_check_only
class GenerateAuditScopeReportRequest(typing.TypedDict, total=False):
    complianceFramework: str
    complianceStandard: str
    reportFormat: typing.Literal[
        "AUDIT_SCOPE_REPORT_FORMAT_UNSPECIFIED", "AUDIT_SCOPE_REPORT_FORMAT_ODF"
    ]
    validateOnly: bool

@typing.type_check_only
class ListAuditReportsResponse(typing.TypedDict, total=False):
    auditReports: _list[AuditReport]
    nextPageToken: str

@typing.type_check_only
class ListControlsResponse(typing.TypedDict, total=False):
    controls: _list[Control]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListResourceEnrollmentStatusesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resourceEnrollmentStatuses: _list[ResourceEnrollmentStatus]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

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
class ReportGenerationProgress(typing.TypedDict, total=False):
    auditReport: str
    destinationGcsBucket: str
    evaluationPercentComplete: float
    failureReason: str
    reportGenerationPercentComplete: float
    reportUploadingPercentComplete: float
    state: typing.Literal[
        "OPERATION_STATE_UNSPECIFIED",
        "OPERATION_STATE_NOT_STARTED",
        "OPERATION_STATE_EVALUATION_IN_PROGRESS",
        "OPERATION_STATE_EVALUATION_DONE",
        "OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS",
        "OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE",
        "OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS",
        "OPERATION_STATE_DONE",
        "OPERATION_STATE_FAILED",
    ]

@typing.type_check_only
class ReportSummary(typing.TypedDict, total=False):
    compliantCount: int
    errorCount: int
    manualReviewNeededCount: int
    totalCount: int
    violationCount: int

@typing.type_check_only
class ResourceEnrollmentStatus(typing.TypedDict, total=False):
    displayName: str
    enrolled: bool
    enrollment: Enrollment
    enrollmentState: typing.Literal[
        "RESOURCE_ENROLLMENT_STATE_UNSPECIFIED", "NOT_ENROLLED", "INHERITED", "ENROLLED"
    ]
    name: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
