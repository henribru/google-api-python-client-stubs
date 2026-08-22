import typing

_list = list

@typing.type_check_only
class GoogleExampleLibraryagentV1Book(typing.TypedDict, total=False):
    author: str
    name: str
    read: bool
    title: str

@typing.type_check_only
class GoogleExampleLibraryagentV1ListBooksResponse(typing.TypedDict, total=False):
    books: _list[GoogleExampleLibraryagentV1Book]
    nextPageToken: str

@typing.type_check_only
class GoogleExampleLibraryagentV1ListShelvesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    shelves: _list[GoogleExampleLibraryagentV1Shelf]

@typing.type_check_only
class GoogleExampleLibraryagentV1Shelf(typing.TypedDict, total=False):
    name: str
    theme: str
