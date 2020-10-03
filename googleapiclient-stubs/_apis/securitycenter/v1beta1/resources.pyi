import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SecurityCommandCenterResource(googleapiclient.discovery.Resource):
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class AssetsResource(googleapiclient.discovery.Resource):
            def runDiscovery(
                self,
                *,
                parent: str,
                body: RunAssetDiscoveryRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def updateSecurityMarks(
                self,
                *,
                name: str,
                body: GoogleCloudSecuritycenterV1beta1SecurityMarks = ...,
                updateMask: str = ...,
                startTime: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest: ...
            def group(
                self,
                *,
                parent: str,
                body: GroupAssetsRequest = ...,
                **kwargs: typing.Any
            ) -> GroupAssetsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                compareDuration: str = ...,
                pageToken: str = ...,
                fieldMask: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                readTime: str = ...,
                **kwargs: typing.Any
            ) -> ListAssetsResponseHttpRequest: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelOperationRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class SourcesResource(googleapiclient.discovery.Resource):
            class FindingsResource(googleapiclient.discovery.Resource):
                def group(
                    self,
                    *,
                    parent: str,
                    body: GroupFindingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GroupFindingsResponseHttpRequest: ...
                def setState(
                    self,
                    *,
                    name: str,
                    body: SetFindingStateRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def updateSecurityMarks(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1beta1SecurityMarks = ...,
                    startTime: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudSecuritycenterV1beta1Finding = ...,
                    findingId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudSecuritycenterV1beta1Finding = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudSecuritycenterV1beta1FindingHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    filter: str = ...,
                    readTime: str = ...,
                    pageToken: str = ...,
                    fieldMask: str = ...,
                    orderBy: str = ...,
                    **kwargs: typing.Any
                ) -> ListFindingsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSourcesResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SourceHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Source = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SourceHttpRequest: ...
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
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def findings(self) -> FindingsResource: ...
        def getOrganizationSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def updateOrganizationSettings(
            self,
            *,
            name: str,
            body: OrganizationSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OrganizationSettingsHttpRequest: ...
        def assets(self) -> AssetsResource: ...
        def operations(self) -> OperationsResource: ...
        def sources(self) -> SourcesResource: ...
    def organizations(self) -> OrganizationsResource: ...

class GoogleCloudSecuritycenterV1beta1SecurityMarksHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudSecuritycenterV1beta1SecurityMarks: ...

class ListFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFindingsResponse: ...

class GroupFindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GroupFindingsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

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

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssetsResponse: ...

class ListSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSourcesResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class GroupAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GroupAssetsResponse: ...

class GoogleCloudSecuritycenterV1beta1FindingHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudSecuritycenterV1beta1Finding: ...
