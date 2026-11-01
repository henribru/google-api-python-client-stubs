import typing

_list = list

@typing.type_check_only
class AnchoredReviewComment(typing.TypedDict, total=False):
    bodyMarkdown: str
    citationReport: CitationReport
    commentId: str
    location: DocumentLocation
    severity: typing.Literal[
        "SEVERITY_UNSPECIFIED", "CRITICAL", "MAJOR", "MINOR", "SUGGESTION"
    ]
    suggestedEdit: str
    summary: str

@typing.type_check_only
class Author(typing.TypedDict, total=False):
    familyName: str
    givenName: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CitationMetadata(typing.TypedDict, total=False):
    authors: _list[Author]
    doi: str
    journal: str
    pages: str
    publicationDate: Date
    source: str
    title: str
    urls: _list[str]
    volume: str

@typing.type_check_only
class CitationReport(typing.TypedDict, total=False):
    citationKey: str
    entryType: str
    extractedMetadata: CitationMetadata
    fieldComparisons: _list[FieldComparison]
    finalVerdict: typing.Literal[
        "VERDICT_UNSPECIFIED",
        "OK",
        "MINOR_MISMATCH",
        "MAJOR_MISMATCH",
        "VERIFIED_BY_SEARCH",
        "NOT_FOUND",
        "HALLUCINATED",
        "SKIPPED",
    ]
    firstAuthorFamilyNameMatch: bool
    groundingUrls: _list[GroundingUrl]
    lookupVerdict: typing.Literal[
        "VERDICT_UNSPECIFIED",
        "OK",
        "MINOR_MISMATCH",
        "MAJOR_MISMATCH",
        "VERIFIED_BY_SEARCH",
        "NOT_FOUND",
        "HALLUCINATED",
        "SKIPPED",
    ]
    rawReference: str
    refNum: int
    retrievedBibtex: str
    retrievedMetadata: CitationMetadata
    searchMethod: str
    searchRationale: str
    searchVerdict: typing.Literal[
        "SEARCH_VERDICT_UNSPECIFIED",
        "NOT_HALLUCINATED",
        "HALLUCINATED_BY_SEARCH",
        "SEARCH_ERROR",
    ]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DeepReviewRunConfig(typing.TypedDict, total=False):
    geminiApiKey: str
    geminiApiKeySet: bool
    model: str
    topology: typing.Literal["TOPOLOGY_UNSPECIFIED", "EXTRA_HIGH", "HIGH", "MID", "LOW"]
    userPrompt: str

@typing.type_check_only
class Document(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    driveSource: DriveSource
    latestReviewSummary: ReviewSummary
    name: str

@typing.type_check_only
class DocumentLocation(typing.TypedDict, total=False):
    pdf: PdfLocation
    text: TextLocation

@typing.type_check_only
class DownloadDocumentResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class DriveSource(typing.TypedDict, total=False):
    fileId: str
    resourceKey: str
    resourceKeySet: bool
    revisionId: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FieldComparison(typing.TypedDict, total=False):
    detail: str
    fieldKey: str
    match: bool

@typing.type_check_only
class GroundingUrl(typing.TypedDict, total=False):
    title: str
    url: str

@typing.type_check_only
class ListDocumentsResponse(typing.TypedDict, total=False):
    documents: _list[Document]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListReviewsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reviews: _list[Review]

@typing.type_check_only
class NormalizedBoundingBox(typing.TypedDict, total=False):
    bottom: float
    left: float
    right: float
    top: float

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class PdfLocation(typing.TypedDict, total=False):
    boundingBoxes: _list[NormalizedBoundingBox]
    pageNumber: int
    quoteSelector: TextQuoteSelector

@typing.type_check_only
class Result(typing.TypedDict, total=False):
    anchoredComments: _list[AnchoredReviewComment]
    error: Status
    reviewMarkdown: str

@typing.type_check_only
class Review(typing.TypedDict, total=False):
    createTime: str
    endTime: str
    name: str
    progressPercent: int
    result: Result
    runConfig: DeepReviewRunConfig
    startTime: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class ReviewSummary(typing.TypedDict, total=False):
    createTime: str
    review: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "PENDING", "RUNNING", "SUCCEEDED", "FAILED"
    ]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TextLocation(typing.TypedDict, total=False):
    firstColumn: int
    firstLine: int
    lastColumn: int
    lastLine: int
    quotedLinePreview: str

@typing.type_check_only
class TextQuoteSelector(typing.TypedDict, total=False):
    exact: str
    prefix: str
    suffix: str

@typing.type_check_only
class UserQuota(typing.TypedDict, total=False):
    customLimitEnabled: bool
    maxReviewCountPerWeek: int
    name: str
    nextAvailableTime: str
    remainingReviewCount: int
    usedReviewCount: int
