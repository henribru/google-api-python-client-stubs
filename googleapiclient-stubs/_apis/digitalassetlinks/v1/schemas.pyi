import typing

import typing_extensions

_list = list

@typing.type_check_only
class AndroidAppAsset(typing_extensions.TypedDict, total=False):
    certificate: CertificateInfo
    packageName: str

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    androidApp: AndroidAppAsset
    web: WebAsset

@typing.type_check_only
class BulkCheckRequest(typing_extensions.TypedDict, total=False):
    allowGoogleInternalDataSources: bool
    defaultRelation: str
    defaultSource: Asset
    defaultTarget: Asset
    skipCacheLookup: bool
    statements: _list[StatementTemplate]

@typing.type_check_only
class BulkCheckResponse(typing_extensions.TypedDict, total=False):
    bulkErrorCode: typing_extensions.Literal[
        "ERROR_CODE_UNSPECIFIED",
        "ERROR_CODE_INVALID_QUERY",
        "ERROR_CODE_FETCH_ERROR",
        "ERROR_CODE_FAILED_SSL_VALIDATION",
        "ERROR_CODE_REDIRECT",
        "ERROR_CODE_TOO_LARGE",
        "ERROR_CODE_MALFORMED_HTTP_RESPONSE",
        "ERROR_CODE_WRONG_CONTENT_TYPE",
        "ERROR_CODE_MALFORMED_CONTENT",
        "ERROR_CODE_SECURE_ASSET_INCLUDES_INSECURE",
        "ERROR_CODE_FETCH_BUDGET_EXHAUSTED",
    ]
    checkResults: _list[CheckResponse]

@typing.type_check_only
class CertificateInfo(typing_extensions.TypedDict, total=False):
    sha256Fingerprint: str

@typing.type_check_only
class CheckResponse(typing_extensions.TypedDict, total=False):
    debugString: str
    errorCode: _list[str]
    linked: bool
    maxAge: str

@typing.type_check_only
class ListResponse(typing_extensions.TypedDict, total=False):
    debugString: str
    errorCode: _list[str]
    maxAge: str
    statements: _list[Statement]

@typing.type_check_only
class Statement(typing_extensions.TypedDict, total=False):
    relation: str
    source: Asset
    target: Asset

@typing.type_check_only
class StatementTemplate(typing_extensions.TypedDict, total=False):
    relation: str
    source: Asset
    target: Asset

@typing.type_check_only
class WebAsset(typing_extensions.TypedDict, total=False):
    site: str
