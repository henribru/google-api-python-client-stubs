import typing

import typing_extensions

class PlatformSummary(typing_extensions.TypedDict, total=False):
    underReview: bool
    enforcementTime: str
    betterAdsStatus: typing_extensions.Literal[
        "UNKNOWN", "PASSING", "WARNING", "FAILING"
    ]
    reportUrl: str
    region: typing.List[str]
    filterStatus: typing_extensions.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    lastChangeTime: str

class ViolatingSitesResponse(typing_extensions.TypedDict, total=False):
    violatingSites: typing.List[SiteSummaryResponse]

class SiteSummaryResponse(typing_extensions.TypedDict, total=False):
    mobileSummary: PlatformSummary
    desktopSummary: PlatformSummary
    reviewedSite: str
