import typing

import typing_extensions

_list = list

@typing.type_check_only
class Accelerator(typing_extensions.TypedDict, total=False):
    acceleratorType: typing_extensions.Literal[
        "ACCELERATOR_TYPE_UNSPECIFIED",
        "CDC",
        "HEALTHCARE",
        "CCAI_INSIGHTS",
        "CLOUDSEARCH",
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ENABLED", "DISABLED", "UNKNOWN"
    ]

@typing.type_check_only
class AssetLocation(typing_extensions.TypedDict, total=False):
    expected: IsolationExpectations
    extraParameters: _list[ExtraParameter]
    locationData: _list[LocationData]
    parentAsset: _list[CloudAsset]

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BlobstoreLocation(typing_extensions.TypedDict, total=False):
    policyId: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloudAsset(typing_extensions.TypedDict, total=False):
    assetName: str
    assetType: str

@typing.type_check_only
class CloudAssetComposition(typing_extensions.TypedDict, total=False):
    childAsset: _list[CloudAsset]

@typing.type_check_only
class CryptoKeyConfig(typing_extensions.TypedDict, total=False):
    keyReference: str

@typing.type_check_only
class DirectLocationAssignment(typing_extensions.TypedDict, total=False):
    location: _list[LocationAssignment]

@typing.type_check_only
class DnsPeering(typing_extensions.TypedDict, total=False):
    description: str
    domain: str
    name: str
    targetNetwork: str
    targetProject: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EventPublishConfig(typing_extensions.TypedDict, total=False):
    enabled: bool
    topic: str

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class ExtraParameter(typing_extensions.TypedDict, total=False):
    regionalMigDistributionPolicy: RegionalMigDistributionPolicy

@typing.type_check_only
class IAMPolicy(typing_extensions.TypedDict, total=False):
    policy: Policy
    status: Status

@typing.type_check_only
class Instance(typing_extensions.TypedDict, total=False):
    accelerators: _list[Accelerator]
    apiEndpoint: str
    availableVersion: _list[Version]
    createTime: str
    cryptoKeyConfig: CryptoKeyConfig
    dataplexDataLineageIntegrationEnabled: bool
    dataprocServiceAccount: str
    description: str
    disabledReason: _list[
        typing_extensions.Literal["DISABLED_REASON_UNSPECIFIED", "KMS_KEY_ISSUE"]
    ]
    displayName: str
    enableRbac: bool
    enableStackdriverLogging: bool
    enableStackdriverMonitoring: bool
    enableZoneSeparation: bool
    eventPublishConfig: EventPublishConfig
    gcsBucket: str
    labels: dict[str, typing.Any]
    maintenancePolicy: MaintenancePolicy
    name: str
    networkConfig: NetworkConfig
    options: dict[str, typing.Any]
    p4ServiceAccount: str
    patchRevision: str
    privateInstance: bool
    satisfiesPzs: bool
    serviceAccount: str
    serviceEndpoint: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "RUNNING",
        "FAILED",
        "DELETING",
        "UPGRADING",
        "RESTARTING",
        "UPDATING",
        "AUTO_UPDATING",
        "AUTO_UPGRADING",
        "DISABLED",
    ]
    stateMessage: str
    tenantProjectId: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "BASIC", "ENTERPRISE", "DEVELOPER"
    ]
    updateTime: str
    version: str
    workforceIdentityServiceEndpoint: str
    zone: str

@typing.type_check_only
class IsolationExpectations(typing_extensions.TypedDict, total=False):
    ziOrgPolicy: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    ziRegionPolicy: typing_extensions.Literal[
        "ZI_REGION_POLICY_UNSPECIFIED",
        "ZI_REGION_POLICY_UNKNOWN",
        "ZI_REGION_POLICY_NOT_SET",
        "ZI_REGION_POLICY_FAIL_OPEN",
        "ZI_REGION_POLICY_FAIL_CLOSED",
    ]
    ziRegionState: typing_extensions.Literal[
        "ZI_REGION_UNSPECIFIED",
        "ZI_REGION_UNKNOWN",
        "ZI_REGION_NOT_ENABLED",
        "ZI_REGION_ENABLED",
    ]
    zoneIsolation: typing_extensions.Literal[
        "ZI_UNSPECIFIED", "ZI_UNKNOWN", "ZI_NOT_REQUIRED", "ZI_PREFERRED", "ZI_REQUIRED"
    ]
    zoneSeparation: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsOrgPolicy: typing_extensions.Literal[
        "ZS_UNSPECIFIED", "ZS_UNKNOWN", "ZS_NOT_REQUIRED", "ZS_REQUIRED"
    ]
    zsRegionState: typing_extensions.Literal[
        "ZS_REGION_UNSPECIFIED",
        "ZS_REGION_UNKNOWN",
        "ZS_REGION_NOT_ENABLED",
        "ZS_REGION_ENABLED",
    ]

