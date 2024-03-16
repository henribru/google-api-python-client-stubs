import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SlidesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PresentationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PagesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, presentationId: str, pageObjectId: str, **kwargs: typing.Any
            ) -> PageHttpRequest: ...
            def getThumbnail(
                self,
                *,
                presentationId: str,
                pageObjectId: str,
                thumbnailProperties_mimeType: typing_extensions.Literal["PNG"] = ...,
                thumbnailProperties_thumbnailSize: typing_extensions.Literal[
                    "THUMBNAIL_SIZE_UNSPECIFIED", "LARGE", "MEDIUM", "SMALL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> ThumbnailHttpRequest: ...

        def batchUpdate(
            self,
            *,
            presentationId: str,
            body: BatchUpdatePresentationRequest = ...,
            **kwargs: typing.Any,
        ) -> BatchUpdatePresentationResponseHttpRequest: ...
        def create(
            self, *, body: Presentation = ..., **kwargs: typing.Any
        ) -> PresentationHttpRequest: ...
        def get(
            self, *, presentationId: str, **kwargs: typing.Any
        ) -> PresentationHttpRequest: ...
        def pages(self) -> PagesResource: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def presentations(self) -> PresentationsResource: ...

@typing.type_check_only
class BatchUpdatePresentationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdatePresentationResponse: ...

@typing.type_check_only
class PageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Page: ...

@typing.type_check_only
class PresentationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Presentation: ...

@typing.type_check_only
class ThumbnailHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Thumbnail: ...
