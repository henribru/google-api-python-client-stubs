import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdExchangeBuyerResource(googleapiclient.discovery.Resource):
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
    class BillingInfoResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> BillingInfoHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> BillingInfoListHttpRequest: ...
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
            accountId: typing.Union[int, typing.List[int]] = ...,
            buyerCreativeId: typing.Union[str, typing.List[str]] = ...,
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
    class MarketplaceprivateauctionResource(googleapiclient.discovery.Resource):
        def updateproposal(
            self,
            *,
            privateAuctionId: str,
            body: UpdatePrivateAuctionProposalRequest = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
    class ProductsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, productId: str, **kwargs: typing.Any
        ) -> ProductHttpRequest: ...
        def search(
            self, *, pqlQuery: str = ..., **kwargs: typing.Any
        ) -> GetOffersResponseHttpRequest: ...
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
    class PubprofilesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, accountId: int, **kwargs: typing.Any
        ) -> GetPublisherProfilesByAccountIdResponseHttpRequest: ...
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

class GetOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOrdersResponse: ...

class PerformanceReportListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PerformanceReportList: ...

class AccountsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsList: ...

class PretargetingConfigListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PretargetingConfigList: ...

class BillingInfoListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BillingInfoList: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class GetOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOrderDealsResponse: ...

class BudgetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Budget: ...

class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PretargetingConfig: ...

class GetOffersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOffersResponse: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

class EditAllOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EditAllOrderDealsResponse: ...

class GetPublisherProfilesByAccountIdResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetPublisherProfilesByAccountIdResponse: ...

class AddOrderNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddOrderNotesResponse: ...

class CreateOrdersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateOrdersResponse: ...

class CreativeDealIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativeDealIds: ...

class AddOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AddOrderDealsResponse: ...

class GetOrderNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetOrderNotesResponse: ...

class BillingInfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BillingInfo: ...

class DeleteOrderDealsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeleteOrderDealsResponse: ...

class ProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Proposal: ...

class CreativesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativesList: ...
