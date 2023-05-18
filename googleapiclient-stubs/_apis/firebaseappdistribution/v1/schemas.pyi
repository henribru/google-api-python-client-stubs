import typing

import typing_extensions

_list = list

@typing.type_check_only
class GdataBlobstore2Info(typing_extensions.TypedDict, total=False):
    blobGeneration: str
    blobId: str
    downloadReadHandle: str
    readToken: str
    uploadMetadataContainer: str

@typing.type_check_only
class GdataCompositeMedia(typing_extensions.TypedDict, total=False):
    blobRef: str
    blobstore2Info: GdataBlobstore2Info
    cosmoBinaryReference: str
    crc32cHash: int
    inline: str
    length: str
    md5Hash: str
    objectId: GdataObjectId
    path: str
    referenceType: typing_extensions.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    sha1Hash: str

@typing.type_check_only
class GdataContentTypeInfo(typing_extensions.TypedDict, total=False):
    bestGuess: str
    fromBytes: str
    fromFileName: str
    fromHeader: str
    fromUrlPath: str

@typing.type_check_only
class GdataDiffChecksumsResponse(typing_extensions.TypedDict, total=False):
    checksumsLocation: GdataCompositeMedia
    chunkSizeBytes: str
    objectLocation: GdataCompositeMedia
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class GdataDiffDownloadResponse(typing_extensions.TypedDict, total=False):
    objectLocation: GdataCompositeMedia

@typing.type_check_only
class GdataDiffUploadRequest(typing_extensions.TypedDict, total=False):
    checksumsInfo: GdataCompositeMedia
    objectInfo: GdataCompositeMedia
    objectVersion: str

@typing.type_check_only
class GdataDiffUploadResponse(typing_extensions.TypedDict, total=False):
    objectVersion: str
    originalObject: GdataCompositeMedia

@typing.type_check_only
class GdataDiffVersionResponse(typing_extensions.TypedDict, total=False):
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class GdataDownloadParameters(typing_extensions.TypedDict, total=False):
    allowGzipCompression: bool
    ignoreRange: bool

@typing.type_check_only
class GdataMedia(typing_extensions.TypedDict, total=False):
    algorithm: str
    bigstoreObjectRef: str
    blobRef: str
    blobstore2Info: GdataBlobstore2Info
    compositeMedia: _list[GdataCompositeMedia]
    contentType: str
    contentTypeInfo: GdataContentTypeInfo
    cosmoBinaryReference: str
    crc32cHash: int
    diffChecksumsResponse: GdataDiffChecksumsResponse
    diffDownloadResponse: GdataDiffDownloadResponse
    diffUploadRequest: GdataDiffUploadRequest
    diffUploadResponse: GdataDiffUploadResponse
    diffVersionResponse: GdataDiffVersionResponse
    downloadParameters: GdataDownloadParameters
    filename: str
    hash: str
    hashVerified: bool
    inline: str
    isPotentialRetry: bool
    length: str
    md5Hash: str
    mediaId: str
    objectId: GdataObjectId
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
class GdataObjectId(typing_extensions.TypedDict, total=False):
    bucketName: str
    generation: str
    objectName: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1AabInfo(typing_extensions.TypedDict, total=False):
    integrationState: typing_extensions.Literal[
        "AAB_INTEGRATION_STATE_UNSPECIFIED",
        "INTEGRATED",
        "PLAY_ACCOUNT_NOT_LINKED",
        "NO_APP_WITH_GIVEN_BUNDLE_ID_IN_PLAY_ACCOUNT",
        "APP_NOT_PUBLISHED",
        "AAB_STATE_UNAVAILABLE",
        "PLAY_IAS_TERMS_NOT_ACCEPTED",
    ]
    name: str
    testCertificate: GoogleFirebaseAppdistroV1TestCertificate

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchAddTestersRequest(
    typing_extensions.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchAddTestersResponse(
    typing_extensions.TypedDict, total=False
):
    testers: _list[GoogleFirebaseAppdistroV1Tester]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchDeleteReleasesRequest(
    typing_extensions.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchJoinGroupRequest(
    typing_extensions.TypedDict, total=False
):
    createMissingTesters: bool
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchLeaveGroupRequest(
    typing_extensions.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchRemoveTestersRequest(
    typing_extensions.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchRemoveTestersResponse(
    typing_extensions.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1DistributeReleaseRequest(
    typing_extensions.TypedDict, total=False
):
    groupAliases: _list[str]
    testerEmails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1DistributeReleaseResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1FeedbackReport(typing_extensions.TypedDict, total=False):
    createTime: str
    firebaseConsoleUri: str
    name: str
    screenshotUri: str
    tester: str
    text: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1Group(typing_extensions.TypedDict, total=False):
    displayName: str
    inviteLinkCount: int
    name: str
    releaseCount: int
    testerCount: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListFeedbackReportsResponse(
    typing_extensions.TypedDict, total=False
):
    feedbackReports: _list[GoogleFirebaseAppdistroV1FeedbackReport]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListGroupsResponse(
    typing_extensions.TypedDict, total=False
):
    groups: _list[GoogleFirebaseAppdistroV1Group]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListReleasesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    releases: _list[GoogleFirebaseAppdistroV1Release]

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListTestersResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    testers: _list[GoogleFirebaseAppdistroV1Tester]

@typing.type_check_only
class GoogleFirebaseAppdistroV1Release(typing_extensions.TypedDict, total=False):
    binaryDownloadUri: str
    buildVersion: str
    createTime: str
    displayVersion: str
    firebaseConsoleUri: str
    name: str
    releaseNotes: GoogleFirebaseAppdistroV1ReleaseNotes
    testingUri: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ReleaseNotes(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1TestCertificate(
    typing_extensions.TypedDict, total=False
):
    hashMd5: str
    hashSha1: str
    hashSha256: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1Tester(typing_extensions.TypedDict, total=False):
    displayName: str
    groups: _list[str]
    lastActivityTime: str
    name: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseRequest(
    typing_extensions.TypedDict, total=False
):
    blob: GdataMedia

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseResponse(
    typing_extensions.TypedDict, total=False
):
    release: GoogleFirebaseAppdistroV1Release
    result: typing_extensions.Literal[
        "UPLOAD_RELEASE_RESULT_UNSPECIFIED",
        "RELEASE_CREATED",
        "RELEASE_UPDATED",
        "RELEASE_UNMODIFIED",
    ]

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
class GoogleLongrunningWaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
