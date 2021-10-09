import typing

import typing_extensions

_list = list

@typing.type_check_only
class AmpUrl(typing_extensions.TypedDict, total=False):
    ampUrl: str
    cdnAmpUrl: str
    originalUrl: str

@typing.type_check_only
class AmpUrlError(typing_extensions.TypedDict, total=False):
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "INPUT_URL_NOT_FOUND",
        "NO_AMP_URL",
        "APPLICATION_ERROR",
        "URL_IS_VALID_AMP",
        "URL_IS_INVALID_AMP",
    ]
    errorMessage: str
    originalUrl: str

@typing.type_check_only
class BatchGetAmpUrlsRequest(typing_extensions.TypedDict, total=False):
    lookupStrategy: typing_extensions.Literal["FETCH_LIVE_DOC", "IN_INDEX_DOC"]
    urls: _list[str]

@typing.type_check_only
class BatchGetAmpUrlsResponse(typing_extensions.TypedDict, total=False):
    ampUrls: _list[AmpUrl]
    urlErrors: _list[AmpUrlError]
