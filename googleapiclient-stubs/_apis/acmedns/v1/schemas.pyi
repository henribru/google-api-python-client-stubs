import typing

_list = list

@typing.type_check_only
class AcmeChallengeSet(typing.TypedDict, total=False):
    record: _list[AcmeTxtRecord]

@typing.type_check_only
class AcmeTxtRecord(typing.TypedDict, total=False):
    digest: str
    fqdn: str
    updateTime: str

@typing.type_check_only
class RotateChallengesRequest(typing.TypedDict, total=False):
    accessToken: str
    keepExpiredRecords: bool
    recordsToAdd: _list[AcmeTxtRecord]
    recordsToRemove: _list[AcmeTxtRecord]
