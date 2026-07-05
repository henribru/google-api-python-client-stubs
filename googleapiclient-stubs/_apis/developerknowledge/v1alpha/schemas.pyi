import typing

import typing_extensions

_list = list

@typing.type_check_only
class Answer(typing_extensions.TypedDict, total=False):
    answerText: str
    citations: _list[AnswerCitation]
    references: _list[AnswerReference]

@typing.type_check_only
class AnswerCitation(typing_extensions.TypedDict, total=False):
    endIndex: int
    sources: _list[CitationSource]
    startIndex: int

@typing.type_check_only
class AnswerQueryRequest(typing_extensions.TypedDict, total=False):
    query: str

@typing.type_check_only
class AnswerQueryResponse(typing_extensions.TypedDict, total=False):
    answer: Answer

@typing.type_check_only
class AnswerReference(typing_extensions.TypedDict, total=False):
    documentReference: DocumentReference

@typing.type_check_only
class BatchGetDocumentsResponse(typing_extensions.TypedDict, total=False):
    documents: _list[Document]

@typing.type_check_only
class CitationSource(typing_extensions.TypedDict, total=False):
    referenceIndex: int

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    content: str
    dataSource: str
    description: str
    name: str
    title: str
    updateTime: str
    uri: str
    view: typing_extensions.Literal[
        "DOCUMENT_VIEW_UNSPECIFIED",
        "DOCUMENT_VIEW_BASIC",
        "DOCUMENT_VIEW_FULL",
        "DOCUMENT_VIEW_CONTENT",
    ]

@typing.type_check_only
class DocumentChunk(typing_extensions.TypedDict, total=False):
    content: str
    document: Document
    id: str
    parent: str

@typing.type_check_only
class DocumentReference(typing_extensions.TypedDict, total=False):
    documentChunk: DocumentChunk

@typing.type_check_only
class SearchDocumentChunksResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[DocumentChunk]
