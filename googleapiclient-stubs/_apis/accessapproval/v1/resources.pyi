import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AccessApprovalResource(googleapiclient.discovery.Resource):
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListApprovalRequestsResponseHttpRequest: ...
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
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
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListApprovalRequestsResponseHttpRequest: ...
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
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
        def deleteAccessApprovalSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def approvalRequests(self) -> ApprovalRequestsResource: ...
    class FoldersResource(googleapiclient.discovery.Resource):
        class ApprovalRequestsResource(googleapiclient.discovery.Resource):
            def dismiss(
                self,
                *,
                name: str,
                body: DismissApprovalRequestMessage = ...,
                **kwargs: typing.Any
            ) -> ApprovalRequestHttpRequest: ...
            def approve(
                self,
                *,
                name: str,
                body: ApproveApprovalRequestMessage = ...,
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
                pageToken: str = ...,
                pageSize: int = ...,
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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def folders(self) -> FoldersResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ApprovalRequestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ApprovalRequest: ...

class ListApprovalRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListApprovalRequestsResponse: ...

class AccessApprovalSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccessApprovalSettings: ...
