import typing

import typing_extensions

_list = list

@typing.type_check_only
class DetectLanguageRequest(typing_extensions.TypedDict, total=False):
    q: _list[str]

@typing.type_check_only
class DetectionsListResponse(typing_extensions.TypedDict, total=False):
    detections: _list[DetectionsResource]

@typing.type_check_only
class DetectionsResource(dict[str, typing.Any]): ...

@typing.type_check_only
class GetSupportedLanguagesRequest(typing_extensions.TypedDict, total=False):
    target: str

@typing.type_check_only
class LanguagesListResponse(typing_extensions.TypedDict, total=False):
    languages: _list[LanguagesResource]

@typing.type_check_only
class LanguagesResource(typing_extensions.TypedDict, total=False):
    language: str
    name: str

@typing.type_check_only
class TranslateTextRequest(typing_extensions.TypedDict, total=False):
    format: str
    model: str
    q: _list[str]
    source: str
    target: str

@typing.type_check_only
class TranslationsListResponse(typing_extensions.TypedDict, total=False):
    translations: _list[TranslationsResource]

@typing.type_check_only
class TranslationsResource(typing_extensions.TypedDict, total=False):
    detectedSourceLanguage: str
    model: str
    translatedText: str
