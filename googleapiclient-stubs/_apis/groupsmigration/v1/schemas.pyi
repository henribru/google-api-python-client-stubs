import typing

import typing_extensions
@typing.type_check_only
class Groups(typing_extensions.TypedDict, total=False):
    kind: str
    responseCode: str
