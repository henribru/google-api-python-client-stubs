import typing

import typing_extensions

class Deployment(typing_extensions.TypedDict, total=False):
    credential: Credential
    fingerprint: str
    labels: typing.List[DeploymentLabelEntry]
    selfLink: str
    outputs: typing.List[DeploymentOutputEntry]
    updateTime: str
    target: TargetConfiguration
    insertTime: str
    id: str
    name: str
    description: str
    manifest: str
    update: DeploymentUpdate
    operation: Operation

class ConfigurableService(typing_extensions.TypedDict, total=False):
    collectionOverrides: typing.List[CollectionOverride]
    credential: Credential
    descriptorUrl: str
    options: Options

class MethodMap(typing_extensions.TypedDict, total=False):
    setIamPolicy: str
    delete: str
    get: str
    update: str
    create: str

class Options(typing_extensions.TypedDict, total=False):
    validationOptions: ValidationOptions
    inputMappings: typing.List[InputMapping]
    asyncOptions: typing.List[AsyncOptions]
    nameProperty: str

class DeploymentsStopRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class DeploymentUpdate(typing_extensions.TypedDict, total=False):
    description: str
    credential: Credential
    manifest: str
    labels: typing.List[DeploymentUpdateLabelEntry]

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    exemptedMembers: typing.List[str]
    auditLogConfigs: typing.List[AuditLogConfig]

class ImportFile(typing_extensions.TypedDict, total=False):
    name: str
    content: str

class Rule(typing_extensions.TypedDict, total=False):
    notIns: typing.List[str]
    ins: typing.List[str]
    conditions: typing.List[Condition]
    permissions: typing.List[str]
    logConfigs: typing.List[LogConfig]
    action: str
    description: str

class TypeLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class AsyncOptions(typing_extensions.TypedDict, total=False):
    pollingOptions: PollingOptions
    methodMatch: str

class CollectionOverride(typing_extensions.TypedDict, total=False):
    collection: str
    methodMap: MethodMap
    options: Options

class TypesListResponse(typing_extensions.TypedDict, total=False):
    types: typing.List[Type]
    nextPageToken: str

class ResourceUpdate(typing_extensions.TypedDict, total=False):
    warnings: typing.List[typing.Dict[str, typing.Any]]
    state: str
    accessControl: ResourceAccessControl
    runtimePolicies: typing.List[str]
    properties: str
    manifest: str
    intent: str
    error: typing.Dict[str, typing.Any]
    finalProperties: str
    credential: Credential

class CompositeTypeLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class TypeProviderLabelEntry(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class Manifest(typing_extensions.TypedDict, total=False):
    name: str
    selfLink: str
    layout: str
    expandedConfig: str
    config: ConfigFile
    insertTime: str
    imports: typing.List[ImportFile]
    id: str

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    rules: typing.List[Rule]
    iamOwned: bool
    version: int
    etag: str
    auditConfigs: typing.List[AuditConfig]

class DeploymentUpdateLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class TemplateContents(typing_extensions.TypedDict, total=False):
    schema: str
    imports: typing.List[ImportFile]
    mainTemplate: str
    interpreter: str
    template: str

class TypeInfo(typing_extensions.TypedDict, total=False):
    description: str
    kind: str
    documentationLink: str
    selfLink: str
    schema: TypeInfoSchemaInfo
    title: str
    name: str

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class Condition(typing_extensions.TypedDict, total=False):
    sys: str
    values: typing.List[str]
    op: str
    svc: str
    iam: str

class Type(typing_extensions.TypedDict, total=False):
    selfLink: str
    configurableService: ConfigurableService
    labels: typing.List[TypeLabelEntry]
    name: str
    insertTime: str
    description: str
    operation: Operation
    id: str

class CompositeType(typing_extensions.TypedDict, total=False):
    selfLink: str
    labels: typing.List[CompositeTypeLabelEntry]
    templateContents: TemplateContents
    description: str
    name: str
    status: str
    id: str
    insertTime: str
    operation: Operation

class OperationsListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class LogConfigCloudAuditOptions(typing_extensions.TypedDict, total=False):
    logName: str
    authorizationLoggingOptions: AuthorizationLoggingOptions

class TypeInfoSchemaInfo(typing_extensions.TypedDict, total=False):
    input: str
    output: str

class TypeProvidersListTypesResponse(typing_extensions.TypedDict, total=False):
    types: typing.List[TypeInfo]
    nextPageToken: str

class TestPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ValidationOptions(typing_extensions.TypedDict, total=False):
    undeclaredProperties: str
    schemaValidation: str

class Credential(typing_extensions.TypedDict, total=False):
    useProjectDefault: bool
    serviceAccount: ServiceAccount
    basicAuth: BasicAuth

class GlobalSetPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    etag: str
    bindings: typing.List[Binding]

class DeploymentLabelEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class InputMapping(typing_extensions.TypedDict, total=False):
    location: str
    value: str
    methodMatch: str
    fieldName: str

class Operation(typing_extensions.TypedDict, total=False):
    selfLink: str
    error: typing.Dict[str, typing.Any]
    zone: str
    kind: str
    targetId: str
    id: str
    user: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    region: str
    insertTime: str
    endTime: str
    name: str
    selfLinkWithId: str
    description: str
    creationTimestamp: str
    targetLink: str
    clientOperationId: str
    httpErrorStatusCode: int
    progress: int
    statusMessage: str
    startTime: str
    status: str
    httpErrorMessage: str
    operationType: str

class Diagnostic(typing_extensions.TypedDict, total=False):
    field: str
    level: str

class LogConfigCounterOptionsCustomField(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class TypeProvider(typing_extensions.TypedDict, total=False):
    collectionOverrides: typing.List[CollectionOverride]
    labels: typing.List[TypeProviderLabelEntry]
    insertTime: str
    descriptorUrl: str
    selfLink: str
    name: str
    description: str
    operation: Operation
    credential: Credential
    customCertificateAuthorityRoots: typing.List[str]
    id: str
    options: Options

class ResourcesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    resources: typing.List[Resource]

class DeploymentsCancelPreviewRequest(typing_extensions.TypedDict, total=False):
    fingerprint: str

class DeploymentsListResponse(typing_extensions.TypedDict, total=False):
    deployments: typing.List[Deployment]
    nextPageToken: str

class ServiceAccount(typing_extensions.TypedDict, total=False):
    email: str

class AuthorizationLoggingOptions(typing_extensions.TypedDict, total=False):
    permissionType: str

class ConfigFile(typing_extensions.TypedDict, total=False):
    content: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: str
    exemptedMembers: typing.List[str]
    ignoreChildExemptions: bool

class CompositeTypesListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    compositeTypes: typing.List[CompositeType]

class DeploymentOutputEntry(typing_extensions.TypedDict, total=False):
    value: str
    key: str

class LogConfig(typing_extensions.TypedDict, total=False):
    counter: LogConfigCounterOptions
    dataAccess: LogConfigDataAccessOptions
    cloudAudit: LogConfigCloudAuditOptions

class PollingOptions(typing_extensions.TypedDict, total=False):
    failCondition: str
    finishCondition: str
    pollingLink: str
    targetLink: str
    diagnostics: typing.List[Diagnostic]

class TypeProvidersListResponse(typing_extensions.TypedDict, total=False):
    typeProviders: typing.List[TypeProvider]
    nextPageToken: str

class LogConfigCounterOptions(typing_extensions.TypedDict, total=False):
    customFields: typing.List[LogConfigCounterOptionsCustomField]
    field: str
    metric: str

class ResourceAccessControl(typing_extensions.TypedDict, total=False):
    gcpIamPolicy: str

class TestPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class TargetConfiguration(typing_extensions.TypedDict, total=False):
    config: ConfigFile
    imports: typing.List[ImportFile]

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

class ManifestsListResponse(typing_extensions.TypedDict, total=False):
    manifests: typing.List[Manifest]
    nextPageToken: str

class LogConfigDataAccessOptions(typing_extensions.TypedDict, total=False):
    logMode: str

class BasicAuth(typing_extensions.TypedDict, total=False):
    user: str
    password: str

class Resource(typing_extensions.TypedDict, total=False):
    type: str
    runtimePolicies: typing.List[str]
    finalProperties: str
    insertTime: str
    properties: str
    warnings: typing.List[typing.Dict[str, typing.Any]]
    manifest: str
    id: str
    updateTime: str
    lastUsedCredential: Credential
    name: str
    update: ResourceUpdate
    url: str
    accessControl: ResourceAccessControl
