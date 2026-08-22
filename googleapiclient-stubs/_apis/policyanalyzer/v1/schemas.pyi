import typing

_list = list

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1Activity(typing.TypedDict, total=False):
    activity: dict[str, typing.Any]
    activityType: str
    fullResourceName: str
    observationPeriod: GoogleCloudPolicyanalyzerV1ObservationPeriod

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1ObservationPeriod(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class GoogleCloudPolicyanalyzerV1QueryActivityResponse(typing.TypedDict, total=False):
    activities: _list[GoogleCloudPolicyanalyzerV1Activity]
    nextPageToken: str
