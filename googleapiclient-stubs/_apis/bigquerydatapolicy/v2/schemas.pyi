import typing

import typing_extensions

_list = list

@typing.type_check_only
class AddGranteesRequest(typing_extensions.TypedDict, total=False):
    grantees: _list[str]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CreateDataPolicyRequest(typing_extensions.TypedDict, total=False):
    dataPolicy: DataPolicy
    dataPolicyId: str

@typing.type_check_only
class DataMaskingPolicy(typing_extensions.TypedDict, total=False):
    predefinedExpression: typing_extensions.Literal[
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
class DataPolicy(typing_extensions.TypedDict, total=False):
    dataMaskingPolicy: DataMaskingPolicy
    dataPolicyId: str
    dataPolicyType: typing_extensions.Literal[
        "DATA_POLICY_TYPE_UNSPECIFIED",
        "DATA_MASKING_POLICY",
        "RAW_DATA_ACCESS_POLICY",
        "COLUMN_LEVEL_SECURITY_POLICY",
    ]
    etag: str
    grantees: _list[str]
    name: str
    policyTag: str
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "V1", "V2"]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListDataPoliciesResponse(typing_extensions.TypedDict, total=False):
    dataPolicies: _list[DataPolicy]
    nextPageToken: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RemoveGranteesRequest(typing_extensions.TypedDict, total=False):
    grantees: _list[str]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]
