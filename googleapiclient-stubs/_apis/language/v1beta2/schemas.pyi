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
class AnalyzeEntitySentimentRequest(typing.TypedDict, total=False):
    document: Document
    encodingType: typing.Literal["NONE", "UTF8", "UTF16", "UTF32"]

@typing.type_check_only
class AnalyzeEntitySentimentResponse(typing.TypedDict, total=False):
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
    features: AnnotateTextRequestFeatures

@typing.type_check_only
class AnnotateTextRequestFeatures(typing.TypedDict, total=False):
    classificationModelOptions: ClassificationModelOptions
    classifyText: bool
    extractDocumentSentiment: bool
    extractEntities: bool
    extractEntitySentiment: bool
    extractSyntax: bool
    moderateText: bool

@typing.type_check_only
class AnnotateTextResponse(typing.TypedDict, total=False):
    categories: _list[ClassificationCategory]
    documentSentiment: Sentiment
    entities: _list[Entity]
    language: str
    moderationCategories: _list[ClassificationCategory]
    sentences: _list[Sentence]
    tokens: _list[Token]

@typing.type_check_only
class ClassificationCategory(typing.TypedDict, total=False):
    confidence: float
    name: str

@typing.type_check_only
class ClassificationModelOptions(typing.TypedDict, total=False):
    v1Model: ClassificationModelOptionsV1Model
    v2Model: ClassificationModelOptionsV2Model

@typing.type_check_only
class ClassificationModelOptionsV1Model(typing.TypedDict, total=False): ...

@typing.type_check_only
class ClassificationModelOptionsV2Model(typing.TypedDict, total=False):
    contentCategoriesVersion: typing.Literal[
        "CONTENT_CATEGORIES_VERSION_UNSPECIFIED", "V1", "V2"
    ]

@typing.type_check_only
class ClassifyTextRequest(typing.TypedDict, total=False):
    classificationModelOptions: ClassificationModelOptions
    document: Document

@typing.type_check_only
class ClassifyTextResponse(typing.TypedDict, total=False):
    categories: _list[ClassificationCategory]

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class CpuMetric(typing.TypedDict, total=False):
    coreNumber: str
    coreSec: str
    cpuType: typing.Literal[
        "UNKNOWN_CPU_TYPE",
        "A2",
        "A3",
        "A4",
        "A4X",
        "C2",
        "C2D",
        "CUSTOM",
        "E2",
        "G2",
        "G4",
        "C3",
        "C4",
        "C4A",
        "C4D",
        "N4",
        "N4A",
        "C3D",
        "M2",
        "M1",
        "N1",
        "N2_CUSTOM",
        "N2",
        "N2D",
    ]
    machineSpec: typing.Literal[
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
        "A3_EDGEGPU_8G",
        "A4_HIGHGPU_8G",
        "A4X_HIGHGPU_4G",
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
        "G4_STANDARD_48",
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
        "C4_STANDARD_8",
        "C4_STANDARD_16",
        "C4_STANDARD_24",
        "C4_STANDARD_32",
        "C4_STANDARD_48",
        "C4_STANDARD_96",
        "C4_STANDARD_144",
        "C4_STANDARD_192",
        "C4_STANDARD_288",
        "C4_HIGHCPU_8",
        "C4_HIGHCPU_16",
        "C4_HIGHCPU_24",
        "C4_HIGHCPU_32",
        "C4_HIGHCPU_48",
        "C4_HIGHCPU_96",
        "C4_HIGHCPU_144",
        "C4_HIGHCPU_192",
        "C4_HIGHCPU_288",
        "C4_HIGHMEM_8",
        "C4_HIGHMEM_16",
        "C4_HIGHMEM_24",
        "C4_HIGHMEM_32",
        "C4_HIGHMEM_48",
        "C4_HIGHMEM_96",
        "C4_HIGHMEM_144",
        "C4_HIGHMEM_192",
        "C4_HIGHMEM_288",
        "C4A_STANDARD_8",
        "C4A_STANDARD_16",
        "C4A_STANDARD_32",
        "C4A_STANDARD_48",
        "C4A_STANDARD_64",
        "C4A_STANDARD_72",
        "C4A_HIGHCPU_8",
        "C4A_HIGHCPU_16",
        "C4A_HIGHCPU_32",
        "C4A_HIGHCPU_48",
        "C4A_HIGHCPU_64",
        "C4A_HIGHCPU_72",
        "C4A_HIGHMEM_8",
        "C4A_HIGHMEM_16",
        "C4A_HIGHMEM_32",
        "C4A_HIGHMEM_48",
        "C4A_HIGHMEM_64",
        "C4A_HIGHMEM_72",
        "C4D_STANDARD_2",
        "C4D_STANDARD_4",
        "C4D_STANDARD_8",
        "C4D_STANDARD_16",
        "C4D_STANDARD_32",
        "C4D_STANDARD_48",
        "C4D_STANDARD_64",
        "C4D_STANDARD_96",
        "C4D_STANDARD_192",
        "C4D_STANDARD_384",
        "C4D_HIGHCPU_2",
        "C4D_HIGHCPU_4",
        "C4D_HIGHCPU_8",
        "C4D_HIGHCPU_16",
        "C4D_HIGHCPU_32",
        "C4D_HIGHCPU_48",
        "C4D_HIGHCPU_64",
        "C4D_HIGHCPU_96",
        "C4D_HIGHCPU_192",
        "C4D_HIGHCPU_384",
        "C4D_HIGHMEM_2",
        "C4D_HIGHMEM_4",
        "C4D_HIGHMEM_8",
        "C4D_HIGHMEM_16",
        "C4D_HIGHMEM_32",
        "C4D_HIGHMEM_48",
        "C4D_HIGHMEM_64",
        "C4D_HIGHMEM_96",
        "C4D_HIGHMEM_192",
        "C4D_HIGHMEM_384",
        "N4_STANDARD_2",
        "N4_STANDARD_4",
        "N4_STANDARD_8",
        "N4_STANDARD_16",
        "N4_STANDARD_32",
        "N4_STANDARD_48",
        "N4_STANDARD_64",
        "N4_STANDARD_80",
        "N4_HIGHCPU_2",
        "N4_HIGHCPU_4",
        "N4_HIGHCPU_8",
        "N4_HIGHCPU_16",
        "N4_HIGHCPU_32",
        "N4_HIGHCPU_48",
        "N4_HIGHCPU_64",
        "N4_HIGHCPU_80",
        "N4_HIGHMEM_2",
        "N4_HIGHMEM_4",
        "N4_HIGHMEM_8",
        "N4_HIGHMEM_16",
        "N4_HIGHMEM_32",
        "N4_HIGHMEM_48",
        "N4_HIGHMEM_64",
        "N4_HIGHMEM_80",
        "N4A_STANDARD_2",
        "N4A_STANDARD_4",
        "N4A_STANDARD_8",
        "N4A_STANDARD_16",
        "N4A_STANDARD_32",
        "N4A_STANDARD_48",
        "N4A_STANDARD_64",
        "N4A_HIGHCPU_2",
        "N4A_HIGHCPU_4",
        "N4A_HIGHCPU_8",
        "N4A_HIGHCPU_16",
        "N4A_HIGHCPU_32",
        "N4A_HIGHCPU_48",
        "N4A_HIGHCPU_64",
        "N4A_HIGHMEM_2",
        "N4A_HIGHMEM_4",
        "N4A_HIGHMEM_8",
        "N4A_HIGHMEM_16",
        "N4A_HIGHMEM_32",
        "N4A_HIGHMEM_48",
        "N4A_HIGHMEM_64",
        "C3D_STANDARD_8",
        "C3D_STANDARD_16",
        "C3D_STANDARD_30",
        "C3D_STANDARD_60",
        "C3D_STANDARD_90",
        "C3D_STANDARD_180",
        "C3D_STANDARD_360",
        "C3D_HIGHCPU_8",
        "C3D_HIGHCPU_16",
        "C3D_HIGHCPU_30",
        "C3D_HIGHCPU_60",
        "C3D_HIGHCPU_90",
        "C3D_HIGHCPU_180",
        "C3D_HIGHCPU_360",
        "C3D_HIGHMEM_8",
        "C3D_HIGHMEM_16",
        "C3D_HIGHMEM_30",
        "C3D_HIGHMEM_60",
        "C3D_HIGHMEM_90",
        "C3D_HIGHMEM_180",
        "C3D_HIGHMEM_360",
    ]
    trackingLabels: dict[str, typing.Any]

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
class DiskMetric(typing.TypedDict, total=False):
    diskType: typing.Literal[
        "UNKNOWN_DISK_TYPE",
        "REGIONAL_SSD",
        "REGIONAL_STORAGE",
        "PD_SSD",
        "PD_STANDARD",
        "STORAGE_SNAPSHOT",
    ]
    gibSec: str

