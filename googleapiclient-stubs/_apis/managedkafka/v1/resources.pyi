import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ManagedKafkaResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AclsResource(googleapiclient.discovery.Resource):
                    def addAclEntry(
                        self, *, acl: str, body: AclEntry = ..., **kwargs: typing.Any
                    ) -> AddAclEntryResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Acl = ...,
                        aclId: str = ...,
                        **kwargs: typing.Any,
                    ) -> AclHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AclHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAclsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAclsResponseHttpRequest,
                        previous_response: ListAclsResponse,
                    ) -> ListAclsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Acl = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> AclHttpRequest: ...
                    def removeAclEntry(
                        self, *, acl: str, body: AclEntry = ..., **kwargs: typing.Any
                    ) -> RemoveAclEntryResponseHttpRequest: ...

                @typing.type_check_only
                class ConsumerGroupsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConsumerGroupHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "CONSUMER_GROUP_VIEW_UNSPECIFIED",
                            "CONSUMER_GROUP_VIEW_BASIC",
                            "CONSUMER_GROUP_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> ListConsumerGroupsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConsumerGroupsResponseHttpRequest,
                        previous_response: ListConsumerGroupsResponse,
                    ) -> ListConsumerGroupsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ConsumerGroup = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ConsumerGroupHttpRequest: ...

                @typing.type_check_only
                class TopicsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Topic = ...,
                        topicId: str = ...,
                        **kwargs: typing.Any,
                    ) -> TopicHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TopicHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListTopicsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListTopicsResponseHttpRequest,
                        previous_response: ListTopicsResponse,
                    ) -> ListTopicsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Topic = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> TopicHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Cluster = ...,
                    clusterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "CLUSTER_VIEW_UNSPECIFIED",
                        "CLUSTER_VIEW_BASIC",
                        "CLUSTER_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ClusterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClustersResponseHttpRequest,
                    previous_response: ListClustersResponse,
                ) -> ListClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Cluster = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def acls(self) -> AclsResource: ...
                def consumerGroups(self) -> ConsumerGroupsResource: ...
                def topics(self) -> TopicsResource: ...

            @typing.type_check_only
            class ConnectClustersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConnectorsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Connector = ...,
                        connectorId: str = ...,
                        **kwargs: typing.Any,
                    ) -> ConnectorHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConnectorHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListConnectorsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConnectorsResponseHttpRequest,
                        previous_response: ListConnectorsResponse,
                    ) -> ListConnectorsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Connector = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> ConnectorHttpRequest: ...
                    def pause(
                        self,
                        *,
                        name: str,
                        body: PauseConnectorRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PauseConnectorResponseHttpRequest: ...
                    def restart(
                        self,
                        *,
                        name: str,
                        body: RestartConnectorRequest = ...,
                        **kwargs: typing.Any,
                    ) -> RestartConnectorResponseHttpRequest: ...
                    def resume(
                        self,
                        *,
                        name: str,
                        body: ResumeConnectorRequest = ...,
                        **kwargs: typing.Any,
                    ) -> ResumeConnectorResponseHttpRequest: ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: StopConnectorRequest = ...,
                        **kwargs: typing.Any,
                    ) -> StopConnectorResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: ConnectCluster = ...,
                    connectClusterId: str = ...,
                    requestId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, requestId: str = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ConnectClusterHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListConnectClustersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListConnectClustersResponseHttpRequest,
                    previous_response: ListConnectClustersResponse,
                ) -> ListConnectClustersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ConnectCluster = ...,
                    requestId: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def connectors(self) -> ConnectorsResource: ...

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
                    returnPartialSuccess: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class SchemaRegistriesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CompatibilityResource(googleapiclient.discovery.Resource):
                    def checkCompatibility(
                        self,
                        *,
                        name: str,
                        body: CheckCompatibilityRequest = ...,
                        **kwargs: typing.Any,
                    ) -> CheckCompatibilityResponseHttpRequest: ...

                @typing.type_check_only
                class ConfigResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SchemaConfigHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        defaultToGlobal: bool = ...,
                        **kwargs: typing.Any,
                    ) -> SchemaConfigHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UpdateSchemaConfigRequest = ...,
                        **kwargs: typing.Any,
                    ) -> SchemaConfigHttpRequest: ...

                @typing.type_check_only
                class ContextsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class CompatibilityResource(googleapiclient.discovery.Resource):
                        def checkCompatibility(
                            self,
                            *,
                            name: str,
                            body: CheckCompatibilityRequest = ...,
                            **kwargs: typing.Any,
                        ) -> CheckCompatibilityResponseHttpRequest: ...

                    @typing.type_check_only
                    class ConfigResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> SchemaConfigHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            defaultToGlobal: bool = ...,
                            **kwargs: typing.Any,
                        ) -> SchemaConfigHttpRequest: ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: UpdateSchemaConfigRequest = ...,
                            **kwargs: typing.Any,
                        ) -> SchemaConfigHttpRequest: ...

                    @typing.type_check_only
                    class ModeResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> SchemaModeHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> SchemaModeHttpRequest: ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: UpdateSchemaModeRequest = ...,
                            **kwargs: typing.Any,
                        ) -> SchemaModeHttpRequest: ...

                    @typing.type_check_only
                    class SchemasResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class SubjectsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                deleted: bool = ...,
                                subject: str = ...,
                                **kwargs: typing.Any,
                            ) -> HttpBodyHttpRequest: ...

                        @typing.type_check_only
                        class TypesResource(googleapiclient.discovery.Resource):
                            def list(
                                self, *, parent: str, **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...

                        @typing.type_check_only
                        class VersionsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                deleted: bool = ...,
                                subject: str = ...,
                                **kwargs: typing.Any,
                            ) -> HttpBodyHttpRequest: ...

                        def get(
                            self, *, name: str, subject: str = ..., **kwargs: typing.Any
                        ) -> SchemaHttpRequest: ...
                        def getSchema(
                            self, *, name: str, subject: str = ..., **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def subjects(self) -> SubjectsResource: ...
                        def types(self) -> TypesResource: ...
                        def versions(self) -> VersionsResource: ...

                    @typing.type_check_only
                    class SubjectsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class VersionsResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class ReferencedbyResource(
                                googleapiclient.discovery.Resource
                            ):
                                def list(
                                    self, *, parent: str, **kwargs: typing.Any
                                ) -> HttpBodyHttpRequest: ...

                            def create(
                                self,
                                *,
                                parent: str,
                                body: CreateVersionRequest = ...,
                                **kwargs: typing.Any,
                            ) -> CreateVersionResponseHttpRequest: ...
                            def delete(
                                self,
                                *,
                                name: str,
                                permanent: bool = ...,
                                **kwargs: typing.Any,
                            ) -> HttpBodyHttpRequest: ...
                            def get(
                                self,
                                *,
                                name: str,
                                deleted: bool = ...,
                                **kwargs: typing.Any,
                            ) -> SchemaVersionHttpRequest: ...
                            def getSchema(
                                self,
                                *,
                                name: str,
                                deleted: bool = ...,
                                **kwargs: typing.Any,
                            ) -> HttpBodyHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                deleted: bool = ...,
                                **kwargs: typing.Any,
                            ) -> HttpBodyHttpRequest: ...
                            def referencedby(self) -> ReferencedbyResource: ...

                        def delete(
                            self,
                            *,
                            name: str,
                            permanent: bool = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            deleted: bool = ...,
                            subjectPrefix: str = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...
                        def lookupVersion(
                            self,
                            *,
                            parent: str,
                            body: LookupVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> SchemaVersionHttpRequest: ...
                        def versions(self) -> VersionsResource: ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ContextHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def compatibility(self) -> CompatibilityResource: ...
                    def config(self) -> ConfigResource: ...
                    def mode(self) -> ModeResource: ...
                    def schemas(self) -> SchemasResource: ...
                    def subjects(self) -> SubjectsResource: ...

                @typing.type_check_only
                class ModeResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SchemaModeHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SchemaModeHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: UpdateSchemaModeRequest = ...,
                        **kwargs: typing.Any,
                    ) -> SchemaModeHttpRequest: ...

                @typing.type_check_only
                class SchemasResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SubjectsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            deleted: bool = ...,
                            subject: str = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...

                    @typing.type_check_only
                    class TypesResource(googleapiclient.discovery.Resource):
                        def list(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            deleted: bool = ...,
                            subject: str = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...

                    def get(
                        self, *, name: str, subject: str = ..., **kwargs: typing.Any
                    ) -> SchemaHttpRequest: ...
                    def getSchema(
                        self, *, name: str, subject: str = ..., **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def subjects(self) -> SubjectsResource: ...
                    def types(self) -> TypesResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class SubjectsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class ReferencedbyResource(googleapiclient.discovery.Resource):
                            def list(
                                self, *, parent: str, **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: CreateVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> CreateVersionResponseHttpRequest: ...
                        def delete(
                            self,
                            *,
                            name: str,
                            permanent: bool = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            deleted: bool = ...,
                            **kwargs: typing.Any,
                        ) -> SchemaVersionHttpRequest: ...
                        def getSchema(
                            self,
                            *,
                            name: str,
                            deleted: bool = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            deleted: bool = ...,
                            **kwargs: typing.Any,
                        ) -> HttpBodyHttpRequest: ...
                        def referencedby(self) -> ReferencedbyResource: ...

                    def delete(
                        self, *, name: str, permanent: bool = ..., **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        deleted: bool = ...,
                        subjectPrefix: str = ...,
                        **kwargs: typing.Any,
                    ) -> HttpBodyHttpRequest: ...
                    def lookupVersion(
                        self,
                        *,
                        parent: str,
                        body: LookupVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> SchemaVersionHttpRequest: ...
                    def versions(self) -> VersionsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: CreateSchemaRegistryRequest = ...,
                    **kwargs: typing.Any,
                ) -> SchemaRegistryHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SchemaRegistryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    view: typing_extensions.Literal[
                        "SCHEMA_REGISTRY_VIEW_UNSPECIFIED",
                        "SCHEMA_REGISTRY_VIEW_BASIC",
                        "SCHEMA_REGISTRY_VIEW_FULL",
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> ListSchemaRegistriesResponseHttpRequest: ...
                def compatibility(self) -> CompatibilityResource: ...
                def config(self) -> ConfigResource: ...
                def contexts(self) -> ContextsResource: ...
                def mode(self) -> ModeResource: ...
                def schemas(self) -> SchemasResource: ...
                def subjects(self) -> SubjectsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                extraLocationTypes: str | _list[str] = ...,
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
            def clusters(self) -> ClustersResource: ...
            def connectClusters(self) -> ConnectClustersResource: ...
            def operations(self) -> OperationsResource: ...
            def schemaRegistries(self) -> SchemaRegistriesResource: ...

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
class AclHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Acl: ...

@typing.type_check_only
class AddAclEntryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AddAclEntryResponse: ...

@typing.type_check_only
class CheckCompatibilityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckCompatibilityResponse: ...

@typing.type_check_only
class ClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cluster: ...

@typing.type_check_only
class ConnectClusterHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConnectCluster: ...

@typing.type_check_only
class ConnectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Connector: ...

@typing.type_check_only
class ConsumerGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ConsumerGroup: ...

@typing.type_check_only
class ContextHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Context: ...

@typing.type_check_only
class CreateVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CreateVersionResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HttpBody: ...

@typing.type_check_only
class ListAclsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAclsResponse: ...

@typing.type_check_only
class ListClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListClustersResponse: ...

@typing.type_check_only
class ListConnectClustersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectClustersResponse: ...

@typing.type_check_only
class ListConnectorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConnectorsResponse: ...

@typing.type_check_only
class ListConsumerGroupsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListConsumerGroupsResponse: ...

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
class ListSchemaRegistriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSchemaRegistriesResponse: ...

@typing.type_check_only
class ListTopicsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTopicsResponse: ...

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
class PauseConnectorResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PauseConnectorResponse: ...

@typing.type_check_only
class RemoveAclEntryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemoveAclEntryResponse: ...

@typing.type_check_only
class RestartConnectorResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RestartConnectorResponse: ...

@typing.type_check_only
class ResumeConnectorResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ResumeConnectorResponse: ...

@typing.type_check_only
class SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Schema: ...

@typing.type_check_only
class SchemaConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SchemaConfig: ...

@typing.type_check_only
class SchemaModeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SchemaMode: ...

@typing.type_check_only
class SchemaRegistryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SchemaRegistry: ...

@typing.type_check_only
class SchemaVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SchemaVersion: ...

@typing.type_check_only
class StopConnectorResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StopConnectorResponse: ...

@typing.type_check_only
class TopicHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Topic: ...
