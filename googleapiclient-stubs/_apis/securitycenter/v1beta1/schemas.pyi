import typing

import typing_extensions

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: typing.List[Source]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSecuritycenterV1Resource(typing_extensions.TypedDict, total=False):
    name: str
    project: str
    projectDisplayName: str
    parentDisplayName: str
    parent: str

class GoogleCloudSecuritycenterV1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    name: str
    marks: typing.Dict[str, typing.Any]

class GroupAssetsResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    groupByResults: typing.List[GroupResult]
    nextPageToken: str

class OrganizationSettings(typing_extensions.TypedDict, total=False):
    enableAssetDiscovery: bool
    name: str
    assetDiscoveryConfig: AssetDiscoveryConfig

class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]
    duration: str

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    members: typing.List[str]
    condition: Expr

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class AssetDiscoveryConfig(typing_extensions.TypedDict, total=False):
    inclusionMode: typing_extensions.Literal[
        "INCLUSION_MODE_UNSPECIFIED", "INCLUDE_ONLY", "EXCLUDE"
    ]
    projectIds: typing.List[str]

class Expr(typing_extensions.TypedDict, total=False):
    description: str
    location: str
    expression: str
    title: str

class Finding(typing_extensions.TypedDict, total=False):
    securityMarks: SecurityMarks
    sourceProperties: typing.Dict[str, typing.Any]
    resourceName: str
    eventTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    parent: str
    category: str
    name: str
    createTime: str
    externalUri: str

class GroupResult(typing_extensions.TypedDict, total=False):
    properties: typing.Dict[str, typing.Any]
    count: str

class GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

class GroupFindingsRequest(typing_extensions.TypedDict, total=False):
    readTime: str
    pageSize: int
    pageToken: str
    filter: str
    groupBy: str

class GoogleCloudSecuritycenterV1beta1Finding(typing_extensions.TypedDict, total=False):
    category: str
    parent: str
    sourceProperties: typing.Dict[str, typing.Any]
    resourceName: str
    createTime: str
    name: str
    eventTime: str
    externalUri: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks

class GoogleCloudSecuritycenterV1p1beta1Finding(
    typing_extensions.TypedDict, total=False
):
    resourceName: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    eventTime: str
    parent: str
    externalUri: str
    name: str
    sourceProperties: typing.Dict[str, typing.Any]
    category: str
    securityMarks: GoogleCloudSecuritycenterV1p1beta1SecurityMarks
    createTime: str

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    name: str
    error: Status
    metadata: typing.Dict[str, typing.Any]
    done: bool

class Asset(typing_extensions.TypedDict, total=False):
    updateTime: str
    name: str
    securityCenterProperties: SecurityCenterProperties
    securityMarks: GoogleCloudSecuritycenterV1beta1SecurityMarks
    createTime: str
    resourceProperties: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    listAssetsResults: typing.List[ListAssetsResult]
    nextPageToken: str
    readTime: str
    totalSize: int

class GoogleCloudSecuritycenterV1p1beta1Resource(
    typing_extensions.TypedDict, total=False
):
    parentDisplayName: str
    name: str
    parent: str
    projectDisplayName: str
    project: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    version: int
    bindings: typing.List[Binding]
    auditConfigs: typing.List[AuditConfig]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class GoogleCloudSecuritycenterV1p1beta1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    finding: GoogleCloudSecuritycenterV1p1beta1Finding
    notificationConfigName: str
    resource: GoogleCloudSecuritycenterV1p1beta1Resource

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]
    exemptedMembers: typing.List[str]

class ListAssetsResult(typing_extensions.TypedDict, total=False):
    asset: Asset
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNUSED", "ADDED", "REMOVED", "ACTIVE"
    ]

class GoogleCloudSecuritycenterV1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]
    duration: str

class SecurityCenterProperties(typing_extensions.TypedDict, total=False):
    resourceProject: str
    resourceType: str
    resourceParent: str
    resourceOwners: typing.List[str]
    resourceName: str

class GoogleCloudSecuritycenterV1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    finding: Finding
    resource: GoogleCloudSecuritycenterV1Resource
    notificationConfigName: str

class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    findings: typing.List[GoogleCloudSecuritycenterV1beta1Finding]
    totalSize: int
    nextPageToken: str
    readTime: str

class GoogleCloudSecuritycenterV1p1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    name: str
    marks: typing.Dict[str, typing.Any]

class SetFindingStateRequest(typing_extensions.TypedDict, total=False):
    startTime: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

class SecurityMarks(typing_extensions.TypedDict, total=False):
    name: str
    marks: typing.Dict[str, typing.Any]

class Source(typing_extensions.TypedDict, total=False):
    displayName: str
    description: str
    name: str

class GroupAssetsRequest(typing_extensions.TypedDict, total=False):
    pageSize: int
    filter: str
    compareDuration: str
    pageToken: str
    groupBy: str
    readTime: str

class RunAssetDiscoveryRequest(typing_extensions.TypedDict, total=False): ...

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class Empty(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class GroupFindingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    groupByResults: typing.List[GroupResult]
    readTime: str
