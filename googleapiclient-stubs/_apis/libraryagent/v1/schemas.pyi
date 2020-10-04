import typing

import typing_extensions
@typing.type_check_only
class GoogleExampleLibraryagentV1Book(typing_extensions.TypedDict, total=False):
    author: str
    name: str
    read: bool
    title: str

@typing.type_check_only
class GoogleExampleLibraryagentV1ListBooksResponse(
    typing_extensions.TypedDict, total=False
):
    books: typing.List[GoogleExampleLibraryagentV1Book]
    nextPageToken: str

@typing.type_check_only
class GoogleExampleLibraryagentV1ListShelvesResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    shelves: typing.List[GoogleExampleLibraryagentV1Shelf]

@typing.type_check_only
class GoogleExampleLibraryagentV1Shelf(typing_extensions.TypedDict, total=False):
    name: str
    theme: str
