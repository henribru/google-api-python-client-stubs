import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class IdentityToolkitResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def createAuthUri(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1CreateAuthUriRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1CreateAuthUriResponseHttpRequest: ...
        def delete(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1DeleteAccountRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1DeleteAccountResponseHttpRequest: ...
        def issueSamlResponse(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1IssueSamlResponseRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1IssueSamlResponseResponseHttpRequest: ...
        def lookup(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1GetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1GetAccountInfoResponseHttpRequest: ...
        def resetPassword(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1ResetPasswordRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1ResetPasswordResponseHttpRequest: ...
        def sendOobCode(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1GetOobCodeRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1GetOobCodeResponseHttpRequest: ...
        def sendVerificationCode(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SendVerificationCodeRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SendVerificationCodeResponseHttpRequest: ...
        def signInWithCustomToken(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithCustomTokenRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithCustomTokenResponseHttpRequest: ...
        def signInWithEmailLink(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithEmailLinkRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithEmailLinkResponseHttpRequest: ...
        def signInWithGameCenter(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithGameCenterRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithGameCenterResponseHttpRequest: ...
        def signInWithIdp(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithIdpRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithIdpResponseHttpRequest: ...
        def signInWithPassword(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithPasswordRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithPasswordResponseHttpRequest: ...
        def signInWithPhoneNumber(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberResponseHttpRequest: ...
        def signUp(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SignUpRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SignUpResponseHttpRequest: ...
        def update(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1SetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1SetAccountInfoResponseHttpRequest: ...
        def verifyIosClient(
            self,
            *,
            body: GoogleCloudIdentitytoolkitV1VerifyIosClientRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1VerifyIosClientResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccountsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1UploadAccountRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1UploadAccountResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1BatchDeleteAccountsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1BatchDeleteAccountsResponseHttpRequest: ...
            def batchGet(
                self,
                *,
                targetProjectId: str,
                delegatedProjectNumber: str = ...,
                maxResults: int = ...,
                nextPageToken: str = ...,
                tenantId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest: ...
            def batchGet_next(
                self,
                previous_request: GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest,
                previous_response: GoogleCloudIdentitytoolkitV1DownloadAccountResponse,
            ) -> GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest | None: ...
            def delete(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1DeleteAccountRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1DeleteAccountResponseHttpRequest: ...
            def lookup(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1GetAccountInfoRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1GetAccountInfoResponseHttpRequest: ...
            def query(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1QueryUserInfoRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1QueryUserInfoResponseHttpRequest: ...
            def sendOobCode(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1GetOobCodeRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1GetOobCodeResponseHttpRequest: ...
            def update(
                self,
                *,
                targetProjectId: str,
                body: GoogleCloudIdentitytoolkitV1SetAccountInfoRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1SetAccountInfoResponseHttpRequest: ...

        @typing.type_check_only
        class TenantsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AccountsResource(googleapiclient.discovery.Resource):
                def batchCreate(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1UploadAccountRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1UploadAccountResponseHttpRequest: ...
                def batchDelete(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1BatchDeleteAccountsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1BatchDeleteAccountsResponseHttpRequest: ...
                def batchGet(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    delegatedProjectNumber: str = ...,
                    maxResults: int = ...,
                    nextPageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest: ...
                def batchGet_next(
                    self,
                    previous_request: GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest,
                    previous_response: GoogleCloudIdentitytoolkitV1DownloadAccountResponse,
                ) -> GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest | None: ...
                def delete(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1DeleteAccountRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1DeleteAccountResponseHttpRequest: ...
                def lookup(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1GetAccountInfoRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1GetAccountInfoResponseHttpRequest: ...
                def query(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1QueryUserInfoRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1QueryUserInfoResponseHttpRequest: ...
                def sendOobCode(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1GetOobCodeRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1GetOobCodeResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    targetProjectId: str,
                    tenantId: str,
                    body: GoogleCloudIdentitytoolkitV1SetAccountInfoRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudIdentitytoolkitV1SetAccountInfoResponseHttpRequest: ...

            def createSessionCookie(
                self,
                *,
                targetProjectId: str,
                tenantId: str,
                body: GoogleCloudIdentitytoolkitV1CreateSessionCookieRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudIdentitytoolkitV1CreateSessionCookieResponseHttpRequest: ...
            def accounts(self) -> AccountsResource: ...

        def createSessionCookie(
            self,
            *,
            targetProjectId: str,
            body: GoogleCloudIdentitytoolkitV1CreateSessionCookieRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1CreateSessionCookieResponseHttpRequest: ...
        def queryAccounts(
            self,
            *,
            targetProjectId: str,
            body: GoogleCloudIdentitytoolkitV1QueryUserInfoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1QueryUserInfoResponseHttpRequest: ...
        def accounts(self) -> AccountsResource: ...
        def tenants(self) -> TenantsResource: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def getProjects(
            self,
            *,
            androidPackageName: str = ...,
            clientId: str = ...,
            delegatedProjectNumber: str = ...,
            firebaseAppId: str = ...,
            iosBundleId: str = ...,
            projectNumber: str = ...,
            returnDynamicLink: bool = ...,
            sha1Cert: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1GetProjectConfigResponseHttpRequest: ...
        def getPublicKeys(
            self, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def getRecaptchaParams(
            self, **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1GetRecaptchaParamResponseHttpRequest: ...
        def getSessionCookiePublicKeys(
            self, **kwargs: typing.Any
        ) -> GoogleCloudIdentitytoolkitV1GetSessionCookiePublicKeysResponseHttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def projects(self) -> ProjectsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1BatchDeleteAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1BatchDeleteAccountsResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateAuthUriResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1CreateAuthUriResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1CreateSessionCookieResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1CreateSessionCookieResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1DeleteAccountResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1DeleteAccountResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1DownloadAccountResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1DownloadAccountResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetAccountInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1GetAccountInfoResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetOobCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1GetOobCodeResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetProjectConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1GetProjectConfigResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetRecaptchaParamResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1GetRecaptchaParamResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1GetSessionCookiePublicKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1GetSessionCookiePublicKeysResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1IssueSamlResponseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1IssueSamlResponseResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1QueryUserInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1QueryUserInfoResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1ResetPasswordResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1ResetPasswordResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SendVerificationCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SendVerificationCodeResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SetAccountInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SetAccountInfoResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithCustomTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithCustomTokenResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithEmailLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithEmailLinkResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithGameCenterResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithGameCenterResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithIdpResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithIdpResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPasswordResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithPasswordResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignInWithPhoneNumberResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1SignUpResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1SignUpResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1UploadAccountResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1UploadAccountResponse: ...

@typing.type_check_only
class GoogleCloudIdentitytoolkitV1VerifyIosClientResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudIdentitytoolkitV1VerifyIosClientResponse: ...
