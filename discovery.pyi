import types
from email.generator import BytesGenerator
from typing import Any, Protocol, TypeVar, overload

import google.auth.credentials
import httplib2
import oauth2client  # type: ignore[import-not-found]
from _typeshed import Incomplete
from google.api_core.client_options import ClientOptions
from typing_extensions import Literal

from googleapiclient.discovery_cache.base import Cache
from googleapiclient.http import HttpMock, HttpRequest
from googleapiclient.model import Model

_T = TypeVar("_T")

class _BytesGenerator(BytesGenerator): ...

def fix_method_name(name): ...
def key2param(key): ...

class ResourceMethodParameters:
    argmap: Incomplete
    required_params: Incomplete
    repeated_params: Incomplete
    pattern_params: Incomplete
    query_params: Incomplete
    path_params: Incomplete
    param_types: Incomplete
    enum_params: Incomplete
    def __init__(self, method_desc) -> None: ...
    def set_parameters(self, method_desc) -> None: ...

class Resource:
    def __init__(
        self,
        http,
        baseUrl,
        model,
        requestBuilder,
        developerKey,
        resourceDesc,
        rootDesc,
        schema,
    ) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...

class _RequestBuilder(Protocol):
    def __call__(
        self,
        http,
        postproc,
        uri,
        method: str = ...,
        body: Incomplete | None = ...,
        headers: Incomplete | None = ...,
        methodId: Incomplete | None = ...,
        resumable: Incomplete | None = ...,
    ) -> HttpRequest: ...
