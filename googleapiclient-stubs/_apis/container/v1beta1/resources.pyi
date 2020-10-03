import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ContainerResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ZonesResource(googleapiclient.discovery.Resource):
            class ClustersResource(googleapiclient.discovery.Resource):
                class NodePoolsResource(googleapiclient.discovery.Resource):
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
                    def create(
                        self,
                        *,
                        projectId: str,
                        zone: str,
                        clusterId: str,
                        body: CreateNodePoolRequest = ...,
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
                def startIpRotation(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: StartIPRotationRequest = ...,
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
                def get(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> ClusterHttpRequest: ...
                def list(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    parent: str = ...,
                    **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
                def master(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: UpdateMasterRequest = ...,
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
                def monitoring(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetMonitoringServiceRequest = ...,
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
                def locations(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLocationsRequest = ...,
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
                def setMasterAuth(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetMasterAuthRequest = ...,
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
                def delete(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    name: str = ...,
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
                def legacyAbac(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    clusterId: str,
                    body: SetLegacyAbacRequest = ...,
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
                def nodePools(self) -> NodePoolsResource: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    operationId: str,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    projectId: str,
                    zone: str,
                    operationId: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
        class AggregatedResource(googleapiclient.discovery.Resource):
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
            def usableSubnetworks(self) -> UsableSubnetworksResource: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class ClustersResource(googleapiclient.discovery.Resource):
                class WellKnownResource(googleapiclient.discovery.Resource):
                    def getOpenid_configuration(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GetOpenIDConfigResponseHttpRequest: ...
                class NodePoolsResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        name: str,
                        projectId: str = ...,
                        clusterId: str = ...,
                        nodePoolId: str = ...,
                        zone: str = ...,
                        **kwargs: typing.Any
                    ) -> NodePoolHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UpdateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setAutoscaling(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolAutoscalingRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: CreateNodePoolRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setSize(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolSizeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setManagement(
                        self,
                        *,
                        name: str,
                        body: SetNodePoolManagementRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def rollback(
                        self,
                        *,
                        name: str,
                        body: RollbackNodePoolUpgradeRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        zone: str = ...,
                        clusterId: str = ...,
                        projectId: str = ...,
                        **kwargs: typing.Any
                    ) -> ListNodePoolsResponseHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        zone: str = ...,
                        projectId: str = ...,
                        nodePoolId: str = ...,
                        clusterId: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                def setMonitoring(
                    self,
                    *,
                    name: str,
                    body: SetMonitoringServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMaintenancePolicy(
                    self,
                    *,
                    name: str,
                    body: SetMaintenancePolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def completeIpRotation(
                    self,
                    *,
                    name: str,
                    body: CompleteIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: UpdateClusterRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setLegacyAbac(
                    self,
                    *,
                    name: str,
                    body: SetLegacyAbacRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setMasterAuth(
                    self,
                    *,
                    name: str,
                    body: SetMasterAuthRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setLogging(
                    self,
                    *,
                    name: str,
                    body: SetLoggingServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def startIpRotation(
                    self,
                    *,
                    name: str,
                    body: StartIPRotationRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    zone: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListClustersResponseHttpRequest: ...
                def setNetworkPolicy(
                    self,
                    *,
                    name: str,
                    body: SetNetworkPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def updateMaster(
                    self,
                    *,
                    name: str,
                    body: UpdateMasterRequest = ...,
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
                    zone: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def getJwks(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GetJSONWebKeysResponseHttpRequest: ...
                def setLocations(
                    self,
                    *,
                    name: str,
                    body: SetLocationsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setResourceLabels(
                    self,
                    *,
                    name: str,
                    body: SetLabelsRequest = ...,
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
                def setAddons(
                    self,
                    *,
                    name: str,
                    body: SetAddonsConfigRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def well_known(self) -> WellKnownResource: ...
                def nodePools(self) -> NodePoolsResource: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    zone: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    projectId: str = ...,
                    zone: str = ...,
                    operationId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def getServerConfig(
                self,
                *,
                name: str,
                projectId: str = ...,
                zone: str = ...,
                **kwargs: typing.Any
            ) -> ServerConfigHttpRequest: ...
            def clusters(self) -> ClustersResource: ...
            def operations(self) -> OperationsResource: ...
        def zones(self) -> ZonesResource: ...
        def aggregated(self) -> AggregatedResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ServerConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServerConfig: ...

class ListUsableSubnetworksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUsableSubnetworksResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClustersResponse: ...

class GetJSONWebKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetJSONWebKeysResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class GetOpenIDConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOpenIDConfigResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Cluster: ...

class NodePoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodePool: ...

class ListNodePoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNodePoolsResponse: ...
