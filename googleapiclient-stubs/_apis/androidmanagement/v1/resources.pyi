import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AndroidManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EnterprisesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ApplicationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> ApplicationHttpRequest: ...

        @typing.type_check_only
        class DevicesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            def delete(
                self,
                *,
                name: str,
                wipeDataFlags: typing_extensions.Literal[
                    "WIPE_DATA_FLAG_UNSPECIFIED",
                    "PRESERVE_RESET_PROTECTION_DATA",
                    "WIPE_EXTERNAL_STORAGE",
                    "WIPE_ESIMS",
                ]
                | _list[
                    typing_extensions.Literal[
                        "WIPE_DATA_FLAG_UNSPECIFIED",
                        "PRESERVE_RESET_PROTECTION_DATA",
                        "WIPE_EXTERNAL_STORAGE",
                        "WIPE_ESIMS",
                    ]
                ] = ...,
                wipeReasonMessage: str = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
            def issueCommand(
                self, *, name: str, body: Command = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListDevicesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDevicesResponseHttpRequest,
                previous_response: ListDevicesResponse,
            ) -> ListDevicesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Device = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> DeviceHttpRequest: ...
            def operations(self) -> OperationsResource: ...

        @typing.type_check_only
        class EnrollmentTokensResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: EnrollmentToken = ..., **kwargs: typing.Any
            ) -> EnrollmentTokenHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EnrollmentTokenHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListEnrollmentTokensResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListEnrollmentTokensResponseHttpRequest,
                previous_response: ListEnrollmentTokensResponse,
            ) -> ListEnrollmentTokensResponseHttpRequest | None: ...

        @typing.type_check_only
        class MigrationTokensResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: MigrationToken = ..., **kwargs: typing.Any
            ) -> MigrationTokenHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> MigrationTokenHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListMigrationTokensResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListMigrationTokensResponseHttpRequest,
                previous_response: ListMigrationTokensResponse,
            ) -> ListMigrationTokensResponseHttpRequest | None: ...

        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListPoliciesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPoliciesResponseHttpRequest,
                previous_response: ListPoliciesResponse,
            ) -> ListPoliciesResponseHttpRequest | None: ...
            def modifyPolicyApplications(
                self,
                *,
                name: str,
                body: ModifyPolicyApplicationsRequest = ...,
                **kwargs: typing.Any,
            ) -> ModifyPolicyApplicationsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Policy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> PolicyHttpRequest: ...
            def removePolicyApplications(
                self,
                *,
                name: str,
                body: RemovePolicyApplicationsRequest = ...,
                **kwargs: typing.Any,
            ) -> RemovePolicyApplicationsResponseHttpRequest: ...

        @typing.type_check_only
        class WebAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: WebApp = ..., **kwargs: typing.Any
            ) -> WebAppHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> WebAppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListWebAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListWebAppsResponseHttpRequest,
                previous_response: ListWebAppsResponse,
            ) -> ListWebAppsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: WebApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> WebAppHttpRequest: ...

        @typing.type_check_only
        class WebTokensResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: WebToken = ..., **kwargs: typing.Any
            ) -> WebTokenHttpRequest: ...

        def create(
            self,
            *,
            body: Enterprise = ...,
            agreementAccepted: bool = ...,
            enterpriseToken: str = ...,
            projectId: str = ...,
            signupUrlName: str = ...,
            **kwargs: typing.Any,
        ) -> EnterpriseHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def generateEnterpriseUpgradeUrl(
            self,
            *,
            name: str,
            body: GenerateEnterpriseUpgradeUrlRequest = ...,
            **kwargs: typing.Any,
        ) -> GenerateEnterpriseUpgradeUrlResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> EnterpriseHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            projectId: str = ...,
            view: typing_extensions.Literal[
                "ENTERPRISE_VIEW_UNSPECIFIED", "BASIC"
            ] = ...,
            **kwargs: typing.Any,
        ) -> ListEnterprisesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListEnterprisesResponseHttpRequest,
            previous_response: ListEnterprisesResponse,
        ) -> ListEnterprisesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: Enterprise = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> EnterpriseHttpRequest: ...
        def applications(self) -> ApplicationsResource: ...
        def devices(self) -> DevicesResource: ...
        def enrollmentTokens(self) -> EnrollmentTokensResource: ...
        def migrationTokens(self) -> MigrationTokensResource: ...
        def policies(self) -> PoliciesResource: ...
        def webApps(self) -> WebAppsResource: ...
        def webTokens(self) -> WebTokensResource: ...

    @typing.type_check_only
    class ProvisioningInfoResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProvisioningInfoHttpRequest: ...

    @typing.type_check_only
    class SignupUrlsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            adminEmail: str = ...,
            allowedDomains: str | _list[str] = ...,
            callbackUrl: str = ...,
            projectId: str = ...,
            **kwargs: typing.Any,
        ) -> SignupUrlHttpRequest: ...

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
    def enterprises(self) -> EnterprisesResource: ...
    def provisioningInfo(self) -> ProvisioningInfoResource: ...
    def signupUrls(self) -> SignupUrlsResource: ...

@typing.type_check_only
class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Application: ...

@typing.type_check_only
class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Device: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EnrollmentTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EnrollmentToken: ...

@typing.type_check_only
class EnterpriseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Enterprise: ...

@typing.type_check_only
class GenerateEnterpriseUpgradeUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateEnterpriseUpgradeUrlResponse: ...

@typing.type_check_only
class ListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDevicesResponse: ...

@typing.type_check_only
class ListEnrollmentTokensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEnrollmentTokensResponse: ...

@typing.type_check_only
class ListEnterprisesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEnterprisesResponse: ...

@typing.type_check_only
class ListMigrationTokensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMigrationTokensResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPoliciesResponse: ...

@typing.type_check_only
class ListWebAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWebAppsResponse: ...

@typing.type_check_only
class MigrationTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MigrationToken: ...

@typing.type_check_only
class ModifyPolicyApplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ModifyPolicyApplicationsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ProvisioningInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProvisioningInfo: ...

@typing.type_check_only
class RemovePolicyApplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemovePolicyApplicationsResponse: ...

@typing.type_check_only
class SignupUrlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SignupUrl: ...

@typing.type_check_only
class WebAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WebApp: ...

@typing.type_check_only
class WebTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WebToken: ...
