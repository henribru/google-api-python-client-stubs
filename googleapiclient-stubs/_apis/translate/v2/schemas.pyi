import typing

import typing_extensions
@typing.type_check_only
class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    q: typing.List[str]

@typing.type_check_only
class DetectionsListResponse(typing_extensions.TypedDict, total=False):
    detections: typing.List[DetectionsResource]

@typing.type_check_only
class DetectionsResource(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class GetSupportedLanguagesRequest(typing_extensions.TypedDict, total=False):
    target: str

@typing.type_check_only
class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    languages: typing.List[LanguagesResource]

@typing.type_check_only
class LanguagesResource(typing_extensions.TypedDict, total=False):
    language: str
    name: str

@typing.type_check_only
class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    format: str
    model: str
    q: typing.List[str]
    source: str
    target: str

@typing.type_check_only
class TranslationsListResponse(typing_extensions.TypedDict, total=False):
    translations: typing.List[TranslationsResource]

@typing.type_check_only
class TranslationsResource(typing_extensions.TypedDict, total=False):
    detectedSourceLanguage: str
    model: str
    translatedText: str
