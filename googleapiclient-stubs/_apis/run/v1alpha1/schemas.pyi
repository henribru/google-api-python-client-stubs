import typing

import typing_extensions
@typing.type_check_only
class Addressable(typing_extensions.TypedDict, total=False):
    hostname: str
    url: str

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
class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class Capabilities(typing_extensions.TypedDict, total=False):
    add: typing.List[str]
    drop: typing.List[str]

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
    items: typing.List[KeyToPath]
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
class ConfigurationCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class ConfigurationSpec(typing_extensions.TypedDict, total=False):
    generation: int
    revisionTemplate: RevisionTemplate
    template: RevisionTemplate

@typing.type_check_only
class ConfigurationStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[ConfigurationCondition]
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int

@typing.type_check_only
class Container(typing_extensions.TypedDict, total=False):
    args: typing.List[str]
    command: typing.List[str]
    env: typing.List[EnvVar]
    envFrom: typing.List[EnvFromSource]
    image: str
    imagePullPolicy: str
    lifecycle: Lifecycle
    livenessProbe: Probe
    name: str
    ports: typing.List[ContainerPort]
    readinessProbe: Probe
    resources: ResourceRequirements
    securityContext: SecurityContext
    stdin: bool
    stdinOnce: bool
    terminationMessagePath: str
    terminationMessagePolicy: str
    tty: bool
    volumeDevices: typing.List[VolumeDevice]
    volumeMounts: typing.List[VolumeMount]
    workingDir: str

