import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponse(
    typing_extensions.TypedDict, total=False
):
    additions: GoogleCloudWebriskV1ThreatEntryAdditions
    checksum: GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum
    newVersionToken: str
    recommendedNextDiff: str
    removals: GoogleCloudWebriskV1ThreatEntryRemovals
    responseType: typing_extensions.Literal[
        "RESPONSE_TYPE_UNSPECIFIED", "DIFF", "RESET"
    ]

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum(
    typing_extensions.TypedDict, total=False
):
    sha256: str

@typing.type_check_only
class GoogleCloudWebriskV1RawHashes(typing_extensions.TypedDict, total=False):
    prefixSize: int
    rawHashes: str

@typing.type_check_only
class GoogleCloudWebriskV1RawIndices(typing_extensions.TypedDict, total=False):
    indices: _list[int]

@typing.type_check_only
class GoogleCloudWebriskV1RiceDeltaEncoding(typing_extensions.TypedDict, total=False):
    encodedData: str
    entryCount: int
    firstValue: str
    riceParameter: int

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponse(
    typing_extensions.TypedDict, total=False
):
    negativeExpireTime: str
    threats: _list[GoogleCloudWebriskV1SearchHashesResponseThreatHash]

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponseThreatHash(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    hash: str
    threatTypes: _list[str]

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponse(typing_extensions.TypedDict, total=False):
    threat: GoogleCloudWebriskV1SearchUrisResponseThreatUri

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponseThreatUri(
    typing_extensions.TypedDict, total=False
):
    expireTime: str
    threatTypes: _list[str]

@typing.type_check_only
class GoogleCloudWebriskV1Submission(typing_extensions.TypedDict, total=False):
    threatTypes: _list[str]
    uri: str

@typing.type_check_only
class GoogleCloudWebriskV1SubmitUriMetadata(typing_extensions.TypedDict, total=False):
    createTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "RUNNING", "SUCCEEDED", "CANCELLED", "FAILED", "CLOSED"
    ]
    updateTime: str

@typing.type_check_only
class GoogleCloudWebriskV1SubmitUriRequest(typing_extensions.TypedDict, total=False):
    submission: GoogleCloudWebriskV1Submission

@typing.type_check_only
class GoogleCloudWebriskV1ThreatEntryAdditions(
    typing_extensions.TypedDict, total=False
):
    rawHashes: _list[GoogleCloudWebriskV1RawHashes]
    riceHashes: GoogleCloudWebriskV1RiceDeltaEncoding

@typing.type_check_only
class GoogleCloudWebriskV1ThreatEntryRemovals(typing_extensions.TypedDict, total=False):
    rawIndices: GoogleCloudWebriskV1RawIndices
    riceIndices: GoogleCloudWebriskV1RiceDeltaEncoding

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
