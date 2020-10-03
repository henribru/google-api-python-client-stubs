import typing

import typing_extensions

class GdataObjectId(typing_extensions.TypedDict, total=False):
    objectName: str
    generation: str
    bucketName: str

class GdataCompositeMedia(typing_extensions.TypedDict, total=False):
    length: str
    objectId: GdataObjectId
    inline: str
    md5Hash: str
    blobRef: str
    sha1Hash: str
    path: str
    crc32cHash: int
    blobstore2Info: GdataBlobstore2Info
    referenceType: typing_extensions.Literal[
        "PATH", "BLOB_REF", "INLINE", "BIGSTORE_REF", "COSMO_BINARY_REFERENCE"
    ]
    cosmoBinaryReference: str

class GdataDiffUploadResponse(typing_extensions.TypedDict, total=False):
    objectVersion: str
    originalObject: GdataCompositeMedia

class Empty(typing_extensions.TypedDict, total=False): ...

class ListReportTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reportTypes: typing.List[ReportType]

class Job(typing_extensions.TypedDict, total=False):
    reportTypeId: str
    name: str
    createTime: str
    id: str
    systemManaged: bool
    expireTime: str

class GdataDiffChecksumsResponse(typing_extensions.TypedDict, total=False):
    checksumsLocation: GdataCompositeMedia
    objectSizeBytes: str
    chunkSizeBytes: str
    objectLocation: GdataCompositeMedia
    objectVersion: str

class Report(typing_extensions.TypedDict, total=False):
    jobExpireTime: str
    downloadUrl: str
    jobId: str
    id: str
    startTime: str
    endTime: str
    createTime: str

class ReportType(typing_extensions.TypedDict, total=False):
    deprecateTime: str
    id: str
    name: str
    systemManaged: bool

class GdataDiffVersionResponse(typing_extensions.TypedDict, total=False):
    objectVersion: str
    objectSizeBytes: str

class ListReportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reports: typing.List[Report]

class GdataDownloadParameters(typing_extensions.TypedDict, total=False):
    ignoreRange: bool
    allowGzipCompression: bool

class GdataContentTypeInfo(typing_extensions.TypedDict, total=False):
    fromHeader: str
    fromFileName: str
    fromUrlPath: str
    bestGuess: str
    fromBytes: str

class ListJobsResponse(typing_extensions.TypedDict, total=False):
    jobs: typing.List[Job]
    nextPageToken: str

class GdataDiffUploadRequest(typing_extensions.TypedDict, total=False):
    objectVersion: str
    checksumsInfo: GdataCompositeMedia
    objectInfo: GdataCompositeMedia

class GdataDiffDownloadResponse(typing_extensions.TypedDict, total=False):
    objectLocation: GdataCompositeMedia

class GdataMedia(typing_extensions.TypedDict, total=False):
    compositeMedia: typing.List[GdataCompositeMedia]
    downloadParameters: GdataDownloadParameters
    sha1Hash: str
    isPotentialRetry: bool
    diffUploadResponse: GdataDiffUploadResponse
    diffVersionResponse: GdataDiffVersionResponse
    objectId: GdataObjectId
    crc32cHash: int
    token: str
    algorithm: str
    bigstoreObjectRef: str
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
    contentType: str
    timestamp: str
    blobstore2Info: GdataBlobstore2Info
    diffDownloadResponse: GdataDiffDownloadResponse
    diffUploadRequest: GdataDiffUploadRequest
    blobRef: str
    hash: str
    inline: str
    length: str
    filename: str
    cosmoBinaryReference: str
    mediaId: str
    hashVerified: bool
    contentTypeInfo: GdataContentTypeInfo
    md5Hash: str
    sha256Hash: str
    diffChecksumsResponse: GdataDiffChecksumsResponse
    path: str

class GdataBlobstore2Info(typing_extensions.TypedDict, total=False):
    blobId: str
    readToken: str
    blobGeneration: str
    downloadReadHandle: str
    uploadMetadataContainer: str