@typing.type_check_only
class ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    hostIP: str
    hostPort: int
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
class DomainMappingCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class DomainMappingSpec(typing_extensions.TypedDict, total=False):
    certificateMode: typing_extensions.Literal[
        "CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    forceOverride: bool
    routeName: str

@typing.type_check_only
class DomainMappingStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[DomainMappingCondition]
    mappedRouteName: str
    observedGeneration: int
    resourceRecords: typing.List[ResourceRecord]
    url: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

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
    command: typing.List[str]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: typing.List[HTTPHeader]
    path: str
    port: IntOrString
    scheme: str

@typing.type_check_only
class HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class Handler(typing_extensions.TypedDict, total=False):
    exec: ExecAction
    httpGet: HTTPGetAction
    tcpSocket: TCPSocketAction

@typing.type_check_only
class InstanceSpec(typing_extensions.TypedDict, total=False):
    activeDeadlineSeconds: str
    containers: typing.List[Container]
    restartPolicy: str
    serviceAccountName: str
    terminationGracePeriodSeconds: str
    volumes: typing.List[Volume]

@typing.type_check_only
class InstanceStatus(typing_extensions.TypedDict, total=False):
    completionTime: str
    failed: int
    index: int
    lastExitCode: int
    restarted: int
    startTime: str
    succeeded: int

@typing.type_check_only
class InstanceTemplateSpec(typing_extensions.TypedDict, total=False):
    spec: InstanceSpec

@typing.type_check_only
class IntOrString(typing_extensions.TypedDict, total=False):
    intVal: int
    strVal: str
    type: int

@typing.type_check_only
class Job(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: JobSpec
    status: JobStatus

@typing.type_check_only
class JobCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class JobSpec(typing_extensions.TypedDict, total=False):
    activeDeadlineSeconds: str
    backoffLimit: int
    completions: int
    parallelism: int
    template: InstanceTemplateSpec
    ttlSecondsAfterFinished: int

@typing.type_check_only
class JobStatus(typing_extensions.TypedDict, total=False):
    active: int
    completionTime: str
    conditions: typing.List[JobCondition]
    failed: int
    imageDigest: str
    instances: typing.List[InstanceStatus]
    observedGeneration: int
    startTime: str
    succeeded: int

@typing.type_check_only
class KeyToPath(typing_extensions.TypedDict, total=False):
    key: str
    mode: int
    path: str

@typing.type_check_only
class Lifecycle(typing_extensions.TypedDict, total=False):
    postStart: Handler
    preStop: Handler

@typing.type_check_only
class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: typing.List[AuthorizedDomain]
    nextPageToken: str

@typing.type_check_only
class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[Configuration]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

@typing.type_check_only
class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[DomainMapping]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

@typing.type_check_only
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[Job]
    kind: str
    metadata: ListMeta
    nextPageToken: str
    unreachable: typing.List[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
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
    items: typing.List[Revision]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

@typing.type_check_only
class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[Route]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

@typing.type_check_only
class ListServicesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[Service]
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]

@typing.type_check_only
class LocalObjectReference(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class ObjectMeta(typing_extensions.TypedDict, total=False):
    annotations: typing.Dict[str, typing.Any]
    clusterName: str
    creationTimestamp: str
    deletionGracePeriodSeconds: int
    deletionTimestamp: str
    finalizers: typing.List[str]
    generateName: str
    generation: int
    labels: typing.Dict[str, typing.Any]
    name: str
    namespace: str
    ownerReferences: typing.List[OwnerReference]
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
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class Probe(typing_extensions.TypedDict, total=False):
    failureThreshold: int
    handler: Handler
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    timeoutSeconds: int

@typing.type_check_only
class Quantity(typing_extensions.TypedDict, total=False):
    string: str

@typing.type_check_only
class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    rrdata: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]

@typing.type_check_only
class ResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: typing.Dict[str, typing.Any]
    limitsInMap: typing.Dict[str, typing.Any]
    requests: typing.Dict[str, typing.Any]
    requestsInMap: typing.Dict[str, typing.Any]

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: RevisionSpec
    status: RevisionStatus

@typing.type_check_only
class RevisionCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class RevisionSpec(typing_extensions.TypedDict, total=False):
    concurrencyModel: str
    container: Container
    containerConcurrency: int
    containers: typing.List[Container]
    generation: int
    serviceAccountName: str
    servingState: typing_extensions.Literal[
        "REVISION_SERVING_STATE_UNSPECIFIED", "ACTIVE", "RESERVE", "RETIRED"
    ]
    timeoutSeconds: int
    volumes: typing.List[Volume]

@typing.type_check_only
class RevisionStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[RevisionCondition]
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
class RouteCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class RouteSpec(typing_extensions.TypedDict, total=False):
    generation: int
    traffic: typing.List[TrafficTarget]

@typing.type_check_only
class RouteStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: typing.List[RouteCondition]
    domain: str
    domainInternal: str
    observedGeneration: int
    traffic: typing.List[TrafficTarget]
    url: str

@typing.type_check_only
class SELinuxOptions(typing_extensions.TypedDict, total=False):
    level: str
    role: str
    type: str
    user: str

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
    items: typing.List[KeyToPath]
    optional: bool
    secretName: str

@typing.type_check_only
class SecurityContext(typing_extensions.TypedDict, total=False):
    allowPrivilegeEscalation: bool
    capabilities: Capabilities
    privileged: bool
    readOnlyRootFilesystem: bool
    runAsGroup: int
    runAsNonRoot: bool
    runAsUser: int
    seLinuxOptions: SELinuxOptions

@typing.type_check_only
class Service(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus

@typing.type_check_only
class ServiceCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class ServiceSpec(typing_extensions.TypedDict, total=False):
    generation: int
    manual: ServiceSpecManualType
    pinned: ServiceSpecPinnedType
    release: ServiceSpecReleaseType
    runLatest: ServiceSpecRunLatest
    template: RevisionTemplate
    traffic: typing.List[TrafficTarget]

@typing.type_check_only
class ServiceSpecManualType(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ServiceSpecPinnedType(typing_extensions.TypedDict, total=False):
    configuration: ConfigurationSpec
    revisionName: str

@typing.type_check_only
class ServiceSpecReleaseType(typing_extensions.TypedDict, total=False):
    configuration: ConfigurationSpec
    revisions: typing.List[str]
    rolloutPercent: int

@typing.type_check_only
class ServiceSpecRunLatest(typing_extensions.TypedDict, total=False):
    configuration: ConfigurationSpec

@typing.type_check_only
class ServiceStatus(typing_extensions.TypedDict, total=False):
    address: Addressable
    conditions: typing.List[ServiceCondition]
    domain: str
    latestCreatedRevisionName: str
    latestReadyRevisionName: str
    observedGeneration: int
    traffic: typing.List[TrafficTarget]
    url: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
    port: IntOrString

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TrafficTarget(typing_extensions.TypedDict, total=False):
    configurationName: str
    latestRevision: bool
    name: str
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
class VolumeDevice(typing_extensions.TypedDict, total=False):
    devicePath: str
    name: str

@typing.type_check_only
class VolumeMount(typing_extensions.TypedDict, total=False):
    mountPath: str
    mountPropagation: str
    name: str
    readOnly: bool
    subPath: str
