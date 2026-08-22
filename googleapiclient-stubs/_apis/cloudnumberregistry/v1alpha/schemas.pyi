import typing

_list = list

@typing.type_check_only
class AggregatedData(typing.TypedDict, total=False):
    customRangesCount: int
    customRealmsCount: int
    discoveredRangesCount: int
    discoveredRealmsCount: int
    uniqueScopesCount: int

@typing.type_check_only
class Attribute(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckAvailabilityIpamAdminScopesResponse(typing.TypedDict, total=False):
    scopeAvailabilities: _list[IpamAdminScopeAvailability]

@typing.type_check_only
class CleanupIpamAdminScopeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class CustomRange(typing.TypedDict, total=False):
    attributes: _list[Attribute]
    description: str
    ipv4CidrRange: str
    ipv6CidrRange: str
    labels: dict[str, typing.Any]
    name: str
    parentRange: str
    realm: str
    registryBook: str

@typing.type_check_only
class DisableIpamAdminScopeRequest(typing.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class DiscoveredRange(typing.TypedDict, total=False):
    attributes: _list[Attribute]
    childCidrOverlapAllowed: bool
    createTime: str
    description: str
    discoveryMetadata: DiscoveryMetadata
    ipv4CidrRange: str
    ipv6CidrRange: str
    labels: dict[str, typing.Any]
    name: str
    parentRange: str
    realm: str
    registryBook: str
    updateTime: str

@typing.type_check_only
class DiscoveryMetadata(typing.TypedDict, total=False):
    createTime: str
    eventTime: str
    resource: str
    resourceUri: str
    sourceId: str
    sourceSubId: str
    state: typing.Literal[
        "RESOURCE_STATE_UNSPECIFIED", "INVALID", "EXISTS", "DOES_NOT_EXIST", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FindCustomRangeFreeIpRangesResponse(typing.TypedDict, total=False):
    freeIpCidrRanges: _list[str]

@typing.type_check_only
class FindDiscoveredRangeFreeIpRangesResponse(typing.TypedDict, total=False):
    freeIpCidrRanges: _list[str]

@typing.type_check_only
class IpamAdminScope(typing.TypedDict, total=False):
    createTime: str
    enabledAddonPlatforms: _list[
        typing.Literal["ADD_ON_PLATFORM_UNSPECIFIED", "COMPUTE_ENGINE", "GCE"]
    ]
    labels: dict[str, typing.Any]
    name: str
    scopes: _list[str]
    state: typing.Literal[
        "DISCOVERY_PIPELINE_STATE_UNSPECIFIED",
        "INTERNAL_FAILURE",
        "FAILED",
        "SETUP_IN_PROGRESS",
        "READY_FOR_USE",
        "DELETING_IN_PROGRESS",
        "UPDATING",
        "RECOVERING",
        "DISABLED",
        "DELETION_COMPLETED",
        "CLEANUP_IN_PROGRESS",
        "READY_FOR_DELETION",
    ]
    updateTime: str

@typing.type_check_only
class IpamAdminScopeAvailability(typing.TypedDict, total=False):
    adminProject: str
    availability: typing.Literal["AVAILABILITY_UNSPECIFIED", "AVAILABLE", "UNAVAILABLE"]
    scope: str

@typing.type_check_only
class ListCustomRangesResponse(typing.TypedDict, total=False):
    customRanges: _list[CustomRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredRangesResponse(typing.TypedDict, total=False):
    discoveredRanges: _list[DiscoveredRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListIpamAdminScopesResponse(typing.TypedDict, total=False):
    ipamAdminScopes: _list[IpamAdminScope]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListRealmsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    realms: _list[Realm]
    unreachable: _list[str]

@typing.type_check_only
class ListRegistryBooksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    registryBooks: _list[RegistryBook]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

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
class Range(typing.TypedDict, total=False):
    customRange: CustomRange
    discoveredRange: DiscoveredRange
    utilization: RangeUtilization

@typing.type_check_only
class RangeUtilization(typing.TypedDict, total=False):
    totalConsumed: str
    totalProduced: str
    usage: float

@typing.type_check_only
class Realm(typing.TypedDict, total=False):
    aggregatedData: RealmAggregatedData
    createTime: str
    discoveryMetadata: DiscoveryMetadata
    ipVersion: typing.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    labels: dict[str, typing.Any]
    managementType: typing.Literal["MANAGEMENT_TYPE_UNSPECIFIED", "CNR", "USER"]
    name: str
    registryBook: str
    trafficType: typing.Literal[
        "TRAFFIC_TYPE_UNSPECIFIED", "UNSET", "INTERNET", "PRIVATE", "LINKLOCAL"
    ]
    updateTime: str

@typing.type_check_only
class RealmAggregatedData(typing.TypedDict, total=False):
    customRangesCount: int
    discoveredRangesCount: int

@typing.type_check_only
class RegistryBook(typing.TypedDict, total=False):
    aggregatedData: AggregatedData
    claimedScopes: _list[str]
    createTime: str
    isDefault: bool
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class SearchIpResourcesRequest(typing.TypedDict, total=False):
    orderBy: str
    pageSize: int
    pageToken: str
    query: str
    searchResourceTypes: _list[
        typing.Literal["SEARCH_RESOURCE_TYPE_UNSPECIFIED", "RANGES", "REALMS"]
    ]
    showUtilization: bool

@typing.type_check_only
class SearchIpResourcesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    ranges: _list[Range]
    results: _list[SearchIpResourcesResult]
    unreachable: _list[str]

@typing.type_check_only
class SearchIpResourcesResult(typing.TypedDict, total=False):
    range: Range
    realm: Realm

@typing.type_check_only
class ShowCustomRangeUtilizationResponse(typing.TypedDict, total=False):
    customRange: CustomRange
    rangeUtilization: RangeUtilization

@typing.type_check_only
class ShowDiscoveredRangeUtilizationResponse(typing.TypedDict, total=False):
    discoveredRange: DiscoveredRange
    rangeUtilization: RangeUtilization

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
