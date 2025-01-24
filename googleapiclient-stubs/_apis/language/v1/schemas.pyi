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
class AnalyzeEntitySentimentRequest(typing_extensions.TypedDict, total=False):
    document: Document
    encodingType: typing_extensions.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeEntitySentimentResponse(typing_extensions.TypedDict, total=False):
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
    features: AnnotateTextRequestFeatures

@typing.type_check_only
class AnnotateTextRequestFeatures(typing_extensions.TypedDict, total=False):
    classificationModelOptions: ClassificationModelOptions
    classifyText: bool
    extractDocumentSentiment: bool
    extractEntities: bool
    extractEntitySentiment: bool
    extractSyntax: bool
    moderateText: bool

@typing.type_check_only
class AnnotateTextResponse(typing_extensions.TypedDict, total=False):
    categories: _list[ClassificationCategory]
    documentSentiment: Sentiment
    entities: _list[Entity]
    language: str
    moderationCategories: _list[ClassificationCategory]
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
class ClassificationCategory(typing_extensions.TypedDict, total=False):
    confidence: float
    name: str

@typing.type_check_only
class ClassificationModelOptions(typing_extensions.TypedDict, total=False):
    v1Model: ClassificationModelOptionsV1Model
    v2Model: ClassificationModelOptionsV2Model

