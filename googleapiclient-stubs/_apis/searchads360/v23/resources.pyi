import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SA360Resource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AudienceInsightsResource(googleapiclient.discovery.Resource):
        def listInsightsEligibleDates(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesResponseHttpRequest: ...

    @typing.type_check_only
    class CustomersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AdGroupCriterionCustomizersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignGoalConfigsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerCustomizersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerCustomizersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerCustomizersResponseHttpRequest: ...

        @typing.type_check_only
        class GoalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class AccountBudgetProposalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResponseHttpRequest: ...

        @typing.type_check_only
        class AccountLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__CreateAccountLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__CreateAccountLinkResponseHttpRequest
            ): ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAccountLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAccountLinkResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AdGroupAdLabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupAdsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupAdsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAdGroupAdsResponseHttpRequest
            ): ...
            def removeAutomaticallyCreatedAssets(
                self,
                *,
                adGroupAd: str,
                body: GoogleAdsSearchads360V23Services__RemoveAutomaticallyCreatedAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleProtobuf__EmptyHttpRequest: ...

        @typing.type_check_only
        class AdGroupAssetSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupAssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupAssetsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAdGroupAssetsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AdGroupBidModifiersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupCriteriaResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupCriterionLabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupCustomizersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersResponseHttpRequest: ...

        @typing.type_check_only
        class AdGroupLabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupLabelsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAdGroupLabelsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AdGroupsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdGroupsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAdGroupsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AdParametersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdParametersRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAdParametersResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AdsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAdsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAdsResponseHttpRequest: ...

        @typing.type_check_only
        class AssetGroupAssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsResponseHttpRequest: ...

        @typing.type_check_only
        class AssetGroupListingGroupFiltersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersResponseHttpRequest: ...

        @typing.type_check_only
        class AssetGroupSignalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsResponseHttpRequest: ...

        @typing.type_check_only
        class AssetGroupsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetGroupsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAssetGroupsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AssetSetAssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetSetAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAssetSetAssetsResponseHttpRequest: ...

        @typing.type_check_only
        class AssetSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetSetsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAssetSetsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class AssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateAssetsResponseHttpRequest: ...

        @typing.type_check_only
        class AudiencesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateAudiencesRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateAudiencesResponseHttpRequest
            ): ...

        @typing.type_check_only
        class BatchJobsResource(googleapiclient.discovery.Resource):
            def addOperations(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__AddBatchJobOperationsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__AddBatchJobOperationsResponseHttpRequest: ...
            def listResults(
                self,
                *,
                resourceName: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                responseContentType: typing_extensions.Literal[
                    "UNSPECIFIED", "RESOURCE_NAME_ONLY", "MUTABLE_RESOURCE"
                ]
                | None = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__ListBatchJobResultsResponseHttpRequest
            ): ...
            def listResults_next(
                self,
                previous_request: GoogleAdsSearchads360V23Services__ListBatchJobResultsResponseHttpRequest,
                previous_response: GoogleAdsSearchads360V23Services__ListBatchJobResultsResponse,
            ) -> (
                GoogleAdsSearchads360V23Services__ListBatchJobResultsResponseHttpRequest
                | None
            ): ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateBatchJobRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateBatchJobResponseHttpRequest
            ): ...
            def run(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__RunBatchJobRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunning__OperationHttpRequest: ...

        @typing.type_check_only
        class BiddingDataExclusionsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResponseHttpRequest: ...

        @typing.type_check_only
        class BiddingSeasonalityAdjustmentsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResponseHttpRequest: ...

        @typing.type_check_only
        class BiddingStrategiesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateBiddingStrategiesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateBiddingStrategiesResponseHttpRequest: ...

        @typing.type_check_only
        class BillingSetupsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateBillingSetupRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateBillingSetupResponseHttpRequest
            ): ...

        @typing.type_check_only
        class CampaignAssetSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignAssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignAssetsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignBidModifiersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignBudgetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignBudgetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignBudgetsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignConversionGoalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignCriteriaResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignCriteriaRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignCriteriaResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignCustomizersResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignCustomizersRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignCustomizersResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignDraftsResource(googleapiclient.discovery.Resource):
            def listAsyncErrors(
                self,
                *,
                resourceName: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponseHttpRequest: ...
            def listAsyncErrors_next(
                self,
                previous_request: GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponseHttpRequest,
                previous_response: GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponse,
            ) -> (
                GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponseHttpRequest
                | None
            ): ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignDraftsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignDraftsResponseHttpRequest: ...
            def promote(
                self,
                *,
                campaignDraft: str,
                body: GoogleAdsSearchads360V23Services__PromoteCampaignDraftRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunning__OperationHttpRequest: ...

        @typing.type_check_only
        class CampaignGroupsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignGroupsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignGroupsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignLabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignLabelsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignLabelsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignLifecycleGoalResource(googleapiclient.discovery.Resource):
            def configureCampaignLifecycleGoals(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignSharedSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsResponseHttpRequest: ...

        @typing.type_check_only
        class CampaignsResource(googleapiclient.discovery.Resource):
            def enablePMaxBrandGuidelines(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesResponseHttpRequest: ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCampaignsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateCampaignsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class ConversionActionsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateConversionActionsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateConversionActionsResponseHttpRequest: ...

        @typing.type_check_only
        class ConversionCustomVariablesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesResponseHttpRequest: ...

        @typing.type_check_only
        class ConversionGoalCampaignConfigsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsResponseHttpRequest: ...

        @typing.type_check_only
        class ConversionValueRuleSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsResponseHttpRequest: ...

        @typing.type_check_only
        class ConversionValueRulesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateConversionValueRulesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateConversionValueRulesResponseHttpRequest: ...

        @typing.type_check_only
        class CustomAudiencesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomAudiencesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomAudiencesResponseHttpRequest: ...

        @typing.type_check_only
        class CustomColumnsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, resourceName: str, **kwargs: typing.Any
            ) -> GoogleAdsSearchads360V23Resources__CustomColumnHttpRequest: ...
            def list(
                self, *, customerId: str, **kwargs: typing.Any
            ) -> (
                GoogleAdsSearchads360V23Services__ListCustomColumnsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class CustomConversionGoalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomInterestsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomInterestsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomInterestsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerAssetSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerAssetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerAssetsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerAssetsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerClientLinksResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerClientLinkRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerConversionGoalsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerLabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerLabelsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerLabelsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerLifecycleGoalResource(googleapiclient.discovery.Resource):
            def configureCustomerLifecycleGoals(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerManagerLinksResource(googleapiclient.discovery.Resource):
            def moveManagerLink(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MoveManagerLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MoveManagerLinkResponseHttpRequest
            ): ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerNegativeCriteriaResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerSkAdNetworkConversionValueSchemasResource(
            googleapiclient.discovery.Resource
        ):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerUserAccessInvitationsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResponseHttpRequest: ...

        @typing.type_check_only
        class CustomerUserAccessesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomerUserAccessRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResponseHttpRequest: ...

        @typing.type_check_only
        class CustomizerAttributesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateCustomizerAttributesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateCustomizerAttributesResponseHttpRequest: ...

        @typing.type_check_only
        class DataLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__CreateDataLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__CreateDataLinkResponseHttpRequest
            ): ...
            def remove(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__RemoveDataLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__RemoveDataLinkResponseHttpRequest
            ): ...
            def update(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__UpdateDataLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__UpdateDataLinkResponseHttpRequest
            ): ...

        @typing.type_check_only
        class ExperimentArmsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateExperimentArmsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateExperimentArmsResponseHttpRequest: ...

        @typing.type_check_only
        class ExperimentsResource(googleapiclient.discovery.Resource):
            def endExperiment(
                self,
                *,
                experiment: str,
                body: GoogleAdsSearchads360V23Services__EndExperimentRequest,
                **kwargs: typing.Any,
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
            def graduateExperiment(
                self,
                *,
                experiment: str,
                body: GoogleAdsSearchads360V23Services__GraduateExperimentRequest,
                **kwargs: typing.Any,
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
            def listExperimentAsyncErrors(
                self,
                *,
                resourceName: str,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponseHttpRequest: ...
            def listExperimentAsyncErrors_next(
                self,
                previous_request: GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponseHttpRequest,
                previous_response: GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponse,
            ) -> (
                GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponseHttpRequest
                | None
            ): ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateExperimentsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateExperimentsResponseHttpRequest
            ): ...
            def promoteExperiment(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__PromoteExperimentRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def scheduleExperiment(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__ScheduleExperimentRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunning__OperationHttpRequest: ...

        @typing.type_check_only
        class IncentivesResource(googleapiclient.discovery.Resource):
            def applyIncentive(
                self,
                *,
                customerId: str,
                selectedIncentiveId: str,
                body: GoogleAdsSearchads360V23Services__ApplyIncentiveRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__ApplyIncentiveResponseHttpRequest
            ): ...

        @typing.type_check_only
        class InvoicesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                customerId: str,
                billingSetup: str | None = ...,
                includeGranularLevelInvoiceDetails: bool | None = ...,
                issueMonth: typing_extensions.Literal[
                    "UNSPECIFIED",
                    "UNKNOWN",
                    "JANUARY",
                    "FEBRUARY",
                    "MARCH",
                    "APRIL",
                    "MAY",
                    "JUNE",
                    "JULY",
                    "AUGUST",
                    "SEPTEMBER",
                    "OCTOBER",
                    "NOVEMBER",
                    "DECEMBER",
                ]
                | None = ...,
                issueYear: str | None = ...,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__ListInvoicesResponseHttpRequest: ...

        @typing.type_check_only
        class KeywordPlanAdGroupKeywordsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsResponseHttpRequest: ...

        @typing.type_check_only
        class KeywordPlanAdGroupsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsResponseHttpRequest: ...

        @typing.type_check_only
        class KeywordPlanCampaignKeywordsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsResponseHttpRequest: ...

        @typing.type_check_only
        class KeywordPlanCampaignsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsResponseHttpRequest: ...

        @typing.type_check_only
        class KeywordPlansResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateKeywordPlansRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateKeywordPlansResponseHttpRequest
            ): ...

        @typing.type_check_only
        class LabelsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateLabelsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateLabelsResponseHttpRequest: ...

        @typing.type_check_only
        class LocalServicesResource(googleapiclient.discovery.Resource):
            def appendLeadConversation(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__AppendLeadConversationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__AppendLeadConversationResponseHttpRequest: ...

        @typing.type_check_only
        class LocalServicesLeadsResource(googleapiclient.discovery.Resource):
            def provideLeadFeedback(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__ProvideLeadFeedbackRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__ProvideLeadFeedbackResponseHttpRequest
            ): ...

        @typing.type_check_only
        class OfflineUserDataJobsResource(googleapiclient.discovery.Resource):
            def addOperations(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsResponseHttpRequest: ...
            def create(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobResponseHttpRequest: ...
            def run(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__RunOfflineUserDataJobRequest,
                **kwargs: typing.Any,
            ) -> GoogleLongrunning__OperationHttpRequest: ...

        @typing.type_check_only
        class PaymentsAccountsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, customerId: str, **kwargs: typing.Any
            ) -> GoogleAdsSearchads360V23Services__ListPaymentsAccountsResponseHttpRequest: ...

        @typing.type_check_only
        class ProductLinkInvitationsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__CreateProductLinkInvitationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__CreateProductLinkInvitationResponseHttpRequest: ...
            def remove(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationResponseHttpRequest: ...
            def update(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationResponseHttpRequest: ...

        @typing.type_check_only
        class ProductLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__CreateProductLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__CreateProductLinkResponseHttpRequest
            ): ...
            def remove(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__RemoveProductLinkRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__RemoveProductLinkResponseHttpRequest
            ): ...

        @typing.type_check_only
        class RecommendationSubscriptionsResource(googleapiclient.discovery.Resource):
            def mutateRecommendationSubscription(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResponseHttpRequest: ...

        @typing.type_check_only
        class RecommendationsResource(googleapiclient.discovery.Resource):
            def apply(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__ApplyRecommendationRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__ApplyRecommendationResponseHttpRequest
            ): ...
            def dismiss(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__DismissRecommendationRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__DismissRecommendationResponseHttpRequest: ...
            def generate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__GenerateRecommendationsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__GenerateRecommendationsResponseHttpRequest: ...

        @typing.type_check_only
        class RemarketingActionsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateRemarketingActionsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateRemarketingActionsResponseHttpRequest: ...

        @typing.type_check_only
        class SearchAds360Resource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateSearchAds360Request,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateSearchAds360ResponseHttpRequest
            ): ...
            def search(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__SearchSearchAds360Request,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__SearchSearchAds360ResponseHttpRequest
            ): ...
            def search_next(
                self,
                previous_request: GoogleAdsSearchads360V23Services__SearchSearchAds360ResponseHttpRequest,
                previous_response: GoogleAdsSearchads360V23Services__SearchSearchAds360Response,
            ) -> (
                GoogleAdsSearchads360V23Services__SearchSearchAds360ResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SharedCriteriaResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateSharedCriteriaRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateSharedCriteriaResponseHttpRequest: ...

        @typing.type_check_only
        class SharedSetsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateSharedSetsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateSharedSetsResponseHttpRequest
            ): ...

        @typing.type_check_only
        class SmartCampaignSettingsResource(googleapiclient.discovery.Resource):
            def getSmartCampaignStatus(
                self, *, resourceName: str, **kwargs: typing.Any
            ) -> GoogleAdsSearchads360V23Services__GetSmartCampaignStatusResponseHttpRequest: ...
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsResponseHttpRequest: ...

        @typing.type_check_only
        class ThirdPartyAppAnalyticsLinksResource(googleapiclient.discovery.Resource):
            def regenerateShareableLinkId(
                self,
                *,
                resourceName: str,
                body: GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdResponseHttpRequest: ...

        @typing.type_check_only
        class UserListCustomerTypesResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesRequest,
                **kwargs: typing.Any,
            ) -> GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesResponseHttpRequest: ...

        @typing.type_check_only
        class UserListsResource(googleapiclient.discovery.Resource):
            def mutate(
                self,
                *,
                customerId: str,
                body: GoogleAdsSearchads360V23Services__MutateUserListsRequest,
                **kwargs: typing.Any,
            ) -> (
                GoogleAdsSearchads360V23Services__MutateUserListsResponseHttpRequest
            ): ...

        def createCustomerClient(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__CreateCustomerClientRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__CreateCustomerClientResponseHttpRequest
        ): ...
        def generateAdGroupThemes(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateAdGroupThemesRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__GenerateAdGroupThemesResponseHttpRequest
        ): ...
        def generateAudienceCompositionInsights(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsResponseHttpRequest: ...
        def generateAudienceDefinition(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionResponseHttpRequest: ...
        def generateAudienceOverlapInsights(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsResponseHttpRequest: ...
        def generateBenchmarksMetrics(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsResponseHttpRequest: ...
        def generateInsightsFinderReport(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportResponseHttpRequest: ...
        def generateKeywordForecastMetrics(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsResponseHttpRequest: ...
        def generateKeywordHistoricalMetrics(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResponseHttpRequest: ...
        def generateKeywordIdeas(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateKeywordIdeasRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponseHttpRequest
        ): ...
        def generateKeywordIdeas_next(
            self,
            previous_request: GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponseHttpRequest,
            previous_response: GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponse,
        ) -> (
            GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponseHttpRequest
            | None
        ): ...
        def generateReachForecast(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateReachForecastRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__GenerateReachForecastResponseHttpRequest
        ): ...
        def generateSuggestedTargetingInsights(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsResponseHttpRequest: ...
        def generateTargetingSuggestionMetrics(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsResponseHttpRequest: ...
        def getIdentityVerification(
            self, *, customerId: str, **kwargs: typing.Any
        ) -> (
            GoogleAdsSearchads360V23Services__GetIdentityVerificationResponseHttpRequest
        ): ...
        def listAccessibleCustomers(
            self, **kwargs: typing.Any
        ) -> (
            GoogleAdsSearchads360V23Services__ListAccessibleCustomersResponseHttpRequest
        ): ...
        def mutate(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__MutateCustomerRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__MutateCustomerResponseHttpRequest: ...
        def removeCampaignAutomaticallyCreatedAsset(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetResponseHttpRequest: ...
        def searchAudienceInsightsAttributes(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesResponseHttpRequest: ...
        def startIdentityVerification(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__StartIdentityVerificationRequest,
            **kwargs: typing.Any,
        ) -> GoogleProtobuf__EmptyHttpRequest: ...
        def suggestKeywordThemes(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__SuggestKeywordThemesRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__SuggestKeywordThemesResponseHttpRequest
        ): ...
        def suggestSmartCampaignAd(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdResponseHttpRequest
        ): ...
        def suggestSmartCampaignBudgetOptions(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsResponseHttpRequest: ...
        def suggestTravelAssets(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__SuggestTravelAssetsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__SuggestTravelAssetsResponseHttpRequest
        ): ...
        def uploadUserData(
            self,
            *,
            customerId: str,
            body: GoogleAdsSearchads360V23Services__UploadUserDataRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__UploadUserDataResponseHttpRequest: ...
        def AdGroupCriterionCustomizers(
            self,
        ) -> AdGroupCriterionCustomizersResource: ...
        def CampaignGoalConfigs(self) -> CampaignGoalConfigsResource: ...
        def CustomerCustomizers(self) -> CustomerCustomizersResource: ...
        def Goals(self) -> GoalsResource: ...
        def accountBudgetProposals(self) -> AccountBudgetProposalsResource: ...
        def accountLinks(self) -> AccountLinksResource: ...
        def adGroupAdLabels(self) -> AdGroupAdLabelsResource: ...
        def adGroupAds(self) -> AdGroupAdsResource: ...
        def adGroupAssetSets(self) -> AdGroupAssetSetsResource: ...
        def adGroupAssets(self) -> AdGroupAssetsResource: ...
        def adGroupBidModifiers(self) -> AdGroupBidModifiersResource: ...
        def adGroupCriteria(self) -> AdGroupCriteriaResource: ...
        def adGroupCriterionLabels(self) -> AdGroupCriterionLabelsResource: ...
        def adGroupCustomizers(self) -> AdGroupCustomizersResource: ...
        def adGroupLabels(self) -> AdGroupLabelsResource: ...
        def adGroups(self) -> AdGroupsResource: ...
        def adParameters(self) -> AdParametersResource: ...
        def ads(self) -> AdsResource: ...
        def assetGroupAssets(self) -> AssetGroupAssetsResource: ...
        def assetGroupListingGroupFilters(
            self,
        ) -> AssetGroupListingGroupFiltersResource: ...
        def assetGroupSignals(self) -> AssetGroupSignalsResource: ...
        def assetGroups(self) -> AssetGroupsResource: ...
        def assetSetAssets(self) -> AssetSetAssetsResource: ...
        def assetSets(self) -> AssetSetsResource: ...
        def assets(self) -> AssetsResource: ...
        def audiences(self) -> AudiencesResource: ...
        def batchJobs(self) -> BatchJobsResource: ...
        def biddingDataExclusions(self) -> BiddingDataExclusionsResource: ...
        def biddingSeasonalityAdjustments(
            self,
        ) -> BiddingSeasonalityAdjustmentsResource: ...
        def biddingStrategies(self) -> BiddingStrategiesResource: ...
        def billingSetups(self) -> BillingSetupsResource: ...
        def campaignAssetSets(self) -> CampaignAssetSetsResource: ...
        def campaignAssets(self) -> CampaignAssetsResource: ...
        def campaignBidModifiers(self) -> CampaignBidModifiersResource: ...
        def campaignBudgets(self) -> CampaignBudgetsResource: ...
        def campaignConversionGoals(self) -> CampaignConversionGoalsResource: ...
        def campaignCriteria(self) -> CampaignCriteriaResource: ...
        def campaignCustomizers(self) -> CampaignCustomizersResource: ...
        def campaignDrafts(self) -> CampaignDraftsResource: ...
        def campaignGroups(self) -> CampaignGroupsResource: ...
        def campaignLabels(self) -> CampaignLabelsResource: ...
        def campaignLifecycleGoal(self) -> CampaignLifecycleGoalResource: ...
        def campaignSharedSets(self) -> CampaignSharedSetsResource: ...
        def campaigns(self) -> CampaignsResource: ...
        def conversionActions(self) -> ConversionActionsResource: ...
        def conversionCustomVariables(self) -> ConversionCustomVariablesResource: ...
        def conversionGoalCampaignConfigs(
            self,
        ) -> ConversionGoalCampaignConfigsResource: ...
        def conversionValueRuleSets(self) -> ConversionValueRuleSetsResource: ...
        def conversionValueRules(self) -> ConversionValueRulesResource: ...
        def customAudiences(self) -> CustomAudiencesResource: ...
        def customColumns(self) -> CustomColumnsResource: ...
        def customConversionGoals(self) -> CustomConversionGoalsResource: ...
        def customInterests(self) -> CustomInterestsResource: ...
        def customerAssetSets(self) -> CustomerAssetSetsResource: ...
        def customerAssets(self) -> CustomerAssetsResource: ...
        def customerClientLinks(self) -> CustomerClientLinksResource: ...
        def customerConversionGoals(self) -> CustomerConversionGoalsResource: ...
        def customerLabels(self) -> CustomerLabelsResource: ...
        def customerLifecycleGoal(self) -> CustomerLifecycleGoalResource: ...
        def customerManagerLinks(self) -> CustomerManagerLinksResource: ...
        def customerNegativeCriteria(self) -> CustomerNegativeCriteriaResource: ...
        def customerSkAdNetworkConversionValueSchemas(
            self,
        ) -> CustomerSkAdNetworkConversionValueSchemasResource: ...
        def customerUserAccessInvitations(
            self,
        ) -> CustomerUserAccessInvitationsResource: ...
        def customerUserAccesses(self) -> CustomerUserAccessesResource: ...
        def customizerAttributes(self) -> CustomizerAttributesResource: ...
        def dataLinks(self) -> DataLinksResource: ...
        def experimentArms(self) -> ExperimentArmsResource: ...
        def experiments(self) -> ExperimentsResource: ...
        def incentives(self) -> IncentivesResource: ...
        def invoices(self) -> InvoicesResource: ...
        def keywordPlanAdGroupKeywords(self) -> KeywordPlanAdGroupKeywordsResource: ...
        def keywordPlanAdGroups(self) -> KeywordPlanAdGroupsResource: ...
        def keywordPlanCampaignKeywords(
            self,
        ) -> KeywordPlanCampaignKeywordsResource: ...
        def keywordPlanCampaigns(self) -> KeywordPlanCampaignsResource: ...
        def keywordPlans(self) -> KeywordPlansResource: ...
        def labels(self) -> LabelsResource: ...
        def localServices(self) -> LocalServicesResource: ...
        def localServicesLeads(self) -> LocalServicesLeadsResource: ...
        def offlineUserDataJobs(self) -> OfflineUserDataJobsResource: ...
        def paymentsAccounts(self) -> PaymentsAccountsResource: ...
        def productLinkInvitations(self) -> ProductLinkInvitationsResource: ...
        def productLinks(self) -> ProductLinksResource: ...
        def recommendationSubscriptions(
            self,
        ) -> RecommendationSubscriptionsResource: ...
        def recommendations(self) -> RecommendationsResource: ...
        def remarketingActions(self) -> RemarketingActionsResource: ...
        def searchAds360(self) -> SearchAds360Resource: ...
        def sharedCriteria(self) -> SharedCriteriaResource: ...
        def sharedSets(self) -> SharedSetsResource: ...
        def smartCampaignSettings(self) -> SmartCampaignSettingsResource: ...
        def thirdPartyAppAnalyticsLinks(
            self,
        ) -> ThirdPartyAppAnalyticsLinksResource: ...
        def userListCustomerTypes(self) -> UserListCustomerTypesResource: ...
        def userLists(self) -> UserListsResource: ...

    @typing.type_check_only
    class GeoTargetConstantsResource(googleapiclient.discovery.Resource):
        def suggest(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsResponseHttpRequest: ...

    @typing.type_check_only
    class IncentivesResource(googleapiclient.discovery.Resource):
        def fetchIncentive(
            self,
            *,
            countryCode: str | None = ...,
            email: str | None = ...,
            languageCode: str | None = ...,
            type: typing_extensions.Literal["UNSPECIFIED", "UNKNOWN", "ACQUISITION"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__FetchIncentiveResponseHttpRequest: ...

    @typing.type_check_only
    class KeywordThemeConstantsResource(googleapiclient.discovery.Resource):
        def suggest(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsResponseHttpRequest: ...

    @typing.type_check_only
    class SearchAds360FieldsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GoogleAdsSearchads360V23Resources__SearchAds360FieldHttpRequest: ...
        def search(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponseHttpRequest,
            previous_response: GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponse,
        ) -> (
            GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponseHttpRequest
            | None
        ): ...

    @typing.type_check_only
    class V23Resource(googleapiclient.discovery.Resource):
        def generateConversionRates(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__GenerateConversionRatesRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__GenerateConversionRatesResponseHttpRequest
        ): ...
        def listBenchmarksAvailableDates(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesResponseHttpRequest: ...
        def listBenchmarksLocations(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListBenchmarksLocationsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListBenchmarksLocationsResponseHttpRequest
        ): ...
        def listBenchmarksProducts(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListBenchmarksProductsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListBenchmarksProductsResponseHttpRequest
        ): ...
        def listBenchmarksSources(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListBenchmarksSourcesRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListBenchmarksSourcesResponseHttpRequest
        ): ...
        def listPlannableLocations(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListPlannableLocationsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListPlannableLocationsResponseHttpRequest
        ): ...
        def listPlannableProducts(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListPlannableProductsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListPlannableProductsResponseHttpRequest
        ): ...
        def listPlannableUserInterests(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListPlannableUserInterestsRequest,
            **kwargs: typing.Any,
        ) -> GoogleAdsSearchads360V23Services__ListPlannableUserInterestsResponseHttpRequest: ...
        def listPlannableUserLists(
            self,
            *,
            body: GoogleAdsSearchads360V23Services__ListPlannableUserListsRequest,
            **kwargs: typing.Any,
        ) -> (
            GoogleAdsSearchads360V23Services__ListPlannableUserListsResponseHttpRequest
        ): ...

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
    def audienceInsights(self) -> AudienceInsightsResource: ...
    def customers(self) -> CustomersResource: ...
    def geoTargetConstants(self) -> GeoTargetConstantsResource: ...
    def incentives(self) -> IncentivesResource: ...
    def keywordThemeConstants(self) -> KeywordThemeConstantsResource: ...
    def searchAds360Fields(self) -> SearchAds360FieldsResource: ...
    def v23(self) -> V23Resource: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__CustomColumnHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Resources__CustomColumn: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Resources__SearchAds360FieldHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Resources__SearchAds360Field: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddBatchJobOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__AddBatchJobOperationsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__AddOfflineUserDataJobOperationsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__AppendLeadConversationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__AppendLeadConversationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyIncentiveResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ApplyIncentiveResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ApplyRecommendationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ApplyRecommendationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ConfigureCampaignLifecycleGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ConfigureCustomerLifecycleGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateAccountLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateAccountLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateCustomerClientResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateCustomerClientResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateDataLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateDataLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateOfflineUserDataJobResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkInvitationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateProductLinkInvitationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__CreateProductLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__CreateProductLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__DismissRecommendationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__DismissRecommendationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__EnablePMaxBrandGuidelinesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__FetchIncentiveResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__FetchIncentiveResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAdGroupThemesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateAdGroupThemesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__GenerateAudienceCompositionInsightsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateAudienceDefinitionResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateAudienceOverlapInsightsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateBenchmarksMetricsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateConversionRatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateConversionRatesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateInsightsFinderReportResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateKeywordForecastMetricsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateKeywordHistoricalMetricsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateKeywordIdeaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateReachForecastResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateReachForecastResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateRecommendationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GenerateRecommendationsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__GenerateSuggestedTargetingInsightsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__GenerateTargetingSuggestionMetricsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GetIdentityVerificationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GetIdentityVerificationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__GetSmartCampaignStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__GetSmartCampaignStatusResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListAccessibleCustomersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListAccessibleCustomersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListAudienceInsightsAttributesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBatchJobResultsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListBatchJobResultsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListBenchmarksAvailableDatesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListBenchmarksLocationsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListBenchmarksProductsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListBenchmarksSourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListBenchmarksSourcesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListCampaignDraftAsyncErrorsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListCustomColumnsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListCustomColumnsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListExperimentAsyncErrorsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListInsightsEligibleDatesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListInvoicesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListInvoicesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPaymentsAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListPaymentsAccountsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListPlannableLocationsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListPlannableProductsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserInterestsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListPlannableUserInterestsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ListPlannableUserListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ListPlannableUserListsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MoveManagerLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MoveManagerLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAccountBudgetProposalResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAccountLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAccountLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAdLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAdsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAdsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAssetSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupBidModifiersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCriteriaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateAdGroupCriterionCustomizersResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCriterionLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupCustomizersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdGroupsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdParametersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdParametersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAdsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAdsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateAssetGroupListingGroupFiltersResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupSignalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetGroupsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetSetAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateAudiencesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBatchJobResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateBatchJobResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateBiddingDataExclusionsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateBiddingSeasonalityAdjustmentsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBiddingStrategiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateBiddingStrategiesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateBillingSetupResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateBillingSetupResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignAssetSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignBidModifiersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignBudgetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignBudgetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignConversionGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCriteriaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignCriteriaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignCustomizersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignCustomizersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignDraftsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignDraftsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignGoalConfigsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignGroupsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignSharedSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCampaignsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCampaignsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateConversionActionsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateConversionCustomVariablesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateConversionGoalCampaignConfigsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateConversionValueRuleSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateConversionValueRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateConversionValueRulesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomAudiencesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomConversionGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomInterestsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomInterestsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerAssetSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerClientLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerConversionGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerCustomizersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerCustomizersResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerManagerLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerNegativeCriteriaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerSkAdNetworkConversionValueSchemaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateCustomerUserAccessInvitationResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomerUserAccessResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateCustomizerAttributesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateCustomizerAttributesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentArmsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateExperimentArmsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateExperimentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateExperimentsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateGoalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateGoalsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupKeywordsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanAdGroupsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignKeywordsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlanCampaignsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateKeywordPlansResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateKeywordPlansResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateLabelsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateRecommendationSubscriptionResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateRemarketingActionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateRemarketingActionsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSearchAds360ResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateSearchAds360Response: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedCriteriaResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateSharedCriteriaResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSharedSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateSharedSetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateSmartCampaignSettingsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateUserListCustomerTypesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__MutateUserListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__MutateUserListsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__ProvideLeadFeedbackResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__ProvideLeadFeedbackResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__RegenerateShareableLinkIdResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__RemoveCampaignAutomaticallyCreatedAssetResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveDataLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__RemoveDataLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__RemoveProductLinkInvitationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__RemoveProductLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__RemoveProductLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SearchSearchAds360FieldsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SearchSearchAds360ResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SearchSearchAds360Response: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SuggestGeoTargetConstantsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SuggestKeywordThemeConstantsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestKeywordThemesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SuggestKeywordThemesResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SuggestSmartCampaignAdResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> (
        GoogleAdsSearchads360V23Services__SuggestSmartCampaignBudgetOptionsResponse
    ): ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__SuggestTravelAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__SuggestTravelAssetsResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateDataLinkResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__UpdateDataLinkResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__UpdateProductLinkInvitationResponse: ...

@typing.type_check_only
class GoogleAdsSearchads360V23Services__UploadUserDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleAdsSearchads360V23Services__UploadUserDataResponse: ...

@typing.type_check_only
class GoogleLongrunning__OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunning__Operation: ...

@typing.type_check_only
class GoogleProtobuf__EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobuf__Empty: ...
