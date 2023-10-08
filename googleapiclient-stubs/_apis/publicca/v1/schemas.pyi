import typing

import typing_extensions

_list = list

@typing.type_check_only
class ExternalAccountKey(typing_extensions.TypedDict, total=False):
    b64MacKey: str
    keyId: str
    name: str
