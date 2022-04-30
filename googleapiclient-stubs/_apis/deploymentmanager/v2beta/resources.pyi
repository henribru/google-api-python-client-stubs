import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DeploymentManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CompositeTypesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, compositeType: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, compositeType: str, **kwargs: typing.Any
        ) -> CompositeTypeHttpRequest: ...
        def insert(
            self, *, project: str, body: CompositeType = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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
        def list_next(
            self,
            previous_request: CompositeTypesListResponseHttpRequest,
            previous_response: CompositeTypesListResponse,
        ) -> CompositeTypesListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            compositeType: str,
            body: CompositeType = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class DeploymentsResource(googleapiclient.discovery.Resource):
        def cancelPreview(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsCancelPreviewRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            deployment: str,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, deployment: str, **kwargs: typing.Any
        ) -> DeploymentHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> DeploymentsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: DeploymentsListResponseHttpRequest,
            previous_response: DeploymentsListResponse,
        ) -> DeploymentsListResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            preview: bool = ...,
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
        def stop(
            self,
            *,
            project: str,
            deployment: str,
            body: DeploymentsStopRequest = ...,
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
        def update(
            self,
            *,
            project: str,
            deployment: str,
            body: Deployment = ...,
            createPolicy: typing_extensions.Literal[
                "CREATE_OR_ACQUIRE", "ACQUIRE", "CREATE"
            ] = ...,
            deletePolicy: typing_extensions.Literal["DELETE", "ABANDON"] = ...,
            preview: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ManifestsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, deployment: str, manifest: str, **kwargs: typing.Any
        ) -> ManifestHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            deployment: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ManifestsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ManifestsListResponseHttpRequest,
            previous_response: ManifestsListResponse,
        ) -> ManifestsListResponseHttpRequest | None: ...

    @typing.type_check_only
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
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> OperationsListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: OperationsListResponseHttpRequest,
            previous_response: OperationsListResponse,
        ) -> OperationsListResponseHttpRequest | None: ...

    @typing.type_check_only
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
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ResourcesListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ResourcesListResponseHttpRequest,
            previous_response: ResourcesListResponse,
        ) -> ResourcesListResponseHttpRequest | None: ...

    @typing.type_check_only
    class TypeProvidersResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, typeProvider: str, **kwargs: typing.Any
        ) -> TypeProviderHttpRequest: ...
        def getType(
            self, *, project: str, typeProvider: str, type: str, **kwargs: typing.Any
        ) -> TypeInfoHttpRequest: ...
        def insert(
            self, *, project: str, body: TypeProvider = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: TypeProvidersListResponseHttpRequest,
            previous_response: TypeProvidersListResponse,
        ) -> TypeProvidersListResponseHttpRequest | None: ...
        def listTypes(
            self,
            *,
            project: str,
            typeProvider: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> TypeProvidersListTypesResponseHttpRequest: ...
        def listTypes_next(
            self,
            previous_request: TypeProvidersListTypesResponseHttpRequest,
            previous_response: TypeProvidersListTypesResponse,
        ) -> TypeProvidersListTypesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            typeProvider: str,
            body: TypeProvider = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: TypesListResponseHttpRequest,
            previous_response: TypesListResponse,
        ) -> TypesListResponseHttpRequest | None: ...

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
    def compositeTypes(self) -> CompositeTypesResource: ...
    def deployments(self) -> DeploymentsResource: ...
    def manifests(self) -> ManifestsResource: ...
    def operations(self) -> OperationsResource: ...
    def resources(self) -> ResourcesResource: ...
    def typeProviders(self) -> TypeProvidersResource: ...
    def types(self) -> TypesResource: ...

@typing.type_check_only
class CompositeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CompositeType: ...

@typing.type_check_only
class CompositeTypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CompositeTypesListResponse: ...

@typing.type_check_only
class DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Deployment: ...

@typing.type_check_only
class DeploymentsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeploymentsListResponse: ...

@typing.type_check_only
class ManifestHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Manifest: ...

@typing.type_check_only
class ManifestsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ManifestsListResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OperationsListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperationsListResponse: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ResourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Resource: ...

@typing.type_check_only
class ResourcesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourcesListResponse: ...

@typing.type_check_only
class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestPermissionsResponse: ...

@typing.type_check_only
class TypeInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TypeInfo: ...

@typing.type_check_only
class TypeProviderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TypeProvider: ...

@typing.type_check_only
class TypeProvidersListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TypeProvidersListResponse: ...

@typing.type_check_only
class TypeProvidersListTypesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TypeProvidersListTypesResponse: ...

@typing.type_check_only
class TypesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TypesListResponse: ...
