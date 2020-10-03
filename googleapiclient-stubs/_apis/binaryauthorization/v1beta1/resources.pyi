import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BinaryAuthorizationResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class AttestorsResource(googleapiclient.discovery.Resource):
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListAttestorsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Attestor = ...,
                attestorId: str = ...,
                **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AttestorHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
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
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
        class PolicyResource(googleapiclient.discovery.Resource):
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
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> IamPolicyHttpRequest: ...
        def updatePolicy(
            self, *, name: str, body: Policy = ..., **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getPolicy(
            self, *, name: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def attestors(self) -> AttestorsResource: ...
        def policy(self) -> PolicyResource: ...
    def projects(self) -> ProjectsResource: ...

class ListAttestorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAttestorsResponse: ...

class ValidateAttestationOccurrenceResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ValidateAttestationOccurrenceResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class IamPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IamPolicy: ...

class AttestorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Attestor: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...
