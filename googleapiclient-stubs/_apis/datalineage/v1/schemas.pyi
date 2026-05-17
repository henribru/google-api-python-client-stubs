import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1Config(
    typing_extensions.TypedDict, total=False
):
    etag: str
    ingestion: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestion
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestion(
    typing_extensions.TypedDict, total=False
):
    rules: _list[
        GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRule
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRule(
    typing_extensions.TypedDict, total=False
):
    integrationSelector: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleIntegrationSelector
    lineageEnablement: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleLineageEnablement

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleIntegrationSelector(
    typing_extensions.TypedDict, total=False
):
    integration: typing_extensions.Literal[
        "INTEGRATION_UNSPECIFIED", "DATAPROC", "LOOKER_CORE"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleLineageEnablement(
    typing_extensions.TypedDict, total=False
):
    enabled: bool

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
class GoogleCloudDatacatalogLineageV1DependencyInfo(
    typing_extensions.TypedDict, total=False
):
    dependencyType: typing_extensions.Literal[
        "DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EntityReference(
    typing_extensions.TypedDict, total=False
):
    field: _list[str]
    fullyQualifiedName: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EventLink(
    typing_extensions.TypedDict, total=False
):
    dependencyInfo: GoogleCloudDatacatalogLineageV1DependencyInfo
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
class GoogleCloudDatacatalogLineageV1LineageLink(
    typing_extensions.TypedDict, total=False
):
    dependencyInfo: _list[GoogleCloudDatacatalogLineageV1LineageLinkDependencyInfo]
    depth: int
    location: str
    processes: _list[GoogleCloudDatacatalogLineageV1LineageLinkLineageProcess]
    source: GoogleCloudDatacatalogLineageV1EntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageLinkDependencyInfo(
    typing_extensions.TypedDict, total=False
):
    dependencyType: typing_extensions.Literal[
        "DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageLinkLineageProcess(
    typing_extensions.TypedDict, total=False
):
    process: GoogleCloudDatacatalogLineageV1Process

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Link(typing_extensions.TypedDict, total=False):
    dependencyInfo: _list[GoogleCloudDatacatalogLineageV1LinkDependencyInfo]
    endTime: str
    name: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    startTime: str
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LinkDependencyInfo(
    typing_extensions.TypedDict, total=False
):
    dependencyType: typing_extensions.Literal[
        "DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"
    ]

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
class GoogleCloudDatacatalogLineageV1MultipleEntityReference(
    typing_extensions.TypedDict, total=False
):
    entities: _list[GoogleCloudDatacatalogLineageV1EntityReference]

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
        "DATAFLOW",
        "LOOKER_CORE",
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
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest(
    typing_extensions.TypedDict, total=False
):
    direction: typing_extensions.Literal[
        "SEARCH_DIRECTION_UNSPECIFIED", "DOWNSTREAM", "UPSTREAM"
    ]
    filters: GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchFilters
    limits: GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchLimits
    locations: _list[str]
    rootCriteria: (
        GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestRootCriteria
    )

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestRootCriteria(
    typing_extensions.TypedDict, total=False
):
    entities: GoogleCloudDatacatalogLineageV1MultipleEntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchFilters(
    typing_extensions.TypedDict, total=False
):
    dependencyTypes: _list[
        typing_extensions.Literal["DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"]
    ]
    entitySet: typing_extensions.Literal["ENTITY_SET_UNSPECIFIED", "ENTITIES"]
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchLimits(
    typing_extensions.TypedDict, total=False
):
    maxDepth: int
    maxProcessPerLink: int
    maxResults: int

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingResponse(
    typing_extensions.TypedDict, total=False
):
    links: _list[GoogleCloudDatacatalogLineageV1LineageLink]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksRequest(
    typing_extensions.TypedDict, total=False
):
    pageSize: int
    pageToken: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    sources: GoogleCloudDatacatalogLineageV1MultipleEntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference
    targets: GoogleCloudDatacatalogLineageV1MultipleEntityReference

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
    unreachable: _list[str]

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

@typing.type_check_only
class GoogleTypeInterval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
