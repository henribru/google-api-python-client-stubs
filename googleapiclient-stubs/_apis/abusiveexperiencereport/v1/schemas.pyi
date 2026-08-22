import typing

_list = list

@typing.type_check_only
class SiteSummaryResponse(typing.TypedDict, total=False):
    abusiveStatus: typing.Literal["UNKNOWN", "PASSING", "FAILING"]
    enforcementTime: str
    filterStatus: typing.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    lastChangeTime: str
    reportUrl: str
    reviewedSite: str
    underReview: bool

@typing.type_check_only
class ViolatingSitesResponse(typing.TypedDict, total=False):
    violatingSites: _list[SiteSummaryResponse]
