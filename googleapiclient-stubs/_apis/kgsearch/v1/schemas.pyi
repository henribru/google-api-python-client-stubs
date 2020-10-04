import typing

import typing_extensions

AlternativeSearchResponse = typing_extensions.TypedDict(
    "AlternativeSearchResponse",
    {
        "@context": typing.Any,
        "@type": typing.Any,
        "itemListElement": typing.List[typing.Any],
    },
    total=False,
)
@typing.type_check_only
class SearchResponse(AlternativeSearchResponse): ...
