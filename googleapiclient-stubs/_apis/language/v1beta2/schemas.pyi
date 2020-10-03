import typing

import typing_extensions

class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str

class Document(typing_extensions.TypedDict, total=False):
    language: str
    boilerplateHandling: typing_extensions.Literal[
        "BOILERPLATE_HANDLING_UNSPECIFIED", "SKIP_BOILERPLATE", "KEEP_BOILERPLATE"
    ]
    gcsContentUri: str
    referenceWebUri: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]
    content: str

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int
    message: str

class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: typing.List[Entity]
    language: str

class Sentiment(typing_extensions.TypedDict, total=False):
    magnitude: float
    score: float

class AnalyzeEntitySentimentResponse(typing_extensions.TypedDict, total=False):
    entities: typing.List[Entity]
    language: str

class PartOfSpeech(typing_extensions.TypedDict, total=False):
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
    gender: typing_extensions.Literal[
        "GENDER_UNKNOWN", "FEMININE", "MASCULINE", "NEUTER"
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
    proper: typing_extensions.Literal["PROPER_UNKNOWN", "PROPER", "NOT_PROPER"]
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
    number: typing_extensions.Literal["NUMBER_UNKNOWN", "SINGULAR", "PLURAL", "DUAL"]
    reciprocity: typing_extensions.Literal[
        "RECIPROCITY_UNKNOWN", "RECIPROCAL", "NON_RECIPROCAL"
    ]

class Entity(typing_extensions.TypedDict, total=False):
    mentions: typing.List[EntityMention]
    sentiment: Sentiment
    metadata: typing.Dict[str, typing.Any]
    name: str
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
    salience: float

class ClassifyTextRequest(typing_extensions.TypedDict, total=False):
    document: Document

class AnalyzeSyntaxResponse(typing_extensions.TypedDict, total=False):
    language: str
    sentences: typing.List[Sentence]
    tokens: typing.List[Token]

class AnalyzeSentimentResponse(typing_extensions.TypedDict, total=False):
    sentences: typing.List[Sentence]
    documentSentiment: Sentiment
    language: str

class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    tokens: typing.List[Token]
    sentences: typing.List[Sentence]
    entities: typing.List[Entity]
    categories: typing.List[ClassificationCategory]
    documentSentiment: Sentiment
    language: str

class ClassifyTextResponse(typing_extensions.TypedDict, total=False):
    categories: typing.List[ClassificationCategory]

class AnnotateTextRequest(typing_extensions.TypedDict, total=False):
    features: Features
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class AnalyzeEntitySentimentRequest(typing_extensions.TypedDict, total=False):
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]
    document: Document

class Token(typing_extensions.TypedDict, total=False):
    partOfSpeech: PartOfSpeech
    text: TextSpan
    dependencyEdge: DependencyEdge
    lemma: str

class AnalyzeSentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class Features(typing_extensions.TypedDict, total=False):
    extractDocumentSentiment: bool
    extractEntities: bool
    extractSyntax: bool
    classifyText: bool
    extractEntitySentiment: bool

class AnalyzeSyntaxRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

class EntityMention(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]
    sentiment: Sentiment
    text: TextSpan

class Sentence(typing_extensions.TypedDict, total=False):
    text: TextSpan
    sentiment: Sentiment

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

class ClassificationCategory(typing_extensions.TypedDict, total=False):
    confidence: float
    name: str
