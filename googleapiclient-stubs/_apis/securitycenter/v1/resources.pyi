import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class NotificationConfigsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: NotificationConfig = ...,
                configId: str = ...,
                **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: NotificationConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NotificationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListNotificationConfigsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class SourcesResource(googleapiclient.discovery.Resource):
            class FindingsResource(googleapiclient.discovery.Resource):
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Finding = ...,
                    findingId: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> SecurityMarksHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    fieldMask: str = ...,
                    readTime: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    compareDuration: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> FindingHttpRequest: ...
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SourceHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def create(
                self, *, parent: str, body: Source = ..., **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Source = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        class AssetsResource(googleapiclient.discovery.Resource):
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: SecurityMarks = ...,
                startTime: str = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SecurityMarksHttpRequest: ...
            def runDiscovery(
                self,
                *,
                parent: str,
                body: RunAssetDiscoveryRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                fieldMask: str = ...,
                compareDuration: str = ...,
                readTime: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                orderBy: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
        def updateOrganizationSettings(
            self,
            *,
            name: str,
            body: OrganizationSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def getOrganizationSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def operations(self) -> OperationsResource: ...
        def notificationConfigs(self) -> NotificationConfigsResource: ...
        def sources(self) -> SourcesResource: ...
        def assets(self) -> AssetsResource: ...
    def organizations(self) -> OrganizationsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class NotificationConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NotificationConfig: ...

class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssetsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class GroupAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GroupAssetsResponse: ...

class SecurityMarksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityMarks: ...

class GroupFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GroupFindingsResponse: ...

class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFindingsResponse: ...

class OrganizationSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrganizationSettings: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class SourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Source: ...

class FindingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Finding: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ListNotificationConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNotificationConfigsResponse: ...

class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSourcesResponse: ...
