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
    class RelyingpartyResource(googleapiclient.discovery.Resource):
        def createAuthUri(
            self,
            *,
            body: IdentitytoolkitRelyingpartyCreateAuthUriRequest = ...,
            **kwargs: typing.Any
        ) -> CreateAuthUriResponseHttpRequest: ...
        def deleteAccount(
            self,
            *,
            body: IdentitytoolkitRelyingpartyDeleteAccountRequest = ...,
            **kwargs: typing.Any
        ) -> DeleteAccountResponseHttpRequest: ...
        def downloadAccount(
            self,
            *,
            body: IdentitytoolkitRelyingpartyDownloadAccountRequest = ...,
            **kwargs: typing.Any
        ) -> DownloadAccountResponseHttpRequest: ...
        def downloadAccount_next(
            self,
            previous_request: DownloadAccountResponseHttpRequest,
            previous_response: DownloadAccountResponse,
        ) -> DownloadAccountResponseHttpRequest | None: ...
        def emailLinkSignin(
            self,
            *,
            body: IdentitytoolkitRelyingpartyEmailLinkSigninRequest = ...,
            **kwargs: typing.Any
        ) -> EmailLinkSigninResponseHttpRequest: ...
        def getAccountInfo(
            self,
            *,
            body: IdentitytoolkitRelyingpartyGetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> GetAccountInfoResponseHttpRequest: ...
        def getOobConfirmationCode(
            self, *, body: Relyingparty = ..., **kwargs: typing.Any
        ) -> GetOobConfirmationCodeResponseHttpRequest: ...
        def getProjectConfig(
            self,
            *,
            delegatedProjectNumber: str = ...,
            projectNumber: str = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartyGetProjectConfigResponseHttpRequest: ...
        def getPublicKeys(
            self, **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartyGetPublicKeysResponseHttpRequest: ...
        def getRecaptchaParam(
            self, **kwargs: typing.Any
        ) -> GetRecaptchaParamResponseHttpRequest: ...
        def resetPassword(
            self,
            *,
            body: IdentitytoolkitRelyingpartyResetPasswordRequest = ...,
            **kwargs: typing.Any
        ) -> ResetPasswordResponseHttpRequest: ...
        def sendVerificationCode(
            self,
            *,
            body: IdentitytoolkitRelyingpartySendVerificationCodeRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySendVerificationCodeResponseHttpRequest: ...
        def setAccountInfo(
            self,
            *,
            body: IdentitytoolkitRelyingpartySetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> SetAccountInfoResponseHttpRequest: ...
        def setProjectConfig(
            self,
            *,
            body: IdentitytoolkitRelyingpartySetProjectConfigRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySetProjectConfigResponseHttpRequest: ...
        def signOutUser(
            self,
            *,
            body: IdentitytoolkitRelyingpartySignOutUserRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySignOutUserResponseHttpRequest: ...
        def signupNewUser(
            self,
            *,
            body: IdentitytoolkitRelyingpartySignupNewUserRequest = ...,
            **kwargs: typing.Any
        ) -> SignupNewUserResponseHttpRequest: ...
        def uploadAccount(
            self,
            *,
            body: IdentitytoolkitRelyingpartyUploadAccountRequest = ...,
            **kwargs: typing.Any
        ) -> UploadAccountResponseHttpRequest: ...
        def verifyAssertion(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyAssertionRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyAssertionResponseHttpRequest: ...
        def verifyCustomToken(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyCustomTokenRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyCustomTokenResponseHttpRequest: ...
        def verifyPassword(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyPasswordRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyPasswordResponseHttpRequest: ...
        def verifyPhoneNumber(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyPhoneNumberRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseHttpRequest: ...

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
    def relyingparty(self) -> RelyingpartyResource: ...

@typing.type_check_only
class CreateAuthUriResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreateAuthUriResponse: ...

@typing.type_check_only
class DeleteAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeleteAccountResponse: ...

@typing.type_check_only
class DownloadAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DownloadAccountResponse: ...

@typing.type_check_only
class EmailLinkSigninResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EmailLinkSigninResponse: ...

@typing.type_check_only
class GetAccountInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetAccountInfoResponse: ...

@typing.type_check_only
class GetOobConfirmationCodeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOobConfirmationCodeResponse: ...

@typing.type_check_only
class GetRecaptchaParamResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetRecaptchaParamResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartyGetProjectConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartyGetProjectConfigResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartyGetPublicKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartyGetPublicKeysResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartySendVerificationCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartySendVerificationCodeResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartySetProjectConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartySetProjectConfigResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartySignOutUserResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartySignOutUserResponse: ...

@typing.type_check_only
class IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse: ...

@typing.type_check_only
class ResetPasswordResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResetPasswordResponse: ...

@typing.type_check_only
class SetAccountInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SetAccountInfoResponse: ...

@typing.type_check_only
class SignupNewUserResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SignupNewUserResponse: ...

@typing.type_check_only
class UploadAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UploadAccountResponse: ...

@typing.type_check_only
class VerifyAssertionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VerifyAssertionResponse: ...

@typing.type_check_only
class VerifyCustomTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VerifyCustomTokenResponse: ...

@typing.type_check_only
class VerifyPasswordResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VerifyPasswordResponse: ...
