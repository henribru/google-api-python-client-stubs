import typing

import typing_extensions

class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Configuration]
    unreachable: typing.List[str]
    metadata: ListMeta
    apiVersion: str

class ServiceSpecRunLatest(typing_extensions.TypedDict, total=False):
    configuration: ConfigurationSpec

class ListCloudSchedulerSourcesResponse(typing_extensions.TypedDict, total=False):
    metadata: ListMeta
    apiVersion: str
    kind: str
    unreachable: typing.List[str]
    items: typing.List[CloudSchedulerSource]

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    metadata: ListMeta
    items: typing.List[Service]
    apiVersion: str
    kind: str
    unreachable: typing.List[str]

class ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    hostIP: str
    name: str
    hostPort: int
    protocol: str

class TriggerCondition(typing_extensions.TypedDict, total=False):
    type: str
    lastTransitionTime: str
    status: str
    reason: str
    message: str
    severity: str

class Handler(typing_extensions.TypedDict, total=False):
    tcpSocket: TCPSocketAction
    httpGet: HTTPGetAction
    exec: ExecAction

class RevisionSpec(typing_extensions.TypedDict, total=False):
    container: Container
    concurrencyModel: str
    volumes: typing.List[Volume]
    timeoutSeconds: int
    containers: typing.List[Container]
    generation: int
    servingState: typing_extensions.Literal[
        "REVISION_SERVING_STATE_UNSPECIFIED", "ACTIVE", "RESERVE", "RETIRED"
    ]
    serviceAccountName: str
    containerConcurrency: int

class OwnerReference(typing_extensions.TypedDict, total=False):
    uid: str
    controller: bool
    blockOwnerDeletion: bool
    apiVersion: str
    kind: str
    name: str

class RevisionStatus(typing_extensions.TypedDict, total=False):
    serviceName: str
    imageDigest: str
    observedGeneration: int
    conditions: typing.List[RevisionCondition]
    logUrl: str

class Destination(typing_extensions.TypedDict, total=False):
    uri: str
    ref: ObjectReference

class CloudStorageSourceStatus(typing_extensions.TypedDict, total=False):
    sinkUri: str
    conditions: typing.List[Condition]
    observedGeneration: int

class Revision(typing_extensions.TypedDict, total=False):
    kind: str
    apiVersion: str
    metadata: ObjectMeta
    status: RevisionStatus
    spec: RevisionSpec

class Empty(typing_extensions.TypedDict, total=False): ...

class ServiceStatus(typing_extensions.TypedDict, total=False):
    latestReadyRevisionName: str
    latestCreatedRevisionName: str
    domain: str
    traffic: typing.List[TrafficTarget]
    url: str
    conditions: typing.List[ServiceCondition]
    observedGeneration: int
    address: Addressable

class ConfigMapEnvSource(typing_extensions.TypedDict, total=False):
    optional: bool
    localObjectReference: LocalObjectReference
    name: str

class TrafficTarget(typing_extensions.TypedDict, total=False):
    revisionName: str
    percent: int
    tag: str
    name: str
    url: str
    latestRevision: bool
    configurationName: str

class CloudSchedulerSourceSpec(typing_extensions.TypedDict, total=False):
    location: str
    ceOverrides: CloudEventOverrides
    project: str
    pubsubSecret: SecretKeySelector
    schedule: str
    data: str
    secret: SecretKeySelector
    sink: Destination

class ConfigMapKeySelector(typing_extensions.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]
    rrdata: str

