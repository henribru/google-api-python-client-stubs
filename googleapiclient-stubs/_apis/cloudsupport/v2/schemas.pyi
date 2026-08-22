import typing

_list = list

@typing.type_check_only
class Actor(typing.TypedDict, total=False):
    displayName: str
    email: str
    googleSupport: bool
    username: str

@typing.type_check_only
class Attachment(typing.TypedDict, total=False):
    createTime: str
    creator: Actor
    filename: str
    mimeType: str
    name: str
    sizeBytes: str

@typing.type_check_only
class Blobstore2Info(typing.TypedDict, total=False):
    blobGeneration: str
    blobId: str
    downloadExternalReadToken: str
    downloadReadHandle: str
    readToken: str
    uploadFragmentListCreationInfo: str
    uploadMetadataContainer: str

@typing.type_check_only
class Case(typing.TypedDict, total=False):
    classification: CaseClassification
    contactEmail: str
    createTime: str
    creator: Actor
    description: str
    displayName: str
    escalated: bool
    languageCode: str
    name: str
    priority: typing.Literal["PRIORITY_UNSPECIFIED", "P0", "P1", "P2", "P3", "P4"]
    state: typing.Literal[
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
class CaseClassification(typing.TypedDict, total=False):
    displayName: str
    id: str

@typing.type_check_only
class CloseCaseRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Comment(typing.TypedDict, total=False):
    body: str
    createTime: str
    creator: Actor
    name: str
    plainTextBody: str

@typing.type_check_only
class CompositeMedia(typing.TypedDict, total=False):
    blobRef: str
    blobstore2Info: Blobstore2Info
    cosmoBinaryReference: str
    crc32cHash: int
    inline: str
    length: str
    md5Hash: str
    objectId: ObjectId
    path: str
    referenceType: typing.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    sha1Hash: str

@typing.type_check_only
class ContentTypeInfo(typing.TypedDict, total=False):
    bestGuess: str
    fromBytes: str
    fromFileName: str
    fromFusionId: str
    fromHeader: str
    fromUrlPath: str
    fusionIdDetectionMetadata: str

@typing.type_check_only
class CreateAttachmentRequest(typing.TypedDict, total=False):
    attachment: Attachment

@typing.type_check_only
class DiffChecksumsResponse(typing.TypedDict, total=False):
    checksumsLocation: CompositeMedia
    chunkSizeBytes: str
    objectLocation: CompositeMedia
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DiffDownloadResponse(typing.TypedDict, total=False):
    objectLocation: CompositeMedia

@typing.type_check_only
class DiffUploadRequest(typing.TypedDict, total=False):
    checksumsInfo: CompositeMedia
    objectInfo: CompositeMedia
    objectVersion: str

@typing.type_check_only
class DiffUploadResponse(typing.TypedDict, total=False):
    objectVersion: str
    originalObject: CompositeMedia

@typing.type_check_only
class DiffVersionResponse(typing.TypedDict, total=False):
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class DownloadParameters(typing.TypedDict, total=False):
    allowGzipCompression: bool
    ignoreRange: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EscalateCaseRequest(typing.TypedDict, total=False):
    escalation: Escalation

@typing.type_check_only
class Escalation(typing.TypedDict, total=False):
    justification: str
    reason: typing.Literal[
        "REASON_UNSPECIFIED",
        "RESOLUTION_TIME",
        "TECHNICAL_EXPERTISE",
        "BUSINESS_IMPACT",
    ]

@typing.type_check_only
class ExpungeSupportEventSubscriptionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListAttachmentsResponse(typing.TypedDict, total=False):
    attachments: _list[Attachment]
    nextPageToken: str

@typing.type_check_only
class ListCasesResponse(typing.TypedDict, total=False):
    cases: _list[Case]
    nextPageToken: str

@typing.type_check_only
class ListCommentsResponse(typing.TypedDict, total=False):
    comments: _list[Comment]
    nextPageToken: str

@typing.type_check_only
class ListSupportEventSubscriptionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    supportEventSubscriptions: _list[SupportEventSubscription]

@typing.type_check_only
class Media(typing.TypedDict, total=False):
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
    referenceType: typing.Literal[
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
    sha512Hash: str
    timestamp: str
    token: str

@typing.type_check_only
class ObjectId(typing.TypedDict, total=False):
    bucketName: str
    generation: str
    objectName: str

@typing.type_check_only
class SearchCaseClassificationsResponse(typing.TypedDict, total=False):
    caseClassifications: _list[CaseClassification]
    nextPageToken: str

@typing.type_check_only
class SearchCasesResponse(typing.TypedDict, total=False):
    cases: _list[Case]
    nextPageToken: str

@typing.type_check_only
class SupportEventSubscription(typing.TypedDict, total=False):
    createTime: str
    deleteTime: str
    failureReason: typing.Literal[
        "FAILURE_REASON_UNSPECIFIED", "PERMISSION_DENIED", "TOPIC_NOT_FOUND", "OTHER"
    ]
    name: str
    pubSubTopic: str
    purgeTime: str
    state: typing.Literal["STATE_UNSPECIFIED", "WORKING", "FAILING", "DELETED"]
    updateTime: str

@typing.type_check_only
class UndeleteSupportEventSubscriptionRequest(typing.TypedDict, total=False): ...
