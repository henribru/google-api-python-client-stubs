import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ApigeeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class HybridResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IssuersResource(googleapiclient.discovery.Resource):
            def list(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest: ...

        def issuers(self) -> IssuersResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnalyticsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatastoresResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def list(
                    self, *, parent: str, targetType: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDatastoresResponseHttpRequest: ...
                def test(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1TestDatastoreResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...

            def datastores(self) -> DatastoresResource: ...

        @typing.type_check_only
        class ApiproductsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttributesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                def updateApiProductAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...

            @typing.type_check_only
            class RateplansResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1RatePlan = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1RatePlanHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1RatePlanHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1RatePlanHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    count: int = ...,
                    expand: bool = ...,
                    orderBy: str = ...,
                    startKey: str = ...,
                    state: typing_extensions.Literal[
                        "STATE_UNSPECIFIED", "DRAFT", "PUBLISHED"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListRatePlansResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1RatePlan = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1RatePlanHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                attributename: str = ...,
                attributevalue: str = ...,
                count: str = ...,
                expand: bool = ...,
                space: str = ...,
                startKey: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListApiProductsResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1MoveApiProductRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def attributes(self) -> AttributesResource: ...
            def rateplans(self) -> RateplansResource: ...

        @typing.type_check_only
        class ApisResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DebugsessionsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListApiDebugSessionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListApiDebugSessionsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListApiDebugSessionsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListApiDebugSessionsResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

            @typing.type_check_only
            class KeyvaluemapsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1KeyValueEntry = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest,
                        previous_response: GoogleCloudApigeeV1ListKeyValueEntriesResponse,
                    ) -> (
                        GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest | None
                    ): ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1KeyValueEntry = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueMap = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def entries(self) -> EntriesResource: ...

            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
                def get(
                    self, *, name: str, format: str = ..., **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def updateApiProxyRevision(
                    self,
                    *,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    validate: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleApiHttpBody = ...,
                action: str = ...,
                name: str = ...,
                space: str = ...,
                validate: bool = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeMetaData: bool = ...,
                includeRevisions: bool = ...,
                space: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1MoveApiProxyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1ApiProxy = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def debugsessions(self) -> DebugsessionsResource: ...
            def deployments(self) -> DeploymentsResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
            def revisions(self) -> RevisionsResource: ...

        @typing.type_check_only
        class AppgroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class KeysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ApiproductsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1AppGroupAppKeyHttpRequest: ...
                        def updateAppGroupAppKeyApiProduct(
                            self, *, name: str, action: str = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1AppGroupAppKey = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1AppGroupAppKeyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AppGroupAppKeyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AppGroupAppKeyHttpRequest: ...
                    def updateAppGroupAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1UpdateAppGroupAppKeyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1AppGroupAppKeyHttpRequest: ...
                    def apiproducts(self) -> ApiproductsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1AppGroupApp = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1AppGroupAppHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AppGroupAppHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AppGroupAppHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListAppGroupAppsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListAppGroupAppsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListAppGroupAppsResponse,
                ) -> GoogleCloudApigeeV1ListAppGroupAppsResponseHttpRequest | None: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1AppGroupApp = ...,
                    action: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1AppGroupAppHttpRequest: ...
                def keys(self) -> KeysResource: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1AppGroup = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1AppGroupHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AppGroupHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AppGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListAppGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListAppGroupsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListAppGroupsResponse,
            ) -> GoogleCloudApigeeV1ListAppGroupsResponseHttpRequest | None: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1AppGroup = ...,
                action: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1AppGroupHttpRequest: ...
            def apps(self) -> AppsResource: ...

        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                apiProduct: str = ...,
                apptype: str = ...,
                expand: bool = ...,
                filter: str = ...,
                ids: str = ...,
                includeCred: bool = ...,
                keyStatus: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                rows: str = ...,
                startKey: str = ...,
                status: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListAppsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListAppsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListAppsResponse,
            ) -> GoogleCloudApigeeV1ListAppsResponseHttpRequest | None: ...

        @typing.type_check_only
        class DatacollectorsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1DataCollector = ...,
                dataCollectorId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListDataCollectorsResponse,
            ) -> GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1DataCollector = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...

        @typing.type_check_only
        class DeploymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

        @typing.type_check_only
        class DevelopersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttributesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                    def updateDeveloperAppAttribute(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1Attribute = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...

                @typing.type_check_only
                class KeysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ApiproductsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                        def updateDeveloperAppKeyApiProduct(
                            self, *, name: str, action: str = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...

                    @typing.type_check_only
                    class CreateResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def replaceDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def updateDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        action: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def apiproducts(self) -> ApiproductsResource: ...
                    def create(self) -> CreateResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def generateKeyPairOrUpdateDeveloperAppStatus(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    action: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    entity: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    count: str = ...,
                    expand: bool = ...,
                    shallowExpand: bool = ...,
                    startKey: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def attributes(self) -> AttributesResource: ...
                def keys(self) -> KeysResource: ...

            @typing.type_check_only
            class AttributesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                def updateDeveloperAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...

            @typing.type_check_only
            class BalanceResource(googleapiclient.discovery.Resource):
                def adjust(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1AdjustDeveloperBalanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperBalanceHttpRequest: ...
                def credit(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1CreditDeveloperBalanceRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperBalanceHttpRequest: ...

            @typing.type_check_only
            class SubscriptionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1DeveloperSubscription = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperSubscriptionHttpRequest: ...
                def expire(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ExpireDeveloperSubscriptionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1DeveloperSubscriptionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperSubscriptionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    count: int = ...,
                    startKey: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseHttpRequest
                ): ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def get(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def getBalance(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperBalanceHttpRequest: ...
            def getMonetizationConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperMonetizationConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                app: str = ...,
                count: str = ...,
                expand: bool = ...,
                ids: str = ...,
                includeCompany: bool = ...,
                startKey: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest: ...
            def setDeveloperStatus(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def updateMonetizationConfig(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1DeveloperMonetizationConfig = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DeveloperMonetizationConfigHttpRequest: ...
            def apps(self) -> AppsResource: ...
            def attributes(self) -> AttributesResource: ...
            def balance(self) -> BalanceResource: ...
            def subscriptions(self) -> SubscriptionsResource: ...

        @typing.type_check_only
        class DnsZonesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1DnsZone = ...,
                dnsZoneId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DnsZoneHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListDnsZonesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListDnsZonesResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListDnsZonesResponse,
            ) -> GoogleCloudApigeeV1ListDnsZonesResponseHttpRequest | None: ...

        @typing.type_check_only
        class EndpointAttachmentsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1EndpointAttachment = ...,
                endpointAttachmentId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EndpointAttachmentHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListEndpointAttachmentsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListEndpointAttachmentsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListEndpointAttachmentsResponse,
            ) -> (
                GoogleCloudApigeeV1ListEndpointAttachmentsResponseHttpRequest | None
            ): ...

        @typing.type_check_only
        class EnvgroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1EnvironmentGroupAttachment = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest
                    | None
                ): ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                name: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentGroupHttpRequest: ...
            def getDeployedIngressConfig(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "INGRESS_CONFIG_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1EnvironmentGroupConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListEnvironmentGroupsResponse,
            ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...

        @typing.type_check_only
        class EnvironmentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AddonsConfigResource(googleapiclient.discovery.Resource):
                def setAddonEnablement(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1SetAddonEnablementRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...

            @typing.type_check_only
            class AnalyticsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AdminResource(googleapiclient.discovery.Resource):
                    def getSchemav2(
                        self,
                        *,
                        name: str,
                        disableCache: bool = ...,
                        type: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1SchemaHttpRequest: ...

                @typing.type_check_only
                class ExportsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1ExportRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1ExportHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ExportHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListExportsResponseHttpRequest: ...

                def admin(self) -> AdminResource: ...
                def exports(self) -> ExportsResource: ...

            @typing.type_check_only
            class ApisResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class DebugsessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class DataResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> (
                                GoogleCloudApigeeV1DebugSessionTransactionHttpRequest
                            ): ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApigeeV1DebugSession = ...,
                            timeout: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApigeeV1DebugSessionHttpRequest: ...
                        def deleteData(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DebugSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest
                        ): ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest,
                            previous_response: GoogleCloudApigeeV1ListDebugSessionsResponse,
                        ) -> (
                            GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest
                            | None
                        ): ...
                        def data(self) -> DataResource: ...

                    @typing.type_check_only
                    class DeploymentsResource(googleapiclient.discovery.Resource):
                        def generateDeployChangeReport(
                            self,
                            *,
                            name: str,
                            override: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudApigeeV1DeploymentChangeReportHttpRequest: ...
                        def generateUndeployChangeReport(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeploymentChangeReportHttpRequest: ...

                    def deploy(
                        self,
                        *,
                        name: str,
                        override: bool = ...,
                        sequencedRollout: bool = ...,
                        serviceAccount: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def getDeployments(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        sequencedRollout: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def debugsessions(self) -> DebugsessionsResource: ...
                    def deployments(self) -> DeploymentsResource: ...

                def deployments(self) -> DeploymentsResource: ...
                def revisions(self) -> RevisionsResource: ...

            @typing.type_check_only
            class ArchiveDeploymentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1ArchiveDeployment = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def generateDownloadUrl(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1GenerateDownloadUrlRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1GenerateDownloadUrlResponseHttpRequest: ...
                def generateUploadUrl(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1GenerateUploadUrlRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1GenerateUploadUrlResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ArchiveDeploymentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListArchiveDeploymentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListArchiveDeploymentsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListArchiveDeploymentsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListArchiveDeploymentsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ArchiveDeployment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ArchiveDeploymentHttpRequest: ...

            @typing.type_check_only
            class CachesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...

            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

            @typing.type_check_only
            class FlowhooksResource(googleapiclient.discovery.Resource):
                def attachSharedFlowToFlowHook(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1FlowHook = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def detachSharedFlowFromFlowHook(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...

            @typing.type_check_only
            class KeystoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AliasesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleApiHttpBody = ...,
                        alias: str = ...,
                        format: str = ...,
                        ignoreExpiryValidation: bool = ...,
                        ignoreNewlineValidation: bool = ...,
                        x_password: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def csr(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def getCertificate(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: GoogleApiHttpBody = ...,
                        ignoreExpiryValidation: bool = ...,
                        ignoreNewlineValidation: bool = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Keystore = ...,
                    name: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def aliases(self) -> AliasesResource: ...

            @typing.type_check_only
            class KeyvaluemapsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntriesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1KeyValueEntry = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest,
                        previous_response: GoogleCloudApigeeV1ListKeyValueEntriesResponse,
                    ) -> (
                        GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest | None
                    ): ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1KeyValueEntry = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueMap = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def entries(self) -> EntriesResource: ...

            @typing.type_check_only
            class OptimizedStatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    accuracy: str = ...,
                    aggTable: str = ...,
                    filter: str = ...,
                    limit: str = ...,
                    offset: str = ...,
                    realtime: bool = ...,
                    select: str = ...,
                    sonar: bool = ...,
                    sort: str = ...,
                    sortby: str = ...,
                    timeRange: str = ...,
                    timeUnit: str = ...,
                    topk: str = ...,
                    tsAscending: bool = ...,
                    tzo: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1OptimizedStatsHttpRequest: ...

            @typing.type_check_only
            class QueriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Query = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def getResult(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def getResulturl(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    dataset: str = ...,
                    inclQueriesWithoutReport: str = ...,
                    status: str = ...,
                    submittedBy: str = ...,
                    to: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest: ...

            @typing.type_check_only
            class ReferencesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Reference = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Reference = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...

            @typing.type_check_only
            class ResourcefilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleApiHttpBody = ...,
                    name: str = ...,
                    type: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
                def delete(
                    self, *, parent: str, type: str, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
                def get(
                    self, *, parent: str, type: str, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def list(
                    self, *, parent: str, type: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
                def listEnvironmentResources(
                    self, *, parent: str, type: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    parent: str,
                    type: str,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...

            @typing.type_check_only
            class SecurityActionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1SecurityAction = ...,
                    securityActionId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityActionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def disable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DisableSecurityActionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityActionHttpRequest: ...
                def enable(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1EnableSecurityActionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityActionHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SecurityActionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListSecurityActionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListSecurityActionsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListSecurityActionsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListSecurityActionsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1SecurityAction = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityActionHttpRequest: ...

            @typing.type_check_only
            class SecurityIncidentsResource(googleapiclient.discovery.Resource):
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1BatchUpdateSecurityIncidentsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponseHttpRequest
                ): ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SecurityIncidentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListSecurityIncidentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListSecurityIncidentsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListSecurityIncidentsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListSecurityIncidentsResponseHttpRequest | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1SecurityIncident = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityIncidentHttpRequest: ...

            @typing.type_check_only
            class SecurityReportsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1SecurityReportQuery = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SecurityReportHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SecurityReportHttpRequest: ...
                def getResult(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def getResultView(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SecurityReportResultViewHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    dataset: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    status: str = ...,
                    submittedBy: str = ...,
                    to: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListSecurityReportsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class SecurityStatsResource(googleapiclient.discovery.Resource):
                def queryTabularStats(
                    self,
                    *,
                    orgenv: str,
                    body: GoogleCloudApigeeV1QueryTabularStatsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1QueryTabularStatsResponseHttpRequest: ...
                def queryTabularStats_next(
                    self,
                    previous_request: GoogleCloudApigeeV1QueryTabularStatsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1QueryTabularStatsResponse,
                ) -> GoogleCloudApigeeV1QueryTabularStatsResponseHttpRequest | None: ...
                def queryTimeSeriesStats(
                    self,
                    *,
                    orgenv: str,
                    body: GoogleCloudApigeeV1QueryTimeSeriesStatsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1QueryTimeSeriesStatsResponseHttpRequest: ...
                def queryTimeSeriesStats_next(
                    self,
                    previous_request: GoogleCloudApigeeV1QueryTimeSeriesStatsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1QueryTimeSeriesStatsResponse,
                ) -> (
                    GoogleCloudApigeeV1QueryTimeSeriesStatsResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class SharedflowsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    def deploy(
                        self,
                        *,
                        name: str,
                        override: bool = ...,
                        serviceAccount: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def getDeployments(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def undeploy(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...

                def deployments(self) -> DeploymentsResource: ...
                def revisions(self) -> RevisionsResource: ...

            @typing.type_check_only
            class StatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    accuracy: str = ...,
                    aggTable: str = ...,
                    filter: str = ...,
                    limit: str = ...,
                    offset: str = ...,
                    realtime: bool = ...,
                    select: str = ...,
                    sonar: bool = ...,
                    sort: str = ...,
                    sortby: str = ...,
                    timeRange: str = ...,
                    timeUnit: str = ...,
                    topk: str = ...,
                    tsAscending: bool = ...,
                    tzo: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1StatsHttpRequest: ...

            @typing.type_check_only
            class TargetserversResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1TargetServer = ...,
                    name: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1TargetServer = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...

            @typing.type_check_only
            class TraceConfigResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1TraceConfigOverride = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest,
                        previous_response: GoogleCloudApigeeV1ListTraceConfigOverridesResponse,
                    ) -> (
                        GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1TraceConfigOverride = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...

                def overrides(self) -> OverridesResource: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Environment = ...,
                name: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def getAddonsConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AddonsConfigHttpRequest: ...
            def getApiSecurityRuntimeConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiSecurityRuntimeConfigHttpRequest: ...
            def getDebugmask(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DebugMaskHttpRequest: ...
            def getDeployedConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentConfigHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def getSecurityActionsConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityActionsConfigHttpRequest: ...
            def getTraceConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1TraceConfigHttpRequest: ...
            def modifyEnvironment(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def subscribe(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SubscriptionHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
            def unsubscribe(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Subscription = ...,
                **kwargs: typing.Any,
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def updateDebugmask(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1DebugMask = ...,
                replaceRepeatedFields: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1DebugMaskHttpRequest: ...
            def updateEnvironment(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def updateSecurityActionsConfig(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1SecurityActionsConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityActionsConfigHttpRequest: ...
            def updateTraceConfig(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1TraceConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1TraceConfigHttpRequest: ...
            def addonsConfig(self) -> AddonsConfigResource: ...
            def analytics(self) -> AnalyticsResource: ...
            def apis(self) -> ApisResource: ...
            def archiveDeployments(self) -> ArchiveDeploymentsResource: ...
            def caches(self) -> CachesResource: ...
            def deployments(self) -> DeploymentsResource: ...
            def flowhooks(self) -> FlowhooksResource: ...
            def keystores(self) -> KeystoresResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
            def optimizedStats(self) -> OptimizedStatsResource: ...
            def queries(self) -> QueriesResource: ...
            def references(self) -> ReferencesResource: ...
            def resourcefiles(self) -> ResourcefilesResource: ...
            def securityActions(self) -> SecurityActionsResource: ...
            def securityIncidents(self) -> SecurityIncidentsResource: ...
            def securityReports(self) -> SecurityReportsResource: ...
            def securityStats(self) -> SecurityStatsResource: ...
            def sharedflows(self) -> SharedflowsResource: ...
            def stats(self) -> StatsResource: ...
            def targetservers(self) -> TargetserversResource: ...
            def traceConfig(self) -> TraceConfigResource: ...

        @typing.type_check_only
        class HostQueriesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Query = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
            def getResult(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleApiHttpBodyHttpRequest: ...
            def getResultView(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AsyncQueryResultViewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                dataset: str = ...,
                envgroupHostname: str = ...,
                inclQueriesWithoutReport: str = ...,
                status: str = ...,
                submittedBy: str = ...,
                to: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest: ...

        @typing.type_check_only
        class HostSecurityReportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1SecurityReportQuery = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityReportHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityReportHttpRequest: ...
            def getResult(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleApiHttpBodyHttpRequest: ...
            def getResultView(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityReportResultViewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                dataset: str = ...,
                envgroupHostname: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                status: str = ...,
                submittedBy: str = ...,
                to: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSecurityReportsResponse,
            ) -> GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest | None: ...

        @typing.type_check_only
        class HostStatsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                accuracy: str = ...,
                envgroupHostname: str = ...,
                filter: str = ...,
                limit: str = ...,
                offset: str = ...,
                realtime: bool = ...,
                select: str = ...,
                sort: str = ...,
                sortby: str = ...,
                timeRange: str = ...,
                timeUnit: str = ...,
                topk: str = ...,
                tsAscending: bool = ...,
                tzo: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1StatsHttpRequest: ...

        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1InstanceAttachment = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1InstanceAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListInstanceAttachmentsResponse,
                ) -> (
                    GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest | None
                ): ...

            @typing.type_check_only
            class CanaryevaluationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1CanaryEvaluation = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1CanaryEvaluationHttpRequest: ...

            @typing.type_check_only
            class NatAddressesResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ActivateNatAddressRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1NatAddress = ...,
                    **kwargs: typing.Any,
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1NatAddressHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListNatAddressesResponse,
                ) -> GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Instance = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1InstanceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListInstancesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListInstancesResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListInstancesResponse,
            ) -> GoogleCloudApigeeV1ListInstancesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Instance = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def reportStatus(
                self,
                *,
                instance: str,
                body: GoogleCloudApigeeV1ReportInstanceStatusRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
            def canaryevaluations(self) -> CanaryevaluationsResource: ...
            def natAddresses(self) -> NatAddressesResource: ...

        @typing.type_check_only
        class KeyvaluemapsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EntriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueEntry = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListKeyValueEntriesResponse,
                ) -> (
                    GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest | None
                ): ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1KeyValueEntry = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1KeyValueEntryHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1KeyValueMap = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            def entries(self) -> EntriesResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunningListOperationsResponse,
            ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

        @typing.type_check_only
        class OptimizedHostStatsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                accuracy: str = ...,
                envgroupHostname: str = ...,
                filter: str = ...,
                limit: str = ...,
                offset: str = ...,
                realtime: bool = ...,
                select: str = ...,
                sort: str = ...,
                sortby: str = ...,
                timeRange: str = ...,
                timeUnit: str = ...,
                topk: str = ...,
                tsAscending: bool = ...,
                tzo: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1OptimizedStatsHttpRequest: ...

        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def list(
                self, *, parent: str, expand: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...

        @typing.type_check_only
        class SecurityAssessmentResultsResource(googleapiclient.discovery.Resource):
            def batchCompute(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponseHttpRequest: ...
            def batchCompute_next(
                self,
                previous_request: GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponse,
            ) -> (
                GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SecurityMonitoringConditionsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1SecurityMonitoringCondition = ...,
                securityMonitoringConditionId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityMonitoringConditionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityMonitoringConditionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponse,
            ) -> (
                GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1SecurityMonitoringCondition = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityMonitoringConditionHttpRequest: ...

        @typing.type_check_only
        class SecurityProfilesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                def computeEnvironmentScores(
                    self,
                    *,
                    profileEnvironment: str,
                    body: GoogleCloudApigeeV1ComputeEnvironmentScoresRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ComputeEnvironmentScoresResponseHttpRequest: ...
                def computeEnvironmentScores_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ComputeEnvironmentScoresResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ComputeEnvironmentScoresResponse,
                ) -> (
                    GoogleCloudApigeeV1ComputeEnvironmentScoresResponseHttpRequest
                    | None
                ): ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationHttpRequest
                ): ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1SecurityProfile = ...,
                securityProfileId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityProfileHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSecurityProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSecurityProfilesResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSecurityProfilesResponse,
            ) -> GoogleCloudApigeeV1ListSecurityProfilesResponseHttpRequest | None: ...
            def listRevisions(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseHttpRequest: ...
            def listRevisions_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSecurityProfileRevisionsResponse,
            ) -> (
                GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1SecurityProfile = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityProfileHttpRequest: ...
            def environments(self) -> EnvironmentsResource: ...

        @typing.type_check_only
        class SecurityProfilesV2Resource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1SecurityProfileV2 = ...,
                securityProfileV2Id: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityProfileV2HttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SecurityProfileV2HttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSecurityProfilesV2ResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSecurityProfilesV2ResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSecurityProfilesV2Response,
            ) -> (
                GoogleCloudApigeeV1ListSecurityProfilesV2ResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1SecurityProfileV2 = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SecurityProfileV2HttpRequest: ...

        @typing.type_check_only
        class SharedflowsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
                def get(
                    self, *, name: str, format: str = ..., **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def updateSharedFlowRevision(
                    self,
                    *,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    validate: bool = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleApiHttpBody = ...,
                action: str = ...,
                name: str = ...,
                space: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeMetaData: bool = ...,
                includeRevisions: bool = ...,
                space: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest: ...
            def move(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1MoveSharedFlowRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
            def revisions(self) -> RevisionsResource: ...

        @typing.type_check_only
        class SitesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ApicategoriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1ApiCategory = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiCategoryResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeleteResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiCategoryResponseHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListApiCategoriesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ApiCategory = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiCategoryResponseHttpRequest: ...

            @typing.type_check_only
            class ApidocsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1ApiDoc = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiDocResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeleteResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiDocResponseHttpRequest: ...
                def getDocumentation(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiDocDocumentationResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ListApiDocsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudApigeeV1ListApiDocsResponseHttpRequest,
                    previous_response: GoogleCloudApigeeV1ListApiDocsResponse,
                ) -> GoogleCloudApigeeV1ListApiDocsResponseHttpRequest | None: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ApiDoc = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiDocResponseHttpRequest: ...
                def updateDocumentation(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ApiDocDocumentation = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudApigeeV1ApiDocDocumentationResponseHttpRequest: ...

            def apicategories(self) -> ApicategoriesResource: ...
            def apidocs(self) -> ApidocsResource: ...

        @typing.type_check_only
        class SpacesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Space = ...,
                spaceId: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SpaceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SpaceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1ListSpacesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudApigeeV1ListSpacesResponseHttpRequest,
                previous_response: GoogleCloudApigeeV1ListSpacesResponse,
            ) -> GoogleCloudApigeeV1ListSpacesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Space = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudApigeeV1SpaceHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1SetIamPolicyRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1TestIamPermissionsRequest = ...,
                **kwargs: typing.Any,
            ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

        def create(
            self,
            *,
            body: GoogleCloudApigeeV1Organization = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            retention: typing_extensions.Literal[
                "DELETION_RETENTION_UNSPECIFIED", "MINIMUM"
            ] = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def getControlPlaneAccess(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1ControlPlaneAccessHttpRequest: ...
        def getDeployedIngressConfig(
            self,
            *,
            name: str,
            view: typing_extensions.Literal[
                "INGRESS_CONFIG_VIEW_UNSPECIFIED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudApigeeV1IngressConfigHttpRequest: ...
        def getProjectMapping(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationProjectMappingHttpRequest: ...
        def getRuntimeConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1RuntimeConfigHttpRequest: ...
        def getSecuritySettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1SecuritySettingsHttpRequest: ...
        def getSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1GetSyncAuthorizationRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def list(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest: ...
        def setAddons(
            self,
            *,
            org: str,
            body: GoogleCloudApigeeV1SetAddonsRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def setSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1SyncAuthorization = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def update(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1Organization = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def updateControlPlaneAccess(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1ControlPlaneAccess = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def updateSecuritySettings(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1SecuritySettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudApigeeV1SecuritySettingsHttpRequest: ...
        def analytics(self) -> AnalyticsResource: ...
        def apiproducts(self) -> ApiproductsResource: ...
        def apis(self) -> ApisResource: ...
        def appgroups(self) -> AppgroupsResource: ...
        def apps(self) -> AppsResource: ...
        def datacollectors(self) -> DatacollectorsResource: ...
        def deployments(self) -> DeploymentsResource: ...
        def developers(self) -> DevelopersResource: ...
        def dnsZones(self) -> DnsZonesResource: ...
        def endpointAttachments(self) -> EndpointAttachmentsResource: ...
        def envgroups(self) -> EnvgroupsResource: ...
        def environments(self) -> EnvironmentsResource: ...
        def hostQueries(self) -> HostQueriesResource: ...
        def hostSecurityReports(self) -> HostSecurityReportsResource: ...
        def hostStats(self) -> HostStatsResource: ...
        def instances(self) -> InstancesResource: ...
        def keyvaluemaps(self) -> KeyvaluemapsResource: ...
        def operations(self) -> OperationsResource: ...
        def optimizedHostStats(self) -> OptimizedHostStatsResource: ...
        def reports(self) -> ReportsResource: ...
        def securityAssessmentResults(self) -> SecurityAssessmentResultsResource: ...
        def securityMonitoringConditions(
            self,
        ) -> SecurityMonitoringConditionsResource: ...
        def securityProfiles(self) -> SecurityProfilesResource: ...
        def securityProfilesV2(self) -> SecurityProfilesV2Resource: ...
        def sharedflows(self) -> SharedflowsResource: ...
        def sites(self) -> SitesResource: ...
        def spaces(self) -> SpacesResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def provisionOrganization(
            self,
            *,
            project: str,
            body: GoogleCloudApigeeV1ProvisionOrganizationRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

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
    def hybrid(self) -> HybridResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudApigeeV1AddonsConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AddonsConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1AliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Alias: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategoryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiCategoryResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocDocumentationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiDocDocumentationResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiDocResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiDocResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiProduct: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiProxy: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyRevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiProxyRevision: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiSecurityRuntimeConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ApiSecurityRuntimeConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1App: ...

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AppGroup: ...

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AppGroupApp: ...

@typing.type_check_only
class GoogleCloudApigeeV1AppGroupAppKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AppGroupAppKey: ...

@typing.type_check_only
class GoogleCloudApigeeV1ArchiveDeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ArchiveDeployment: ...

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AsyncQuery: ...

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryResultViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1AsyncQueryResultView: ...

@typing.type_check_only
class GoogleCloudApigeeV1AttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Attribute: ...

@typing.type_check_only
class GoogleCloudApigeeV1AttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Attributes: ...

@typing.type_check_only
class GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1BatchComputeSecurityAssessmentResultsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1BatchUpdateSecurityIncidentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1CanaryEvaluation: ...

@typing.type_check_only
class GoogleCloudApigeeV1ComputeEnvironmentScoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ComputeEnvironmentScoresResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ControlPlaneAccessHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ControlPlaneAccess: ...

@typing.type_check_only
class GoogleCloudApigeeV1CustomReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1CustomReport: ...

@typing.type_check_only
class GoogleCloudApigeeV1DataCollectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DataCollector: ...

@typing.type_check_only
class GoogleCloudApigeeV1DatastoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Datastore: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugMaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DebugMask: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DebugSession: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionTransactionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DebugSessionTransaction: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeleteCustomReportResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeleteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeleteResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Deployment: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeploymentChangeReport: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Developer: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeveloperApp: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeveloperAppKey: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperBalanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeveloperBalance: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperMonetizationConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeveloperMonetizationConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperSubscriptionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DeveloperSubscription: ...

@typing.type_check_only
class GoogleCloudApigeeV1DnsZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1DnsZone: ...

@typing.type_check_only
class GoogleCloudApigeeV1EndpointAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1EndpointAttachment: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Environment: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1EnvironmentConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1EnvironmentGroup: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1EnvironmentGroupAttachment: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1EnvironmentGroupConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Export: ...

@typing.type_check_only
class GoogleCloudApigeeV1FlowHookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1FlowHook: ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateDownloadUrlResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1GenerateDownloadUrlResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1GenerateUploadUrlResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1GenerateUploadUrlResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1GetAsyncQueryResultUrlResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1GetAsyncQueryResultUrlResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1IngressConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1IngressConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Instance: ...

@typing.type_check_only
class GoogleCloudApigeeV1InstanceAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1InstanceAttachment: ...

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1KeyValueEntry: ...

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1KeyValueMap: ...

@typing.type_check_only
class GoogleCloudApigeeV1KeystoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Keystore: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiCategoriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListApiCategoriesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiDebugSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListApiDebugSessionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiDocsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListApiDocsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListApiProductsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListApiProxiesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListAppGroupAppsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAppGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListAppGroupsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListAppsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListArchiveDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListArchiveDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListAsyncQueriesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListCustomReportsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDataCollectorsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDatastoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDatastoresResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDebugSessionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDeveloperAppsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperSubscriptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDeveloperSubscriptionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDnsZonesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListDnsZonesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEndpointAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListEndpointAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListExportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListExportsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListHybridIssuersResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListInstancesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListKeyValueEntriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListKeyValueEntriesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListNatAddressesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListOfDevelopersResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListOrganizationsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListRatePlansResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListRatePlansResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityActionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityIncidentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityIncidentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityMonitoringConditionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfileRevisionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityProfileRevisionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityProfilesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityProfilesV2ResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityProfilesV2Response: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSecurityReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSecurityReportsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSharedFlowsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSpacesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListSpacesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ListTraceConfigOverridesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1NatAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1NatAddress: ...

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1OptimizedStats: ...

@typing.type_check_only
class GoogleCloudApigeeV1OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Organization: ...

@typing.type_check_only
class GoogleCloudApigeeV1OrganizationProjectMappingHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1OrganizationProjectMapping: ...

@typing.type_check_only
class GoogleCloudApigeeV1QueryTabularStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1QueryTabularStatsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1QueryTimeSeriesStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1QueryTimeSeriesStatsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1RatePlanHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1RatePlan: ...

@typing.type_check_only
class GoogleCloudApigeeV1ReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Reference: ...

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ReportInstanceStatusResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1ResourceFile: ...

@typing.type_check_only
class GoogleCloudApigeeV1RuntimeConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1RuntimeConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Schema: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityAction: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityActionsConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityActionsConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityIncidentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityIncident: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityMonitoringConditionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityMonitoringCondition: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityProfile: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileEnvironmentAssociationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityProfileEnvironmentAssociation: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityProfileV2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityProfileV2: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityReport: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecurityReportResultViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecurityReportResultView: ...

@typing.type_check_only
class GoogleCloudApigeeV1SecuritySettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SecuritySettings: ...

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SharedFlow: ...

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowRevisionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SharedFlowRevision: ...

@typing.type_check_only
class GoogleCloudApigeeV1SpaceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Space: ...

@typing.type_check_only
class GoogleCloudApigeeV1StatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Stats: ...

@typing.type_check_only
class GoogleCloudApigeeV1SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1Subscription: ...

@typing.type_check_only
class GoogleCloudApigeeV1SyncAuthorizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1SyncAuthorization: ...

@typing.type_check_only
class GoogleCloudApigeeV1TargetServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1TargetServer: ...

@typing.type_check_only
class GoogleCloudApigeeV1TestDatastoreResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1TestDatastoreResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1TraceConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigOverrideHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudApigeeV1TraceConfigOverride: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...
