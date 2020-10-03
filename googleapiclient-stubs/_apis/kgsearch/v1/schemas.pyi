import typing

import typing_extensions

SearchResponse = typing_extensions.TypedDict(
    "SearchResponse",
    {
        "@type": typing.Any,
        "@context": typing.Any,
        "itemListElement": typing.List[typing.Any],
    },
    total=False,
)
