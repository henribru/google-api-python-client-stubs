import typing

import typing_extensions

_list = list
AlternativeSearchResponse = typing_extensions.TypedDict(
    "AlternativeSearchResponse",
    {
        "@context": typing.Any,
        "@type": typing.Any,
        "itemListElement": _list[typing.Any],
    },
    total=False,
)

@typing.type_check_only
class SearchResponse(AlternativeSearchResponse): ...
