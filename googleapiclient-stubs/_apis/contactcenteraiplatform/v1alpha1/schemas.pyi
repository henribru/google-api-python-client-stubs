import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdminUser(typing_extensions.TypedDict, total=False):
    familyName: str
    givenName: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Component(typing_extensions.TypedDict, total=False):
    name: str
    serviceAttachmentNames: _list[str]

@typing.type_check_only
class ContactCenter(typing_extensions.TypedDict, total=False):
    adminUser: AdminUser
    ccaipManagedUsers: bool
    createTime: str
    critical: Critical
    customerDomainPrefix: str
    displayName: str
    early: Early
    instanceConfig: InstanceConfig
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    normal: Normal
    privateAccess: PrivateAccess
    privateComponents: _list[str]
    samlParams: SAMLParams
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_DEPLOYING",
        "STATE_DEPLOYED",
        "STATE_TERMINATING",
        "STATE_FAILED",
        "STATE_TERMINATING_FAILED",
        "STATE_TERMINATED",
        "STATE_IN_GRACE_PERIOD",
        "STATE_FAILING_OVER",
        "STATE_DEGRADED",
        "STATE_REPAIRING",
    ]
    updateTime: str
    uris: URIs
    userEmail: str

@typing.type_check_only
class ContactCenterQuota(typing_extensions.TypedDict, total=False):
    contactCenterCountLimit: int
    contactCenterCountSum: int
    quotas: _list[Quota]

@typing.type_check_only
class Critical(typing_extensions.TypedDict, total=False):
    peakHours: _list[WeeklySchedule]

@typing.type_check_only
class Early(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    instanceSize: typing_extensions.Literal[
        "INSTANCE_SIZE_UNSPECIFIED",
        "STANDARD_SMALL",
        "STANDARD_MEDIUM",
        "STANDARD_LARGE",
        "STANDARD_XLARGE",
        "STANDARD_2XLARGE",
        "STANDARD_3XLARGE",
        "DEV_XSMALL",
        "MULTIREGION_SMALL",
        "MULTIREGION_MEDIUM",
        "MULTIREGION_LARGE",
        "MULTIREGION_XLARGE",
        "MULTIREGION_2XLARGE",
        "MULTIREGION_3XLARGE",
        "DEV_SMALL",
        "SANDBOX_SMALL",
        "TRIAL_SMALL",
        "TIME_LIMITED_TRIAL_SMALL",
    ]

@typing.type_check_only
class ListContactCentersResponse(typing_extensions.TypedDict, total=False):
    contactCenters: _list[ContactCenter]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Normal(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    contactCenter: ContactCenter
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class PrivateAccess(typing_extensions.TypedDict, total=False):
    egressSettings: _list[Component]
    ingressSettings: _list[Component]
    pscSetting: PscSetting

@typing.type_check_only
class PscSetting(typing_extensions.TypedDict, total=False):
    allowedConsumerProjectIds: _list[str]
    producerProjectIds: _list[str]

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    contactCenterCountLimit: int
    contactCenterCountSum: int
    contactCenterInstanceSize: typing_extensions.Literal[
        "INSTANCE_SIZE_UNSPECIFIED",
        "STANDARD_SMALL",
        "STANDARD_MEDIUM",
        "STANDARD_LARGE",
        "STANDARD_XLARGE",
        "STANDARD_2XLARGE",
        "STANDARD_3XLARGE",
        "DEV_XSMALL",
        "MULTIREGION_SMALL",
        "MULTIREGION_MEDIUM",
        "MULTIREGION_LARGE",
        "MULTIREGION_XLARGE",
        "MULTIREGION_2XLARGE",
        "MULTIREGION_3XLARGE",
        "DEV_SMALL",
        "SANDBOX_SMALL",
        "TRIAL_SMALL",
        "TIME_LIMITED_TRIAL_SMALL",
    ]

@typing.type_check_only
class SAMLParams(typing_extensions.TypedDict, total=False):
    authenticationContexts: _list[
        typing_extensions.Literal[
            "AUTHENTICATION_CONTEXT_UNSPECIFIED",
            "INTERNET_PROTOCOL",
            "INTERNET_PROTOCOL_PASSWORD",
            "KERBEROS",
            "MOBILE_ONE_FACTOR_UNREGISTERED",
            "MOBILE_TWO_FACTOR_UNREGISTERED",
            "MOBILE_ONE_FACTOR_CONTRACT",
            "MOBILE_TWO_FACTOR_CONTRACT",
            "PASSWORD",
            "PASSWORD_PROTECTED_TRANSPORT",
            "PREVIOUS_SESSION",
            "PUBLIC_KEY_X509",
            "PUBLIC_KEY_PGP",
            "PUBLIC_KEY_SPKI",
            "PUBLIC_KEY_XML_DIGITAL_SIGNATURE",
            "SMARTCARD",
            "SMARTCARD_PKI",
            "SOFTWARE_PKI",
            "TELEPHONY",
            "TELEPHONY_NOMADIC",
            "TELEPHONY_PERSONALIZED",
            "TELEPHONY_AUTHENTICATED",
            "SECURE_REMOTE_PASSWORD",
            "SSL_TLS_CERTIFICATE_BASED",
            "TIME_SYNC_TOKEN",
        ]
    ]
    certificate: str
    emailMapping: str
    entityId: str
    ssoUri: str
    userEmail: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TimeOfDay(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int
    nanos: int
    seconds: int

@typing.type_check_only
class URIs(typing_extensions.TypedDict, total=False):
    chatBotUri: str
    mediaUri: str
    rootUri: str
    virtualAgentStreamingServiceUri: str

@typing.type_check_only
class WeeklySchedule(typing_extensions.TypedDict, total=False):
    days: _list[
        typing_extensions.Literal[
            "DAY_OF_WEEK_UNSPECIFIED",
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY",
        ]
    ]
    duration: str
    endTime: TimeOfDay
    startTime: TimeOfDay
