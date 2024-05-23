import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnalyticsAccountLink(typing_extensions.TypedDict, total=False):
    analyticsAccount: str
    displayName: str
    linkVerificationState: typing_extensions.Literal[
        "LINK_VERIFICATION_STATE_UNSPECIFIED",
        "LINK_VERIFICATION_STATE_VERIFIED",
        "LINK_VERIFICATION_STATE_NOT_VERIFIED",
    ]
    name: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAnalyticsAccountLinksResponse(typing_extensions.TypedDict, total=False):
    analyticsAccountLinks: _list[AnalyticsAccountLink]
    nextPageToken: str

@typing.type_check_only
class Organization(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str

@typing.type_check_only
class SetPropertyServiceLevelRequest(typing_extensions.TypedDict, total=False):
    analyticsProperty: str
    serviceLevel: typing_extensions.Literal[
        "ANALYTICS_SERVICE_LEVEL_UNSPECIFIED",
        "ANALYTICS_SERVICE_LEVEL_STANDARD",
        "ANALYTICS_SERVICE_LEVEL_360",
    ]

@typing.type_check_only
class SetPropertyServiceLevelResponse(typing_extensions.TypedDict, total=False): ...
