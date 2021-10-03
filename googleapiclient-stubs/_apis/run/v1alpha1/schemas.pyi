import typing

import typing_extensions

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
class Container(typing_extensions.TypedDict, total=False):
    args: typing.List[str]
    command: typing.List[str]
    env: typing.List[EnvVar]
    envFrom: typing.List[EnvFromSource]
    image: str
    imagePullPolicy: str
    livenessProbe: Probe
    name: str
    ports: typing.List[ContainerPort]
    readinessProbe: Probe
    resources: ResourceRequirements
    securityContext: SecurityContext
    startupProbe: Probe
    terminationMessagePath: str
    terminationMessagePolicy: str
    volumeMounts: typing.List[VolumeMount]
    workingDir: str

@typing.type_check_only
class ContainerPort(typing_extensions.TypedDict, total=False):
    containerPort: int
    name: str
    protocol: str

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
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HTTPGetAction(typing_extensions.TypedDict, total=False):
    host: str
    httpHeaders: typing.List[HTTPHeader]
    path: str
    scheme: str

@typing.type_check_only
class HTTPHeader(typing_extensions.TypedDict, total=False):
    name: str
    value: str

@typing.type_check_only
class InstanceAttemptResult(typing_extensions.TypedDict, total=False):
    exitCode: int
    status: GoogleRpcStatus

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
    lastAttemptResult: InstanceAttemptResult
    lastExitCode: int
    restarted: int
    startTime: str
    succeeded: int

@typing.type_check_only
class InstanceTemplateSpec(typing_extensions.TypedDict, total=False):
    spec: InstanceSpec

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
class ListJobsResponse(typing_extensions.TypedDict, total=False):
    apiVersion: str
    items: typing.List[Job]
    kind: str
    metadata: ListMeta
    nextPageToken: str
    unreachable: typing.List[str]

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
class LocalObjectReference(typing_extensions.TypedDict, total=False):
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
class Probe(typing_extensions.TypedDict, total=False):
    exec: ExecAction
    failureThreshold: int
    httpGet: HTTPGetAction
    initialDelaySeconds: int
    periodSeconds: int
    successThreshold: int
    tcpSocket: TCPSocketAction
    timeoutSeconds: int

@typing.type_check_only
class ResourceRequirements(typing_extensions.TypedDict, total=False):
    limits: typing.Dict[str, typing.Any]
    requests: typing.Dict[str, typing.Any]

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
    runAsUser: int

@typing.type_check_only
class TCPSocketAction(typing_extensions.TypedDict, total=False):
    host: str
    port: int

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