@typing.type_check_only
class ClassificationModelOptionsV1Model(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ClassificationModelOptionsV2Model(typing_extensions.TypedDict, total=False):
    contentCategoriesVersion: typing_extensions.Literal[
        "CONTENT_CATEGORIES_VERSION_UNSPECIFIED", "V1", "V2"
    ]

@typing.type_check_only
class ClassifyTextRequest(typing_extensions.TypedDict, total=False):
    classificationModelOptions: ClassificationModelOptions
    document: Document

@typing.type_check_only
class ClassifyTextResponse(typing_extensions.TypedDict, total=False):
    categories: _list[ClassificationCategory]

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class CpuMetric(typing_extensions.TypedDict, total=False):
    coreNumber: str
    coreSec: str
    cpuType: typing_extensions.Literal[
        "UNKNOWN_CPU_TYPE",
        "A2",
        "A3",
        "C2",
        "C2D",
        "CUSTOM",
        "E2",
        "G2",
        "C3",
        "M2",
        "M1",
        "N1",
        "N2_CUSTOM",
        "N2",
        "N2D",
    ]
    machineSpec: typing_extensions.Literal[
        "UNKNOWN_MACHINE_SPEC",
        "N1_STANDARD_2",
        "N1_STANDARD_4",
        "N1_STANDARD_8",
        "N1_STANDARD_16",
        "N1_STANDARD_32",
        "N1_STANDARD_64",
        "N1_STANDARD_96",
        "N1_HIGHMEM_2",
        "N1_HIGHMEM_4",
        "N1_HIGHMEM_8",
        "N1_HIGHMEM_16",
        "N1_HIGHMEM_32",
        "N1_HIGHMEM_64",
        "N1_HIGHMEM_96",
        "N1_HIGHCPU_2",
        "N1_HIGHCPU_4",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_16",
        "N1_HIGHCPU_32",
        "N1_HIGHCPU_64",
        "N1_HIGHCPU_96",
        "A2_HIGHGPU_1G",
        "A2_HIGHGPU_2G",
        "A2_HIGHGPU_4G",
        "A2_HIGHGPU_8G",
        "A2_MEGAGPU_16G",
        "A2_ULTRAGPU_1G",
        "A2_ULTRAGPU_2G",
        "A2_ULTRAGPU_4G",
        "A2_ULTRAGPU_8G",
        "A3_HIGHGPU_1G",
        "A3_HIGHGPU_2G",
        "A3_HIGHGPU_4G",
        "A3_HIGHGPU_8G",
        "A3_MEGAGPU_8G",
        "A3_ULTRAGPU_8G",
        "E2_STANDARD_2",
        "E2_STANDARD_4",
        "E2_STANDARD_8",
        "E2_STANDARD_16",
        "E2_STANDARD_32",
        "E2_HIGHMEM_2",
        "E2_HIGHMEM_4",
        "E2_HIGHMEM_8",
        "E2_HIGHMEM_16",
        "E2_HIGHCPU_2",
        "E2_HIGHCPU_4",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_16",
        "E2_HIGHCPU_32",
        "N2_STANDARD_2",
        "N2_STANDARD_4",
        "N2_STANDARD_8",
        "N2_STANDARD_16",
        "N2_STANDARD_32",
        "N2_STANDARD_48",
        "N2_STANDARD_64",
        "N2_STANDARD_80",
        "N2_STANDARD_96",
        "N2_STANDARD_128",
        "N2_HIGHMEM_2",
        "N2_HIGHMEM_4",
        "N2_HIGHMEM_8",
        "N2_HIGHMEM_16",
        "N2_HIGHMEM_32",
        "N2_HIGHMEM_48",
        "N2_HIGHMEM_64",
        "N2_HIGHMEM_80",
        "N2_HIGHMEM_96",
        "N2_HIGHMEM_128",
        "N2_HIGHCPU_2",
        "N2_HIGHCPU_4",
        "N2_HIGHCPU_8",
        "N2_HIGHCPU_16",
        "N2_HIGHCPU_32",
        "N2_HIGHCPU_48",
        "N2_HIGHCPU_64",
        "N2_HIGHCPU_80",
        "N2_HIGHCPU_96",
        "N2D_STANDARD_2",
        "N2D_STANDARD_4",
        "N2D_STANDARD_8",
        "N2D_STANDARD_16",
        "N2D_STANDARD_32",
        "N2D_STANDARD_48",
        "N2D_STANDARD_64",
        "N2D_STANDARD_80",
        "N2D_STANDARD_96",
        "N2D_STANDARD_128",
        "N2D_STANDARD_224",
        "N2D_HIGHMEM_2",
        "N2D_HIGHMEM_4",
        "N2D_HIGHMEM_8",
        "N2D_HIGHMEM_16",
        "N2D_HIGHMEM_32",
        "N2D_HIGHMEM_48",
        "N2D_HIGHMEM_64",
        "N2D_HIGHMEM_80",
        "N2D_HIGHMEM_96",
        "N2D_HIGHCPU_2",
        "N2D_HIGHCPU_4",
        "N2D_HIGHCPU_8",
        "N2D_HIGHCPU_16",
        "N2D_HIGHCPU_32",
        "N2D_HIGHCPU_48",
        "N2D_HIGHCPU_64",
        "N2D_HIGHCPU_80",
        "N2D_HIGHCPU_96",
        "N2D_HIGHCPU_128",
        "N2D_HIGHCPU_224",
        "C2_STANDARD_4",
        "C2_STANDARD_8",
        "C2_STANDARD_16",
        "C2_STANDARD_30",
        "C2_STANDARD_60",
        "C2D_STANDARD_2",
        "C2D_STANDARD_4",
        "C2D_STANDARD_8",
        "C2D_STANDARD_16",
        "C2D_STANDARD_32",
        "C2D_STANDARD_56",
        "C2D_STANDARD_112",
        "C2D_HIGHCPU_2",
        "C2D_HIGHCPU_4",
        "C2D_HIGHCPU_8",
        "C2D_HIGHCPU_16",
        "C2D_HIGHCPU_32",
        "C2D_HIGHCPU_56",
        "C2D_HIGHCPU_112",
        "C2D_HIGHMEM_2",
        "C2D_HIGHMEM_4",
        "C2D_HIGHMEM_8",
        "C2D_HIGHMEM_16",
        "C2D_HIGHMEM_32",
        "C2D_HIGHMEM_56",
        "C2D_HIGHMEM_112",
        "G2_STANDARD_4",
        "G2_STANDARD_8",
        "G2_STANDARD_12",
        "G2_STANDARD_16",
        "G2_STANDARD_24",
        "G2_STANDARD_32",
        "G2_STANDARD_48",
        "G2_STANDARD_96",
        "C3_STANDARD_4",
        "C3_STANDARD_8",
        "C3_STANDARD_22",
        "C3_STANDARD_44",
        "C3_STANDARD_88",
        "C3_STANDARD_176",
        "C3_HIGHCPU_4",
        "C3_HIGHCPU_8",
        "C3_HIGHCPU_22",
        "C3_HIGHCPU_44",
        "C3_HIGHCPU_88",
        "C3_HIGHCPU_176",
        "C3_HIGHMEM_4",
        "C3_HIGHMEM_8",
        "C3_HIGHMEM_22",
        "C3_HIGHMEM_44",
        "C3_HIGHMEM_88",
        "C3_HIGHMEM_176",
    ]
    trackingLabels: dict[str, typing.Any]

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
class DiskMetric(typing_extensions.TypedDict, total=False):
    diskType: typing_extensions.Literal[
        "UNKNOWN_DISK_TYPE",
        "REGIONAL_SSD",
        "REGIONAL_STORAGE",
        "PD_SSD",
        "PD_STANDARD",
        "STORAGE_SNAPSHOT",
    ]
    gibSec: str

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
    sentiment: Sentiment
    text: TextSpan
    type: typing_extensions.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

@typing.type_check_only
class GpuMetric(typing_extensions.TypedDict, total=False):
    gpuSec: str
    gpuType: typing_extensions.Literal[
        "UNKNOWN_GPU_TYPE",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_TESLA_K80",
        "NVIDIA_L4",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_V100",
        "NVIDIA_H100_80GB",
    ]
    machineSpec: typing_extensions.Literal[
        "UNKNOWN_MACHINE_SPEC",
        "N1_STANDARD_2",
        "N1_STANDARD_4",
        "N1_STANDARD_8",
        "N1_STANDARD_16",
        "N1_STANDARD_32",
        "N1_STANDARD_64",
        "N1_STANDARD_96",
        "N1_HIGHMEM_2",
        "N1_HIGHMEM_4",
        "N1_HIGHMEM_8",
        "N1_HIGHMEM_16",
        "N1_HIGHMEM_32",
        "N1_HIGHMEM_64",
        "N1_HIGHMEM_96",
        "N1_HIGHCPU_2",
        "N1_HIGHCPU_4",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_16",
        "N1_HIGHCPU_32",
        "N1_HIGHCPU_64",
        "N1_HIGHCPU_96",
        "A2_HIGHGPU_1G",
        "A2_HIGHGPU_2G",
        "A2_HIGHGPU_4G",
        "A2_HIGHGPU_8G",
        "A2_MEGAGPU_16G",
        "A2_ULTRAGPU_1G",
        "A2_ULTRAGPU_2G",
        "A2_ULTRAGPU_4G",
        "A2_ULTRAGPU_8G",
        "A3_HIGHGPU_1G",
        "A3_HIGHGPU_2G",
        "A3_HIGHGPU_4G",
        "A3_HIGHGPU_8G",
        "A3_MEGAGPU_8G",
        "A3_ULTRAGPU_8G",
        "E2_STANDARD_2",
        "E2_STANDARD_4",
        "E2_STANDARD_8",
        "E2_STANDARD_16",
        "E2_STANDARD_32",
        "E2_HIGHMEM_2",
        "E2_HIGHMEM_4",
        "E2_HIGHMEM_8",
        "E2_HIGHMEM_16",
        "E2_HIGHCPU_2",
        "E2_HIGHCPU_4",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_16",
        "E2_HIGHCPU_32",
        "N2_STANDARD_2",
        "N2_STANDARD_4",
        "N2_STANDARD_8",
        "N2_STANDARD_16",
        "N2_STANDARD_32",
        "N2_STANDARD_48",
        "N2_STANDARD_64",
        "N2_STANDARD_80",
        "N2_STANDARD_96",
        "N2_STANDARD_128",
        "N2_HIGHMEM_2",
        "N2_HIGHMEM_4",
        "N2_HIGHMEM_8",
        "N2_HIGHMEM_16",
        "N2_HIGHMEM_32",
        "N2_HIGHMEM_48",
        "N2_HIGHMEM_64",
        "N2_HIGHMEM_80",
        "N2_HIGHMEM_96",
        "N2_HIGHMEM_128",
        "N2_HIGHCPU_2",
        "N2_HIGHCPU_4",
        "N2_HIGHCPU_8",
        "N2_HIGHCPU_16",
        "N2_HIGHCPU_32",
        "N2_HIGHCPU_48",
        "N2_HIGHCPU_64",
        "N2_HIGHCPU_80",
        "N2_HIGHCPU_96",
        "N2D_STANDARD_2",
        "N2D_STANDARD_4",
        "N2D_STANDARD_8",
        "N2D_STANDARD_16",
        "N2D_STANDARD_32",
        "N2D_STANDARD_48",
        "N2D_STANDARD_64",
        "N2D_STANDARD_80",
        "N2D_STANDARD_96",
        "N2D_STANDARD_128",
        "N2D_STANDARD_224",
        "N2D_HIGHMEM_2",
        "N2D_HIGHMEM_4",
        "N2D_HIGHMEM_8",
        "N2D_HIGHMEM_16",
        "N2D_HIGHMEM_32",
        "N2D_HIGHMEM_48",
        "N2D_HIGHMEM_64",
        "N2D_HIGHMEM_80",
        "N2D_HIGHMEM_96",
        "N2D_HIGHCPU_2",
        "N2D_HIGHCPU_4",
        "N2D_HIGHCPU_8",
        "N2D_HIGHCPU_16",
        "N2D_HIGHCPU_32",
        "N2D_HIGHCPU_48",
        "N2D_HIGHCPU_64",
        "N2D_HIGHCPU_80",
        "N2D_HIGHCPU_96",
        "N2D_HIGHCPU_128",
        "N2D_HIGHCPU_224",
        "C2_STANDARD_4",
        "C2_STANDARD_8",
        "C2_STANDARD_16",
        "C2_STANDARD_30",
        "C2_STANDARD_60",
        "C2D_STANDARD_2",
        "C2D_STANDARD_4",
        "C2D_STANDARD_8",
        "C2D_STANDARD_16",
        "C2D_STANDARD_32",
        "C2D_STANDARD_56",
        "C2D_STANDARD_112",
        "C2D_HIGHCPU_2",
        "C2D_HIGHCPU_4",
        "C2D_HIGHCPU_8",
        "C2D_HIGHCPU_16",
        "C2D_HIGHCPU_32",
        "C2D_HIGHCPU_56",
        "C2D_HIGHCPU_112",
        "C2D_HIGHMEM_2",
        "C2D_HIGHMEM_4",
        "C2D_HIGHMEM_8",
        "C2D_HIGHMEM_16",
        "C2D_HIGHMEM_32",
        "C2D_HIGHMEM_56",
        "C2D_HIGHMEM_112",
        "G2_STANDARD_4",
        "G2_STANDARD_8",
        "G2_STANDARD_12",
        "G2_STANDARD_16",
        "G2_STANDARD_24",
        "G2_STANDARD_32",
        "G2_STANDARD_48",
        "G2_STANDARD_96",
        "C3_STANDARD_4",
        "C3_STANDARD_8",
        "C3_STANDARD_22",
        "C3_STANDARD_44",
        "C3_STANDARD_88",
        "C3_STANDARD_176",
        "C3_HIGHCPU_4",
        "C3_HIGHCPU_8",
        "C3_HIGHCPU_22",
        "C3_HIGHCPU_44",
        "C3_HIGHCPU_88",
        "C3_HIGHCPU_176",
        "C3_HIGHMEM_4",
        "C3_HIGHMEM_8",
        "C3_HIGHMEM_22",
        "C3_HIGHMEM_44",
        "C3_HIGHMEM_88",
        "C3_HIGHMEM_176",
    ]
    trackingLabels: dict[str, typing.Any]

@typing.type_check_only
class InfraUsage(typing_extensions.TypedDict, total=False):
    cpuMetrics: _list[CpuMetric]
    diskMetrics: _list[DiskMetric]
    gpuMetrics: _list[GpuMetric]
    ramMetrics: _list[RamMetric]
    tpuMetrics: _list[TpuMetric]

@typing.type_check_only
class ModerateTextRequest(typing_extensions.TypedDict, total=False):
    document: Document

@typing.type_check_only
class ModerateTextResponse(typing_extensions.TypedDict, total=False):
    moderationCategories: _list[ClassificationCategory]

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
class RamMetric(typing_extensions.TypedDict, total=False):
    gibSec: str
    machineSpec: typing_extensions.Literal[
        "UNKNOWN_MACHINE_SPEC",
        "N1_STANDARD_2",
        "N1_STANDARD_4",
        "N1_STANDARD_8",
        "N1_STANDARD_16",
        "N1_STANDARD_32",
        "N1_STANDARD_64",
        "N1_STANDARD_96",
        "N1_HIGHMEM_2",
        "N1_HIGHMEM_4",
        "N1_HIGHMEM_8",
        "N1_HIGHMEM_16",
        "N1_HIGHMEM_32",
        "N1_HIGHMEM_64",
        "N1_HIGHMEM_96",
        "N1_HIGHCPU_2",
        "N1_HIGHCPU_4",
        "N1_HIGHCPU_8",
        "N1_HIGHCPU_16",
        "N1_HIGHCPU_32",
        "N1_HIGHCPU_64",
        "N1_HIGHCPU_96",
        "A2_HIGHGPU_1G",
        "A2_HIGHGPU_2G",
        "A2_HIGHGPU_4G",
        "A2_HIGHGPU_8G",
        "A2_MEGAGPU_16G",
        "A2_ULTRAGPU_1G",
        "A2_ULTRAGPU_2G",
        "A2_ULTRAGPU_4G",
        "A2_ULTRAGPU_8G",
        "A3_HIGHGPU_1G",
        "A3_HIGHGPU_2G",
        "A3_HIGHGPU_4G",
        "A3_HIGHGPU_8G",
        "A3_MEGAGPU_8G",
        "A3_ULTRAGPU_8G",
        "E2_STANDARD_2",
        "E2_STANDARD_4",
        "E2_STANDARD_8",
        "E2_STANDARD_16",
        "E2_STANDARD_32",
        "E2_HIGHMEM_2",
        "E2_HIGHMEM_4",
        "E2_HIGHMEM_8",
        "E2_HIGHMEM_16",
        "E2_HIGHCPU_2",
        "E2_HIGHCPU_4",
        "E2_HIGHCPU_8",
        "E2_HIGHCPU_16",
        "E2_HIGHCPU_32",
        "N2_STANDARD_2",
        "N2_STANDARD_4",
        "N2_STANDARD_8",
        "N2_STANDARD_16",
        "N2_STANDARD_32",
        "N2_STANDARD_48",
        "N2_STANDARD_64",
        "N2_STANDARD_80",
        "N2_STANDARD_96",
        "N2_STANDARD_128",
        "N2_HIGHMEM_2",
        "N2_HIGHMEM_4",
        "N2_HIGHMEM_8",
        "N2_HIGHMEM_16",
        "N2_HIGHMEM_32",
        "N2_HIGHMEM_48",
        "N2_HIGHMEM_64",
        "N2_HIGHMEM_80",
        "N2_HIGHMEM_96",
        "N2_HIGHMEM_128",
        "N2_HIGHCPU_2",
        "N2_HIGHCPU_4",
        "N2_HIGHCPU_8",
        "N2_HIGHCPU_16",
        "N2_HIGHCPU_32",
        "N2_HIGHCPU_48",
        "N2_HIGHCPU_64",
        "N2_HIGHCPU_80",
        "N2_HIGHCPU_96",
        "N2D_STANDARD_2",
        "N2D_STANDARD_4",
        "N2D_STANDARD_8",
        "N2D_STANDARD_16",
        "N2D_STANDARD_32",
        "N2D_STANDARD_48",
        "N2D_STANDARD_64",
        "N2D_STANDARD_80",
        "N2D_STANDARD_96",
        "N2D_STANDARD_128",
        "N2D_STANDARD_224",
        "N2D_HIGHMEM_2",
        "N2D_HIGHMEM_4",
        "N2D_HIGHMEM_8",
        "N2D_HIGHMEM_16",
        "N2D_HIGHMEM_32",
        "N2D_HIGHMEM_48",
        "N2D_HIGHMEM_64",
        "N2D_HIGHMEM_80",
        "N2D_HIGHMEM_96",
        "N2D_HIGHCPU_2",
        "N2D_HIGHCPU_4",
        "N2D_HIGHCPU_8",
        "N2D_HIGHCPU_16",
        "N2D_HIGHCPU_32",
        "N2D_HIGHCPU_48",
        "N2D_HIGHCPU_64",
        "N2D_HIGHCPU_80",
        "N2D_HIGHCPU_96",
        "N2D_HIGHCPU_128",
        "N2D_HIGHCPU_224",
        "C2_STANDARD_4",
        "C2_STANDARD_8",
        "C2_STANDARD_16",
        "C2_STANDARD_30",
        "C2_STANDARD_60",
        "C2D_STANDARD_2",
        "C2D_STANDARD_4",
        "C2D_STANDARD_8",
        "C2D_STANDARD_16",
        "C2D_STANDARD_32",
        "C2D_STANDARD_56",
        "C2D_STANDARD_112",
        "C2D_HIGHCPU_2",
        "C2D_HIGHCPU_4",
        "C2D_HIGHCPU_8",
        "C2D_HIGHCPU_16",
        "C2D_HIGHCPU_32",
        "C2D_HIGHCPU_56",
        "C2D_HIGHCPU_112",
        "C2D_HIGHMEM_2",
        "C2D_HIGHMEM_4",
        "C2D_HIGHMEM_8",
        "C2D_HIGHMEM_16",
        "C2D_HIGHMEM_32",
        "C2D_HIGHMEM_56",
        "C2D_HIGHMEM_112",
        "G2_STANDARD_4",
        "G2_STANDARD_8",
        "G2_STANDARD_12",
        "G2_STANDARD_16",
        "G2_STANDARD_24",
        "G2_STANDARD_32",
        "G2_STANDARD_48",
        "G2_STANDARD_96",
        "C3_STANDARD_4",
        "C3_STANDARD_8",
        "C3_STANDARD_22",
        "C3_STANDARD_44",
        "C3_STANDARD_88",
        "C3_STANDARD_176",
        "C3_HIGHCPU_4",
        "C3_HIGHCPU_8",
        "C3_HIGHCPU_22",
        "C3_HIGHCPU_44",
        "C3_HIGHCPU_88",
        "C3_HIGHCPU_176",
        "C3_HIGHMEM_4",
        "C3_HIGHMEM_8",
        "C3_HIGHMEM_22",
        "C3_HIGHMEM_44",
        "C3_HIGHMEM_88",
        "C3_HIGHMEM_176",
    ]
    memories: float
    ramType: typing_extensions.Literal[
        "UNKNOWN_RAM_TYPE",
        "A2",
        "A3",
        "C2",
        "C2D",
        "CUSTOM",
        "E2",
        "G2",
        "C3",
        "M2",
        "M1",
        "N1",
        "N2_CUSTOM",
        "N2",
        "N2D",
    ]
    trackingLabels: dict[str, typing.Any]

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

@typing.type_check_only
class Token(typing_extensions.TypedDict, total=False):
    dependencyEdge: DependencyEdge
    lemma: str
    partOfSpeech: PartOfSpeech
    text: TextSpan

@typing.type_check_only
class TpuMetric(typing_extensions.TypedDict, total=False):
    tpuSec: str
    tpuType: typing_extensions.Literal[
        "UNKNOWN_TPU_TYPE",
        "TPU_V2_POD",
        "TPU_V2",
        "TPU_V3_POD",
        "TPU_V3",
        "TPU_V5_LITEPOD",
    ]

@typing.type_check_only
class XPSArrayStats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    memberStats: XPSDataStats

@typing.type_check_only
class XPSBatchPredictResponse(typing_extensions.TypedDict, total=False):
    exampleSet: XPSExampleSet

@typing.type_check_only
class XPSBoundingBoxMetricsEntry(typing_extensions.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSBoundingBoxMetricsEntryConfidenceMetricsEntry]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class XPSBoundingBoxMetricsEntryConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class XPSCategoryStats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    topCategoryStats: _list[XPSCategoryStatsSingleCategoryStats]

@typing.type_check_only
class XPSCategoryStatsSingleCategoryStats(typing_extensions.TypedDict, total=False):
    count: str
    value: str

@typing.type_check_only
class XPSClassificationEvaluationMetrics(typing_extensions.TypedDict, total=False):
    auPrc: float
    auRoc: float
    baseAuPrc: float
    confidenceMetricsEntries: _list[XPSConfidenceMetricsEntry]
    confusionMatrix: XPSConfusionMatrix
    evaluatedExamplesCount: int
    logLoss: float

@typing.type_check_only
class XPSColorMap(typing_extensions.TypedDict, total=False):
    annotationSpecIdToken: str
    color: Color
    displayName: str
    intColor: XPSColorMapIntColor

@typing.type_check_only
class XPSColorMapIntColor(typing_extensions.TypedDict, total=False):
    blue: int
    green: int
    red: int

@typing.type_check_only
class XPSColumnSpec(typing_extensions.TypedDict, total=False):
    columnId: int
    dataStats: XPSDataStats
    dataType: XPSDataType
    displayName: str
    forecastingMetadata: XPSColumnSpecForecastingMetadata
    topCorrelatedColumns: _list[XPSColumnSpecCorrelatedColumn]

@typing.type_check_only
class XPSColumnSpecCorrelatedColumn(typing_extensions.TypedDict, total=False):
    columnId: int
    correlationStats: XPSCorrelationStats

@typing.type_check_only
class XPSColumnSpecForecastingMetadata(typing_extensions.TypedDict, total=False):
    columnType: typing_extensions.Literal[
        "COLUMN_TYPE_UNSPECIFIED",
        "KEY",
        "KEY_METADATA",
        "TIME_SERIES_AVAILABLE_PAST_ONLY",
        "TIME_SERIES_AVAILABLE_PAST_AND_FUTURE",
    ]

@typing.type_check_only
class XPSCommonStats(typing_extensions.TypedDict, total=False):
    distinctValueCount: str
    nullValueCount: str
    validValueCount: str

@typing.type_check_only
class XPSConfidenceMetricsEntry(typing_extensions.TypedDict, total=False):
    confidenceThreshold: float
    f1Score: float
    f1ScoreAt1: float
    falseNegativeCount: str
    falsePositiveCount: str
    falsePositiveRate: float
    falsePositiveRateAt1: float
    positionThreshold: int
    precision: float
    precisionAt1: float
    recall: float
    recallAt1: float
    trueNegativeCount: str
    truePositiveCount: str

@typing.type_check_only
class XPSConfusionMatrix(typing_extensions.TypedDict, total=False):
    annotationSpecIdToken: _list[str]
    category: _list[int]
    row: _list[XPSConfusionMatrixRow]
    sentimentLabel: _list[int]

@typing.type_check_only
class XPSConfusionMatrixRow(typing_extensions.TypedDict, total=False):
    count: _list[str]
    exampleCount: _list[int]

@typing.type_check_only
class XPSCoreMlFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSCorrelationStats(typing_extensions.TypedDict, total=False):
    cramersV: float

@typing.type_check_only
class XPSDataErrors(typing_extensions.TypedDict, total=False):
    count: int
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "UNSUPPORTED_AUDIO_FORMAT",
        "FILE_EXTENSION_MISMATCH_WITH_AUDIO_FORMAT",
        "FILE_TOO_LARGE",
        "MISSING_TRANSCRIPTION",
    ]

