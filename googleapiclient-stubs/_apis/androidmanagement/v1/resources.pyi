import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AndroidManagementResource(googleapiclient.discovery.Resource):
    class SignupUrlsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, callbackUrl: str = ..., projectId: str = ..., **kwargs: typing.Any
        ) -> SignupUrlHttpRequest: ...
    class EnterprisesResource(googleapiclient.discovery.Resource):
        class WebTokensResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: WebToken = ..., **kwargs: typing.Any
            ) -> WebTokenHttpRequest: ...
        class PoliciesResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                name: str,
                body: Policy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListPoliciesResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> PolicyHttpRequest: ...
        class DevicesResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DeviceHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Device = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> DeviceHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                wipeReasonMessage: str = ...,
                wipeDataFlags: typing.Union[
                    typing_extensions.Literal[
                        "WIPE_DATA_FLAG_UNSPECIFIED",
                        "PRESERVE_RESET_PROTECTION_DATA",
                        "WIPE_EXTERNAL_STORAGE",
                    ],
                    typing.List[
                        typing_extensions.Literal[
                            "WIPE_DATA_FLAG_UNSPECIFIED",
                            "PRESERVE_RESET_PROTECTION_DATA",
                            "WIPE_EXTERNAL_STORAGE",
                        ]
                    ],
                ] = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def issueCommand(
                self, *, name: str, body: Command = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListDevicesResponseHttpRequest: ...
            def operations(self) -> OperationsResource: ...
        class WebAppsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListWebAppsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: WebApp = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> WebAppHttpRequest: ...
            def create(
                self, *, parent: str, body: WebApp = ..., **kwargs: typing.Any
            ) -> WebAppHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> WebAppHttpRequest: ...
        class EnrollmentTokensResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: EnrollmentToken = ..., **kwargs: typing.Any
            ) -> EnrollmentTokenHttpRequest: ...
        class ApplicationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
            ) -> ApplicationHttpRequest: ...
        def create(
            self,
            *,
            body: Enterprise = ...,
            enterpriseToken: str = ...,
            signupUrlName: str = ...,
            projectId: str = ...,
            **kwargs: typing.Any
        ) -> EnterpriseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Enterprise = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> EnterpriseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> EnterpriseHttpRequest: ...
        def webTokens(self) -> WebTokensResource: ...
        def policies(self) -> PoliciesResource: ...
        def devices(self) -> DevicesResource: ...
        def webApps(self) -> WebAppsResource: ...
        def enrollmentTokens(self) -> EnrollmentTokensResource: ...
        def applications(self) -> ApplicationsResource: ...
    def signupUrls(self) -> SignupUrlsResource: ...
    def enterprises(self) -> EnterprisesResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class WebAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebApp: ...

class EnterpriseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Enterprise: ...

class WebTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WebToken: ...

class ListWebAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListWebAppsResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Application: ...

class ListPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPoliciesResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListDevicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDevicesResponse: ...

class EnrollmentTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EnrollmentToken: ...

class SignupUrlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SignupUrl: ...

class DeviceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Device: ...
