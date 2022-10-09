import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListConstraintsResponse,
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest | None: ...

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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListPoliciesResponse,
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest | None: ...
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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListConstraintsResponse,
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest | None: ...

        @typing.type_check_only
        class CustomConstraintsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudOrgpolicyV2CustomConstraint = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2CustomConstraintHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2CustomConstraintHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2ListCustomConstraintsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListCustomConstraintsResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListCustomConstraintsResponse,
            ) -> GoogleCloudOrgpolicyV2ListCustomConstraintsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2CustomConstraint = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2CustomConstraintHttpRequest: ...

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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListPoliciesResponse,
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...

        def constraints(self) -> ConstraintsResource: ...
        def customConstraints(self) -> CustomConstraintsResource: ...
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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListConstraintsResponse,
            ) -> GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest | None: ...

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
            def list_next(
                self,
                previous_request: GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest,
                previous_response: GoogleCloudOrgpolicyV2ListPoliciesResponse,
            ) -> GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudOrgpolicyV2Policy = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudOrgpolicyV2PolicyHttpRequest: ...

        def constraints(self) -> ConstraintsResource: ...
        def policies(self) -> PoliciesResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2CustomConstraintHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2CustomConstraint: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListConstraintsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2ListConstraintsResponse: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListCustomConstraintsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2ListCustomConstraintsResponse: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2ListPoliciesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2ListPoliciesResponse: ...

@typing.type_check_only
class GoogleCloudOrgpolicyV2PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudOrgpolicyV2Policy: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
