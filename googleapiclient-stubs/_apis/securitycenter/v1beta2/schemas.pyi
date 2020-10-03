import typing

import typing_extensions

class EventThreatDetectionSettings(typing_extensions.TypedDict, total=False):
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    modules: typing.Dict[str, typing.Any]
    name: str
    updateTime: str

class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

class SecurityHealthAnalyticsSettings(typing_extensions.TypedDict, total=False):
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    name: str
    modules: typing.Dict[str, typing.Any]
    serviceAccount: str
    updateTime: str

class GoogleCloudSecuritycenterV1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

class GoogleCloudSecuritycenterV1p1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    marks: typing.Dict[str, typing.Any]
    name: str

class Details(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "STANDARD", "TRIAL", "ALPHA"]
    startTime: str
    endTime: str

class ContainerThreatDetectionSettings(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    name: str
    updateTime: str
    modules: typing.Dict[str, typing.Any]

class GoogleCloudSecuritycenterV1p1beta1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    resource: GoogleCloudSecuritycenterV1p1beta1Resource
    finding: GoogleCloudSecuritycenterV1p1beta1Finding
    notificationConfigName: str

class WebSecurityScannerSettings(typing_extensions.TypedDict, total=False):
    serviceEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    updateTime: str
    modules: typing.Dict[str, typing.Any]
    name: str

class Finding(typing_extensions.TypedDict, total=False):
    createTime: str
    securityMarks: SecurityMarks
    resourceName: str
    externalUri: str
    eventTime: str
    sourceProperties: typing.Dict[str, typing.Any]
    name: str
    parent: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    category: str

class SecurityMarks(typing_extensions.TypedDict, total=False):
    marks: typing.Dict[str, typing.Any]
    name: str

class GoogleCloudSecuritycenterV1p1beta1Resource(
    typing_extensions.TypedDict, total=False
):
    project: str
    projectDisplayName: str
    parentDisplayName: str
    parent: str
    name: str

class GoogleCloudSecuritycenterV1p1beta1Finding(
    typing_extensions.TypedDict, total=False
):
    resourceName: str
    externalUri: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    name: str
    securityMarks: GoogleCloudSecuritycenterV1p1beta1SecurityMarks
    category: str
    createTime: str
    parent: str
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    eventTime: str
    sourceProperties: typing.Dict[str, typing.Any]

class GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]
    duration: str

class GoogleCloudSecuritycenterV1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1Resource
    finding: Finding

class Subscription(typing_extensions.TypedDict, total=False):
    details: Details
    tier: typing_extensions.Literal["TIER_UNSPECIFIED", "STANDARD", "PREMIUM"]
    name: str

class GoogleCloudSecuritycenterV1Resource(typing_extensions.TypedDict, total=False):
    parentDisplayName: str
    name: str
    parent: str
    projectDisplayName: str
    project: str

class SecurityCenterSettings(typing_extensions.TypedDict, total=False):
    logSinkProject: str
    orgServiceAccount: str
    name: str

class Config(typing_extensions.TypedDict, total=False):
    moduleEnablementState: typing_extensions.Literal[
        "ENABLEMENT_STATE_UNSPECIFIED", "INHERITED", "ENABLED", "DISABLED"
    ]
    value: typing.Dict[str, typing.Any]
