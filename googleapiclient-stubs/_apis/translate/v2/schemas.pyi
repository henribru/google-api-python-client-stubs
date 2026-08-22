import typing

_list = list

@typing.type_check_only
class DetectLanguageRequest(typing.TypedDict, total=False):
    q: _list[str]

@typing.type_check_only
class DetectionsListResponse(typing.TypedDict, total=False):
    detections: _list[DetectionsResource]

@typing.type_check_only
class DetectionsResource(dict[str, typing.Any]): ...

@typing.type_check_only
class GetSupportedLanguagesRequest(typing.TypedDict, total=False):
    target: str

@typing.type_check_only
class LanguagesListResponse(typing.TypedDict, total=False):
    languages: _list[LanguagesResource]

@typing.type_check_only
class LanguagesResource(typing.TypedDict, total=False):
    language: str
    name: str

@typing.type_check_only
class TranslateTextRequest(typing.TypedDict, total=False):
    format: str
    model: str
    q: _list[str]
    source: str
    target: str

@typing.type_check_only
class TranslationsListResponse(typing.TypedDict, total=False):
    translations: _list[TranslationsResource]

@typing.type_check_only
class TranslationsResource(typing.TypedDict, total=False):
    detectedSourceLanguage: str
    model: str
    translatedText: str
