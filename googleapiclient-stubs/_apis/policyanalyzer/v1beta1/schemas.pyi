import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1beta1Activity(
    typing_extensions.TypedDict, total=False
):
    activity: dict[str, typing.Any]
    activityType: str
    fullResourceName: str
    observationPeriod: GoogleCloudPolicyanalyzerV1beta1ObservationPeriod

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1beta1ObservationPeriod(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1beta1QueryActivityResponse(
    typing_extensions.TypedDict, total=False
):
    activities: _list[GoogleCloudPolicyanalyzerV1beta1Activity]
    nextPageToken: str
