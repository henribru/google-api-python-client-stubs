import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
    class PhotoSequenceResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: PhotoSequence = ...,
            inputType: typing_extensions.Literal[
                "INPUT_TYPE_UNSPECIFIED", "VIDEO", "XDM"
            ] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, sequenceId: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self,
            *,
            sequenceId: str,
            filter: str = ...,
            view: typing_extensions.Literal["BASIC", "INCLUDE_DOWNLOAD_URL"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def startUpload(
            self, *, body: Empty = ..., **kwargs: typing.Any
        ) -> UploadRefHttpRequest: ...

    @typing.type_check_only
    class PhotoSequencesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListPhotoSequencesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListPhotoSequencesResponseHttpRequest,
            previous_response: ListPhotoSequencesResponse,
        ) -> ListPhotoSequencesResponseHttpRequest | None: ...

    @typing.type_check_only
    class PhotosResource(googleapiclient.discovery.Resource):
        def batchDelete(
            self, *, body: BatchDeletePhotosRequest = ..., **kwargs: typing.Any
        ) -> BatchDeletePhotosResponseHttpRequest: ...
        def batchGet(
            self,
            *,
            languageCode: str = ...,
            photoIds: str | _list[str] = ...,
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
        def list_next(
            self,
            previous_request: ListPhotosResponseHttpRequest,
            previous_response: ListPhotosResponse,
        ) -> ListPhotosResponseHttpRequest | None: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def photo(self) -> PhotoResource: ...
    def photoSequence(self) -> PhotoSequenceResource: ...
    def photoSequences(self) -> PhotoSequencesResource: ...
    def photos(self) -> PhotosResource: ...

@typing.type_check_only
class BatchDeletePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchDeletePhotosResponse: ...

@typing.type_check_only
class BatchGetPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetPhotosResponse: ...

@typing.type_check_only
class BatchUpdatePhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdatePhotosResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListPhotoSequencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPhotoSequencesResponse: ...

@typing.type_check_only
class ListPhotosResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPhotosResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PhotoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Photo: ...

@typing.type_check_only
class UploadRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UploadRef: ...
