import typing

_list = list

@typing.type_check_only
class CloudControl2SharedOperationsReconciliationOperationMetadata(
    typing.TypedDict, total=False
):
    deleteResource: bool
    exclusiveAction: typing.Literal["UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"]

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamAdminV1AuditData(typing.TypedDict, total=False):
    permissionDelta: GoogleIamAdminV1AuditDataPermissionDelta

@typing.type_check_only
class GoogleIamAdminV1AuditDataPermissionDelta(typing.TypedDict, total=False):
    addedPermissions: _list[str]
    removedPermissions: _list[str]

@typing.type_check_only
class GoogleIamV1BindingDelta(typing.TypedDict, total=False):
    action: typing.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    condition: GoogleTypeExpr
    member: str
    role: str

@typing.type_check_only
class GoogleIamV1LoggingAuditData(typing.TypedDict, total=False):
    policyDelta: GoogleIamV1PolicyDelta

@typing.type_check_only
class GoogleIamV1PolicyDelta(typing.TypedDict, total=False):
    bindingDeltas: _list[GoogleIamV1BindingDelta]

@typing.type_check_only
class GoogleIamV1betaWorkloadIdentityPoolOperationMetadata(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleIamV2betaDenyRule(typing.TypedDict, total=False):
    denialCondition: GoogleTypeExpr
    deniedPermissions: _list[str]
    deniedPrincipals: _list[str]
    exceptionPermissions: _list[str]
    exceptionPrincipals: _list[str]

@typing.type_check_only
class GoogleIamV2betaListPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policies: _list[GoogleIamV2betaPolicy]

@typing.type_check_only
class GoogleIamV2betaPolicy(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    kind: str
    name: str
    rules: _list[GoogleIamV2betaPolicyRule]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleIamV2betaPolicyOperationMetadata(typing.TypedDict, total=False):
    createTime: str

@typing.type_check_only
class GoogleIamV2betaPolicyRule(typing.TypedDict, total=False):
    denyRule: GoogleIamV2betaDenyRule
    description: str

@typing.type_check_only
class GoogleIamV3OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3alphaOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3betaOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3mainOperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

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
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
