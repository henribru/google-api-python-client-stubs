import typing

import typing_extensions
@typing.type_check_only
class Webfont(typing_extensions.TypedDict, total=False):
    category: str
    family: str
    files: typing.Dict[str, typing.Any]
    kind: str
    lastModified: str
    subsets: typing.List[str]
    variants: typing.List[str]
    version: str

@typing.type_check_only
class WebfontList(typing_extensions.TypedDict, total=False):
    items: typing.List[Webfont]
    kind: str
