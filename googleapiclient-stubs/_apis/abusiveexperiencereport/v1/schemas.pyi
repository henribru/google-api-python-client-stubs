import typing

import typing_extensions
@typing.type_check_only
class SiteSummaryResponse(typing_extensions.TypedDict, total=False):
    abusiveStatus: typing_extensions.Literal["UNKNOWN", "PASSING", "FAILING"]
    enforcementTime: str
    filterStatus: typing_extensions.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    lastChangeTime: str
    reportUrl: str
    reviewedSite: str
    underReview: bool

@typing.type_check_only
class ViolatingSitesResponse(typing_extensions.TypedDict, total=False):
    violatingSites: typing.List[SiteSummaryResponse]
