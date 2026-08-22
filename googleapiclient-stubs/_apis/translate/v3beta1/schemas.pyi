import typing

_list = list

@typing.type_check_only
class BatchDocumentInputConfig(typing.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class BatchDocumentOutputConfig(typing.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class BatchTranslateDocumentRequest(typing.TypedDict, total=False):
    customizedAttribution: str
    enableRotationCorrection: bool
    enableShadowRemovalNativePdf: bool
    formatConversions: dict[str, typing.Any]
    glossaries: dict[str, typing.Any]
    inputConfigs: _list[BatchDocumentInputConfig]
    models: dict[str, typing.Any]
    outputConfig: BatchDocumentOutputConfig
    pdfNativeOnly: bool
    sourceLanguageCode: str
    targetLanguageCodes: _list[str]

@typing.type_check_only
class BatchTranslateTextRequest(typing.TypedDict, total=False):
    glossaries: dict[str, typing.Any]
    inputConfigs: _list[InputConfig]
    labels: dict[str, typing.Any]
    models: dict[str, typing.Any]
    outputConfig: OutputConfig
    sourceLanguageCode: str
    targetLanguageCodes: _list[str]

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class DetectLanguageRequest(typing.TypedDict, total=False):
    content: str
    labels: dict[str, typing.Any]
    mimeType: str
    model: str

@typing.type_check_only
class DetectLanguageResponse(typing.TypedDict, total=False):
    languages: _list[DetectedLanguage]

@typing.type_check_only
class DetectedLanguage(typing.TypedDict, total=False):
    confidence: float
    languageCode: str

@typing.type_check_only
class DocumentInputConfig(typing.TypedDict, total=False):
    content: str
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class DocumentOutputConfig(typing.TypedDict, total=False):
    gcsDestination: GcsDestination
    mimeType: str

@typing.type_check_only
class DocumentTranslation(typing.TypedDict, total=False):
    byteStreamOutputs: _list[str]
    detectedLanguageCode: str
    mimeType: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GcsDestination(typing.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GcsSource(typing.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class Glossary(typing.TypedDict, total=False):
    endTime: str
    entryCount: int
    inputConfig: GlossaryInputConfig
    languageCodesSet: LanguageCodesSet
    languagePair: LanguageCodePair
    name: str
    submitTime: str

@typing.type_check_only
class GlossaryInputConfig(typing.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class InputConfig(typing.TypedDict, total=False):
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class LanguageCodePair(typing.TypedDict, total=False):
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class LanguageCodesSet(typing.TypedDict, total=False):
    languageCodes: _list[str]

@typing.type_check_only
class ListGlossariesResponse(typing.TypedDict, total=False):
    glossaries: _list[Glossary]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class RefineTextRequest(typing.TypedDict, total=False):
    refinementEntries: _list[RefinementEntry]
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class RefineTextResponse(typing.TypedDict, total=False):
    refinedTranslations: _list[str]

@typing.type_check_only
class RefinementEntry(typing.TypedDict, total=False):
    originalTranslation: str
    sourceText: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedLanguage(typing.TypedDict, total=False):
    displayName: str
    languageCode: str
    supportSource: bool
    supportTarget: bool

@typing.type_check_only
class SupportedLanguages(typing.TypedDict, total=False):
    languages: _list[SupportedLanguage]

@typing.type_check_only
class TranslateDocumentRequest(typing.TypedDict, total=False):
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
class TranslateDocumentResponse(typing.TypedDict, total=False):
    documentTranslation: DocumentTranslation
    glossaryConfig: TranslateTextGlossaryConfig
    glossaryDocumentTranslation: DocumentTranslation
    model: str

@typing.type_check_only
class TranslateTextGlossaryConfig(typing.TypedDict, total=False):
    contextualTranslationEnabled: bool
    glossary: str
    ignoreCase: bool

@typing.type_check_only
class TranslateTextRequest(typing.TypedDict, total=False):
    contents: _list[str]
    glossaryConfig: TranslateTextGlossaryConfig
    labels: dict[str, typing.Any]
    mimeType: str
    model: str
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class TranslateTextResponse(typing.TypedDict, total=False):
    glossaryTranslations: _list[Translation]
    translations: _list[Translation]

@typing.type_check_only
class Translation(typing.TypedDict, total=False):
    detectedLanguageCode: str
    glossaryConfig: TranslateTextGlossaryConfig
    model: str
    translatedText: str

@typing.type_check_only
class WaitOperationRequest(typing.TypedDict, total=False):
    timeout: str
