import typing

import typing_extensions

class GoogleExampleLibraryagentV1ListBooksResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    books: typing.List[GoogleExampleLibraryagentV1Book]

class GoogleExampleLibraryagentV1ListShelvesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    shelves: typing.List[GoogleExampleLibraryagentV1Shelf]

class GoogleExampleLibraryagentV1Shelf(typing_extensions.TypedDict, total=False):
    theme: str
    name: str

class GoogleExampleLibraryagentV1Book(typing_extensions.TypedDict, total=False):
    name: str
    read: bool
    author: str
    title: str
