import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SlidesResource(googleapiclient.discovery.Resource):
    class PresentationsResource(googleapiclient.discovery.Resource):
        class PagesResource(googleapiclient.discovery.Resource):
            def getThumbnail(
                self,
                *,
                presentationId: str,
                pageObjectId: str,
                thumbnailProperties_mimeType: typing_extensions.Literal["PNG"] = ...,
                thumbnailProperties_thumbnailSize: typing_extensions.Literal[
                    "THUMBNAIL_SIZE_UNSPECIFIED", "LARGE", "MEDIUM", "SMALL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ThumbnailHttpRequest: ...
            def get(
                self, *, presentationId: str, pageObjectId: str, **kwargs: typing.Any
            ) -> PageHttpRequest: ...
        def get(
            self, *, presentationId: str, **kwargs: typing.Any
        ) -> PresentationHttpRequest: ...
        def create(
            self, *, body: Presentation = ..., **kwargs: typing.Any
        ) -> PresentationHttpRequest: ...
        def batchUpdate(
            self,
            *,
            presentationId: str,
            body: BatchUpdatePresentationRequest = ...,
            **kwargs: typing.Any
        ) -> BatchUpdatePresentationResponseHttpRequest: ...
        def pages(self) -> PagesResource: ...
    def presentations(self) -> PresentationsResource: ...

class ThumbnailHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Thumbnail: ...

class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Page: ...

class PresentationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Presentation: ...

class BatchUpdatePresentationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdatePresentationResponse: ...
