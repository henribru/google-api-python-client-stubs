import typing

import typing_extensions

_list = list

@typing.type_check_only
class AsyncOptions(typing_extensions.TypedDict, total=False):
    methodMatch: str
    pollingOptions: PollingOptions

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
class BaseType(typing_extensions.TypedDict, total=False):
    collectionOverrides: _list[CollectionOverride]
    credential: Credential
    descriptorUrl: str
    options: Options

@typing.type_check_only
class BasicAuth(typing_extensions.TypedDict, total=False):
    password: str
    user: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CollectionOverride(typing_extensions.TypedDict, total=False):
    collection: str
    options: Options

@typing.type_check_only
class CompositeType(typing_extensions.TypedDict, total=False):
    description: str
    id: str
    insertTime: str
    labels: _list[CompositeTypeLabelEntry]
    name: str
    operation: Operation
    selfLink: str
    status: typing_extensions.Literal[
        "UNKNOWN_STATUS", "DEPRECATED", "EXPERIMENTAL", "SUPPORTED"
    ]
    templateContents: TemplateContents

@typing.type_check_only
class CompositeTypeLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class CompositeTypesListResponse(typing_extensions.TypedDict, total=False):
    compositeTypes: _list[CompositeType]
    nextPageToken: str

@typing.type_check_only
class ConfigFile(typing_extensions.TypedDict, total=False):
    content: str

@typing.type_check_only
class Credential(typing_extensions.TypedDict, total=False):
    basicAuth: BasicAuth
    serviceAccount: ServiceAccount
    useProjectDefault: bool

@typing.type_check_only
class Deployment(typing_extensions.TypedDict, total=False):
    description: str
    fingerprint: str
    id: str
    insertTime: str
    labels: _list[DeploymentLabelEntry]
    manifest: str
    name: str
    operation: Operation
    selfLink: str
    target: TargetConfiguration
    update: DeploymentUpdate
    updateTime: str

@typing.type_check_only
class DeploymentLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentUpdate(typing_extensions.TypedDict, total=False):
    description: str
    labels: _list[DeploymentUpdateLabelEntry]
    manifest: str

@typing.type_check_only
class DeploymentUpdateLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class DeploymentsCancelPreviewRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class DeploymentsListResponse(typing_extensions.TypedDict, total=False):
    deployments: _list[Deployment]
    nextPageToken: str

@typing.type_check_only
class DeploymentsStopRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

@typing.type_check_only
class Diagnostic(typing_extensions.TypedDict, total=False):
    field: str
    level: typing_extensions.Literal["UNKNOWN", "INFORMATION", "WARNING", "ERROR"]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    policy: Policy

@typing.type_check_only
class ImportFile(typing_extensions.TypedDict, total=False):
    content: str
    name: str

@typing.type_check_only
class InputMapping(typing_extensions.TypedDict, total=False):
    fieldName: str
    location: typing_extensions.Literal["UNKNOWN", "PATH", "QUERY", "BODY", "HEADER"]
    methodMatch: str
    value: str

@typing.type_check_only
class Manifest(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    expandedConfig: str
    id: str
    imports: _list[ImportFile]
    insertTime: str
    layout: str
    manifestSizeBytes: str
    manifestSizeLimitBytes: str
    name: str
    selfLink: str

@typing.type_check_only
class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    manifests: _list[Manifest]
    nextPageToken: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: dict[str, typing.Any]
    httpErrorMessage: str
    httpErrorStatusCode: int
    id: str
    insertTime: str
    kind: str
    name: str
    operationGroupId: str
    operationType: str
    progress: int
    region: str
    selfLink: str
    startTime: str
    status: typing_extensions.Literal["PENDING", "RUNNING", "DONE"]
    statusMessage: str
    targetId: str
    targetLink: str
    user: str
    warnings: _list[dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    asyncOptions: _list[AsyncOptions]
    inputMappings: _list[InputMapping]
    validationOptions: ValidationOptions
    virtualProperties: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PollingOptions(typing_extensions.TypedDict, total=False):
    diagnostics: _list[Diagnostic]
    failCondition: str
    finishCondition: str
    pollingLink: str
    targetLink: str

@typing.type_check_only
class Resource(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    finalProperties: str
    id: str
    insertTime: str
    manifest: str
    name: str
    properties: str
    type: str
    update: ResourceUpdate
    updateTime: str
    url: str
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

@typing.type_check_only
class ResourceUpdate(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    error: dict[str, typing.Any]
    finalProperties: str
    intent: typing_extensions.Literal[
        "CREATE_OR_ACQUIRE", "DELETE", "ACQUIRE", "UPDATE", "ABANDON", "CREATE"
    ]
    manifest: str
    properties: str
    state: typing_extensions.Literal[
        "PENDING", "IN_PROGRESS", "IN_PREVIEW", "FAILED", "ABORTED"
    ]
    warnings: _list[dict[str, typing.Any]]

@typing.type_check_only
class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: _list[Resource]

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class TargetConfiguration(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    imports: _list[ImportFile]

@typing.type_check_only
class TemplateContents(typing_extensions.TypedDict, total=False):
    imports: _list[ImportFile]
    interpreter: typing_extensions.Literal["UNKNOWN_INTERPRETER", "PYTHON", "JINJA"]
    mainTemplate: str
    schema: str
    template: str

@typing.type_check_only
class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    base: BaseType
    description: str
    id: str
    insertTime: str
    labels: _list[TypeLabelEntry]
    name: str
    operation: Operation
    selfLink: str

@typing.type_check_only
class TypeInfo(typing_extensions.TypedDict, total=False):
    description: str
    documentationLink: str
    kind: str
    name: str
    schema: TypeInfoSchemaInfo
    selfLink: str
    title: str

@typing.type_check_only
class TypeInfoSchemaInfo(typing_extensions.TypedDict, total=False):
    input: str
    output: str

@typing.type_check_only
class TypeLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class TypeProvider(typing_extensions.TypedDict, total=False):
    collectionOverrides: _list[CollectionOverride]
    credential: Credential
    customCertificateAuthorityRoots: _list[str]
    description: str
    descriptorUrl: str
    id: str
    insertTime: str
    labels: _list[TypeProviderLabelEntry]
    name: str
    operation: Operation
    options: Options
    selfLink: str

@typing.type_check_only
class TypeProviderLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class TypeProvidersListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    typeProviders: _list[TypeProvider]

@typing.type_check_only
class TypeProvidersListTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: _list[TypeInfo]

@typing.type_check_only
class TypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: _list[Type]

@typing.type_check_only
class ValidationOptions(typing_extensions.TypedDict, total=False):
    schemaValidation: typing_extensions.Literal[
        "UNKNOWN", "IGNORE", "IGNORE_WITH_WARNINGS", "FAIL"
    ]
    undeclaredProperties: typing_extensions.Literal[
        "UNKNOWN",
        "INCLUDE",
        "IGNORE",
        "INCLUDE_WITH_WARNINGS",
        "IGNORE_WITH_WARNINGS",
        "FAIL",
    ]
