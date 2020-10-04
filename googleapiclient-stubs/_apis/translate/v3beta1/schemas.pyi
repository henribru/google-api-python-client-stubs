import typing

import typing_extensions
@typing.type_check_only
class BatchTranslateTextRequest(typing_extensions.TypedDict, total=False):
    glossaries: typing.Dict[str, typing.Any]
    inputConfigs: typing.List[InputConfig]
    labels: typing.Dict[str, typing.Any]
    models: typing.Dict[str, typing.Any]
    outputConfig: OutputConfig
    sourceLanguageCode: str
    targetLanguageCodes: typing.List[str]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    content: str
    labels: typing.Dict[str, typing.Any]
    mimeType: str
    model: str

@typing.type_check_only
class DetectLanguageResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[DetectedLanguage]

@typing.type_check_only
class DetectedLanguage(typing_extensions.TypedDict, total=False):
    confidence: float
    languageCode: str

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
    languageCodes: typing.List[str]

@typing.type_check_only
class ListGlossariesResponse(typing_extensions.TypedDict, total=False):
    glossaries: typing.List[Glossary]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SupportedLanguage(typing_extensions.TypedDict, total=False):
    displayName: str
    languageCode: str
    supportSource: bool
    supportTarget: bool

@typing.type_check_only
class SupportedLanguages(typing_extensions.TypedDict, total=False):
    languages: typing.List[SupportedLanguage]

@typing.type_check_only
class TranslateTextGlossaryConfig(typing_extensions.TypedDict, total=False):
    glossary: str
    ignoreCase: bool

@typing.type_check_only
class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    contents: typing.List[str]
    glossaryConfig: TranslateTextGlossaryConfig
    labels: typing.Dict[str, typing.Any]
    mimeType: str
    model: str
    sourceLanguageCode: str
    targetLanguageCode: str

@typing.type_check_only
class TranslateTextResponse(typing_extensions.TypedDict, total=False):
    glossaryTranslations: typing.List[Translation]
    translations: typing.List[Translation]

@typing.type_check_only
class Translation(typing_extensions.TypedDict, total=False):
    detectedLanguageCode: str
    glossaryConfig: TranslateTextGlossaryConfig
    model: str
    translatedText: str

@typing.type_check_only
class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str
