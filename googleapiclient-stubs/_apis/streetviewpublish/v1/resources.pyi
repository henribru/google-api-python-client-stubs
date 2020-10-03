import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class StreetViewPublishResource(googleapiclient.discovery.Resource):
    class PhotoResource(googleapiclient.discovery.Resource):
        def startUpload(
            self, *, body: Empty = ..., **kwargs: typing.Any
        ) -> UploadRefHttpRequest: ...
        def delete(self, *, photoId: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def update(
            self,
            *,
            id: str,
            body: Photo = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
        def create(
            self, *, body: Photo = ..., **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
        def get(
            self,
            *,
            photoId: str,
            languageCode: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
    class PhotosResource(googleapiclient.discovery.Resource):
        def batchUpdate(
            self, *, body: BatchUpdatePhotosRequest = ..., **kwargs: typing.Any
        ) -> BatchUpdatePhotosResponseHttpRequest: ...
        def batchGet(
            self,
            *,
            photoIds: typing.Union[str, typing.List[str]] = ...,
            languageCode: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> BatchGetPhotosResponseHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            languageCode: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListPhotosResponseHttpRequest: ...
        def batchDelete(
            self, *, body: BatchDeletePhotosRequest = ..., **kwargs: typing.Any
        ) -> BatchDeletePhotosResponseHttpRequest: ...
    def photo(self) -> PhotoResource: ...
    def photos(self) -> PhotosResource: ...

class BatchDeletePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchDeletePhotosResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class UploadRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UploadRef: ...

class BatchGetPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetPhotosResponse: ...

class BatchUpdatePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdatePhotosResponse: ...

class ListPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPhotosResponse: ...

class PhotoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Photo: ...
