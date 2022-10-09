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
        ) -> GoogleFirebaseAppcheckV1betaPublicJwkSetHttpRequest: ...

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
                ) -> GoogleFirebaseAppcheckV1betaBatchGetAppAttestConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaAppAttestConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaAppAttestConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaAppAttestConfigHttpRequest: ...

            @typing.type_check_only
            class DebugTokensResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirebaseAppcheckV1betaDebugToken = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaDebugTokenHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaDebugTokenHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaListDebugTokensResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleFirebaseAppcheckV1betaListDebugTokensResponseHttpRequest,
                    previous_response: GoogleFirebaseAppcheckV1betaListDebugTokensResponse,
                ) -> GoogleFirebaseAppcheckV1betaListDebugTokensResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaDebugToken = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaDebugTokenHttpRequest: ...

            @typing.type_check_only
            class DeviceCheckConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaDeviceCheckConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaDeviceCheckConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaDeviceCheckConfigHttpRequest: ...

            @typing.type_check_only
            class PlayIntegrityConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetPlayIntegrityConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaPlayIntegrityConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaPlayIntegrityConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaPlayIntegrityConfigHttpRequest: ...

            @typing.type_check_only
            class RecaptchaConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaRecaptchaConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaConfigHttpRequest: ...

            @typing.type_check_only
            class RecaptchaEnterpriseConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaEnterpriseConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfigHttpRequest: ...

            @typing.type_check_only
            class RecaptchaV3ConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaV3ConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaV3ConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaRecaptchaV3Config = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaRecaptchaV3ConfigHttpRequest: ...

            @typing.type_check_only
            class SafetyNetConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaBatchGetSafetyNetConfigsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaSafetyNetConfigHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppcheckV1betaSafetyNetConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseAppcheckV1betaSafetyNetConfigHttpRequest: ...

            def exchangeAppAttestAssertion(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeAppAttestAssertionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeAppAttestAttestation(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationResponseHttpRequest: ...
            def exchangeCustomToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeCustomTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeDebugToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeDebugTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeDeviceCheckToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeDeviceCheckTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangePlayIntegrityToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangePlayIntegrityTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeRecaptchaEnterpriseToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeRecaptchaEnterpriseTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeRecaptchaToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeRecaptchaTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeRecaptchaV3Token(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeRecaptchaV3TokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def exchangeSafetyNetToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeSafetyNetTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest: ...
            def generateAppAttestChallenge(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeResponseHttpRequest: ...
            def generatePlayIntegrityChallenge(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeResponseHttpRequest: ...
            def appAttestConfig(self) -> AppAttestConfigResource: ...
            def debugTokens(self) -> DebugTokensResource: ...
            def deviceCheckConfig(self) -> DeviceCheckConfigResource: ...
            def playIntegrityConfig(self) -> PlayIntegrityConfigResource: ...
            def recaptchaConfig(self) -> RecaptchaConfigResource: ...
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
                body: GoogleFirebaseAppcheckV1betaBatchUpdateServicesRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaListServicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleFirebaseAppcheckV1betaListServicesResponseHttpRequest,
                previous_response: GoogleFirebaseAppcheckV1betaListServicesResponse,
            ) -> GoogleFirebaseAppcheckV1betaListServicesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleFirebaseAppcheckV1betaService = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaServiceHttpRequest: ...

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
class GoogleFirebaseAppcheckV1betaAppAttestConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaAppAttestConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAppCheckTokenHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaAppCheckToken: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetAppAttestConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetAppAttestConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetPlayIntegrityConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetPlayIntegrityConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaEnterpriseConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaEnterpriseConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaV3ConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaV3ConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetSafetyNetConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetSafetyNetConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDebugTokenHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaDebugToken: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDeviceCheckConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaDeviceCheckConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaExchangeAppAttestAttestationResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaGenerateAppAttestChallengeResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaGeneratePlayIntegrityChallengeResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListDebugTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaListDebugTokensResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaListServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPlayIntegrityConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaPlayIntegrityConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwkSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaPublicJwkSet: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaRecaptchaConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaRecaptchaEnterpriseConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaV3ConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaRecaptchaV3Config: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaSafetyNetConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaSafetyNetConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaService: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
