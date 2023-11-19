import typing

import typing_extensions

_list = list

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
class GoogleSecuritySafebrowsingV5SearchHashesResponse(
    typing_extensions.TypedDict, total=False
):
    cacheDuration: str
    fullHashes: _list[GoogleSecuritySafebrowsingV5FullHash]
