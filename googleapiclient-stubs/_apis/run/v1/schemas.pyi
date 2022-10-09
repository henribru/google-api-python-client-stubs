import typing

import typing_extensions

_list = list

@typing.type_check_only
class Addressable(typing_extensions.TypedDict, total=False):
    url: str

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
class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class CancelExecutionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConfigMapEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapKeySelector(typing_extensions.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapVolumeSource(typing_extensions.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    name: str
    optional: bool

@typing.type_check_only
class Configuration(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ConfigurationSpec
    status: ConfigurationStatus

@typing.type_check_only
class ConfigurationSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate

@typing.type_check_only
class ConfigurationStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    args: _list[str]
    command: _list[str]
    env: _list[EnvVar]
    envFrom: _list[EnvFromSource]
    image: str
    imagePullPolicy: str
    livenessProbe: Probe
    name: str
    ports: _list[ContainerPort]
    readinessProbe: Probe
    resources: ResourceRequirements
    securityContext: SecurityContext
    startupProbe: Probe
    terminationMessagePath: str
    terminationMessagePolicy: str
    volumeMounts: _list[VolumeMount]
    workingDir: str

@typing.type_check_only
class ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    name: str
    protocol: str

@typing.type_check_only
class DomainMapping(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: DomainMappingSpec
    status: DomainMappingStatus

@typing.type_check_only
class DomainMappingSpec(typing_extensions.TypedDict, total=False):
    certificateMode: typing_extensions.Literal[
        "CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    forceOverride: bool
    routeName: str

@typing.type_check_only
class DomainMappingStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    mappedRouteName: str
    observedGeneration: int
    resourceRecords: _list[ResourceRecord]
    url: str

@typing.type_check_only
class EnvFromSource(typing_extensions.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    prefix: str
    secretRef: SecretEnvSource

@typing.type_check_only
class EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    valueFrom: EnvVarSource

@typing.type_check_only
class EnvVarSource(typing_extensions.TypedDict, total=False):
    configMapKeyRef: ConfigMapKeySelector
    secretKeyRef: SecretKeySelector

@typing.type_check_only
class ExecAction(typing_extensions.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class Execution(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ExecutionSpec
    status: ExecutionStatus

@typing.type_check_only
class ExecutionReference(typing_extensions.TypedDict, total=False):
    completionTimestamp: str
    creationTimestamp: str
    name: str

@typing.type_check_only
class ExecutionSpec(typing_extensions.TypedDict, total=False):
    parallelism: int
    taskCount: int
    template: TaskTemplateSpec

@typing.type_check_only
class ExecutionStatus(typing_extensions.TypedDict, total=False):
    cancelledCount: int
    completionTime: str
    conditions: _list[GoogleCloudRunV1Condition]
    failedCount: int
    logUri: str
    observedGeneration: int
    retriedCount: int
    runningCount: int
    startTime: str
    succeededCount: int

@typing.type_check_only
class ExecutionTemplateSpec(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: ExecutionSpec

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GRPCAction(typing_extensions.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleCloudRunV1Condition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: _list[HTTPHeader]
    path: str
    scheme: str

@typing.type_check_only
class HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: JobSpec
    status: JobStatus

@typing.type_check_only
class JobSpec(typing_extensions.TypedDict, total=False):
    template: ExecutionTemplateSpec

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    executionCount: int
    latestCreatedExecution: ExecutionReference
    observedGeneration: int

@typing.type_check_only
class KeyToPath(typing_extensions.TypedDict, total=False):
    key: str
    mode: int
    path: str

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: _list[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Configuration]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[DomainMapping]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListExecutionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Execution]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Job]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

AlternativeListMeta = typing_extensions.TypedDict(
    "AlternativeListMeta",
    {
        "continue": str,
        "resourceVersion": str,
        "selfLink": str,
    },
    total=False,
)

@typing.type_check_only
class ListMeta(AlternativeListMeta): ...

@typing.type_check_only
class ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Revision]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Route]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Service]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class ListTasksResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: _list[Task]
    kind: str
    metadata: ListMeta
    unreachable: _list[str]

@typing.type_check_only
class LocalObjectReference(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ObjectMeta(typing_extensions.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: _list[str]
    generateName: str
    generation: int
    labels: dict[str, typing.Any]
    name: str
    namespace: str
    ownerReferences: _list[OwnerReference]
    resourceVersion: str
    selfLink: str
    uid: str

@typing.type_check_only
class OwnerReference(typing_extensions.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Probe(typing_extensions.TypedDict, total=False):
    exec: ExecAction
    failureThreshold: int
    grpc: GRPCAction
    httpGet: HTTPGetAction
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: TCPSocketAction
    timeoutSeconds: int

@typing.type_check_only
class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

@typing.type_check_only
class ResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RevisionSpec
    status: RevisionStatus

@typing.type_check_only
class RevisionSpec(typing_extensions.TypedDict, total=False):
    containerConcurrency: int
    containers: _list[Container]
    enableServiceLinks: bool
    imagePullSecrets: _list[LocalObjectReference]
    serviceAccountName: str
    timeoutSeconds: int
    volumes: _list[Volume]

@typing.type_check_only
class RevisionStatus(typing_extensions.TypedDict, total=False):
    conditions: _list[GoogleCloudRunV1Condition]
    imageDigest: str
    logUrl: str
    observedGeneration: int
    serviceName: str

@typing.type_check_only
class RevisionTemplate(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: RevisionSpec

@typing.type_check_only
class Route(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RouteSpec
    status: RouteStatus

@typing.type_check_only
class RouteSpec(typing_extensions.TypedDict, total=False):
    traffic: _list[TrafficTarget]

@typing.type_check_only
class RouteStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class RunJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SecretEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretKeySelector(typing_extensions.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretVolumeSource(typing_extensions.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    optional: bool
    secretName: str

@typing.type_check_only
class SecurityContext(typing_extensions.TypedDict, total=False):
    runAsUser: int

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus

@typing.type_check_only
class ServiceSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate
    traffic: _list[TrafficTarget]

@typing.type_check_only
class ServiceStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: _list[GoogleCloudRunV1Condition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int
    traffic: _list[TrafficTarget]
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: StatusDetails
    message: str
    metadata: ListMeta
    reason: str
    status: str

@typing.type_check_only
class StatusCause(typing_extensions.TypedDict, total=False):
    field: str
    message: str
    reason: str

@typing.type_check_only
class StatusDetails(typing_extensions.TypedDict, total=False):
    causes: _list[StatusCause]
    group: str
    kind: str
    name: str
    retryAfterSeconds: int
    uid: str

@typing.type_check_only
class TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class Task(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: TaskSpec
    status: TaskStatus

@typing.type_check_only
class TaskAttemptResult(typing_extensions.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus

@typing.type_check_only
class TaskSpec(typing_extensions.TypedDict, total=False):
    containers: _list[Container]
    maxRetries: int
    serviceAccountName: str
    timeoutSeconds: str
    volumes: _list[Volume]

@typing.type_check_only
class TaskStatus(typing_extensions.TypedDict, total=False):
    completionTime: str
    conditions: _list[GoogleCloudRunV1Condition]
    index: int
    lastAttemptResult: TaskAttemptResult
    logUri: str
    observedGeneration: int
    retried: int
    startTime: str

@typing.type_check_only
class TaskTemplateSpec(typing_extensions.TypedDict, total=False):
    spec: TaskSpec

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TrafficTarget(typing_extensions.TypedDict, total=False):
    configurationName: str
    latestRevision: bool
    percent: int
    revisionName: str
    tag: str
    url: str

@typing.type_check_only
class Volume(typing_extensions.TypedDict, total=False):
    configMap: ConfigMapVolumeSource
    name: str
    secret: SecretVolumeSource

@typing.type_check_only
class VolumeMount(typing_extensions.TypedDict, total=False):
    mountPath: str
    name: str
    readOnly: bool
    subPath: str
