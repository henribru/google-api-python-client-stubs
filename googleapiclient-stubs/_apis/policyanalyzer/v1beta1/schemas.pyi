import typing

import typing_extensions

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1beta1Activity(
    typing_extensions.TypedDict, total=False
):
    activity: typing.Dict[str, typing.Any]
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
    activities: typing.List[GoogleCloudPolicyanalyzerV1beta1Activity]
    nextPageToken: str
