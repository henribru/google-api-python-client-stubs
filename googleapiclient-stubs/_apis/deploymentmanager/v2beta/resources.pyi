import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DeploymentManagerV2BetaResource(googleapiclient.discovery.Resource):
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
            maxResults: int = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            **kwargs: typing.Any
        ) -> ResourcesListResponseHttpRequest: ...
    class CompositeTypesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CompositeTypesListResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, compositeType: str, **kwargs: typing.Any
        ) -> CompositeTypeHttpRequest: ...
        def insert(
            self, *, project: str, body: CompositeType = ..., **kwargs: typing.Any
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
    class TypeProvidersResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> TypeProviderHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self, *, project: str, body: TypeProvider = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def listTypes(
            self,
            *,
            project: str,
            typeProvider: str,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListTypesResponseHttpRequest: ...
        def getType(
            self, *, project: str, typeProvider: str, type: str, **kwargs: typing.Any
        ) -> TypeInfoHttpRequest: ...
        def delete(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            pageToken: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListResponseHttpRequest: ...
    class ManifestsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, deployment: str, manifest: str, **kwargs: typing.Any
        ) -> ManifestHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            orderBy: str = ...,
            maxResults: int = ...,
            filter: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ManifestsListResponseHttpRequest: ...
    class DeploymentsResource(googleapiclient.discovery.Resource):
        def getIamPolicy(
            self, *, project: str, resource: str, **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, **kwargs: typing.Any
        ) -> DeploymentHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            preview: bool = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
            ] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Deployment = ...,
            preview: bool = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
            ] = ...,
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
        def cancelPreview(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsCancelPreviewRequest = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            deletePolicy: typing_extensions.Literal["ABANDON", "DELETE"] = ...,
            createPolicy: typing_extensions.Literal[
                "ACQUIRE", "CREATE", "CREATE_OR_ACQUIRE"
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
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            pageToken: str = ...,
            orderBy: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
    def resources(self) -> ResourcesResource: ...
    def compositeTypes(self) -> CompositeTypesResource: ...
    def types(self) -> TypesResource: ...
    def typeProviders(self) -> TypeProvidersResource: ...
    def manifests(self) -> ManifestsResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def operations(self) -> OperationsResource: ...

class TypeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeInfo: ...

class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestPermissionsResponse: ...

class TypeProvidersListTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvidersListTypesResponse: ...

class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Manifest: ...

class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypesListResponse: ...

class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeploymentsListResponse: ...

class CompositeTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompositeTypesListResponse: ...

class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Deployment: ...

class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationsListResponse: ...

class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcesListResponse: ...

class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ManifestsListResponse: ...

class TypeProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvider: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class TypeProvidersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TypeProvidersListResponse: ...

class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Resource: ...

class CompositeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CompositeType: ...
