import typing

import typing_extensions

_list = list

@typing.type_check_only
class Actor(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str
    googleSupport: bool

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    createTime: str
    creator: Actor
    filename: str
    mimeType: str
    name: str
    sizeBytes: str

@typing.type_check_only
class Blobstore2Info(typing_extensions.TypedDict, total=False):
    blobGeneration: str
    blobId: str
    downloadReadHandle: str
    readToken: str
    uploadMetadataContainer: str

@typing.type_check_only
class Case(typing_extensions.TypedDict, total=False):
    classification: CaseClassification
    createTime: str
    creator: Actor
    description: str
    displayName: str
    escalated: bool
    name: str
    priority: typing_extensions.Literal[
        "PRIORITY_UNSPECIFIED", "P0", "P1", "P2", "P3", "P4"
    ]
    severity: typing_extensions.Literal[
        "SEVERITY_UNSPECIFIED", "S0", "S1", "S2", "S3", "S4"
    ]
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "NEW",
        "IN_PROGRESS_GOOGLE_SUPPORT",
        "ACTION_REQUIRED",
        "SOLUTION_PROVIDED",
        "CLOSED",
    ]
    subscriberEmailAddresses: _list[str]
    testCase: bool
    timeZone: str
    updateTime: str

@typing.type_check_only
class CaseClassification(typing_extensions.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class CloseCaseRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    body: str
    createTime: str
    creator: Actor
    name: str
    plainTextBody: str

@typing.type_check_only
class CompositeMedia(typing_extensions.TypedDict, total=False):
    blobRef: str
    blobstore2Info: Blobstore2Info
    cosmoBinaryReference: str
    crc32cHash: int
    inline: str
    length: str
    md5Hash: str
    objectId: ObjectId
    path: str
    referenceType: typing_extensions.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    sha1Hash: str

@typing.type_check_only
class ContentTypeInfo(typing_extensions.TypedDict, total=False):
    bestGuess: str
    fromBytes: str
    fromFileName: str
    fromHeader: str
    fromUrlPath: str

@typing.type_check_only
class CreateAttachmentRequest(typing_extensions.TypedDict, total=False):
    attachment: Attachment

@typing.type_check_only
class DiffChecksumsResponse(typing_extensions.TypedDict, total=False):
    checksumsLocation: CompositeMedia
    chunkSizeBytes: str
    objectLocation: CompositeMedia
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DiffDownloadResponse(typing_extensions.TypedDict, total=False):
    objectLocation: CompositeMedia

@typing.type_check_only
class DiffUploadRequest(typing_extensions.TypedDict, total=False):
    checksumsInfo: CompositeMedia
    objectInfo: CompositeMedia
    objectVersion: str

@typing.type_check_only
class DiffUploadResponse(typing_extensions.TypedDict, total=False):
    objectVersion: str
    originalObject: CompositeMedia

@typing.type_check_only
class DiffVersionResponse(typing_extensions.TypedDict, total=False):
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DownloadParameters(typing_extensions.TypedDict, total=False):
    allowGzipCompression: bool
    ignoreRange: bool

@typing.type_check_only
class EscalateCaseRequest(typing_extensions.TypedDict, total=False):
    escalation: Escalation

@typing.type_check_only
class Escalation(typing_extensions.TypedDict, total=False):
    justification: str
    reason: typing_extensions.Literal[
        "REASON_UNSPECIFIED",
        "RESOLUTION_TIME",
        "TECHNICAL_EXPERTISE",
        "BUSINESS_IMPACT",
    ]

@typing.type_check_only
class ListAttachmentsResponse(typing_extensions.TypedDict, total=False):
    attachments: _list[Attachment]
    nextPageToken: str

@typing.type_check_only
class ListCasesResponse(typing_extensions.TypedDict, total=False):
    cases: _list[Case]
    nextPageToken: str

@typing.type_check_only
class ListCommentsResponse(typing_extensions.TypedDict, total=False):
    comments: _list[Comment]
    nextPageToken: str

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    algorithm: str
    bigstoreObjectRef: str
    blobRef: str
    blobstore2Info: Blobstore2Info
    compositeMedia: _list[CompositeMedia]
    contentType: str
    contentTypeInfo: ContentTypeInfo
    cosmoBinaryReference: str
    crc32cHash: int
    diffChecksumsResponse: DiffChecksumsResponse
    diffDownloadResponse: DiffDownloadResponse
    diffUploadRequest: DiffUploadRequest
    diffUploadResponse: DiffUploadResponse
    diffVersionResponse: DiffVersionResponse
    downloadParameters: DownloadParameters
    filename: str
    hash: str
    hashVerified: bool
    inline: str
    isPotentialRetry: bool
    length: str
    md5Hash: str
    mediaId: str
    objectId: ObjectId
    path: str
    referenceType: typing_extensions.Literal[
        "PATH",
        "BLOB_REF",
        "INLINE",
        "GET_MEDIA",
        "COMPOSITE_MEDIA",
        "BIGSTORE_REF",
        "DIFF_VERSION_RESPONSE",
        "DIFF_CHECKSUMS_RESPONSE",
        "DIFF_DOWNLOAD_RESPONSE",
        "DIFF_UPLOAD_REQUEST",
        "DIFF_UPLOAD_RESPONSE",
        "COSMO_BINARY_REFERENCE",
        "ARBITRARY_BYTES",
    ]
    sha1Hash: str
    sha256Hash: str
    timestamp: str
    token: str

@typing.type_check_only
class ObjectId(typing_extensions.TypedDict, total=False):
    bucketName: str
    generation: str
    objectName: str

@typing.type_check_only
class SearchCaseClassificationsResponse(typing_extensions.TypedDict, total=False):
    caseClassifications: _list[CaseClassification]
    nextPageToken: str

@typing.type_check_only
class SearchCasesResponse(typing_extensions.TypedDict, total=False):
    cases: _list[Case]
    nextPageToken: str

@typing.type_check_only
class WorkflowOperationMetadata(typing_extensions.TypedDict, total=False):
    namespace: str
    operationAction: typing_extensions.Literal[
        "OPERATION_ACTION_UNSPECIFIED",
        "CREATE_SUPPORT_ACCOUNT",
        "UPDATE_SUPPORT_ACCOUNT",
        "PURCHASE_SUPPORT_ACCOUNT",
    ]
    workflowOperationType: typing_extensions.Literal[
        "UNKNOWN_OPERATION_TYPE", "WORKFLOWS_V1", "WORKFLOWS_V2"
    ]
