import typing

import typing_extensions

class AnalyzeEntitySentimentResponse(typing_extensions.TypedDict, total=False):
    entities: typing.List[Entity]
    language: str

class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: typing.List[Entity]
    language: str

class Sentence(typing_extensions.TypedDict, total=False):
    text: TextSpan
    sentiment: Sentiment

class AnalyzeSentimentResponse(typing_extensions.TypedDict, total=False):
    language: str
    sentences: typing.List[Sentence]
    documentSentiment: Sentiment

class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str

class Features(typing_extensions.TypedDict, total=False):
    extractDocumentSentiment: bool
    classifyText: bool
    extractEntities: bool
    extractSyntax: bool
    extractEntitySentiment: bool

class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class PartOfSpeech(typing_extensions.TypedDict, total=False):
    reciprocity: typing_extensions.Literal[
        "RECIPROCITY_UNKNOWN", "RECIPROCAL", "NON_RECIPROCAL"
    ]
    voice: typing_extensions.Literal["VOICE_UNKNOWN", "ACTIVE", "CAUSATIVE", "PASSIVE"]
    person: typing_extensions.Literal[
        "PERSON_UNKNOWN", "FIRST", "SECOND", "THIRD", "REFLEXIVE_PERSON"
    ]
    aspect: typing_extensions.Literal[
        "ASPECT_UNKNOWN", "PERFECTIVE", "IMPERFECTIVE", "PROGRESSIVE"
    ]
    tense: typing_extensions.Literal[
        "TENSE_UNKNOWN",
        "CONDITIONAL_TENSE",
        "FUTURE",
        "PAST",
        "PRESENT",
        "IMPERFECT",
        "PLUPERFECT",
    ]
    mood: typing_extensions.Literal[
        "MOOD_UNKNOWN",
        "CONDITIONAL_MOOD",
        "IMPERATIVE",
        "INDICATIVE",
        "INTERROGATIVE",
        "JUSSIVE",
        "SUBJUNCTIVE",
    ]
    gender: typing_extensions.Literal[
        "GENDER_UNKNOWN", "FEMININE", "MASCULINE", "NEUTER"
    ]
    number: typing_extensions.Literal["NUMBER_UNKNOWN", "SINGULAR", "PLURAL", "DUAL"]
    case: typing_extensions.Literal[
        "CASE_UNKNOWN",
        "ACCUSATIVE",
        "ADVERBIAL",
        "COMPLEMENTIVE",
        "DATIVE",
        "GENITIVE",
        "INSTRUMENTAL",
        "LOCATIVE",
        "NOMINATIVE",
        "OBLIQUE",
        "PARTITIVE",
        "PREPOSITIONAL",
        "REFLEXIVE_CASE",
        "RELATIVE_CASE",
        "VOCATIVE",
    ]
    proper: typing_extensions.Literal["PROPER_UNKNOWN", "PROPER", "NOT_PROPER"]
    tag: typing_extensions.Literal[
        "UNKNOWN",
        "ADJ",
        "ADP",
        "ADV",
        "CONJ",
        "DET",
        "NOUN",
        "NUM",
        "PRON",
        "PRT",
        "PUNCT",
        "VERB",
        "X",
        "AFFIX",
    ]
    form: typing_extensions.Literal[
        "FORM_UNKNOWN",
        "ADNOMIAL",
        "AUXILIARY",
        "COMPLEMENTIZER",
        "FINAL_ENDING",
        "GERUND",
        "REALIS",
        "IRREALIS",
        "SHORT",
        "LONG",
        "ORDER",
        "SPECIFIC",
    ]

class Entity(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    name: str
    salience: float
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
    sentiment: Sentiment
    mentions: typing.List[EntityMention]

class Token(typing_extensions.TypedDict, total=False):
    text: TextSpan
    partOfSpeech: PartOfSpeech
    lemma: str
    dependencyEdge: DependencyEdge

class DependencyEdge(typing_extensions.TypedDict, total=False):
    headTokenIndex: int
    label: typing_extensions.Literal[
        "UNKNOWN",
        "ABBREV",
        "ACOMP",
        "ADVCL",
        "ADVMOD",
        "AMOD",
        "APPOS",
        "ATTR",
        "AUX",
        "AUXPASS",
        "CC",
        "CCOMP",
        "CONJ",
        "CSUBJ",
        "CSUBJPASS",
        "DEP",
        "DET",
        "DISCOURSE",
        "DOBJ",
        "EXPL",
        "GOESWITH",
        "IOBJ",
        "MARK",
        "MWE",
        "MWV",
        "NEG",
        "NN",
        "NPADVMOD",
        "NSUBJ",
        "NSUBJPASS",
        "NUM",
        "NUMBER",
        "P",
        "PARATAXIS",
        "PARTMOD",
        "PCOMP",
        "POBJ",
        "POSS",
        "POSTNEG",
        "PRECOMP",
        "PRECONJ",
        "PREDET",
        "PREF",
        "PREP",
        "PRONL",
        "PRT",
        "PS",
        "QUANTMOD",
        "RCMOD",
        "RCMODREL",
        "RDROP",
        "REF",
        "REMNANT",
        "REPARANDUM",
        "ROOT",
        "SNUM",
        "SUFF",
        "TMOD",
        "TOPIC",
        "VMOD",
        "VOCATIVE",
        "XCOMP",
        "SUFFIX",
        "TITLE",
        "ADVPHMOD",
        "AUXCAUS",
        "AUXVV",
        "DTMOD",
        "FOREIGN",
        "KW",
        "LIST",
        "NOMC",
        "NOMCSUBJ",
        "NOMCSUBJPASS",
        "NUMC",
        "COP",
        "DISLOCATED",
        "ASP",
        "GMOD",
        "GOBJ",
        "INFMOD",
        "MES",
        "NCOMP",
    ]

class AnalyzeSentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class AnalyzeSyntaxRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class AnalyzeSyntaxResponse(typing_extensions.TypedDict, total=False):
    language: str
    tokens: typing.List[Token]
    sentences: typing.List[Sentence]

class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    tokens: typing.List[Token]
    categories: typing.List[ClassificationCategory]
    language: str
    entities: typing.List[Entity]
    sentences: typing.List[Sentence]
    documentSentiment: Sentiment

class ClassifyTextResponse(typing_extensions.TypedDict, total=False):
    categories: typing.List[ClassificationCategory]

class AnalyzeEntitySentimentRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class AnnotateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document
    features: Features
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class Document(typing_extensions.TypedDict, total=False):
    language: str
    gcsContentUri: str
    content: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class ClassificationCategory(typing_extensions.TypedDict, total=False):
    name: str
    confidence: float

class EntityMention(typing_extensions.TypedDict, total=False):
    text: TextSpan
    sentiment: Sentiment
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

class Sentiment(typing_extensions.TypedDict, total=False):
    score: float
    magnitude: float

class ClassifyTextRequest(typing_extensions.TypedDict, total=False):
    document: Document
