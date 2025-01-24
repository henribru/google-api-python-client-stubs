import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AutofeedSettingsResource(googleapiclient.discovery.Resource):
            def getAutofeedSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> AutofeedSettingsHttpRequest: ...
            def updateAutofeedSettings(
                self,
                *,
                name: str,
                body: AutofeedSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> AutofeedSettingsHttpRequest: ...

        @typing.type_check_only
        class BusinessIdentityResource(googleapiclient.discovery.Resource):
            def getBusinessIdentity(
                self, *, name: str, **kwargs: typing.Any
            ) -> BusinessIdentityHttpRequest: ...
            def updateBusinessIdentity(
                self,
                *,
                name: str,
                body: BusinessIdentity = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> BusinessIdentityHttpRequest: ...

        @typing.type_check_only
        class BusinessInfoResource(googleapiclient.discovery.Resource):
            def getBusinessInfo(
                self, *, name: str, **kwargs: typing.Any
            ) -> BusinessInfoHttpRequest: ...
            def updateBusinessInfo(
                self,
                *,
                name: str,
                body: BusinessInfo = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> BusinessInfoHttpRequest: ...

        @typing.type_check_only
        class EmailPreferencesResource(googleapiclient.discovery.Resource):
            def getEmailPreferences(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmailPreferencesHttpRequest: ...
            def updateEmailPreferences(
                self,
                *,
                name: str,
                body: EmailPreferences = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> EmailPreferencesHttpRequest: ...

        @typing.type_check_only
        class HomepageResource(googleapiclient.discovery.Resource):
            def claim(
                self,
                *,
                name: str,
                body: ClaimHomepageRequest = ...,
                **kwargs: typing.Any,
            ) -> HomepageHttpRequest: ...
            def getHomepage(
                self, *, name: str, **kwargs: typing.Any
            ) -> HomepageHttpRequest: ...
            def unclaim(
                self,
                *,
                name: str,
                body: UnclaimHomepageRequest = ...,
                **kwargs: typing.Any,
            ) -> HomepageHttpRequest: ...
            def updateHomepage(
                self,
                *,
                name: str,
                body: Homepage = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> HomepageHttpRequest: ...

        @typing.type_check_only
        class IssuesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                timeZone: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccountIssuesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountIssuesResponseHttpRequest,
                previous_response: ListAccountIssuesResponse,
            ) -> ListAccountIssuesResponseHttpRequest | None: ...

        @typing.type_check_only
        class OnlineReturnPoliciesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OnlineReturnPolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListOnlineReturnPoliciesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOnlineReturnPoliciesResponseHttpRequest,
                previous_response: ListOnlineReturnPoliciesResponse,
            ) -> ListOnlineReturnPoliciesResponseHttpRequest | None: ...

        @typing.type_check_only
        class ProgramsResource(googleapiclient.discovery.Resource):
            def disable(
                self,
                *,
                name: str,
                body: DisableProgramRequest = ...,
                **kwargs: typing.Any,
            ) -> ProgramHttpRequest: ...
            def enable(
                self,
                *,
                name: str,
                body: EnableProgramRequest = ...,
                **kwargs: typing.Any,
            ) -> ProgramHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ProgramHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListProgramsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProgramsResponseHttpRequest,
                previous_response: ListProgramsResponse,
            ) -> ListProgramsResponseHttpRequest | None: ...

        @typing.type_check_only
        class RegionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Region = ...,
                regionId: str = ...,
                **kwargs: typing.Any,
            ) -> RegionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RegionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListRegionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRegionsResponseHttpRequest,
                previous_response: ListRegionsResponse,
            ) -> ListRegionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Region = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> RegionHttpRequest: ...

        @typing.type_check_only
        class ShippingSettingsResource(googleapiclient.discovery.Resource):
            def getShippingSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> ShippingSettingsHttpRequest: ...
            def insert(
                self, *, parent: str, body: ShippingSettings = ..., **kwargs: typing.Any
            ) -> ShippingSettingsHttpRequest: ...

        @typing.type_check_only
        class TermsOfServiceAgreementStatesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TermsOfServiceAgreementStateHttpRequest: ...
            def retrieveForApplication(
                self, *, parent: str, **kwargs: typing.Any
            ) -> TermsOfServiceAgreementStateHttpRequest: ...

        @typing.type_check_only
        class UsersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: User = ...,
                userId: str = ...,
                **kwargs: typing.Any,
            ) -> UserHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> UserHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListUsersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUsersResponseHttpRequest,
                previous_response: ListUsersResponse,
            ) -> ListUsersResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: User = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> UserHttpRequest: ...

        def createAndConfigure(
            self, *, body: CreateAndConfigureAccountRequest = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def delete(
            self, *, name: str, force: bool = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAccountsResponseHttpRequest,
            previous_response: ListAccountsResponse,
        ) -> ListAccountsResponseHttpRequest | None: ...
        def listSubaccounts(
            self,
            *,
            provider: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListSubAccountsResponseHttpRequest: ...
        def listSubaccounts_next(
            self,
            previous_request: ListSubAccountsResponseHttpRequest,
            previous_response: ListSubAccountsResponse,
        ) -> ListSubAccountsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Account = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> AccountHttpRequest: ...
        def autofeedSettings(self) -> AutofeedSettingsResource: ...
        def businessIdentity(self) -> BusinessIdentityResource: ...
        def businessInfo(self) -> BusinessInfoResource: ...
        def emailPreferences(self) -> EmailPreferencesResource: ...
        def homepage(self) -> HomepageResource: ...
        def issues(self) -> IssuesResource: ...
        def onlineReturnPolicies(self) -> OnlineReturnPoliciesResource: ...
        def programs(self) -> ProgramsResource: ...
        def regions(self) -> RegionsResource: ...
        def shippingSettings(self) -> ShippingSettingsResource: ...
        def termsOfServiceAgreementStates(
            self,
        ) -> TermsOfServiceAgreementStatesResource: ...
        def users(self) -> UsersResource: ...

    @typing.type_check_only
    class TermsOfServiceResource(googleapiclient.discovery.Resource):
        def accept(
            self,
            *,
            name: str,
            account: str = ...,
            regionCode: str = ...,
            **kwargs: typing.Any,
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> TermsOfServiceHttpRequest: ...
        def retrieveLatest(
            self,
            *,
            kind: typing_extensions.Literal[
                "TERMS_OF_SERVICE_KIND_UNSPECIFIED", "MERCHANT_CENTER"
            ] = ...,
            regionCode: str = ...,
            **kwargs: typing.Any,
        ) -> TermsOfServiceHttpRequest: ...

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
    def termsOfService(self) -> TermsOfServiceResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Account: ...

@typing.type_check_only
class AutofeedSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutofeedSettings: ...

@typing.type_check_only
class BusinessIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BusinessIdentity: ...

@typing.type_check_only
class BusinessInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BusinessInfo: ...

@typing.type_check_only
class EmailPreferencesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EmailPreferences: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class HomepageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Homepage: ...

@typing.type_check_only
class ListAccountIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountIssuesResponse: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListOnlineReturnPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOnlineReturnPoliciesResponse: ...

@typing.type_check_only
class ListProgramsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProgramsResponse: ...

@typing.type_check_only
class ListRegionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRegionsResponse: ...

@typing.type_check_only
class ListSubAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSubAccountsResponse: ...

@typing.type_check_only
class ListUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUsersResponse: ...

@typing.type_check_only
class OnlineReturnPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OnlineReturnPolicy: ...

@typing.type_check_only
class ProgramHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Program: ...

@typing.type_check_only
class RegionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Region: ...

@typing.type_check_only
class ShippingSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ShippingSettings: ...

@typing.type_check_only
class TermsOfServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TermsOfService: ...

@typing.type_check_only
class TermsOfServiceAgreementStateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TermsOfServiceAgreementState: ...

@typing.type_check_only
class UserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> User: ...
