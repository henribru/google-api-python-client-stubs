import typing

_list = list

@typing.type_check_only
class Axis(typing.TypedDict, total=False):
    end: float
    start: float
    tag: str

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    name: str
    weight: float

@typing.type_check_only
class Webfont(typing.TypedDict, total=False):
    axes: _list[Axis]
    category: str
    colorCapabilities: _list[str]
    family: str
    files: dict[str, typing.Any]
    kind: str
    lastModified: str
    menu: str
    subsets: _list[str]
    tags: _list[Tag]
    variants: _list[str]
    version: str

@typing.type_check_only
class WebfontList(typing.TypedDict, total=False):
    items: _list[Webfont]
    kind: str
