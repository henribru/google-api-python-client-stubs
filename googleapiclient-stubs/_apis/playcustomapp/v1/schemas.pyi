import typing

import typing_extensions
@typing.type_check_only
class CustomApp(typing_extensions.TypedDict, total=False):
    languageCode: str
    packageName: str
    title: str
