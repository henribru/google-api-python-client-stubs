import typing

import typing_extensions

_list = list

@typing.type_check_only
class CustomApp(typing_extensions.TypedDict, total=False):
    languageCode: str
    packageName: str
    title: str
