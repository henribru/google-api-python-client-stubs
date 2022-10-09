import typing

import typing_extensions

_list = list

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
class GoogleIamV2betaDenyRule(typing_extensions.TypedDict, total=False):
    denialCondition: GoogleTypeExpr
    deniedPermissions: _list[str]
    deniedPrincipals: _list[str]
    exceptionPermissions: _list[str]
    exceptionPrincipals: _list[str]

@typing.type_check_only
class GoogleIamV2betaListPoliciesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    policies: _list[GoogleIamV2betaPolicy]

@typing.type_check_only
class GoogleIamV2betaPolicy(typing_extensions.TypedDict, total=False):
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
class GoogleIamV2betaPolicyOperationMetadata(typing_extensions.TypedDict, total=False):
    createTime: str

@typing.type_check_only
class GoogleIamV2betaPolicyRule(typing_extensions.TypedDict, total=False):
    denyRule: GoogleIamV2betaDenyRule
    description: str

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
