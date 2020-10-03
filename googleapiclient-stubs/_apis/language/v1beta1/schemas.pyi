import typing

import typing_extensions

class AnalyzeSyntaxRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class AnalyzeSentimentResponse(typing_extensions.TypedDict, total=False):
    language: str
    documentSentiment: Sentiment
    sentences: typing.List[Sentence]

class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    language: str
    entities: typing.List[Entity]

class AnalyzeSentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class Token(typing_extensions.TypedDict, total=False):
    text: TextSpan
    dependencyEdge: DependencyEdge
    lemma: str
    partOfSpeech: PartOfSpeech

class Entity(typing_extensions.TypedDict, total=False):
    name: str
    mentions: typing.List[EntityMention]
    salience: float
    metadata: typing.Dict[str, typing.Any]
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

class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    language: str
    entities: typing.List[Entity]
    sentences: typing.List[Sentence]
    tokens: typing.List[Token]
    documentSentiment: Sentiment

class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class Document(typing_extensions.TypedDict, total=False):
    gcsContentUri: str
    content: str
    language: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

class Features(typing_extensions.TypedDict, total=False):
    extractEntities: bool
    extractDocumentSentiment: bool
    extractSyntax: bool

class PartOfSpeech(typing_extensions.TypedDict, total=False):
    reciprocity: typing_extensions.Literal[
        "RECIPROCITY_UNKNOWN", "RECIPROCAL", "NON_RECIPROCAL"
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
    aspect: typing_extensions.Literal[
        "ASPECT_UNKNOWN", "PERFECTIVE", "IMPERFECTIVE", "PROGRESSIVE"
    ]
    gender: typing_extensions.Literal[
        "GENDER_UNKNOWN", "FEMININE", "MASCULINE", "NEUTER"
    ]
    proper: typing_extensions.Literal["PROPER_UNKNOWN", "PROPER", "NOT_PROPER"]
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
    number: typing_extensions.Literal["NUMBER_UNKNOWN", "SINGULAR", "PLURAL", "DUAL"]
    tense: typing_extensions.Literal[
        "TENSE_UNKNOWN",
        "CONDITIONAL_TENSE",
        "FUTURE",
        "PAST",
        "PRESENT",
        "IMPERFECT",
        "PLUPERFECT",
    ]
    person: typing_extensions.Literal[
        "PERSON_UNKNOWN", "FIRST", "SECOND", "THIRD", "REFLEXIVE_PERSON"
    ]
    voice: typing_extensions.Literal["VOICE_UNKNOWN", "ACTIVE", "CAUSATIVE", "PASSIVE"]
    mood: typing_extensions.Literal[
        "MOOD_UNKNOWN",
        "CONDITIONAL_MOOD",
        "IMPERATIVE",
        "INDICATIVE",
        "INTERROGATIVE",
        "JUSSIVE",
        "SUBJUNCTIVE",
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

class AnnotateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    features: Features

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Sentiment(typing_extensions.TypedDict, total=False):
    score: float
    polarity: float
    magnitude: float

class EntityMention(typing_extensions.TypedDict, total=False):
    text: TextSpan
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

class DependencyEdge(typing_extensions.TypedDict, total=False):
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
    headTokenIndex: int

class AnalyzeSyntaxResponse(typing_extensions.TypedDict, total=False):
    language: str
    tokens: typing.List[Token]
    sentences: typing.List[Sentence]

class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str

class Sentence(typing_extensions.TypedDict, total=False):
    text: TextSpan
    sentiment: Sentiment
