import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdaptiveMtDataset(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    exampleCount: int
    name: str
    sourceLanguageCode: str
    targetLanguageCode: str
    updateTime: str

@typing.type_check_only
class AdaptiveMtFile(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    entryCount: int
    name: str
    updateTime: str

@typing.type_check_only
class AdaptiveMtSentence(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    sourceSentence: str
    targetSentence: str
    updateTime: str

@typing.type_check_only
class AdaptiveMtTranslateRequest(typing_extensions.TypedDict, total=False):
    content: _list[str]
    dataset: str
    glossaryConfig: GlossaryConfig
    referenceSentenceConfig: ReferenceSentenceConfig

@typing.type_check_only
class AdaptiveMtTranslateResponse(typing_extensions.TypedDict, total=False):
    glossaryTranslations: _list[AdaptiveMtTranslation]
    languageCode: str
    translations: _list[AdaptiveMtTranslation]

@typing.type_check_only
class AdaptiveMtTranslation(typing_extensions.TypedDict, total=False):
    translatedText: str

@typing.type_check_only
class BatchDocumentInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class BatchDocumentOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class BatchTranslateDocumentRequest(typing_extensions.TypedDict, total=False):
    customizedAttribution: str
    enableRotationCorrection: bool
    enableShadowRemovalNativePdf: bool
    formatConversions: dict[str, typing.Any]
    glossaries: dict[str, typing.Any]
    inputConfigs: _list[BatchDocumentInputConfig]
    models: dict[str, typing.Any]
    outputConfig: BatchDocumentOutputConfig
    sourceLanguageCode: str
    targetLanguageCodes: _list[str]

@typing.type_check_only
class BatchTranslateTextRequest(typing_extensions.TypedDict, total=False):
    glossaries: dict[str, typing.Any]
    inputConfigs: _list[InputConfig]
    labels: dict[str, typing.Any]
    models: dict[str, typing.Any]
    outputConfig: OutputConfig
    sourceLanguageCode: str
    targetLanguageCodes: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    exampleCount: int
    name: str
    sourceLanguageCode: str
    targetLanguageCode: str
    testExampleCount: int
    trainExampleCount: int
    updateTime: str
    validateExampleCount: int

@typing.type_check_only
class DatasetInputConfig(typing_extensions.TypedDict, total=False):
    inputFiles: _list[InputFile]

@typing.type_check_only
class DatasetOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsOutputDestination

@typing.type_check_only
class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    content: str
    labels: dict[str, typing.Any]
    mimeType: str
    model: str

@typing.type_check_only
class DetectLanguageResponse(typing_extensions.TypedDict, total=False):
    languages: _list[DetectedLanguage]

@typing.type_check_only
class DetectedLanguage(typing_extensions.TypedDict, total=False):
    confidence: float
    languageCode: str

@typing.type_check_only
class DocumentInputConfig(typing_extensions.TypedDict, total=False):
    content: str
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class DocumentOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination
    mimeType: str

@typing.type_check_only
class DocumentTranslation(typing_extensions.TypedDict, total=False):
    byteStreamOutputs: _list[str]
    detectedLanguageCode: str
    mimeType: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Example(typing_extensions.TypedDict, total=False):
    name: str
    sourceText: str
    targetText: str
    usage: str

@typing.type_check_only
class ExportDataRequest(typing_extensions.TypedDict, total=False):
    outputConfig: DatasetOutputConfig

@typing.type_check_only
class FileInputSource(typing_extensions.TypedDict, total=False):
    content: str
    displayName: str
    mimeType: str

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GcsInputSource(typing_extensions.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class GcsOutputDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class Glossary(typing_extensions.TypedDict, total=False):
    displayName: str
    endTime: str
    entryCount: int
    inputConfig: GlossaryInputConfig
    languageCodesSet: LanguageCodesSet
    languagePair: LanguageCodePair
    name: str
    submitTime: str

@typing.type_check_only
class GlossaryConfig(typing_extensions.TypedDict, total=False):
    contextualTranslationEnabled: bool
    glossary: str
    ignoreCase: bool

@typing.type_check_only
class GlossaryEntry(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    termsPair: GlossaryTermsPair
    termsSet: GlossaryTermsSet

@typing.type_check_only
class GlossaryInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class GlossaryTerm(typing_extensions.TypedDict, total=False):
    languageCode: str
    text: str

@typing.type_check_only
class GlossaryTermsPair(typing_extensions.TypedDict, total=False):
    sourceTerm: GlossaryTerm
    targetTerm: GlossaryTerm

@typing.type_check_only
class GlossaryTermsSet(typing_extensions.TypedDict, total=False):
    terms: _list[GlossaryTerm]

@typing.type_check_only
class ImportAdaptiveMtFileRequest(typing_extensions.TypedDict, total=False):
    fileInputSource: FileInputSource
    gcsInputSource: GcsInputSource

@typing.type_check_only
class ImportAdaptiveMtFileResponse(typing_extensions.TypedDict, total=False):
    adaptiveMtFile: AdaptiveMtFile

@typing.type_check_only
class ImportDataRequest(typing_extensions.TypedDict, total=False):
    inputConfig: DatasetInputConfig

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class InputFile(typing_extensions.TypedDict, total=False):
    gcsSource: GcsInputSource
    usage: str

@typing.type_check_only
class LanguageCodePair(typing_extensions.TypedDict, total=False):
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class LanguageCodesSet(typing_extensions.TypedDict, total=False):
    languageCodes: _list[str]

@typing.type_check_only
class ListAdaptiveMtDatasetsResponse(typing_extensions.TypedDict, total=False):
    adaptiveMtDatasets: _list[AdaptiveMtDataset]
    nextPageToken: str

@typing.type_check_only
class ListAdaptiveMtFilesResponse(typing_extensions.TypedDict, total=False):
    adaptiveMtFiles: _list[AdaptiveMtFile]
    nextPageToken: str

@typing.type_check_only
class ListAdaptiveMtSentencesResponse(typing_extensions.TypedDict, total=False):
    adaptiveMtSentences: _list[AdaptiveMtSentence]
    nextPageToken: str

@typing.type_check_only
class ListDatasetsResponse(typing_extensions.TypedDict, total=False):
    datasets: _list[Dataset]
    nextPageToken: str

@typing.type_check_only
class ListExamplesResponse(typing_extensions.TypedDict, total=False):
    examples: _list[Example]
    nextPageToken: str

@typing.type_check_only
class ListGlossariesResponse(typing_extensions.TypedDict, total=False):
    glossaries: _list[Glossary]
    nextPageToken: str

@typing.type_check_only
class ListGlossaryEntriesResponse(typing_extensions.TypedDict, total=False):
    glossaryEntries: _list[GlossaryEntry]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListModelsResponse(typing_extensions.TypedDict, total=False):
    models: _list[Model]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Model(typing_extensions.TypedDict, total=False):
    createTime: str
    dataset: str
    displayName: str
    name: str
    sourceLanguageCode: str
    targetLanguageCode: str
    testExampleCount: int
    trainExampleCount: int
    updateTime: str
    validateExampleCount: int

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class ReferenceSentenceConfig(typing_extensions.TypedDict, total=False):
    referenceSentencePairLists: _list[ReferenceSentencePairList]
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class ReferenceSentencePair(typing_extensions.TypedDict, total=False):
    sourceSentence: str
    targetSentence: str

@typing.type_check_only
class ReferenceSentencePairList(typing_extensions.TypedDict, total=False):
    referenceSentencePairs: _list[ReferenceSentencePair]

@typing.type_check_only
class Romanization(typing_extensions.TypedDict, total=False):
    detectedLanguageCode: str
    romanizedText: str

@typing.type_check_only
class RomanizeTextRequest(typing_extensions.TypedDict, total=False):
    contents: _list[str]
    sourceLanguageCode: str

@typing.type_check_only
class RomanizeTextResponse(typing_extensions.TypedDict, total=False):
    romanizations: _list[Romanization]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedLanguage(typing_extensions.TypedDict, total=False):
    displayName: str
    languageCode: str
    supportSource: bool
    supportTarget: bool

@typing.type_check_only
class SupportedLanguages(typing_extensions.TypedDict, total=False):
    languages: _list[SupportedLanguage]

@typing.type_check_only
class TranslateDocumentRequest(typing_extensions.TypedDict, total=False):
    customizedAttribution: str
    documentInputConfig: DocumentInputConfig
    documentOutputConfig: DocumentOutputConfig
    enableRotationCorrection: bool
    enableShadowRemovalNativePdf: bool
    glossaryConfig: TranslateTextGlossaryConfig
    isTranslateNativePdfOnly: bool
    labels: dict[str, typing.Any]
    model: str
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class TranslateDocumentResponse(typing_extensions.TypedDict, total=False):
    documentTranslation: DocumentTranslation
    glossaryConfig: TranslateTextGlossaryConfig
    glossaryDocumentTranslation: DocumentTranslation
    model: str

@typing.type_check_only
class TranslateTextGlossaryConfig(typing_extensions.TypedDict, total=False):
    contextualTranslationEnabled: bool
    glossary: str
    ignoreCase: bool

@typing.type_check_only
class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    contents: _list[str]
    glossaryConfig: TranslateTextGlossaryConfig
    labels: dict[str, typing.Any]
    mimeType: str
    model: str
    sourceLanguageCode: str
    targetLanguageCode: str
    transliterationConfig: TransliterationConfig

@typing.type_check_only
class TranslateTextResponse(typing_extensions.TypedDict, total=False):
    glossaryTranslations: _list[Translation]
    translations: _list[Translation]

@typing.type_check_only
class Translation(typing_extensions.TypedDict, total=False):
    detectedLanguageCode: str
    glossaryConfig: TranslateTextGlossaryConfig
    model: str
    translatedText: str

@typing.type_check_only
class TransliterationConfig(typing_extensions.TypedDict, total=False):
    enableTransliteration: bool

@typing.type_check_only
class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str
