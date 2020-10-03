import typing

import typing_extensions

class SupportedLanguage(typing_extensions.TypedDict, total=False):
    languageCode: str
    displayName: str
    supportTarget: bool
    supportSource: bool

class Glossary(typing_extensions.TypedDict, total=False):
    submitTime: str
    languageCodesSet: LanguageCodesSet
    name: str
    inputConfig: GlossaryInputConfig
    languagePair: LanguageCodePair
    endTime: str
    entryCount: int

class SupportedLanguages(typing_extensions.TypedDict, total=False):
    languages: typing.List[SupportedLanguage]

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class DetectLanguageResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[DetectedLanguage]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    mimeType: str
    sourceLanguageCode: str
    model: str
    contents: typing.List[str]
    glossaryConfig: TranslateTextGlossaryConfig
    targetLanguageCode: str
    labels: typing.Dict[str, typing.Any]

class DetectedLanguage(typing_extensions.TypedDict, total=False):
    confidence: float
    languageCode: str

class Location(typing_extensions.TypedDict, total=False):
    name: str
    locationId: str
    displayName: str
    labels: typing.Dict[str, typing.Any]
    metadata: typing.Dict[str, typing.Any]

class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str

class LanguageCodesSet(typing_extensions.TypedDict, total=False):
    languageCodes: typing.List[str]

class TranslateTextResponse(typing_extensions.TypedDict, total=False):
    translations: typing.List[Translation]
    glossaryTranslations: typing.List[Translation]

class GcsSource(typing_extensions.TypedDict, total=False):
    inputUri: str

class BatchTranslateTextRequest(typing_extensions.TypedDict, total=False):
    inputConfigs: typing.List[InputConfig]
    sourceLanguageCode: str
    outputConfig: OutputConfig
    models: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    targetLanguageCodes: typing.List[str]
    glossaries: typing.Dict[str, typing.Any]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class TranslateTextGlossaryConfig(typing_extensions.TypedDict, total=False):
    glossary: str
    ignoreCase: bool

class InputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource
    mimeType: str

class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    mimeType: str
    model: str
    content: str

class LanguageCodePair(typing_extensions.TypedDict, total=False):
    sourceLanguageCode: str
    targetLanguageCode: str

class ListGlossariesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    glossaries: typing.List[Glossary]

class Empty(typing_extensions.TypedDict, total=False): ...

class Translation(typing_extensions.TypedDict, total=False):
    model: str
    glossaryConfig: TranslateTextGlossaryConfig
    translatedText: str
    detectedLanguageCode: str

class GcsDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    metadata: typing.Dict[str, typing.Any]
    error: Status
    name: str
    response: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class GlossaryInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource
