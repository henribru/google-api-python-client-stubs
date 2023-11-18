import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessVerificationsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class VerificationsResource(googleapiclient.discovery.Resource):
            def complete(
                self,
                *,
                name: str,
                body: CompleteVerificationRequest = ...,
                **kwargs: typing.Any
            ) -> CompleteVerificationResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListVerificationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListVerificationsResponseHttpRequest,
                previous_response: ListVerificationsResponse,
            ) -> ListVerificationsResponseHttpRequest | None: ...

        def fetchVerificationOptions(
            self,
            *,
            location: str,
            body: FetchVerificationOptionsRequest = ...,
            **kwargs: typing.Any
        ) -> FetchVerificationOptionsResponseHttpRequest: ...
        def getVoiceOfMerchantState(
            self, *, name: str, **kwargs: typing.Any
        ) -> VoiceOfMerchantStateHttpRequest: ...
        def verify(
            self, *, name: str, body: VerifyLocationRequest = ..., **kwargs: typing.Any
        ) -> VerifyLocationResponseHttpRequest: ...
        def verifications(self) -> VerificationsResource: ...

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
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class CompleteVerificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CompleteVerificationResponse: ...

@typing.type_check_only
class FetchVerificationOptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FetchVerificationOptionsResponse: ...

@typing.type_check_only
class ListVerificationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVerificationsResponse: ...

@typing.type_check_only
class VerifyLocationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyLocationResponse: ...

@typing.type_check_only
class VoiceOfMerchantStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VoiceOfMerchantState: ...
