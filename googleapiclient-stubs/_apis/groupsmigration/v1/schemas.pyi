import typing

_list = list

@typing.type_check_only
class Groups(typing.TypedDict, total=False):
    kind: str
    responseCode: str