class DomainMappingSpec(typing_extensions.TypedDict, total=False):
    certificateMode: typing_extensions.Literal[
        "CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    routeName: str
    forceOverride: bool

class Trigger(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    kind: str
    status: TriggerStatus
    spec: TriggerSpec
    apiVersion: str

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class SecurityContext(typing_extensions.TypedDict, total=False):
    allowPrivilegeEscalation: bool
    seLinuxOptions: SELinuxOptions
    runAsGroup: int
    privileged: bool
    capabilities: Capabilities
    runAsNonRoot: bool
    readOnlyRootFilesystem: bool
    runAsUser: int

class CloudSchedulerSourceStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[Condition]
    sinkUri: str
    observedGeneration: int

class ServiceSpecPinnedType(typing_extensions.TypedDict, total=False):
    revisionName: str
    configuration: ConfigurationSpec

class EnvVarSource(typing_extensions.TypedDict, total=False):
    secretKeyRef: SecretKeySelector
    configMapKeyRef: ConfigMapKeySelector

class ResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: typing.Dict[str, typing.Any]
    requests: typing.Dict[str, typing.Any]
    requestsInMap: typing.Dict[str, typing.Any]
    limitsInMap: typing.Dict[str, typing.Any]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    version: int
    bindings: typing.List[Binding]
    etag: str

class ServiceSpecManualType(typing_extensions.TypedDict, total=False): ...

class ObjectMeta(typing_extensions.TypedDict, total=False):
    creationTimestamp: str
    deletionTimestamp: str
    deletionGracePeriodSeconds: int
    annotations: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    finalizers: typing.List[str]
    clusterName: str
    generation: int
    selfLink: str
    uid: str
    resourceVersion: str
    namespace: str
    generateName: str
    name: str
    ownerReferences: typing.List[OwnerReference]

class HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class SecretVolumeSource(typing_extensions.TypedDict, total=False):
    secretName: str
    optional: bool
    defaultMode: int
    items: typing.List[KeyToPath]

class CloudPubSubSourceStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[Condition]
    observedGeneration: int
    sinkUri: str

class Route(typing_extensions.TypedDict, total=False):
    kind: str
    metadata: ObjectMeta
    apiVersion: str
    spec: RouteSpec
    status: RouteStatus

class DomainMappingStatus(typing_extensions.TypedDict, total=False):
    resourceRecords: typing.List[ResourceRecord]
    conditions: typing.List[DomainMappingCondition]
    mappedRouteName: str
    url: str
    observedGeneration: int

class RouteStatus(typing_extensions.TypedDict, total=False):
    observedGeneration: int
    domainInternal: str
    domain: str
    address: Addressable
    url: str
    conditions: typing.List[RouteCondition]
    traffic: typing.List[TrafficTarget]

class ConfigurationCondition(typing_extensions.TypedDict, total=False):
    severity: str
    status: str
    type: str
    reason: str
    lastTransitionTime: str
    message: str

class LocalObjectReference(typing_extensions.TypedDict, total=False):
    name: str

class CloudStorageSourceSpec(typing_extensions.TypedDict, total=False):
    serviceAccountName: str
    ceOverrides: CloudEventOverrides
    pubsubSecret: SecretKeySelector
    project: str
    eventTypes: typing.List[str]
    sink: Destination
    secret: SecretKeySelector
    objectNamePrefix: str
    payloadFormat: str
    bucket: str

class ConfigurationStatus(typing_extensions.TypedDict, total=False):
    observedGeneration: int
    latestReadyRevisionName: str
    conditions: typing.List[ConfigurationCondition]
    latestCreatedRevisionName: str

class ConfigMapVolumeSource(typing_extensions.TypedDict, total=False):
    name: str
    defaultMode: int
    items: typing.List[KeyToPath]
    optional: bool

class SecretKeySelector(typing_extensions.TypedDict, total=False):
    optional: bool
    name: str
    localObjectReference: LocalObjectReference
    key: str

class ServiceSpecReleaseType(typing_extensions.TypedDict, total=False):
    rolloutPercent: int
    revisions: typing.List[str]
    configuration: ConfigurationSpec

class ListCloudAuditLogsSourcesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    apiVersion: str
    kind: str
    metadata: ListMeta
    items: typing.List[CloudAuditLogsSource]

class TriggerSpec(typing_extensions.TypedDict, total=False):
    subscriber: Destination
    broker: str
    filter: TriggerFilter

class RouteCondition(typing_extensions.TypedDict, total=False):
    type: str
    status: str
    severity: str
    reason: str
    message: str
    lastTransitionTime: str

class Volume(typing_extensions.TypedDict, total=False):
    name: str
    configMap: ConfigMapVolumeSource
    secret: SecretVolumeSource

class ExecAction(typing_extensions.TypedDict, total=False):
    command: typing.List[str]

class CloudPubSubSource(typing_extensions.TypedDict, total=False):
    status: CloudPubSubSourceStatus
    kind: str
    apiVersion: str
    metadata: ObjectMeta
    spec: CloudPubSubSourceSpec

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class Capabilities(typing_extensions.TypedDict, total=False):
    add: typing.List[str]
    drop: typing.List[str]

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    domains: typing.List[AuthorizedDomain]

class VolumeMount(typing_extensions.TypedDict, total=False):
    name: str
    readOnly: bool
    subPath: str
    mountPropagation: str
    mountPath: str

class ServiceSpec(typing_extensions.TypedDict, total=False):
    pinned: ServiceSpecPinnedType
    release: ServiceSpecReleaseType
    runLatest: ServiceSpecRunLatest
    generation: int
    traffic: typing.List[TrafficTarget]
    manual: ServiceSpecManualType
    template: RevisionTemplate

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class CloudStorageSource(typing_extensions.TypedDict, total=False):
    status: CloudStorageSourceStatus
    apiVersion: str
    kind: str
    spec: CloudStorageSourceSpec
    metadata: ObjectMeta

class TriggerFilter(typing_extensions.TypedDict, total=False):
    attributes: typing.Dict[str, typing.Any]

class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    name: str
    id: str

class IntOrString(typing_extensions.TypedDict, total=False):
    type: int
    strVal: str
    intVal: int

class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[DomainMapping]
    unreachable: typing.List[str]
    kind: str
    metadata: ListMeta
    apiVersion: str

class Lifecycle(typing_extensions.TypedDict, total=False):
    postStart: Handler
    preStop: Handler

class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    unreachable: typing.List[str]
    items: typing.List[Route]
    kind: str
    metadata: ListMeta

class TriggerStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[TriggerCondition]
    subscriberUri: str
    observedGeneration: int

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str
    displayName: str
    labels: typing.Dict[str, typing.Any]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class RouteSpec(typing_extensions.TypedDict, total=False):
    traffic: typing.List[TrafficTarget]
    generation: int

class KeyToPath(typing_extensions.TypedDict, total=False):
    key: str
    mode: int
    path: str

class RevisionTemplate(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: RevisionSpec

class Quantity(typing_extensions.TypedDict, total=False):
    string: str

class ListTriggersResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    apiVersion: str
    items: typing.List[Trigger]
    kind: str
    metadata: ListMeta

class EnvVar(typing_extensions.TypedDict, total=False):
    name: str
    value: str
    valueFrom: EnvVarSource

class HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: typing.List[HTTPHeader]
    path: str
    port: IntOrString
    scheme: str

class Configuration(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: ConfigurationSpec
    status: ConfigurationStatus

class TCPSocketAction(typing_extensions.TypedDict, total=False):
    port: IntOrString
    host: str

class RevisionCondition(typing_extensions.TypedDict, total=False):
    status: str
    severity: str
    type: str
    message: str
    lastTransitionTime: str
    reason: str

class Condition(typing_extensions.TypedDict, total=False):
    severity: str
    type: str
    status: str
    reason: str
    message: str
    lastTransitionTime: str

class CloudAuditLogsSourceSpec(typing_extensions.TypedDict, total=False):
    serviceAccountName: str
    ceOverrides: CloudEventOverrides
    methodName: str
    sink: Destination
    resourceName: str
    serviceName: str

class CloudPubSubSourceSpec(typing_extensions.TypedDict, total=False):
    sink: Destination
    pubsubSecret: SecretKeySelector
    ceOverrides: CloudEventOverrides
    ackDeadline: str
    topic: str
    project: str
    secret: SecretKeySelector
    retainAckedMessages: bool
    retentionDuration: str

class ServiceCondition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    reason: str
    message: str
    severity: str
    status: str
    type: str

class ListCloudStorageSourcesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    kind: str
    metadata: ListMeta
    apiVersion: str
    items: typing.List[CloudStorageSource]

ListMeta = typing_extensions.TypedDict(
    "ListMeta",
    {
        "continue": str,
        "selfLink": str,
        "resourceVersion": str,
    },
    total=False,
)

class EnvFromSource(typing_extensions.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    secretRef: SecretEnvSource
    prefix: str

class ConfigurationSpec(typing_extensions.TypedDict, total=False):
    revisionTemplate: RevisionTemplate
    template: RevisionTemplate
    generation: int

class CloudEventOverrides(typing_extensions.TypedDict, total=False):
    extensions: typing.Dict[str, typing.Any]

class VolumeDevice(typing_extensions.TypedDict, total=False):
    name: str
    devicePath: str

class CloudAuditLogsSource(typing_extensions.TypedDict, total=False):
    spec: CloudAuditLogsSourceSpec
    kind: str
    status: CloudAuditLogsSourceStatus
    metadata: ObjectMeta
    apiVersion: str

class ListCloudPubSubSourcesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    apiVersion: str
    items: typing.List[CloudPubSubSource]
    metadata: ListMeta
    kind: str

class Container(typing_extensions.TypedDict, total=False):
    workingDir: str
    lifecycle: Lifecycle
    terminationMessagePath: str
    volumeMounts: typing.List[VolumeMount]
    livenessProbe: Probe
    name: str
    args: typing.List[str]
    resources: ResourceRequirements
    terminationMessagePolicy: str
    imagePullPolicy: str
    volumeDevices: typing.List[VolumeDevice]
    readinessProbe: Probe
    image: str
    envFrom: typing.List[EnvFromSource]
    command: typing.List[str]
    ports: typing.List[ContainerPort]
    tty: bool
    securityContext: SecurityContext
    stdinOnce: bool
    stdin: bool
    env: typing.List[EnvVar]

class CloudSchedulerSource(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    status: CloudSchedulerSourceStatus
    apiVersion: str
    spec: CloudSchedulerSourceSpec
    kind: str

class SELinuxOptions(typing_extensions.TypedDict, total=False):
    user: str
    role: str
    type: str
    level: str

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: Expr
    role: str

class DomainMappingCondition(typing_extensions.TypedDict, total=False):
    status: str
    type: str
    message: str
    severity: str
    lastTransitionTime: str
    reason: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SecretEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

class ObjectReference(typing_extensions.TypedDict, total=False):
    namespace: str
    name: str
    apiVersion: str
    uid: str
    kind: str
    resourceVersion: str
    fieldPath: str

class ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    items: typing.List[Revision]
    apiVersion: str
    unreachable: typing.List[str]
    metadata: ListMeta
    kind: str

class Probe(typing_extensions.TypedDict, total=False):
    handler: Handler
    initialDelaySeconds: int
    failureThreshold: int
    successThreshold: int
    timeoutSeconds: int
    periodSeconds: int

class CloudAuditLogsSourceStatus(typing_extensions.TypedDict, total=False):
    observedGeneration: int
    conditions: typing.List[Condition]
    sinkUri: str

class Service(typing_extensions.TypedDict, total=False):
    kind: str
    status: ServiceStatus
    spec: ServiceSpec
    apiVersion: str
    metadata: ObjectMeta

class Addressable(typing_extensions.TypedDict, total=False):
    hostname: str
    url: str

class DomainMapping(typing_extensions.TypedDict, total=False):
    apiVersion: str
    metadata: ObjectMeta
    kind: str
    spec: DomainMappingSpec
    status: DomainMappingStatus
