import typing

import typing_extensions

_list = list

@typing.type_check_only
class CheckFreeAccessResponse(typing_extensions.TypedDict, total=False):
    isAllowed: bool
