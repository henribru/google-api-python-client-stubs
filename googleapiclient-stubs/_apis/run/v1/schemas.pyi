import typing

import typing_extensions

class Volume(typing_extensions.TypedDict, total=False):
    name: str
    secret: SecretVolumeSource
    configMap: ConfigMapVolumeSource

class ConfigMapEnvSource(typing_extensions.TypedDict, total=False):
    name: str
    localObjectReference: LocalObjectReference
    optional: bool

class ListDomainMappingsResponse(typing_extensions.TypedDict, total=False):
    metadata: ListMeta
    apiVersion: str
    kind: str
    items: typing.List[DomainMapping]
    unreachable: typing.List[str]

class SecretVolumeSource(typing_extensions.TypedDict, total=False):
    secretName: str
    defaultMode: int
    optional: bool
    items: typing.List[KeyToPath]

class ResourceRequirements(typing_extensions.TypedDict, total=False):
    requests: typing.Dict[str, typing.Any]
    limits: typing.Dict[str, typing.Any]

class HTTPGetAction(typing_extensions.TypedDict, total=False):
    scheme: str
    path: str
    httpHeaders: typing.List[HTTPHeader]
    host: str

class DomainMapping(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: DomainMappingSpec
    status: DomainMappingStatus
    apiVersion: str
    kind: str

class DomainMappingStatus(typing_extensions.TypedDict, total=False):
    mappedRouteName: str
    conditions: typing.List[GoogleCloudRunV1Condition]
    url: str
    resourceRecords: typing.List[ResourceRecord]
    observedGeneration: int

class HTTPHeader(typing_extensions.TypedDict, total=False):
    value: str
    name: str

class LocalObjectReference(typing_extensions.TypedDict, total=False):
    name: str

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: Expr
    role: str

class SecretEnvSource(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    optional: bool
    name: str

class ServiceSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate
    traffic: typing.List[TrafficTarget]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Revision(typing_extensions.TypedDict, total=False):
    kind: str
    spec: RevisionSpec
    apiVersion: str
    status: RevisionStatus
    metadata: ObjectMeta

class ConfigMapVolumeSource(typing_extensions.TypedDict, total=False):
    name: str
    items: typing.List[KeyToPath]
    optional: bool
    defaultMode: int

class OwnerReference(typing_extensions.TypedDict, total=False):
    kind: str
    uid: str
    name: str
    blockOwnerDeletion: bool
    controller: bool
    apiVersion: str

class ListRoutesResponse(typing_extensions.TypedDict, total=False):
    unreachable: typing.List[str]
    kind: str
    apiVersion: str
    items: typing.List[Route]
    metadata: ListMeta

class Addressable(typing_extensions.TypedDict, total=False):
    url: str

class RevisionStatus(typing_extensions.TypedDict, total=False):
    logUrl: str
    observedGeneration: int
    conditions: typing.List[GoogleCloudRunV1Condition]
    imageDigest: str
    serviceName: str

class AuthorizedDomain(typing_extensions.TypedDict, total=False):
    id: str
    name: str

class ListAuthorizedDomainsResponse(typing_extensions.TypedDict, total=False):
    domains: typing.List[AuthorizedDomain]
    nextPageToken: str

class VolumeMount(typing_extensions.TypedDict, total=False):
    subPath: str
    readOnly: bool
    name: str
    mountPath: str

class ListRevisionsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    apiVersion: str
    metadata: ListMeta
    items: typing.List[Revision]
    unreachable: typing.List[str]

class EnvVar(typing_extensions.TypedDict, total=False):
    valueFrom: EnvVarSource
    name: str
    value: str

class ListConfigurationsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    unreachable: typing.List[str]
    metadata: ListMeta
    items: typing.List[Configuration]
    kind: str

class RevisionTemplate(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: RevisionSpec

class TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
    port: int

class ListServicesResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ListMeta
    unreachable: typing.List[str]
    items: typing.List[Service]

class Status(typing_extensions.TypedDict, total=False):
    reason: str
    code: int
    status: str
    metadata: ListMeta
    message: str
    details: StatusDetails

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class EnvVarSource(typing_extensions.TypedDict, total=False):
    secretKeyRef: SecretKeySelector
    configMapKeyRef: ConfigMapKeySelector

class KeyToPath(typing_extensions.TypedDict, total=False):
    key: str
    mode: int
    path: str

class StatusDetails(typing_extensions.TypedDict, total=False):
    kind: str
    causes: typing.List[StatusCause]
    retryAfterSeconds: int
    group: str
    uid: str
    name: str

class ServiceStatus(typing_extensions.TypedDict, total=False):
    conditions: typing.List[GoogleCloudRunV1Condition]
    url: str
    address: Addressable
    latestCreatedRevisionName: str
    traffic: typing.List[TrafficTarget]
    latestReadyRevisionName: str
    observedGeneration: int

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    expression: str
    title: str

class TrafficTarget(typing_extensions.TypedDict, total=False):
    latestRevision: bool
    percent: int
    revisionName: str
    configurationName: str
    tag: str
    url: str

class Service(typing_extensions.TypedDict, total=False):
    metadata: ObjectMeta
    spec: ServiceSpec
    status: ServiceStatus
    apiVersion: str
    kind: str

class ExecAction(typing_extensions.TypedDict, total=False):
    command: typing.List[str]

class EnvFromSource(typing_extensions.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    secretRef: SecretEnvSource
    prefix: str

class Configuration(typing_extensions.TypedDict, total=False):
    spec: ConfigurationSpec
    metadata: ObjectMeta
    status: ConfigurationStatus
    kind: str
    apiVersion: str

class GoogleCloudRunV1Condition(typing_extensions.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    type: str
    reason: str
    status: str
    severity: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class ResourceRecord(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal["RECORD_TYPE_UNSPECIFIED", "A", "AAAA", "CNAME"]
    rrdata: str

class StatusCause(typing_extensions.TypedDict, total=False):
    field: str
    message: str
    reason: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class RevisionSpec(typing_extensions.TypedDict, total=False):
    timeoutSeconds: int
    serviceAccountName: str
    containerConcurrency: int
    containers: typing.List[Container]
    volumes: typing.List[Volume]

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    labels: typing.Dict[str, typing.Any]
    displayName: str
    metadata: typing.Dict[str, typing.Any]
    name: str

class SecurityContext(typing_extensions.TypedDict, total=False):
    runAsUser: int

ListMeta = typing_extensions.TypedDict(
    "ListMeta",
    {
        "selfLink": str,
        "continue": str,
        "resourceVersion": str,
    },
    total=False,
)

class Probe(typing_extensions.TypedDict, total=False):
    periodSeconds: int
    successThreshold: int
    failureThreshold: int
    tcpSocket: TCPSocketAction
    httpGet: HTTPGetAction
    initialDelaySeconds: int
    timeoutSeconds: int
    exec: ExecAction

class ObjectMeta(typing_extensions.TypedDict, total=False):
    deletionTimestamp: str
    creationTimestamp: str
    finalizers: typing.List[str]
    generation: int
    name: str
    namespace: str
    generateName: str
    deletionGracePeriodSeconds: int
    resourceVersion: str
    uid: str
    selfLink: str
    annotations: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    clusterName: str
    ownerReferences: typing.List[OwnerReference]

class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

class ConfigurationStatus(typing_extensions.TypedDict, total=False):
    latestReadyRevisionName: str
    latestCreatedRevisionName: str
    observedGeneration: int
    conditions: typing.List[GoogleCloudRunV1Condition]

class Route(typing_extensions.TypedDict, total=False):
    status: RouteStatus
    kind: str
    apiVersion: str
    spec: RouteSpec
    metadata: ObjectMeta

class RouteSpec(typing_extensions.TypedDict, total=False):
    traffic: typing.List[TrafficTarget]

class RouteStatus(typing_extensions.TypedDict, total=False):
    url: str
    conditions: typing.List[GoogleCloudRunV1Condition]
    address: Addressable
    observedGeneration: int
    traffic: typing.List[TrafficTarget]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SecretKeySelector(typing_extensions.TypedDict, total=False):
    optional: bool
    name: str
    localObjectReference: LocalObjectReference
    key: str

class DomainMappingSpec(typing_extensions.TypedDict, total=False):
    certificateMode: typing_extensions.Literal[
        "CERTIFICATE_MODE_UNSPECIFIED", "NONE", "AUTOMATIC"
    ]
    forceOverride: bool
    routeName: str

class ConfigMapKeySelector(typing_extensions.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    key: str
    name: str
    optional: bool

class ContainerPort(typing_extensions.TypedDict, total=False):
    protocol: str
    containerPort: int
    name: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ConfigurationSpec(typing_extensions.TypedDict, total=False):
    template: RevisionTemplate

class Container(typing_extensions.TypedDict, total=False):
    name: str
    env: typing.List[EnvVar]
    terminationMessagePolicy: str
    ports: typing.List[ContainerPort]
    livenessProbe: Probe
    readinessProbe: Probe
    imagePullPolicy: str
    securityContext: SecurityContext
    workingDir: str
    command: typing.List[str]
    terminationMessagePath: str
    image: str
    resources: ResourceRequirements
    args: typing.List[str]
    envFrom: typing.List[EnvFromSource]
    volumeMounts: typing.List[VolumeMount]
