import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdExchangeBuyerIIResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        class ProposalsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, accountId: str, body: Proposal = ..., **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def cancelNegotiation(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: CancelNegotiationRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: Proposal = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def pause(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: PauseProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def addNote(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: AddNoteRequest = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                filter: str = ...,
                pageSize: int = ...,
                filterSyntax: typing_extensions.Literal[
                    "FILTER_SYNTAX_UNSPECIFIED", "PQL", "LIST_FILTER"
                ] = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProposalsResponseHttpRequest: ...
            def completeSetup(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: CompleteSetupRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def resume(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: ResumeProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def get(
                self, *, accountId: str, proposalId: str, **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
            def accept(
                self,
                *,
                accountId: str,
                proposalId: str,
                body: AcceptProposalRequest = ...,
                **kwargs: typing.Any
            ) -> ProposalHttpRequest: ...
        class PublisherProfilesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListPublisherProfilesResponseHttpRequest: ...
            def get(
                self, *, accountId: str, publisherProfileId: str, **kwargs: typing.Any
            ) -> PublisherProfileHttpRequest: ...
        class ClientsResource(googleapiclient.discovery.Resource):
            class UsersResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    userId: str,
                    body: ClientUser = ...,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    userId: str,
                    **kwargs: typing.Any
                ) -> ClientUserHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListClientUsersResponseHttpRequest: ...
            class InvitationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListClientUserInvitationsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    invitationId: str,
                    **kwargs: typing.Any
                ) -> ClientUserInvitationHttpRequest: ...
                def create(
                    self,
                    *,
                    accountId: str,
                    clientAccountId: str,
                    body: ClientUserInvitation = ...,
                    **kwargs: typing.Any
                ) -> ClientUserInvitationHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                partnerClientId: str = ...,
                **kwargs: typing.Any
            ) -> ListClientsResponseHttpRequest: ...
            def create(
                self, *, accountId: str, body: Client = ..., **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def get(
                self, *, accountId: str, clientAccountId: str, **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                clientAccountId: str,
                body: Client = ...,
                **kwargs: typing.Any
            ) -> ClientHttpRequest: ...
            def users(self) -> UsersResource: ...
            def invitations(self) -> InvitationsResource: ...
        class CreativesResource(googleapiclient.discovery.Resource):
            class DealAssociationsResource(googleapiclient.discovery.Resource):
                def add(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    body: AddDealAssociationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def remove(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    body: RemoveDealAssociationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    creativeId: str,
                    pageToken: str = ...,
                    query: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListDealAssociationsResponseHttpRequest: ...
            def list(
                self,
                *,
                accountId: str,
                query: str = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: Creative = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def get(
                self, *, accountId: str, creativeId: str, **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def watch(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: WatchCreativeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                accountId: str,
                body: Creative = ...,
                duplicateIdMode: typing_extensions.Literal[
                    "NO_DUPLICATES", "FORCE_ENABLE_DUPLICATE_IDS"
                ] = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def stopWatching(
                self,
                *,
                accountId: str,
                creativeId: str,
                body: StopWatchingCreativeRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def dealAssociations(self) -> DealAssociationsResource: ...
        class ProductsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProductsResponseHttpRequest: ...
            def get(
                self, *, accountId: str, productId: str, **kwargs: typing.Any
            ) -> ProductHttpRequest: ...
        class FinalizedProposalsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                accountId: str,
                filterSyntax: typing_extensions.Literal[
                    "FILTER_SYNTAX_UNSPECIFIED", "PQL", "LIST_FILTER"
                ] = ...,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProposalsResponseHttpRequest: ...
        def proposals(self) -> ProposalsResource: ...
        def publisherProfiles(self) -> PublisherProfilesResource: ...
        def clients(self) -> ClientsResource: ...
        def creatives(self) -> CreativesResource: ...
        def products(self) -> ProductsResource: ...
        def finalizedProposals(self) -> FinalizedProposalsResource: ...
    class BiddersResource(googleapiclient.discovery.Resource):
        class FilterSetsResource(googleapiclient.discovery.Resource):
            class BidResponseErrorsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListBidResponseErrorsResponseHttpRequest: ...
            class FilteredBidsResource(googleapiclient.discovery.Resource):
                class DetailsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        creativeStatusId: int,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListCreativeStatusBreakdownByDetailResponseHttpRequest: ...
                class CreativesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        creativeStatusId: int,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListCreativeStatusBreakdownByCreativeResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListFilteredBidsResponseHttpRequest: ...
                def details(self) -> DetailsResource: ...
                def creatives(self) -> CreativesResource: ...
            class FilteredBidRequestsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListFilteredBidRequestsResponseHttpRequest: ...
            class LosingBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListLosingBidsResponseHttpRequest: ...
            class BidResponsesWithoutBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListBidResponsesWithoutBidsResponseHttpRequest: ...
            class BidMetricsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBidMetricsResponseHttpRequest: ...
            class ImpressionMetricsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListImpressionMetricsResponseHttpRequest: ...
            class NonBillableWinningBidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    filterSetName: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListNonBillableWinningBidsResponseHttpRequest: ...
            def list(
                self,
                *,
                ownerName: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListFilterSetsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> FilterSetHttpRequest: ...
            def create(
                self,
                *,
                ownerName: str,
                body: FilterSet = ...,
                isTransient: bool = ...,
                **kwargs: typing.Any
            ) -> FilterSetHttpRequest: ...
            def bidResponseErrors(self) -> BidResponseErrorsResource: ...
            def filteredBids(self) -> FilteredBidsResource: ...
            def filteredBidRequests(self) -> FilteredBidRequestsResource: ...
            def losingBids(self) -> LosingBidsResource: ...
            def bidResponsesWithoutBids(self) -> BidResponsesWithoutBidsResource: ...
            def bidMetrics(self) -> BidMetricsResource: ...
            def impressionMetrics(self) -> ImpressionMetricsResource: ...
            def nonBillableWinningBids(self) -> NonBillableWinningBidsResource: ...
        class AccountsResource(googleapiclient.discovery.Resource):
            class FilterSetsResource(googleapiclient.discovery.Resource):
                class NonBillableWinningBidsResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListNonBillableWinningBidsResponseHttpRequest: ...
                class BidResponseErrorsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListBidResponseErrorsResponseHttpRequest: ...
                class ImpressionMetricsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListImpressionMetricsResponseHttpRequest: ...
                class BidMetricsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListBidMetricsResponseHttpRequest: ...
                class BidResponsesWithoutBidsResource(
                    googleapiclient.discovery.Resource
                ):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListBidResponsesWithoutBidsResponseHttpRequest: ...
                class FilteredBidsResource(googleapiclient.discovery.Resource):
                    class DetailsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            filterSetName: str,
                            creativeStatusId: int,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> ListCreativeStatusBreakdownByDetailResponseHttpRequest: ...
                    class CreativesResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            filterSetName: str,
                            creativeStatusId: int,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> ListCreativeStatusBreakdownByCreativeResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListFilteredBidsResponseHttpRequest: ...
                    def details(self) -> DetailsResource: ...
                    def creatives(self) -> CreativesResource: ...
                class LosingBidsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListLosingBidsResponseHttpRequest: ...
                class FilteredBidRequestsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        filterSetName: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListFilteredBidRequestsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    ownerName: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListFilterSetsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    ownerName: str,
                    body: FilterSet = ...,
                    isTransient: bool = ...,
                    **kwargs: typing.Any
                ) -> FilterSetHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> FilterSetHttpRequest: ...
                def nonBillableWinningBids(self) -> NonBillableWinningBidsResource: ...
                def bidResponseErrors(self) -> BidResponseErrorsResource: ...
                def impressionMetrics(self) -> ImpressionMetricsResource: ...
                def bidMetrics(self) -> BidMetricsResource: ...
                def bidResponsesWithoutBids(
                    self,
                ) -> BidResponsesWithoutBidsResource: ...
                def filteredBids(self) -> FilteredBidsResource: ...
                def losingBids(self) -> LosingBidsResource: ...
                def filteredBidRequests(self) -> FilteredBidRequestsResource: ...
            def filterSets(self) -> FilterSetsResource: ...
        def filterSets(self) -> FilterSetsResource: ...
        def accounts(self) -> AccountsResource: ...
    def accounts(self) -> AccountsResource: ...
    def bidders(self) -> BiddersResource: ...

class ListFilteredBidRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilteredBidRequestsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListClientUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientUsersResponse: ...

class ListNonBillableWinningBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNonBillableWinningBidsResponse: ...

class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Note: ...

class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductsResponse: ...

class ListProposalsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProposalsResponse: ...

class ListBidMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidMetricsResponse: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class ListDealAssociationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDealAssociationsResponse: ...

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

class ListClientsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientsResponse: ...

class ListCreativeStatusBreakdownByCreativeResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativeStatusBreakdownByCreativeResponse: ...

class ListPublisherProfilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPublisherProfilesResponse: ...

class ListImpressionMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListImpressionMetricsResponse: ...

class PublisherProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublisherProfile: ...

class ListFilteredBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilteredBidsResponse: ...

class ListBidResponseErrorsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidResponseErrorsResponse: ...

class ListCreativeStatusBreakdownByDetailResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativeStatusBreakdownByDetailResponse: ...

class ClientHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Client: ...

class ClientUserInvitationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientUserInvitation: ...

class ListBidResponsesWithoutBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBidResponsesWithoutBidsResponse: ...

class FilterSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FilterSet: ...

class ListClientUserInvitationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListClientUserInvitationsResponse: ...

class ClientUserHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ClientUser: ...

class ProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Proposal: ...

class ListFilterSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFilterSetsResponse: ...

class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCreativesResponse: ...

class ListLosingBidsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLosingBidsResponse: ...
