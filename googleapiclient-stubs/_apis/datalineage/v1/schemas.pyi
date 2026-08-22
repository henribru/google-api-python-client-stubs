import typing

_list = list

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1Config(
    typing.TypedDict, total=False
):
    etag: str
    ingestion: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestion
    name: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestion(
    typing.TypedDict, total=False
):
    rules: _list[
        GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRule
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRule(
    typing.TypedDict, total=False
):
    integrationSelector: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleIntegrationSelector
    lineageEnablement: GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleLineageEnablement

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleIntegrationSelector(
    typing.TypedDict, total=False
):
    integration: typing.Literal[
        "INTEGRATION_UNSPECIFIED",
        "BIGQUERY",
        "DATAPROC",
        "LOOKER_CORE",
        "MANAGED_AIRFLOW",
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageConfigmanagementV1ConfigIngestionIngestionRuleLineageEnablement(
    typing.TypedDict, total=False
):
    enabled: bool

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesRequest(
    typing.TypedDict, total=False
):
    links: _list[str]
    pageSize: int
    pageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1BatchSearchLinkProcessesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    processLinks: _list[GoogleCloudDatacatalogLineageV1ProcessLinks]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1DependencyInfo(typing.TypedDict, total=False):
    dependencyType: typing.Literal["DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EntityReference(typing.TypedDict, total=False):
    field: _list[str]
    fullyQualifiedName: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1EventLink(typing.TypedDict, total=False):
    dependencyInfo: GoogleCloudDatacatalogLineageV1DependencyInfo
    source: GoogleCloudDatacatalogLineageV1EntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageEvent(typing.TypedDict, total=False):
    endTime: str
    links: _list[GoogleCloudDatacatalogLineageV1EventLink]
    name: str
    startTime: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageLink(typing.TypedDict, total=False):
    dependencyInfo: _list[GoogleCloudDatacatalogLineageV1LineageLinkDependencyInfo]
    depth: int
    location: str
    processes: _list[GoogleCloudDatacatalogLineageV1LineageLinkLineageProcess]
    source: GoogleCloudDatacatalogLineageV1EntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageLinkDependencyInfo(
    typing.TypedDict, total=False
):
    dependencyType: typing.Literal["DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LineageLinkLineageProcess(
    typing.TypedDict, total=False
):
    process: GoogleCloudDatacatalogLineageV1Process

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Link(typing.TypedDict, total=False):
    dependencyInfo: _list[GoogleCloudDatacatalogLineageV1LinkDependencyInfo]
    endTime: str
    name: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    startTime: str
    target: GoogleCloudDatacatalogLineageV1EntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1LinkDependencyInfo(typing.TypedDict, total=False):
    dependencyType: typing.Literal["DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListLineageEventsResponse(
    typing.TypedDict, total=False
):
    lineageEvents: _list[GoogleCloudDatacatalogLineageV1LineageEvent]
    nextPageToken: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListProcessesResponse(
    typing.TypedDict, total=False
):
    nextPageToken: str
    processes: _list[GoogleCloudDatacatalogLineageV1Process]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ListRunsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    runs: _list[GoogleCloudDatacatalogLineageV1Run]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1MultipleEntityReference(
    typing.TypedDict, total=False
):
    entities: _list[GoogleCloudDatacatalogLineageV1EntityReference]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1OperationMetadata(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    operationType: typing.Literal["TYPE_UNSPECIFIED", "DELETE", "CREATE"]
    resource: str
    resourceUuid: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Origin(typing.TypedDict, total=False):
    name: str
    sourceType: typing.Literal[
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
class GoogleCloudDatacatalogLineageV1Process(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    displayName: str
    name: str
    origin: GoogleCloudDatacatalogLineageV1Origin

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessLinkInfo(typing.TypedDict, total=False):
    endTime: str
    link: str
    startTime: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessLinks(typing.TypedDict, total=False):
    links: _list[GoogleCloudDatacatalogLineageV1ProcessLinkInfo]
    process: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1ProcessOpenLineageRunEventResponse(
    typing.TypedDict, total=False
):
    lineageEvents: _list[str]
    process: str
    run: str

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1Run(typing.TypedDict, total=False):
    attributes: dict[str, typing.Any]
    displayName: str
    endTime: str
    name: str
    startTime: str
    state: typing.Literal["UNKNOWN", "STARTED", "COMPLETED", "FAILED", "ABORTED"]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequest(
    typing.TypedDict, total=False
):
    direction: typing.Literal["SEARCH_DIRECTION_UNSPECIFIED", "DOWNSTREAM", "UPSTREAM"]
    filters: GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchFilters
    limits: GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchLimits
    locations: _list[str]
    rootCriteria: (
        GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestRootCriteria
    )

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestRootCriteria(
    typing.TypedDict, total=False
):
    entities: GoogleCloudDatacatalogLineageV1MultipleEntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchFilters(
    typing.TypedDict, total=False
):
    dependencyTypes: _list[
        typing.Literal["DEPENDENCY_TYPE_UNSPECIFIED", "EXACT_COPY", "OTHER"]
    ]
    entitySet: typing.Literal["ENTITY_SET_UNSPECIFIED", "ENTITIES"]
    timeRange: GoogleTypeInterval

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingRequestSearchLimits(
    typing.TypedDict, total=False
):
    maxDepth: int
    maxProcessPerLink: int
    maxResults: int

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLineageStreamingResponse(
    typing.TypedDict, total=False
):
    links: _list[GoogleCloudDatacatalogLineageV1LineageLink]
    unreachable: _list[str]

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksRequest(typing.TypedDict, total=False):
    pageSize: int
    pageToken: str
    source: GoogleCloudDatacatalogLineageV1EntityReference
    sources: GoogleCloudDatacatalogLineageV1MultipleEntityReference
    target: GoogleCloudDatacatalogLineageV1EntityReference
    targets: GoogleCloudDatacatalogLineageV1MultipleEntityReference

@typing.type_check_only
class GoogleCloudDatacatalogLineageV1SearchLinksResponse(typing.TypedDict, total=False):
    links: _list[GoogleCloudDatacatalogLineageV1Link]
    nextPageToken: str

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
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class GoogleTypeInterval(typing.TypedDict, total=False):
    endTime: str
    startTime: str
