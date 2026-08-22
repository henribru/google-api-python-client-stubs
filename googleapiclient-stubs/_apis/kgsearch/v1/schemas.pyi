import typing

_list = list
AlternativeSearchResponse = typing.TypedDict(
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
