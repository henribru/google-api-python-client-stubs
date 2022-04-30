import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AdExchangeBuyerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: int, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> AccountsListHttpRequest: ...
        def patch(
            self,
            *,
            id: int,
            body: Account = ...,
            confirmUnsafeAccountChange: bool = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self,
            *,
            id: int,
            body: Account = ...,
            confirmUnsafeAccountChange: bool = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...

    @typing.type_check_only
    class BillingInfoResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> BillingInfoHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> BillingInfoListHttpRequest: ...

    @typing.type_check_only
    class BudgetResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: str, billingId: str, **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...
        def patch(
            self,
            *,
            accountId: str,
            billingId: str,
            body: Budget = ...,
            **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...
        def update(
            self,
            *,
            accountId: str,
            billingId: str,
            body: Budget = ...,
            **kwargs: typing.Any
        ) -> BudgetHttpRequest: ...

    @typing.type_check_only
    class CreativesResource(googleapiclient.discovery.Resource):
        def addDeal(
            self,
            *,
            accountId: int,
            buyerCreativeId: str,
            dealId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, accountId: int, buyerCreativeId: str, **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def insert(
            self, *, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def list(
            self,
            *,
            accountId: int | _list[int] = ...,
            buyerCreativeId: str | _list[str] = ...,
            dealsStatusFilter: typing_extensions.Literal[
                "approved", "conditionally_approved", "disapproved", "not_checked"
            ] = ...,
            maxResults: int = ...,
            openAuctionStatusFilter: typing_extensions.Literal[
                "approved", "conditionally_approved", "disapproved", "not_checked"
            ] = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CreativesListHttpRequest: ...
        def list_next(
            self,
            previous_request: CreativesListHttpRequest,
            previous_response: CreativesList,
        ) -> CreativesListHttpRequest | None: ...
        def listDeals(
            self, *, accountId: int, buyerCreativeId: str, **kwargs: typing.Any
        ) -> CreativeDealIdsHttpRequest: ...
        def removeDeal(
            self,
            *,
            accountId: int,
            buyerCreativeId: str,
            dealId: str,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class MarketplacedealsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            proposalId: str,
            body: DeleteOrderDealsRequest = ...,
            **kwargs: typing.Any
        ) -> DeleteOrderDealsResponseHttpRequest: ...
        def insert(
            self,
            *,
            proposalId: str,
            body: AddOrderDealsRequest = ...,
            **kwargs: typing.Any
        ) -> AddOrderDealsResponseHttpRequest: ...
        def list(
            self, *, proposalId: str, pqlQuery: str = ..., **kwargs: typing.Any
        ) -> GetOrderDealsResponseHttpRequest: ...
        def update(
            self,
            *,
            proposalId: str,
            body: EditAllOrderDealsRequest = ...,
            **kwargs: typing.Any
        ) -> EditAllOrderDealsResponseHttpRequest: ...

    @typing.type_check_only
    class MarketplacenotesResource(googleapiclient.discovery.Resource):
        def insert(
            self,
            *,
            proposalId: str,
            body: AddOrderNotesRequest = ...,
            **kwargs: typing.Any
        ) -> AddOrderNotesResponseHttpRequest: ...
        def list(
            self, *, proposalId: str, pqlQuery: str = ..., **kwargs: typing.Any
        ) -> GetOrderNotesResponseHttpRequest: ...

    @typing.type_check_only
    class MarketplaceprivateauctionResource(googleapiclient.discovery.Resource):
        def updateproposal(
            self,
            *,
            privateAuctionId: str,
            body: UpdatePrivateAuctionProposalRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class PerformanceReportResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            accountId: str,
            endDateTime: str,
            startDateTime: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> PerformanceReportListHttpRequest: ...

    @typing.type_check_only
    class PretargetingConfigResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, accountId: str, configId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, accountId: str, configId: str, **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def insert(
            self,
            *,
            accountId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def list(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> PretargetingConfigListHttpRequest: ...
        def patch(
            self,
            *,
            accountId: str,
            configId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...
        def update(
            self,
            *,
            accountId: str,
            configId: str,
            body: PretargetingConfig = ...,
            **kwargs: typing.Any
        ) -> PretargetingConfigHttpRequest: ...

    @typing.type_check_only
    class ProductsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, productId: str, **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def search(
            self, *, pqlQuery: str = ..., **kwargs: typing.Any
        ) -> GetOffersResponseHttpRequest: ...

    @typing.type_check_only
    class ProposalsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, proposalId: str, **kwargs: typing.Any
        ) -> ProposalHttpRequest: ...
        def insert(
            self, *, body: CreateOrdersRequest = ..., **kwargs: typing.Any
        ) -> CreateOrdersResponseHttpRequest: ...
        def patch(
            self,
            *,
            proposalId: str,
            revisionNumber: str,
            updateAction: typing_extensions.Literal[
                "accept",
                "cancel",
                "propose",
                "proposeAndAccept",
                "unknownAction",
                "updateNonTerms",
            ],
            body: Proposal = ...,
            **kwargs: typing.Any
        ) -> ProposalHttpRequest: ...
        def search(
            self, *, pqlQuery: str = ..., **kwargs: typing.Any
        ) -> GetOrdersResponseHttpRequest: ...
        def setupcomplete(
            self, *, proposalId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def update(
            self,
            *,
            proposalId: str,
            revisionNumber: str,
            updateAction: typing_extensions.Literal[
                "accept",
                "cancel",
                "propose",
                "proposeAndAccept",
                "unknownAction",
                "updateNonTerms",
            ],
            body: Proposal = ...,
            **kwargs: typing.Any
        ) -> ProposalHttpRequest: ...

    @typing.type_check_only
    class PubprofilesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> GetPublisherProfilesByAccountIdResponseHttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def billingInfo(self) -> BillingInfoResource: ...
    def budget(self) -> BudgetResource: ...
    def creatives(self) -> CreativesResource: ...
    def marketplacedeals(self) -> MarketplacedealsResource: ...
    def marketplacenotes(self) -> MarketplacenotesResource: ...
    def marketplaceprivateauction(self) -> MarketplaceprivateauctionResource: ...
    def performanceReport(self) -> PerformanceReportResource: ...
    def pretargetingConfig(self) -> PretargetingConfigResource: ...
    def products(self) -> ProductsResource: ...
    def proposals(self) -> ProposalsResource: ...
    def pubprofiles(self) -> PubprofilesResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class AccountsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AccountsList: ...

@typing.type_check_only
class AddOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AddOrderDealsResponse: ...

@typing.type_check_only
class AddOrderNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AddOrderNotesResponse: ...

@typing.type_check_only
class BillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BillingInfo: ...

@typing.type_check_only
class BillingInfoListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BillingInfoList: ...

@typing.type_check_only
class BudgetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Budget: ...

@typing.type_check_only
class CreateOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreateOrdersResponse: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Creative: ...

@typing.type_check_only
class CreativeDealIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativeDealIds: ...

@typing.type_check_only
class CreativesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreativesList: ...

@typing.type_check_only
class DeleteOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeleteOrderDealsResponse: ...

@typing.type_check_only
class EditAllOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EditAllOrderDealsResponse: ...

@typing.type_check_only
class GetOffersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOffersResponse: ...

@typing.type_check_only
class GetOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOrderDealsResponse: ...

@typing.type_check_only
class GetOrderNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOrderNotesResponse: ...

@typing.type_check_only
class GetOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetOrdersResponse: ...

@typing.type_check_only
class GetPublisherProfilesByAccountIdResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetPublisherProfilesByAccountIdResponse: ...

@typing.type_check_only
class PerformanceReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PerformanceReportList: ...

@typing.type_check_only
class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PretargetingConfig: ...

@typing.type_check_only
class PretargetingConfigListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PretargetingConfigList: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Product: ...

@typing.type_check_only
class ProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Proposal: ...
