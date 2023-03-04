import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ComputeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: AcceleratorTypeAggregatedListHttpRequest,
            previous_response: AcceleratorTypeAggregatedList,
        ) -> AcceleratorTypeAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: AcceleratorTypeListHttpRequest,
            previous_response: AcceleratorTypeList,
        ) -> AcceleratorTypeListHttpRequest | None: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: AddressAggregatedListHttpRequest,
            previous_response: AddressAggregatedList,
        ) -> AddressAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: AddressListHttpRequest,
            previous_response: AddressList,
        ) -> AddressListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: AutoscalerAggregatedListHttpRequest,
            previous_response: AutoscalerAggregatedList,
        ) -> AutoscalerAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: AutoscalerListHttpRequest,
            previous_response: AutoscalerList,
        ) -> AutoscalerListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: BackendBucketListHttpRequest,
            previous_response: BackendBucketList,
        ) -> BackendBucketListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            backendBucket: str,
            body: BackendBucket = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setEdgeSecurityPolicy(
            self,
            *,
            project: str,
            backendBucket: str,
            body: SecurityPolicyReference = ...,
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: BackendServiceAggregatedListHttpRequest,
            previous_response: BackendServiceAggregatedList,
        ) -> BackendServiceAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: BackendServiceListHttpRequest,
            previous_response: BackendServiceList,
        ) -> BackendServiceListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            backendService: str,
            body: BackendService = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setEdgeSecurityPolicy(
            self,
            *,
            project: str,
            backendService: str,
            body: SecurityPolicyReference = ...,
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: DiskTypeAggregatedListHttpRequest,
            previous_response: DiskTypeAggregatedList,
        ) -> DiskTypeAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: DiskTypeListHttpRequest,
            previous_response: DiskTypeList,
        ) -> DiskTypeListHttpRequest | None: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: DiskAggregatedListHttpRequest,
            previous_response: DiskAggregatedList,
        ) -> DiskAggregatedListHttpRequest | None: ...
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
        def list_next(
            self, previous_request: DiskListHttpRequest, previous_response: DiskList
        ) -> DiskListHttpRequest | None: ...
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
        def update(
            self,
            *,
            project: str,
            zone: str,
            disk: str,
            body: Disk = ...,
            paths: str | _list[str] = ...,
            requestId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: ExternalVpnGatewayListHttpRequest,
            previous_response: ExternalVpnGatewayList,
        ) -> ExternalVpnGatewayListHttpRequest | None: ...
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

    @typing.type_check_only
    class FirewallPoliciesResource(googleapiclient.discovery.Resource):
        def addAssociation(
            self,
            *,
            firewallPolicy: str,
            body: FirewallPolicyAssociation = ...,
            replaceExistingAssociation: bool = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addRule(
            self,
            *,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def cloneRules(
            self,
            *,
            firewallPolicy: str,
            requestId: str = ...,
            sourceFirewallPolicy: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, firewallPolicy: str, requestId: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, firewallPolicy: str, **kwargs: typing.Any
        ) -> FirewallPolicyHttpRequest: ...
        def getAssociation(
            self, *, firewallPolicy: str, name: str = ..., **kwargs: typing.Any
        ) -> FirewallPolicyAssociationHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getRule(
            self, *, firewallPolicy: str, priority: int = ..., **kwargs: typing.Any
        ) -> FirewallPolicyRuleHttpRequest: ...
        def insert(
            self,
            *,
            body: FirewallPolicy = ...,
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
        ) -> FirewallPolicyListHttpRequest: ...
        def list_next(
            self,
            previous_request: FirewallPolicyListHttpRequest,
            previous_response: FirewallPolicyList,
        ) -> FirewallPolicyListHttpRequest | None: ...
        def listAssociations(
            self, *, targetResource: str = ..., **kwargs: typing.Any
        ) -> FirewallPoliciesListAssociationsResponseHttpRequest: ...
        def move(
            self,
            *,
            firewallPolicy: str,
            parentId: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            firewallPolicy: str,
            body: FirewallPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchRule(
            self,
            *,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            priority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeAssociation(
            self,
            *,
            firewallPolicy: str,
            name: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeRule(
            self,
            *,
            firewallPolicy: str,
            priority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: GlobalOrganizationSetPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: FirewallListHttpRequest,
            previous_response: FirewallList,
        ) -> FirewallListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: ForwardingRuleAggregatedListHttpRequest,
            previous_response: ForwardingRuleAggregatedList,
        ) -> ForwardingRuleAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: ForwardingRuleListHttpRequest,
            previous_response: ForwardingRuleList,
        ) -> ForwardingRuleListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: AddressListHttpRequest,
            previous_response: AddressList,
        ) -> AddressListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: ForwardingRuleListHttpRequest,
            previous_response: ForwardingRuleList,
        ) -> ForwardingRuleListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: NetworkEndpointGroupListHttpRequest,
            previous_response: NetworkEndpointGroupList,
        ) -> NetworkEndpointGroupListHttpRequest | None: ...
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
        def listNetworkEndpoints_next(
            self,
            previous_request: NetworkEndpointGroupsListNetworkEndpointsHttpRequest,
            previous_response: NetworkEndpointGroupsListNetworkEndpoints,
        ) -> NetworkEndpointGroupsListNetworkEndpointsHttpRequest | None: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: OperationAggregatedListHttpRequest,
            previous_response: OperationAggregatedList,
        ) -> OperationAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: OperationListHttpRequest,
            previous_response: OperationList,
        ) -> OperationListHttpRequest | None: ...
        def wait(
            self, *, project: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: OperationListHttpRequest,
            previous_response: OperationList,
        ) -> OperationListHttpRequest | None: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: PublicDelegatedPrefixListHttpRequest,
            previous_response: PublicDelegatedPrefixList,
        ) -> PublicDelegatedPrefixListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            publicDelegatedPrefix: str,
            body: PublicDelegatedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: HealthChecksAggregatedListHttpRequest,
            previous_response: HealthChecksAggregatedList,
        ) -> HealthChecksAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: HealthCheckListHttpRequest,
            previous_response: HealthCheckList,
        ) -> HealthCheckListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: HttpHealthCheckListHttpRequest,
            previous_response: HttpHealthCheckList,
        ) -> HttpHealthCheckListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: HttpsHealthCheckListHttpRequest,
            previous_response: HttpsHealthCheckList,
        ) -> HttpsHealthCheckListHttpRequest | None: ...
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

    @typing.type_check_only
    class ImageFamilyViewsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, zone: str, family: str, **kwargs: typing.Any
        ) -> ImageFamilyViewHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self, previous_request: ImageListHttpRequest, previous_response: ImageList
        ) -> ImageListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: InstanceGroupManagerAggregatedListHttpRequest,
            previous_response: InstanceGroupManagerAggregatedList,
        ) -> InstanceGroupManagerAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: InstanceGroupManagerListHttpRequest,
            previous_response: InstanceGroupManagerList,
        ) -> InstanceGroupManagerListHttpRequest | None: ...
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
        def listErrors_next(
            self,
            previous_request: InstanceGroupManagersListErrorsResponseHttpRequest,
            previous_response: InstanceGroupManagersListErrorsResponse,
        ) -> InstanceGroupManagersListErrorsResponseHttpRequest | None: ...
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
        def listManagedInstances_next(
            self,
            previous_request: InstanceGroupManagersListManagedInstancesResponseHttpRequest,
            previous_response: InstanceGroupManagersListManagedInstancesResponse,
        ) -> InstanceGroupManagersListManagedInstancesResponseHttpRequest | None: ...
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
        def listPerInstanceConfigs_next(
            self,
            previous_request: InstanceGroupManagersListPerInstanceConfigsRespHttpRequest,
            previous_response: InstanceGroupManagersListPerInstanceConfigsResp,
        ) -> InstanceGroupManagersListPerInstanceConfigsRespHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: InstanceGroupAggregatedListHttpRequest,
            previous_response: InstanceGroupAggregatedList,
        ) -> InstanceGroupAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: InstanceGroupListHttpRequest,
            previous_response: InstanceGroupList,
        ) -> InstanceGroupListHttpRequest | None: ...
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
        def listInstances_next(
            self,
            previous_request: InstanceGroupsListInstancesHttpRequest,
            previous_response: InstanceGroupsListInstances,
        ) -> InstanceGroupsListInstancesHttpRequest | None: ...
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

    @typing.type_check_only
    class InstanceTemplatesResource(googleapiclient.discovery.Resource):
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
        ) -> InstanceTemplateAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: InstanceTemplateAggregatedListHttpRequest,
            previous_response: InstanceTemplateAggregatedList,
        ) -> InstanceTemplateAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: InstanceTemplateListHttpRequest,
            previous_response: InstanceTemplateList,
        ) -> InstanceTemplateListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: InstanceAggregatedListHttpRequest,
            previous_response: InstanceAggregatedList,
        ) -> InstanceAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: InstanceListHttpRequest,
            previous_response: InstanceList,
        ) -> InstanceListHttpRequest | None: ...
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
        def listReferrers_next(
            self,
            previous_request: InstanceListReferrersHttpRequest,
            previous_response: InstanceListReferrers,
        ) -> InstanceListReferrersHttpRequest | None: ...
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
        def sendDiagnosticInterrupt(
            self, *, project: str, zone: str, instance: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: InterconnectAttachmentAggregatedListHttpRequest,
            previous_response: InterconnectAttachmentAggregatedList,
        ) -> InterconnectAttachmentAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: InterconnectAttachmentListHttpRequest,
            previous_response: InterconnectAttachmentList,
        ) -> InterconnectAttachmentListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: InterconnectLocationListHttpRequest,
            previous_response: InterconnectLocationList,
        ) -> InterconnectLocationListHttpRequest | None: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: InterconnectListHttpRequest,
            previous_response: InterconnectList,
        ) -> InterconnectListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            interconnect: str,
            body: Interconnect = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class LicenseCodesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, project: str, licenseCode: str, **kwargs: typing.Any
        ) -> LicenseCodeHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: LicensesListResponseHttpRequest,
            previous_response: LicensesListResponse,
        ) -> LicensesListResponseHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: MachineImageListHttpRequest,
            previous_response: MachineImageList,
        ) -> MachineImageListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: MachineTypeAggregatedListHttpRequest,
            previous_response: MachineTypeAggregatedList,
        ) -> MachineTypeAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: MachineTypeListHttpRequest,
            previous_response: MachineTypeList,
        ) -> MachineTypeListHttpRequest | None: ...

    @typing.type_check_only
    class NetworkAttachmentsResource(googleapiclient.discovery.Resource):
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
        ) -> NetworkAttachmentAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: NetworkAttachmentAggregatedListHttpRequest,
            previous_response: NetworkAttachmentAggregatedList,
        ) -> NetworkAttachmentAggregatedListHttpRequest | None: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            networkAttachment: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            networkAttachment: str,
            **kwargs: typing.Any
        ) -> NetworkAttachmentHttpRequest: ...
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
            body: NetworkAttachment = ...,
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
        ) -> NetworkAttachmentListHttpRequest: ...
        def list_next(
            self,
            previous_request: NetworkAttachmentListHttpRequest,
            previous_response: NetworkAttachmentList,
        ) -> NetworkAttachmentListHttpRequest | None: ...
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

    @typing.type_check_only
    class NetworkEdgeSecurityServicesResource(googleapiclient.discovery.Resource):
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
        ) -> NetworkEdgeSecurityServiceAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: NetworkEdgeSecurityServiceAggregatedListHttpRequest,
            previous_response: NetworkEdgeSecurityServiceAggregatedList,
        ) -> NetworkEdgeSecurityServiceAggregatedListHttpRequest | None: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            networkEdgeSecurityService: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            networkEdgeSecurityService: str,
            **kwargs: typing.Any
        ) -> NetworkEdgeSecurityServiceHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: NetworkEdgeSecurityService = ...,
            requestId: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            networkEdgeSecurityService: str,
            body: NetworkEdgeSecurityService = ...,
            paths: str | _list[str] = ...,
            requestId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: NetworkEndpointGroupAggregatedListHttpRequest,
            previous_response: NetworkEndpointGroupAggregatedList,
        ) -> NetworkEndpointGroupAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: NetworkEndpointGroupListHttpRequest,
            previous_response: NetworkEndpointGroupList,
        ) -> NetworkEndpointGroupListHttpRequest | None: ...
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
        def listNetworkEndpoints_next(
            self,
            previous_request: NetworkEndpointGroupsListNetworkEndpointsHttpRequest,
            previous_response: NetworkEndpointGroupsListNetworkEndpoints,
        ) -> NetworkEndpointGroupsListNetworkEndpointsHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
            maxPriority: int = ...,
            minPriority: int = ...,
            requestId: str = ...,
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
        def list_next(
            self,
            previous_request: FirewallPolicyListHttpRequest,
            previous_response: FirewallPolicyList,
        ) -> FirewallPolicyListHttpRequest | None: ...
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
            requestId: str = ...,
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: NetworkListHttpRequest,
            previous_response: NetworkList,
        ) -> NetworkListHttpRequest | None: ...
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
        def listPeeringRoutes_next(
            self,
            previous_request: ExchangedPeeringRoutesListHttpRequest,
            previous_response: ExchangedPeeringRoutesList,
        ) -> ExchangedPeeringRoutesListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: NodeGroupAggregatedListHttpRequest,
            previous_response: NodeGroupAggregatedList,
        ) -> NodeGroupAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: NodeGroupListHttpRequest,
            previous_response: NodeGroupList,
        ) -> NodeGroupListHttpRequest | None: ...
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
        def listNodes_next(
            self,
            previous_request: NodeGroupsListNodesHttpRequest,
            previous_response: NodeGroupsListNodes,
        ) -> NodeGroupsListNodesHttpRequest | None: ...
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
        def simulateMaintenanceEvent(
            self,
            *,
            project: str,
            zone: str,
            nodeGroup: str,
            body: NodeGroupsSimulateMaintenanceEventRequest = ...,
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: NodeTemplateAggregatedListHttpRequest,
            previous_response: NodeTemplateAggregatedList,
        ) -> NodeTemplateAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: NodeTemplateListHttpRequest,
            previous_response: NodeTemplateList,
        ) -> NodeTemplateListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: NodeTypeAggregatedListHttpRequest,
            previous_response: NodeTypeAggregatedList,
        ) -> NodeTypeAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: NodeTypeListHttpRequest,
            previous_response: NodeTypeList,
        ) -> NodeTypeListHttpRequest | None: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: SecurityPolicyListHttpRequest,
            previous_response: SecurityPolicyList,
        ) -> SecurityPolicyListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: PacketMirroringAggregatedListHttpRequest,
            previous_response: PacketMirroringAggregatedList,
        ) -> PacketMirroringAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: PacketMirroringListHttpRequest,
            previous_response: PacketMirroringList,
        ) -> PacketMirroringListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def getXpnResources_next(
            self,
            previous_request: ProjectsGetXpnResourcesHttpRequest,
            previous_response: ProjectsGetXpnResources,
        ) -> ProjectsGetXpnResourcesHttpRequest | None: ...
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
        def listXpnHosts_next(
            self,
            previous_request: XpnHostListHttpRequest,
            previous_response: XpnHostList,
        ) -> XpnHostListHttpRequest | None: ...
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
        def setUsageExportBucket(
            self,
            *,
            project: str,
            body: UsageExportLocation = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: PublicAdvertisedPrefixListHttpRequest,
            previous_response: PublicAdvertisedPrefixList,
        ) -> PublicAdvertisedPrefixListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            publicAdvertisedPrefix: str,
            body: PublicAdvertisedPrefix = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: PublicDelegatedPrefixAggregatedListHttpRequest,
            previous_response: PublicDelegatedPrefixAggregatedList,
        ) -> PublicDelegatedPrefixAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: PublicDelegatedPrefixListHttpRequest,
            previous_response: PublicDelegatedPrefixList,
        ) -> PublicDelegatedPrefixListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: RegionAutoscalerListHttpRequest,
            previous_response: RegionAutoscalerList,
        ) -> RegionAutoscalerListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: BackendServiceListHttpRequest,
            previous_response: BackendServiceList,
        ) -> BackendServiceListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: CommitmentAggregatedListHttpRequest,
            previous_response: CommitmentAggregatedList,
        ) -> CommitmentAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: CommitmentListHttpRequest,
            previous_response: CommitmentList,
        ) -> CommitmentListHttpRequest | None: ...
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
            commitment: str,
            body: Commitment = ...,
            paths: str | _list[str] = ...,
            requestId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: RegionDiskTypeListHttpRequest,
            previous_response: RegionDiskTypeList,
        ) -> RegionDiskTypeListHttpRequest | None: ...

    @typing.type_check_only
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
        def list_next(
            self, previous_request: DiskListHttpRequest, previous_response: DiskList
        ) -> DiskListHttpRequest | None: ...
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
        def update(
            self,
            *,
            project: str,
            region: str,
            disk: str,
            body: Disk = ...,
            paths: str | _list[str] = ...,
            requestId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: HealthCheckServicesListHttpRequest,
            previous_response: HealthCheckServicesList,
        ) -> HealthCheckServicesListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: HealthCheckListHttpRequest,
            previous_response: HealthCheckList,
        ) -> HealthCheckListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: RegionInstanceGroupManagerListHttpRequest,
            previous_response: RegionInstanceGroupManagerList,
        ) -> RegionInstanceGroupManagerListHttpRequest | None: ...
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
        def listErrors_next(
            self,
            previous_request: RegionInstanceGroupManagersListErrorsResponseHttpRequest,
            previous_response: RegionInstanceGroupManagersListErrorsResponse,
        ) -> RegionInstanceGroupManagersListErrorsResponseHttpRequest | None: ...
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
        def listManagedInstances_next(
            self,
            previous_request: RegionInstanceGroupManagersListInstancesResponseHttpRequest,
            previous_response: RegionInstanceGroupManagersListInstancesResponse,
        ) -> RegionInstanceGroupManagersListInstancesResponseHttpRequest | None: ...
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
        def listPerInstanceConfigs_next(
            self,
            previous_request: RegionInstanceGroupManagersListInstanceConfigsRespHttpRequest,
            previous_response: RegionInstanceGroupManagersListInstanceConfigsResp,
        ) -> RegionInstanceGroupManagersListInstanceConfigsRespHttpRequest | None: ...
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
        def resizeAdvanced(
            self,
            *,
            project: str,
            region: str,
            instanceGroupManager: str,
            body: RegionInstanceGroupManagersResizeAdvancedRequest = ...,
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: RegionInstanceGroupListHttpRequest,
            previous_response: RegionInstanceGroupList,
        ) -> RegionInstanceGroupListHttpRequest | None: ...
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
        def listInstances_next(
            self,
            previous_request: RegionInstanceGroupsListInstancesHttpRequest,
            previous_response: RegionInstanceGroupsListInstances,
        ) -> RegionInstanceGroupsListInstancesHttpRequest | None: ...
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

    @typing.type_check_only
    class RegionInstanceTemplatesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            instanceTemplate: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            instanceTemplate: str,
            **kwargs: typing.Any
        ) -> InstanceTemplateHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: InstanceTemplate = ...,
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
        ) -> InstanceTemplateListHttpRequest: ...
        def list_next(
            self,
            previous_request: InstanceTemplateListHttpRequest,
            previous_response: InstanceTemplateList,
        ) -> InstanceTemplateListHttpRequest | None: ...

    @typing.type_check_only
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: NetworkEndpointGroupListHttpRequest,
            previous_response: NetworkEndpointGroupList,
        ) -> NetworkEndpointGroupListHttpRequest | None: ...

    @typing.type_check_only
    class RegionNetworkFirewallPoliciesResource(googleapiclient.discovery.Resource):
        def addAssociation(
            self,
            *,
            project: str,
            region: str,
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
            region: str,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            maxPriority: int = ...,
            minPriority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def cloneRules(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            requestId: str = ...,
            sourceFirewallPolicy: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            **kwargs: typing.Any
        ) -> FirewallPolicyHttpRequest: ...
        def getAssociation(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            name: str = ...,
            **kwargs: typing.Any
        ) -> FirewallPolicyAssociationHttpRequest: ...
        def getEffectiveFirewalls(
            self, *, project: str, region: str, network: str, **kwargs: typing.Any
        ) -> RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            optionsRequestedPolicyVersion: int = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def getRule(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            priority: int = ...,
            **kwargs: typing.Any
        ) -> FirewallPolicyRuleHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: FirewallPolicy = ...,
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
        ) -> FirewallPolicyListHttpRequest: ...
        def list_next(
            self,
            previous_request: FirewallPolicyListHttpRequest,
            previous_response: FirewallPolicyList,
        ) -> FirewallPolicyListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            body: FirewallPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patchRule(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            body: FirewallPolicyRule = ...,
            priority: int = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeAssociation(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            name: str = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def removeRule(
            self,
            *,
            project: str,
            region: str,
            firewallPolicy: str,
            priority: int = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: NotificationEndpointListHttpRequest,
            previous_response: NotificationEndpointList,
        ) -> NotificationEndpointListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: OperationListHttpRequest,
            previous_response: OperationList,
        ) -> OperationListHttpRequest | None: ...
        def wait(
            self, *, project: str, region: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class RegionSecurityPoliciesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            securityPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            securityPolicy: str,
            **kwargs: typing.Any
        ) -> SecurityPolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: SecurityPolicy = ...,
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
        ) -> SecurityPolicyListHttpRequest: ...
        def list_next(
            self,
            previous_request: SecurityPolicyListHttpRequest,
            previous_response: SecurityPolicyList,
        ) -> SecurityPolicyListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            securityPolicy: str,
            body: SecurityPolicy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: SslCertificateListHttpRequest,
            previous_response: SslCertificateList,
        ) -> SslCertificateListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class RegionSslPoliciesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            sslPolicy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, project: str, region: str, sslPolicy: str, **kwargs: typing.Any
        ) -> SslPolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: SslPolicy = ...,
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
        ) -> SslPoliciesListHttpRequest: ...
        def list_next(
            self,
            previous_request: SslPoliciesListHttpRequest,
            previous_response: SslPoliciesList,
        ) -> SslPoliciesListHttpRequest | None: ...
        def listAvailableFeatures(
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
        ) -> SslPoliciesListAvailableFeaturesResponseHttpRequest: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            sslPolicy: str,
            body: SslPolicy = ...,
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: TargetHttpProxyListHttpRequest,
            previous_response: TargetHttpProxyList,
        ) -> TargetHttpProxyListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: TargetHttpsProxyListHttpRequest,
            previous_response: TargetHttpsProxyList,
        ) -> TargetHttpsProxyListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            targetHttpsProxy: str,
            body: TargetHttpsProxy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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

    @typing.type_check_only
    class RegionTargetTcpProxiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            project: str,
            region: str,
            targetTcpProxy: str,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self,
            *,
            project: str,
            region: str,
            targetTcpProxy: str,
            **kwargs: typing.Any
        ) -> TargetTcpProxyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            region: str,
            body: TargetTcpProxy = ...,
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
        ) -> TargetTcpProxyListHttpRequest: ...
        def list_next(
            self,
            previous_request: TargetTcpProxyListHttpRequest,
            previous_response: TargetTcpProxyList,
        ) -> TargetTcpProxyListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self, previous_request: UrlMapListHttpRequest, previous_response: UrlMapList
        ) -> UrlMapListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self, previous_request: RegionListHttpRequest, previous_response: RegionList
        ) -> RegionListHttpRequest | None: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: ReservationAggregatedListHttpRequest,
            previous_response: ReservationAggregatedList,
        ) -> ReservationAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: ReservationListHttpRequest,
            previous_response: ReservationList,
        ) -> ReservationListHttpRequest | None: ...
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
        def update(
            self,
            *,
            project: str,
            zone: str,
            reservation: str,
            body: Reservation = ...,
            paths: str | _list[str] = ...,
            requestId: str = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: ResourcePolicyAggregatedListHttpRequest,
            previous_response: ResourcePolicyAggregatedList,
        ) -> ResourcePolicyAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: ResourcePolicyListHttpRequest,
            previous_response: ResourcePolicyList,
        ) -> ResourcePolicyListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            resourcePolicy: str,
            body: ResourcePolicy = ...,
            requestId: str = ...,
            updateMask: str = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: RouterAggregatedListHttpRequest,
            previous_response: RouterAggregatedList,
        ) -> RouterAggregatedListHttpRequest | None: ...
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
        def getNatMappingInfo_next(
            self,
            previous_request: VmEndpointNatMappingsListHttpRequest,
            previous_response: VmEndpointNatMappingsList,
        ) -> VmEndpointNatMappingsListHttpRequest | None: ...
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
        def list_next(
            self, previous_request: RouterListHttpRequest, previous_response: RouterList
        ) -> RouterListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self, previous_request: RouteListHttpRequest, previous_response: RouteList
        ) -> RouteListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        ) -> SecurityPoliciesAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: SecurityPoliciesAggregatedListHttpRequest,
            previous_response: SecurityPoliciesAggregatedList,
        ) -> SecurityPoliciesAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: SecurityPolicyListHttpRequest,
            previous_response: SecurityPolicyList,
        ) -> SecurityPolicyListHttpRequest | None: ...
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

    @typing.type_check_only
    class ServiceAttachmentsResource(googleapiclient.discovery.Resource):
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
        ) -> ServiceAttachmentAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: ServiceAttachmentAggregatedListHttpRequest,
            previous_response: ServiceAttachmentAggregatedList,
        ) -> ServiceAttachmentAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: ServiceAttachmentListHttpRequest,
            previous_response: ServiceAttachmentList,
        ) -> ServiceAttachmentListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            region: str,
            serviceAttachment: str,
            body: ServiceAttachment = ...,
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
        def testIamPermissions(
            self,
            *,
            project: str,
            region: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: SnapshotListHttpRequest,
            previous_response: SnapshotList,
        ) -> SnapshotListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: SslCertificateAggregatedListHttpRequest,
            previous_response: SslCertificateAggregatedList,
        ) -> SslCertificateAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: SslCertificateListHttpRequest,
            previous_response: SslCertificateList,
        ) -> SslCertificateListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class SslPoliciesResource(googleapiclient.discovery.Resource):
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
        ) -> SslPoliciesAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: SslPoliciesAggregatedListHttpRequest,
            previous_response: SslPoliciesAggregatedList,
        ) -> SslPoliciesAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: SslPoliciesListHttpRequest,
            previous_response: SslPoliciesList,
        ) -> SslPoliciesListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: SubnetworkAggregatedListHttpRequest,
            previous_response: SubnetworkAggregatedList,
        ) -> SubnetworkAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: SubnetworkListHttpRequest,
            previous_response: SubnetworkList,
        ) -> SubnetworkListHttpRequest | None: ...
        def listUsable(
            self,
            *,
            project: str,
            filter: str = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            returnPartialSuccess: bool = ...,
            serviceProject: str = ...,
            **kwargs: typing.Any
        ) -> UsableSubnetworksAggregatedListHttpRequest: ...
        def listUsable_next(
            self,
            previous_request: UsableSubnetworksAggregatedListHttpRequest,
            previous_response: UsableSubnetworksAggregatedList,
        ) -> UsableSubnetworksAggregatedListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: TargetGrpcProxyListHttpRequest,
            previous_response: TargetGrpcProxyList,
        ) -> TargetGrpcProxyListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: TargetHttpProxyAggregatedListHttpRequest,
            previous_response: TargetHttpProxyAggregatedList,
        ) -> TargetHttpProxyAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetHttpProxyListHttpRequest,
            previous_response: TargetHttpProxyList,
        ) -> TargetHttpProxyListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: TargetHttpsProxyAggregatedListHttpRequest,
            previous_response: TargetHttpsProxyAggregatedList,
        ) -> TargetHttpsProxyAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetHttpsProxyListHttpRequest,
            previous_response: TargetHttpsProxyList,
        ) -> TargetHttpsProxyListHttpRequest | None: ...
        def patch(
            self,
            *,
            project: str,
            targetHttpsProxy: str,
            body: TargetHttpsProxy = ...,
            requestId: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: TargetInstanceAggregatedListHttpRequest,
            previous_response: TargetInstanceAggregatedList,
        ) -> TargetInstanceAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetInstanceListHttpRequest,
            previous_response: TargetInstanceList,
        ) -> TargetInstanceListHttpRequest | None: ...
        def testIamPermissions(
            self,
            *,
            project: str,
            zone: str,
            resource: str,
            body: TestPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestPermissionsResponseHttpRequest: ...

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: TargetPoolAggregatedListHttpRequest,
            previous_response: TargetPoolAggregatedList,
        ) -> TargetPoolAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetPoolListHttpRequest,
            previous_response: TargetPoolList,
        ) -> TargetPoolListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: TargetSslProxyListHttpRequest,
            previous_response: TargetSslProxyList,
        ) -> TargetSslProxyListHttpRequest | None: ...
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

    @typing.type_check_only
    class TargetTcpProxiesResource(googleapiclient.discovery.Resource):
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
        ) -> TargetTcpProxyAggregatedListHttpRequest: ...
        def aggregatedList_next(
            self,
            previous_request: TargetTcpProxyAggregatedListHttpRequest,
            previous_response: TargetTcpProxyAggregatedList,
        ) -> TargetTcpProxyAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetTcpProxyListHttpRequest,
            previous_response: TargetTcpProxyList,
        ) -> TargetTcpProxyListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: TargetVpnGatewayAggregatedListHttpRequest,
            previous_response: TargetVpnGatewayAggregatedList,
        ) -> TargetVpnGatewayAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: TargetVpnGatewayListHttpRequest,
            previous_response: TargetVpnGatewayList,
        ) -> TargetVpnGatewayListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: UrlMapsAggregatedListHttpRequest,
            previous_response: UrlMapsAggregatedList,
        ) -> UrlMapsAggregatedListHttpRequest | None: ...
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
        def list_next(
            self, previous_request: UrlMapListHttpRequest, previous_response: UrlMapList
        ) -> UrlMapListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: VpnGatewayAggregatedListHttpRequest,
            previous_response: VpnGatewayAggregatedList,
        ) -> VpnGatewayAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: VpnGatewayListHttpRequest,
            previous_response: VpnGatewayList,
        ) -> VpnGatewayListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def aggregatedList_next(
            self,
            previous_request: VpnTunnelAggregatedListHttpRequest,
            previous_response: VpnTunnelAggregatedList,
        ) -> VpnTunnelAggregatedListHttpRequest | None: ...
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
        def list_next(
            self,
            previous_request: VpnTunnelListHttpRequest,
            previous_response: VpnTunnelList,
        ) -> VpnTunnelListHttpRequest | None: ...
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

    @typing.type_check_only
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
        def list_next(
            self,
            previous_request: OperationListHttpRequest,
            previous_response: OperationList,
        ) -> OperationListHttpRequest | None: ...
        def wait(
            self, *, project: str, zone: str, operation: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
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
        def list_next(
            self, previous_request: ZoneListHttpRequest, previous_response: ZoneList
        ) -> ZoneListHttpRequest | None: ...

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
    def acceleratorTypes(self) -> AcceleratorTypesResource: ...
    def addresses(self) -> AddressesResource: ...
    def autoscalers(self) -> AutoscalersResource: ...
    def backendBuckets(self) -> BackendBucketsResource: ...
    def backendServices(self) -> BackendServicesResource: ...
    def diskTypes(self) -> DiskTypesResource: ...
    def disks(self) -> DisksResource: ...
    def externalVpnGateways(self) -> ExternalVpnGatewaysResource: ...
    def firewallPolicies(self) -> FirewallPoliciesResource: ...
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
    def imageFamilyViews(self) -> ImageFamilyViewsResource: ...
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
    def networkAttachments(self) -> NetworkAttachmentsResource: ...
    def networkEdgeSecurityServices(self) -> NetworkEdgeSecurityServicesResource: ...
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
    def regionInstanceGroupManagers(self) -> RegionInstanceGroupManagersResource: ...
    def regionInstanceGroups(self) -> RegionInstanceGroupsResource: ...
    def regionInstanceTemplates(self) -> RegionInstanceTemplatesResource: ...
    def regionInstances(self) -> RegionInstancesResource: ...
    def regionNetworkEndpointGroups(self) -> RegionNetworkEndpointGroupsResource: ...
    def regionNetworkFirewallPolicies(
        self,
    ) -> RegionNetworkFirewallPoliciesResource: ...
    def regionNotificationEndpoints(self) -> RegionNotificationEndpointsResource: ...
    def regionOperations(self) -> RegionOperationsResource: ...
    def regionSecurityPolicies(self) -> RegionSecurityPoliciesResource: ...
    def regionSslCertificates(self) -> RegionSslCertificatesResource: ...
    def regionSslPolicies(self) -> RegionSslPoliciesResource: ...
    def regionTargetHttpProxies(self) -> RegionTargetHttpProxiesResource: ...
    def regionTargetHttpsProxies(self) -> RegionTargetHttpsProxiesResource: ...
    def regionTargetTcpProxies(self) -> RegionTargetTcpProxiesResource: ...
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
    def zoneOperations(self) -> ZoneOperationsResource: ...
    def zones(self) -> ZonesResource: ...

@typing.type_check_only
class AcceleratorTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AcceleratorType: ...

@typing.type_check_only
class AcceleratorTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AcceleratorTypeAggregatedList: ...

@typing.type_check_only
class AcceleratorTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AcceleratorTypeList: ...

@typing.type_check_only
class AddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Address: ...

@typing.type_check_only
class AddressAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AddressAggregatedList: ...

@typing.type_check_only
class AddressListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AddressList: ...

@typing.type_check_only
class AutoscalerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Autoscaler: ...

@typing.type_check_only
class AutoscalerAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AutoscalerAggregatedList: ...

@typing.type_check_only
class AutoscalerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AutoscalerList: ...

@typing.type_check_only
class BackendBucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendBucket: ...

@typing.type_check_only
class BackendBucketListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendBucketList: ...

@typing.type_check_only
class BackendServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendService: ...

@typing.type_check_only
class BackendServiceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendServiceAggregatedList: ...

@typing.type_check_only
class BackendServiceGroupHealthHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendServiceGroupHealth: ...

@typing.type_check_only
class BackendServiceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BackendServiceList: ...

@typing.type_check_only
class CommitmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Commitment: ...

@typing.type_check_only
class CommitmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommitmentAggregatedList: ...

@typing.type_check_only
class CommitmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommitmentList: ...

@typing.type_check_only
class DiskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Disk: ...

@typing.type_check_only
class DiskAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiskAggregatedList: ...

@typing.type_check_only
class DiskListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiskList: ...

@typing.type_check_only
class DiskTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiskType: ...

@typing.type_check_only
class DiskTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiskTypeAggregatedList: ...

@typing.type_check_only
class DiskTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DiskTypeList: ...

@typing.type_check_only
class ExchangedPeeringRoutesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExchangedPeeringRoutesList: ...

@typing.type_check_only
class ExternalVpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExternalVpnGateway: ...

@typing.type_check_only
class ExternalVpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ExternalVpnGatewayList: ...

@typing.type_check_only
class FirewallHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Firewall: ...

@typing.type_check_only
class FirewallListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallList: ...

@typing.type_check_only
class FirewallPoliciesListAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallPoliciesListAssociationsResponse: ...

@typing.type_check_only
class FirewallPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallPolicy: ...

@typing.type_check_only
class FirewallPolicyAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallPolicyAssociation: ...

@typing.type_check_only
class FirewallPolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallPolicyList: ...

@typing.type_check_only
class FirewallPolicyRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FirewallPolicyRule: ...

@typing.type_check_only
class ForwardingRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ForwardingRule: ...

@typing.type_check_only
class ForwardingRuleAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ForwardingRuleAggregatedList: ...

@typing.type_check_only
class ForwardingRuleListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ForwardingRuleList: ...

@typing.type_check_only
class GuestAttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GuestAttributes: ...

@typing.type_check_only
class HealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HealthCheck: ...

@typing.type_check_only
class HealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HealthCheckList: ...

@typing.type_check_only
class HealthCheckServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HealthCheckService: ...

@typing.type_check_only
class HealthCheckServicesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HealthCheckServicesList: ...

@typing.type_check_only
class HealthChecksAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HealthChecksAggregatedList: ...

@typing.type_check_only
class HttpHealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpHealthCheck: ...

@typing.type_check_only
class HttpHealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpHealthCheckList: ...

@typing.type_check_only
class HttpsHealthCheckHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpsHealthCheck: ...

@typing.type_check_only
class HttpsHealthCheckListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpsHealthCheckList: ...

@typing.type_check_only
class ImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Image: ...

@typing.type_check_only
class ImageFamilyViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImageFamilyView: ...

@typing.type_check_only
class ImageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ImageList: ...

@typing.type_check_only
class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Instance: ...

@typing.type_check_only
class InstanceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceAggregatedList: ...

@typing.type_check_only
class InstanceGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroup: ...

@typing.type_check_only
class InstanceGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupAggregatedList: ...

@typing.type_check_only
class InstanceGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupList: ...

@typing.type_check_only
class InstanceGroupManagerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManager: ...

@typing.type_check_only
class InstanceGroupManagerAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManagerAggregatedList: ...

@typing.type_check_only
class InstanceGroupManagerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManagerList: ...

@typing.type_check_only
class InstanceGroupManagersListErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManagersListErrorsResponse: ...

@typing.type_check_only
class InstanceGroupManagersListManagedInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManagersListManagedInstancesResponse: ...

@typing.type_check_only
class InstanceGroupManagersListPerInstanceConfigsRespHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupManagersListPerInstanceConfigsResp: ...

@typing.type_check_only
class InstanceGroupsListInstancesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceGroupsListInstances: ...

@typing.type_check_only
class InstanceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceList: ...

@typing.type_check_only
class InstanceListReferrersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceListReferrers: ...

@typing.type_check_only
class InstanceTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceTemplate: ...

@typing.type_check_only
class InstanceTemplateAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceTemplateAggregatedList: ...

@typing.type_check_only
class InstanceTemplateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstanceTemplateList: ...

@typing.type_check_only
class InstancesGetEffectiveFirewallsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InstancesGetEffectiveFirewallsResponse: ...

@typing.type_check_only
class InterconnectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Interconnect: ...

@typing.type_check_only
class InterconnectAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectAttachment: ...

@typing.type_check_only
class InterconnectAttachmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectAttachmentAggregatedList: ...

@typing.type_check_only
class InterconnectAttachmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectAttachmentList: ...

@typing.type_check_only
class InterconnectListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectList: ...

@typing.type_check_only
class InterconnectLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectLocation: ...

@typing.type_check_only
class InterconnectLocationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectLocationList: ...

@typing.type_check_only
class InterconnectsGetDiagnosticsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> InterconnectsGetDiagnosticsResponse: ...

@typing.type_check_only
class LicenseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> License: ...

@typing.type_check_only
class LicenseCodeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LicenseCode: ...

@typing.type_check_only
class LicensesListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LicensesListResponse: ...

@typing.type_check_only
class MachineImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MachineImage: ...

@typing.type_check_only
class MachineImageListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MachineImageList: ...

@typing.type_check_only
class MachineTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MachineType: ...

@typing.type_check_only
class MachineTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MachineTypeAggregatedList: ...

@typing.type_check_only
class MachineTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> MachineTypeList: ...

@typing.type_check_only
class NetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Network: ...

@typing.type_check_only
class NetworkAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkAttachment: ...

@typing.type_check_only
class NetworkAttachmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkAttachmentAggregatedList: ...

@typing.type_check_only
class NetworkAttachmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkAttachmentList: ...

@typing.type_check_only
class NetworkEdgeSecurityServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEdgeSecurityService: ...

@typing.type_check_only
class NetworkEdgeSecurityServiceAggregatedListHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEdgeSecurityServiceAggregatedList: ...

@typing.type_check_only
class NetworkEndpointGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEndpointGroup: ...

@typing.type_check_only
class NetworkEndpointGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEndpointGroupAggregatedList: ...

@typing.type_check_only
class NetworkEndpointGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEndpointGroupList: ...

@typing.type_check_only
class NetworkEndpointGroupsListNetworkEndpointsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkEndpointGroupsListNetworkEndpoints: ...

@typing.type_check_only
class NetworkListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworkList: ...

@typing.type_check_only
class NetworksGetEffectiveFirewallsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NetworksGetEffectiveFirewallsResponse: ...

@typing.type_check_only
class NodeGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeGroup: ...

@typing.type_check_only
class NodeGroupAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeGroupAggregatedList: ...

@typing.type_check_only
class NodeGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeGroupList: ...

@typing.type_check_only
class NodeGroupsListNodesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeGroupsListNodes: ...

@typing.type_check_only
class NodeTemplateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeTemplate: ...

@typing.type_check_only
class NodeTemplateAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeTemplateAggregatedList: ...

@typing.type_check_only
class NodeTemplateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeTemplateList: ...

@typing.type_check_only
class NodeTypeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeType: ...

@typing.type_check_only
class NodeTypeAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeTypeAggregatedList: ...

@typing.type_check_only
class NodeTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NodeTypeList: ...

@typing.type_check_only
class NotificationEndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NotificationEndpoint: ...

@typing.type_check_only
class NotificationEndpointListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> NotificationEndpointList: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class OperationAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperationAggregatedList: ...

@typing.type_check_only
class OperationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OperationList: ...

@typing.type_check_only
class OrganizationSecurityPoliciesListAssociationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> OrganizationSecurityPoliciesListAssociationsResponse: ...

@typing.type_check_only
class PacketMirroringHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PacketMirroring: ...

@typing.type_check_only
class PacketMirroringAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PacketMirroringAggregatedList: ...

@typing.type_check_only
class PacketMirroringListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PacketMirroringList: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Project: ...

@typing.type_check_only
class ProjectsGetXpnResourcesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProjectsGetXpnResources: ...

@typing.type_check_only
class PublicAdvertisedPrefixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicAdvertisedPrefix: ...

@typing.type_check_only
class PublicAdvertisedPrefixListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicAdvertisedPrefixList: ...

@typing.type_check_only
class PublicDelegatedPrefixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicDelegatedPrefix: ...

@typing.type_check_only
class PublicDelegatedPrefixAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicDelegatedPrefixAggregatedList: ...

@typing.type_check_only
class PublicDelegatedPrefixListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublicDelegatedPrefixList: ...

@typing.type_check_only
class RegionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Region: ...

@typing.type_check_only
class RegionAutoscalerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionAutoscalerList: ...

@typing.type_check_only
class RegionDiskTypeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionDiskTypeList: ...

@typing.type_check_only
class RegionInstanceGroupListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupList: ...

@typing.type_check_only
class RegionInstanceGroupManagerListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupManagerList: ...

@typing.type_check_only
class RegionInstanceGroupManagersListErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupManagersListErrorsResponse: ...

@typing.type_check_only
class RegionInstanceGroupManagersListInstanceConfigsRespHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupManagersListInstanceConfigsResp: ...

@typing.type_check_only
class RegionInstanceGroupManagersListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupManagersListInstancesResponse: ...

@typing.type_check_only
class RegionInstanceGroupsListInstancesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionInstanceGroupsListInstances: ...

@typing.type_check_only
class RegionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionList: ...

@typing.type_check_only
class RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RegionNetworkFirewallPoliciesGetEffectiveFirewallsResponse: ...

@typing.type_check_only
class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Reservation: ...

@typing.type_check_only
class ReservationAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReservationAggregatedList: ...

@typing.type_check_only
class ReservationListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReservationList: ...

@typing.type_check_only
class ResourcePolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourcePolicy: ...

@typing.type_check_only
class ResourcePolicyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourcePolicyAggregatedList: ...

@typing.type_check_only
class ResourcePolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ResourcePolicyList: ...

@typing.type_check_only
class RouteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Route: ...

@typing.type_check_only
class RouteListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RouteList: ...

@typing.type_check_only
class RouterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Router: ...

@typing.type_check_only
class RouterAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RouterAggregatedList: ...

@typing.type_check_only
class RouterListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RouterList: ...

@typing.type_check_only
class RouterStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RouterStatusResponse: ...

@typing.type_check_only
class RoutersPreviewResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RoutersPreviewResponse: ...

@typing.type_check_only
class ScreenshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Screenshot: ...

@typing.type_check_only
class SecurityPoliciesAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPoliciesAggregatedList: ...

@typing.type_check_only
class SecurityPoliciesListPreconfiguredExpressionSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPoliciesListPreconfiguredExpressionSetsResponse: ...

@typing.type_check_only
class SecurityPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPolicy: ...

@typing.type_check_only
class SecurityPolicyAssociationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPolicyAssociation: ...

@typing.type_check_only
class SecurityPolicyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPolicyList: ...

@typing.type_check_only
class SecurityPolicyRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SecurityPolicyRule: ...

@typing.type_check_only
class SerialPortOutputHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SerialPortOutput: ...

@typing.type_check_only
class ServiceAttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAttachment: ...

@typing.type_check_only
class ServiceAttachmentAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAttachmentAggregatedList: ...

@typing.type_check_only
class ServiceAttachmentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAttachmentList: ...

@typing.type_check_only
class ShieldedInstanceIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShieldedInstanceIdentity: ...

@typing.type_check_only
class ShieldedVmIdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ShieldedVmIdentity: ...

@typing.type_check_only
class SnapshotHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Snapshot: ...

@typing.type_check_only
class SnapshotListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SnapshotList: ...

@typing.type_check_only
class SslCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslCertificate: ...

@typing.type_check_only
class SslCertificateAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslCertificateAggregatedList: ...

@typing.type_check_only
class SslCertificateListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslCertificateList: ...

@typing.type_check_only
class SslPoliciesAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslPoliciesAggregatedList: ...

@typing.type_check_only
class SslPoliciesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslPoliciesList: ...

@typing.type_check_only
class SslPoliciesListAvailableFeaturesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslPoliciesListAvailableFeaturesResponse: ...

@typing.type_check_only
class SslPolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SslPolicy: ...

@typing.type_check_only
class SubnetworkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Subnetwork: ...

@typing.type_check_only
class SubnetworkAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubnetworkAggregatedList: ...

@typing.type_check_only
class SubnetworkListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SubnetworkList: ...

@typing.type_check_only
class TargetGrpcProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetGrpcProxy: ...

@typing.type_check_only
class TargetGrpcProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetGrpcProxyList: ...

@typing.type_check_only
class TargetHttpProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpProxy: ...

@typing.type_check_only
class TargetHttpProxyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpProxyAggregatedList: ...

@typing.type_check_only
class TargetHttpProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpProxyList: ...

@typing.type_check_only
class TargetHttpsProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpsProxy: ...

@typing.type_check_only
class TargetHttpsProxyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpsProxyAggregatedList: ...

@typing.type_check_only
class TargetHttpsProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetHttpsProxyList: ...

@typing.type_check_only
class TargetInstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetInstance: ...

@typing.type_check_only
class TargetInstanceAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetInstanceAggregatedList: ...

@typing.type_check_only
class TargetInstanceListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetInstanceList: ...

@typing.type_check_only
class TargetPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetPool: ...

@typing.type_check_only
class TargetPoolAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetPoolAggregatedList: ...

@typing.type_check_only
class TargetPoolInstanceHealthHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetPoolInstanceHealth: ...

@typing.type_check_only
class TargetPoolListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetPoolList: ...

@typing.type_check_only
class TargetSslProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetSslProxy: ...

@typing.type_check_only
class TargetSslProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetSslProxyList: ...

@typing.type_check_only
class TargetTcpProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetTcpProxy: ...

@typing.type_check_only
class TargetTcpProxyAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetTcpProxyAggregatedList: ...

@typing.type_check_only
class TargetTcpProxyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetTcpProxyList: ...

@typing.type_check_only
class TargetVpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetVpnGateway: ...

@typing.type_check_only
class TargetVpnGatewayAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetVpnGatewayAggregatedList: ...

@typing.type_check_only
class TargetVpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TargetVpnGatewayList: ...

@typing.type_check_only
class TestPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestPermissionsResponse: ...

@typing.type_check_only
class UrlMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UrlMap: ...

@typing.type_check_only
class UrlMapListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UrlMapList: ...

@typing.type_check_only
class UrlMapsAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UrlMapsAggregatedList: ...

@typing.type_check_only
class UrlMapsValidateResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UrlMapsValidateResponse: ...

@typing.type_check_only
class UsableSubnetworksAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UsableSubnetworksAggregatedList: ...

@typing.type_check_only
class VmEndpointNatMappingsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VmEndpointNatMappingsList: ...

@typing.type_check_only
class VpnGatewayHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnGateway: ...

@typing.type_check_only
class VpnGatewayAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnGatewayAggregatedList: ...

@typing.type_check_only
class VpnGatewayListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnGatewayList: ...

@typing.type_check_only
class VpnGatewaysGetStatusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnGatewaysGetStatusResponse: ...

@typing.type_check_only
class VpnTunnelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnTunnel: ...

@typing.type_check_only
class VpnTunnelAggregatedListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnTunnelAggregatedList: ...

@typing.type_check_only
class VpnTunnelListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VpnTunnelList: ...

@typing.type_check_only
class XpnHostListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> XpnHostList: ...

@typing.type_check_only
class ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Zone: ...

@typing.type_check_only
class ZoneListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ZoneList: ...
