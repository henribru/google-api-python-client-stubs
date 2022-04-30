import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BinaryAuthorizationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AttestorsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Attestor = ...,
                attestorId: str = ...,
                **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAttestorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAttestorsResponseHttpRequest,
                previous_response: ListAttestorsResponse,
            ) -> ListAttestorsResponseHttpRequest | None: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def update(
                self, *, name: str, body: Attestor = ..., **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def validateAttestationOccurrence(
                self,
                *,
                attestor: str,
                body: ValidateAttestationOccurrenceRequest = ...,
                **kwargs: typing.Any
            ) -> ValidateAttestationOccurrenceResponseHttpRequest: ...

        @typing.type_check_only
        class PolicyResource(googleapiclient.discovery.Resource):
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...

        def getPolicy(
            self, *, name: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def updatePolicy(
            self, *, name: str, body: Policy = ..., **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def attestors(self) -> AttestorsResource: ...
        def policy(self) -> PolicyResource: ...

    @typing.type_check_only
    class SystempolicyResource(googleapiclient.discovery.Resource):
        def getPolicy(
            self, *, name: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...

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
    def projects(self) -> ProjectsResource: ...
    def systempolicy(self) -> SystempolicyResource: ...

@typing.type_check_only
class AttestorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Attestor: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class IamPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IamPolicy: ...

@typing.type_check_only
class ListAttestorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAttestorsResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class ValidateAttestationOccurrenceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ValidateAttestationOccurrenceResponse: ...
