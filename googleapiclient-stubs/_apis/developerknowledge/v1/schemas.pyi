import typing

_list = list

@typing.type_check_only
class Answer(typing.TypedDict, total=False):
    answerText: str
    citations: _list[AnswerCitation]
    references: _list[AnswerReference]

@typing.type_check_only
class AnswerCitation(typing.TypedDict, total=False):
    endIndex: int
    sources: _list[CitationSource]
    startIndex: int

@typing.type_check_only
class AnswerQueryRequest(typing.TypedDict, total=False):
    query: str

@typing.type_check_only
class AnswerQueryResponse(typing.TypedDict, total=False):
    answer: Answer

@typing.type_check_only
class AnswerReference(typing.TypedDict, total=False):
    documentReference: DocumentReference

@typing.type_check_only
class BatchGetDocumentsResponse(typing.TypedDict, total=False):
    documents: _list[Document]

@typing.type_check_only
class CitationSource(typing.TypedDict, total=False):
    referenceIndex: int

@typing.type_check_only
class Document(typing.TypedDict, total=False):
    content: str
    contentLengthBytes: int
    dataSource: str
    description: str
    name: str
    title: str
    updateTime: str
    uri: str
    view: typing.Literal[
        "DOCUMENT_VIEW_UNSPECIFIED",
        "DOCUMENT_VIEW_BASIC",
        "DOCUMENT_VIEW_FULL",
        "DOCUMENT_VIEW_CONTENT",
    ]

@typing.type_check_only
class DocumentChunk(typing.TypedDict, total=False):
    content: str
    document: Document
    id: str
    parent: str

@typing.type_check_only
class DocumentReference(typing.TypedDict, total=False):
    documentChunk: DocumentChunk

@typing.type_check_only
class SearchDocumentChunksResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[DocumentChunk]
