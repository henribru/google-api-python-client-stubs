import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ApiKeysServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class KeysResource(googleapiclient.discovery.Resource):
        def lookupKey(
            self, *, keyString: str = ..., **kwargs: typing.Any
        ) -> V2LookupKeyResponseHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class KeysResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: V2Key = ...,
                    keyId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> V2KeyHttpRequest: ...
                def getKeyString(
                    self, *, name: str, **kwargs: typing.Any
                ) -> V2GetKeyStringResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> V2ListKeysResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: V2ListKeysResponseHttpRequest,
                    previous_response: V2ListKeysResponse,
                ) -> V2ListKeysResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: V2Key = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: V2UndeleteKeyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def keys(self) -> KeysResource: ...

        def locations(self) -> LocationsResource: ...

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
    def keys(self) -> KeysResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class V2GetKeyStringResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V2GetKeyStringResponse: ...

@typing.type_check_only
class V2KeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V2Key: ...

@typing.type_check_only
class V2ListKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V2ListKeysResponse: ...

@typing.type_check_only
class V2LookupKeyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V2LookupKeyResponse: ...
