import typing

import typing_extensions

_list = list

@typing.type_check_only
class CloudControl2SharedOperationsReconciliationOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    deleteResource: bool
    exclusiveAction: typing_extensions.Literal[
        "UNKNOWN_REPAIR_ACTION", "DELETE", "RETRY"
    ]

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamAdminV1AuditData(typing_extensions.TypedDict, total=False):
    permissionDelta: GoogleIamAdminV1AuditDataPermissionDelta

@typing.type_check_only
class GoogleIamAdminV1AuditDataPermissionDelta(
    typing_extensions.TypedDict, total=False
):
    addedPermissions: _list[str]
    removedPermissions: _list[str]

@typing.type_check_only
class GoogleIamV1BindingDelta(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    condition: GoogleTypeExpr
    member: str
    role: str

@typing.type_check_only
class GoogleIamV1LoggingAuditData(typing_extensions.TypedDict, total=False):
    policyDelta: GoogleIamV1PolicyDelta

@typing.type_check_only
class GoogleIamV1PolicyDelta(typing_extensions.TypedDict, total=False):
    bindingDeltas: _list[GoogleIamV1BindingDelta]

@typing.type_check_only
class GoogleIamV1betaWorkloadIdentityPoolOperationMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleIamV2DenyRule(typing_extensions.TypedDict, total=False):
    denialCondition: GoogleTypeExpr
    deniedPermissions: _list[str]
    deniedPrincipals: _list[str]
    exceptionPermissions: _list[str]
    exceptionPrincipals: _list[str]

@typing.type_check_only
class GoogleIamV2ListPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: _list[GoogleIamV2Policy]

@typing.type_check_only
class GoogleIamV2Policy(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    kind: str
    name: str
    rules: _list[GoogleIamV2PolicyRule]
    uid: str
    updateTime: str

@typing.type_check_only
class GoogleIamV2PolicyOperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str

@typing.type_check_only
class GoogleIamV2PolicyRule(typing_extensions.TypedDict, total=False):
    denyRule: GoogleIamV2DenyRule
    description: str

@typing.type_check_only
class GoogleIamV3OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3alphaOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3betaOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class GoogleIamV3mainOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

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
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
