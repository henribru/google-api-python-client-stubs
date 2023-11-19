import httplib2  # type: ignore[import-untyped]
from _typeshed import Incomplete

class Error(Exception): ...

class HttpError(Error):
    resp: httplib2.Response
    content: bytes
    uri: str | None
    error_details: str
    reason: str
    def __init__(
        self, resp: httplib2.Response, content: bytes, uri: str | None = None
    ) -> None: ...
    @property
    def status_code(self) -> int: ...

class InvalidJsonError(Error): ...
class UnknownFileType(Error): ...
class UnknownLinkType(Error): ...
class UnknownApiNameOrVersion(Error): ...
class UnacceptableMimeTypeError(Error): ...
class MediaUploadSizeError(Error): ...
class ResumableUploadError(HttpError): ...
class InvalidChunkSizeError(Error): ...
class InvalidNotificationError(Error): ...

class BatchError(HttpError):
    resp: httplib2.Response | None  # type: ignore[assignment]
    content: str | None  # type: ignore[assignment]
    reason: str
    def __init__(
        self,
        reason: str,
        resp: httplib2.Response | None = None,
        content: str | None = None,
    ) -> None: ...

class UnexpectedMethodError(Error):
    def __init__(self, methodId: Incomplete | None = None) -> None: ...

class UnexpectedBodyError(Error):
    def __init__(self, expected, provided) -> None: ...
