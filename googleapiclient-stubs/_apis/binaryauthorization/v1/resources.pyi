import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> IamPolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> IamPolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def update(
                self, *, name: str, body: Attestor = ..., **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def validateAttestationOccurrence(
                self,
                *,
                attestor: str,
                body: ValidateAttestationOccurrenceRequest = ...,
                **kwargs: typing.Any,
            ) -> ValidateAttestationOccurrenceResponseHttpRequest: ...

        @typing.type_check_only
        class PlatformsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GkeResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class PoliciesResource(googleapiclient.discovery.Resource):
                    def evaluate(
                        self,
                        *,
                        name: str,
                        body: EvaluateGkePolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> EvaluateGkePolicyResponseHttpRequest: ...

                def policies(self) -> PoliciesResource: ...

            @typing.type_check_only
            class PoliciesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: PlatformPolicy = ...,
                    policyId: str = ...,
                    **kwargs: typing.Any,
                ) -> PlatformPolicyHttpRequest: ...
                def delete(
                    self, *, name: str, etag: str = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> PlatformPolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListPlatformPoliciesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListPlatformPoliciesResponseHttpRequest,
                    previous_response: ListPlatformPoliciesResponse,
                ) -> ListPlatformPoliciesResponseHttpRequest | None: ...
                def replacePlatformPolicy(
                    self, *, name: str, body: PlatformPolicy = ..., **kwargs: typing.Any
                ) -> PlatformPolicyHttpRequest: ...

            def gke(self) -> GkeResource: ...
            def policies(self) -> PoliciesResource: ...

        @typing.type_check_only
        class PolicyResource(googleapiclient.discovery.Resource):
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any,
            ) -> IamPolicyHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> IamPolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> TestIamPermissionsResponseHttpRequest: ...

        def getPolicy(
            self, *, name: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def updatePolicy(
            self, *, name: str, body: Policy = ..., **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def attestors(self) -> AttestorsResource: ...
        def platforms(self) -> PlatformsResource: ...
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def systempolicy(self) -> SystempolicyResource: ...

@typing.type_check_only
class AttestorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Attestor: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class EvaluateGkePolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EvaluateGkePolicyResponse: ...

@typing.type_check_only
class IamPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IamPolicy: ...

@typing.type_check_only
class ListAttestorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAttestorsResponse: ...

@typing.type_check_only
class ListPlatformPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPlatformPoliciesResponse: ...

@typing.type_check_only
class PlatformPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PlatformPolicy: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class ValidateAttestationOccurrenceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ValidateAttestationOccurrenceResponse: ...
