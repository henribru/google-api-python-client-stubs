import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

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
class Job(typing.TypedDict, total=False):
    createTime: str
    expireTime: str
    id: str
    name: str
    reportTypeId: str
    systemManaged: bool

@typing.type_check_only
class ListJobsResponse(typing.TypedDict, total=False):
    jobs: _list[Job]
    nextPageToken: str

@typing.type_check_only
class ListReportTypesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reportTypes: _list[ReportType]

@typing.type_check_only
class ListReportsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reports: _list[Report]

@typing.type_check_only
class Report(typing.TypedDict, total=False):
    createTime: str
    downloadUrl: str
    endTime: str
    id: str
    jobExpireTime: str
    jobId: str
    startTime: str

@typing.type_check_only
class ReportType(typing.TypedDict, total=False):
    deprecateTime: str
    id: str
    name: str
    systemManaged: bool
