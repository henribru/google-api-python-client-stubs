import typing

import typing_extensions
@typing.type_check_only
class AsyncOptions(typing_extensions.TypedDict, total=False):
    methodMatch: str
    pollingOptions: PollingOptions

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BaseType(typing_extensions.TypedDict, total=False):
    collectionOverrides: typing.List[CollectionOverride]
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
    members: typing.List[str]
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
    labels: typing.List[CompositeTypeLabelEntry]
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
    compositeTypes: typing.List[CompositeType]
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
    labels: typing.List[DeploymentLabelEntry]
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
    labels: typing.List[DeploymentUpdateLabelEntry]
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
    deployments: typing.List[Deployment]
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
    bindings: typing.List[Binding]
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
    imports: typing.List[ImportFile]
    insertTime: str
    layout: str
    manifestSizeBytes: str
    manifestSizeLimitBytes: str
    name: str
    selfLink: str

@typing.type_check_only
class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    manifests: typing.List[Manifest]
    nextPageToken: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    clientOperationId: str
    creationTimestamp: str
    description: str
    endTime: str
    error: typing.Dict[str, typing.Any]
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
    warnings: typing.List[typing.Dict[str, typing.Any]]
    zone: str

@typing.type_check_only
class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    asyncOptions: typing.List[AsyncOptions]
    inputMappings: typing.List[InputMapping]
    validationOptions: ValidationOptions
    virtualProperties: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class PollingOptions(typing_extensions.TypedDict, total=False):
    diagnostics: typing.List[Diagnostic]
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
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

@typing.type_check_only
class ResourceUpdate(typing_extensions.TypedDict, total=False):
    accessControl: ResourceAccessControl
    error: typing.Dict[str, typing.Any]
    finalProperties: str
    intent: typing_extensions.Literal[
        "CREATE_OR_ACQUIRE", "DELETE", "ACQUIRE", "UPDATE", "ABANDON", "CREATE"
    ]
    manifest: str
    properties: str
    state: typing_extensions.Literal[
        "PENDING", "IN_PROGRESS", "IN_PREVIEW", "FAILED", "ABORTED"
    ]
    warnings: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Resource]

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class TargetConfiguration(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    imports: typing.List[ImportFile]

@typing.type_check_only
class TemplateContents(typing_extensions.TypedDict, total=False):
    imports: typing.List[ImportFile]
    interpreter: typing_extensions.Literal["UNKNOWN_INTERPRETER", "PYTHON", "JINJA"]
    mainTemplate: str
    schema: str
    template: str

@typing.type_check_only
class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    base: BaseType
    description: str
    id: str
    insertTime: str
    labels: typing.List[TypeLabelEntry]
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
    collectionOverrides: typing.List[CollectionOverride]
    credential: Credential
    customCertificateAuthorityRoots: typing.List[str]
    description: str
    descriptorUrl: str
    id: str
    insertTime: str
    labels: typing.List[TypeProviderLabelEntry]
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
    typeProviders: typing.List[TypeProvider]

@typing.type_check_only
class TypeProvidersListTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: typing.List[TypeInfo]

@typing.type_check_only
class TypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: typing.List[Type]

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
