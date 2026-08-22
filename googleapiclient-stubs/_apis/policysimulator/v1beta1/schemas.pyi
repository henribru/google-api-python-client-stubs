import typing

_list = list

@typing.type_check_only
class GoogleCloudPolicysimulatorV1Replay(typing.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1ReplayResultsSummary
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayConfig(typing.TypedDict, total=False):
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayOperationMetadata(
    typing.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayResultsSummary(typing.TypedDict, total=False):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1Replay(typing.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1beta1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1beta1ReplayResultsSummary
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayConfig(typing.TypedDict, total=False):
    logSource: typing.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayOperationMetadata(
    typing.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayResultsSummary(
    typing.TypedDict, total=False
):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleIamV1AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
