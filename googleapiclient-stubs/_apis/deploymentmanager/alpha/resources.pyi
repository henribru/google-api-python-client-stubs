import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DeploymentManagerAlphaResource(googleapiclient.discovery.Resource):
    class CompositeTypesResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, compositeType: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, compositeType: str, **kwargs: typing.Any
        ) -> CompositeTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            filter: str = ...,
            returnPartialSuccess: bool = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CompositeTypesListResponseHttpRequest: ...
        def insert(
            self, *, project: str, body: CompositeType = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class TypeProvidersResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            pageToken: str = ...,
            orderBy: str = ...,
            filter: str = ...,
            maxResults: int = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def listTypes(
            self,
            *,
            project: str,
            typeProvider: str,
            pageToken: str = ...,
            orderBy: str = ...,
            filter: str = ...,
            maxResults: int = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListTypesResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def getType(
            self, *, project: str, typeProvider: str, type: str, **kwargs: typing.Any
        ) -> TypeInfoHttpRequest: ...
        def get(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> TypeProviderHttpRequest: ...
        def insert(
            self, *, project: str, body: TypeProvider = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            returnPartialSuccess: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    class TypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, type: str, **kwargs: typing.Any
        ) -> TypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TypesListResponseHttpRequest: ...
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
            maxResults: int = ...,
            returnPartialSuccess: bool = ...,
            orderBy: str = ...,
            **kwargs: typing.Any
        ) -> ResourcesListResponseHttpRequest: ...
    class ManifestsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            deployment: str,
            pageToken: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            returnPartialSuccess: bool = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ManifestsListResponseHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, manifest: str, **kwargs: typing.Any
        ) -> ManifestHttpRequest: ...
    class DeploymentsResource(googleapiclient.discovery.Resource):
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
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
            ] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            deployment: str,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            returnPartialSuccess: bool = ...,
            maxResults: int = ...,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
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
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            preview: bool = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, **kwargs: typing.Any
        ) -> DeploymentHttpRequest: ...
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
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
            ] = ...,
            preview: bool = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def compositeTypes(self) -> CompositeTypesResource: ...
    def typeProviders(self) -> TypeProvidersResource: ...
    def operations(self) -> OperationsResource: ...
    def types(self) -> TypesResource: ...
    def resources(self) -> ResourcesResource: ...
    def manifests(self) -> ManifestsResource: ...
    def deployments(self) -> DeploymentsResource: ...

class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestPermissionsResponse: ...

class TypeProvidersListTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvidersListTypesResponse: ...

class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeploymentsListResponse: ...

class CompositeTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompositeTypesListResponse: ...

class CompositeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompositeType: ...

class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Deployment: ...

class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcesListResponse: ...

class TypeProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvider: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class TypeProvidersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvidersListResponse: ...

class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationsListResponse: ...

class TypeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeInfo: ...

class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Manifest: ...

class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypesListResponse: ...

class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManifestsListResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Resource: ...

class TypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Type: ...
