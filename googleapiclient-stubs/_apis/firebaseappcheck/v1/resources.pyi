import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseappcheckResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class JwksResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleFirebaseAppcheckV1PublicJwkSetHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppAttestConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1AppAttestConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1AppAttestConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1AppAttestConfigHttpRequest: ...

            @typing.type_check_only
            class DebugTokensResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirebaseAppcheckV1DebugToken = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1DebugTokenHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1DebugTokenHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1ListDebugTokensResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleFirebaseAppcheckV1ListDebugTokensResponseHttpRequest,
                    previous_response: GoogleFirebaseAppcheckV1ListDebugTokensResponse,
                ) -> GoogleFirebaseAppcheckV1ListDebugTokensResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1DebugToken = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1DebugTokenHttpRequest: ...

            @typing.type_check_only
            class DeviceCheckConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1DeviceCheckConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1DeviceCheckConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1DeviceCheckConfigHttpRequest: ...

            @typing.type_check_only
            class PlayIntegrityConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1PlayIntegrityConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1PlayIntegrityConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1PlayIntegrityConfigHttpRequest: ...

            @typing.type_check_only
            class RecaptchaEnterpriseConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigHttpRequest: ...

            @typing.type_check_only
            class RecaptchaV3ConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1RecaptchaV3ConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1RecaptchaV3Config = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1RecaptchaV3ConfigHttpRequest: ...

            @typing.type_check_only
            class SafetyNetConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1SafetyNetConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1SafetyNetConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1SafetyNetConfigHttpRequest: ...

            def exchangeAppAttestAssertion(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeAppAttestAssertionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeAppAttestAttestation(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseHttpRequest: ...
            def exchangeCustomToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeCustomTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeDebugToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeDebugTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeDeviceCheckToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeDeviceCheckTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangePlayIntegrityToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangePlayIntegrityTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeRecaptchaEnterpriseToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeRecaptchaEnterpriseTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeRecaptchaV3Token(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeRecaptchaV3TokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def exchangeSafetyNetToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1ExchangeSafetyNetTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest: ...
            def generateAppAttestChallenge(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1GenerateAppAttestChallengeRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseHttpRequest: ...
            def generatePlayIntegrityChallenge(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseHttpRequest: ...
            def appAttestConfig(self) -> AppAttestConfigResource: ...
            def debugTokens(self) -> DebugTokensResource: ...
            def deviceCheckConfig(self) -> DeviceCheckConfigResource: ...
            def playIntegrityConfig(self) -> PlayIntegrityConfigResource: ...
            def recaptchaEnterpriseConfig(
                self,
            ) -> RecaptchaEnterpriseConfigResource: ...
            def recaptchaV3Config(self) -> RecaptchaV3ConfigResource: ...
            def safetyNetConfig(self) -> SafetyNetConfigResource: ...

        @typing.type_check_only
        class ServicesResource(googleapiclient.discovery.Resource):
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleFirebaseAppcheckV1BatchUpdateServicesRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1BatchUpdateServicesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1ServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1ListServicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleFirebaseAppcheckV1ListServicesResponseHttpRequest,
                previous_response: GoogleFirebaseAppcheckV1ListServicesResponse,
            ) -> GoogleFirebaseAppcheckV1ListServicesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleFirebaseAppcheckV1Service = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1ServiceHttpRequest: ...

        def apps(self) -> AppsResource: ...
        def services(self) -> ServicesResource: ...

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
    def jwks(self) -> JwksResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppAttestConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1AppAttestConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1AppCheckTokenHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1AppCheckToken: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetAppAttestConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetDeviceCheckConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetPlayIntegrityConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetRecaptchaEnterpriseConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetRecaptchaV3ConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchGetSafetyNetConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1BatchUpdateServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1BatchUpdateServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1DebugTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1DebugToken: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1DeviceCheckConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1DeviceCheckConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1ExchangeAppAttestAttestationResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1GenerateAppAttestChallengeResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1GeneratePlayIntegrityChallengeResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListDebugTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1ListDebugTokensResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1ListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1ListServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1PlayIntegrityConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1PlayIntegrityConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1PublicJwkSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1PublicJwkSet: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1RecaptchaEnterpriseConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1RecaptchaV3ConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1RecaptchaV3Config: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1SafetyNetConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1SafetyNetConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1Service: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
