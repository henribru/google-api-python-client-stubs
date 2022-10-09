import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ContainerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AggregatedResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class UsableSubnetworksResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListUsableSubnetworksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUsableSubnetworksResponseHttpRequest,
                    previous_response: ListUsableSubnetworksResponse,
                ) -> ListUsableSubnetworksResponseHttpRequest | None: ...

            def usableSubnetworks(self) -> UsableSubnetworksResource: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NodePoolsResource(googleapiclient.discovery.Resource):
                    def completeUpgrade(
                        self,
                        *,
                        name: str,
                        body: CompleteNodePoolUpgradeRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CreateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        clusterId: str = ...,
                        nodePoolId: str = ...,
                        projectId: str = ...,
                        zone: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        clusterId: str = ...,
                        nodePoolId: str = ...,
                        projectId: str = ...,
                        zone: str = ...,
                        **kwargs: typing.Any
                    ) -> NodePoolHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        clusterId: str = ...,
                        projectId: str = ...,
                        zone: str = ...,
                        **kwargs: typing.Any
                    ) -> ListNodePoolsResponseHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        name: str,
                        body: RollbackNodePoolUpgradeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setAutoscaling(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolAutoscalingRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setManagement(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolManagementRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setSize(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolSizeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UpdateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                @typing.type_check_only
                class WellKnownResource(googleapiclient.discovery.Resource):
                    def getOpenid_configuration(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GetOpenIDConfigResponseHttpRequest: ...

                def completeIpRotation(
                    self,
                    *,
                    name: str,
                    body: CompleteIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    clusterId: str = ...,
                    projectId: str = ...,
                    zone: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    clusterId: str = ...,
                    projectId: str = ...,
                    zone: str = ...,
                    **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def getJwks(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GetJSONWebKeysResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    projectId: str = ...,
                    zone: str = ...,
                    **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
                def setAddons(
                    self,
                    *,
                    name: str,
                    body: SetAddonsConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setLegacyAbac(
                    self,
                    *,
                    name: str,
                    body: SetLegacyAbacRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setLocations(
                    self,
                    *,
                    name: str,
                    body: SetLocationsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setLogging(
                    self,
                    *,
                    name: str,
                    body: SetLoggingServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMaintenancePolicy(
                    self,
                    *,
                    name: str,
                    body: SetMaintenancePolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMasterAuth(
                    self,
                    *,
                    name: str,
                    body: SetMasterAuthRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMonitoring(
                    self,
                    *,
                    name: str,
                    body: SetMonitoringServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setNetworkPolicy(
                    self,
                    *,
                    name: str,
                    body: SetNetworkPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setResourceLabels(
                    self,
                    *,
                    name: str,
                    body: SetLabelsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def startIpRotation(
                    self,
                    *,
                    name: str,
                    body: StartIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: UpdateClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def updateMaster(
                    self,
                    *,
                    name: str,
                    body: UpdateMasterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def nodePools(self) -> NodePoolsResource: ...
                def well_known(self) -> WellKnownResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    operationId: str = ...,
                    projectId: str = ...,
                    zone: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    projectId: str = ...,
                    zone: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...

            def getServerConfig(
                self,
                *,
                name: str,
                projectId: str = ...,
                zone: str = ...,
                **kwargs: typing.Any
            ) -> ServerConfigHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def clusters(self) -> ClustersResource: ...
            def operations(self) -> OperationsResource: ...

        @typing.type_check_only
        class ZonesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NodePoolsResource(googleapiclient.discovery.Resource):
                    def autoscaling(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        body: SetNodePoolAutoscalingRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        body: CreateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        name: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        name: str = ...,
                        **kwargs: typing.Any
                    ) -> NodePoolHttpRequest: ...
                    def list(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        parent: str = ...,
                        **kwargs: typing.Any
                    ) -> ListNodePoolsResponseHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        body: RollbackNodePoolUpgradeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setManagement(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        body: SetNodePoolManagementRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setSize(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        body: SetNodePoolSizeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def update(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        nodePoolId: str,
                        body: UpdateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...

                def addons(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetAddonsConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def completeIpRotation(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: CompleteIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    body: CreateClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def legacyAbac(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLegacyAbacRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    parent: str = ...,
                    **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
                def locations(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLocationsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def logging(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLoggingServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def master(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: UpdateMasterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def monitoring(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetMonitoringServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def resourceLabels(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLabelsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMaintenancePolicy(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetMaintenancePolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMasterAuth(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetMasterAuthRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setNetworkPolicy(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetNetworkPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def startIpRotation(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: StartIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def update(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: UpdateClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def nodePools(self) -> NodePoolsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    operationId: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    operationId: str,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    parent: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...

            def getServerconfig(
                self,
                *,
                projectId: str,
                zone: str,
                name: str = ...,
                **kwargs: typing.Any
            ) -> ServerConfigHttpRequest: ...
            def clusters(self) -> ClustersResource: ...
            def operations(self) -> OperationsResource: ...

        def aggregated(self) -> AggregatedResource: ...
        def locations(self) -> LocationsResource: ...
        def zones(self) -> ZonesResource: ...

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
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Cluster: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetJSONWebKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetJSONWebKeysResponse: ...

@typing.type_check_only
class GetOpenIDConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOpenIDConfigResponse: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListNodePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNodePoolsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListUsableSubnetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUsableSubnetworksResponse: ...

@typing.type_check_only
class NodePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodePool: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ServerConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServerConfig: ...
