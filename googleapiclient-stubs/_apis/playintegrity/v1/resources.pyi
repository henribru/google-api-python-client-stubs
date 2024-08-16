import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class PlayIntegrityResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DeviceRecallResource(googleapiclient.discovery.Resource):
        def write(
            self,
            *,
            packageName: str,
            body: WriteDeviceRecallRequest = ...,
            **kwargs: typing.Any,
        ) -> WriteDeviceRecallResponseHttpRequest: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def decodeIntegrityToken(
            self,
            *,
            packageName: str,
            body: DecodeIntegrityTokenRequest = ...,
            **kwargs: typing.Any,
        ) -> DecodeIntegrityTokenResponseHttpRequest: ...

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
    def deviceRecall(self) -> DeviceRecallResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class DecodeIntegrityTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DecodeIntegrityTokenResponse: ...

@typing.type_check_only
class WriteDeviceRecallResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WriteDeviceRecallResponse: ...