@typing.type_check_only
class XPSDataStats(typing_extensions.TypedDict, total=False):
    arrayStats: XPSArrayStats
    categoryStats: XPSCategoryStats
    distinctValueCount: str
    float64Stats: XPSFloat64Stats
    nullValueCount: str
    stringStats: XPSStringStats
    structStats: XPSStructStats
    timestampStats: XPSTimestampStats
    validValueCount: str

@typing.type_check_only
class XPSDataType(typing_extensions.TypedDict, total=False):
    compatibleDataTypes: _list[XPSDataType]
    listElementType: XPSDataType
    nullable: bool
    structType: XPSStructType
    timeFormat: str
    typeCode: typing_extensions.Literal[
        "TYPE_CODE_UNSPECIFIED",
        "FLOAT64",
        "TIMESTAMP",
        "STRING",
        "ARRAY",
        "STRUCT",
        "CATEGORY",
    ]

@typing.type_check_only
class XPSDockerFormat(typing_extensions.TypedDict, total=False):
    cpuArchitecture: typing_extensions.Literal[
        "CPU_ARCHITECTURE_UNSPECIFIED", "CPU_ARCHITECTURE_X86_64"
    ]
    gpuArchitecture: typing_extensions.Literal[
        "GPU_ARCHITECTURE_UNSPECIFIED", "GPU_ARCHITECTURE_NVIDIA"
    ]

