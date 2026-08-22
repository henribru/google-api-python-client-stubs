import typing

_list = list

@typing.type_check_only
class AndroidAppAsset(typing.TypedDict, total=False):
    certificate: CertificateInfo
    packageName: str

@typing.type_check_only
class Asset(typing.TypedDict, total=False):
    androidApp: AndroidAppAsset
    web: WebAsset

@typing.type_check_only
class BulkCheckRequest(typing.TypedDict, total=False):
    defaultRelation: str
    defaultSource: Asset
    defaultTarget: Asset
    returnRelationExtensions: bool
    statements: _list[StatementTemplate]

@typing.type_check_only
class BulkCheckResponse(typing.TypedDict, total=False):
    bulkErrorCode: typing.Literal[
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
class CertificateInfo(typing.TypedDict, total=False):
    sha256Fingerprint: str

@typing.type_check_only
class CheckResponse(typing.TypedDict, total=False):
    debugString: str
    errorCode: _list[
        typing.Literal[
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
    ]
    linked: bool
    maxAge: str
    relationExtensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class ListResponse(typing.TypedDict, total=False):
    debugString: str
    errorCode: _list[
        typing.Literal[
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
    ]
    maxAge: str
    statements: _list[Statement]

@typing.type_check_only
class Statement(typing.TypedDict, total=False):
    relation: str
    relationExtensions: dict[str, typing.Any]
    source: Asset
    target: Asset

@typing.type_check_only
class StatementTemplate(typing.TypedDict, total=False):
    relation: str
    source: Asset
    target: Asset

@typing.type_check_only
class WebAsset(typing.TypedDict, total=False):
    site: str