@typing.type_check_only
class Document(typing.TypedDict, total=False):
    boilerplateHandling: typing.Literal[
        "BOILERPLATE_HANDLING_UNSPECIFIED", "SKIP_BOILERPLATE", "KEEP_BOILERPLATE"
    ]
    content: str
    gcsContentUri: str
    language: str
    referenceWebUri: str
    type: typing.Literal["TYPE_UNSPECIFIED", "PLAIN_TEXT", "HTML"]

@typing.type_check_only
class Entity(typing.TypedDict, total=False):
    mentions: _list[EntityMention]
    metadata: dict[str, typing.Any]
    name: str
    salience: float
    sentiment: Sentiment
    type: typing.Literal[
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
class EntityMention(typing.TypedDict, total=False):
    sentiment: Sentiment
    text: TextSpan
    type: typing.Literal["TYPE_UNKNOWN", "PROPER", "COMMON"]

@typing.type_check_only
class GpuMetric(typing.TypedDict, total=False):
    gpuSec: str
    gpuType: typing.Literal[
        "UNKNOWN_GPU_TYPE",
        "NVIDIA_TESLA_A100",
        "NVIDIA_A100_80GB",
        "NVIDIA_B200",
        "NVIDIA_GB200",
        "NVIDIA_TESLA_K80",
        "NVIDIA_L4",
        "NVIDIA_TESLA_P100",
        "NVIDIA_TESLA_P4",
        "NVIDIA_TESLA_T4",
        "NVIDIA_TESLA_V100",
        "NVIDIA_H100_80GB",
        "NVIDIA_H100_MEGA_80GB",
        "NVIDIA_H200_141GB",
        "NVIDIA_RTX_PRO_6000",
    ]
    machineSpec: typing.Literal[
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
        "A3_EDGEGPU_8G",
        "A4_HIGHGPU_8G",
        "A4X_HIGHGPU_4G",
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
        "G4_STANDARD_48",
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
        "C4_STANDARD_8",
        "C4_STANDARD_16",
        "C4_STANDARD_24",
        "C4_STANDARD_32",
        "C4_STANDARD_48",
        "C4_STANDARD_96",
        "C4_STANDARD_144",
        "C4_STANDARD_192",
        "C4_STANDARD_288",
        "C4_HIGHCPU_8",
        "C4_HIGHCPU_16",
        "C4_HIGHCPU_24",
        "C4_HIGHCPU_32",
        "C4_HIGHCPU_48",
        "C4_HIGHCPU_96",
        "C4_HIGHCPU_144",
        "C4_HIGHCPU_192",
        "C4_HIGHCPU_288",
        "C4_HIGHMEM_8",
        "C4_HIGHMEM_16",
        "C4_HIGHMEM_24",
        "C4_HIGHMEM_32",
        "C4_HIGHMEM_48",
        "C4_HIGHMEM_96",
        "C4_HIGHMEM_144",
        "C4_HIGHMEM_192",
        "C4_HIGHMEM_288",
        "C4A_STANDARD_8",
        "C4A_STANDARD_16",
        "C4A_STANDARD_32",
        "C4A_STANDARD_48",
        "C4A_STANDARD_64",
        "C4A_STANDARD_72",
        "C4A_HIGHCPU_8",
        "C4A_HIGHCPU_16",
        "C4A_HIGHCPU_32",
        "C4A_HIGHCPU_48",
        "C4A_HIGHCPU_64",
        "C4A_HIGHCPU_72",
        "C4A_HIGHMEM_8",
        "C4A_HIGHMEM_16",
        "C4A_HIGHMEM_32",
        "C4A_HIGHMEM_48",
        "C4A_HIGHMEM_64",
        "C4A_HIGHMEM_72",
        "C4D_STANDARD_2",
        "C4D_STANDARD_4",
        "C4D_STANDARD_8",
        "C4D_STANDARD_16",
        "C4D_STANDARD_32",
        "C4D_STANDARD_48",
        "C4D_STANDARD_64",
        "C4D_STANDARD_96",
        "C4D_STANDARD_192",
        "C4D_STANDARD_384",
        "C4D_HIGHCPU_2",
        "C4D_HIGHCPU_4",
        "C4D_HIGHCPU_8",
        "C4D_HIGHCPU_16",
        "C4D_HIGHCPU_32",
        "C4D_HIGHCPU_48",
        "C4D_HIGHCPU_64",
        "C4D_HIGHCPU_96",
        "C4D_HIGHCPU_192",
        "C4D_HIGHCPU_384",
        "C4D_HIGHMEM_2",
        "C4D_HIGHMEM_4",
        "C4D_HIGHMEM_8",
        "C4D_HIGHMEM_16",
        "C4D_HIGHMEM_32",
        "C4D_HIGHMEM_48",
        "C4D_HIGHMEM_64",
        "C4D_HIGHMEM_96",
        "C4D_HIGHMEM_192",
        "C4D_HIGHMEM_384",
        "N4_STANDARD_2",
        "N4_STANDARD_4",
        "N4_STANDARD_8",
        "N4_STANDARD_16",
        "N4_STANDARD_32",
        "N4_STANDARD_48",
        "N4_STANDARD_64",
        "N4_STANDARD_80",
        "N4_HIGHCPU_2",
        "N4_HIGHCPU_4",
        "N4_HIGHCPU_8",
        "N4_HIGHCPU_16",
        "N4_HIGHCPU_32",
        "N4_HIGHCPU_48",
        "N4_HIGHCPU_64",
        "N4_HIGHCPU_80",
        "N4_HIGHMEM_2",
        "N4_HIGHMEM_4",
        "N4_HIGHMEM_8",
        "N4_HIGHMEM_16",
        "N4_HIGHMEM_32",
        "N4_HIGHMEM_48",
        "N4_HIGHMEM_64",
        "N4_HIGHMEM_80",
        "N4A_STANDARD_2",
        "N4A_STANDARD_4",
        "N4A_STANDARD_8",
        "N4A_STANDARD_16",
        "N4A_STANDARD_32",
        "N4A_STANDARD_48",
        "N4A_STANDARD_64",
        "N4A_HIGHCPU_2",
        "N4A_HIGHCPU_4",
        "N4A_HIGHCPU_8",
        "N4A_HIGHCPU_16",
        "N4A_HIGHCPU_32",
        "N4A_HIGHCPU_48",
        "N4A_HIGHCPU_64",
        "N4A_HIGHMEM_2",
        "N4A_HIGHMEM_4",
        "N4A_HIGHMEM_8",
        "N4A_HIGHMEM_16",
        "N4A_HIGHMEM_32",
        "N4A_HIGHMEM_48",
        "N4A_HIGHMEM_64",
        "C3D_STANDARD_8",
        "C3D_STANDARD_16",
        "C3D_STANDARD_30",
        "C3D_STANDARD_60",
        "C3D_STANDARD_90",
        "C3D_STANDARD_180",
        "C3D_STANDARD_360",
        "C3D_HIGHCPU_8",
        "C3D_HIGHCPU_16",
        "C3D_HIGHCPU_30",
        "C3D_HIGHCPU_60",
        "C3D_HIGHCPU_90",
        "C3D_HIGHCPU_180",
        "C3D_HIGHCPU_360",
        "C3D_HIGHMEM_8",
        "C3D_HIGHMEM_16",
        "C3D_HIGHMEM_30",
        "C3D_HIGHMEM_60",
        "C3D_HIGHMEM_90",
        "C3D_HIGHMEM_180",
        "C3D_HIGHMEM_360",
    ]
    trackingLabels: dict[str, typing.Any]

@typing.type_check_only
class InfraUsage(typing.TypedDict, total=False):
    cpuMetrics: _list[CpuMetric]
    diskMetrics: _list[DiskMetric]
    gpuMetrics: _list[GpuMetric]
    ramMetrics: _list[RamMetric]
    tpuMetrics: _list[TpuMetric]

@typing.type_check_only
class ModerateTextRequest(typing.TypedDict, total=False):
    document: Document

@typing.type_check_only
class ModerateTextResponse(typing.TypedDict, total=False):
    moderationCategories: _list[ClassificationCategory]

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
class RamMetric(typing.TypedDict, total=False):
    gibSec: str
    machineSpec: typing.Literal[
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
        "A3_EDGEGPU_8G",
        "A4_HIGHGPU_8G",
        "A4X_HIGHGPU_4G",
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
        "G4_STANDARD_48",
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
        "C4_STANDARD_8",
        "C4_STANDARD_16",
        "C4_STANDARD_24",
        "C4_STANDARD_32",
        "C4_STANDARD_48",
        "C4_STANDARD_96",
        "C4_STANDARD_144",
        "C4_STANDARD_192",
        "C4_STANDARD_288",
        "C4_HIGHCPU_8",
        "C4_HIGHCPU_16",
        "C4_HIGHCPU_24",
        "C4_HIGHCPU_32",
        "C4_HIGHCPU_48",
        "C4_HIGHCPU_96",
        "C4_HIGHCPU_144",
        "C4_HIGHCPU_192",
        "C4_HIGHCPU_288",
        "C4_HIGHMEM_8",
        "C4_HIGHMEM_16",
        "C4_HIGHMEM_24",
        "C4_HIGHMEM_32",
        "C4_HIGHMEM_48",
        "C4_HIGHMEM_96",
        "C4_HIGHMEM_144",
        "C4_HIGHMEM_192",
        "C4_HIGHMEM_288",
        "C4A_STANDARD_8",
        "C4A_STANDARD_16",
        "C4A_STANDARD_32",
        "C4A_STANDARD_48",
        "C4A_STANDARD_64",
        "C4A_STANDARD_72",
        "C4A_HIGHCPU_8",
        "C4A_HIGHCPU_16",
        "C4A_HIGHCPU_32",
        "C4A_HIGHCPU_48",
        "C4A_HIGHCPU_64",
        "C4A_HIGHCPU_72",
        "C4A_HIGHMEM_8",
        "C4A_HIGHMEM_16",
        "C4A_HIGHMEM_32",
        "C4A_HIGHMEM_48",
        "C4A_HIGHMEM_64",
        "C4A_HIGHMEM_72",
        "C4D_STANDARD_2",
        "C4D_STANDARD_4",
        "C4D_STANDARD_8",
        "C4D_STANDARD_16",
        "C4D_STANDARD_32",
        "C4D_STANDARD_48",
        "C4D_STANDARD_64",
        "C4D_STANDARD_96",
        "C4D_STANDARD_192",
        "C4D_STANDARD_384",
        "C4D_HIGHCPU_2",
        "C4D_HIGHCPU_4",
        "C4D_HIGHCPU_8",
        "C4D_HIGHCPU_16",
        "C4D_HIGHCPU_32",
        "C4D_HIGHCPU_48",
        "C4D_HIGHCPU_64",
        "C4D_HIGHCPU_96",
        "C4D_HIGHCPU_192",
        "C4D_HIGHCPU_384",
        "C4D_HIGHMEM_2",
        "C4D_HIGHMEM_4",
        "C4D_HIGHMEM_8",
        "C4D_HIGHMEM_16",
        "C4D_HIGHMEM_32",
        "C4D_HIGHMEM_48",
        "C4D_HIGHMEM_64",
        "C4D_HIGHMEM_96",
        "C4D_HIGHMEM_192",
        "C4D_HIGHMEM_384",
        "N4_STANDARD_2",
        "N4_STANDARD_4",
        "N4_STANDARD_8",
        "N4_STANDARD_16",
        "N4_STANDARD_32",
        "N4_STANDARD_48",
        "N4_STANDARD_64",
        "N4_STANDARD_80",
        "N4_HIGHCPU_2",
        "N4_HIGHCPU_4",
        "N4_HIGHCPU_8",
        "N4_HIGHCPU_16",
        "N4_HIGHCPU_32",
        "N4_HIGHCPU_48",
        "N4_HIGHCPU_64",
        "N4_HIGHCPU_80",
        "N4_HIGHMEM_2",
        "N4_HIGHMEM_4",
        "N4_HIGHMEM_8",
        "N4_HIGHMEM_16",
        "N4_HIGHMEM_32",
        "N4_HIGHMEM_48",
        "N4_HIGHMEM_64",
        "N4_HIGHMEM_80",
        "N4A_STANDARD_2",
        "N4A_STANDARD_4",
        "N4A_STANDARD_8",
        "N4A_STANDARD_16",
        "N4A_STANDARD_32",
        "N4A_STANDARD_48",
        "N4A_STANDARD_64",
        "N4A_HIGHCPU_2",
        "N4A_HIGHCPU_4",
        "N4A_HIGHCPU_8",
        "N4A_HIGHCPU_16",
        "N4A_HIGHCPU_32",
        "N4A_HIGHCPU_48",
        "N4A_HIGHCPU_64",
        "N4A_HIGHMEM_2",
        "N4A_HIGHMEM_4",
        "N4A_HIGHMEM_8",
        "N4A_HIGHMEM_16",
        "N4A_HIGHMEM_32",
        "N4A_HIGHMEM_48",
        "N4A_HIGHMEM_64",
        "C3D_STANDARD_8",
        "C3D_STANDARD_16",
        "C3D_STANDARD_30",
        "C3D_STANDARD_60",
        "C3D_STANDARD_90",
        "C3D_STANDARD_180",
        "C3D_STANDARD_360",
        "C3D_HIGHCPU_8",
        "C3D_HIGHCPU_16",
        "C3D_HIGHCPU_30",
        "C3D_HIGHCPU_60",
        "C3D_HIGHCPU_90",
        "C3D_HIGHCPU_180",
        "C3D_HIGHCPU_360",
        "C3D_HIGHMEM_8",
        "C3D_HIGHMEM_16",
        "C3D_HIGHMEM_30",
        "C3D_HIGHMEM_60",
        "C3D_HIGHMEM_90",
        "C3D_HIGHMEM_180",
        "C3D_HIGHMEM_360",
    ]
    memories: float
    ramType: typing.Literal[
        "UNKNOWN_RAM_TYPE",
        "A2",
        "A3",
        "A4",
        "A4X",
        "C2",
        "C2D",
        "CUSTOM",
        "E2",
        "G2",
        "G4",
        "C4",
        "C4A",
        "C4D",
        "N4",
        "N4A",
        "C3D",
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
class Sentence(typing.TypedDict, total=False):
    sentiment: Sentiment
    text: TextSpan

@typing.type_check_only
class Sentiment(typing.TypedDict, total=False):
    magnitude: float
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

@typing.type_check_only
class TpuMetric(typing.TypedDict, total=False):
    tpuSec: str
    tpuType: typing.Literal[
        "UNKNOWN_TPU_TYPE",
        "TPU_V2_POD",
        "TPU_V2",
        "TPU_V3_POD",
        "TPU_V3",
        "TPU_V5_LITEPOD",
    ]

@typing.type_check_only
class XPSArrayStats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    memberStats: XPSDataStats

@typing.type_check_only
class XPSBatchPredictResponse(typing.TypedDict, total=False):
    exampleSet: XPSExampleSet

@typing.type_check_only
class XPSBoundingBoxMetricsEntry(typing.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSBoundingBoxMetricsEntryConfidenceMetricsEntry]
    iouThreshold: float
    meanAveragePrecision: float

@typing.type_check_only
class XPSBoundingBoxMetricsEntryConfidenceMetricsEntry(typing.TypedDict, total=False):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class XPSCategoryStats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    topCategoryStats: _list[XPSCategoryStatsSingleCategoryStats]

@typing.type_check_only
class XPSCategoryStatsSingleCategoryStats(typing.TypedDict, total=False):
    count: str
    value: str

@typing.type_check_only
class XPSClassificationEvaluationMetrics(typing.TypedDict, total=False):
    auPrc: float
    auRoc: float
    baseAuPrc: float
    confidenceMetricsEntries: _list[XPSConfidenceMetricsEntry]
    confusionMatrix: XPSConfusionMatrix
    evaluatedExamplesCount: int
    logLoss: float

@typing.type_check_only
class XPSColorMap(typing.TypedDict, total=False):
    annotationSpecIdToken: str
    color: Color
    displayName: str
    intColor: XPSColorMapIntColor

@typing.type_check_only
class XPSColorMapIntColor(typing.TypedDict, total=False):
    blue: int
    green: int
    red: int

@typing.type_check_only
class XPSColumnSpec(typing.TypedDict, total=False):
    columnId: int
    dataStats: XPSDataStats
    dataType: XPSDataType
    displayName: str
    forecastingMetadata: XPSColumnSpecForecastingMetadata
    topCorrelatedColumns: _list[XPSColumnSpecCorrelatedColumn]

@typing.type_check_only
class XPSColumnSpecCorrelatedColumn(typing.TypedDict, total=False):
    columnId: int
    correlationStats: XPSCorrelationStats

@typing.type_check_only
class XPSColumnSpecForecastingMetadata(typing.TypedDict, total=False):
    columnType: typing.Literal[
        "COLUMN_TYPE_UNSPECIFIED",
        "KEY",
        "KEY_METADATA",
        "TIME_SERIES_AVAILABLE_PAST_ONLY",
        "TIME_SERIES_AVAILABLE_PAST_AND_FUTURE",
    ]

@typing.type_check_only
class XPSCommonStats(typing.TypedDict, total=False):
    distinctValueCount: str
    nullValueCount: str
    validValueCount: str

@typing.type_check_only
class XPSConfidenceMetricsEntry(typing.TypedDict, total=False):
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
class XPSConfusionMatrix(typing.TypedDict, total=False):
    annotationSpecIdToken: _list[str]
    category: _list[int]
    row: _list[XPSConfusionMatrixRow]
    sentimentLabel: _list[int]

@typing.type_check_only
class XPSConfusionMatrixRow(typing.TypedDict, total=False):
    count: _list[str]
    exampleCount: _list[int]

@typing.type_check_only
class XPSCoreMlFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSCorrelationStats(typing.TypedDict, total=False):
    cramersV: float

@typing.type_check_only
class XPSDataErrors(typing.TypedDict, total=False):
    count: int
    errorType: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "UNSUPPORTED_AUDIO_FORMAT",
        "FILE_EXTENSION_MISMATCH_WITH_AUDIO_FORMAT",
        "FILE_TOO_LARGE",
        "MISSING_TRANSCRIPTION",
    ]

@typing.type_check_only
class XPSDataStats(typing.TypedDict, total=False):
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
class XPSDataType(typing.TypedDict, total=False):
    compatibleDataTypes: _list[XPSDataType]
    listElementType: XPSDataType
    nullable: bool
    structType: XPSStructType
    timeFormat: str
    typeCode: typing.Literal[
        "TYPE_CODE_UNSPECIFIED",
        "FLOAT64",
        "TIMESTAMP",
        "STRING",
        "ARRAY",
        "STRUCT",
        "CATEGORY",
    ]

@typing.type_check_only
class XPSDockerFormat(typing.TypedDict, total=False):
    cpuArchitecture: typing.Literal[
        "CPU_ARCHITECTURE_UNSPECIFIED", "CPU_ARCHITECTURE_X86_64"
    ]
    gpuArchitecture: typing.Literal[
        "GPU_ARCHITECTURE_UNSPECIFIED", "GPU_ARCHITECTURE_NVIDIA"
    ]

@typing.type_check_only
class XPSEdgeTpuTfLiteFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSEvaluationMetrics(typing.TypedDict, total=False):
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
class XPSEvaluationMetricsSet(typing.TypedDict, total=False):
    evaluationMetrics: _list[XPSEvaluationMetrics]
    fileSpec: XPSFileSpec
    numEvaluationMetrics: str

@typing.type_check_only
class XPSExampleSet(typing.TypedDict, total=False):
    fileSpec: XPSFileSpec
    fingerprint: str
    numExamples: str
    numInputSources: str

@typing.type_check_only
class XPSExportModelOutputConfig(typing.TypedDict, total=False):
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
class XPSFileSpec(typing.TypedDict, total=False):
    directoryPath: str
    fileFormat: typing.Literal[
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
class XPSFloat64Stats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    histogramBuckets: _list[XPSFloat64StatsHistogramBucket]
    mean: float
    quantiles: _list[float]
    standardDeviation: float

@typing.type_check_only
class XPSFloat64StatsHistogramBucket(typing.TypedDict, total=False):
    count: str
    max: float
    min: float

@typing.type_check_only
class XPSImageClassificationTrainResponse(typing.TypedDict, total=False):
    classCount: str
    exportModelSpec: XPSImageExportModelSpec
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostInNodeTime: str
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSImageExportModelSpec(typing.TypedDict, total=False):
    exportModelOutputConfig: _list[XPSExportModelOutputConfig]

@typing.type_check_only
class XPSImageModelArtifactSpec(typing.TypedDict, total=False):
    checkpointArtifact: XPSModelArtifactItem
    exportArtifact: _list[XPSModelArtifactItem]
    labelGcsUri: str
    servingArtifact: XPSModelArtifactItem
    tfJsBinaryGcsPrefix: str
    tfLiteMetadataGcsUri: str

@typing.type_check_only
class XPSImageModelServingSpec(typing.TypedDict, total=False):
    modelThroughputEstimation: _list[XPSImageModelServingSpecModelThroughputEstimation]
    nodeQps: float
    tfRuntimeVersion: str

@typing.type_check_only
class XPSImageModelServingSpecModelThroughputEstimation(typing.TypedDict, total=False):
    computeEngineAcceleratorType: typing.Literal[
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
        "NVIDIA_B200",
        "NVIDIA_GB200",
        "TPU_V2",
        "TPU_V3",
        "TPU_V4_POD",
        "TPU_V5_LITEPOD",
    ]
    latencyInMilliseconds: float
    nodeQps: float
    servomaticPartitionType: typing.Literal[
        "PARTITION_TYPE_UNSPECIFIED",
        "PARTITION_ZERO",
        "PARTITION_REDUCED_HOMING",
        "PARTITION_JELLYFISH",
        "PARTITION_CPU",
        "PARTITION_CUSTOM_STORAGE_CPU",
    ]

@typing.type_check_only
class XPSImageObjectDetectionEvaluationMetrics(typing.TypedDict, total=False):
    boundingBoxMeanAveragePrecision: float
    boundingBoxMetricsEntries: _list[XPSBoundingBoxMetricsEntry]
    evaluatedBoundingBoxCount: int

@typing.type_check_only
class XPSImageObjectDetectionModelSpec(typing.TypedDict, total=False):
    classCount: str
    exportModelSpec: XPSImageExportModelSpec
    maxBoundingBoxCount: str
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSImageSegmentationEvaluationMetrics(typing.TypedDict, total=False):
    confidenceMetricsEntries: _list[
        XPSImageSegmentationEvaluationMetricsConfidenceMetricsEntry
    ]

@typing.type_check_only
class XPSImageSegmentationEvaluationMetricsConfidenceMetricsEntry(
    typing.TypedDict, total=False
):
    confidenceThreshold: float
    confusionMatrix: XPSConfusionMatrix
    diceScoreCoefficient: float
    iouScore: float
    precision: float
    recall: float

@typing.type_check_only
class XPSImageSegmentationTrainResponse(typing.TypedDict, total=False):
    colorMaps: _list[XPSColorMap]
    exportModelSpec: XPSImageExportModelSpec
    modelArtifactSpec: XPSImageModelArtifactSpec
    modelServingSpec: XPSImageModelServingSpec
    stopReason: typing.Literal[
        "TRAIN_STOP_REASON_UNSPECIFIED",
        "TRAIN_STOP_REASON_BUDGET_REACHED",
        "TRAIN_STOP_REASON_MODEL_CONVERGED",
        "TRAIN_STOP_REASON_MODEL_EARLY_STOPPED",
    ]
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSIntegratedGradientsAttribution(typing.TypedDict, total=False):
    stepCount: int

@typing.type_check_only
class XPSMetricEntry(typing.TypedDict, total=False):
    argentumMetricId: str
    doubleValue: float
    int64Value: str
    metricName: str
    systemLabels: _list[XPSMetricEntryLabel]

@typing.type_check_only
class XPSMetricEntryLabel(typing.TypedDict, total=False):
    labelName: str
    labelValue: str

@typing.type_check_only
class XPSModelArtifactItem(typing.TypedDict, total=False):
    artifactFormat: typing.Literal[
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
class XPSPreprocessResponse(typing.TypedDict, total=False):
    outputExampleSet: XPSExampleSet
    speechPreprocessResp: XPSSpeechPreprocessResponse
    tablesPreprocessResponse: XPSTablesPreprocessResponse
    translationPreprocessResp: XPSTranslationPreprocessResponse

@typing.type_check_only
class XPSRegressionEvaluationMetrics(typing.TypedDict, total=False):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    regressionMetricsEntries: _list[XPSRegressionMetricsEntry]
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class XPSRegressionMetricsEntry(typing.TypedDict, total=False):
    predictedValue: float
    trueValue: float

@typing.type_check_only
class XPSReportingMetrics(typing.TypedDict, total=False):
    effectiveTrainingDuration: str
    metricEntries: _list[XPSMetricEntry]

@typing.type_check_only
class XPSResponseExplanationMetadata(typing.TypedDict, total=False):
    inputs: dict[str, typing.Any]
    outputs: dict[str, typing.Any]

@typing.type_check_only
class XPSResponseExplanationMetadataInputMetadata(typing.TypedDict, total=False):
    inputTensorName: str
    modality: typing.Literal["MODALITY_UNSPECIFIED", "NUMERIC", "IMAGE", "CATEGORICAL"]
    visualizationConfig: XPSVisualization

@typing.type_check_only
class XPSResponseExplanationMetadataOutputMetadata(typing.TypedDict, total=False):
    outputTensorName: str

@typing.type_check_only
class XPSResponseExplanationParameters(typing.TypedDict, total=False):
    integratedGradientsAttribution: XPSIntegratedGradientsAttribution
    xraiAttribution: XPSXraiAttribution

@typing.type_check_only
class XPSResponseExplanationSpec(typing.TypedDict, total=False):
    explanationType: str
    metadata: XPSResponseExplanationMetadata
    parameters: XPSResponseExplanationParameters

@typing.type_check_only
class XPSRow(typing.TypedDict, total=False):
    columnIds: _list[int]
    values: _list[typing.Any]

@typing.type_check_only
class XPSSpeechEvaluationMetrics(typing.TypedDict, total=False):
    subModelEvaluationMetrics: _list[XPSSpeechEvaluationMetricsSubModelEvaluationMetric]

@typing.type_check_only
class XPSSpeechEvaluationMetricsSubModelEvaluationMetric(typing.TypedDict, total=False):
    biasingModelType: typing.Literal[
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
class XPSSpeechModelSpec(typing.TypedDict, total=False):
    datasetId: str
    language: str
    subModelSpecs: _list[XPSSpeechModelSpecSubModelSpec]

@typing.type_check_only
class XPSSpeechModelSpecSubModelSpec(typing.TypedDict, total=False):
    biasingModelType: typing.Literal[
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
class XPSSpeechPreprocessResponse(typing.TypedDict, total=False):
    cnsTestDataPath: str
    cnsTrainDataPath: str
    prebuiltModelEvaluationMetrics: XPSSpeechEvaluationMetrics
    speechPreprocessStats: XPSSpeechPreprocessStats

@typing.type_check_only
class XPSSpeechPreprocessStats(typing.TypedDict, total=False):
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
class XPSStringStats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    topUnigramStats: _list[XPSStringStatsUnigramStats]

@typing.type_check_only
class XPSStringStatsUnigramStats(typing.TypedDict, total=False):
    count: str
    value: str

@typing.type_check_only
class XPSStructStats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    fieldStats: dict[str, typing.Any]

@typing.type_check_only
class XPSStructType(typing.TypedDict, total=False):
    fields: dict[str, typing.Any]

@typing.type_check_only
class XPSTableSpec(typing.TypedDict, total=False):
    columnSpecs: dict[str, typing.Any]
    importedDataSizeInBytes: str
    rowCount: str
    timeColumnId: int
    validRowCount: str

@typing.type_check_only
class XPSTablesClassificationMetrics(typing.TypedDict, total=False):
    curveMetrics: _list[XPSTablesClassificationMetricsCurveMetrics]

@typing.type_check_only
class XPSTablesClassificationMetricsCurveMetrics(typing.TypedDict, total=False):
    aucPr: float
    aucRoc: float
    confidenceMetricsEntries: _list[XPSTablesConfidenceMetricsEntry]
    logLoss: float
    positionThreshold: int
    value: str

@typing.type_check_only
class XPSTablesConfidenceMetricsEntry(typing.TypedDict, total=False):
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
class XPSTablesDatasetMetadata(typing.TypedDict, total=False):
    mlUseColumnId: int
    primaryTableSpec: XPSTableSpec
    targetColumnCorrelations: dict[str, typing.Any]
    targetColumnId: int
    weightColumnId: int

@typing.type_check_only
class XPSTablesEvaluationMetrics(typing.TypedDict, total=False):
    classificationMetrics: XPSTablesClassificationMetrics
    regressionMetrics: XPSTablesRegressionMetrics

@typing.type_check_only
class XPSTablesModelColumnInfo(typing.TypedDict, total=False):
    columnId: int
    featureImportance: float

@typing.type_check_only
class XPSTablesModelStructure(typing.TypedDict, total=False):
    modelParameters: _list[XPSTablesModelStructureModelParameters]

@typing.type_check_only
class XPSTablesModelStructureModelParameters(typing.TypedDict, total=False):
    hyperparameters: _list[XPSTablesModelStructureModelParametersParameter]

@typing.type_check_only
class XPSTablesModelStructureModelParametersParameter(typing.TypedDict, total=False):
    floatValue: float
    intValue: str
    name: str
    stringValue: str

@typing.type_check_only
class XPSTablesPreprocessResponse(typing.TypedDict, total=False):
    tablesDatasetMetadata: XPSTablesDatasetMetadata

@typing.type_check_only
class XPSTablesRegressionMetrics(typing.TypedDict, total=False):
    meanAbsoluteError: float
    meanAbsolutePercentageError: float
    rSquared: float
    regressionMetricsEntries: _list[XPSRegressionMetricsEntry]
    rootMeanSquaredError: float
    rootMeanSquaredLogError: float

@typing.type_check_only
class XPSTablesTrainResponse(typing.TypedDict, total=False):
    modelStructure: XPSTablesModelStructure
    predictionSampleRows: _list[XPSRow]
    tablesModelColumnInfo: _list[XPSTablesModelColumnInfo]
    trainCostMilliNodeHours: str

@typing.type_check_only
class XPSTablesTrainingOperationMetadata(typing.TypedDict, total=False):
    createModelStage: typing.Literal[
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
class XPSTextComponentModel(typing.TypedDict, total=False):
    batchPredictionModelGcsUri: str
    onlinePredictionModelGcsUri: str
    partition: typing.Literal[
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
    submodelType: typing.Literal[
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
class XPSTextExtractionEvaluationMetrics(typing.TypedDict, total=False):
    bestF1ConfidenceMetrics: XPSConfidenceMetricsEntry
    confidenceMetricsEntries: _list[XPSConfidenceMetricsEntry]
    confusionMatrix: XPSConfusionMatrix
    perLabelConfidenceMetrics: dict[str, typing.Any]

@typing.type_check_only
class XPSTextSentimentEvaluationMetrics(typing.TypedDict, total=False):
    confusionMatrix: XPSConfusionMatrix
    f1Score: float
    linearKappa: float
    meanAbsoluteError: float
    meanSquaredError: float
    precision: float
    quadraticKappa: float
    recall: float

@typing.type_check_only
class XPSTextToSpeechTrainResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSTextTrainResponse(typing.TypedDict, total=False):
    componentModel: _list[XPSTextComponentModel]

@typing.type_check_only
class XPSTfJsFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSTfLiteFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSTfSavedModelFormat(typing.TypedDict, total=False): ...

@typing.type_check_only
class XPSTimestampStats(typing.TypedDict, total=False):
    commonStats: XPSCommonStats
    granularStats: dict[str, typing.Any]
    medianTimestampNanos: str

@typing.type_check_only
class XPSTimestampStatsGranularStats(typing.TypedDict, total=False):
    buckets: dict[str, typing.Any]

@typing.type_check_only
class XPSTrackMetricsEntry(typing.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSTrackMetricsEntryConfidenceMetricsEntry]
    iouThreshold: float
    meanBoundingBoxIou: float
    meanMismatchRate: float
    meanTrackingAveragePrecision: float

@typing.type_check_only
class XPSTrackMetricsEntryConfidenceMetricsEntry(typing.TypedDict, total=False):
    boundingBoxIou: float
    confidenceThreshold: float
    mismatchRate: float
    trackingPrecision: float
    trackingRecall: float

@typing.type_check_only
class XPSTrainResponse(typing.TypedDict, total=False):
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
class XPSTrainingObjectivePoint(typing.TypedDict, total=False):
    createTime: str
    value: float

@typing.type_check_only
class XPSTranslationEvaluationMetrics(typing.TypedDict, total=False):
    baseBleuScore: float
    bleuScore: float

@typing.type_check_only
class XPSTranslationPreprocessResponse(typing.TypedDict, total=False):
    parsedExampleCount: str
    validExampleCount: str

@typing.type_check_only
class XPSTranslationTrainResponse(typing.TypedDict, total=False):
    modelType: typing.Literal["MODEL_TYPE_UNSPECIFIED", "LEGACY", "CURRENT"]

@typing.type_check_only
class XPSTuningTrial(typing.TypedDict, total=False):
    modelStructure: XPSTablesModelStructure
    trainingObjectivePoint: XPSTrainingObjectivePoint

@typing.type_check_only
class XPSVideoActionMetricsEntry(typing.TypedDict, total=False):
    confidenceMetricsEntries: _list[XPSVideoActionMetricsEntryConfidenceMetricsEntry]
    meanAveragePrecision: float
    precisionWindowLength: str

@typing.type_check_only
class XPSVideoActionMetricsEntryConfidenceMetricsEntry(typing.TypedDict, total=False):
    confidenceThreshold: float
    f1Score: float
    precision: float
    recall: float

@typing.type_check_only
class XPSVideoActionRecognitionEvaluationMetrics(typing.TypedDict, total=False):
    evaluatedActionCount: int
    videoActionMetricsEntries: _list[XPSVideoActionMetricsEntry]

@typing.type_check_only
class XPSVideoActionRecognitionTrainResponse(typing.TypedDict, total=False):
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoBatchPredictOperationMetadata(typing.TypedDict, total=False):
    outputExamples: _list[str]

@typing.type_check_only
class XPSVideoClassificationTrainResponse(typing.TypedDict, total=False):
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoExportModelSpec(typing.TypedDict, total=False):
    exportModelOutputConfig: _list[XPSExportModelOutputConfig]

@typing.type_check_only
class XPSVideoModelArtifactSpec(typing.TypedDict, total=False):
    exportArtifact: _list[XPSModelArtifactItem]
    servingArtifact: XPSModelArtifactItem

@typing.type_check_only
class XPSVideoObjectTrackingEvaluationMetrics(typing.TypedDict, total=False):
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
class XPSVideoObjectTrackingTrainResponse(typing.TypedDict, total=False):
    exportModelSpec: XPSVideoExportModelSpec
    modelArtifactSpec: XPSVideoModelArtifactSpec
    trainCostNodeSeconds: str

@typing.type_check_only
class XPSVideoTrainingOperationMetadata(typing.TypedDict, total=False):
    trainCostMilliNodeHour: str

@typing.type_check_only
class XPSVisionErrorAnalysisConfig(typing.TypedDict, total=False):
    exampleCount: int
    queryType: typing.Literal[
        "QUERY_TYPE_UNSPECIFIED",
        "QUERY_TYPE_ALL_SIMILAR",
        "QUERY_TYPE_SAME_CLASS_SIMILAR",
        "QUERY_TYPE_SAME_CLASS_DISSIMILAR",
    ]

@typing.type_check_only
class XPSVisionTrainingOperationMetadata(typing.TypedDict, total=False):
    explanationUsage: InfraUsage

@typing.type_check_only
class XPSVisualization(typing.TypedDict, total=False):
    clipPercentLowerbound: float
    clipPercentUpperbound: float
    colorMap: typing.Literal[
        "COLOR_MAP_UNSPECIFIED",
        "PINK_GREEN",
        "VIRIDIS",
        "RED",
        "GREEN",
        "RED_GREEN",
        "PINK_WHITE_GREEN",
    ]
    overlayType: typing.Literal[
        "OVERLAY_TYPE_UNSPECIFIED", "NONE", "ORIGINAL", "GRAYSCALE", "MASK_BLACK"
    ]
    polarity: typing.Literal["POLARITY_UNSPECIFIED", "POSITIVE", "NEGATIVE", "BOTH"]
    type: typing.Literal["TYPE_UNSPECIFIED", "PIXELS", "OUTLINES"]

@typing.type_check_only
class XPSXpsOperationMetadata(typing.TypedDict, total=False):
    exampleCount: str
    reportingMetrics: XPSReportingMetrics
    tablesTrainingOperationMetadata: XPSTablesTrainingOperationMetadata
    videoBatchPredictOperationMetadata: XPSVideoBatchPredictOperationMetadata
    videoTrainingOperationMetadata: XPSVideoTrainingOperationMetadata
    visionTrainingOperationMetadata: XPSVisionTrainingOperationMetadata

@typing.type_check_only
class XPSXraiAttribution(typing.TypedDict, total=False):
    stepCount: int
