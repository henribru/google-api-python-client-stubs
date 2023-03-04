import typing

import typing_extensions

_list = list

@typing.type_check_only
class AcmeChallengeSet(typing_extensions.TypedDict, total=False):
    record: _list[AcmeTxtRecord]

@typing.type_check_only
class AcmeTxtRecord(typing_extensions.TypedDict, total=False):
    digest: str
    fqdn: str
    updateTime: str

@typing.type_check_only
class RotateChallengesRequest(typing_extensions.TypedDict, total=False):
    accessToken: str
    keepExpiredRecords: bool
    recordsToAdd: _list[AcmeTxtRecord]
    recordsToRemove: _list[AcmeTxtRecord]
