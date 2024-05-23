import typing

import typing_extensions

_list = list

@typing.type_check_only
class Axis(typing_extensions.TypedDict, total=False):
    end: float
    start: float
    tag: str

@typing.type_check_only
class Webfont(typing_extensions.TypedDict, total=False):
    axes: _list[Axis]
    category: str
    colorCapabilities: _list[str]
    family: str
    files: dict[str, typing.Any]
    kind: str
    lastModified: str
    menu: str
    subsets: _list[str]
    variants: _list[str]
    version: str

@typing.type_check_only
class WebfontList(typing_extensions.TypedDict, total=False):
    items: _list[Webfont]
    kind: str
