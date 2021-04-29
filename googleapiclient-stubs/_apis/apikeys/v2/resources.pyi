import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
                def clone(
                    self,
                    *,
                    name: str,
                    body: V2CloneKeyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
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
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> V2ListKeysResponseHttpRequest: ...
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
    def keys(self) -> KeysResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class V2GetKeyStringResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V2GetKeyStringResponse: ...

@typing.type_check_only
class V2KeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V2Key: ...

@typing.type_check_only
class V2ListKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V2ListKeysResponse: ...

@typing.type_check_only
class V2LookupKeyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V2LookupKeyResponse: ...
