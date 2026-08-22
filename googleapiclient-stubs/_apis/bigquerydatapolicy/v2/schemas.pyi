import typing

_list = list

@typing.type_check_only
class AddGranteesRequest(typing.TypedDict, total=False):
    grantees: _list[str]

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CreateDataPolicyRequest(typing.TypedDict, total=False):
    dataPolicy: DataPolicy
    dataPolicyId: str

@typing.type_check_only
class DataGovernanceTag(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DataMaskingPolicy(typing.TypedDict, total=False):
    predefinedExpression: typing.Literal[
        "PREDEFINED_EXPRESSION_UNSPECIFIED",
        "SHA256",
        "ALWAYS_NULL",
        "DEFAULT_MASKING_VALUE",
        "LAST_FOUR_CHARACTERS",
        "FIRST_FOUR_CHARACTERS",
        "EMAIL_MASK",
        "DATE_YEAR_MASK",
        "RANDOM_HASH",
    ]
    routine: str

@typing.type_check_only
class DataPolicy(typing.TypedDict, total=False):
    dataGovernanceTag: DataGovernanceTag
    dataMaskingPolicy: DataMaskingPolicy
    dataPolicyId: str
    dataPolicyType: typing.Literal[
        "DATA_POLICY_TYPE_UNSPECIFIED",
        "DATA_MASKING_POLICY",
        "RAW_DATA_ACCESS_POLICY",
        "COLUMN_LEVEL_SECURITY_POLICY",
    ]
    etag: str
    grantees: _list[str]
    name: str
    policyTag: str
    version: typing.Literal["VERSION_UNSPECIFIED", "V1", "V2"]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListDataPoliciesResponse(typing.TypedDict, total=False):
    dataPolicies: _list[DataPolicy]
    nextPageToken: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RemoveGranteesRequest(typing.TypedDict, total=False):
    grantees: _list[str]

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
