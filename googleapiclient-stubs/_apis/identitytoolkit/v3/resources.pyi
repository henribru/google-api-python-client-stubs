import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class IdentityToolkitResource(googleapiclient.discovery.Resource):
    class RelyingpartyResource(googleapiclient.discovery.Resource):
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
        def setProjectConfig(
            self,
            *,
            body: IdentitytoolkitRelyingpartySetProjectConfigRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySetProjectConfigResponseHttpRequest: ...
        def getOobConfirmationCode(
            self, *, body: Relyingparty = ..., **kwargs: typing.Any
        ) -> GetOobConfirmationCodeResponseHttpRequest: ...
        def getRecaptchaParam(
            self, **kwargs: typing.Any
        ) -> GetRecaptchaParamResponseHttpRequest: ...
        def verifyCustomToken(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyCustomTokenRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyCustomTokenResponseHttpRequest: ...
        def getPublicKeys(
            self, **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartyGetPublicKeysResponseHttpRequest: ...
        def verifyAssertion(
            self,
            *,
            body: IdentitytoolkitRelyingpartyVerifyAssertionRequest = ...,
            **kwargs: typing.Any
        ) -> VerifyAssertionResponseHttpRequest: ...
        def emailLinkSignin(
            self,
            *,
            body: IdentitytoolkitRelyingpartyEmailLinkSigninRequest = ...,
            **kwargs: typing.Any
        ) -> EmailLinkSigninResponseHttpRequest: ...
        def uploadAccount(
            self,
            *,
            body: IdentitytoolkitRelyingpartyUploadAccountRequest = ...,
            **kwargs: typing.Any
        ) -> UploadAccountResponseHttpRequest: ...
        def signupNewUser(
            self,
            *,
            body: IdentitytoolkitRelyingpartySignupNewUserRequest = ...,
            **kwargs: typing.Any
        ) -> SignupNewUserResponseHttpRequest: ...
        def createAuthUri(
            self,
            *,
            body: IdentitytoolkitRelyingpartyCreateAuthUriRequest = ...,
            **kwargs: typing.Any
        ) -> CreateAuthUriResponseHttpRequest: ...
        def signOutUser(
            self,
            *,
            body: IdentitytoolkitRelyingpartySignOutUserRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySignOutUserResponseHttpRequest: ...
        def setAccountInfo(
            self,
            *,
            body: IdentitytoolkitRelyingpartySetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> SetAccountInfoResponseHttpRequest: ...
        def sendVerificationCode(
            self,
            *,
            body: IdentitytoolkitRelyingpartySendVerificationCodeRequest = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartySendVerificationCodeResponseHttpRequest: ...
        def getAccountInfo(
            self,
            *,
            body: IdentitytoolkitRelyingpartyGetAccountInfoRequest = ...,
            **kwargs: typing.Any
        ) -> GetAccountInfoResponseHttpRequest: ...
        def resetPassword(
            self,
            *,
            body: IdentitytoolkitRelyingpartyResetPasswordRequest = ...,
            **kwargs: typing.Any
        ) -> ResetPasswordResponseHttpRequest: ...
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
        def getProjectConfig(
            self,
            *,
            projectNumber: str = ...,
            delegatedProjectNumber: str = ...,
            **kwargs: typing.Any
        ) -> IdentitytoolkitRelyingpartyGetProjectConfigResponseHttpRequest: ...
    def relyingparty(self) -> RelyingpartyResource: ...

class ResetPasswordResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResetPasswordResponse: ...

class DeleteAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeleteAccountResponse: ...

class IdentitytoolkitRelyingpartyGetProjectConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartyGetProjectConfigResponse: ...

class IdentitytoolkitRelyingpartySignOutUserResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartySignOutUserResponse: ...

class IdentitytoolkitRelyingpartyVerifyPhoneNumberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartyVerifyPhoneNumberResponse: ...

class DownloadAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DownloadAccountResponse: ...

class GetAccountInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetAccountInfoResponse: ...

class UploadAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UploadAccountResponse: ...

class VerifyPasswordResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VerifyPasswordResponse: ...

class GetOobConfirmationCodeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOobConfirmationCodeResponse: ...

class EmailLinkSigninResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EmailLinkSigninResponse: ...

class VerifyCustomTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VerifyCustomTokenResponse: ...

class IdentitytoolkitRelyingpartyGetPublicKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartyGetPublicKeysResponse: ...

class CreateAuthUriResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateAuthUriResponse: ...

class SetAccountInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SetAccountInfoResponse: ...

class IdentitytoolkitRelyingpartySendVerificationCodeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartySendVerificationCodeResponse: ...

class IdentitytoolkitRelyingpartySetProjectConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IdentitytoolkitRelyingpartySetProjectConfigResponse: ...

class SignupNewUserResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignupNewUserResponse: ...

class GetRecaptchaParamResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetRecaptchaParamResponse: ...

class VerifyAssertionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VerifyAssertionResponse: ...
