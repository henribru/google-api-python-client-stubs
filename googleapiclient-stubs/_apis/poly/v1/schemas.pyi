import typing

import typing_extensions

_list = list

@typing.type_check_only
class Asset(typing_extensions.TypedDict, total=False):
    authorName: str
    createTime: str
    description: str
    displayName: str
    formats: _list[Format]
    isCurated: bool
    license: typing_extensions.Literal[
        "UNKNOWN", "CREATIVE_COMMONS_BY", "ALL_RIGHTS_RESERVED"
    ]
    metadata: str
    name: str
    presentationParams: PresentationParams
    remixInfo: RemixInfo
    thumbnail: File
    updateTime: str
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED", "PRIVATE", "UNLISTED", "PUBLIC"
    ]

@typing.type_check_only
class AssetImportMessage(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "NO_IMPORTABLE_FILE",
        "EMPTY_MODEL",
        "OBJ_PARSE_ERROR",
        "EXPIRED",
        "IMAGE_ERROR",
        "EXTRA_FILES_WITH_ARCHIVE",
        "DEFAULT_MATERIALS",
        "FATAL_ERROR",
        "INVALID_ELEMENT_TYPE",
    ]
    filePath: str
    imageError: ImageError
    objParseError: ObjParseError

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    contentType: str
    relativePath: str
    url: str

@typing.type_check_only
class Format(typing_extensions.TypedDict, total=False):
    formatComplexity: FormatComplexity
    formatType: str
    resources: _list[File]
    root: File

@typing.type_check_only
class FormatComplexity(typing_extensions.TypedDict, total=False):
    lodHint: int
    triangleCount: str

@typing.type_check_only
class ImageError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "INVALID_IMAGE", "IMAGE_TOO_BIG", "WRONG_IMAGE_TYPE"
    ]
    filePath: str

@typing.type_check_only
class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[Asset]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListLikedAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: _list[Asset]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListUserAssetsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    totalSize: int
    userAssets: _list[UserAsset]

@typing.type_check_only
class ObjParseError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "INCONSISTENT_VERTEX_REFS",
        "INVALID_COMMAND",
        "INVALID_NUMBER",
        "INVALID_VERTEX_REF",
        "MISSING_GEOMETRIC_VERTEX",
        "MISSING_TOKEN",
        "TOO_FEW_DIMENSIONS",
        "TOO_FEW_VERTICES",
        "TOO_MANY_DIMENSIONS",
        "UNSUPPORTED_COMMAND",
        "UNUSED_TOKENS",
        "VERTEX_NOT_FOUND",
        "NUMBER_OUT_OF_RANGE",
        "INVALID_VALUE",
        "INVALID_TEXTURE_OPTION",
        "TOO_MANY_PROBLEMS",
        "MISSING_FILE_NAME",
        "FILE_NOT_FOUND",
        "UNKNOWN_MATERIAL",
        "NO_MATERIAL_DEFINED",
        "INVALID_SMOOTHING_GROUP",
        "MISSING_VERTEX_COLORS",
        "FILE_SUBSTITUTION",
        "LINE_TOO_LONG",
        "INVALID_FILE_PATH",
    ]
    endIndex: int
    filePath: str
    line: str
    lineNumber: int
    startIndex: int

@typing.type_check_only
class PresentationParams(typing_extensions.TypedDict, total=False):
    backgroundColor: str
    colorSpace: typing_extensions.Literal["UNKNOWN", "LINEAR", "GAMMA"]
    orientingRotation: Quaternion

@typing.type_check_only
class Quaternion(typing_extensions.TypedDict, total=False):
    w: float
    x: float
    y: float
    z: float

@typing.type_check_only
class RemixInfo(typing_extensions.TypedDict, total=False):
    sourceAsset: _list[str]

@typing.type_check_only
class StartAssetImportResponse(typing_extensions.TypedDict, total=False):
    assetId: str
    assetImportId: str
    assetImportMessages: _list[AssetImportMessage]
    publishUrl: str

@typing.type_check_only
class UserAsset(typing_extensions.TypedDict, total=False):
    asset: Asset
