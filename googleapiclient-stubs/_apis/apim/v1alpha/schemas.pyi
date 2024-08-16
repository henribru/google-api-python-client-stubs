import typing

import typing_extensions

_list = list

@typing.type_check_only
class ApiObservation(typing_extensions.TypedDict, total=False):
    apiOperationCount: str
    createTime: str
    hostname: str
    lastEventDetectedTime: str
    name: str
    serverIps: _list[str]
    sourceLocations: _list[str]
    style: typing_extensions.Literal["STYLE_UNSPECIFIED", "REST", "GRPC", "GRAPHQL"]
    tags: _list[str]
    updateTime: str

@typing.type_check_only
class ApiOperation(typing_extensions.TypedDict, total=False):
    count: str
    firstSeenTime: str
    httpOperation: HttpOperation
    lastSeenTime: str
    name: str

@typing.type_check_only
class BatchEditTagsApiObservationsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[EditTagsApiObservationsRequest]

@typing.type_check_only
class BatchEditTagsApiObservationsResponse(typing_extensions.TypedDict, total=False):
    apiObservations: _list[ApiObservation]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DisableObservationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EditTagsApiObservationsRequest(typing_extensions.TypedDict, total=False):
    apiObservationId: str
    tagActions: _list[TagAction]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EnableObservationJobRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GclbObservationSource(typing_extensions.TypedDict, total=False):
    pscNetworkConfigs: _list[GclbObservationSourcePscNetworkConfig]

@typing.type_check_only
class GclbObservationSourcePscNetworkConfig(typing_extensions.TypedDict, total=False):
    network: str
    subnetwork: str

@typing.type_check_only
class HttpOperation(typing_extensions.TypedDict, total=False):
    method: typing_extensions.Literal[
        "HTTP_METHOD_UNSPECIFIED",
        "GET",
        "HEAD",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "TRACE",
        "OPTIONS",
        "CONNECT",
    ]
    path: str
    pathParams: _list[HttpOperationPathParam]
    queryParams: dict[str, typing.Any]
    request: HttpOperationHttpRequest
    response: HttpOperationHttpResponse

@typing.type_check_only
class HttpOperationHeader(typing_extensions.TypedDict, total=False):
    count: str
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    name: str

@typing.type_check_only
class HttpOperationHttpRequest(typing_extensions.TypedDict, total=False):
    headers: dict[str, typing.Any]

@typing.type_check_only
class HttpOperationHttpResponse(typing_extensions.TypedDict, total=False):
    headers: dict[str, typing.Any]
    responseCodes: dict[str, typing.Any]

@typing.type_check_only
class HttpOperationPathParam(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    position: int

@typing.type_check_only
class HttpOperationQueryParam(typing_extensions.TypedDict, total=False):
    count: str
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED", "BOOL", "INTEGER", "FLOAT", "STRING", "UUID"
    ]
    name: str

@typing.type_check_only
class ListApiObservationTagsResponse(typing_extensions.TypedDict, total=False):
    apiObservationTags: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListApiObservationsResponse(typing_extensions.TypedDict, total=False):
    apiObservations: _list[ApiObservation]
    nextPageToken: str

@typing.type_check_only
class ListApiOperationsResponse(typing_extensions.TypedDict, total=False):
    apiOperations: _list[ApiOperation]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListObservationJobsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    observationJobs: _list[ObservationJob]
    unreachable: _list[str]

@typing.type_check_only
class ListObservationSourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    observationSources: _list[ObservationSource]
    unreachable: _list[str]

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
class ObservationJob(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    sources: _list[str]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "CREATING",
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
        "DELETING",
        "ERROR",
    ]
    updateTime: str

@typing.type_check_only
class ObservationSource(typing_extensions.TypedDict, total=False):
    createTime: str
    gclbObservationSource: GclbObservationSource
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "CREATING", "CREATED", "DELETING", "ERROR"
    ]
    updateTime: str

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
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TagAction(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ADD", "REMOVE"]
    tag: str
