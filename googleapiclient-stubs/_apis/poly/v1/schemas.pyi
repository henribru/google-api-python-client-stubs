import typing

import typing_extensions

class FormatComplexity(typing_extensions.TypedDict, total=False):
    lodHint: int
    triangleCount: str

class Quaternion(typing_extensions.TypedDict, total=False):
    z: float
    w: float
    x: float
    y: float

class ImageError(typing_extensions.TypedDict, total=False):
    filePath: str
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "INVALID_IMAGE", "IMAGE_TOO_BIG", "WRONG_IMAGE_TYPE"
    ]

class UserAsset(typing_extensions.TypedDict, total=False):
    asset: Asset

class ListUserAssetsResponse(typing_extensions.TypedDict, total=False):
    userAssets: typing.List[UserAsset]
    nextPageToken: str
    totalSize: int

class Asset(typing_extensions.TypedDict, total=False):
    updateTime: str
    metadata: str
    name: str
    license: typing_extensions.Literal[
        "UNKNOWN", "CREATIVE_COMMONS_BY", "ALL_RIGHTS_RESERVED"
    ]
    visibility: typing_extensions.Literal[
        "VISIBILITY_UNSPECIFIED", "PRIVATE", "UNLISTED", "PUBLIC"
    ]
    displayName: str
    remixInfo: RemixInfo
    thumbnail: File
    authorName: str
    presentationParams: PresentationParams
    description: str
    createTime: str
    formats: typing.List[Format]
    isCurated: bool

class File(typing_extensions.TypedDict, total=False):
    contentType: str
    url: str
    relativePath: str

class PresentationParams(typing_extensions.TypedDict, total=False):
    backgroundColor: str
    colorSpace: typing_extensions.Literal["UNKNOWN", "LINEAR", "GAMMA"]
    orientingRotation: Quaternion

class Format(typing_extensions.TypedDict, total=False):
    formatType: str
    root: File
    formatComplexity: FormatComplexity
    resources: typing.List[File]

class RemixInfo(typing_extensions.TypedDict, total=False):
    sourceAsset: typing.List[str]

class ListLikedAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: typing.List[Asset]
    nextPageToken: str
    totalSize: int

class ListAssetsResponse(typing_extensions.TypedDict, total=False):
    assets: typing.List[Asset]
    nextPageToken: str
    totalSize: int

class ObjParseError(typing_extensions.TypedDict, total=False):
    filePath: str
    lineNumber: int
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
    line: str
    endIndex: int
    startIndex: int

class AssetImportMessage(typing_extensions.TypedDict, total=False):
    imageError: ImageError
    objParseError: ObjParseError
    filePath: str
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

class StartAssetImportResponse(typing_extensions.TypedDict, total=False):
    assetId: str
    assetImportId: str
    assetImportMessages: typing.List[AssetImportMessage]
    publishUrl: str
