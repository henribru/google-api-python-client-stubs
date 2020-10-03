import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ComputeResource(googleapiclient.discovery.Resource):
    class AcceleratorTypesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AcceleratorTypeAggregatedListHttpRequest: ...
        def get(
            self, *, project: str, zone: str, acceleratorType: str, **kwargs: typing.Any
        ) -> AcceleratorTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AcceleratorTypeListHttpRequest: ...
    class AddressesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AddressAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            address: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, address: str, **kwargs: typing.Any
        ) -> AddressHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Address = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AddressListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class AutoscalersResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AutoscalerAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            autoscaler: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, autoscaler: str, **kwargs: typing.Any
        ) -> AutoscalerHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: Autoscaler = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AutoscalerListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            zone: str,
            body: Autoscaler = ...,
            autoscaler: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            zone: str,
            body: Autoscaler = ...,
            autoscaler: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class BackendBucketsResource(googleapiclient.discovery.Resource):
        def addSignedUrlKey(
            self,
            *,
            project: str,
            backendBucket: str,
            body: SignedUrlKey = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            backendBucket: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteSignedUrlKey(
            self,
            *,
            project: str,
            backendBucket: str,
            keyName: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, backendBucket: str, **kwargs: typing.Any
        ) -> BackendBucketHttpRequest: ...
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
            body: BackendBucket = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> BackendBucketListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            backendBucket: str,
            body: BackendBucket = ...,
            requestId: str = ...,
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
            backendBucket: str,
            body: BackendBucket = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class BackendServicesResource(googleapiclient.discovery.Resource):
        def addSignedUrlKey(
            self,
            *,
            project: str,
            backendService: str,
            body: SignedUrlKey = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> BackendServiceAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            backendService: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteSignedUrlKey(
            self,
            *,
            project: str,
            backendService: str,
            keyName: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, backendService: str, **kwargs: typing.Any
        ) -> BackendServiceHttpRequest: ...
        def getHealth(
            self,
            *,
            project: str,
            backendService: str,
            body: ResourceGroupReference = ...,
            **kwargs: typing.Any
        ) -> BackendServiceGroupHealthHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: BackendService = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> BackendServiceListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            backendService: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setSecurityPolicy(
            self,
            *,
            project: str,
            backendService: str,
            body: SecurityPolicyReference = ...,
            requestId: str = ...,
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
            backendService: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class DiskTypesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> DiskTypeAggregatedListHttpRequest: ...
        def get(
            self, *, project: str, zone: str, diskType: str, **kwargs: typing.Any
        ) -> DiskTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> DiskTypeListHttpRequest: ...
    class DisksResource(googleapiclient.discovery.Resource):
        def addResourcePolicies(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            body: DisksAddResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> DiskAggregatedListHttpRequest: ...
        def createSnapshot(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            body: Snapshot = ...,
            guestFlush: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, disk: str, **kwargs: typing.Any
        ) -> DiskHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: Disk = ...,
            requestId: str = ...,
            sourceImage: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> DiskListHttpRequest: ...
        def removeResourcePolicies(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            body: DisksRemoveResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resize(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            body: DisksResizeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ExternalVpnGatewaysResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            externalVpnGateway: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, externalVpnGateway: str, **kwargs: typing.Any
        ) -> ExternalVpnGatewayHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: ExternalVpnGateway = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ExternalVpnGatewayListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class FirewallsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            firewall: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, firewall: str, **kwargs: typing.Any
        ) -> FirewallHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Firewall = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> FirewallListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            firewall: str,
            body: Firewall = ...,
            requestId: str = ...,
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
            firewall: str,
            body: Firewall = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ForwardingRulesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ForwardingRuleAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            forwardingRule: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            forwardingRule: str,
            **kwargs: typing.Any
        ) -> ForwardingRuleHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: ForwardingRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ForwardingRuleListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            forwardingRule: str,
            body: ForwardingRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setTarget(
            self,
            *,
            project: str,
            region: str,
            forwardingRule: str,
            body: TargetReference = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class GlobalAddressesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            address: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, address: str, **kwargs: typing.Any
        ) -> AddressHttpRequest: ...
        def getOwnerInstance(
            self, *, project: str, ipAddress: str = ..., **kwargs: typing.Any
        ) -> GetOwnerInstanceResponseHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Address = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> AddressListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class GlobalForwardingRulesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            forwardingRule: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, forwardingRule: str, **kwargs: typing.Any
        ) -> ForwardingRuleHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: ForwardingRule = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ForwardingRuleListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            forwardingRule: str,
            body: ForwardingRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setTarget(
            self,
            *,
            project: str,
            forwardingRule: str,
            body: TargetReference = ...,
            requestId: str = ...,
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
    class GlobalNetworkEndpointGroupsResource(googleapiclient.discovery.Resource):
        def attachNetworkEndpoints(
            self,
            *,
            project: str,
            networkEndpointGroup: str,
            body: GlobalNetworkEndpointGroupsAttachEndpointsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            networkEndpointGroup: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def detachNetworkEndpoints(
            self,
            *,
            project: str,
            networkEndpointGroup: str,
            body: GlobalNetworkEndpointGroupsDetachEndpointsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, networkEndpointGroup: str, **kwargs: typing.Any
        ) -> NetworkEndpointGroupHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: NetworkEndpointGroup = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupListHttpRequest: ...
        def listNetworkEndpoints(
            self,
            *,
            project: str,
            networkEndpointGroup: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupsListNetworkEndpointsHttpRequest: ...
    class GlobalOperationsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> OperationAggregatedListHttpRequest: ...
        def delete(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> OperationListHttpRequest: ...
        def wait(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class GlobalOrganizationOperationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, operation: str, parentId: str = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, operation: str, parentId: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            parentId: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> OperationListHttpRequest: ...
    class GlobalPublicDelegatedPrefixesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            publicDelegatedPrefix: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, publicDelegatedPrefix: str, **kwargs: typing.Any
        ) -> PublicDelegatedPrefixHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: PublicDelegatedPrefix = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PublicDelegatedPrefixListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            publicDelegatedPrefix: str,
            body: PublicDelegatedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class HealthChecksResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HealthChecksAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            healthCheck: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, healthCheck: str, **kwargs: typing.Any
        ) -> HealthCheckHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: HealthCheck = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HealthCheckListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            healthCheck: str,
            body: HealthCheck = ...,
            requestId: str = ...,
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
            healthCheck: str,
            body: HealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class HttpHealthChecksResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            httpHealthCheck: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, httpHealthCheck: str, **kwargs: typing.Any
        ) -> HttpHealthCheckHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: HttpHealthCheck = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HttpHealthCheckListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            httpHealthCheck: str,
            body: HttpHealthCheck = ...,
            requestId: str = ...,
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
            httpHealthCheck: str,
            body: HttpHealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class HttpsHealthChecksResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            httpsHealthCheck: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, httpsHealthCheck: str, **kwargs: typing.Any
        ) -> HttpsHealthCheckHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: HttpsHealthCheck = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HttpsHealthCheckListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            httpsHealthCheck: str,
            body: HttpsHealthCheck = ...,
            requestId: str = ...,
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
            httpsHealthCheck: str,
            body: HttpsHealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ImagesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            image: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deprecate(
            self,
            *,
            project: str,
            image: str,
            body: DeprecationStatus = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, image: str, **kwargs: typing.Any
        ) -> ImageHttpRequest: ...
        def getFromFamily(
            self, *, project: str, family: str, **kwargs: typing.Any
        ) -> ImageHttpRequest: ...
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
            body: Image = ...,
            forceCreate: bool = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ImageListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            image: str,
            body: Image = ...,
            requestId: str = ...,
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
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class InstanceGroupManagersResource(googleapiclient.discovery.Resource):
        def abandonInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersAbandonInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupManagerAggregatedListHttpRequest: ...
        def applyUpdatesToInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersApplyUpdatesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def createInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersCreateInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersDeleteInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deletePerInstanceConfigs(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersDeletePerInstanceConfigsReq = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            **kwargs: typing.Any
        ) -> InstanceGroupManagerHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupManagerListHttpRequest: ...
        def listErrors(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupManagersListErrorsResponseHttpRequest: ...
        def listManagedInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupManagersListManagedInstancesResponseHttpRequest: ...
        def listPerInstanceConfigs(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupManagersListPerInstanceConfigsRespHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchPerInstanceConfigs(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersPatchPerInstanceConfigsReq = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def recreateInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersRecreateInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resize(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            size: int,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resizeAdvanced(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersResizeAdvancedRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setAutoHealingPolicies(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersSetAutoHealingRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setInstanceTemplate(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersSetInstanceTemplateRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setTargetPools(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersSetTargetPoolsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updatePerInstanceConfigs(
            self,
            *,
            project: str,
            zone: str,
            instanceGroupManager: str,
            body: InstanceGroupManagersUpdatePerInstanceConfigsReq = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class InstanceGroupsResource(googleapiclient.discovery.Resource):
        def addInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroup: str,
            body: InstanceGroupsAddInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            instanceGroup: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, instanceGroup: str, **kwargs: typing.Any
        ) -> InstanceGroupHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: InstanceGroup = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupListHttpRequest: ...
        def listInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroup: str,
            body: InstanceGroupsListInstancesRequest = ...,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceGroupsListInstancesHttpRequest: ...
        def removeInstances(
            self,
            *,
            project: str,
            zone: str,
            instanceGroup: str,
            body: InstanceGroupsRemoveInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setNamedPorts(
            self,
            *,
            project: str,
            zone: str,
            instanceGroup: str,
            body: InstanceGroupsSetNamedPortsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class InstanceTemplatesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            instanceTemplate: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, instanceTemplate: str, **kwargs: typing.Any
        ) -> InstanceTemplateHttpRequest: ...
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
            body: InstanceTemplate = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceTemplateListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
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
    class InstancesResource(googleapiclient.discovery.Resource):
        def addAccessConfig(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            networkInterface: str,
            body: AccessConfig = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addResourcePolicies(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesAddResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceAggregatedListHttpRequest: ...
        def attachDisk(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: AttachedDisk = ...,
            forceAttach: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def bulkInsert(
            self,
            *,
            project: str,
            zone: str,
            body: BulkInsertInstanceResource = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteAccessConfig(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            accessConfig: str,
            networkInterface: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def detachDisk(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            deviceName: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> InstanceHttpRequest: ...
        def getEffectiveFirewalls(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            networkInterface: str,
            **kwargs: typing.Any
        ) -> InstancesGetEffectiveFirewallsResponseHttpRequest: ...
        def getGuestAttributes(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            queryPath: str = ...,
            variableKey: str = ...,
            **kwargs: typing.Any
        ) -> GuestAttributesHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getScreenshot(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> ScreenshotHttpRequest: ...
        def getSerialPortOutput(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            port: int = ...,
            start: str = ...,
            **kwargs: typing.Any
        ) -> SerialPortOutputHttpRequest: ...
        def getShieldedInstanceIdentity(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> ShieldedInstanceIdentityHttpRequest: ...
        def getShieldedVmIdentity(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> ShieldedVmIdentityHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: Instance = ...,
            requestId: str = ...,
            sourceInstanceTemplate: str = ...,
            sourceMachineImage: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceListHttpRequest: ...
        def listReferrers(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstanceListReferrersHttpRequest: ...
        def removeResourcePolicies(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesRemoveResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def reset(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resume(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesResumeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setDeletionProtection(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            deletionProtection: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setDiskAutoDelete(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            autoDelete: bool,
            deviceName: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setMachineResources(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetMachineResourcesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setMachineType(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetMachineTypeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setMetadata(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: Metadata = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setMinCpuPlatform(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetMinCpuPlatformRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setName(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetNameRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setScheduling(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: Scheduling = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setServiceAccount(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesSetServiceAccountRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setShieldedInstanceIntegrityPolicy(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: ShieldedInstanceIntegrityPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setShieldedVmIntegrityPolicy(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: ShieldedVmIntegrityPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setTags(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: Tags = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def simulateMaintenanceEvent(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def start(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def startWithEncryptionKey(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: InstancesStartWithEncryptionKeyRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def stop(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            discardLocalSsd: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def suspend(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            discardLocalSsd: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: Instance = ...,
            minimalAction: typing_extensions.Literal[
                "INVALID", "NO_EFFECT", "REFRESH", "RESTART"
            ] = ...,
            mostDisruptiveAllowedAction: typing_extensions.Literal[
                "INVALID", "NO_EFFECT", "REFRESH", "RESTART"
            ] = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateAccessConfig(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            networkInterface: str,
            body: AccessConfig = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateDisplayDevice(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: DisplayDevice = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateNetworkInterface(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            networkInterface: str,
            body: NetworkInterface = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateShieldedInstanceConfig(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: ShieldedInstanceConfig = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updateShieldedVmConfig(
            self,
            *,
            project: str,
            zone: str,
            instance: str,
            body: ShieldedVmConfig = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class InterconnectAttachmentsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InterconnectAttachmentAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            interconnectAttachment: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            interconnectAttachment: str,
            **kwargs: typing.Any
        ) -> InterconnectAttachmentHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: InterconnectAttachment = ...,
            requestId: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InterconnectAttachmentListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            interconnectAttachment: str,
            body: InterconnectAttachment = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class InterconnectLocationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, interconnectLocation: str, **kwargs: typing.Any
        ) -> InterconnectLocationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InterconnectLocationListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class InterconnectsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            interconnect: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, interconnect: str, **kwargs: typing.Any
        ) -> InterconnectHttpRequest: ...
        def getDiagnostics(
            self, *, project: str, interconnect: str, **kwargs: typing.Any
        ) -> InterconnectsGetDiagnosticsResponseHttpRequest: ...
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
            body: Interconnect = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InterconnectListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            interconnect: str,
            body: Interconnect = ...,
            requestId: str = ...,
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
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class LicenseCodesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, licenseCode: str, **kwargs: typing.Any
        ) -> LicenseCodeHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
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
    class LicensesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            license: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, license: str, **kwargs: typing.Any
        ) -> LicenseHttpRequest: ...
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
            body: License = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> LicensesListResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
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
    class MachineImagesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            machineImage: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, machineImage: str, **kwargs: typing.Any
        ) -> MachineImageHttpRequest: ...
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
            body: MachineImage = ...,
            requestId: str = ...,
            sourceInstance: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> MachineImageListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
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
    class MachineTypesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> MachineTypeAggregatedListHttpRequest: ...
        def get(
            self, *, project: str, zone: str, machineType: str, **kwargs: typing.Any
        ) -> MachineTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> MachineTypeListHttpRequest: ...
    class NetworkEndpointGroupsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupAggregatedListHttpRequest: ...
        def attachNetworkEndpoints(
            self,
            *,
            project: str,
            zone: str,
            networkEndpointGroup: str,
            body: NetworkEndpointGroupsAttachEndpointsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            networkEndpointGroup: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def detachNetworkEndpoints(
            self,
            *,
            project: str,
            zone: str,
            networkEndpointGroup: str,
            body: NetworkEndpointGroupsDetachEndpointsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            zone: str,
            networkEndpointGroup: str,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: NetworkEndpointGroup = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupListHttpRequest: ...
        def listNetworkEndpoints(
            self,
            *,
            project: str,
            zone: str,
            networkEndpointGroup: str,
            body: NetworkEndpointGroupsListEndpointsRequest = ...,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupsListNetworkEndpointsHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class NetworkFirewallPoliciesResource(googleapiclient.discovery.Resource):
        def addAssociation(
            self,
            *,
            project: str,
            firewallPolicy: str,
            body: FirewallPolicyAssociation = ...,
            replaceExistingAssociation: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addRule(
            self,
            *,
            project: str,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def cloneRules(
            self,
            *,
            project: str,
            firewallPolicy: str,
            requestId: str = ...,
            sourceFirewallPolicy: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            firewallPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, firewallPolicy: str, **kwargs: typing.Any
        ) -> FirewallPolicyHttpRequest: ...
        def getAssociation(
            self,
            *,
            project: str,
            firewallPolicy: str,
            name: str = ...,
            **kwargs: typing.Any
        ) -> FirewallPolicyAssociationHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getRule(
            self,
            *,
            project: str,
            firewallPolicy: str,
            priority: int = ...,
            **kwargs: typing.Any
        ) -> FirewallPolicyRuleHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: FirewallPolicy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> FirewallPolicyListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            firewallPolicy: str,
            body: FirewallPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchRule(
            self,
            *,
            project: str,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            priority: int = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeAssociation(
            self,
            *,
            project: str,
            firewallPolicy: str,
            name: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeRule(
            self,
            *,
            project: str,
            firewallPolicy: str,
            priority: int = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class NetworksResource(googleapiclient.discovery.Resource):
        def addPeering(
            self,
            *,
            project: str,
            network: str,
            body: NetworksAddPeeringRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            network: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, network: str, **kwargs: typing.Any
        ) -> NetworkHttpRequest: ...
        def getEffectiveFirewalls(
            self, *, project: str, network: str, **kwargs: typing.Any
        ) -> NetworksGetEffectiveFirewallsResponseHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Network = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkListHttpRequest: ...
        def listIpAddresses(
            self,
            *,
            project: str,
            network: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            types: str = ...,
            **kwargs: typing.Any
        ) -> IpAddressesListHttpRequest: ...
        def listIpOwners(
            self,
            *,
            project: str,
            network: str,
            filter: str = ...,
            ipCidrRange: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            ownerProjects: str = ...,
            ownerTypes: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            subnetName: str = ...,
            subnetRegion: str = ...,
            **kwargs: typing.Any
        ) -> IpOwnerListHttpRequest: ...
        def listPeeringRoutes(
            self,
            *,
            project: str,
            network: str,
            direction: typing_extensions.Literal["INCOMING", "OUTGOING"] = ...,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            peeringName: str = ...,
            region: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ExchangedPeeringRoutesListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            network: str,
            body: Network = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removePeering(
            self,
            *,
            project: str,
            network: str,
            body: NetworksRemovePeeringRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def switchToCustomMode(
            self,
            *,
            project: str,
            network: str,
            requestId: str = ...,
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
        def updatePeering(
            self,
            *,
            project: str,
            network: str,
            body: NetworksUpdatePeeringRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class NodeGroupsResource(googleapiclient.discovery.Resource):
        def addNodes(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            body: NodeGroupsAddNodesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeGroupAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteNodes(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            body: NodeGroupsDeleteNodesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, nodeGroup: str, **kwargs: typing.Any
        ) -> NodeGroupHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            initialNodeCount: int,
            body: NodeGroup = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeGroupListHttpRequest: ...
        def listNodes(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeGroupsListNodesHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            body: NodeGroup = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setNodeTemplate(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            body: NodeGroupsSetNodeTemplateRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class NodeTemplatesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeTemplateAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            nodeTemplate: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, nodeTemplate: str, **kwargs: typing.Any
        ) -> NodeTemplateHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: NodeTemplate = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeTemplateListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class NodeTypesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeTypeAggregatedListHttpRequest: ...
        def get(
            self, *, project: str, zone: str, nodeType: str, **kwargs: typing.Any
        ) -> NodeTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NodeTypeListHttpRequest: ...
    class OrganizationSecurityPoliciesResource(googleapiclient.discovery.Resource):
        def addAssociation(
            self,
            *,
            securityPolicy: str,
            body: SecurityPolicyAssociation = ...,
            replaceExistingAssociation: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addRule(
            self,
            *,
            securityPolicy: str,
            body: SecurityPolicyRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def copyRules(
            self,
            *,
            securityPolicy: str,
            requestId: str = ...,
            sourceSecurityPolicy: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, securityPolicy: str, requestId: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, securityPolicy: str, **kwargs: typing.Any
        ) -> SecurityPolicyHttpRequest: ...
        def getAssociation(
            self, *, securityPolicy: str, name: str = ..., **kwargs: typing.Any
        ) -> SecurityPolicyAssociationHttpRequest: ...
        def getRule(
            self, *, securityPolicy: str, priority: int = ..., **kwargs: typing.Any
        ) -> SecurityPolicyRuleHttpRequest: ...
        def insert(
            self,
            *,
            body: SecurityPolicy = ...,
            parentId: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            parentId: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SecurityPolicyListHttpRequest: ...
        def listAssociations(
            self, *, targetResource: str = ..., **kwargs: typing.Any
        ) -> OrganizationSecurityPoliciesListAssociationsResponseHttpRequest: ...
        def move(
            self,
            *,
            securityPolicy: str,
            parentId: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            securityPolicy: str,
            body: SecurityPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchRule(
            self,
            *,
            securityPolicy: str,
            body: SecurityPolicyRule = ...,
            priority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeAssociation(
            self,
            *,
            securityPolicy: str,
            name: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeRule(
            self,
            *,
            securityPolicy: str,
            priority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class PacketMirroringsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PacketMirroringAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            packetMirroring: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            packetMirroring: str,
            **kwargs: typing.Any
        ) -> PacketMirroringHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: PacketMirroring = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PacketMirroringListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            packetMirroring: str,
            body: PacketMirroring = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        def disableXpnHost(
            self, *, project: str, requestId: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def disableXpnResource(
            self,
            *,
            project: str,
            body: ProjectsDisableXpnResourceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enableXpnHost(
            self, *, project: str, requestId: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enableXpnResource(
            self,
            *,
            project: str,
            body: ProjectsEnableXpnResourceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, project: str, **kwargs: typing.Any) -> ProjectHttpRequest: ...
        def getXpnHost(
            self, *, project: str, **kwargs: typing.Any
        ) -> ProjectHttpRequest: ...
        def getXpnResources(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ProjectsGetXpnResourcesHttpRequest: ...
        def listXpnHosts(
            self,
            *,
            project: str,
            body: ProjectsListXpnHostsRequest = ...,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> XpnHostListHttpRequest: ...
        def moveDisk(
            self,
            *,
            project: str,
            body: DiskMoveRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def moveInstance(
            self,
            *,
            project: str,
            body: InstanceMoveRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setCommonInstanceMetadata(
            self,
            *,
            project: str,
            body: Metadata = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setDefaultNetworkTier(
            self,
            *,
            project: str,
            body: ProjectsSetDefaultNetworkTierRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setDefaultServiceAccount(
            self,
            *,
            project: str,
            body: ProjectsSetDefaultServiceAccountRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setUsageExportBucket(
            self,
            *,
            project: str,
            body: UsageExportLocation = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class PublicAdvertisedPrefixesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            publicAdvertisedPrefix: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, publicAdvertisedPrefix: str, **kwargs: typing.Any
        ) -> PublicAdvertisedPrefixHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: PublicAdvertisedPrefix = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PublicAdvertisedPrefixListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            publicAdvertisedPrefix: str,
            body: PublicAdvertisedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class PublicDelegatedPrefixesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PublicDelegatedPrefixAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            publicDelegatedPrefix: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            publicDelegatedPrefix: str,
            **kwargs: typing.Any
        ) -> PublicDelegatedPrefixHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: PublicDelegatedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> PublicDelegatedPrefixListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            publicDelegatedPrefix: str,
            body: PublicDelegatedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionAutoscalersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            autoscaler: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, autoscaler: str, **kwargs: typing.Any
        ) -> AutoscalerHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Autoscaler = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionAutoscalerListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            body: Autoscaler = ...,
            autoscaler: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            body: Autoscaler = ...,
            autoscaler: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionBackendServicesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            backendService: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            backendService: str,
            **kwargs: typing.Any
        ) -> BackendServiceHttpRequest: ...
        def getHealth(
            self,
            *,
            project: str,
            region: str,
            backendService: str,
            body: ResourceGroupReference = ...,
            **kwargs: typing.Any
        ) -> BackendServiceGroupHealthHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> BackendServiceListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            backendService: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            backendService: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionCommitmentsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> CommitmentAggregatedListHttpRequest: ...
        def get(
            self, *, project: str, region: str, commitment: str, **kwargs: typing.Any
        ) -> CommitmentHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Commitment = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> CommitmentListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def updateReservations(
            self,
            *,
            project: str,
            region: str,
            commitment: str,
            body: RegionCommitmentsUpdateReservationsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionDiskTypesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, region: str, diskType: str, **kwargs: typing.Any
        ) -> DiskTypeHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionDiskTypeListHttpRequest: ...
    class RegionDisksResource(googleapiclient.discovery.Resource):
        def addResourcePolicies(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            body: RegionDisksAddResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def createSnapshot(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            body: Snapshot = ...,
            guestFlush: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, disk: str, **kwargs: typing.Any
        ) -> DiskHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Disk = ...,
            requestId: str = ...,
            sourceImage: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> DiskListHttpRequest: ...
        def removeResourcePolicies(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            body: RegionDisksRemoveResourcePoliciesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resize(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            body: RegionDisksResizeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionHealthCheckServicesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            healthCheckService: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            healthCheckService: str,
            **kwargs: typing.Any
        ) -> HealthCheckServiceHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: HealthCheckService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HealthCheckServicesListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            healthCheckService: str,
            body: HealthCheckService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionHealthChecksResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            healthCheck: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, healthCheck: str, **kwargs: typing.Any
        ) -> HealthCheckHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: HealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> HealthCheckListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            healthCheck: str,
            body: HealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            healthCheck: str,
            body: HealthCheck = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionInPlaceSnapshotsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            inPlaceSnapshot: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            inPlaceSnapshot: str,
            **kwargs: typing.Any
        ) -> InPlaceSnapshotHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: InPlaceSnapshot = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InPlaceSnapshotListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionInstanceGroupManagersResource(googleapiclient.discovery.Resource):
        def abandonInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersAbandonInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def applyUpdatesToInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersApplyUpdatesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def createInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersCreateInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deleteInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersDeleteInstancesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def deletePerInstanceConfigs(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagerDeleteInstanceConfigReq = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            **kwargs: typing.Any
        ) -> InstanceGroupManagerHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupManagerListHttpRequest: ...
        def listErrors(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupManagersListErrorsResponseHttpRequest: ...
        def listManagedInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupManagersListInstancesResponseHttpRequest: ...
        def listPerInstanceConfigs(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupManagersListInstanceConfigsRespHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchPerInstanceConfigs(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagerPatchInstanceConfigReq = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def recreateInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersRecreateRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def resize(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            size: int,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setAutoHealingPolicies(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersSetAutoHealingRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setInstanceTemplate(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersSetTemplateRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setTargetPools(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersSetTargetPoolsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: InstanceGroupManager = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def updatePerInstanceConfigs(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagerUpdateInstanceConfigReq = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionInstanceGroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, region: str, instanceGroup: str, **kwargs: typing.Any
        ) -> InstanceGroupHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupListHttpRequest: ...
        def listInstances(
            self,
            *,
            project: str,
            region: str,
            instanceGroup: str,
            body: RegionInstanceGroupsListInstancesRequest = ...,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionInstanceGroupsListInstancesHttpRequest: ...
        def setNamedPorts(
            self,
            *,
            project: str,
            region: str,
            instanceGroup: str,
            body: RegionInstanceGroupsSetNamedPortsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionInstancesResource(googleapiclient.discovery.Resource):
        def bulkInsert(
            self,
            *,
            project: str,
            region: str,
            body: BulkInsertInstanceResource = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionInstantSnapshotsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            instantSnapshot: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            instantSnapshot: str,
            **kwargs: typing.Any
        ) -> InstantSnapshotHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: InstantSnapshot = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstantSnapshotListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionNetworkEndpointGroupsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            networkEndpointGroup: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            networkEndpointGroup: str,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: NetworkEndpointGroup = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NetworkEndpointGroupListHttpRequest: ...
    class RegionNotificationEndpointsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            notificationEndpoint: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            notificationEndpoint: str,
            **kwargs: typing.Any
        ) -> NotificationEndpointHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: NotificationEndpoint = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> NotificationEndpointListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionOperationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, region: str, operation: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, project: str, region: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> OperationListHttpRequest: ...
        def wait(
            self, *, project: str, region: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RegionSslCertificatesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            sslCertificate: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            sslCertificate: str,
            **kwargs: typing.Any
        ) -> SslCertificateHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: SslCertificate = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SslCertificateListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionTargetHttpProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            targetHttpProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            targetHttpProxy: str,
            **kwargs: typing.Any
        ) -> TargetHttpProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: TargetHttpProxy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpProxyListHttpRequest: ...
        def setUrlMap(
            self,
            *,
            project: str,
            region: str,
            targetHttpProxy: str,
            body: UrlMapReference = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionTargetHttpsProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            targetHttpsProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            targetHttpsProxy: str,
            **kwargs: typing.Any
        ) -> TargetHttpsProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: TargetHttpsProxy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpsProxyListHttpRequest: ...
        def setSslCertificates(
            self,
            *,
            project: str,
            region: str,
            targetHttpsProxy: str,
            body: RegionTargetHttpsProxiesSetSslCertificatesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setUrlMap(
            self,
            *,
            project: str,
            region: str,
            targetHttpsProxy: str,
            body: UrlMapReference = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RegionUrlMapsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            urlMap: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, urlMap: str, **kwargs: typing.Any
        ) -> UrlMapHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: UrlMap = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def invalidateCache(
            self,
            *,
            project: str,
            region: str,
            urlMap: str,
            body: CacheInvalidationRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> UrlMapListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            urlMap: str,
            body: UrlMap = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            urlMap: str,
            body: UrlMap = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def validate(
            self,
            *,
            project: str,
            region: str,
            urlMap: str,
            body: RegionUrlMapsValidateRequest = ...,
            **kwargs: typing.Any
        ) -> UrlMapsValidateResponseHttpRequest: ...
    class RegionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, region: str, **kwargs: typing.Any
        ) -> RegionHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RegionListHttpRequest: ...
    class ReservationsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ReservationAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            reservation: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, reservation: str, **kwargs: typing.Any
        ) -> ReservationHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: Reservation = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ReservationListHttpRequest: ...
        def resize(
            self,
            *,
            project: str,
            zone: str,
            reservation: str,
            body: ReservationsResizeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ResourcePoliciesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ResourcePolicyAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            resourcePolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            resourcePolicy: str,
            **kwargs: typing.Any
        ) -> ResourcePolicyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: ResourcePolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ResourcePolicyListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class RoutersResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RouterAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            router: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, router: str, **kwargs: typing.Any
        ) -> RouterHttpRequest: ...
        def getNatMappingInfo(
            self,
            *,
            project: str,
            region: str,
            router: str,
            filter: str = ...,
            maxResults: int = ...,
            natName: str = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> VmEndpointNatMappingsListHttpRequest: ...
        def getRouterStatus(
            self, *, project: str, region: str, router: str, **kwargs: typing.Any
        ) -> RouterStatusResponseHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Router = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RouterListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            router: str,
            body: Router = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def preview(
            self,
            *,
            project: str,
            region: str,
            router: str,
            body: Router = ...,
            **kwargs: typing.Any
        ) -> RoutersPreviewResponseHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            project: str,
            region: str,
            router: str,
            body: Router = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class RoutesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            route: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, route: str, **kwargs: typing.Any
        ) -> RouteHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Route = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> RouteListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class SecurityPoliciesResource(googleapiclient.discovery.Resource):
        def addRule(
            self,
            *,
            project: str,
            securityPolicy: str,
            body: SecurityPolicyRule = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            securityPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, securityPolicy: str, **kwargs: typing.Any
        ) -> SecurityPolicyHttpRequest: ...
        def getRule(
            self,
            *,
            project: str,
            securityPolicy: str,
            priority: int = ...,
            **kwargs: typing.Any
        ) -> SecurityPolicyRuleHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: SecurityPolicy = ...,
            requestId: str = ...,
            validateOnly: bool = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SecurityPolicyListHttpRequest: ...
        def listPreconfiguredExpressionSets(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SecurityPoliciesListPreconfiguredExpressionSetsResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            securityPolicy: str,
            body: SecurityPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchRule(
            self,
            *,
            project: str,
            securityPolicy: str,
            body: SecurityPolicyRule = ...,
            priority: int = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeRule(
            self,
            *,
            project: str,
            securityPolicy: str,
            priority: int = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class ServiceAttachmentsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            serviceAttachment: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            serviceAttachment: str,
            **kwargs: typing.Any
        ) -> ServiceAttachmentHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: ServiceAttachment = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ServiceAttachmentListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class SnapshotsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            snapshot: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, snapshot: str, **kwargs: typing.Any
        ) -> SnapshotHttpRequest: ...
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
            body: Snapshot = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SnapshotListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            resource: str,
            body: GlobalSetLabelsRequest = ...,
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
    class SslCertificatesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SslCertificateAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            sslCertificate: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, sslCertificate: str, **kwargs: typing.Any
        ) -> SslCertificateHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: SslCertificate = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SslCertificateListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class SslPoliciesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            sslPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, sslPolicy: str, **kwargs: typing.Any
        ) -> SslPolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: SslPolicy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SslPoliciesListHttpRequest: ...
        def listAvailableFeatures(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SslPoliciesListAvailableFeaturesResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            sslPolicy: str,
            body: SslPolicy = ...,
            requestId: str = ...,
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
    class SubnetworksResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SubnetworkAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            subnetwork: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def expandIpCidrRange(
            self,
            *,
            project: str,
            region: str,
            subnetwork: str,
            body: SubnetworksExpandIpCidrRangeRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, subnetwork: str, **kwargs: typing.Any
        ) -> SubnetworkHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: Subnetwork = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> SubnetworkListHttpRequest: ...
        def listUsable(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> UsableSubnetworksAggregatedListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            subnetwork: str,
            body: Subnetwork = ...,
            drainTimeoutSeconds: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setPrivateIpGoogleAccess(
            self,
            *,
            project: str,
            region: str,
            subnetwork: str,
            body: SubnetworksSetPrivateIpGoogleAccessRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class TargetGrpcProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            targetGrpcProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, targetGrpcProxy: str, **kwargs: typing.Any
        ) -> TargetGrpcProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TargetGrpcProxy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetGrpcProxyListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            targetGrpcProxy: str,
            body: TargetGrpcProxy = ...,
            requestId: str = ...,
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
    class TargetHttpProxiesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpProxyAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            targetHttpProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, targetHttpProxy: str, **kwargs: typing.Any
        ) -> TargetHttpProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TargetHttpProxy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpProxyListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            targetHttpProxy: str,
            body: TargetHttpProxy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setUrlMap(
            self,
            *,
            project: str,
            targetHttpProxy: str,
            body: UrlMapReference = ...,
            requestId: str = ...,
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
    class TargetHttpsProxiesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpsProxyAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, targetHttpsProxy: str, **kwargs: typing.Any
        ) -> TargetHttpsProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TargetHttpsProxy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetHttpsProxyListHttpRequest: ...
        def setCertificateMap(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: TargetHttpsProxiesSetCertificateMapRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setQuicOverride(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: TargetHttpsProxiesSetQuicOverrideRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setSslCertificates(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: TargetHttpsProxiesSetSslCertificatesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setSslPolicy(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: SslPolicyReference = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setUrlMap(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: UrlMapReference = ...,
            requestId: str = ...,
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
    class TargetInstancesResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetInstanceAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            zone: str,
            targetInstance: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, targetInstance: str, **kwargs: typing.Any
        ) -> TargetInstanceHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: TargetInstance = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetInstanceListHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class TargetPoolsResource(googleapiclient.discovery.Resource):
        def addHealthCheck(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: TargetPoolsAddHealthCheckRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addInstance(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: TargetPoolsAddInstanceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetPoolAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, targetPool: str, **kwargs: typing.Any
        ) -> TargetPoolHttpRequest: ...
        def getHealth(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: InstanceReference = ...,
            **kwargs: typing.Any
        ) -> TargetPoolInstanceHealthHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: TargetPool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetPoolListHttpRequest: ...
        def removeHealthCheck(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: TargetPoolsRemoveHealthCheckRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeInstance(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: TargetPoolsRemoveInstanceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setBackup(
            self,
            *,
            project: str,
            region: str,
            targetPool: str,
            body: TargetReference = ...,
            failoverRatio: float = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class TargetSslProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            targetSslProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, targetSslProxy: str, **kwargs: typing.Any
        ) -> TargetSslProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TargetSslProxy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetSslProxyListHttpRequest: ...
        def setBackendService(
            self,
            *,
            project: str,
            targetSslProxy: str,
            body: TargetSslProxiesSetBackendServiceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setCertificateMap(
            self,
            *,
            project: str,
            targetSslProxy: str,
            body: TargetSslProxiesSetCertificateMapRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setProxyHeader(
            self,
            *,
            project: str,
            targetSslProxy: str,
            body: TargetSslProxiesSetProxyHeaderRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setSslCertificates(
            self,
            *,
            project: str,
            targetSslProxy: str,
            body: TargetSslProxiesSetSslCertificatesRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setSslPolicy(
            self,
            *,
            project: str,
            targetSslProxy: str,
            body: SslPolicyReference = ...,
            requestId: str = ...,
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
    class TargetTcpProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            targetTcpProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, targetTcpProxy: str, **kwargs: typing.Any
        ) -> TargetTcpProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: TargetTcpProxy = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetTcpProxyListHttpRequest: ...
        def setBackendService(
            self,
            *,
            project: str,
            targetTcpProxy: str,
            body: TargetTcpProxiesSetBackendServiceRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setProxyHeader(
            self,
            *,
            project: str,
            targetTcpProxy: str,
            body: TargetTcpProxiesSetProxyHeaderRequest = ...,
            requestId: str = ...,
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
    class TargetVpnGatewaysResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetVpnGatewayAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            targetVpnGateway: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            targetVpnGateway: str,
            **kwargs: typing.Any
        ) -> TargetVpnGatewayHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: TargetVpnGateway = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> TargetVpnGatewayListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class UrlMapsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> UrlMapsAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            urlMap: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, urlMap: str, **kwargs: typing.Any
        ) -> UrlMapHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: UrlMap = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def invalidateCache(
            self,
            *,
            project: str,
            urlMap: str,
            body: CacheInvalidationRule = ...,
            requestId: str = ...,
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
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> UrlMapListHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            urlMap: str,
            body: UrlMap = ...,
            requestId: str = ...,
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
            urlMap: str,
            body: UrlMap = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def validate(
            self,
            *,
            project: str,
            urlMap: str,
            body: UrlMapsValidateRequest = ...,
            **kwargs: typing.Any
        ) -> UrlMapsValidateResponseHttpRequest: ...
    class VpnGatewaysResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> VpnGatewayAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            vpnGateway: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, vpnGateway: str, **kwargs: typing.Any
        ) -> VpnGatewayHttpRequest: ...
        def getStatus(
            self, *, project: str, region: str, vpnGateway: str, **kwargs: typing.Any
        ) -> VpnGatewaysGetStatusResponseHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: VpnGateway = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> VpnGatewayListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class VpnTunnelsResource(googleapiclient.discovery.Resource):
        def aggregatedList(
            self,
            *,
            project: str,
            filter: str = ...,
            includeAllScopes: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> VpnTunnelAggregatedListHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            vpnTunnel: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, vpnTunnel: str, **kwargs: typing.Any
        ) -> VpnTunnelHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: VpnTunnel = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            region: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> VpnTunnelListHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: RegionSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ZoneInPlaceSnapshotsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            zone: str,
            inPlaceSnapshot: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, inPlaceSnapshot: str, **kwargs: typing.Any
        ) -> InPlaceSnapshotHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: InPlaceSnapshot = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InPlaceSnapshotListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ZoneInstantSnapshotsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            zone: str,
            instantSnapshot: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, zone: str, instantSnapshot: str, **kwargs: typing.Any
        ) -> InstantSnapshotHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            zone: str,
            body: InstantSnapshot = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> InstantSnapshotListHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def setLabels(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: ZoneSetLabelsRequest = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...
    class ZoneOperationsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, project: str, zone: str, operation: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, project: str, zone: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            zone: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> OperationListHttpRequest: ...
        def wait(
            self, *, project: str, zone: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ZonesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, zone: str, **kwargs: typing.Any
        ) -> ZoneHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            **kwargs: typing.Any
        ) -> ZoneListHttpRequest: ...
    def acceleratorTypes(self) -> AcceleratorTypesResource: ...
    def addresses(self) -> AddressesResource: ...
    def autoscalers(self) -> AutoscalersResource: ...
    def backendBuckets(self) -> BackendBucketsResource: ...
    def backendServices(self) -> BackendServicesResource: ...
    def diskTypes(self) -> DiskTypesResource: ...
    def disks(self) -> DisksResource: ...
    def externalVpnGateways(self) -> ExternalVpnGatewaysResource: ...
    def firewalls(self) -> FirewallsResource: ...
    def forwardingRules(self) -> ForwardingRulesResource: ...
    def globalAddresses(self) -> GlobalAddressesResource: ...
    def globalForwardingRules(self) -> GlobalForwardingRulesResource: ...
    def globalNetworkEndpointGroups(self) -> GlobalNetworkEndpointGroupsResource: ...
    def globalOperations(self) -> GlobalOperationsResource: ...
    def globalOrganizationOperations(self) -> GlobalOrganizationOperationsResource: ...
    def globalPublicDelegatedPrefixes(
        self,
    ) -> GlobalPublicDelegatedPrefixesResource: ...
    def healthChecks(self) -> HealthChecksResource: ...
    def httpHealthChecks(self) -> HttpHealthChecksResource: ...
    def httpsHealthChecks(self) -> HttpsHealthChecksResource: ...
    def images(self) -> ImagesResource: ...
    def instanceGroupManagers(self) -> InstanceGroupManagersResource: ...
    def instanceGroups(self) -> InstanceGroupsResource: ...
    def instanceTemplates(self) -> InstanceTemplatesResource: ...
    def instances(self) -> InstancesResource: ...
    def interconnectAttachments(self) -> InterconnectAttachmentsResource: ...
    def interconnectLocations(self) -> InterconnectLocationsResource: ...
    def interconnects(self) -> InterconnectsResource: ...
    def licenseCodes(self) -> LicenseCodesResource: ...
    def licenses(self) -> LicensesResource: ...
    def machineImages(self) -> MachineImagesResource: ...
    def machineTypes(self) -> MachineTypesResource: ...
    def networkEndpointGroups(self) -> NetworkEndpointGroupsResource: ...
    def networkFirewallPolicies(self) -> NetworkFirewallPoliciesResource: ...
    def networks(self) -> NetworksResource: ...
    def nodeGroups(self) -> NodeGroupsResource: ...
    def nodeTemplates(self) -> NodeTemplatesResource: ...
    def nodeTypes(self) -> NodeTypesResource: ...
    def organizationSecurityPolicies(self) -> OrganizationSecurityPoliciesResource: ...
    def packetMirrorings(self) -> PacketMirroringsResource: ...
    def projects(self) -> ProjectsResource: ...
    def publicAdvertisedPrefixes(self) -> PublicAdvertisedPrefixesResource: ...
    def publicDelegatedPrefixes(self) -> PublicDelegatedPrefixesResource: ...
    def regionAutoscalers(self) -> RegionAutoscalersResource: ...
    def regionBackendServices(self) -> RegionBackendServicesResource: ...
    def regionCommitments(self) -> RegionCommitmentsResource: ...
    def regionDiskTypes(self) -> RegionDiskTypesResource: ...
    def regionDisks(self) -> RegionDisksResource: ...
    def regionHealthCheckServices(self) -> RegionHealthCheckServicesResource: ...
    def regionHealthChecks(self) -> RegionHealthChecksResource: ...
    def regionInPlaceSnapshots(self) -> RegionInPlaceSnapshotsResource: ...
    def regionInstanceGroupManagers(self) -> RegionInstanceGroupManagersResource: ...
    def regionInstanceGroups(self) -> RegionInstanceGroupsResource: ...
    def regionInstances(self) -> RegionInstancesResource: ...
    def regionInstantSnapshots(self) -> RegionInstantSnapshotsResource: ...
    def regionNetworkEndpointGroups(self) -> RegionNetworkEndpointGroupsResource: ...
    def regionNotificationEndpoints(self) -> RegionNotificationEndpointsResource: ...
    def regionOperations(self) -> RegionOperationsResource: ...
    def regionSslCertificates(self) -> RegionSslCertificatesResource: ...
    def regionTargetHttpProxies(self) -> RegionTargetHttpProxiesResource: ...
    def regionTargetHttpsProxies(self) -> RegionTargetHttpsProxiesResource: ...
    def regionUrlMaps(self) -> RegionUrlMapsResource: ...
    def regions(self) -> RegionsResource: ...
    def reservations(self) -> ReservationsResource: ...
    def resourcePolicies(self) -> ResourcePoliciesResource: ...
    def routers(self) -> RoutersResource: ...
    def routes(self) -> RoutesResource: ...
    def securityPolicies(self) -> SecurityPoliciesResource: ...
    def serviceAttachments(self) -> ServiceAttachmentsResource: ...
    def snapshots(self) -> SnapshotsResource: ...
    def sslCertificates(self) -> SslCertificatesResource: ...
    def sslPolicies(self) -> SslPoliciesResource: ...
    def subnetworks(self) -> SubnetworksResource: ...
    def targetGrpcProxies(self) -> TargetGrpcProxiesResource: ...
    def targetHttpProxies(self) -> TargetHttpProxiesResource: ...
    def targetHttpsProxies(self) -> TargetHttpsProxiesResource: ...
    def targetInstances(self) -> TargetInstancesResource: ...
    def targetPools(self) -> TargetPoolsResource: ...
    def targetSslProxies(self) -> TargetSslProxiesResource: ...
    def targetTcpProxies(self) -> TargetTcpProxiesResource: ...
    def targetVpnGateways(self) -> TargetVpnGatewaysResource: ...
    def urlMaps(self) -> UrlMapsResource: ...
    def vpnGateways(self) -> VpnGatewaysResource: ...
    def vpnTunnels(self) -> VpnTunnelsResource: ...
    def zoneInPlaceSnapshots(self) -> ZoneInPlaceSnapshotsResource: ...
    def zoneInstantSnapshots(self) -> ZoneInstantSnapshotsResource: ...
    def zoneOperations(self) -> ZoneOperationsResource: ...
    def zones(self) -> ZonesResource: ...

class RouterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Router: ...

class NetworkEndpointGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworkEndpointGroupList: ...

class ResourcePolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcePolicyList: ...

class InPlaceSnapshotListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InPlaceSnapshotList: ...

class NetworkEndpointGroupsListNetworkEndpointsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworkEndpointGroupsListNetworkEndpoints: ...

class InstanceGroupManagerAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManagerAggregatedList: ...

class SecurityPolicyRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityPolicyRule: ...

class TargetGrpcProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetGrpcProxyList: ...

class TargetInstanceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetInstanceAggregatedList: ...

class PublicDelegatedPrefixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicDelegatedPrefix: ...

class BackendServiceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendServiceList: ...

class SslCertificateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCertificateList: ...

class ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Zone: ...

class TargetGrpcProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetGrpcProxy: ...

class TargetSslProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetSslProxyList: ...

class MachineTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MachineType: ...

class FirewallPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallPolicy: ...

class RegionInstanceGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupList: ...

class VpnTunnelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnTunnel: ...

class NodeTemplateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeTemplateList: ...

class TargetSslProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetSslProxy: ...

class NodeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeType: ...

class SubnetworkListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubnetworkList: ...

class PublicAdvertisedPrefixListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicAdvertisedPrefixList: ...

class NodeTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeTemplate: ...

class VpnGatewaysGetStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnGatewaysGetStatusResponse: ...

class GetOwnerInstanceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOwnerInstanceResponse: ...

class InstanceListReferrersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceListReferrers: ...

class BackendServiceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendServiceAggregatedList: ...

class PacketMirroringAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PacketMirroringAggregatedList: ...

class InstanceTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceTemplate: ...

class InstanceGroupManagerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManagerList: ...

class RoutersPreviewResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RoutersPreviewResponse: ...

class NotificationEndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NotificationEndpoint: ...

class TargetHttpProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpProxyList: ...

class TargetHttpProxyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpProxyAggregatedList: ...

class ServiceAttachmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceAttachmentList: ...

class DiskTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DiskType: ...

class ImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Image: ...

class InstanceGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupList: ...

class ExchangedPeeringRoutesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExchangedPeeringRoutesList: ...

class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Snapshot: ...

class ForwardingRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ForwardingRule: ...

class ScreenshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Screenshot: ...

class RouteListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RouteList: ...

class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestPermissionsResponse: ...

class ForwardingRuleListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ForwardingRuleList: ...

class BackendServiceGroupHealthHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendServiceGroupHealth: ...

class TargetVpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetVpnGatewayList: ...

class TargetPoolListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetPoolList: ...

class NetworkEndpointGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworkEndpointGroupAggregatedList: ...

class TargetTcpProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetTcpProxyList: ...

class RouterAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RouterAggregatedList: ...

class DiskTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DiskTypeAggregatedList: ...

class UrlMapsAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlMapsAggregatedList: ...

class InstanceGroupsListInstancesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupsListInstances: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ShieldedInstanceIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShieldedInstanceIdentity: ...

class ImageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ImageList: ...

class IpOwnerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IpOwnerList: ...

class AddressAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddressAggregatedList: ...

class UrlMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlMap: ...

class VpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnGateway: ...

class RegionInstanceGroupManagersListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupManagersListInstancesResponse: ...

class RouterStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RouterStatusResponse: ...

class IpAddressesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IpAddressesList: ...

class NodeTemplateAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeTemplateAggregatedList: ...

class InstantSnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstantSnapshot: ...

class SerialPortOutputHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SerialPortOutput: ...

class TargetInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetInstance: ...

class OrganizationSecurityPoliciesListAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OrganizationSecurityPoliciesListAssociationsResponse: ...

class TargetTcpProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetTcpProxy: ...

class MachineImageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MachineImageList: ...

class NetworksGetEffectiveFirewallsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworksGetEffectiveFirewallsResponse: ...

class LicensesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LicensesListResponse: ...

class InterconnectLocationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectLocationList: ...

class MachineImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MachineImage: ...

class NodeGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeGroupList: ...

class PublicDelegatedPrefixAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicDelegatedPrefixAggregatedList: ...

class RegionDiskTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionDiskTypeList: ...

class AutoscalerAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AutoscalerAggregatedList: ...

class SubnetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Subnetwork: ...

class MachineTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MachineTypeAggregatedList: ...

class HttpsHealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpsHealthCheck: ...

class InterconnectLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectLocation: ...

class PublicAdvertisedPrefixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicAdvertisedPrefix: ...

class ResourcePolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcePolicy: ...

class FirewallHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Firewall: ...

class RegionInstanceGroupsListInstancesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupsListInstances: ...

class ForwardingRuleAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ForwardingRuleAggregatedList: ...

class RegionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Region: ...

class InstanceGroupManagersListManagedInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManagersListManagedInstancesResponse: ...

class UsableSubnetworksAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UsableSubnetworksAggregatedList: ...

class TargetInstanceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetInstanceList: ...

class RegionAutoscalerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionAutoscalerList: ...

class VpnGatewayAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnGatewayAggregatedList: ...

class DiskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Disk: ...

class SecurityPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityPolicy: ...

class NodeGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeGroup: ...

class SslCertificateAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCertificateAggregatedList: ...

class InstanceGroupManagerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManager: ...

class NetworkListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworkList: ...

class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Project: ...

class AcceleratorTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AcceleratorTypeList: ...

class ResourcePolicyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ResourcePolicyAggregatedList: ...

class ReservationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReservationList: ...

class OperationAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationAggregatedList: ...

class MachineTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> MachineTypeList: ...

class VpnTunnelListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnTunnelList: ...

class NodeGroupsListNodesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeGroupsListNodes: ...

class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Reservation: ...

class CommitmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommitmentAggregatedList: ...

class NetworkEndpointGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NetworkEndpointGroup: ...

class TargetVpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetVpnGateway: ...

class NodeTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeTypeAggregatedList: ...

class InterconnectAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectAttachment: ...

class InstanceGroupManagersListPerInstanceConfigsRespHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManagersListPerInstanceConfigsResp: ...

class AutoscalerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Autoscaler: ...

class InstanceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceList: ...

class FirewallPolicyAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallPolicyAssociation: ...

class InstanceGroupManagersListErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupManagersListErrorsResponse: ...

class InstanceGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroupAggregatedList: ...

class AddressListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddressList: ...

class TargetHttpsProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpsProxyList: ...

class ServiceAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceAttachment: ...

class ShieldedVmIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ShieldedVmIdentity: ...

class HttpHealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpHealthCheck: ...

class RegionInstanceGroupManagersListErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupManagersListErrorsResponse: ...

class FirewallPolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallPolicyList: ...

class SecurityPolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityPolicyList: ...

class InstancesGetEffectiveFirewallsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstancesGetEffectiveFirewallsResponse: ...

class PacketMirroringListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PacketMirroringList: ...

class AddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Address: ...

class GuestAttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GuestAttributes: ...

class ExternalVpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExternalVpnGateway: ...

class InstantSnapshotListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstantSnapshotList: ...

class DiskAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DiskAggregatedList: ...

class SnapshotListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SnapshotList: ...

class BackendServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendService: ...

class HealthCheckServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HealthCheckService: ...

class InstanceTemplateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceTemplateList: ...

class AcceleratorTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AcceleratorType: ...

class DiskListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DiskList: ...

class CommitmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommitmentList: ...

class HealthChecksAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HealthChecksAggregatedList: ...

class UrlMapsValidateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlMapsValidateResponse: ...

class VpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnGatewayList: ...

class HealthCheckServicesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HealthCheckServicesList: ...

class AcceleratorTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AcceleratorTypeAggregatedList: ...

class AutoscalerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AutoscalerList: ...

class InstanceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceAggregatedList: ...

class NetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Network: ...

class PacketMirroringHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PacketMirroring: ...

class SecurityPoliciesListPreconfiguredExpressionSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityPoliciesListPreconfiguredExpressionSetsResponse: ...

class RegionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionList: ...

class BackendBucketListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendBucketList: ...

class HttpsHealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpsHealthCheckList: ...

class NodeTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeTypeList: ...

class SslPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslPolicy: ...

class NotificationEndpointListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NotificationEndpointList: ...

class PublicDelegatedPrefixListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublicDelegatedPrefixList: ...

class RegionInstanceGroupManagerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupManagerList: ...

class TargetHttpProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpProxy: ...

class InterconnectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Interconnect: ...

class NodeGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> NodeGroupAggregatedList: ...

class SslPoliciesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslPoliciesList: ...

class BackendBucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BackendBucket: ...

class LicenseCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LicenseCode: ...

class TargetPoolInstanceHealthHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetPoolInstanceHealth: ...

class FirewallPolicyRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallPolicyRule: ...

class InterconnectAttachmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectAttachmentList: ...

class RegionInstanceGroupManagersListInstanceConfigsRespHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RegionInstanceGroupManagersListInstanceConfigsResp: ...

class TargetPoolAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetPoolAggregatedList: ...

class SslCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslCertificate: ...

class SslPoliciesListAvailableFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SslPoliciesListAvailableFeaturesResponse: ...

class TargetVpnGatewayAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetVpnGatewayAggregatedList: ...

class ExternalVpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ExternalVpnGatewayList: ...

class ReservationAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReservationAggregatedList: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class TargetHttpsProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpsProxy: ...

class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Route: ...

class TargetPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetPool: ...

class VpnTunnelAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VpnTunnelAggregatedList: ...

class RouterListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RouterList: ...

class InPlaceSnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InPlaceSnapshot: ...

class CommitmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Commitment: ...

class SubnetworkAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SubnetworkAggregatedList: ...

class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Instance: ...

class VmEndpointNatMappingsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VmEndpointNatMappingsList: ...

class HealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HealthCheckList: ...

class OperationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> OperationList: ...

class HealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HealthCheck: ...

class HttpHealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpHealthCheckList: ...

class SecurityPolicyAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SecurityPolicyAssociation: ...

class FirewallListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallList: ...

class UrlMapListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlMapList: ...

class InterconnectListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectList: ...

class InterconnectsGetDiagnosticsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectsGetDiagnosticsResponse: ...

class ProjectsGetXpnResourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProjectsGetXpnResources: ...

class ZoneListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ZoneList: ...

class XpnHostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> XpnHostList: ...

class TargetHttpsProxyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TargetHttpsProxyAggregatedList: ...

class InterconnectAttachmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InterconnectAttachmentAggregatedList: ...

class LicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> License: ...

class InstanceGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> InstanceGroup: ...

class DiskTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DiskTypeList: ...
