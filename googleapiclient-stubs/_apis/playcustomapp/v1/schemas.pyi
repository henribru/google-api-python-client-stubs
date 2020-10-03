import typing

import typing_extensions

class CustomApp(typing_extensions.TypedDict, total=False):
    title: str
    languageCode: str
    packageName: str
