import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPolicysimulatorV1Replay(typing_extensions.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1ReplayResultsSummary
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayConfig(
    typing_extensions.TypedDict, total=False
):
    logSource: typing_extensions.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1ReplayResultsSummary(
    typing_extensions.TypedDict, total=False
):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1Replay(typing_extensions.TypedDict, total=False):
    config: GoogleCloudPolicysimulatorV1beta1ReplayConfig
    name: str
    resultsSummary: GoogleCloudPolicysimulatorV1beta1ReplayResultsSummary
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayConfig(
    typing_extensions.TypedDict, total=False
):
    logSource: typing_extensions.Literal["LOG_SOURCE_UNSPECIFIED", "RECENT_ACCESSES"]
    policyOverlay: dict[str, typing.Any]

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str

@typing.type_check_only
class GoogleCloudPolicysimulatorV1beta1ReplayResultsSummary(
    typing_extensions.TypedDict, total=False
):
    differenceCount: int
    errorCount: int
    logCount: int
    newestDate: GoogleTypeDate
    oldestDate: GoogleTypeDate
    unchangedCount: int

@typing.type_check_only
class GoogleIamV1AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[GoogleIamV1AuditLogConfig]
    service: str

@typing.type_check_only
class GoogleIamV1AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class GoogleIamV1Binding(typing_extensions.TypedDict, total=False):
    condition: GoogleTypeExpr
    members: _list[str]
    role: str

@typing.type_check_only
class GoogleIamV1Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[GoogleIamV1AuditConfig]
    bindings: _list[GoogleIamV1Binding]
    etag: str
    version: int

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
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
