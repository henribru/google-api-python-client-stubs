import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AuthorizedBuyersMarketplaceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BiddersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class FinalizedDealsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListFinalizedDealsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListFinalizedDealsResponseHttpRequest,
                previous_response: ListFinalizedDealsResponse,
            ) -> ListFinalizedDealsResponseHttpRequest | None: ...

        def finalizedDeals(self) -> FinalizedDealsResource: ...

    @typing.type_check_only
    class BuyersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AuctionPackagesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> AuctionPackageHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAuctionPackagesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAuctionPackagesResponseHttpRequest,
                previous_response: ListAuctionPackagesResponse,
            ) -> ListAuctionPackagesResponseHttpRequest | None: ...
            def subscribe(
                self,
                *,
                name: str,
                body: SubscribeAuctionPackageRequest = ...,
                **kwargs: typing.Any
            ) -> AuctionPackageHttpRequest: ...
            def subscribeClients(
                self,
                *,
                auctionPackage: str,
                body: SubscribeClientsRequest = ...,
                **kwargs: typing.Any
            ) -> AuctionPackageHttpRequest: ...
            def unsubscribe(
                self,
                *,
                name: str,
                body: UnsubscribeAuctionPackageRequest = ...,
                **kwargs: typing.Any
            ) -> AuctionPackageHttpRequest: ...
            def unsubscribeClients(
                self,
                *,
                auctionPackage: str,
                body: UnsubscribeClientsRequest = ...,
                **kwargs: typing.Any
            ) -> AuctionPackageHttpRequest: ...

        @typing.type_check_only
        class ClientsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class UsersResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: ActivateClientUserRequest = ...,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def create(
                    self, *, parent: str, body: ClientUser = ..., **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def deactivate(
                    self,
                    *,
                    name: str,
                    body: DeactivateClientUserRequest = ...,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListClientUsersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListClientUsersResponseHttpRequest,
                    previous_response: ListClientUsersResponse,
                ) -> ListClientUsersResponseHttpRequest | None: ...

            def activate(
                self,
                *,
                name: str,
                body: ActivateClientRequest = ...,
                **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def create(
                self, *, parent: str, body: Client = ..., **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def deactivate(
                self,
                *,
                name: str,
                body: DeactivateClientRequest = ...,
                **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ClientHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListClientsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListClientsResponseHttpRequest,
                previous_response: ListClientsResponse,
            ) -> ListClientsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Client = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def users(self) -> UsersResource: ...

        @typing.type_check_only
        class FinalizedDealsResource(googleapiclient.discovery.Resource):
            def addCreative(
                self, *, deal: str, body: AddCreativeRequest = ..., **kwargs: typing.Any
            ) -> FinalizedDealHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> FinalizedDealHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                orderBy: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListFinalizedDealsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListFinalizedDealsResponseHttpRequest,
                previous_response: ListFinalizedDealsResponse,
            ) -> ListFinalizedDealsResponseHttpRequest | None: ...
            def pause(
                self,
                *,
                name: str,
                body: PauseFinalizedDealRequest = ...,
                **kwargs: typing.Any
            ) -> FinalizedDealHttpRequest: ...
            def resume(
                self,
                *,
                name: str,
                body: ResumeFinalizedDealRequest = ...,
                **kwargs: typing.Any
            ) -> FinalizedDealHttpRequest: ...
            def setReadyToServe(
                self,
                *,
                deal: str,
                body: SetReadyToServeRequest = ...,
                **kwargs: typing.Any
            ) -> FinalizedDealHttpRequest: ...

        @typing.type_check_only
        class ProposalsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DealsResource(googleapiclient.discovery.Resource):
                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: BatchUpdateDealsRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchUpdateDealsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DealHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDealsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDealsResponseHttpRequest,
                    previous_response: ListDealsResponse,
                ) -> ListDealsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Deal = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> DealHttpRequest: ...

            def accept(
                self,
                *,
                name: str,
                body: AcceptProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def addNote(
                self, *, proposal: str, body: AddNoteRequest = ..., **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def cancelNegotiation(
                self,
                *,
                proposal: str,
                body: CancelNegotiationRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProposalsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProposalsResponseHttpRequest,
                previous_response: ListProposalsResponse,
            ) -> ListProposalsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Proposal = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def sendRfp(
                self, *, buyer: str, body: SendRfpRequest = ..., **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def deals(self) -> DealsResource: ...

        @typing.type_check_only
        class PublisherProfilesResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PublisherProfileHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPublisherProfilesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPublisherProfilesResponseHttpRequest,
                previous_response: ListPublisherProfilesResponse,
            ) -> ListPublisherProfilesResponseHttpRequest | None: ...

        def auctionPackages(self) -> AuctionPackagesResource: ...
        def clients(self) -> ClientsResource: ...
        def finalizedDeals(self) -> FinalizedDealsResource: ...
        def proposals(self) -> ProposalsResource: ...
        def publisherProfiles(self) -> PublisherProfilesResource: ...

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
class AuctionPackageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AuctionPackage: ...

@typing.type_check_only
class BatchUpdateDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUpdateDealsResponse: ...

@typing.type_check_only
class ClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Client: ...

@typing.type_check_only
class ClientUserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ClientUser: ...

@typing.type_check_only
class DealHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Deal: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FinalizedDealHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FinalizedDeal: ...

@typing.type_check_only
class ListAuctionPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAuctionPackagesResponse: ...

@typing.type_check_only
class ListClientUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClientUsersResponse: ...

@typing.type_check_only
class ListClientsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListClientsResponse: ...

@typing.type_check_only
class ListDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDealsResponse: ...

@typing.type_check_only
class ListFinalizedDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFinalizedDealsResponse: ...

@typing.type_check_only
class ListProposalsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProposalsResponse: ...

@typing.type_check_only
class ListPublisherProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPublisherProfilesResponse: ...

@typing.type_check_only
class ProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Proposal: ...

@typing.type_check_only
class PublisherProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublisherProfile: ...
