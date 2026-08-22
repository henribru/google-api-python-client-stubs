import typing

_list = list

@typing.type_check_only
class GoogleCloudOrgpolicyV2AlternatePolicySpec(typing.TypedDict, total=False):
    launch: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2Constraint(typing.TypedDict, total=False):
    booleanConstraint: GoogleCloudOrgpolicyV2ConstraintBooleanConstraint
    constraintDefault: typing.Literal["CONSTRAINT_DEFAULT_UNSPECIFIED", "ALLOW", "DENY"]
    description: str
    displayName: str
    equivalentConstraint: str
    listConstraint: GoogleCloudOrgpolicyV2ConstraintListConstraint
    name: str
    supportsDryRun: bool
    supportsSimulation: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintBooleanConstraint(typing.TypedDict, total=False):
    customConstraintDefinition: (
        GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinition
    )

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinition(
    typing.TypedDict, total=False
):
    actionType: typing.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    methodTypes: _list[
        typing.Literal[
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
    typing.TypedDict, total=False
):
    defaultValue: typing.Any
    item: typing.Literal["TYPE_UNSPECIFIED", "LIST", "STRING", "BOOLEAN"]
    metadata: (
        GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinitionParameterMetadata
    )
    type: typing.Literal["TYPE_UNSPECIFIED", "LIST", "STRING", "BOOLEAN"]
    validValuesExpr: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintCustomConstraintDefinitionParameterMetadata(
    typing.TypedDict, total=False
):
    description: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ConstraintListConstraint(typing.TypedDict, total=False):
    supportsIn: bool
    supportsUnder: bool

@typing.type_check_only
class GoogleCloudOrgpolicyV2CustomConstraint(typing.TypedDict, total=False):
    actionType: typing.Literal["ACTION_TYPE_UNSPECIFIED", "ALLOW", "DENY"]
    condition: str
    description: str
    displayName: str
    methodTypes: _list[
        typing.Literal[
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
class GoogleCloudOrgpolicyV2ListConstraintsResponse(typing.TypedDict, total=False):
    constraints: _list[GoogleCloudOrgpolicyV2Constraint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListCustomConstraintsResponse(
    typing.TypedDict, total=False
):
    customConstraints: _list[GoogleCloudOrgpolicyV2CustomConstraint]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListPoliciesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    policies: _list[GoogleCloudOrgpolicyV2Policy]

@typing.type_check_only
class GoogleCloudOrgpolicyV2Policy(typing.TypedDict, total=False):
    alternate: GoogleCloudOrgpolicyV2AlternatePolicySpec
    dryRunSpec: GoogleCloudOrgpolicyV2PolicySpec
    etag: str
    name: str
    spec: GoogleCloudOrgpolicyV2PolicySpec

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpec(typing.TypedDict, total=False):
    etag: str
    inheritFromParent: bool
    reset: bool
    rules: _list[GoogleCloudOrgpolicyV2PolicySpecPolicyRule]
    updateTime: str

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRule(typing.TypedDict, total=False):
    allowAll: bool
    condition: GoogleTypeExpr
    denyAll: bool
    enforce: bool
    parameters: dict[str, typing.Any]
    values: GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicySpecPolicyRuleStringValues(
    typing.TypedDict, total=False
):
    allowedValues: _list[str]
    deniedValues: _list[str]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeExpr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str
