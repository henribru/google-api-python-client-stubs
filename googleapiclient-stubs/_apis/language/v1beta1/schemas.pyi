import typing

_list = list

@typing.type_check_only
class AnalyzeEntitiesRequest(typing.TypedDict, total=False):
    document: Document
    encodingType: typing.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeEntitiesResponse(typing.TypedDict, total=False):
    entities: _list[Entity]
    language: str

@typing.type_check_only
class AnalyzeSentimentRequest(typing.TypedDict, total=False):
    document: Document
    encodingType: typing.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeSentimentResponse(typing.TypedDict, total=False):
    documentSentiment: Sentiment
    language: str
    sentences: _list[Sentence]

@typing.type_check_only
class AnalyzeSyntaxRequest(typing.TypedDict, total=False):
    document: Document
    encodingType: typing.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeSyntaxResponse(typing.TypedDict, total=False):
    language: str
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
class AnnotateTextRequest(typing.TypedDict, total=False):
    document: Document
    encodingType: typing.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    features: Features

@typing.type_check_only
class AnnotateTextResponse(typing.TypedDict, total=False):
    documentSentiment: Sentiment
    entities: _list[Entity]
    language: str
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
class DependencyEdge(typing.TypedDict, total=False):
    headTokenIndex: int
    label: typing.Literal[
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
class Document(typing.TypedDict, total=False):
    content: str
    gcsContentUri: str
    language: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

@typing.type_check_only
class Entity(typing.TypedDict, total=False):
    mentions: _list[EntityMention]
    metadata: dict[str, typing.Any]
    name: str
    salience: float
    type: typing.Literal[
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
class EntityMention(typing.TypedDict, total=False):
    text: TextSpan
    type: typing.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

@typing.type_check_only
class Features(typing.TypedDict, total=False):
    extractDocumentSentiment: bool
    extractEntities: bool
    extractSyntax: bool

@typing.type_check_only
class PartOfSpeech(typing.TypedDict, total=False):
    aspect: typing.Literal[
        "ASPECT_UNKNOWN", "PERFECTIVE", "IMPERFECTIVE", "PROGRESSIVE"
    ]
    case: typing.Literal[
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
    form: typing.Literal[
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
    gender: typing.Literal["GENDER_UNKNOWN", "FEMININE", "MASCULINE", "NEUTER"]
    mood: typing.Literal[
        "MOOD_UNKNOWN",
        "CONDITIONAL_MOOD",
        "IMPERATIVE",
        "INDICATIVE",
        "INTERROGATIVE",
        "JUSSIVE",
        "SUBJUNCTIVE",
    ]
    number: typing.Literal["NUMBER_UNKNOWN", "SINGULAR", "PLURAL", "DUAL"]
    person: typing.Literal[
        "PERSON_UNKNOWN", "FIRST", "SECOND", "THIRD", "REFLEXIVE_PERSON"
    ]
    proper: typing.Literal["PROPER_UNKNOWN", "PROPER", "NOT_PROPER"]
    reciprocity: typing.Literal["RECIPROCITY_UNKNOWN", "RECIPROCAL", "NON_RECIPROCAL"]
    tag: typing.Literal[
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
    tense: typing.Literal[
        "TENSE_UNKNOWN",
        "CONDITIONAL_TENSE",
        "FUTURE",
        "PAST",
        "PRESENT",
        "IMPERFECT",
        "PLUPERFECT",
    ]
    voice: typing.Literal["VOICE_UNKNOWN", "ACTIVE", "CAUSATIVE", "PASSIVE"]

@typing.type_check_only
class Sentence(typing.TypedDict, total=False):
    sentiment: Sentiment
    text: TextSpan

@typing.type_check_only
class Sentiment(typing.TypedDict, total=False):
    magnitude: float
    polarity: float
    score: float

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TextSpan(typing.TypedDict, total=False):
    beginOffset: int
    content: str

@typing.type_check_only
class Token(typing.TypedDict, total=False):
    dependencyEdge: DependencyEdge
    lemma: str
    partOfSpeech: PartOfSpeech
    text: TextSpan
