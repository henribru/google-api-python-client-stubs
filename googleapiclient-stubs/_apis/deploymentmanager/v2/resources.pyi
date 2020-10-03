import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DeploymentManagerResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    class ResourcesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, deployment: str, resource: str, **kwargs: typing.Any
        ) -> ResourceHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ResourcesListResponseHttpRequest: ...
    class ManifestsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ManifestsListResponseHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, manifest: str, **kwargs: typing.Any
        ) -> ManifestHttpRequest: ...
    class DeploymentsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            deployment: str,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, **kwargs: typing.Any
        ) -> DeploymentHttpRequest: ...
        def getIamPolicy(
            self, *, project: str, resource: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            preview: bool = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            orderBy: str = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> DeploymentsListResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def cancelPreview(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsCancelPreviewRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def stop(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsStopRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            preview: bool = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE_OR_ACQUIRE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class TypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TypesListResponseHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def resources(self) -> ResourcesResource: ...
    def manifests(self) -> ManifestsResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def types(self) -> TypesResource: ...

class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestPermissionsResponse: ...

class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Manifest: ...

class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeploymentsListResponse: ...

class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypesListResponse: ...

class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Deployment: ...

class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcesListResponse: ...

class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManifestsListResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationsListResponse: ...

class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Resource: ...
