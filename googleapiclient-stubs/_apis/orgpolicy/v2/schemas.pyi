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
    equivalentConstraint: str
    listConstraint: GoogleCloudOrgpolicyV2ConstraintListConstraint
    name: str
    supportsDryRun: bool
    supportsSimulation: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintBooleanConstraint(
    typing_extensions.TypedDict, total=False
):
    customConstraintDefinition: (
        GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinition
    )

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinition(
    typing_extensions.TypedDict, total=False
):
    actionType: typing_extensions.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    methodTypes: _list[
        typing_extensions.Literal[
            "METHOD_TYPE_UNSPECIFIED",
            "CREATE",
            "UPDATE",
            "DELETE",
            "REMOVE_GRANT",
            "GOVERN_TAGS",
        ]
    ]
    parameters: dict[str, typing.Any]
    resourceTypes: _list[str]

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinitionParameter(
    typing_extensions.TypedDict, total=False
):
    defaultValue: typing.Any
    item: typing_extensions.Literal["TYPE_UNSPECIFIED", "LIST", "STRING", "BOOLEAN"]
    metadata: (
        GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinitionParameterMetadata
    )
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "LIST", "STRING", "BOOLEAN"]
    validValuesExpr: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinitionParameterMetadata(
    typing_extensions.TypedDict, total=False
):
    description: str

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
    methodTypes: _list[
        typing_extensions.Literal[
            "METHOD_TYPE_UNSPECIFIED",
            "CREATE",
            "UPDATE",
            "DELETE",
            "REMOVE_GRANT",
            "GOVERN_TAGS",
        ]
    ]
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
    dryRunSpec: GoogleCloudOrgpolicyV2PolicySpec
    etag: str
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
    parameters: dict[str, typing.Any]
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
