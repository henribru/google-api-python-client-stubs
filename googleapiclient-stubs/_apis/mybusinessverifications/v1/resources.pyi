import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
    @typing.type_check_only
    class VerificationTokensResource(googleapiclient.discovery.Resource):
        def generate(
            self, *, body: GenerateVerificationTokenRequest = ..., **kwargs: typing.Any
        ) -> GenerateVerificationTokenResponseHttpRequest: ...
    def locations(self) -> LocationsResource: ...
    def verificationTokens(self) -> VerificationTokensResource: ...

@typing.type_check_only
class CompleteVerificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CompleteVerificationResponse: ...

@typing.type_check_only
class FetchVerificationOptionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> FetchVerificationOptionsResponse: ...

@typing.type_check_only
class GenerateVerificationTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GenerateVerificationTokenResponse: ...

@typing.type_check_only
class ListVerificationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVerificationsResponse: ...

@typing.type_check_only
class VerifyLocationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VerifyLocationResponse: ...

@typing.type_check_only
class VoiceOfMerchantStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VoiceOfMerchantState: ...
