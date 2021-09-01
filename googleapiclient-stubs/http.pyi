from typing import Any, Optional

from googleapiclient.errors import (
    BatchError as BatchError,
    HttpError as HttpError,
    InvalidChunkSizeError as InvalidChunkSizeError,
    ResumableUploadError as ResumableUploadError,
    UnexpectedBodyError as UnexpectedBodyError,
    UnexpectedMethodError as UnexpectedMethodError,
)
from googleapiclient.model import JsonModel as JsonModel

LOGGER: Any
DEFAULT_CHUNK_SIZE: Any
MAX_URI_LENGTH: int
MAX_BATCH_LIMIT: int
DEFAULT_HTTP_TIMEOUT_SEC: int

class MediaUploadProgress:
    resumable_progress: Any = ...
    total_size: Any = ...
    def __init__(self, resumable_progress: Any, total_size: Any) -> None: ...
    def progress(self): ...

class MediaDownloadProgress:
    resumable_progress: Any = ...
    total_size: Any = ...
    def __init__(self, resumable_progress: Any, total_size: Any) -> None: ...
    def progress(self): ...

class MediaUpload:
    def chunksize(self) -> None: ...
    def mimetype(self): ...
    def size(self) -> None: ...
    def resumable(self): ...
    def getbytes(self, begin: Any, end: Any) -> None: ...
    def has_stream(self): ...
    def stream(self) -> None: ...
    def to_json(self): ...
    @classmethod
    def new_from_json(cls, s: Any): ...

class MediaIoBaseUpload(MediaUpload):
    def __init__(
        self, fd: Any, mimetype: Any, chunksize: Any = ..., resumable: bool = ...
    ) -> None: ...
    def chunksize(self): ...
    def mimetype(self): ...
    def size(self): ...
    def resumable(self): ...
    def getbytes(self, begin: Any, length: Any): ...
    def has_stream(self): ...
    def stream(self): ...
    def to_json(self) -> None: ...

class MediaFileUpload(MediaIoBaseUpload):
    def __init__(
        self,
        filename: Any,
        mimetype: Optional[Any] = ...,
        chunksize: Any = ...,
        resumable: bool = ...,
    ) -> None: ...
    def __del__(self) -> None: ...
    def to_json(self): ...
    @staticmethod
    def from_json(s: Any): ...

class MediaInMemoryUpload(MediaIoBaseUpload):
    def __init__(
        self,
        body: Any,
        mimetype: str = ...,
        chunksize: Any = ...,
        resumable: bool = ...,
    ) -> None: ...

class MediaIoBaseDownload:
    def __init__(self, fd: Any, request: Any, chunksize: Any = ...) -> None: ...
    def next_chunk(self, num_retries: int = ...): ...

class _StreamSlice:
    def __init__(self, stream: Any, begin: Any, chunksize: Any) -> None: ...
    def read(self, n: int = ...): ...

class HttpRequest:
    uri: Any = ...
    method: Any = ...
    body: Any = ...
    headers: Any = ...
    methodId: Any = ...
    http: Any = ...
    postproc: Any = ...
    resumable: Any = ...
    response_callbacks: Any = ...
    body_size: Any = ...
    resumable_uri: Any = ...
    resumable_progress: int = ...
    def __init__(
        self,
        http: Any,
        postproc: Any,
        uri: Any,
        method: str = ...,
        body: Optional[Any] = ...,
        headers: Optional[Any] = ...,
        methodId: Optional[Any] = ...,
        resumable: Optional[Any] = ...,
    ) -> None: ...
    def execute(self, http: Optional[Any] = ..., num_retries: int = ...): ...
    def add_response_callback(self, cb: Any) -> None: ...
    def next_chunk(self, http: Optional[Any] = ..., num_retries: int = ...): ...
    def to_json(self): ...
    @staticmethod
    def from_json(s: Any, http: Any, postproc: Any): ...
    @staticmethod
    def null_postproc(resp: Any, contents: Any): ...

class BatchHttpRequest:
    def __init__(
        self, callback: Optional[Any] = ..., batch_uri: Optional[Any] = ...
    ) -> None: ...
    def add(
        self,
        request: Any,
        callback: Optional[Any] = ...,
        request_id: Optional[Any] = ...,
    ) -> None: ...
    def execute(self, http: Optional[Any] = ...) -> None: ...

class HttpRequestMock:
    resp: Any = ...
    content: Any = ...
    postproc: Any = ...
    def __init__(self, resp: Any, content: Any, postproc: Any) -> None: ...
    def execute(self, http: Optional[Any] = ...): ...

class RequestMockBuilder:
    responses: Any = ...
    check_unexpected: Any = ...
    def __init__(self, responses: Any, check_unexpected: bool = ...) -> None: ...
    def __call__(
        self,
        http: Any,
        postproc: Any,
        uri: Any,
        method: str = ...,
        body: Optional[Any] = ...,
        headers: Optional[Any] = ...,
        methodId: Optional[Any] = ...,
        resumable: Optional[Any] = ...,
    ): ...

class HttpMock:
    data: Any = ...
    response_headers: Any = ...
    headers: Any = ...
    uri: Any = ...
    method: Any = ...
    body: Any = ...
    def __init__(
        self, filename: Optional[Any] = ..., headers: Optional[Any] = ...
    ) -> None: ...
    def request(
        self,
        uri: Any,
        method: str = ...,
        body: Optional[Any] = ...,
        headers: Optional[Any] = ...,
        redirections: int = ...,
        connection_type: Optional[Any] = ...,
    ): ...
    def close(self) -> None: ...

class HttpMockSequence:
    follow_redirects: bool = ...
    request_sequence: Any = ...
    def __init__(self, iterable: Any) -> None: ...
    def request(
        self,
        uri: Any,
        method: str = ...,
        body: Optional[Any] = ...,
        headers: Optional[Any] = ...,
        redirections: int = ...,
        connection_type: Optional[Any] = ...,
    ): ...

def set_user_agent(http: Any, user_agent: Any): ...
def tunnel_patch(http: Any): ...
def build_http(): ...