@typing.type_check_only
class XPSEdgeTpuTfLiteFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSEvaluationMetrics(typing_extensions.TypedDict, total=False):
    annotationSpecIdToken: str
    category: int
    evaluatedExampleCount: int
    imageClassificationEvalMetrics: XPSClassificationEvaluationMetrics
    imageObjectDetectionEvalMetrics: XPSImageObjectDetectionEvaluationMetrics
    imageSegmentationEvalMetrics: XPSImageSegmentationEvaluationMetrics
    label: str
    regressionEvalMetrics: XPSRegressionEvaluationMetrics
    tablesClassificationEvalMetrics: XPSClassificationEvaluationMetrics
    tablesEvalMetrics: XPSTablesEvaluationMetrics
    textClassificationEvalMetrics: XPSClassificationEvaluationMetrics
    textExtractionEvalMetrics: XPSTextExtractionEvaluationMetrics
    textSentimentEvalMetrics: XPSTextSentimentEvaluationMetrics
    translationEvalMetrics: XPSTranslationEvaluationMetrics
    videoActionRecognitionEvalMetrics: XPSVideoActionRecognitionEvaluationMetrics
    videoClassificationEvalMetrics: XPSClassificationEvaluationMetrics
    videoObjectTrackingEvalMetrics: XPSVideoObjectTrackingEvaluationMetrics

