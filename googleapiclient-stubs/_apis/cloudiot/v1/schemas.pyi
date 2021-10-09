import typing

import typing_extensions

_list = list

@typing.type_check_only
class BindDeviceToGatewayRequest(typing_extensions.TypedDict, total=False):
    deviceId: str
    gatewayId: str

@typing.type_check_only
class BindDeviceToGatewayResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Device(typing_extensions.TypedDict, total=False):
    blocked: bool
    config: DeviceConfig
    credentials: _list[DeviceCredential]
    gatewayConfig: GatewayConfig
    id: str
    lastConfigAckTime: str
    lastConfigSendTime: str
    lastErrorStatus: Status
    lastErrorTime: str
    lastEventTime: str
    lastHeartbeatTime: str
    lastStateTime: str
    logLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "NONE", "ERROR", "INFO", "DEBUG"
    ]
    metadata: dict[str, typing.Any]
    name: str
    numId: str
    state: DeviceState

@typing.type_check_only
class DeviceConfig(typing_extensions.TypedDict, total=False):
    binaryData: str
    cloudUpdateTime: str
    deviceAckTime: str
    version: str

@typing.type_check_only
class DeviceCredential(typing_extensions.TypedDict, total=False):
    expirationTime: str
    publicKey: PublicKeyCredential

@typing.type_check_only
class DeviceRegistry(typing_extensions.TypedDict, total=False):
    credentials: _list[RegistryCredential]
    eventNotificationConfigs: _list[EventNotificationConfig]
    httpConfig: HttpConfig
    id: str
    logLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "NONE", "ERROR", "INFO", "DEBUG"
    ]
    mqttConfig: MqttConfig
    name: str
    stateNotificationConfig: StateNotificationConfig

@typing.type_check_only
class DeviceState(typing_extensions.TypedDict, total=False):
    binaryData: str
    updateTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EventNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopicName: str
    subfolderMatches: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GatewayConfig(typing_extensions.TypedDict, total=False):
    gatewayAuthMethod: typing_extensions.Literal[
        "GATEWAY_AUTH_METHOD_UNSPECIFIED",
        "ASSOCIATION_ONLY",
        "DEVICE_AUTH_TOKEN_ONLY",
        "ASSOCIATION_AND_DEVICE_AUTH_TOKEN",
    ]
    gatewayType: typing_extensions.Literal[
        "GATEWAY_TYPE_UNSPECIFIED", "GATEWAY", "NON_GATEWAY"
    ]
    lastAccessedGatewayId: str
    lastAccessedGatewayTime: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class HttpConfig(typing_extensions.TypedDict, total=False):
    httpEnabledState: typing_extensions.Literal[
        "HTTP_STATE_UNSPECIFIED", "HTTP_ENABLED", "HTTP_DISABLED"
    ]

@typing.type_check_only
class ListDeviceConfigVersionsResponse(typing_extensions.TypedDict, total=False):
    deviceConfigs: _list[DeviceConfig]

@typing.type_check_only
class ListDeviceRegistriesResponse(typing_extensions.TypedDict, total=False):
    deviceRegistries: _list[DeviceRegistry]
    nextPageToken: str

@typing.type_check_only
class ListDeviceStatesResponse(typing_extensions.TypedDict, total=False):
    deviceStates: _list[DeviceState]

@typing.type_check_only
class ListDevicesResponse(typing_extensions.TypedDict, total=False):
    devices: _list[Device]
    nextPageToken: str

@typing.type_check_only
class ModifyCloudToDeviceConfigRequest(typing_extensions.TypedDict, total=False):
    binaryData: str
    versionToUpdate: str

@typing.type_check_only
class MqttConfig(typing_extensions.TypedDict, total=False):
    mqttEnabledState: typing_extensions.Literal[
        "MQTT_STATE_UNSPECIFIED", "MQTT_ENABLED", "MQTT_DISABLED"
    ]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PublicKeyCertificate(typing_extensions.TypedDict, total=False):
    certificate: str
    format: typing_extensions.Literal[
        "UNSPECIFIED_PUBLIC_KEY_CERTIFICATE_FORMAT", "X509_CERTIFICATE_PEM"
    ]
    x509Details: X509CertificateDetails

@typing.type_check_only
class PublicKeyCredential(typing_extensions.TypedDict, total=False):
    format: typing_extensions.Literal[
        "UNSPECIFIED_PUBLIC_KEY_FORMAT",
        "RSA_PEM",
        "RSA_X509_PEM",
        "ES256_PEM",
        "ES256_X509_PEM",
    ]
    key: str

@typing.type_check_only
class RegistryCredential(typing_extensions.TypedDict, total=False):
    publicKeyCertificate: PublicKeyCertificate

@typing.type_check_only
class SendCommandToDeviceRequest(typing_extensions.TypedDict, total=False):
    binaryData: str
    subfolder: str

@typing.type_check_only
class SendCommandToDeviceResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class StateNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopicName: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class UnbindDeviceFromGatewayRequest(typing_extensions.TypedDict, total=False):
    deviceId: str
    gatewayId: str

@typing.type_check_only
class UnbindDeviceFromGatewayResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class X509CertificateDetails(typing_extensions.TypedDict, total=False):
    expiryTime: str
    issuer: str
    publicKeyType: str
    signatureAlgorithm: str
    startTime: str
    subject: str
