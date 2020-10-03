import typing

import typing_extensions

class Webfont(typing_extensions.TypedDict, total=False):
    files: typing.Dict[str, typing.Any]
    lastModified: str
    category: str
    version: str
    family: str
    variants: typing.List[str]
    kind: str
    subsets: typing.List[str]

class WebfontList(typing_extensions.TypedDict, total=False):
    kind: str
    items: typing.List[Webfont]
