import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1Activity(typing_extensions.TypedDict, total=False):
    activity: dict[str, typing.Any]
    activityType: str
    fullResourceName: str
    observationPeriod: GoogleCloudPolicyanalyzerV1ObservationPeriod

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1ObservationPeriod(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1QueryActivityResponse(
    typing_extensions.TypedDict, total=False
):
    activities: _list[GoogleCloudPolicyanalyzerV1Activity]
    nextPageToken: str
