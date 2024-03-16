import collections.abc
import io
import logging
import typing

import httplib2
from _typeshed import Incomplete, StrPath

from googleapiclient.errors import (
    BatchError as BatchError,
    HttpError as HttpError,
    InvalidChunkSizeError as InvalidChunkSizeError,
    ResumableUploadError as ResumableUploadError,
    UnexpectedBodyError as UnexpectedBodyError,
    UnexpectedMethodError as UnexpectedMethodError,
)
from googleapiclient.model import JsonModel as JsonModel

LOGGER: logging.Logger
DEFAULT_CHUNK_SIZE: int
MAX_URI_LENGTH: int
MAX_BATCH_LIMIT: int
DEFAULT_HTTP_TIMEOUT_SEC: int

class MediaUploadProgress:
    resumable_progress: int
    total_size: int
    def __init__(self, resumable_progress: int, total_size: int) -> None: ...
    def progress(self) -> float: ...

class MediaDownloadProgress:
    resumable_progress: int
    total_size: int
    def __init__(self, resumable_progress: int, total_size: int) -> None: ...
    def progress(self) -> float: ...

_T = typing.TypeVar("_T")

class MediaUpload:
    def chunksize(self) -> int: ...
    def mimetype(self) -> str: ...
    def size(self) -> int | None: ...
    def resumable(self) -> bool: ...
    def getbytes(self, begin: int, end: int) -> bytes: ...
    def has_stream(self) -> bool: ...
    def stream(self) -> io.IOBase: ...
    def to_json(self) -> str: ...
    @classmethod
    def new_from_json(cls: _T, s: str) -> _T: ...

class MediaIoBaseUpload(MediaUpload):
    def __init__(
        self,
        fd: io.IOBase,
        mimetype: str,
        chunksize: int = 104857600,
        resumable: bool = False,
    ) -> None: ...

class MediaFileUpload(MediaIoBaseUpload):
    def __init__(
        self,
        filename: StrPath,
        mimetype: str | None = None,
        chunksize: int = 104857600,
        resumable: bool = False,
    ) -> None: ...

class MediaInMemoryUpload(MediaIoBaseUpload):
    def __init__(
        self,
        body: bytes,
        mimetype: str = "application/octet-stream",
        chunksize: int = 104857600,
        resumable: bool = False,
    ) -> None: ...

class MediaIoBaseDownload:
    def __init__(
        self, fd: io.IOBase, request: HttpRequest, chunksize: int = 104857600
    ) -> None: ...
    def next_chunk(
        self, num_retries: int = 0
    ) -> tuple[MediaDownloadProgress, bool]: ...

class HttpRequest:
    uri: str
    method: str
    body: str | None
    headers: dict[str, str] | None
    methodId: str | None
    http: httplib2.Http | HttpMock
    postproc: collections.abc.Callable[[httplib2.Response, bytes], typing.Any]
    resumable: MediaUpload | None
    response_callbacks: collections.abc.Callable[[httplib2.Response], typing.Any]
    body_size: int
    resumable_uri: str | None
    resumable_progress: int
    def __init__(
        self,
        http: httplib2.Http | HttpMock,
        postproc: collections.abc.Callable[[httplib2.Response, bytes], typing.Any],
        uri: str,
        method: str = "GET",
        body: str | None = None,
        headers: dict[str, str] | None = None,
        methodId: str | None = None,
        resumable: MediaUpload | None = None,
    ) -> None: ...
    def execute(
        self, http: httplib2.Http | HttpMock | None = None, num_retries: int = 0
    ) -> typing.Any: ...
    def add_response_callback(
        self, cb: collections.abc.Callable[[httplib2.Response], typing.Any]
    ) -> None: ...
    def next_chunk(
        self, http: httplib2.Http | HttpMock | None = None, num_retries: int = 0
    ) -> tuple[MediaUploadProgress, typing.Any]: ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(
        s: str,
        http: httplib2.Http | HttpMock,
        postproc: collections.abc.Callable[[httplib2.Response, bytes], typing.Any],
    ) -> HttpRequest: ...
    @staticmethod
    def null_postproc(
        resp: httplib2.Response, contents: bytes
    ) -> tuple[httplib2.Response, bytes]: ...

class BatchHttpRequest:
    def __init__(
        self,
        callback: (
            collections.abc.Callable[[str, typing.Any, HttpError | None], typing.Any]
            | None
        ) = None,
        batch_uri: str | None = None,
    ) -> None: ...
    def add(
        self,
        request: HttpRequest,
        callback: (
            collections.abc.Callable[[str, typing.Any, HttpError], typing.Any] | None
        ) = None,
        request_id: str | None = None,
    ) -> None: ...
    def execute(self, http: httplib2.Http | HttpMock | None = None) -> None: ...

class HttpRequestMock:
    resp: Incomplete
    content: Incomplete
    postproc: Incomplete
    def __init__(self, resp, content, postproc) -> None: ...
    def execute(self, http: Incomplete | None = None): ...

class RequestMockBuilder:
    responses: Incomplete
    check_unexpected: Incomplete
    def __init__(self, responses, check_unexpected: bool = False) -> None: ...
    def __call__(
        self,
        http,
        postproc,
        uri,
        method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        methodId: Incomplete | None = None,
        resumable: Incomplete | None = None,
    ): ...

class HttpMock:
    data: Incomplete
    response_headers: Incomplete
    headers: Incomplete
    uri: Incomplete
    method: Incomplete
    body: Incomplete
    def __init__(
        self, filename: Incomplete | None = None, headers: Incomplete | None = None
    ) -> None: ...
    def request(
        self,
        uri,
        method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        redirections: int = 1,
        connection_type: Incomplete | None = None,
    ): ...
    def close(self) -> None: ...

class HttpMockSequence:
    follow_redirects: bool
    request_sequence: Incomplete
    def __init__(self, iterable) -> None: ...
    def request(
        self,
        uri,
        method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        redirections: int = 1,
        connection_type: Incomplete | None = None,
    ): ...

def set_user_agent(http, user_agent): ...
def tunnel_patch(http): ...
def build_http(): ...
