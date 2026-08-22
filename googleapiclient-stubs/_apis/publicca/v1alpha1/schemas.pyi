import typing

_list = list

@typing.type_check_only
class ExternalAccountKey(typing.TypedDict, total=False):
    b64MacKey: str
    keyId: str
    name: str
