import typing

_list = list

@typing.type_check_only
class AllocationOptions(typing.TypedDict, total=False):
    allocationStrategy: typing.Literal[
        "ALLOCATION_STRATEGY_UNSPECIFIED",
        "RANDOM",
        "FIRST_AVAILABLE",
        "RANDOM_FIRST_N_AVAILABLE",
        "FIRST_SMALLEST_FITTING",
    ]
    firstAvailableRangesLookupSize: int

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]
    unreachable: _list[str]

@typing.type_check_only
class GoogleLongrunningOperation(typing.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Hub(typing.TypedDict, total=False):
    createTime: str
    description: str
    labels: dict[str, typing.Any]
    name: str
    spokes: _list[str]
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING", "FAILED"
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class InternalRange(typing.TypedDict, total=False):
    allocationOptions: AllocationOptions
    createTime: str
    description: str
    excludeCidrRanges: _list[str]
    immutable: bool
    ipCidrRange: str
    labels: dict[str, typing.Any]
    migration: Migration
    name: str
    network: str
    overlaps: _list[
        typing.Literal[
            "OVERLAP_UNSPECIFIED",
            "OVERLAP_ROUTE_RANGE",
            "OVERLAP_EXISTING_SUBNET_RANGE",
        ]
    ]
    peering: typing.Literal["PEERING_UNSPECIFIED", "FOR_SELF", "FOR_PEER", "NOT_SHARED"]
    prefixLength: int
    rangeStatus: typing.Literal[
        "RANGE_STATUS_UNSPECIFIED", "ACTIVE", "OBSOLETE", "CREATING", "DELETING"
    ]
    targetCidrRange: _list[str]
    updateTime: str
    usage: typing.Literal[
        "USAGE_UNSPECIFIED", "FOR_VPC", "EXTERNAL_TO_VPC", "FOR_MIGRATION"
    ]
    users: _list[str]

@typing.type_check_only
class ListHubsResponse(typing.TypedDict, total=False):
    hubs: _list[Hub]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListInternalRangesResponse(typing.TypedDict, total=False):
    internalRanges: _list[InternalRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListSpokesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    spokes: _list[Spoke]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Migration(typing.TypedDict, total=False):
    source: str
    target: str

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RouterApplianceInstance(typing.TypedDict, total=False):
    ipAddress: str
    networkInterface: str
    virtualMachine: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Spoke(typing.TypedDict, total=False):
    createTime: str
    description: str
    hub: str
    labels: dict[str, typing.Any]
    linkedInterconnectAttachments: _list[str]
    linkedRouterApplianceInstances: _list[RouterApplianceInstance]
    linkedVpnTunnels: _list[str]
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "CREATING", "ACTIVE", "DELETING", "UPDATING", "FAILED"
    ]
    uniqueId: str
    updateTime: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]
