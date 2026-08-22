import typing

_list = list

@typing.type_check_only
class PlatformSummary(typing.TypedDict, total=False):
    betterAdsStatus: typing.Literal["UNKNOWN", "PASSING", "WARNING", "FAILING"]
    enforcementTime: str
    filterStatus: typing.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    lastChangeTime: str
    region: _list[typing.Literal["REGION_UNKNOWN", "REGION_A", "REGION_B", "REGION_C"]]
    reportUrl: str
    underReview: bool

@typing.type_check_only
class SiteSummaryResponse(typing.TypedDict, total=False):
    desktopSummary: PlatformSummary
    mobileSummary: PlatformSummary
    reviewedSite: str

@typing.type_check_only
class ViolatingSitesResponse(typing.TypedDict, total=False):
    violatingSites: _list[SiteSummaryResponse]
