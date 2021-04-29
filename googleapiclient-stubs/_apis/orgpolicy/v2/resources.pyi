import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class OrgPolicyAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConstraintsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest: ...
        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def getEffectivePolicy(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
        def constraints(self) -> ConstraintsResource: ...
        def policies(self) -> PoliciesResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConstraintsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest: ...
        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def getEffectivePolicy(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
        def constraints(self) -> ConstraintsResource: ...
        def policies(self) -> PoliciesResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConstraintsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest: ...
        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def getEffectivePolicy(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...
        def constraints(self) -> ConstraintsResource: ...
        def policies(self) -> PoliciesResource: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2ListConstraintsResponse: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2ListPoliciesResponse: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2Policy: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
