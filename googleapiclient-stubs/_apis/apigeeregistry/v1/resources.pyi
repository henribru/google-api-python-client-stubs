import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ApigeeRegistryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ApisResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ArtifactsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Artifact = ...,
                        artifactId: str = ...,
                        **kwargs: typing.Any
                    ) -> ArtifactHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ArtifactHttpRequest: ...
                    def getContents(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListArtifactsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListArtifactsResponseHttpRequest,
                        previous_response: ListArtifactsResponse,
                    ) -> ListArtifactsResponseHttpRequest | None: ...
                    def replaceArtifact(
                        self, *, name: str, body: Artifact = ..., **kwargs: typing.Any
                    ) -> ArtifactHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ArtifactsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Artifact = ...,
                            artifactId: str = ...,
                            **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...
                        def getContents(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListArtifactsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListArtifactsResponseHttpRequest,
                            previous_response: ListArtifactsResponse,
                        ) -> ListArtifactsResponseHttpRequest | None: ...
                        def replaceArtifact(
                            self,
                            *,
                            name: str,
                            body: Artifact = ...,
                            **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: ApiDeployment = ...,
                        apiDeploymentId: str = ...,
                        **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def deleteRevision(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListApiDeploymentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListApiDeploymentsResponseHttpRequest,
                        previous_response: ListApiDeploymentsResponse,
                    ) -> ListApiDeploymentsResponseHttpRequest | None: ...
                    def listRevisions(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListApiDeploymentRevisionsResponseHttpRequest: ...
                    def listRevisions_next(
                        self,
                        previous_request: ListApiDeploymentRevisionsResponseHttpRequest,
                        previous_response: ListApiDeploymentRevisionsResponse,
                    ) -> ListApiDeploymentRevisionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ApiDeployment = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        name: str,
                        body: RollbackApiDeploymentRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def tagRevision(
                        self,
                        *,
                        name: str,
                        body: TagApiDeploymentRevisionRequest = ...,
                        **kwargs: typing.Any
                    ) -> ApiDeploymentHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def artifacts(self) -> ArtifactsResource: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ArtifactsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Artifact = ...,
                            artifactId: str = ...,
                            **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...
                        def getContents(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any
                        ) -> PolicyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListArtifactsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListArtifactsResponseHttpRequest,
                            previous_response: ListArtifactsResponse,
                        ) -> ListArtifactsResponseHttpRequest | None: ...
                        def replaceArtifact(
                            self,
                            *,
                            name: str,
                            body: Artifact = ...,
                            **kwargs: typing.Any
                        ) -> ArtifactHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: SetIamPolicyRequest = ...,
                            **kwargs: typing.Any
                        ) -> PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any
                        ) -> TestIamPermissionsResponseHttpRequest: ...

                    @typing.type_check_only
                    class SpecsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class ArtifactsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: Artifact = ...,
                                artifactId: str = ...,
                                **kwargs: typing.Any
                            ) -> ArtifactHttpRequest: ...
                            def delete(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> EmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> ArtifactHttpRequest: ...
                            def getContents(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def getIamPolicy(
                                self,
                                *,
                                resource: str,
                                options_requestedPolicyVersion: int = ...,
                                **kwargs: typing.Any
                            ) -> PolicyHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> ListArtifactsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: ListArtifactsResponseHttpRequest,
                                previous_response: ListArtifactsResponse,
                            ) -> ListArtifactsResponseHttpRequest | None: ...
                            def replaceArtifact(
                                self,
                                *,
                                name: str,
                                body: Artifact = ...,
                                **kwargs: typing.Any
                            ) -> ArtifactHttpRequest: ...
                            def setIamPolicy(
                                self,
                                *,
                                resource: str,
                                body: SetIamPolicyRequest = ...,
                                **kwargs: typing.Any
                            ) -> PolicyHttpRequest: ...
                            def testIamPermissions(
                                self,
                                *,
                                resource: str,
                                body: TestIamPermissionsRequest = ...,
                                **kwargs: typing.Any
                            ) -> TestIamPermissionsResponseHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: ApiSpec = ...,
                            apiSpecId: str = ...,
                            **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def deleteRevision(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def getContents(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any
                        ) -> PolicyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListApiSpecsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListApiSpecsResponseHttpRequest,
                            previous_response: ListApiSpecsResponse,
                        ) -> ListApiSpecsResponseHttpRequest | None: ...
                        def listRevisions(
                            self,
                            *,
                            name: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListApiSpecRevisionsResponseHttpRequest: ...
                        def listRevisions_next(
                            self,
                            previous_request: ListApiSpecRevisionsResponseHttpRequest,
                            previous_response: ListApiSpecRevisionsResponse,
                        ) -> ListApiSpecRevisionsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: ApiSpec = ...,
                            allowMissing: bool = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def rollback(
                            self,
                            *,
                            name: str,
                            body: RollbackApiSpecRequest = ...,
                            **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: SetIamPolicyRequest = ...,
                            **kwargs: typing.Any
                        ) -> PolicyHttpRequest: ...
                        def tagRevision(
                            self,
                            *,
                            name: str,
                            body: TagApiSpecRevisionRequest = ...,
                            **kwargs: typing.Any
                        ) -> ApiSpecHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any
                        ) -> TestIamPermissionsResponseHttpRequest: ...
                        def artifacts(self) -> ArtifactsResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: ApiVersion = ...,
                        apiVersionId: str = ...,
                        **kwargs: typing.Any
                    ) -> ApiVersionHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ApiVersionHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListApiVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListApiVersionsResponseHttpRequest,
                        previous_response: ListApiVersionsResponse,
                    ) -> ListApiVersionsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ApiVersion = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ApiVersionHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def artifacts(self) -> ArtifactsResource: ...
                    def specs(self) -> SpecsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Api = ...,
                    apiId: str = ...,
                    **kwargs: typing.Any
                ) -> ApiHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(self, *, name: str, **kwargs: typing.Any) -> ApiHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListApisResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListApisResponseHttpRequest,
                    previous_response: ListApisResponse,
                ) -> ListApisResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Api = ...,
                    allowMissing: bool = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ApiHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def artifacts(self) -> ArtifactsResource: ...
                def deployments(self) -> DeploymentsResource: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class ArtifactsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Artifact = ...,
                    artifactId: str = ...,
                    **kwargs: typing.Any
                ) -> ArtifactHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ArtifactHttpRequest: ...
                def getContents(
                    self, *, name: str, **kwargs: typing.Any
                ) -> HttpBodyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListArtifactsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListArtifactsResponseHttpRequest,
                    previous_response: ListArtifactsResponse,
                ) -> ListArtifactsResponseHttpRequest | None: ...
                def replaceArtifact(
                    self, *, name: str, body: Artifact = ..., **kwargs: typing.Any
                ) -> ArtifactHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class InstancesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Instance = ...,
                    instanceId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> InstanceHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RuntimeResource(googleapiclient.discovery.Resource):
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def apis(self) -> ApisResource: ...
            def artifacts(self) -> ArtifactsResource: ...
            def instances(self) -> InstancesResource: ...
            def operations(self) -> OperationsResource: ...
            def runtime(self) -> RuntimeResource: ...

        def locations(self) -> LocationsResource: ...

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

@typing.type_check_only
class ApiHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Api: ...

@typing.type_check_only
class ApiDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApiDeployment: ...

@typing.type_check_only
class ApiSpecHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApiSpec: ...

@typing.type_check_only
class ApiVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ApiVersion: ...

@typing.type_check_only
class ArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Artifact: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Instance: ...

@typing.type_check_only
class ListApiDeploymentRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApiDeploymentRevisionsResponse: ...

@typing.type_check_only
class ListApiDeploymentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApiDeploymentsResponse: ...

@typing.type_check_only
class ListApiSpecRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApiSpecRevisionsResponse: ...

@typing.type_check_only
class ListApiSpecsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApiSpecsResponse: ...

@typing.type_check_only
class ListApiVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApiVersionsResponse: ...

@typing.type_check_only
class ListApisResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListApisResponse: ...

@typing.type_check_only
class ListArtifactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListArtifactsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

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
