import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class RealTimeBiddingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BiddersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCreativesResponseHttpRequest,
                previous_response: ListCreativesResponse,
            ) -> ListCreativesResponseHttpRequest | None: ...
            def watch(
                self,
                *,
                parent: str,
                body: WatchCreativesRequest = ...,
                **kwargs: typing.Any
            ) -> WatchCreativesResponseHttpRequest: ...

        @typing.type_check_only
        class EndpointsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> EndpointHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListEndpointsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListEndpointsResponseHttpRequest,
                previous_response: ListEndpointsResponse,
            ) -> ListEndpointsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Endpoint = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> EndpointHttpRequest: ...

        @typing.type_check_only
        class PretargetingConfigsResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: ActivatePretargetingConfigRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedApps(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedAppsRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedPublishers(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedPublishersRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedSites(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedSitesRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: PretargetingConfig = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPretargetingConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPretargetingConfigsResponseHttpRequest,
                previous_response: ListPretargetingConfigsResponse,
            ) -> ListPretargetingConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: PretargetingConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedApps(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedAppsRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedPublishers(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedPublishersRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedSites(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedSitesRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def suspend(
                self,
                *,
                name: str,
                body: SuspendPretargetingConfigRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...

        @typing.type_check_only
        class PublisherConnectionsResource(googleapiclient.discovery.Resource):
            def batchApprove(
                self,
                *,
                parent: str,
                body: BatchApprovePublisherConnectionsRequest = ...,
                **kwargs: typing.Any
            ) -> BatchApprovePublisherConnectionsResponseHttpRequest: ...
            def batchReject(
                self,
                *,
                parent: str,
                body: BatchRejectPublisherConnectionsRequest = ...,
                **kwargs: typing.Any
            ) -> BatchRejectPublisherConnectionsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PublisherConnectionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPublisherConnectionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPublisherConnectionsResponseHttpRequest,
                previous_response: ListPublisherConnectionsResponse,
            ) -> ListPublisherConnectionsResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> BidderHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListBiddersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListBiddersResponseHttpRequest,
            previous_response: ListBiddersResponse,
        ) -> ListBiddersResponseHttpRequest | None: ...
        def creatives(self) -> CreativesResource: ...
        def endpoints(self) -> EndpointsResource: ...
        def pretargetingConfigs(self) -> PretargetingConfigsResource: ...
        def publisherConnections(self) -> PublisherConnectionsResource: ...

    @typing.type_check_only
    class BuyersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Creative = ..., **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListCreativesResponseHttpRequest,
                previous_response: ListCreativesResponse,
            ) -> ListCreativesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Creative = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...

        @typing.type_check_only
        class UserListsResource(googleapiclient.discovery.Resource):
            def close(self, *, name: str, body: CloseUserListRequest = ..., **kwargs: typing.Any) -> UserListHttpRequest: ...  # type: ignore
            def create(
                self, *, parent: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def getRemarketingTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GetRemarketingTagResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListUserListsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListUserListsResponseHttpRequest,
                previous_response: ListUserListsResponse,
            ) -> ListUserListsResponseHttpRequest | None: ...
            def open(
                self,
                *,
                name: str,
                body: OpenUserListRequest = ...,
                **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def update(
                self, *, name: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> BuyerHttpRequest: ...
        def getRemarketingTag(
            self, *, name: str, **kwargs: typing.Any
        ) -> GetRemarketingTagResponseHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListBuyersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListBuyersResponseHttpRequest,
            previous_response: ListBuyersResponse,
        ) -> ListBuyersResponseHttpRequest | None: ...
        def creatives(self) -> CreativesResource: ...
        def userLists(self) -> UserListsResource: ...

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
    def bidders(self) -> BiddersResource: ...
    def buyers(self) -> BuyersResource: ...

@typing.type_check_only
class BatchApprovePublisherConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchApprovePublisherConnectionsResponse: ...

@typing.type_check_only
class BatchRejectPublisherConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchRejectPublisherConnectionsResponse: ...

@typing.type_check_only
class BidderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Bidder: ...

@typing.type_check_only
class BuyerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Buyer: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Creative: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EndpointHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Endpoint: ...

@typing.type_check_only
class GetRemarketingTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetRemarketingTagResponse: ...

@typing.type_check_only
class ListBiddersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBiddersResponse: ...

@typing.type_check_only
class ListBuyersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBuyersResponse: ...

@typing.type_check_only
class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCreativesResponse: ...

@typing.type_check_only
class ListEndpointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEndpointsResponse: ...

@typing.type_check_only
class ListPretargetingConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPretargetingConfigsResponse: ...

@typing.type_check_only
class ListPublisherConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPublisherConnectionsResponse: ...

@typing.type_check_only
class ListUserListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUserListsResponse: ...

@typing.type_check_only
class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PretargetingConfig: ...

@typing.type_check_only
class PublisherConnectionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublisherConnection: ...

@typing.type_check_only
class UserListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserList: ...

@typing.type_check_only
class WatchCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> WatchCreativesResponse: ...
