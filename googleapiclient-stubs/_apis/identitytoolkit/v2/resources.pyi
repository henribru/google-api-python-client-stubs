import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class IdentityToolkitResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class MfaEnrollmentResource(googleapiclient.discovery.Resource):
            def finalize(
                self,
                *,
                body: GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentResponseHttpRequest
            ): ...
            def start(
                self,
                *,
                body: GoogleCloudIdentitytoolkitV2StartMfaEnrollmentRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitV2StartMfaEnrollmentResponseHttpRequest: ...
            def withdraw(
                self,
                *,
                body: GoogleCloudIdentitytoolkitV2WithdrawMfaRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitV2WithdrawMfaResponseHttpRequest: ...

        @typing.type_check_only
        class MfaSignInResource(googleapiclient.discovery.Resource):
            def finalize(
                self,
                *,
                body: GoogleCloudIdentitytoolkitV2FinalizeMfaSignInRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitV2FinalizeMfaSignInResponseHttpRequest: ...
            def start(
                self,
                *,
                body: GoogleCloudIdentitytoolkitV2StartMfaSignInRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitV2StartMfaSignInResponseHttpRequest: ...

        def revokeToken(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV2RevokeTokenRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudIdentitytoolkitV2RevokeTokenResponseHttpRequest: ...
        def mfaEnrollment(self) -> MfaEnrollmentResource: ...
        def mfaSignIn(self) -> MfaSignInResource: ...

    @typing.type_check_only
    class DefaultSupportedIdpsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> (
            GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponseHttpRequest
        ): ...
        def list_next(
            self,
            previous_request: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponseHttpRequest,
            previous_response: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponse,
        ) -> (
            GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponseHttpRequest
            | None
        ): ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DefaultSupportedIdpConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig = ...,
                idpId: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest
            ): ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest
            ): ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest,
                previous_response: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponse,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest
            ): ...

        @typing.type_check_only
        class IdentityPlatformResource(googleapiclient.discovery.Resource):
            def initializeAuth(
                self,
                *,
                project: str,
                body: GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformResponseHttpRequest: ...

        @typing.type_check_only
        class InboundSamlConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig = ...,
                inboundSamlConfigId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest,
                previous_response: GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponse,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...

        @typing.type_check_only
        class OauthIdpConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig = ...,
                oauthIdpConfigId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest,
                previous_response: GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponse,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...

        @typing.type_check_only
        class TenantsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DefaultSupportedIdpConfigsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig = ...,
                    idpId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest,
                    previous_response: GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponse,
                ) -> (
                    GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest: ...

            @typing.type_check_only
            class InboundSamlConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig = ...,
                    inboundSamlConfigId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest,
                    previous_response: GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponse,
                ) -> (
                    GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest: ...

            @typing.type_check_only
            class OauthIdpConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig = ...,
                    oauthIdpConfigId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest,
                    previous_response: GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponse,
                ) -> (
                    GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudIdentitytoolkitAdminV2Tenant = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2TenantHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitAdminV2TenantHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1GetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2ListTenantsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudIdentitytoolkitAdminV2ListTenantsResponseHttpRequest,
                previous_response: GoogleCloudIdentitytoolkitAdminV2ListTenantsResponse,
            ) -> (
                GoogleCloudIdentitytoolkitAdminV2ListTenantsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudIdentitytoolkitAdminV2Tenant = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudIdentitytoolkitAdminV2TenantHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
            def defaultSupportedIdpConfigs(
                self,
            ) -> DefaultSupportedIdpConfigsResource: ...
            def inboundSamlConfigs(self) -> InboundSamlConfigsResource: ...
            def oauthIdpConfigs(self) -> OauthIdpConfigsResource: ...

        def getConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitAdminV2ConfigHttpRequest: ...
        def updateConfig(
            self,
            *,
            name: str,
            body: GoogleCloudIdentitytoolkitAdminV2Config = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudIdentitytoolkitAdminV2ConfigHttpRequest: ...
        def defaultSupportedIdpConfigs(self) -> DefaultSupportedIdpConfigsResource: ...
        def identityPlatform(self) -> IdentityPlatformResource: ...
        def inboundSamlConfigs(self) -> InboundSamlConfigsResource: ...
        def oauthIdpConfigs(self) -> OauthIdpConfigsResource: ...
        def tenants(self) -> TenantsResource: ...

    @typing.type_check_only
    class V2Resource(googleapiclient.discovery.Resource):
        def getPasswordPolicy(
            self, *, tenantId: str = ..., **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV2PasswordPolicyHttpRequest: ...
        def getRecaptchaConfig(
            self,
            *,
            clientType: typing_extensions.Literal[
                "CLIENT_TYPE_UNSPECIFIED",
                "CLIENT_TYPE_WEB",
                "CLIENT_TYPE_ANDROID",
                "CLIENT_TYPE_IOS",
            ] = ...,
            tenantId: str = ...,
            version: typing_extensions.Literal[
                "RECAPTCHA_VERSION_UNSPECIFIED", "RECAPTCHA_ENTERPRISE"
            ] = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudIdentitytoolkitV2RecaptchaConfigHttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def defaultSupportedIdps(self) -> DefaultSupportedIdpsResource: ...
    def projects(self) -> ProjectsResource: ...
    def v2(self) -> V2Resource: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2Config: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2DefaultSupportedIdpConfig: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2InboundSamlConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2InboundSamlConfig: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2InitializeIdentityPlatformResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpConfigsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2ListDefaultSupportedIdpsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2ListInboundSamlConfigsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2ListOAuthIdpConfigsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2ListTenantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2ListTenantsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2OAuthIdpConfig: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitAdminV2TenantHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitAdminV2Tenant: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2FinalizeMfaSignInResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2FinalizeMfaSignInResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2PasswordPolicyHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2PasswordPolicy: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RecaptchaConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2RecaptchaConfig: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2RevokeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2RevokeTokenResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaEnrollmentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2StartMfaEnrollmentResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2StartMfaSignInResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2StartMfaSignInResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV2WithdrawMfaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIdentitytoolkitV2WithdrawMfaResponse: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
