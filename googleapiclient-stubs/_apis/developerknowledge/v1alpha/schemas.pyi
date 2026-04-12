import typing

import typing_extensions

_list = list

@typing.type_check_only
class BatchGetDocumentsResponse(typing_extensions.TypedDict, total=False):
    documents: _list[Document]

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    content: str
    description: str
    name: str
    uri: str

@typing.type_check_only
class DocumentChunk(typing_extensions.TypedDict, total=False):
    content: str
    id: str
    parent: str

@typing.type_check_only
class SearchDocumentChunksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[DocumentChunk]
