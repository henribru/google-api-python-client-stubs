import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequest(
    typing_extensions.TypedDict, total=False
):
    links: _list[str]
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    processLinks: _list[GoogleCloudDatacatalogLineageV1ProcessLinks]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EntityReference(
    typing_extensions.TypedDict, total=False
):
    fullyQualifiedName: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EventLink(
    typing_extensions.TypedDict, total=False
):
    source: GoogleCloudDatacatalogLineageV1EntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageEvent(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    links: _list[GoogleCloudDatacatalogLineageV1EventLink]
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Link(typing_extensions.TypedDict, total=False):
    endTime: str
    name: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    startTime: str
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListLineageEventsResponse(
    typing_extensions.TypedDict, total=False
):
    lineageEvents: _list[GoogleCloudDatacatalogLineageV1LineageEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListProcessesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    processes: _list[GoogleCloudDatacatalogLineageV1Process]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListRunsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    runs: _list[GoogleCloudDatacatalogLineageV1Run]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1OperationMetadata(
    typing_extensions.TypedDict, total=False
):
    createTime: str
    endTime: str
    operationType: typing_extensions.Literal["TYPE_UNSPECIFIED", "DELETE", "CREATE"]
    resource: str
    resourceUuid: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Origin(typing_extensions.TypedDict, total=False):
    name: str
    sourceType: typing_extensions.Literal[
        "SOURCE_TYPE_UNSPECIFIED",
        "CUSTOM",
        "BIGQUERY",
        "DATA_FUSION",
        "COMPOSER",
        "LOOKER_STUDIO",
        "DATAPROC",
        "VERTEX_AI",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Process(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    displayName: str
    name: str
    origin: GoogleCloudDatacatalogLineageV1Origin

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessLinkInfo(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    link: str
    startTime: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessLinks(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudDatacatalogLineageV1ProcessLinkInfo]
    process: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessOpenLineageRunEventResponse(
    typing_extensions.TypedDict, total=False
):
    lineageEvents: _list[str]
    process: str
    run: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Run(typing_extensions.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    displayName: str
    endTime: str
    name: str
    startTime: str
    state: typing_extensions.Literal[
        "UNKNOWN", "STARTED", "COMPLETED", "FAILED", "ABORTED"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksResponse(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudDatacatalogLineageV1Link]
    nextPageToken: str

@typing.type_check_only
class GoogleLongrunningCancelOperationRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
