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
        class AutomaticImprovementsResource(googleapiclient.discovery.Resource):
            def getAutomaticImprovements(
                self, *, name: str, **kwargs: typing.Any
            ) -> AutomaticImprovementsHttpRequest: ...
            def updateAutomaticImprovements(
                self,
                *,
                name: str,
                body: AutomaticImprovements = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> AutomaticImprovementsHttpRequest: ...

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
        class DeveloperRegistrationResource(googleapiclient.discovery.Resource):
            def registerGcp(
                self, *, name: str, body: RegisterGCPRequest = ..., **kwargs: typing.Any
            ) -> DeveloperRegistrationHttpRequest: ...
            def unregisterGcp(
                self,
                *,
                name: str,
                body: UnregisterGCPRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...

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
        class GbpAccountsResource(googleapiclient.discovery.Resource):
            def linkGbpAccount(
                self,
                *,
                parent: str,
                body: LinkGbpAccountRequest = ...,
                **kwargs: typing.Any,
            ) -> LinkGbpAccountResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListGbpAccountsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListGbpAccountsResponseHttpRequest,
                previous_response: ListGbpAccountsResponse,
            ) -> ListGbpAccountsResponseHttpRequest | None: ...

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
        class OmnichannelSettingsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LfpProvidersResource(googleapiclient.discovery.Resource):
                def find(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> FindLfpProvidersResponseHttpRequest: ...
                def find_next(
                    self,
                    previous_request: FindLfpProvidersResponseHttpRequest,
                    previous_response: FindLfpProvidersResponse,
                ) -> FindLfpProvidersResponseHttpRequest | None: ...
                def linkLfpProvider(
                    self,
                    *,
                    name: str,
                    body: LinkLfpProviderRequest = ...,
                    **kwargs: typing.Any,
                ) -> LinkLfpProviderResponseHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: OmnichannelSetting = ...,
                **kwargs: typing.Any,
            ) -> OmnichannelSettingHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OmnichannelSettingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListOmnichannelSettingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOmnichannelSettingsResponseHttpRequest,
                previous_response: ListOmnichannelSettingsResponse,
            ) -> ListOmnichannelSettingsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: OmnichannelSetting = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OmnichannelSettingHttpRequest: ...
            def requestInventoryVerification(
                self,
                *,
                name: str,
                body: RequestInventoryVerificationRequest = ...,
                **kwargs: typing.Any,
            ) -> RequestInventoryVerificationResponseHttpRequest: ...
            def lfpProviders(self) -> LfpProvidersResource: ...

        @typing.type_check_only
        class OnlineReturnPoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: OnlineReturnPolicy = ...,
                **kwargs: typing.Any,
            ) -> OnlineReturnPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
            def patch(
                self,
                *,
                name: str,
                body: OnlineReturnPolicy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OnlineReturnPolicyHttpRequest: ...

        @typing.type_check_only
        class ProgramsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CheckoutSettingsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CheckoutSettings = ...,
                    **kwargs: typing.Any,
                ) -> CheckoutSettingsHttpRequest: ...
                def deleteCheckoutSettings(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def getCheckoutSettings(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CheckoutSettingsHttpRequest: ...
                def updateCheckoutSettings(
                    self,
                    *,
                    name: str,
                    body: CheckoutSettings = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> CheckoutSettingsHttpRequest: ...

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
            def checkoutSettings(self) -> CheckoutSettingsResource: ...

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
        class RelationshipsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AccountRelationshipHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccountRelationshipsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountRelationshipsResponseHttpRequest,
                previous_response: ListAccountRelationshipsResponse,
            ) -> ListAccountRelationshipsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: AccountRelationship = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> AccountRelationshipHttpRequest: ...

        @typing.type_check_only
        class ServicesResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveAccountServiceRequest = ...,
                **kwargs: typing.Any,
            ) -> AccountServiceHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AccountServiceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAccountServicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAccountServicesResponseHttpRequest,
                previous_response: ListAccountServicesResponse,
            ) -> ListAccountServicesResponseHttpRequest | None: ...
            def propose(
                self,
                *,
                parent: str,
                body: ProposeAccountServiceRequest = ...,
                **kwargs: typing.Any,
            ) -> AccountServiceHttpRequest: ...
            def reject(
                self,
                *,
                name: str,
                body: RejectAccountServiceRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...

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
        def getDeveloperRegistration(
            self, *, name: str, **kwargs: typing.Any
        ) -> DeveloperRegistrationHttpRequest: ...
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
        def automaticImprovements(self) -> AutomaticImprovementsResource: ...
        def businessIdentity(self) -> BusinessIdentityResource: ...
        def businessInfo(self) -> BusinessInfoResource: ...
        def developerRegistration(self) -> DeveloperRegistrationResource: ...
        def emailPreferences(self) -> EmailPreferencesResource: ...
        def gbpAccounts(self) -> GbpAccountsResource: ...
        def homepage(self) -> HomepageResource: ...
        def issues(self) -> IssuesResource: ...
        def omnichannelSettings(self) -> OmnichannelSettingsResource: ...
        def onlineReturnPolicies(self) -> OnlineReturnPoliciesResource: ...
        def programs(self) -> ProgramsResource: ...
        def regions(self) -> RegionsResource: ...
        def relationships(self) -> RelationshipsResource: ...
        def services(self) -> ServicesResource: ...
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
        ) -> AcceptTermsOfServiceResponseHttpRequest: ...
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
class AcceptTermsOfServiceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AcceptTermsOfServiceResponse: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Account: ...

@typing.type_check_only
class AccountRelationshipHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountRelationship: ...

@typing.type_check_only
class AccountServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccountService: ...

@typing.type_check_only
class AutofeedSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutofeedSettings: ...

@typing.type_check_only
class AutomaticImprovementsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AutomaticImprovements: ...

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
class CheckoutSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckoutSettings: ...

@typing.type_check_only
class DeveloperRegistrationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeveloperRegistration: ...

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
class FindLfpProvidersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FindLfpProvidersResponse: ...

@typing.type_check_only
class HomepageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Homepage: ...

@typing.type_check_only
class LinkGbpAccountResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LinkGbpAccountResponse: ...

@typing.type_check_only
class LinkLfpProviderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LinkLfpProviderResponse: ...

@typing.type_check_only
class ListAccountIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountIssuesResponse: ...

@typing.type_check_only
class ListAccountRelationshipsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountRelationshipsResponse: ...

@typing.type_check_only
class ListAccountServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountServicesResponse: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListGbpAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListGbpAccountsResponse: ...

@typing.type_check_only
class ListOmnichannelSettingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOmnichannelSettingsResponse: ...

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
class OmnichannelSettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OmnichannelSetting: ...

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
class RequestInventoryVerificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RequestInventoryVerificationResponse: ...

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