@typing.type_check_only
class ListAvailableVersionsResponse(typing_extensions.TypedDict, total=False):
    availableVersions: _list[Version]
    nextPageToken: str

@typing.type_check_only
class ListDnsPeeringsResponse(typing_extensions.TypedDict, total=False):
    dnsPeerings: _list[DnsPeering]
    nextPageToken: str

@typing.type_check_only
class ListInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[Instance]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListNamespacesResponse(typing_extensions.TypedDict, total=False):
    namespaces: _list[Namespace]
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
class LocationAssignment(typing_extensions.TypedDict, total=False):
    location: str
    locationType: typing_extensions.Literal[
        "UNSPECIFIED",
        "CLUSTER",
        "POP",
        "CLOUD_ZONE",
        "CLOUD_REGION",
        "MULTI_REGION_GEO",
        "MULTI_REGION_JURISDICTION",
        "GLOBAL",
        "OTHER",
    ]

@typing.type_check_only
class LocationData(typing_extensions.TypedDict, total=False):
    blobstoreLocation: BlobstoreLocation
    childAssetLocation: CloudAssetComposition
    directLocation: DirectLocationAssignment
    gcpProjectProxy: TenantProjectProxy
    placerLocation: PlacerLocation
    spannerLocation: SpannerLocation

@typing.type_check_only
class MaintenancePolicy(typing_extensions.TypedDict, total=False):
    maintenanceExclusionWindow: TimeWindow
    maintenanceWindow: MaintenanceWindow

@typing.type_check_only
class MaintenanceWindow(typing_extensions.TypedDict, total=False):
    recurringTimeWindow: RecurringTimeWindow

@typing.type_check_only
class Namespace(typing_extensions.TypedDict, total=False):
    iamPolicy: IAMPolicy
    name: str

@typing.type_check_only
class NetworkConfig(typing_extensions.TypedDict, total=False):
    connectionType: typing_extensions.Literal[
        "CONNECTION_TYPE_UNSPECIFIED",
        "VPC_PEERING",
        "PRIVATE_SERVICE_CONNECT_INTERFACES",
    ]
    ipAllocation: str
    network: str
    privateServiceConnectConfig: PrivateServiceConnectConfig

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    additionalStatus: dict[str, typing.Any]
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class PlacerLocation(typing_extensions.TypedDict, total=False):
    placerConfig: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class PrivateServiceConnectConfig(typing_extensions.TypedDict, total=False):
    effectiveUnreachableCidrBlock: str
    networkAttachment: str
    unreachableCidrBlock: str

@typing.type_check_only
class RecurringTimeWindow(typing_extensions.TypedDict, total=False):
    recurrence: str
    window: TimeWindow

@typing.type_check_only
class RegionalMigDistributionPolicy(typing_extensions.TypedDict, total=False):
    targetShape: int
    zones: _list[ZoneConfiguration]

@typing.type_check_only
class RemoveIamPolicyRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveIamPolicyResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RestartInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SpannerLocation(typing_extensions.TypedDict, total=False):
    backupName: _list[str]
    dbName: _list[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TenantProjectProxy(typing_extensions.TypedDict, total=False):
    projectNumbers: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TimeWindow(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UpgradeInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    availableFeatures: _list[str]
    defaultVersion: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "TYPE_PREVIEW", "TYPE_GENERAL_AVAILABILITY"
    ]
    versionNumber: str

@typing.type_check_only
class ZoneConfiguration(typing_extensions.TypedDict, total=False):
    zone: str