@typing.type_check_only
class XPSEvaluationMetricsSet(typing_extensions.TypedDict, total=False):
    evaluationMetrics: _list[XPSEvaluationMetrics]
    fileSpec: XPSFileSpec
    numEvaluationMetrics: str

@typing.type_check_only
class XPSExampleSet(typing_extensions.TypedDict, total=False):
    fileSpec: XPSFileSpec
    fingerprint: str
    numExamples: str
    numInputSources: str

@typing.type_check_only
class XPSExportModelOutputConfig(typing_extensions.TypedDict, total=False):
    coreMlFormat: XPSCoreMlFormat
    dockerFormat: XPSDockerFormat
    edgeTpuTfLiteFormat: XPSEdgeTpuTfLiteFormat
    exportFirebaseAuxiliaryInfo: bool
    outputGcrUri: str
    outputGcsUri: str
    tfJsFormat: XPSTfJsFormat
    tfLiteFormat: XPSTfLiteFormat
    tfSavedModelFormat: XPSTfSavedModelFormat

@typing.type_check_only
class XPSFileSpec(typing_extensions.TypedDict, total=False):
    directoryPath: str
    fileFormat: typing_extensions.Literal[
        "FILE_FORMAT_UNKNOWN",
        "FILE_FORMAT_SSTABLE",
        "FILE_FORMAT_TRANSLATION_RKV",
        "FILE_FORMAT_RECORDIO",
        "FILE_FORMAT_RAW_CSV",
        "FILE_FORMAT_RAW_CAPACITOR",
    ]
    fileSpec: str
    singleFilePath: str

@typing.type_check_only
class XPSFloat64Stats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    histogramBuckets: _list[XPSFloat64StatsHistogramBucket]
    mean: float
    quantiles: _list[float]
    standardDeviation: float

@typing.type_check_only
class XPSFloat64StatsHistogramBucket(typing_extensions.TypedDict, total=False):
    count: str
    max: float
    min: float

@typing.type_check_only
class XPSImageClassificationTrainResponse(typing_extensions.TypedDict, total=False):
    classCount: str
    exportModelSpec: XPSImageExportModelSpec
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing_extensions.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostInNodeTime: str
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSImageExportModelSpec(typing_extensions.TypedDict, total=False):
    exportModelOutputConfig: _list[XPSExportModelOutputConfig]

@typing.type_check_only
class XPSImageModelArtifactSpec(typing_extensions.TypedDict, total=False):
    checkpointArtifact: XPSModelArtifactItem
    exportArtifact: _list[XPSModelArtifactItem]
    labelGcsUri: str
    servingArtifact: XPSModelArtifactItem
    tfJsBinaryGcsPrefix: str
    tfLiteMetadataGcsUri: str

@typing.type_check_only
class XPSImageModelServingSpec(typing_extensions.TypedDict, total=False):
    modelThroughputEstimation: _list[XPSImageModelServingSpecModelThroughputEstimation]
    nodeQps: float
    tfRuntimeVersion: str

