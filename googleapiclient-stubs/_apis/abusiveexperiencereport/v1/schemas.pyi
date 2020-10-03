import typing

import typing_extensions

class SiteSummaryResponse(typing_extensions.TypedDict, total=False):
    reportUrl: str
    underReview: bool
    enforcementTime: str
    lastChangeTime: str
    filterStatus: typing_extensions.Literal["UNKNOWN", "ON", "OFF", "PAUSED", "PENDING"]
    abusiveStatus: typing_extensions.Literal["UNKNOWN", "PASSING", "FAILING"]
    reviewedSite: str

class ViolatingSitesResponse(typing_extensions.TypedDict, total=False):
    violatingSites: typing.List[SiteSummaryResponse]
