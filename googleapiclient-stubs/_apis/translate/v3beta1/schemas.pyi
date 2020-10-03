import typing

import typing_extensions

class LanguageCodePair(typing_extensions.TypedDict, total=False):
    sourceLanguageCode: str
    targetLanguageCode: str

class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    targetLanguageCode: str
    mimeType: str
    model: str
    contents: typing.List[str]
    glossaryConfig: TranslateTextGlossaryConfig
    labels: typing.Dict[str, typing.Any]
    sourceLanguageCode: str

class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    model: str
    mimeType: str
    content: str

class BatchTranslateTextRequest(typing_extensions.TypedDict, total=False):
    models: typing.Dict[str, typing.Any]
    outputConfig: OutputConfig
    sourceLanguageCode: str
    labels: typing.Dict[str, typing.Any]
    glossaries: typing.Dict[str, typing.Any]
    targetLanguageCodes: typing.List[str]
    inputConfigs: typing.List[InputConfig]

class GcsSource(typing_extensions.TypedDict, total=False):
    inputUri: str

class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str

class SupportedLanguage(typing_extensions.TypedDict, total=False):
    supportSource: bool
    supportTarget: bool
    displayName: str
    languageCode: str

class Translation(typing_extensions.TypedDict, total=False):
    model: str
    glossaryConfig: TranslateTextGlossaryConfig
    detectedLanguageCode: str
    translatedText: str

class InputConfig(typing_extensions.TypedDict, total=False):
    mimeType: str
    gcsSource: GcsSource

class SupportedLanguages(typing_extensions.TypedDict, total=False):
    languages: typing.List[SupportedLanguage]

class LanguageCodesSet(typing_extensions.TypedDict, total=False):
    languageCodes: typing.List[str]

class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    response: typing.Dict[str, typing.Any]
    name: str

class GlossaryInputConfig(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

class TranslateTextGlossaryConfig(typing_extensions.TypedDict, total=False):
    ignoreCase: bool
    glossary: str

class DetectLanguageResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[DetectedLanguage]

class OutputConfig(typing_extensions.TypedDict, total=False):
    gcsDestination: GcsDestination

class GcsDestination(typing_extensions.TypedDict, total=False):
    outputUriPrefix: str

class TranslateTextResponse(typing_extensions.TypedDict, total=False):
    glossaryTranslations: typing.List[Translation]
    translations: typing.List[Translation]

class Status(typing_extensions.TypedDict, total=False):
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]
    code: int

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class DetectedLanguage(typing_extensions.TypedDict, total=False):
    languageCode: str
    confidence: float

class Empty(typing_extensions.TypedDict, total=False): ...
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class Glossary(typing_extensions.TypedDict, total=False):
    languageCodesSet: LanguageCodesSet
    endTime: str
    submitTime: str
    languagePair: LanguageCodePair
    inputConfig: GlossaryInputConfig
    entryCount: int
    name: str

class Location(typing_extensions.TypedDict, total=False):
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]
    name: str
    displayName: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class ListGlossariesResponse(typing_extensions.TypedDict, total=False):
    glossaries: typing.List[Glossary]
    nextPageToken: str
