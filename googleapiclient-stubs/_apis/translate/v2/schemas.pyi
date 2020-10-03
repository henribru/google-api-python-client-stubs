import typing

import typing_extensions

class LanguagesResource(typing_extensions.TypedDict, total=False):
    language: str
    name: str

class DetectionsListResponse(typing_extensions.TypedDict, total=False):
    detections: typing.List[DetectionsResource]

class DetectionsResource(typing.Dict[str, typing.Any]): ...

class TranslationsResource(typing_extensions.TypedDict, total=False):
    translatedText: str
    model: str
    detectedSourceLanguage: str

class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[LanguagesResource]

class GetSupportedLanguagesRequest(typing_extensions.TypedDict, total=False):
    target: str

class TranslationsListResponse(typing_extensions.TypedDict, total=False):
    translations: typing.List[TranslationsResource]

class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    q: typing.List[str]

class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    q: typing.List[str]
    source: str
    model: str
    target: str
    format: str
