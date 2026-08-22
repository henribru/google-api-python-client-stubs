import typing

_list = list

@typing.type_check_only
class Bucket(typing.TypedDict, total=False):
    cmekSettings: CmekSettings
    createTime: str
    deleteTime: str
    description: str
    displayName: str
    name: str
    purgeTime: str
    updateTime: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CmekSettings(typing.TypedDict, total=False):
    kmsKey: str
    kmsKeyVersion: str
    serviceAccountId: str

@typing.type_check_only
class Dataset(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    description: str
    displayName: str
    name: str
    purgeTime: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str

@typing.type_check_only
class ListBucketsResponse(typing.TypedDict, total=False):
    buckets: _list[Bucket]
    nextPageToken: str

@typing.type_check_only
class ListDatasetsResponse(typing.TypedDict, total=False):
    datasets: _list[Dataset]
    nextPageToken: str

@typing.type_check_only
class ListLinksResponse(typing.TypedDict, total=False):
    links: _list[Link]
    nextPageToken: str

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
class ListTraceScopesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    traceScopes: _list[TraceScope]

@typing.type_check_only
class ListViewsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    views: _list[View]

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
class Scope(typing.TypedDict, total=False):
    logScope: str
    name: str
    traceScope: str
    updateTime: str

@typing.type_check_only
class Settings(typing.TypedDict, total=False):
    defaultStorageLocation: str
    kmsKeyName: str
    name: str
    serviceAccountId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TraceScope(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    resourceNames: _list[str]
    updateTime: str

@typing.type_check_only
class View(typing.TypedDict, total=False):
    createTime: str
    description: str
    displayName: str
    name: str
    updateTime: str
