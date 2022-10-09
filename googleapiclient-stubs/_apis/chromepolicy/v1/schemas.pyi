import typing

import typing_extensions

_list = list

@typing.type_check_only
class ChromeCrosDpanelAutosettingsProtoPolicyApiLifecycle(
    typing_extensions.TypedDict, total=False
):
    description: str
    endSupport: GoogleTypeDate
    policyApiLifecycleStage: typing_extensions.Literal[
        "API_UNSPECIFIED",
        "API_PREVIEW",
        "API_DEVELOPMENT",
        "API_CURRENT",
        "API_DEPRECATED",
    ]

@typing.type_check_only
class GoogleChromePolicyV1BatchDeleteGroupPoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyV1DeleteGroupPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyV1BatchInheritOrgUnitPoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyV1InheritOrgUnitPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyV1BatchModifyGroupPoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyV1ModifyGroupPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyV1BatchModifyOrgUnitPoliciesRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyV1ModifyOrgUnitPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyV1DefineCertificateRequest(
    typing_extensions.TypedDict, total=False
):
    ceritificateName: str
    certificate: str
    settings: _list[GoogleChromePolicyV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1DefineCertificateResponse(
    typing_extensions.TypedDict, total=False
):
    networkId: str
    settings: _list[GoogleChromePolicyV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1DefineNetworkRequest(
    typing_extensions.TypedDict, total=False
):
    name: str
    settings: _list[GoogleChromePolicyV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1DefineNetworkResponse(
    typing_extensions.TypedDict, total=False
):
    networkId: str
    settings: _list[GoogleChromePolicyV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1DeleteGroupPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    policySchema: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyV1InheritOrgUnitPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    policySchema: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyV1ListGroupPriorityOrderingRequest(
    typing_extensions.TypedDict, total=False
):
    policyNamespace: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyV1ListGroupPriorityOrderingResponse(
    typing_extensions.TypedDict, total=False
):
    groupIds: _list[str]
    policyNamespace: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyV1ModifyGroupPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey
    policyValue: GoogleChromePolicyV1PolicyValue
    updateMask: str

@typing.type_check_only
class GoogleChromePolicyV1ModifyOrgUnitPolicyRequest(
    typing_extensions.TypedDict, total=False
):
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey
    policyValue: GoogleChromePolicyV1PolicyValue
    updateMask: str

@typing.type_check_only
class GoogleChromePolicyV1NetworkSetting(typing_extensions.TypedDict, total=False):
    policySchema: str
    value: dict[str, typing.Any]

@typing.type_check_only
class GoogleChromePolicyV1PolicyModificationFieldError(
    typing_extensions.TypedDict, total=False
):
    error: str
    field: str

@typing.type_check_only
class GoogleChromePolicyV1PolicyTargetKey(typing_extensions.TypedDict, total=False):
    additionalTargetKeys: dict[str, typing.Any]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1PolicyValue(typing_extensions.TypedDict, total=False):
    policySchema: str
    value: dict[str, typing.Any]

@typing.type_check_only
class GoogleChromePolicyV1RemoveCertificateRequest(
    typing_extensions.TypedDict, total=False
):
    networkId: str
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1RemoveCertificateResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleChromePolicyV1RemoveNetworkRequest(
    typing_extensions.TypedDict, total=False
):
    networkId: str
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyV1RemoveNetworkResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleChromePolicyV1ResolveRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    pageToken: str
    policySchemaFilter: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyV1ResolveResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resolvedPolicies: _list[GoogleChromePolicyV1ResolvedPolicy]

@typing.type_check_only
class GoogleChromePolicyV1ResolvedPolicy(typing_extensions.TypedDict, total=False):
    addedSourceKey: GoogleChromePolicyV1PolicyTargetKey
    sourceKey: GoogleChromePolicyV1PolicyTargetKey
    targetKey: GoogleChromePolicyV1PolicyTargetKey
    value: GoogleChromePolicyV1PolicyValue

@typing.type_check_only
class GoogleChromePolicyV1UpdateGroupPriorityOrderingRequest(
    typing_extensions.TypedDict, total=False
):
    groupIds: _list[str]
    policyNamespace: str
    policyTargetKey: GoogleChromePolicyV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1AdditionalTargetKeyName(
    typing_extensions.TypedDict, total=False
):
    key: str
    keyDescription: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1ListPolicySchemasResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    policySchemas: _list[GoogleChromePolicyVersionsV1PolicySchema]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchema(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies(
    typing_extensions.TypedDict, total=False
):
    sourceField: str
    sourceFieldValue: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldDescription(
    dict[str, typing.Any]
): ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription(
    typing_extensions.TypedDict, total=False
):
    description: str
    value: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription(
    typing_extensions.TypedDict, total=False
):
    acknowledgementRequired: bool
    field: str
    noticeMessage: str
    noticeValue: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaRequiredItems(
    typing_extensions.TypedDict, total=False
):
    fieldConditions: _list[str]
    requiredFields: _list[str]

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadPolicyFileRequest(
    typing_extensions.TypedDict, total=False
):
    policyField: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadPolicyFileResponse(
    typing_extensions.TypedDict, total=False
):
    downloadUri: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Proto2DescriptorProto(dict[str, typing.Any]): ...

@typing.type_check_only
class Proto2EnumDescriptorProto(typing_extensions.TypedDict, total=False):
    name: str
    value: _list[Proto2EnumValueDescriptorProto]

@typing.type_check_only
class Proto2EnumValueDescriptorProto(typing_extensions.TypedDict, total=False):
    name: str
    number: int

@typing.type_check_only
class Proto2FieldDescriptorProto(typing_extensions.TypedDict, total=False):
    defaultValue: str
    jsonName: str
    label: typing_extensions.Literal[
        "LABEL_OPTIONAL", "LABEL_REQUIRED", "LABEL_REPEATED"
    ]
    name: str
    number: int
    oneofIndex: int
    proto3Optional: bool
    type: typing_extensions.Literal[
        "TYPE_DOUBLE",
        "TYPE_FLOAT",
        "TYPE_INT64",
        "TYPE_UINT64",
        "TYPE_INT32",
        "TYPE_FIXED64",
        "TYPE_FIXED32",
        "TYPE_BOOL",
        "TYPE_STRING",
        "TYPE_GROUP",
        "TYPE_MESSAGE",
        "TYPE_BYTES",
        "TYPE_UINT32",
        "TYPE_ENUM",
        "TYPE_SFIXED32",
        "TYPE_SFIXED64",
        "TYPE_SINT32",
        "TYPE_SINT64",
    ]
    typeName: str

@typing.type_check_only
class Proto2FileDescriptorProto(dict[str, typing.Any]): ...

@typing.type_check_only
class Proto2OneofDescriptorProto(typing_extensions.TypedDict, total=False):
    name: str
