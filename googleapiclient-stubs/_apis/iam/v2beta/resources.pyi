import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class IamResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PoliciesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...

        def createPolicy(
            self,
            *,
            parent: str,
            body: GoogleIamV2betaPolicy = ...,
            policyId: str = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def delete(
            self, *, name: str, etag: str = ..., **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleIamV2betaPolicyHttpRequest: ...
        def listPolicies(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleIamV2betaListPoliciesResponseHttpRequest: ...
        def listPolicies_next(
            self,
            previous_request: GoogleIamV2betaListPoliciesResponseHttpRequest,
            previous_response: GoogleIamV2betaListPoliciesResponse,
        ) -> GoogleIamV2betaListPoliciesResponseHttpRequest | None: ...
        def update(
            self, *, name: str, body: GoogleIamV2betaPolicy = ..., **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...

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
    def policies(self) -> PoliciesResource: ...

@typing.type_check_only
class GoogleIamV2betaListPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV2betaListPoliciesResponse: ...

@typing.type_check_only
class GoogleIamV2betaPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV2betaPolicy: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...
