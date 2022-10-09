import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ChromePolicyResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GroupsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1BatchDeleteGroupPoliciesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchModify(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1BatchModifyGroupPoliciesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def listGroupPriorityOrdering(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1ListGroupPriorityOrderingRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromePolicyV1ListGroupPriorityOrderingResponseHttpRequest: ...
                def updateGroupPriorityOrdering(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1UpdateGroupPriorityOrderingRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...

            @typing.type_check_only
            class NetworksResource(googleapiclient.discovery.Resource):
                def defineCertificate(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1DefineCertificateRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromePolicyV1DefineCertificateResponseHttpRequest: ...
                def defineNetwork(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1DefineNetworkRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromePolicyV1DefineNetworkResponseHttpRequest: ...
                def removeCertificate(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1RemoveCertificateRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromePolicyV1RemoveCertificateResponseHttpRequest: ...
                def removeNetwork(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1RemoveNetworkRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleChromePolicyV1RemoveNetworkResponseHttpRequest: ...

            @typing.type_check_only
            class OrgunitsResource(googleapiclient.discovery.Resource):
                def batchInherit(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1BatchInheritOrgUnitPoliciesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def batchModify(
                    self,
                    *,
                    customer: str,
                    body: GoogleChromePolicyV1BatchModifyOrgUnitPoliciesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...

            def resolve(
                self,
                *,
                customer: str,
                body: GoogleChromePolicyV1ResolveRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleChromePolicyV1ResolveResponseHttpRequest: ...
            def resolve_next(
                self,
                previous_request: GoogleChromePolicyV1ResolveResponseHttpRequest,
                previous_response: GoogleChromePolicyV1ResolveResponse,
            ) -> GoogleChromePolicyV1ResolveResponseHttpRequest | None: ...
            def groups(self) -> GroupsResource: ...
            def networks(self) -> NetworksResource: ...
            def orgunits(self) -> OrgunitsResource: ...

        @typing.type_check_only
        class PolicySchemasResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromePolicyVersionsV1PolicySchemaHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromePolicyVersionsV1ListPolicySchemasResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleChromePolicyVersionsV1ListPolicySchemasResponseHttpRequest,
                previous_response: GoogleChromePolicyVersionsV1ListPolicySchemasResponse,
            ) -> GoogleChromePolicyVersionsV1ListPolicySchemasResponseHttpRequest | None: ...

        def policies(self) -> PoliciesResource: ...
        def policySchemas(self) -> PolicySchemasResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            customer: str,
            body: GoogleChromePolicyVersionsV1UploadPolicyFileRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleChromePolicyVersionsV1UploadPolicyFileResponseHttpRequest: ...

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
    def customers(self) -> CustomersResource: ...
    def media(self) -> MediaResource: ...

@typing.type_check_only
class GoogleChromePolicyV1DefineCertificateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1DefineCertificateResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1DefineNetworkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1DefineNetworkResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1ListGroupPriorityOrderingResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1ListGroupPriorityOrderingResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1RemoveCertificateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1RemoveCertificateResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1RemoveNetworkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1RemoveNetworkResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1ResolveResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1ResolveResponse: ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1ListPolicySchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyVersionsV1ListPolicySchemasResponse: ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1PolicySchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyVersionsV1PolicySchema: ...

@typing.type_check_only
class GoogleChromePolicyVersionsV1UploadPolicyFileResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyVersionsV1UploadPolicyFileResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
