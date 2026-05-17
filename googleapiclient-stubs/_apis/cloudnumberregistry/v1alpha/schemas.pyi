import typing

import typing_extensions

_list = list

@typing.type_check_only
class AggregatedData(typing_extensions.TypedDict, total=False):
    customRangesCount: int
    customRealmsCount: int
    discoveredRangesCount: int
    discoveredRealmsCount: int
    uniqueScopesCount: int

@typing.type_check_only
class Attribute(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckAvailabilityIpamAdminScopesResponse(
    typing_extensions.TypedDict, total=False
):
    scopeAvailabilities: _list[IpamAdminScopeAvailability]

@typing.type_check_only
class CleanupIpamAdminScopeRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class CustomRange(typing_extensions.TypedDict, total=False):
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
class DisableIpamAdminScopeRequest(typing_extensions.TypedDict, total=False):
    requestId: str

@typing.type_check_only
class DiscoveredRange(typing_extensions.TypedDict, total=False):
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
class DiscoveryMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    eventTime: str
    resource: str
    resourceUri: str
    sourceId: str
    sourceSubId: str
    state: typing_extensions.Literal[
        "RESOURCE_STATE_UNSPECIFIED", "INVALID", "EXISTS", "DOES_NOT_EXIST", "ERROR"
    ]
    updateTime: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FindCustomRangeFreeIpRangesResponse(typing_extensions.TypedDict, total=False):
    freeIpCidrRanges: _list[str]

@typing.type_check_only
class FindDiscoveredRangeFreeIpRangesResponse(typing_extensions.TypedDict, total=False):
    freeIpCidrRanges: _list[str]

@typing.type_check_only
class IpamAdminScope(typing_extensions.TypedDict, total=False):
    createTime: str
    enabledAddonPlatforms: _list[
        typing_extensions.Literal[
            "ADD_ON_PLATFORM_UNSPECIFIED", "COMPUTE_ENGINE", "GCE"
        ]
    ]
    labels: dict[str, typing.Any]
    name: str
    scopes: _list[str]
    state: typing_extensions.Literal[
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
class IpamAdminScopeAvailability(typing_extensions.TypedDict, total=False):
    adminProject: str
    availability: typing_extensions.Literal[
        "AVAILABILITY_UNSPECIFIED", "AVAILABLE", "UNAVAILABLE"
    ]
    scope: str

@typing.type_check_only
class ListCustomRangesResponse(typing_extensions.TypedDict, total=False):
    customRanges: _list[CustomRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListDiscoveredRangesResponse(typing_extensions.TypedDict, total=False):
    discoveredRanges: _list[DiscoveredRange]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListIpamAdminScopesResponse(typing_extensions.TypedDict, total=False):
    ipamAdminScopes: _list[IpamAdminScope]
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
    unreachable: _list[str]

@typing.type_check_only
class ListRealmsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    realms: _list[Realm]
    unreachable: _list[str]

@typing.type_check_only
class ListRegistryBooksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    registryBooks: _list[RegistryBook]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

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
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Range(typing_extensions.TypedDict, total=False):
    customRange: CustomRange
    discoveredRange: DiscoveredRange
    utilization: RangeUtilization

@typing.type_check_only
class RangeUtilization(typing_extensions.TypedDict, total=False):
    totalConsumed: str
    totalProduced: str
    usage: float

@typing.type_check_only
class Realm(typing_extensions.TypedDict, total=False):
    aggregatedData: RealmAggregatedData
    createTime: str
    discoveryMetadata: DiscoveryMetadata
    ipVersion: typing_extensions.Literal["IP_VERSION_UNSPECIFIED", "IPV4", "IPV6"]
    labels: dict[str, typing.Any]
    managementType: typing_extensions.Literal[
        "MANAGEMENT_TYPE_UNSPECIFIED", "CNR", "USER"
    ]
    name: str
    registryBook: str
    trafficType: typing_extensions.Literal[
        "TRAFFIC_TYPE_UNSPECIFIED", "UNSET", "INTERNET", "PRIVATE", "LINKLOCAL"
    ]
    updateTime: str

@typing.type_check_only
class RealmAggregatedData(typing_extensions.TypedDict, total=False):
    customRangesCount: int
    discoveredRangesCount: int

@typing.type_check_only
class RegistryBook(typing_extensions.TypedDict, total=False):
    aggregatedData: AggregatedData
    claimedScopes: _list[str]
    createTime: str
    isDefault: bool
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class SearchIpResourcesRequest(typing_extensions.TypedDict, total=False):
    orderBy: str
    pageSize: int
    pageToken: str
    query: str
    searchResourceTypes: _list[
        typing_extensions.Literal[
            "SEARCH_RESOURCE_TYPE_UNSPECIFIED", "RANGES", "REALMS"
        ]
    ]
    showUtilization: bool

@typing.type_check_only
class SearchIpResourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    ranges: _list[Range]
    results: _list[SearchIpResourcesResult]
    unreachable: _list[str]

@typing.type_check_only
class SearchIpResourcesResult(typing_extensions.TypedDict, total=False):
    range: Range
    realm: Realm

@typing.type_check_only
class ShowCustomRangeUtilizationResponse(typing_extensions.TypedDict, total=False):
    customRange: CustomRange
    rangeUtilization: RangeUtilization

@typing.type_check_only
class ShowDiscoveredRangeUtilizationResponse(typing_extensions.TypedDict, total=False):
    discoveredRange: DiscoveredRange
    rangeUtilization: RangeUtilization

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
