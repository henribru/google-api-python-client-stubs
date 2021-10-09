import typing

import typing_extensions

_list = list

@typing.type_check_only
class Webfont(typing_extensions.TypedDict, total=False):
    category: str
    family: str
    files: dict[str, typing.Any]
    kind: str
    lastModified: str
    subsets: _list[str]
    variants: _list[str]
    version: str

@typing.type_check_only
class WebfontList(typing_extensions.TypedDict, total=False):
    items: _list[Webfont]
    kind: str