@typing.type_check_only
class XPSImageModelServingSpecModelThroughputEstimation(
    typing_extensions.TypedDict, total=False
):
    computeEngineAcceleratorType: typing_extensions.Literal[
        "UNSPECIFIED",
        "NVIDIA_TESLA_K80",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_V100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_L4",
        "NVIDIA_H100_80GB",
        "NVIDIA_H100_MEGA_80GB",
        "NVIDIA_H200_141GB",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    latencyInMilliseconds: float
    nodeQps: float
    servomaticPartitionType: typing_extensions.Literal[
        "PARTITION_TYPE_UNSPECIFIED",
        "PARTITION_ZERO",
        "PARTITION_REDUCED_HOMING",
        "PARTITION_JELLYFISH",
        "PARTITION_CPU",
        "PARTITION_CUSTOM_STORAGE_CPU",
    ]

@typing.type_check_only
class XPSImageObjectDetectionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetricsEntries: _list[XPSBoundingBoxMetricsEntry]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class XPSImageObjectDetectionModelSpec(typing_extensions.TypedDict, total=False):
    classCount: str
    exportModelSpec: XPSImageExportModelSpec
    maxBoundingBoxCount: str
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing_extensions.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSImageSegmentationEvaluationMetrics(typing_extensions.TypedDict, total=False):
    confidenceMetricsEntries: _list[
        XPSImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class XPSImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: XPSConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class XPSImageSegmentationTrainResponse(typing_extensions.TypedDict, total=False):
    colorMaps: _list[XPSColorMap]
    exportModelSpec: XPSImageExportModelSpec
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing_extensions.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSIntegratedGradientsAttribution(typing_extensions.TypedDict, total=False):
    stepCount: int

@typing.type_check_only
class XPSMetricEntry(typing_extensions.TypedDict, total=False):
    argentumMetricId: str
    doubleValue: float
    int64Value: str
    metricName: str
    systemLabels: _list[XPSMetricEntryLabel]

@typing.type_check_only
class XPSMetricEntryLabel(typing_extensions.TypedDict, total=False):
    labelName: str
    labelValue: str

@typing.type_check_only
class XPSModelArtifactItem(typing_extensions.TypedDict, total=False):
    artifactFormat: typing_extensions.Literal[
        "ARTIFACT_FORMAT_UNSPECIFIED",
        "TF_CHECKPOINT",
        "TF_SAVED_MODEL",
        "TF_LITE",
        "EDGE_TPU_TF_LITE",
        "TF_JS",
        "CORE_ML",
    ]
    gcsUri: str

@typing.type_check_only
class XPSPreprocessResponse(typing_extensions.TypedDict, total=False):
    outputExampleSet: XPSExampleSet
    speechPreprocessResp: XPSSpeechPreprocessResponse
    tablesPreprocessResponse: XPSTablesPreprocessResponse
    translationPreprocessResp: XPSTranslationPreprocessResponse

@typing.type_check_only
class XPSRegressionEvaluationMetrics(typing_extensions.TypedDict, total=False):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    regressionMetricsEntries: _list[XPSRegressionMetricsEntry]
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class XPSRegressionMetricsEntry(typing_extensions.TypedDict, total=False):
    predictedValue: float
    trueValue: float

@typing.type_check_only
class XPSReportingMetrics(typing_extensions.TypedDict, total=False):
    effectiveTrainingDuration: str
    metricEntries: _list[XPSMetricEntry]

@typing.type_check_only
class XPSResponseExplanationMetadata(typing_extensions.TypedDict, total=False):
    inputs: dict[str, typing.Any]
    outputs: dict[str, typing.Any]

@typing.type_check_only
class XPSResponseExplanationMetadataInputMetadata(
    typing_extensions.TypedDict, total=False
):
    inputTensorName: str
    modality: typing_extensions.Literal[
        "MODALITY_UNSPECIFIED", "NUMERIC", "IMAGE", "CATEGORICAL"
    ]
    visualizationConfig: XPSVisualization

@typing.type_check_only
class XPSResponseExplanationMetadataOutputMetadata(
    typing_extensions.TypedDict, total=False
):
    outputTensorName: str

@typing.type_check_only
class XPSResponseExplanationParameters(typing_extensions.TypedDict, total=False):
    integratedGradientsAttribution: XPSIntegratedGradientsAttribution
    xraiAttribution: XPSXraiAttribution

@typing.type_check_only
class XPSResponseExplanationSpec(typing_extensions.TypedDict, total=False):
    explanationType: str
    metadata: XPSResponseExplanationMetadata
    parameters: XPSResponseExplanationParameters

@typing.type_check_only
class XPSRow(typing_extensions.TypedDict, total=False):
    columnIds: _list[int]
    values: _list[typing.Any]

@typing.type_check_only
class XPSSpeechEvaluationMetrics(typing_extensions.TypedDict, total=False):
    subModelEvaluationMetrics: _list[XPSSpeechEvaluationMetricsSubModelEvaluationMetric]

@typing.type_check_only
class XPSSpeechEvaluationMetricsSubModelEvaluationMetric(
    typing_extensions.TypedDict, total=False
):
    biasingModelType: typing_extensions.Literal[
        "BIASING_MODEL_TYPE_UNSPECIFIED",
        "COMMAND_AND_SEARCH",
        "PHONE_CALL",
        "VIDEO",
        "DEFAULT",
    ]
    isEnhancedModel: bool
    numDeletions: int
    numInsertions: int
    numSubstitutions: int
    numUtterances: int
    numWords: int
    sentenceAccuracy: float
    wer: float

@typing.type_check_only
class XPSSpeechModelSpec(typing_extensions.TypedDict, total=False):
    datasetId: str
    language: str
    subModelSpecs: _list[XPSSpeechModelSpecSubModelSpec]

@typing.type_check_only
class XPSSpeechModelSpecSubModelSpec(typing_extensions.TypedDict, total=False):
    biasingModelType: typing_extensions.Literal[
        "BIASING_MODEL_TYPE_UNSPECIFIED",
        "COMMAND_AND_SEARCH",
        "PHONE_CALL",
        "VIDEO",
        "DEFAULT",
    ]
    clientId: str
    contextId: str
    isEnhancedModel: bool

@typing.type_check_only
class XPSSpeechPreprocessResponse(typing_extensions.TypedDict, total=False):
    cnsTestDataPath: str
    cnsTrainDataPath: str
    prebuiltModelEvaluationMetrics: XPSSpeechEvaluationMetrics
    speechPreprocessStats: XPSSpeechPreprocessStats

@typing.type_check_only
class XPSSpeechPreprocessStats(typing_extensions.TypedDict, total=False):
    dataErrors: _list[XPSDataErrors]
    numHumanLabeledExamples: int
    numLogsExamples: int
    numMachineTranscribedExamples: int
    testExamplesCount: int
    testSentencesCount: int
    testWordsCount: int
    trainExamplesCount: int
    trainSentencesCount: int
    trainWordsCount: int

@typing.type_check_only
class XPSStringStats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    topUnigramStats: _list[XPSStringStatsUnigramStats]

@typing.type_check_only
class XPSStringStatsUnigramStats(typing_extensions.TypedDict, total=False):
    count: str
    value: str

@typing.type_check_only
class XPSStructStats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    fieldStats: dict[str, typing.Any]

@typing.type_check_only
class XPSStructType(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class XPSTableSpec(typing_extensions.TypedDict, total=False):
    columnSpecs: dict[str, typing.Any]
    importedDataSizeInBytes: str
    rowCount: str
    timeColumnId: int
    validRowCount: str

@typing.type_check_only
class XPSTablesClassificationMetrics(typing_extensions.TypedDict, total=False):
    curveMetrics: _list[XPSTablesClassificationMetricsCurveMetrics]

@typing.type_check_only
class XPSTablesClassificationMetricsCurveMetrics(
    typing_extensions.TypedDict, total=False
):
    aucPr: float
    aucRoc: float
    confidenceMetricsEntries: _list[XPSTablesConfidenceMetricsEntry]
    logLoss: float
    positionThreshold: int
    value: str

@typing.type_check_only
class XPSTablesConfidenceMetricsEntry(typing_extensions.TypedDict, total=False):
    confidenceThreshold: float
    f1Score: float
    falseNegativeCount: str
    falsePositiveCount: str
    falsePositiveRate: float
    precision: float
    recall: float
    trueNegativeCount: str
    truePositiveCount: str
    truePositiveRate: float

@typing.type_check_only
class XPSTablesDatasetMetadata(typing_extensions.TypedDict, total=False):
    mlUseColumnId: int
    primaryTableSpec: XPSTableSpec
    targetColumnCorrelations: dict[str, typing.Any]
    targetColumnId: int
    weightColumnId: int

@typing.type_check_only
class XPSTablesEvaluationMetrics(typing_extensions.TypedDict, total=False):
    classificationMetrics: XPSTablesClassificationMetrics
    regressionMetrics: XPSTablesRegressionMetrics

@typing.type_check_only
class XPSTablesModelColumnInfo(typing_extensions.TypedDict, total=False):
    columnId: int
    featureImportance: float

@typing.type_check_only
class XPSTablesModelStructure(typing_extensions.TypedDict, total=False):
    modelParameters: _list[XPSTablesModelStructureModelParameters]

@typing.type_check_only
class XPSTablesModelStructureModelParameters(typing_extensions.TypedDict, total=False):
    hyperparameters: _list[XPSTablesModelStructureModelParametersParameter]

@typing.type_check_only
class XPSTablesModelStructureModelParametersParameter(
    typing_extensions.TypedDict, total=False
):
    floatValue: float
    intValue: str
    name: str
    stringValue: str

@typing.type_check_only
class XPSTablesPreprocessResponse(typing_extensions.TypedDict, total=False):
    tablesDatasetMetadata: XPSTablesDatasetMetadata

@typing.type_check_only
class XPSTablesRegressionMetrics(typing_extensions.TypedDict, total=False):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    regressionMetricsEntries: _list[XPSRegressionMetricsEntry]
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class XPSTablesTrainResponse(typing_extensions.TypedDict, total=False):
    modelStructure: XPSTablesModelStructure
    predictionSampleRows: _list[XPSRow]
    tablesModelColumnInfo: _list[XPSTablesModelColumnInfo]
    trainCostMilliNodeHours: str

@typing.type_check_only
class XPSTablesTrainingOperationMetadata(typing_extensions.TypedDict, total=False):
    createModelStage: typing_extensions.Literal[
        "CREATE_MODEL_STAGE_UNSPECIFIED",
        "DATA_PREPROCESSING",
        "TRAINING",
        "EVALUATING",
        "MODEL_POST_PROCESSING",
    ]
    optimizationObjective: str
    topTrials: _list[XPSTuningTrial]
    trainBudgetMilliNodeHours: str
    trainingObjectivePoints: _list[XPSTrainingObjectivePoint]
    trainingStartTime: str

@typing.type_check_only
class XPSTextComponentModel(typing_extensions.TypedDict, total=False):
    batchPredictionModelGcsUri: str
    onlinePredictionModelGcsUri: str
    partition: typing_extensions.Literal[
        "PARTITION_TYPE_UNSPECIFIED",
        "PARTITION_ZERO",
        "PARTITION_REDUCED_HOMING",
        "PARTITION_JELLYFISH",
        "PARTITION_CPU",
        "PARTITION_CUSTOM_STORAGE_CPU",
    ]
    servingArtifact: XPSModelArtifactItem
    servoModelName: str
    submodelName: str
    submodelType: typing_extensions.Literal[
        "TEXT_MODEL_TYPE_UNSPECIFIED",
        "TEXT_MODEL_TYPE_DEFAULT",
        "TEXT_MODEL_TYPE_META_ARCHITECT",
        "TEXT_MODEL_TYPE_ATC",
        "TEXT_MODEL_TYPE_CLARA2",
        "TEXT_MODEL_TYPE_CHATBASE",
        "TEXT_MODEL_TYPE_SAFT_SPAN_LABELING",
        "TEXT_MODEL_TYPE_TEXT_EXTRACTION",
        "TEXT_MODEL_TYPE_RELATIONSHIP_EXTRACTION",
        "TEXT_MODEL_TYPE_COMPOSITE",
        "TEXT_MODEL_TYPE_ALL_MODELS",
        "TEXT_MODEL_TYPE_BERT",
        "TEXT_MODEL_TYPE_ENC_PALM",
    ]
    tfRuntimeVersion: str
    versionNumber: str

@typing.type_check_only
class XPSTextExtractionEvaluationMetrics(typing_extensions.TypedDict, total=False):
    bestF1ConfidenceMetrics: XPSConfidenceMetricsEntry
    confidenceMetricsEntries: _list[XPSConfidenceMetricsEntry]
    confusionMatrix: XPSConfusionMatrix
    perLabelConfidenceMetrics: dict[str, typing.Any]

@typing.type_check_only
class XPSTextSentimentEvaluationMetrics(typing_extensions.TypedDict, total=False):
    confusionMatrix: XPSConfusionMatrix
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class XPSTextToSpeechTrainResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSTextTrainResponse(typing_extensions.TypedDict, total=False):
    componentModel: _list[XPSTextComponentModel]

@typing.type_check_only
class XPSTfJsFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSTfLiteFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSTfSavedModelFormat(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class XPSTimestampStats(typing_extensions.TypedDict, total=False):
    commonStats: XPSCommonStats
    granularStats: dict[str, typing.Any]
    medianTimestampNanos: str

@typing.type_check_only
class XPSTimestampStatsGranularStats(typing_extensions.TypedDict, total=False):
    buckets: dict[str, typing.Any]

@typing.type_check_only
class XPSTrackMetricsEntry(typing_extensions.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSTrackMetricsEntryConfidenceMetricsEntry]
    iouThreshold: float
    meanBoundingBoxIou: float
    meanMismatchRate: float
    meanTrackingAveragePrecision: float

@typing.type_check_only
class XPSTrackMetricsEntryConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class XPSTrainResponse(typing_extensions.TypedDict, total=False):
    deployedModelSizeBytes: str
    errorAnalysisConfigs: _list[XPSVisionErrorAnalysisConfig]
    evaluatedExampleSet: XPSExampleSet
    evaluationMetricsSet: XPSEvaluationMetricsSet
    explanationConfigs: _list[XPSResponseExplanationSpec]
    imageClassificationTrainResp: XPSImageClassificationTrainResponse
    imageObjectDetectionTrainResp: XPSImageObjectDetectionModelSpec
    imageSegmentationTrainResp: XPSImageSegmentationTrainResponse
    modelToken: str
    speechTrainResp: XPSSpeechModelSpec
    tablesTrainResp: XPSTablesTrainResponse
    textToSpeechTrainResp: XPSTextToSpeechTrainResponse
    textTrainResp: XPSTextTrainResponse
    translationTrainResp: XPSTranslationTrainResponse
    videoActionRecognitionTrainResp: XPSVideoActionRecognitionTrainResponse
    videoClassificationTrainResp: XPSVideoClassificationTrainResponse
    videoObjectTrackingTrainResp: XPSVideoObjectTrackingTrainResponse

@typing.type_check_only
class XPSTrainingObjectivePoint(typing_extensions.TypedDict, total=False):
    createTime: str
    value: float

@typing.type_check_only
class XPSTranslationEvaluationMetrics(typing_extensions.TypedDict, total=False):
    baseBleuScore: float
    bleuScore: float

@typing.type_check_only
class XPSTranslationPreprocessResponse(typing_extensions.TypedDict, total=False):
    parsedExampleCount: str
    validExampleCount: str

@typing.type_check_only
class XPSTranslationTrainResponse(typing_extensions.TypedDict, total=False):
    modelType: typing_extensions.Literal["MODEL_TYPE_UNSPECIFIED", "LEGACY", "CURRENT"]

@typing.type_check_only
class XPSTuningTrial(typing_extensions.TypedDict, total=False):
    modelStructure: XPSTablesModelStructure
    trainingObjectivePoint: XPSTrainingObjectivePoint

@typing.type_check_only
class XPSVideoActionMetricsEntry(typing_extensions.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSVideoActionMetricsEntryConfidenceMetricsEntry]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class XPSVideoActionMetricsEntryConfidenceMetricsEntry(
    typing_extensions.TypedDict, total=False
):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class XPSVideoActionRecognitionEvaluationMetrics(
    typing_extensions.TypedDict, total=False
):
    evaluatedActionCount: int
    videoActionMetricsEntries: _list[XPSVideoActionMetricsEntry]

@typing.type_check_only
class XPSVideoActionRecognitionTrainResponse(typing_extensions.TypedDict, total=False):
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoBatchPredictOperationMetadata(typing_extensions.TypedDict, total=False):
    outputExamples: _list[str]

@typing.type_check_only
class XPSVideoClassificationTrainResponse(typing_extensions.TypedDict, total=False):
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoExportModelSpec(typing_extensions.TypedDict, total=False):
    exportModelOutputConfig: _list[XPSExportModelOutputConfig]

@typing.type_check_only
class XPSVideoModelArtifactSpec(typing_extensions.TypedDict, total=False):
    exportArtifact: _list[XPSModelArtifactItem]
    servingArtifact: XPSModelArtifactItem

@typing.type_check_only
class XPSVideoObjectTrackingEvaluationMetrics(typing_extensions.TypedDict, total=False):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetricsEntries: _list[XPSBoundingBoxMetricsEntry]
    evaluatedBoundingboxCount: int
    evaluatedFrameCount: int
    evaluatedTrackCount: int
    trackMeanAveragePrecision: float
    trackMeanBoundingBoxIou: float
    trackMeanMismatchRate: float
    trackMetricsEntries: _list[XPSTrackMetricsEntry]

@typing.type_check_only
class XPSVideoObjectTrackingTrainResponse(typing_extensions.TypedDict, total=False):
    exportModelSpec: XPSVideoExportModelSpec
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoTrainingOperationMetadata(typing_extensions.TypedDict, total=False):
    trainCostMilliNodeHour: str

@typing.type_check_only
class XPSVisionErrorAnalysisConfig(typing_extensions.TypedDict, total=False):
    exampleCount: int
    queryType: typing_extensions.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "QUERY_TYPE_ALL_SIMILAR",
        "QUERY_TYPE_SAME_CLASS_SIMILAR",
        "QUERY_TYPE_SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class XPSVisionTrainingOperationMetadata(typing_extensions.TypedDict, total=False):
    explanationUsage: InfraUsage

@typing.type_check_only
class XPSVisualization(typing_extensions.TypedDict, total=False):
    clipPercentLowerbound: float
    clipPercentUpperbound: float
    colorMap: typing_extensions.Literal[
        "COLOR_MAP_UNSPECIFIED",
        "PINK_GREEN",
        "VIRIDIS",
        "RED",
        "GREEN",
        "RED_GREEN",
        "PINK_WHITE_GREEN",
    ]
    overlayType: typing_extensions.Literal[
        "OVERLAY_TYPE_UNSPECIFIED", "NONE", "ORIGINAL", "GRAYSCALE", "MASK_BLACK"
    ]
    polarity: typing_extensions.Literal[
        "POLARITY_UNSPECIFIED", "POSITIVE", "NEGATIVE", "BOTH"
    ]
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "PIXELS", "OUTLINES"]

@typing.type_check_only
class XPSXpsOperationMetadata(typing_extensions.TypedDict, total=False):
    exampleCount: str
    reportingMetrics: XPSReportingMetrics
    tablesTrainingOperationMetadata: XPSTablesTrainingOperationMetadata
    videoBatchPredictOperationMetadata: XPSVideoBatchPredictOperationMetadata
    videoTrainingOperationMetadata: XPSVideoTrainingOperationMetadata
    visionTrainingOperationMetadata: XPSVisionTrainingOperationMetadata

@typing.type_check_only
class XPSXraiAttribution(typing_extensions.TypedDict, total=False):
    stepCount: int
