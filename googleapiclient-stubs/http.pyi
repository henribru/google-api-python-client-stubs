from _typeshed import Incomplete

from googleapiclient.errors import (
    BatchError as BatchError,
    HttpError as HttpError,
    InvalidChunkSizeError as InvalidChunkSizeError,
    ResumableUploadError as ResumableUploadError,
    UnexpectedBodyError as UnexpectedBodyError,
    UnexpectedMethodError as UnexpectedMethodError,
)
from googleapiclient.model import JsonModel as JsonModel

LOGGER: Incomplete
DEFAULT_CHUNK_SIZE: Incomplete
MAX_URI_LENGTH: int
MAX_BATCH_LIMIT: int
DEFAULT_HTTP_TIMEOUT_SEC: int

class MediaUploadProgress:
    resumable_progress: Incomplete
    total_size: Incomplete
    def __init__(self, resumable_progress, total_size) -> None: ...
    def progress(self): ...

class MediaDownloadProgress:
    resumable_progress: Incomplete
    total_size: Incomplete
    def __init__(self, resumable_progress, total_size) -> None: ...
    def progress(self): ...

class MediaUpload:
    def chunksize(self) -> None: ...
    def mimetype(self): ...
    def size(self) -> None: ...
    def resumable(self): ...
    def getbytes(self, begin, end) -> None: ...
    def has_stream(self): ...
    def stream(self) -> None: ...
    def to_json(self): ...
    @classmethod
    def new_from_json(cls, s): ...

class MediaIoBaseUpload(MediaUpload):
    def __init__(
        self, fd, mimetype, chunksize=104857600, resumable: bool = False
    ) -> None: ...
    def chunksize(self): ...
    def mimetype(self): ...
    def size(self): ...
    def resumable(self): ...
    def getbytes(self, begin, length): ...
    def has_stream(self): ...
    def stream(self): ...
    def to_json(self) -> None: ...

class MediaFileUpload(MediaIoBaseUpload):
    def __init__(
        self,
        filename,
        mimetype: Incomplete | None = None,
        chunksize=104857600,
        resumable: bool = False,
    ) -> None: ...
    def __del__(self) -> None: ...
    def to_json(self): ...
    @staticmethod
    def from_json(s): ...

class MediaInMemoryUpload(MediaIoBaseUpload):
    def __init__(
        self,
        body,
        mimetype: str = "application/octet-stream",
        chunksize=104857600,
        resumable: bool = False,
    ) -> None: ...

class MediaIoBaseDownload:
    def __init__(self, fd, request, chunksize=104857600) -> None: ...
    def next_chunk(self, num_retries: int = 0): ...

class _StreamSlice:
    def __init__(self, stream, begin, chunksize) -> None: ...
    def read(self, n: int = -1): ...

class HttpRequest:
    uri: Incomplete
    method: Incomplete
    body: Incomplete
    headers: Incomplete
    methodId: Incomplete
    http: Incomplete
    postproc: Incomplete
    resumable: Incomplete
    response_callbacks: Incomplete
    body_size: Incomplete
    resumable_uri: Incomplete
    resumable_progress: int
    def __init__(
        self,
        http,
        postproc,
        uri,
        method: str = "GET",
        body: Incomplete | None = None,
        headers: Incomplete | None = None,
        methodId: Incomplete | None = None,
        resumable: Incomplete | None = None,
    ) -> None: ...
    def execute(self, http: Incomplete | None = None, num_retries: int = 0): ...
    def add_response_callback(self, cb) -> None: ...
    def next_chunk(self, http: Incomplete | None = None, num_retries: int = 0): ...
    def to_json(self): ...
    @staticmethod
    def from_json(s, http, postproc): ...
    @staticmethod
    def null_postproc(resp, contents): ...

class BatchHttpRequest:
    def __init__(
        self, callback: Incomplete | None = None, batch_uri: Incomplete | None = None
    ) -> None: ...
    def add(
        self,
        request,
        callback: Incomplete | None = None,
        request_id: Incomplete | None = None,
    ) -> None: ...
    def execute(self, http: Incomplete | None = None) -> None: ...

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
