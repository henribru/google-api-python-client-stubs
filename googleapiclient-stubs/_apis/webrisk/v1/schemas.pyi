import typing

_list = list

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponse(typing.TypedDict, total=False):
    additions: GoogleCloudWebriskV1ThreatEntryAdditions
    checksum: GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum
    newVersionToken: str
    recommendedNextDiff: str
    removals: GoogleCloudWebriskV1ThreatEntryRemovals
    responseType: typing.Literal["RESPONSE_TYPE_UNSPECIFIED", "DIFF", "RESET"]

@typing.type_check_only
class GoogleCloudWebriskV1ComputeThreatListDiffResponseChecksum(
    typing.TypedDict, total=False
):
    sha256: str

@typing.type_check_only
class GoogleCloudWebriskV1RawHashes(typing.TypedDict, total=False):
    prefixSize: int
    rawHashes: str

@typing.type_check_only
class GoogleCloudWebriskV1RawIndices(typing.TypedDict, total=False):
    indices: _list[int]

@typing.type_check_only
class GoogleCloudWebriskV1RiceDeltaEncoding(typing.TypedDict, total=False):
    encodedData: str
    entryCount: int
    firstValue: str
    riceParameter: int

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponse(typing.TypedDict, total=False):
    negativeExpireTime: str
    threats: _list[GoogleCloudWebriskV1SearchHashesResponseThreatHash]

@typing.type_check_only
class GoogleCloudWebriskV1SearchHashesResponseThreatHash(typing.TypedDict, total=False):
    expireTime: str
    hash: str
    threatTypes: _list[
        typing.Literal[
            "THREAT_TYPE_UNSPECIFIED",
            "MALWARE",
            "SOCIAL_ENGINEERING",
            "UNWANTED_SOFTWARE",
            "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponse(typing.TypedDict, total=False):
    threat: GoogleCloudWebriskV1SearchUrisResponseThreatUri

@typing.type_check_only
class GoogleCloudWebriskV1SearchUrisResponseThreatUri(typing.TypedDict, total=False):
    expireTime: str
    threatTypes: _list[
        typing.Literal[
            "THREAT_TYPE_UNSPECIFIED",
            "MALWARE",
            "SOCIAL_ENGINEERING",
            "UNWANTED_SOFTWARE",
            "SOCIAL_ENGINEERING_EXTENDED_COVERAGE",
        ]
    ]

@typing.type_check_only
class GoogleCloudWebriskV1Submission(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudWebriskV1ThreatEntryAdditions(typing.TypedDict, total=False):
    rawHashes: _list[GoogleCloudWebriskV1RawHashes]
    riceHashes: GoogleCloudWebriskV1RiceDeltaEncoding

@typing.type_check_only
class GoogleCloudWebriskV1ThreatEntryRemovals(typing.TypedDict, total=False):
    rawIndices: GoogleCloudWebriskV1RawIndices
    riceIndices: GoogleCloudWebriskV1RiceDeltaEncoding

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
