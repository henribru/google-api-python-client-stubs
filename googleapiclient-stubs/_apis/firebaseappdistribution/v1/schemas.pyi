import typing

_list = list

@typing.type_check_only
class GdataBlobstore2Info(typing.TypedDict, total=False):
    blobGeneration: str
    blobId: str
    downloadExternalReadToken: str
    downloadReadHandle: str
    readToken: str
    uploadFragmentListCreationInfo: str
    uploadMetadataContainer: str

@typing.type_check_only
class GdataCompositeMedia(typing.TypedDict, total=False):
    blobRef: str
    blobstore2Info: GdataBlobstore2Info
    cosmoBinaryReference: str
    crc32cHash: int
    inline: str
    length: str
    md5Hash: str
    objectId: GdataObjectId
    path: str
    referenceType: typing.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    sha1Hash: str

@typing.type_check_only
class GdataContentTypeInfo(typing.TypedDict, total=False):
    bestGuess: str
    fromBytes: str
    fromFileName: str
    fromFusionId: str
    fromHeader: str
    fromUrlPath: str
    fusionIdDetectionMetadata: str

@typing.type_check_only
class GdataDiffChecksumsResponse(typing.TypedDict, total=False):
    checksumsLocation: GdataCompositeMedia
    chunkSizeBytes: str
    objectLocation: GdataCompositeMedia
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class GdataDiffDownloadResponse(typing.TypedDict, total=False):
    objectLocation: GdataCompositeMedia

@typing.type_check_only
class GdataDiffUploadRequest(typing.TypedDict, total=False):
    checksumsInfo: GdataCompositeMedia
    objectInfo: GdataCompositeMedia
    objectVersion: str

@typing.type_check_only
class GdataDiffUploadResponse(typing.TypedDict, total=False):
    objectVersion: str
    originalObject: GdataCompositeMedia

@typing.type_check_only
class GdataDiffVersionResponse(typing.TypedDict, total=False):
    objectSizeBytes: str
    objectVersion: str

@typing.type_check_only
class GdataDownloadParameters(typing.TypedDict, total=False):
    allowGzipCompression: bool
    ignoreRange: bool

@typing.type_check_only
class GdataMedia(typing.TypedDict, total=False):
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
class GdataObjectId(typing.TypedDict, total=False):
    bucketName: str
    generation: str
    objectName: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1AabInfo(typing.TypedDict, total=False):
    integrationState: typing.Literal[
        "AAB_INTEGRATION_STATE_UNSPECIFIED",
        "INTEGRATED",
        "PLAY_ACCOUNT_NOT_LINKED",
        "NO_APP_WITH_GIVEN_BUNDLE_ID_IN_PLAY_ACCOUNT",
        "APP_NOT_PUBLISHED",
        "AAB_STATE_UNAVAILABLE",
        "PLAY_IAS_TERMS_NOT_ACCEPTED",
        "ADHOC_SHARING_KEY_NOT_GENERATED",
        "ADHOC_SHARING_KEY_NOT_REGISTERED",
        "PLAY_ANDROID_DEVELOPER_CONSOLE_ACCOUNT_NOT_FOUND",
        "PLAY_ANDROID_DEVELOPER_CONSOLE_PACKAGE_NOT_FOUND",
    ]
    name: str
    testCertificate: GoogleFirebaseAppdistroV1TestCertificate

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchAddTestersRequest(typing.TypedDict, total=False):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchAddTestersResponse(typing.TypedDict, total=False):
    testers: _list[GoogleFirebaseAppdistroV1Tester]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchDeleteReleasesRequest(
    typing.TypedDict, total=False
):
    names: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchJoinGroupRequest(typing.TypedDict, total=False):
    createMissingTesters: bool
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchLeaveGroupRequest(typing.TypedDict, total=False):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchRemoveTestersRequest(typing.TypedDict, total=False):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1BatchRemoveTestersResponse(
    typing.TypedDict, total=False
):
    emails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1DistributeReleaseRequest(typing.TypedDict, total=False):
    groupAliases: _list[str]
    testerEmails: _list[str]

@typing.type_check_only
class GoogleFirebaseAppdistroV1DistributeReleaseResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1FeedbackReport(typing.TypedDict, total=False):
    createTime: str
    firebaseConsoleUri: str
    name: str
    screenshotUri: str
    tester: str
    text: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1Group(typing.TypedDict, total=False):
    displayName: str
    inviteLinkCount: int
    name: str
    releaseCount: int
    testerCount: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListFeedbackReportsResponse(
    typing.TypedDict, total=False
):
    feedbackReports: _list[GoogleFirebaseAppdistroV1FeedbackReport]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListGroupsResponse(typing.TypedDict, total=False):
    groups: _list[GoogleFirebaseAppdistroV1Group]
    nextPageToken: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListReleasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    releases: _list[GoogleFirebaseAppdistroV1Release]
    totalSize: int

@typing.type_check_only
class GoogleFirebaseAppdistroV1ListTestersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    testers: _list[GoogleFirebaseAppdistroV1Tester]

@typing.type_check_only
class GoogleFirebaseAppdistroV1Release(typing.TypedDict, total=False):
    acceptedInvitationCount: int
    androidPackageRegistrationState: typing.Literal[
        "ANDROID_PACKAGE_REGISTRATION_STATE_UNSPECIFIED",
        "REGISTERED",
        "NOT_REGISTERED",
        "REGISTERED_WITH_ANOTHER_CERTIFICATE_FINGERPRINT",
    ]
    binaryDownloadUri: str
    binaryType: typing.Literal["BINARY_TYPE_UNSPECIFIED", "IPA", "APK", "AAB"]
    buildVersion: str
    createTime: str
    displayVersion: str
    expireTime: str
    feedbackCount: int
    firebaseConsoleUri: str
    installationCount: int
    name: str
    openInvitationCount: int
    releaseNotes: GoogleFirebaseAppdistroV1ReleaseNotes
    testState: typing.Literal[
        "TEST_STATE_UNSPECIFIED",
        "NO_TESTS_REQUESTED",
        "IN_PROGRESS",
        "PASSED",
        "FAILED",
        "INCONCLUSIVE",
    ]
    testingUri: str
    updateTime: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1ReleaseNotes(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1TestCertificate(typing.TypedDict, total=False):
    hashMd5: str
    hashSha1: str
    hashSha256: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1Tester(typing.TypedDict, total=False):
    displayName: str
    groups: _list[str]
    lastActivityTime: str
    name: str

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseMetadata(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseRequest(typing.TypedDict, total=False):
    blob: GdataMedia

@typing.type_check_only
class GoogleFirebaseAppdistroV1UploadReleaseResponse(typing.TypedDict, total=False):
    release: GoogleFirebaseAppdistroV1Release
    result: typing.Literal[
        "UPLOAD_RELEASE_RESULT_UNSPECIFIED",
        "RELEASE_CREATED",
        "RELEASE_UPDATED",
        "RELEASE_UNMODIFIED",
    ]

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
class GoogleLongrunningWaitOperationRequest(typing.TypedDict, total=False):
    timeout: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleRpcStatus(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str
