import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class AccessApprovalResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListApprovalRequestsResponseHttpRequest: ...
        def deleteAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def updateAccessApprovalSettings(
            self,
            *,
            name: str,
            body: AccessApprovalSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def approvalRequests(self) -> ApprovalRequestsResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListApprovalRequestsResponseHttpRequest: ...
        def deleteAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def updateAccessApprovalSettings(
            self,
            *,
            name: str,
            body: AccessApprovalSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def approvalRequests(self) -> ApprovalRequestsResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListApprovalRequestsResponseHttpRequest: ...
        def deleteAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def updateAccessApprovalSettings(
            self,
            *,
            name: str,
            body: AccessApprovalSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> AccessApprovalSettingsHttpRequest: ...
        def approvalRequests(self) -> ApprovalRequestsResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AccessApprovalSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AccessApprovalSettings: ...

@typing.type_check_only
class ApprovalRequestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ApprovalRequest: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListApprovalRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListApprovalRequestsResponse: ...
