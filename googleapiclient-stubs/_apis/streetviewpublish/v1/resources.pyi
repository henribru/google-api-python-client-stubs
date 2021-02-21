import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class StreetViewPublishResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PhotoResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Photo = ..., **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
        def delete(self, *, photoId: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            photoId: str,
            languageCode: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
        def startUpload(
            self, *, body: Empty = ..., **kwargs: typing.Any
        ) -> UploadRefHttpRequest: ...
        def update(
            self,
            *,
            id: str,
            body: Photo = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> PhotoHttpRequest: ...
    @typing.type_check_only
    class PhotosResource(googleapiclient.discovery.Resource):
        def batchDelete(
            self, *, body: BatchDeletePhotosRequest = ..., **kwargs: typing.Any
        ) -> BatchDeletePhotosResponseHttpRequest: ...
        def batchGet(
            self,
            *,
            languageCode: str = ...,
            photoIds: typing.Union[str, typing.List[str]] = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> BatchGetPhotosResponseHttpRequest: ...
        def batchUpdate(
            self, *, body: BatchUpdatePhotosRequest = ..., **kwargs: typing.Any
        ) -> BatchUpdatePhotosResponseHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> ListPhotosResponseHttpRequest: ...
    def photo(self) -> PhotoResource: ...
    def photos(self) -> PhotosResource: ...

@typing.type_check_only
class BatchDeletePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchDeletePhotosResponse: ...

@typing.type_check_only
class BatchGetPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchGetPhotosResponse: ...

@typing.type_check_only
class BatchUpdatePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchUpdatePhotosResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPhotosResponse: ...

@typing.type_check_only
class PhotoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Photo: ...

@typing.type_check_only
class UploadRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UploadRef: ...
