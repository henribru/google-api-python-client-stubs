import typing

import typing_extensions

_list = list

@typing.type_check_only
class BatchDocumentInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class BatchDocumentOutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class BatchTranslateDocumentRequest(typing_extensions.TypedDict, total=False):
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
class GcsDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    inputUri: str

@typing.type_check_only
class Glossary(typing_extensions.TypedDict, total=False):
    endTime: str
    entryCount: int
    inputConfig: GlossaryInputConfig
    languageCodesSet: LanguageCodesSet
    languagePair: LanguageCodePair
    name: str
    submitTime: str

@typing.type_check_only
class GlossaryInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource
    mimeType: str

@typing.type_check_only
class LanguageCodePair(typing_extensions.TypedDict, total=False):
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class LanguageCodesSet(typing_extensions.TypedDict, total=False):
    languageCodes: _list[str]

@typing.type_check_only
class ListGlossariesResponse(typing_extensions.TypedDict, total=False):
    glossaries: _list[Glossary]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
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
    glossaryConfig: TranslateTextGlossaryConfig
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
class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str
