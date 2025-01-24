import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GKEOnPremResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BareMetalAdminClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                        **kwargs: typing.Any,
                    ) -> ListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOperationsResponseHttpRequest,
                        previous_response: ListOperationsResponse,
                    ) -> ListOperationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: BareMetalAdminCluster = ...,
                    allowPreflightFailure: bool = ...,
                    bareMetalAdminClusterId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enroll(
                    self,
                    *,
                    parent: str,
                    body: EnrollBareMetalAdminClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> BareMetalAdminClusterHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    allowMissing: bool = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListBareMetalAdminClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBareMetalAdminClustersResponseHttpRequest,
                    previous_response: ListBareMetalAdminClustersResponse,
                ) -> ListBareMetalAdminClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: BareMetalAdminCluster = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def queryVersionConfig(
                    self,
                    *,
                    parent: str,
                    upgradeConfig_clusterName: str = ...,
                    **kwargs: typing.Any,
                ) -> QueryBareMetalAdminVersionConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def unenroll(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    ignoreErrors: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class BareMetalClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class BareMetalNodePoolsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                            **kwargs: typing.Any,
                        ) -> ListOperationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListOperationsResponseHttpRequest,
                            previous_response: ListOperationsResponse,
                        ) -> ListOperationsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: BareMetalNodePool = ...,
                        bareMetalNodePoolId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        etag: str = ...,
                        ignoreErrors: bool = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def enroll(
                        self,
                        *,
                        parent: str,
                        body: EnrollBareMetalNodePoolRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "NODE_POOL_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> BareMetalNodePoolHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "NODE_POOL_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListBareMetalNodePoolsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListBareMetalNodePoolsResponseHttpRequest,
                        previous_response: ListBareMetalNodePoolsResponse,
                    ) -> ListBareMetalNodePoolsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: BareMetalNodePool = ...,
                        allowMissing: bool = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def unenroll(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        etag: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                        **kwargs: typing.Any,
                    ) -> ListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOperationsResponseHttpRequest,
                        previous_response: ListOperationsResponse,
                    ) -> ListOperationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: BareMetalCluster = ...,
                    allowPreflightFailure: bool = ...,
                    bareMetalClusterId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    force: bool = ...,
                    ignoreErrors: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enroll(
                    self,
                    *,
                    parent: str,
                    body: EnrollBareMetalClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> BareMetalClusterHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    allowMissing: bool = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListBareMetalClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBareMetalClustersResponseHttpRequest,
                    previous_response: ListBareMetalClustersResponse,
                ) -> ListBareMetalClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: BareMetalCluster = ...,
                    allowMissing: bool = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def queryVersionConfig(
                    self,
                    *,
                    parent: str,
                    createConfig_adminClusterMembership: str = ...,
                    createConfig_adminClusterName: str = ...,
                    upgradeConfig_clusterName: str = ...,
                    **kwargs: typing.Any,
                ) -> QueryBareMetalVersionConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def unenroll(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    force: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def bareMetalNodePools(self) -> BareMetalNodePoolsResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class VmwareAdminClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                        **kwargs: typing.Any,
                    ) -> ListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOperationsResponseHttpRequest,
                        previous_response: ListOperationsResponse,
                    ) -> ListOperationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: VmwareAdminCluster = ...,
                    allowPreflightFailure: bool = ...,
                    validateOnly: bool = ...,
                    vmwareAdminClusterId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enroll(
                    self,
                    *,
                    parent: str,
                    body: EnrollVmwareAdminClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> VmwareAdminClusterHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    allowMissing: bool = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListVmwareAdminClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVmwareAdminClustersResponseHttpRequest,
                    previous_response: ListVmwareAdminClustersResponse,
                ) -> ListVmwareAdminClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: VmwareAdminCluster = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def unenroll(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class VmwareClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
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
                        **kwargs: typing.Any,
                    ) -> ListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOperationsResponseHttpRequest,
                        previous_response: ListOperationsResponse,
                    ) -> ListOperationsResponseHttpRequest | None: ...

                @typing.type_check_only
                class VmwareNodePoolsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class OperationsResource(googleapiclient.discovery.Resource):
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
                            **kwargs: typing.Any,
                        ) -> ListOperationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListOperationsResponseHttpRequest,
                            previous_response: ListOperationsResponse,
                        ) -> ListOperationsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: VmwareNodePool = ...,
                        validateOnly: bool = ...,
                        vmwareNodePoolId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        etag: str = ...,
                        ignoreErrors: bool = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def enroll(
                        self,
                        *,
                        parent: str,
                        body: EnrollVmwareNodePoolRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "NODE_POOL_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> VmwareNodePoolHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "NODE_POOL_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListVmwareNodePoolsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListVmwareNodePoolsResponseHttpRequest,
                        previous_response: ListVmwareNodePoolsResponse,
                    ) -> ListVmwareNodePoolsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: VmwareNodePool = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def unenroll(
                        self,
                        *,
                        name: str,
                        allowMissing: bool = ...,
                        etag: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def operations(self) -> OperationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: VmwareCluster = ...,
                    allowPreflightFailure: bool = ...,
                    validateOnly: bool = ...,
                    vmwareClusterId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    force: bool = ...,
                    ignoreErrors: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def enroll(
                    self,
                    *,
                    parent: str,
                    body: EnrollVmwareClusterRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> VmwareClusterHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    allowMissing: bool = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListVmwareClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListVmwareClustersResponseHttpRequest,
                    previous_response: ListVmwareClustersResponse,
                ) -> ListVmwareClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: VmwareCluster = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def queryVersionConfig(
                    self,
                    *,
                    parent: str,
                    createConfig_adminClusterMembership: str = ...,
                    createConfig_adminClusterName: str = ...,
                    upgradeConfig_clusterName: str = ...,
                    **kwargs: typing.Any,
                ) -> QueryVmwareVersionConfigResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def unenroll(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    force: bool = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
                def vmwareNodePools(self) -> VmwareNodePoolsResource: ...

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
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def bareMetalAdminClusters(self) -> BareMetalAdminClustersResource: ...
            def bareMetalClusters(self) -> BareMetalClustersResource: ...
            def operations(self) -> OperationsResource: ...
            def vmwareAdminClusters(self) -> VmwareAdminClustersResource: ...
            def vmwareClusters(self) -> VmwareClustersResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BareMetalAdminClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BareMetalAdminCluster: ...

@typing.type_check_only
class BareMetalClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BareMetalCluster: ...

@typing.type_check_only
class BareMetalNodePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BareMetalNodePool: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListBareMetalAdminClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBareMetalAdminClustersResponse: ...

@typing.type_check_only
class ListBareMetalClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBareMetalClustersResponse: ...

@typing.type_check_only
class ListBareMetalNodePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBareMetalNodePoolsResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListVmwareAdminClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVmwareAdminClustersResponse: ...

@typing.type_check_only
class ListVmwareClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVmwareClustersResponse: ...

@typing.type_check_only
class ListVmwareNodePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVmwareNodePoolsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class QueryBareMetalAdminVersionConfigResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryBareMetalAdminVersionConfigResponse: ...

@typing.type_check_only
class QueryBareMetalVersionConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryBareMetalVersionConfigResponse: ...

@typing.type_check_only
class QueryVmwareVersionConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryVmwareVersionConfigResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class VmwareAdminClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VmwareAdminCluster: ...

@typing.type_check_only
class VmwareClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VmwareCluster: ...

@typing.type_check_only
class VmwareNodePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VmwareNodePool: ...
