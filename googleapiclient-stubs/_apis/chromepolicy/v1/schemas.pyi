import typing

_list = list

@typing.type_check_only
class GoogleChromePolicyVersionsV1AdditionalTargetKeyName(
    typing.TypedDict, total=False
):
    key: str
    keyDescription: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1BatchDeleteGroupPoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyVersionsV1DeleteGroupPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyVersionsV1BatchInheritOrgUnitPoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyVersionsV1BatchModifyGroupPoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyVersionsV1BatchModifyOrgUnitPoliciesRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequest]

@typing.type_check_only
class GoogleChromePolicyVersionsV1CertificateReference(typing.TypedDict, total=False):
    network: str
    orgUnitId: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1DefineCertificateRequest(
    typing.TypedDict, total=False
):
    ceritificateName: str
    certificate: str
    settings: _list[GoogleChromePolicyVersionsV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1DefineCertificateResponse(
    typing.TypedDict, total=False
):
    networkId: str
    settings: _list[GoogleChromePolicyVersionsV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1DefineNetworkRequest(typing.TypedDict, total=False):
    name: str
    settings: _list[GoogleChromePolicyVersionsV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1DefineNetworkResponse(typing.TypedDict, total=False):
    networkId: str
    settings: _list[GoogleChromePolicyVersionsV1NetworkSetting]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1DeleteGroupPolicyRequest(
    typing.TypedDict, total=False
):
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1FieldConstraints(typing.TypedDict, total=False):
    numericRangeConstraint: GoogleChromePolicyVersionsV1NumericRangeConstraint
    uploadedFileConstraints: GoogleChromePolicyVersionsV1UploadedFileConstraints

@typing.type_check_only
class GoogleChromePolicyVersionsV1InheritOrgUnitPolicyRequest(
    typing.TypedDict, total=False
):
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1ListGroupPriorityOrderingRequest(
    typing.TypedDict, total=False
):
    policyNamespace: str
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1ListGroupPriorityOrderingResponse(
    typing.TypedDict, total=False
):
    groupIds: _list[str]
    policyNamespace: str
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1ListPolicySchemasResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    policySchemas: _list[GoogleChromePolicyVersionsV1PolicySchema]

@typing.type_check_only
class GoogleChromePolicyVersionsV1ModifyGroupPolicyRequest(
    typing.TypedDict, total=False
):
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey
    policyValue: GoogleChromePolicyVersionsV1PolicyValue
    updateMask: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1ModifyOrgUnitPolicyRequest(
    typing.TypedDict, total=False
):
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey
    policyValue: GoogleChromePolicyVersionsV1PolicyValue
    updateMask: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1NetworkSetting(typing.TypedDict, total=False):
    policySchema: str
    value: dict[str, typing.Any]

@typing.type_check_only
class GoogleChromePolicyVersionsV1NumericRangeConstraint(typing.TypedDict, total=False):
    maximum: str
    minimum: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyApiLifecycle(typing.TypedDict, total=False):
    deprecatedInFavorOf: _list[str]
    description: str
    endSupport: GoogleTypeDate
    policyApiLifecycleStage: typing.Literal[
        "API_UNSPECIFIED",
        "API_PREVIEW",
        "API_DEVELOPMENT",
        "API_CURRENT",
        "API_DEPRECATED",
    ]
    scheduledToDeprecatePolicies: _list[str]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyModificationError(
    typing.TypedDict, total=False
):
    errors: _list[str]
    fieldErrors: _list[GoogleChromePolicyVersionsV1PolicyModificationFieldError]
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyModificationErrorDetails(
    typing.TypedDict, total=False
):
    modificationErrors: _list[GoogleChromePolicyVersionsV1PolicyModificationError]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyModificationFieldError(
    typing.TypedDict, total=False
):
    error: str
    field: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchema(typing.TypedDict, total=False):
    accessRestrictions: _list[str]
    additionalTargetKeyNames: _list[GoogleChromePolicyVersionsV1AdditionalTargetKeyName]
    categoryTitle: str
    definition: Proto2FileDescriptorProto
    fieldDescriptions: _list[GoogleChromePolicyVersionsV1PolicySchemaFieldDescription]
    name: str
    notices: _list[GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription]
    policyApiLifecycle: GoogleChromePolicyVersionsV1PolicyApiLifecycle
    policyDescription: str
    schemaName: str
    supportUri: str
    supportedPlatforms: _list[
        typing.Literal[
            "PLATFORM_UNSPECIFIED",
            "CHROME_OS",
            "CHROME_BROWSER",
            "CHROME_BROWSER_FOR_ANDROID",
            "CHROME_BROWSER_FOR_IOS",
        ]
    ]
    validTargetResources: _list[
        typing.Literal["TARGET_RESOURCE_UNSPECIFIED", "ORG_UNIT", "GROUP"]
    ]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies(
    typing.TypedDict, total=False
):
    sourceField: str
    sourceFieldValue: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldDescription(
    typing.TypedDict, total=False
):
    defaultValue: typing.Any
    description: str
    field: str
    fieldConstraints: GoogleChromePolicyVersionsV1FieldConstraints
    fieldDependencies: _list[GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies]
    fieldDescription: str
    inputConstraint: str
    knownValueDescriptions: _list[
        GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription
    ]
    name: str
    nestedFieldDescriptions: _list[
        GoogleChromePolicyVersionsV1PolicySchemaFieldDescription
    ]
    requiredItems: _list[GoogleChromePolicyVersionsV1PolicySchemaRequiredItems]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaFieldKnownValueDescription(
    typing.TypedDict, total=False
):
    description: str
    fieldDependencies: _list[GoogleChromePolicyVersionsV1PolicySchemaFieldDependencies]
    value: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaNoticeDescription(
    typing.TypedDict, total=False
):
    acknowledgementRequired: bool
    field: str
    noticeMessage: str
    noticeValue: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaRequiredItems(
    typing.TypedDict, total=False
):
    fieldConditions: _list[str]
    requiredFields: _list[str]

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyTargetKey(typing.TypedDict, total=False):
    additionalTargetKeys: dict[str, typing.Any]
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicyValue(typing.TypedDict, total=False):
    policySchema: str
    value: dict[str, typing.Any]

@typing.type_check_only
class GoogleChromePolicyVersionsV1RemoveCertificateErrorDetails(
    typing.TypedDict, total=False
):
    certificateReferences: _list[GoogleChromePolicyVersionsV1CertificateReference]

@typing.type_check_only
class GoogleChromePolicyVersionsV1RemoveCertificateRequest(
    typing.TypedDict, total=False
):
    networkId: str
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1RemoveCertificateResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1RemoveNetworkRequest(typing.TypedDict, total=False):
    networkId: str
    targetResource: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1RemoveNetworkResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1ResolveRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    policySchemaFilter: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1ResolveResponse(typing.TypedDict, total=False):
    nextPageToken: str
    resolvedPolicies: _list[GoogleChromePolicyVersionsV1ResolvedPolicy]

@typing.type_check_only
class GoogleChromePolicyVersionsV1ResolvedPolicy(typing.TypedDict, total=False):
    addedSourceKey: GoogleChromePolicyVersionsV1PolicyTargetKey
    sourceKey: GoogleChromePolicyVersionsV1PolicyTargetKey
    targetKey: GoogleChromePolicyVersionsV1PolicyTargetKey
    value: GoogleChromePolicyVersionsV1PolicyValue

@typing.type_check_only
class GoogleChromePolicyVersionsV1UpdateGroupPriorityOrderingRequest(
    typing.TypedDict, total=False
):
    groupIds: _list[str]
    policyNamespace: str
    policySchema: str
    policyTargetKey: GoogleChromePolicyVersionsV1PolicyTargetKey

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadPolicyFileRequest(
    typing.TypedDict, total=False
):
    policyField: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadPolicyFileResponse(
    typing.TypedDict, total=False
):
    downloadUri: str

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadedFileConstraints(
    typing.TypedDict, total=False
):
    sizeLimitBytes: str
    supportedContentTypes: _list[
        typing.Literal[
            "CONTENT_TYPE_UNSPECIFIED",
            "CONTENT_TYPE_PLAIN_TEXT",
            "CONTENT_TYPE_HTML",
            "CONTENT_TYPE_IMAGE_JPEG",
            "CONTENT_TYPE_IMAGE_GIF",
            "CONTENT_TYPE_IMAGE_PNG",
            "CONTENT_TYPE_JSON",
            "CONTENT_TYPE_ZIP",
            "CONTENT_TYPE_GZIP",
            "CONTENT_TYPE_CSV",
            "CONTENT_TYPE_YAML",
            "CONTENT_TYPE_IMAGE_WEBP",
        ]
    ]

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class Proto2DescriptorProto(typing.TypedDict, total=False):
    enumType: _list[Proto2EnumDescriptorProto]
    field: _list[Proto2FieldDescriptorProto]
    name: str
    nestedType: _list[Proto2DescriptorProto]
    oneofDecl: _list[Proto2OneofDescriptorProto]
    visibility: typing.Literal[
        "VISIBILITY_UNSET", "VISIBILITY_LOCAL", "VISIBILITY_EXPORT"
    ]

@typing.type_check_only
class Proto2EnumDescriptorProto(typing.TypedDict, total=False):
    name: str
    value: _list[Proto2EnumValueDescriptorProto]
    visibility: typing.Literal[
        "VISIBILITY_UNSET", "VISIBILITY_LOCAL", "VISIBILITY_EXPORT"
    ]

@typing.type_check_only
class Proto2EnumValueDescriptorProto(typing.TypedDict, total=False):
    name: str
    number: int

@typing.type_check_only
class Proto2FieldDescriptorProto(typing.TypedDict, total=False):
    defaultValue: str
    jsonName: str
    label: typing.Literal["LABEL_OPTIONAL", "LABEL_REPEATED", "LABEL_REQUIRED"]
    name: str
    number: int
    oneofIndex: int
    proto3Optional: bool
    type: typing.Literal[
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
class Proto2FileDescriptorProto(typing.TypedDict, total=False):
    editionDeprecated: str
    enumType: _list[Proto2EnumDescriptorProto]
    messageType: _list[Proto2DescriptorProto]
    name: str
    optionDependency: _list[str]
    package: str
    syntax: str

@typing.type_check_only
class Proto2OneofDescriptorProto(typing.TypedDict, total=False):
    name: str
