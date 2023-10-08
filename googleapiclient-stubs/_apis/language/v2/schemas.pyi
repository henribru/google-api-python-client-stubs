import typing

import typing_extensions

_list = list

@typing.type_check_only
class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: _list[Entity]
    languageCode: str
    languageSupported: bool

@typing.type_check_only
class AnalyzeSentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeSentimentResponse(typing_extensions.TypedDict, total=False):
    documentSentiment: Sentiment
    languageCode: str
    languageSupported: bool
    sentences: _list[Sentence]

@typing.type_check_only
class AnnotateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    features: Features

@typing.type_check_only
class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    categories: _list[ClassificationCategory]
    documentSentiment: Sentiment
    entities: _list[Entity]
    languageCode: str
    languageSupported: bool
    moderationCategories: _list[ClassificationCategory]
    sentences: _list[Sentence]

@typing.type_check_only
class ClassificationCategory(typing_extensions.TypedDict, total=False):
    confidence: float
    name: str

@typing.type_check_only
class ClassifyTextRequest(typing_extensions.TypedDict, total=False):
    document: Document

@typing.type_check_only
class ClassifyTextResponse(typing_extensions.TypedDict, total=False):
    categories: _list[ClassificationCategory]
    languageCode: str
    languageSupported: bool

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    content: str
    gcsContentUri: str
    languageCode: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    mentions: _list[EntityMention]
    metadata: dict[str, typing.Any]
    name: str
    sentiment: Sentiment
    type: typing_extensions.Literal[
        "UNKNOWN",
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "EVENT",
        "WORK_OF_ART",
        "CONSUMER_GOOD",
        "OTHER",
        "PHONE_NUMBER",
        "ADDRESS",
        "DATE",
        "NUMBER",
        "PRICE",
    ]

@typing.type_check_only
class EntityMention(typing_extensions.TypedDict, total=False):
    probability: float
    sentiment: Sentiment
    text: TextSpan
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

@typing.type_check_only
class Features(typing_extensions.TypedDict, total=False):
    classifyText: bool
    extractDocumentSentiment: bool
    extractEntities: bool
    moderateText: bool

@typing.type_check_only
class ModerateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document

@typing.type_check_only
class ModerateTextResponse(typing_extensions.TypedDict, total=False):
    languageCode: str
    languageSupported: bool
    moderationCategories: _list[ClassificationCategory]

@typing.type_check_only
class Sentence(typing_extensions.TypedDict, total=False):
    sentiment: Sentiment
    text: TextSpan

@typing.type_check_only
class Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str
