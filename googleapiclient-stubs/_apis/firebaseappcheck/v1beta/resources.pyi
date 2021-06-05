import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
                    names: typing.Union[str, typing.List[str]] = ...,
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
            class RecaptchaConfigResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: typing.Union[str, typing.List[str]] = ...,
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
            def exchangeCustomToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeCustomTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest: ...
            def exchangeDebugToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeDebugTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest: ...
            def exchangeDeviceCheckToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeDeviceCheckTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest: ...
            def exchangeRecaptchaToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeRecaptchaTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest: ...
            def exchangeSafetyNetToken(
                self,
                *,
                app: str,
                body: GoogleFirebaseAppcheckV1betaExchangeSafetyNetTokenRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest: ...
            def debugTokens(self) -> DebugTokensResource: ...
            def deviceCheckConfig(self) -> DeviceCheckConfigResource: ...
            def recaptchaConfig(self) -> RecaptchaConfigResource: ...
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
    def jwks(self) -> JwksResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaAttestationTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaAttestationTokenResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetDeviceCheckConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchGetRecaptchaConfigsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaBatchUpdateServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDebugTokenHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaDebugToken: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaDeviceCheckConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaDeviceCheckConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListDebugTokensResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaListDebugTokensResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaListServicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaListServicesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaPublicJwkSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaPublicJwkSet: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaRecaptchaConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaRecaptchaConfig: ...

@typing.type_check_only
class GoogleFirebaseAppcheckV1betaServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseAppcheckV1betaService: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
