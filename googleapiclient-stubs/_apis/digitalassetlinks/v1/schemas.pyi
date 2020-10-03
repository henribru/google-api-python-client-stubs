import typing

import typing_extensions

class WebAsset(typing_extensions.TypedDict, total=False):
    site: str

class AndroidAppAsset(typing_extensions.TypedDict, total=False):
    certificate: CertificateInfo
    packageName: str

class CheckResponse(typing_extensions.TypedDict, total=False):
    errorCode: typing.List[str]
    maxAge: str
    debugString: str
    linked: bool

class Statement(typing_extensions.TypedDict, total=False):
    relation: str
    target: Asset
    source: Asset

class ListResponse(typing_extensions.TypedDict, total=False):
    statements: typing.List[Statement]
    debugString: str
    maxAge: str
    errorCode: typing.List[str]

class Asset(typing_extensions.TypedDict, total=False):
    androidApp: AndroidAppAsset
    web: WebAsset

class CertificateInfo(typing_extensions.TypedDict, total=False):
    sha256Fingerprint: str
