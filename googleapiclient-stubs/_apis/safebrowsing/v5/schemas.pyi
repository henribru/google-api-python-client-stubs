import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleSecuritySafebrowsingV5BatchGetHashListsResponse(
    typing_extensions.TypedDict, total=False
):
    hashLists: _list[GoogleSecuritySafebrowsingV5HashList]

@typing.type_check_only
class GoogleSecuritySafebrowsingV5FullHash(typing_extensions.TypedDict, total=False):
    fullHash: str
    fullHashDetails: _list[GoogleSecuritySafebrowsingV5FullHashFullHashDetail]

@typing.type_check_only
class GoogleSecuritySafebrowsingV5FullHashFullHashDetail(
    typing_extensions.TypedDict, total=False
):
    attributes: _list[
        typing_extensions.Literal[
            "THREAT_ATTRIBUTE_UNSPECIFIED", "CANARY", "FRAME_ONLY"
        ]
    ]
    threatType: typing_extensions.Literal[
        "THREAT_TYPE_UNSPECIFIED",
        "MALWARE",
        "SOCIAL_ENGINEERING",
        "UNWANTED_SOFTWARE",
        "POTENTIALLY_HARMFUL_APPLICATION",
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV5HashList(typing_extensions.TypedDict, total=False):
    additionsEightBytes: GoogleSecuritySafebrowsingV5RiceDeltaEncoded64Bit
    additionsFourBytes: GoogleSecuritySafebrowsingV5RiceDeltaEncoded32Bit
    additionsSixteenBytes: GoogleSecuritySafebrowsingV5RiceDeltaEncoded128Bit
    additionsThirtyTwoBytes: GoogleSecuritySafebrowsingV5RiceDeltaEncoded256Bit
    compressedRemovals: GoogleSecuritySafebrowsingV5RiceDeltaEncoded32Bit
    metadata: GoogleSecuritySafebrowsingV5HashListMetadata
    minimumWaitDuration: str
    name: str
    partialUpdate: bool
    sha256Checksum: str
    version: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV5HashListMetadata(
    typing_extensions.TypedDict, total=False
):
    description: str
    hashLength: typing_extensions.Literal[
        "HASH_LENGTH_UNSPECIFIED",
        "FOUR_BYTES",
        "EIGHT_BYTES",
        "SIXTEEN_BYTES",
        "THIRTY_TWO_BYTES",
    ]
    likelySafeTypes: _list[
        typing_extensions.Literal[
            "LIKELY_SAFE_TYPE_UNSPECIFIED", "GENERAL_BROWSING", "CSD", "DOWNLOAD"
        ]
    ]
    threatTypes: _list[
        typing_extensions.Literal[
            "THREAT_TYPE_UNSPECIFIED",
            "MALWARE",
            "SOCIAL_ENGINEERING",
            "UNWANTED_SOFTWARE",
            "POTENTIALLY_HARMFUL_APPLICATION",
        ]
    ]

@typing.type_check_only
class GoogleSecuritySafebrowsingV5ListHashListsResponse(
    typing_extensions.TypedDict, total=False
):
    hashLists: _list[GoogleSecuritySafebrowsingV5HashList]
    nextPageToken: str

@typing.type_check_only
class GoogleSecuritySafebrowsingV5RiceDeltaEncoded128Bit(
    typing_extensions.TypedDict, total=False
):
    encodedData: str
    entriesCount: int
    firstValueHi: str
    firstValueLo: str
    riceParameter: int

@typing.type_check_only
class GoogleSecuritySafebrowsingV5RiceDeltaEncoded256Bit(
    typing_extensions.TypedDict, total=False
):
    encodedData: str
    entriesCount: int
    firstValueFirstPart: str
    firstValueFourthPart: str
    firstValueSecondPart: str
    firstValueThirdPart: str
    riceParameter: int

@typing.type_check_only
class GoogleSecuritySafebrowsingV5RiceDeltaEncoded32Bit(
    typing_extensions.TypedDict, total=False
):
    encodedData: str
    entriesCount: int
    firstValue: int
    riceParameter: int

@typing.type_check_only
class GoogleSecuritySafebrowsingV5RiceDeltaEncoded64Bit(
    typing_extensions.TypedDict, total=False
):
    encodedData: str
    entriesCount: int
    firstValue: str
    riceParameter: int

@typing.type_check_only
class GoogleSecuritySafebrowsingV5SearchHashesResponse(
    typing_extensions.TypedDict, total=False
):
    cacheDuration: str
    fullHashes: _list[GoogleSecuritySafebrowsingV5FullHash]
