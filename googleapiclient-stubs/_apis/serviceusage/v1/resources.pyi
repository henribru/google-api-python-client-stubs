import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceUsageResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str = ...,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
    class ServicesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleApiServiceusageV1ServiceHttpRequest: ...
        def batchGet(
            self,
            *,
            parent: str,
            names: typing.Union[str, typing.List[str]] = ...,
            **kwargs: typing.Any
        ) -> BatchGetServicesResponseHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageToken: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def batchEnable(
            self,
            *,
            parent: str,
            body: BatchEnableServicesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enable(
            self, *, name: str, body: EnableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def disable(
            self, *, name: str, body: DisableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class GoogleApiServiceusageV1ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleApiServiceusageV1Service: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class BatchGetServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetServicesResponse: ...
