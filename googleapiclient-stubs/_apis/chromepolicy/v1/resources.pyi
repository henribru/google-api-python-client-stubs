import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class ChromePolicyResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PoliciesResource(googleapiclient.discovery.Resource):
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
            def orgunits(self) -> OrgunitsResource: ...
        @typing.type_check_only
        class PolicySchemasResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleChromePolicyV1PolicySchemaHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleChromePolicyV1ListPolicySchemasResponseHttpRequest: ...
        def policies(self) -> PoliciesResource: ...
        def policySchemas(self) -> PolicySchemasResource: ...
    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self,
            *,
            customer: str,
            body: GoogleChromePolicyV1UploadPolicyFileRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleChromePolicyV1UploadPolicyFileResponseHttpRequest: ...
    def customers(self) -> CustomersResource: ...
    def media(self) -> MediaResource: ...

@typing.type_check_only
class GoogleChromePolicyV1ListPolicySchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1ListPolicySchemasResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1PolicySchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1PolicySchema: ...

@typing.type_check_only
class GoogleChromePolicyV1ResolveResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1ResolveResponse: ...

@typing.type_check_only
class GoogleChromePolicyV1UploadPolicyFileResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleChromePolicyV1UploadPolicyFileResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
