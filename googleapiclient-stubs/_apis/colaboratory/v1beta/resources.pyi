import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ColabResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class RuntimesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: Runtime,
            requestId: str | None = ...,
            runtimeId: str | None = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, allowMissing: bool | None = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> RuntimeHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> ListRuntimesResponseHttpRequest: ...

    @typing.type_check_only
    class RuntimespecsResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> ListRuntimeSpecsResponseHttpRequest: ...

    @typing.type_check_only
    class V1betaResource(googleapiclient.discovery.Resource):
        def getSubscription(
            self, *, name: str, **kwargs: typing.Any
        ) -> SubscriptionHttpRequest: ...

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
    def runtimes(self) -> RuntimesResource: ...
    def runtimespecs(self) -> RuntimespecsResource: ...
    def v1beta(self) -> V1betaResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListRuntimeSpecsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimeSpecsResponse: ...

@typing.type_check_only
class ListRuntimesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRuntimesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class RuntimeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Runtime: ...

@typing.type_check_only
class SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Subscription: ...
