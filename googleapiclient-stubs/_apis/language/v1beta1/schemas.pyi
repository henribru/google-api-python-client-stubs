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
    language: str

@typing.type_check_only
class AnalyzeSentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeSentimentResponse(typing_extensions.TypedDict, total=False):
    documentSentiment: Sentiment
    language: str
    sentences: _list[Sentence]

@typing.type_check_only
class AnalyzeSyntaxRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeSyntaxResponse(typing_extensions.TypedDict, total=False):
    language: str
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
class AnnotateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    features: Features

@typing.type_check_only
class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    documentSentiment: Sentiment
    entities: _list[Entity]
    language: str
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
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

@typing.type_check_only
class Document(typing_extensions.TypedDict, total=False):
    content: str
    gcsContentUri: str
    language: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    mentions: _list[EntityMention]
    metadata: dict[str, typing.Any]
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
    ]

@typing.type_check_only
class EntityMention(typing_extensions.TypedDict, total=False):
    text: TextSpan
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

@typing.type_check_only
class Features(typing_extensions.TypedDict, total=False):
    extractDocumentSentiment: bool
    extractEntities: bool
    extractSyntax: bool

@typing.type_check_only
class PartOfSpeech(typing_extensions.TypedDict, total=False):
    aspect: typing_extensions.Literal[
        "ASPECT_UNKNOWN", "PERFECTIVE", "IMPERFECTIVE", "PROGRESSIVE"
    ]
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
    gender: typing_extensions.Literal[
        "GENDER_UNKNOWN", "FEMININE", "MASCULINE", "NEUTER"
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
    number: typing_extensions.Literal["NUMBER_UNKNOWN", "SINGULAR", "PLURAL", "DUAL"]
    person: typing_extensions.Literal[
        "PERSON_UNKNOWN", "FIRST", "SECOND", "THIRD", "REFLEXIVE_PERSON"
    ]
    proper: typing_extensions.Literal["PROPER_UNKNOWN", "PROPER", "NOT_PROPER"]
    reciprocity: typing_extensions.Literal[
        "RECIPROCITY_UNKNOWN", "RECIPROCAL", "NON_RECIPROCAL"
    ]
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
    tense: typing_extensions.Literal[
        "TENSE_UNKNOWN",
        "CONDITIONAL_TENSE",
        "FUTURE",
        "PAST",
        "PRESENT",
        "IMPERFECT",
        "PLUPERFECT",
    ]
    voice: typing_extensions.Literal["VOICE_UNKNOWN", "ACTIVE", "CAUSATIVE", "PASSIVE"]

@typing.type_check_only
class Sentence(typing_extensions.TypedDict, total=False):
    sentiment: Sentiment
    text: TextSpan

@typing.type_check_only
class Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    polarity: float
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

@typing.type_check_only
class Token(typing_extensions.TypedDict, total=False):
    dependencyEdge: DependencyEdge
    lemma: str
    partOfSpeech: PartOfSpeech
    text: TextSpan
