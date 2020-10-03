import typing

import typing_extensions

class CompositeTypeLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class TypeProviderLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    manifests: typing.List[Manifest]

class DeploymentUpdate(typing_extensions.TypedDict, total=False):
    manifest: str
    description: str
    labels: typing.List[DeploymentUpdateLabelEntry]

class TargetConfiguration(typing_extensions.TypedDict, total=False):
    imports: typing.List[ImportFile]
    config: ConfigFile

class BaseType(typing_extensions.TypedDict, total=False):
    options: Options
    credential: Credential
    collectionOverrides: typing.List[CollectionOverride]
    descriptorUrl: str

class LogConfigCounterOptionsCustomField(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class DeploymentsListResponse(typing_extensions.TypedDict, total=False):
    deployments: typing.List[Deployment]
    nextPageToken: str

class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: str

class ConfigFile(typing_extensions.TypedDict, total=False):
    content: str

class TypeInfo(typing_extensions.TypedDict, total=False):
    schema: TypeInfoSchemaInfo
    description: str
    documentationLink: str
    kind: str
    title: str
    selfLink: str
    name: str

class OperationsListResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    bindings: typing.List[Binding]
    version: int
    iamOwned: bool
    rules: typing.List[Rule]
    auditConfigs: typing.List[AuditConfig]

class TemplateContents(typing_extensions.TypedDict, total=False):
    schema: str
    imports: typing.List[ImportFile]
    interpreter: str
    mainTemplate: str
    template: str

class DeploymentLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class DeploymentsStopRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class InputMapping(typing_extensions.TypedDict, total=False):
    methodMatch: str
    location: str
    fieldName: str
    value: str

class LogConfigDataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: str

class Resource(typing_extensions.TypedDict, total=False):
    name: str
    finalProperties: str
    type: str
    insertTime: str
    accessControl: ResourceAccessControl
    id: str
    properties: str
    manifest: str
    updateTime: str
    url: str
    update: ResourceUpdate
    warnings: typing.List[typing.Dict[str, typing.Any]]

class TypeProvidersListTypesResponse(typing_extensions.TypedDict, total=False):
    types: typing.List[TypeInfo]
    nextPageToken: str

class CompositeType(typing_extensions.TypedDict, total=False):
    status: str
    operation: Operation
    templateContents: TemplateContents
    id: str
    name: str
    description: str
    selfLink: str
    insertTime: str
    labels: typing.List[CompositeTypeLabelEntry]

class Condition(typing_extensions.TypedDict, total=False):
    svc: str
    sys: str
    values: typing.List[str]
    op: str
    iam: str

class LogConfigCounterOptions(typing_extensions.TypedDict, total=False):
    field: str
    customFields: typing.List[LogConfigCounterOptionsCustomField]
    metric: str

class Rule(typing_extensions.TypedDict, total=False):
    conditions: typing.List[Condition]
    notIns: typing.List[str]
    logConfigs: typing.List[LogConfig]
    action: str
    description: str
    ins: typing.List[str]
    permissions: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    targetId: str
    description: str
    name: str
    targetLink: str
    kind: str
    selfLink: str
    insertTime: str
    user: str
    operationType: str
    httpErrorStatusCode: int
    statusMessage: str
    endTime: str
    httpErrorMessage: str
    clientOperationId: str
    zone: str
    error: typing.Dict[str, typing.Any]
    status: str
    startTime: str
    progress: int
    id: str
    region: str

class CompositeTypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    compositeTypes: typing.List[CompositeType]

class Diagnostic(typing_extensions.TypedDict, total=False):
    level: str
    field: str

class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Deployment(typing_extensions.TypedDict, total=False):
    selfLink: str
    id: str
    labels: typing.List[DeploymentLabelEntry]
    name: str
    fingerprint: str
    manifest: str
    update: DeploymentUpdate
    updateTime: str
    insertTime: str
    target: TargetConfiguration
    description: str
    operation: Operation

class BasicAuth(typing_extensions.TypedDict, total=False):
    password: str
    user: str

class Manifest(typing_extensions.TypedDict, total=False):
    imports: typing.List[ImportFile]
    insertTime: str
    expandedConfig: str
    id: str
    layout: str
    selfLink: str
    config: ConfigFile
    name: str

class Credential(typing_extensions.TypedDict, total=False):
    basicAuth: BasicAuth
    serviceAccount: ServiceAccount
    useProjectDefault: bool

class ValidationOptions(typing_extensions.TypedDict, total=False):
    undeclaredProperties: str
    schemaValidation: str

class Type(typing_extensions.TypedDict, total=False):
    base: BaseType
    id: str
    labels: typing.List[TypeLabelEntry]
    selfLink: str
    description: str
    name: str
    operation: Operation
    insertTime: str

class TypeProvidersListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    typeProviders: typing.List[TypeProvider]

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

class TypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: typing.List[Type]

class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Resource]

class TypeProvider(typing_extensions.TypedDict, total=False):
    description: str
    credential: Credential
    insertTime: str
    id: str
    labels: typing.List[TypeProviderLabelEntry]
    operation: Operation
    customCertificateAuthorityRoots: typing.List[str]
    collectionOverrides: typing.List[CollectionOverride]
    name: str
    selfLink: str
    options: Options
    descriptorUrl: str

class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

class LogConfig(typing_extensions.TypedDict, total=False):
    cloudAudit: LogConfigCloudAuditOptions
    counter: LogConfigCounterOptions
    dataAccess: LogConfigDataAccessOptions

class AsyncOptions(typing_extensions.TypedDict, total=False):
    pollingOptions: PollingOptions
    methodMatch: str

class ImportFile(typing_extensions.TypedDict, total=False):
    content: str
    name: str

class PollingOptions(typing_extensions.TypedDict, total=False):
    finishCondition: str
    targetLink: str
    pollingLink: str
    failCondition: str
    diagnostics: typing.List[Diagnostic]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    ignoreChildExemptions: bool
    logType: str
    exemptedMembers: typing.List[str]

class TypeLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class DeploymentsCancelPreviewRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    bindings: typing.List[Binding]
    etag: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    exemptedMembers: typing.List[str]
    service: str

class ResourceUpdate(typing_extensions.TypedDict, total=False):
    state: str
    intent: str
    manifest: str
    finalProperties: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    properties: str
    accessControl: ResourceAccessControl
    error: typing.Dict[str, typing.Any]

class LogConfigCloudAuditOptions(typing_extensions.TypedDict, total=False):
    authorizationLoggingOptions: AuthorizationLoggingOptions
    logName: str

class DeploymentUpdateLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class TypeInfoSchemaInfo(typing_extensions.TypedDict, total=False):
    input: str
    output: str

class Options(typing_extensions.TypedDict, total=False):
    validationOptions: ValidationOptions
    inputMappings: typing.List[InputMapping]
    asyncOptions: typing.List[AsyncOptions]
    virtualProperties: str

class CollectionOverride(typing_extensions.TypedDict, total=False):
    options: Options
    collection: str

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str
