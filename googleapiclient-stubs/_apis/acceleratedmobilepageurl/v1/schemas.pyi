import typing

import typing_extensions

class AmpUrl(typing_extensions.TypedDict, total=False):
    cdnAmpUrl: str
    originalUrl: str
    ampUrl: str

class AmpUrlError(typing_extensions.TypedDict, total=False):
    originalUrl: str
    errorMessage: str
    errorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "INPUT_URL_NOT_FOUND",
        "NO_AMP_URL",
        "APPLICATION_ERROR",
        "URL_IS_VALID_AMP",
        "URL_IS_INVALID_AMP",
    ]

class BatchGetAmpUrlsResponse(typing_extensions.TypedDict, total=False):
    ampUrls: typing.List[AmpUrl]
    urlErrors: typing.List[AmpUrlError]

class BatchGetAmpUrlsRequest(typing_extensions.TypedDict, total=False):
    urls: typing.List[str]
    lookupStrategy: typing_extensions.Literal["FETCH_LIVE_DOC", "IN_INDEX_DOC"]
