import typing

_list = list

@typing.type_check_only
class ConfigMapEnvSource(typing.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapKeySelector(typing.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class ConfigMapVolumeSource(typing.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    name: str
    optional: bool

@typing.type_check_only
class Container(typing.TypedDict, total=False):
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
class ContainerPort(typing.TypedDict, total=False):
    containerPort: int
    name: str
    protocol: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EnvFromSource(typing.TypedDict, total=False):
    configMapRef: ConfigMapEnvSource
    prefix: str
    secretRef: SecretEnvSource

@typing.type_check_only
class EnvVar(typing.TypedDict, total=False):
    name: str
    value: str
    valueFrom: EnvVarSource

@typing.type_check_only
class EnvVarSource(typing.TypedDict, total=False):
    configMapKeyRef: ConfigMapKeySelector
    secretKeyRef: SecretKeySelector

@typing.type_check_only
class ExecAction(typing.TypedDict, total=False):
    command: _list[str]

@typing.type_check_only
class GRPCAction(typing.TypedDict, total=False):
    port: int
    service: str

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HTTPGetAction(typing.TypedDict, total=False):
    host: str
    httpHeaders: _list[HTTPHeader]
    path: str
    scheme: str

@typing.type_check_only
class HTTPHeader(typing.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class InstanceAttemptResult(typing.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus

@typing.type_check_only
class InstanceSpec(typing.TypedDict, total=False):
    activeDeadlineSeconds: str
    containers: _list[Container]
    restartPolicy: str
    serviceAccountName: str
    terminationGracePeriodSeconds: str
    volumes: _list[Volume]

@typing.type_check_only
class InstanceStatus(typing.TypedDict, total=False):
    completionTime: str
    failed: int
    index: int
    lastAttemptResult: InstanceAttemptResult
    lastExitCode: int
    restarted: int
    startTime: str
    succeeded: int

@typing.type_check_only
class InstanceTemplateSpec(typing.TypedDict, total=False):
    spec: InstanceSpec

@typing.type_check_only
class Job(typing.TypedDict, total=False):
    apiVersion: str
    kind: str
    metadata: ObjectMeta
    spec: JobSpec
    status: JobStatus

@typing.type_check_only
class JobCondition(typing.TypedDict, total=False):
    lastTransitionTime: str
    message: str
    reason: str
    severity: str
    status: str
    type: str

@typing.type_check_only
class JobSpec(typing.TypedDict, total=False):
    activeDeadlineSeconds: str
    backoffLimit: int
    completions: int
    parallelism: int
    template: InstanceTemplateSpec
    ttlSecondsAfterFinished: int

@typing.type_check_only
class JobStatus(typing.TypedDict, total=False):
    active: int
    completionTime: str
    conditions: _list[JobCondition]
    failed: int
    imageDigest: str
    instances: _list[InstanceStatus]
    observedGeneration: int
    startTime: str
    succeeded: int

@typing.type_check_only
class KeyToPath(typing.TypedDict, total=False):
    key: str
    mode: int
    path: str

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    apiVersion: str
    items: _list[Job]
    kind: str
    metadata: ListMeta
    nextPageToken: str
    unreachable: _list[str]

AlternativeListMeta = typing.TypedDict(
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
class LocalObjectReference(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class ObjectMeta(typing.TypedDict, total=False):
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
class OwnerReference(typing.TypedDict, total=False):
    apiVersion: str
    blockOwnerDeletion: bool
    controller: bool
    kind: str
    name: str
    uid: str

@typing.type_check_only
class Probe(typing.TypedDict, total=False):
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
class ResourceRequirements(typing.TypedDict, total=False):
    limits: dict[str, typing.Any]
    requests: dict[str, typing.Any]

@typing.type_check_only
class SecretEnvSource(typing.TypedDict, total=False):
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretKeySelector(typing.TypedDict, total=False):
    key: str
    localObjectReference: LocalObjectReference
    name: str
    optional: bool

@typing.type_check_only
class SecretVolumeSource(typing.TypedDict, total=False):
    defaultMode: int
    items: _list[KeyToPath]
    optional: bool
    secretName: str

@typing.type_check_only
class SecurityContext(typing.TypedDict, total=False):
    runAsUser: int

@typing.type_check_only
class TCPSocketAction(typing.TypedDict, total=False):
    host: str
    port: int

@typing.type_check_only
class Volume(typing.TypedDict, total=False):
    configMap: ConfigMapVolumeSource
    name: str
    secret: SecretVolumeSource

@typing.type_check_only
class VolumeMount(typing.TypedDict, total=False):
    mountPath: str
    name: str
    readOnly: bool
    subPath: str
