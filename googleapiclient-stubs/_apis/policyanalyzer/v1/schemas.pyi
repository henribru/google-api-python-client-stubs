import typing

import typing_extensions

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1Activity(typing_extensions.TypedDict, total=False):
    activity: typing.Dict[str, typing.Any]
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
    activities: typing.List[GoogleCloudPolicyanalyzerV1Activity]
    nextPageToken: str
