import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudOrgpolicyV2AlternatePolicySpec(
    typing_extensions.TypedDict, total=False
):
    launch: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2Constraint(typing_extensions.TypedDict, total=False):
    booleanConstraint: GoogleCloudOrgpolicyV2ConstraintBooleanConstraint
    constraintDefault: typing_extensions.Literal[
        "CONSTRAINT_DEFAULT_UNSPECIFIED", "ALLOW", "DENY"
    ]
    description: str
    displayName: str
    listConstraint: GoogleCloudOrgpolicyV2ConstraintListConstraint
    name: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintBooleanConstraint(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintListConstraint(
    typing_extensions.TypedDict, total=False
):
    supportsIn: bool
    supportsUnder: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV2CustomConstraint(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    description: str
    displayName: str
    methodTypes: _list[str]
    name: str
    resourceTypes: _list[str]
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListConstraintsResponse(
    typing_extensions.TypedDict, total=False
):
    constraints: _list[GoogleCloudOrgpolicyV2Constraint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListCustomConstraintsResponse(
    typing_extensions.TypedDict, total=False
):
    customConstraints: _list[GoogleCloudOrgpolicyV2CustomConstraint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListPoliciesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policies: _list[GoogleCloudOrgpolicyV2Policy]

@typing.type_check_only
class GoogleCloudOrgpolicyV2Policy(typing_extensions.TypedDict, total=False):
    alternate: GoogleCloudOrgpolicyV2AlternatePolicySpec
    name: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpec(typing_extensions.TypedDict, total=False):
    etag: str
    inheritFromParent: bool
    reset: bool
    rules: _list[GoogleCloudOrgpolicyV2PolicySpecPolicyRule]
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRule(
    typing_extensions.TypedDict, total=False
):
    allowAll: bool
    condition: GoogleTypeExpr
    denyAll: bool
    enforce: bool
    values: GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues(
    typing_extensions.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeExpr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
