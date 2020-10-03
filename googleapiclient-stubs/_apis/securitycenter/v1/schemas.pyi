import typing

import typing_extensions

class Resource(typing_extensions.TypedDict, total=False):
    projectDisplayName: str
    projectName: str
    name: str
    parentDisplayName: str
    parentName: str

class Finding(typing_extensions.TypedDict, total=False):
    eventTime: str
    category: str
    securityMarks: SecurityMarks
    externalUri: str
    sourceProperties: typing.Dict[str, typing.Any]
    parent: str
    resourceName: str
    createTime: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Binding(typing_extensions.TypedDict, total=False):
    role: str
    condition: Expr
    members: typing.List[str]

class GoogleCloudSecuritycenterV1p1beta1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    notificationConfigName: str
    finding: GoogleCloudSecuritycenterV1p1beta1Finding
    resource: GoogleCloudSecuritycenterV1p1beta1Resource

class ListNotificationConfigsResponse(typing_extensions.TypedDict, total=False):
    notificationConfigs: typing.List[NotificationConfig]
    nextPageToken: str

class ListAssetsResult(typing_extensions.TypedDict, total=False):
    asset: Asset
    stateChange: typing_extensions.Literal["UNUSED", "ADDED", "REMOVED", "ACTIVE"]

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleCloudSecuritycenterV1p1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    duration: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]

class GoogleCloudSecuritycenterV1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]
    duration: str

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    auditConfigs: typing.List[AuditConfig]
    etag: str
    bindings: typing.List[Binding]

class SecurityCenterProperties(typing_extensions.TypedDict, total=False):
    resourceDisplayName: str
    resourceType: str
    resourceParentDisplayName: str
    resourceName: str
    resourceProjectDisplayName: str
    resourceProject: str
    resourceParent: str
    resourceOwners: typing.List[str]

class ListSourcesResponse(typing_extensions.TypedDict, total=False):
    sources: typing.List[Source]
    nextPageToken: str

class AssetDiscoveryConfig(typing_extensions.TypedDict, total=False):
    inclusionMode: typing_extensions.Literal[
        "INCLUSION_MODE_UNSPECIFIED", "INCLUDE_ONLY", "EXCLUDE"
    ]
    projectIds: typing.List[str]

class GroupFindingsRequest(typing_extensions.TypedDict, total=False):
    filter: str
    compareDuration: str
    readTime: str
    pageToken: str
    pageSize: int
    groupBy: str

class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    listAssetsResults: typing.List[ListAssetsResult]
    totalSize: int
    readTime: str
    nextPageToken: str

class SetFindingStateRequest(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]
    startTime: str

class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    location: str
    description: str
    title: str

class SecurityMarks(typing_extensions.TypedDict, total=False):
    name: str
    marks: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ListFindingsResult(typing_extensions.TypedDict, total=False):
    finding: Finding
    stateChange: typing_extensions.Literal[
        "UNUSED", "CHANGED", "UNCHANGED", "ADDED", "REMOVED"
    ]
    resource: Resource

class GoogleCloudSecuritycenterV1Resource(typing_extensions.TypedDict, total=False):
    project: str
    parentDisplayName: str
    parent: str
    projectDisplayName: str
    name: str

class StreamingConfig(typing_extensions.TypedDict, total=False):
    filter: str

class GoogleCloudSecuritycenterV1p1beta1Finding(
    typing_extensions.TypedDict, total=False
):
    externalUri: str
    securityMarks: GoogleCloudSecuritycenterV1p1beta1SecurityMarks
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "HIGH", "MEDIUM", "LOW"
    ]
    name: str
    sourceProperties: typing.Dict[str, typing.Any]
    eventTime: str
    parent: str
    createTime: str
    category: str
    resourceName: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "INACTIVE"]

class GroupFindingsResponse(typing_extensions.TypedDict, total=False):
    readTime: str
    nextPageToken: str
    groupByResults: typing.List[GroupResult]
    totalSize: int

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class GroupResult(typing_extensions.TypedDict, total=False):
    count: str
    properties: typing.Dict[str, typing.Any]

class Source(typing_extensions.TypedDict, total=False):
    name: str
    description: str
    displayName: str

class GroupAssetsRequest(typing_extensions.TypedDict, total=False):
    groupBy: str
    readTime: str
    filter: str
    compareDuration: str
    pageToken: str
    pageSize: int

class OrganizationSettings(typing_extensions.TypedDict, total=False):
    enableAssetDiscovery: bool
    name: str
    assetDiscoveryConfig: AssetDiscoveryConfig

class NotificationConfig(typing_extensions.TypedDict, total=False):
    serviceAccount: str
    description: str
    streamingConfig: StreamingConfig
    name: str
    pubsubTopic: str

class GoogleCloudSecuritycenterV1beta1RunAssetDiscoveryResponse(
    typing_extensions.TypedDict, total=False
):
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "COMPLETED", "SUPERSEDED", "TERMINATED"
    ]
    duration: str

class GoogleCloudSecuritycenterV1NotificationMessage(
    typing_extensions.TypedDict, total=False
):
    resource: GoogleCloudSecuritycenterV1Resource
    finding: Finding
    notificationConfigName: str

class Asset(typing_extensions.TypedDict, total=False):
    resourceProperties: typing.Dict[str, typing.Any]
    updateTime: str
    securityCenterProperties: SecurityCenterProperties
    iamPolicy: IamPolicy
    name: str
    createTime: str
    securityMarks: SecurityMarks

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class GoogleCloudSecuritycenterV1p1beta1SecurityMarks(
    typing_extensions.TypedDict, total=False
):
    name: str
    marks: typing.Dict[str, typing.Any]

class GoogleCloudSecuritycenterV1p1beta1Resource(
    typing_extensions.TypedDict, total=False
):
    projectDisplayName: str
    parentDisplayName: str
    name: str
    parent: str
    project: str

class ListFindingsResponse(typing_extensions.TypedDict, total=False):
    totalSize: int
    readTime: str
    listFindingsResults: typing.List[ListFindingsResult]
    nextPageToken: str

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

class Operation(typing_extensions.TypedDict, total=False):
    response: typing.Dict[str, typing.Any]
    done: bool
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status

class Status(typing_extensions.TypedDict, total=False):
    message: str
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]

class GroupAssetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    readTime: str
    groupByResults: typing.List[GroupResult]
    totalSize: int

class IamPolicy(typing_extensions.TypedDict, total=False):
    policyBlob: str

class RunAssetDiscoveryRequest(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]
