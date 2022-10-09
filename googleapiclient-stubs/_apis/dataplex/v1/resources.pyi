import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudDataplexResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LakesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ActionsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListActionsResponse,
                    ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest | None: ...

                @typing.type_check_only
                class ContentResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONTENT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListContentResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListContentResponse,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class ContentitemsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self,
                        *,
                        name: str,
                        view: typing_extensions.Literal[
                            "CONTENT_VIEW_UNSPECIFIED", "BASIC", "FULL"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListContentResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListContentResponse,
                    ) -> GoogleCloudDataplexV1ListContentResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Content = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ContentHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...

                @typing.type_check_only
                class EnvironmentsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SessionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1ListSessionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListSessionsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListSessionsResponse,
                        ) -> GoogleCloudDataplexV1ListSessionsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Environment = ...,
                        environmentId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1EnvironmentHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListEnvironmentsResponse,
                    ) -> GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Environment = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def sessions(self) -> SessionsResource: ...

                @typing.type_check_only
                class TasksResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class JobsResource(googleapiclient.discovery.Resource):
                        def cancel(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1CancelJobRequest = ...,
                            **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1JobHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1ListJobsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListJobsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListJobsResponse,
                        ) -> GoogleCloudDataplexV1ListJobsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Task = ...,
                        taskId: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1TaskHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListTasksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListTasksResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListTasksResponse,
                    ) -> GoogleCloudDataplexV1ListTasksResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Task = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def jobs(self) -> JobsResource: ...

                @typing.type_check_only
                class ZonesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ActionsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListActionsResponse,
                        ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class AssetsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class ActionsResource(googleapiclient.discovery.Resource):
                            def list(
                                self,
                                *,
                                parent: str,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDataplexV1ListActionsResponseHttpRequest,
                                previous_response: GoogleCloudDataplexV1ListActionsResponse,
                            ) -> GoogleCloudDataplexV1ListActionsResponseHttpRequest | None: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDataplexV1Asset = ...,
                            assetId: str = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1AssetHttpRequest: ...
                        def getIamPolicy(
                            self,
                            *,
                            resource: str,
                            options_requestedPolicyVersion: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1ListAssetsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListAssetsResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListAssetsResponse,
                        ) -> GoogleCloudDataplexV1ListAssetsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1Asset = ...,
                            updateMask: str = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleLongrunningOperationHttpRequest: ...
                        def setIamPolicy(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1SetIamPolicyRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleIamV1PolicyHttpRequest: ...
                        def testIamPermissions(
                            self,
                            *,
                            resource: str,
                            body: GoogleIamV1TestIamPermissionsRequest = ...,
                            **kwargs: typing.Any
                        ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                        def actions(self) -> ActionsResource: ...

                    @typing.type_check_only
                    class EntitiesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class PartitionsResource(googleapiclient.discovery.Resource):
                            def create(
                                self,
                                *,
                                parent: str,
                                body: GoogleCloudDataplexV1Partition = ...,
                                validateOnly: bool = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDataplexV1PartitionHttpRequest: ...
                            def delete(
                                self,
                                *,
                                name: str,
                                etag: str = ...,
                                **kwargs: typing.Any
                            ) -> EmptyHttpRequest: ...
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudDataplexV1PartitionHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any
                            ) -> GoogleCloudDataplexV1ListPartitionsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudDataplexV1ListPartitionsResponseHttpRequest,
                                previous_response: GoogleCloudDataplexV1ListPartitionsResponse,
                            ) -> GoogleCloudDataplexV1ListPartitionsResponseHttpRequest | None: ...

                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudDataplexV1Entity = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def delete(
                            self, *, name: str, etag: str = ..., **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "ENTITY_VIEW_UNSPECIFIED", "BASIC", "SCHEMA", "FULL"
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "ENTITY_VIEW_UNSPECIFIED", "TABLES", "FILESETS"
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1ListEntitiesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudDataplexV1ListEntitiesResponseHttpRequest,
                            previous_response: GoogleCloudDataplexV1ListEntitiesResponse,
                        ) -> GoogleCloudDataplexV1ListEntitiesResponseHttpRequest | None: ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudDataplexV1Entity = ...,
                            validateOnly: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudDataplexV1EntityHttpRequest: ...
                        def partitions(self) -> PartitionsResource: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudDataplexV1Zone = ...,
                        validateOnly: bool = ...,
                        zoneId: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ZoneHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDataplexV1ListZonesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDataplexV1ListZonesResponseHttpRequest,
                        previous_response: GoogleCloudDataplexV1ListZonesResponse,
                    ) -> GoogleCloudDataplexV1ListZonesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudDataplexV1Zone = ...,
                        updateMask: str = ...,
                        validateOnly: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: GoogleIamV1TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                    def actions(self) -> ActionsResource: ...
                    def assets(self) -> AssetsResource: ...
                    def entities(self) -> EntitiesResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDataplexV1Lake = ...,
                    lakeId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1LakeHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDataplexV1ListLakesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudDataplexV1ListLakesResponseHttpRequest,
                    previous_response: GoogleCloudDataplexV1ListLakesResponse,
                ) -> GoogleCloudDataplexV1ListLakesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDataplexV1Lake = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: GoogleIamV1TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
                def actions(self) -> ActionsResource: ...
                def content(self) -> ContentResource: ...
                def contentitems(self) -> ContentitemsResource: ...
                def environments(self) -> EnvironmentsResource: ...
                def tasks(self) -> TasksResource: ...
                def zones(self) -> ZonesResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunningCancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
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
                    **kwargs: typing.Any
                ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
                    previous_response: GoogleLongrunningListOperationsResponse,
                ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudLocationLocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudLocationListLocationsResponseHttpRequest,
                previous_response: GoogleCloudLocationListLocationsResponse,
            ) -> GoogleCloudLocationListLocationsResponseHttpRequest | None: ...
            def lakes(self) -> LakesResource: ...
            def operations(self) -> OperationsResource: ...

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
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleCloudDataplexV1AssetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Asset: ...

@typing.type_check_only
class GoogleCloudDataplexV1ContentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Content: ...

@typing.type_check_only
class GoogleCloudDataplexV1EntityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Entity: ...

@typing.type_check_only
class GoogleCloudDataplexV1EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Environment: ...

@typing.type_check_only
class GoogleCloudDataplexV1JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Job: ...

@typing.type_check_only
class GoogleCloudDataplexV1LakeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Lake: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListActionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListAssetsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListContentResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListContentResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEntitiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListEntitiesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListEnvironmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListEnvironmentsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListJobsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListLakesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListLakesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListPartitionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListPartitionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListSessionsResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListTasksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListTasksResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1ListZonesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1ListZonesResponse: ...

@typing.type_check_only
class GoogleCloudDataplexV1PartitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Partition: ...

@typing.type_check_only
class GoogleCloudDataplexV1TaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Task: ...

@typing.type_check_only
class GoogleCloudDataplexV1ZoneHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDataplexV1Zone: ...

@typing.type_check_only
class GoogleCloudLocationListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudLocationLocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudLocationLocation: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...
