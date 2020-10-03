import typing

import typing_extensions

class BindDeviceToGatewayResponse(typing_extensions.TypedDict, total=False): ...

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    etag: str
    version: int

class MqttConfig(typing_extensions.TypedDict, total=False):
    mqttEnabledState: typing_extensions.Literal[
        "MQTT_STATE_UNSPECIFIED", "MQTT_ENABLED", "MQTT_DISABLED"
    ]

class Device(typing_extensions.TypedDict, total=False):
    lastEventTime: str
    state: DeviceState
    blocked: bool
    name: str
    lastConfigSendTime: str
    lastStateTime: str
    metadata: typing.Dict[str, typing.Any]
    logLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "NONE", "ERROR", "INFO", "DEBUG"
    ]
    id: str
    lastErrorStatus: Status
    lastErrorTime: str
    lastConfigAckTime: str
    credentials: typing.List[DeviceCredential]
    gatewayConfig: GatewayConfig
    config: DeviceConfig
    lastHeartbeatTime: str
    numId: str

class ListDeviceConfigVersionsResponse(typing_extensions.TypedDict, total=False):
    deviceConfigs: typing.List[DeviceConfig]

class PublicKeyCertificate(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT", "X509_CERTIFICATE_PEM"
    ]
    certificate: str
    x509Details: X509CertificateDetails

class StateNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopicName: str

class BindDeviceToGatewayRequest(typing_extensions.TypedDict, total=False):
    deviceId: str
    gatewayId: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Empty(typing_extensions.TypedDict, total=False): ...

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: typing.List[Device]
    nextPageToken: str

class EventNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopicName: str
    subfolderMatches: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class X509CertificateDetails(typing_extensions.TypedDict, total=False):
    expiryTime: str
    publicKeyType: str
    signatureAlgorithm: str
    startTime: str
    subject: str
    issuer: str

class ListDeviceRegistriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    deviceRegistries: typing.List[DeviceRegistry]

class UnbindDeviceFromGatewayResponse(typing_extensions.TypedDict, total=False): ...

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    title: str
    description: str
    location: str

class GatewayConfig(typing_extensions.TypedDict, total=False):
    lastAccessedGatewayId: str
    gatewayAuthMethod: typing_extensions.Literal[
        "GATEWAY_AUTH_METHOD_UNSPECIFIED",
        "ASSOCIATION_ONLY",
        "DEVICE_AUTH_TOKEN_ONLY",
        "ASSOCIATION_AND_DEVICE_AUTH_TOKEN",
    ]
    gatewayType: typing_extensions.Literal[
        "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
    ]
    lastAccessedGatewayTime: str

class ModifyCloudToDeviceConfigRequest(typing_extensions.TypedDict, total=False):
    versionToUpdate: str
    binaryData: str

class ListDeviceStatesResponse(typing_extensions.TypedDict, total=False):
    deviceStates: typing.List[DeviceState]

class UnbindDeviceFromGatewayRequest(typing_extensions.TypedDict, total=False):
    gatewayId: str
    deviceId: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    bindingId: str
    members: typing.List[str]
    role: str

class RegistryCredential(typing_extensions.TypedDict, total=False):
    publicKeyCertificate: PublicKeyCertificate

class DeviceState(typing_extensions.TypedDict, total=False):
    binaryData: str
    updateTime: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class SendCommandToDeviceResponse(typing_extensions.TypedDict, total=False): ...

class DeviceCredential(typing_extensions.TypedDict, total=False):
    expirationTime: str
    publicKey: PublicKeyCredential

class DeviceRegistry(typing_extensions.TypedDict, total=False):
    stateNotificationConfig: StateNotificationConfig
    mqttConfig: MqttConfig
    name: str
    httpConfig: HttpConfig
    logLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "NONE", "ERROR", "INFO", "DEBUG"
    ]
    eventNotificationConfigs: typing.List[EventNotificationConfig]
    id: str
    credentials: typing.List[RegistryCredential]

class HttpConfig(typing_extensions.TypedDict, total=False):
    httpEnabledState: typing_extensions.Literal[
        "HTTP_STATE_UNSPECIFIED", "HTTP_ENABLED", "HTTP_DISABLED"
    ]

class PublicKeyCredential(typing_extensions.TypedDict, total=False):
    key: str
    format: typing_extensions.Literal[
        "UNSPECIFIED_PUBLIC_KEY_FORMAT",
        "RSA_PEM",
        "RSA_X509_PEM",
        "ES256_PEM",
        "ES256_X509_PEM",
    ]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class DeviceConfig(typing_extensions.TypedDict, total=False):
    version: str
    binaryData: str
    deviceAckTime: str
    cloudUpdateTime: str

class SendCommandToDeviceRequest(typing_extensions.TypedDict, total=False):
    subfolder: str
    binaryData: str
