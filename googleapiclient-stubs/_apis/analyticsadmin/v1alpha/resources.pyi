import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GoogleAnalyticsAdminResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountSummariesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1alphaListAccountSummariesResponse,
        ) -> (
            GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest | None
        ): ...

    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccessBindingsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponseHttpRequest
            ): ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: str | _list[str] = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponseHttpRequest
            ): ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponseHttpRequest
            ): ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAccessBinding = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListAccessBindingsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaAccessBinding = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...

        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def getDataSharingSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1alphaListAccountsResponse,
        ) -> GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def provisionAccountTicket(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest: ...
        def runAccessReport(
            self,
            *,
            entity: str,
            body: GoogleAnalyticsAdminV1alphaRunAccessReportRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaRunAccessReportResponseHttpRequest: ...
        def searchChangeHistoryEvents(
            self,
            *,
            account: str,
            body: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest = ...,
            **kwargs: typing.Any
        ) -> (
            GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest
        ): ...
        def searchChangeHistoryEvents_next(
            self,
            previous_request: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse,
        ) -> (
            GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest
            | None
        ): ...
        def accessBindings(self) -> AccessBindingsResource: ...

    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AccessBindingsResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponseHttpRequest
            ): ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: str | _list[str] = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponseHttpRequest
            ): ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsRequest = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponseHttpRequest
            ): ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAccessBinding = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListAccessBindingsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaAccessBinding = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest: ...

        @typing.type_check_only
        class AdSenseLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAdSenseLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAdSenseLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAdSenseLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAdSenseLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListAdSenseLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListAdSenseLinksResponseHttpRequest | None
            ): ...

        @typing.type_check_only
        class AudiencesResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaArchiveAudienceRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAudience = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAudienceHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAudienceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAudiencesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListAudiencesResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListAudiencesResponse,
            ) -> GoogleAnalyticsAdminV1alphaListAudiencesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaAudience = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAudienceHttpRequest: ...

        @typing.type_check_only
        class BigQueryLinksResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBigQueryLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListBigQueryLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListBigQueryLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListBigQueryLinksResponseHttpRequest | None
            ): ...

        @typing.type_check_only
        class ChannelGroupsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaChannelGroup = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaChannelGroupHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaChannelGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListChannelGroupsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListChannelGroupsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListChannelGroupsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListChannelGroupsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaChannelGroup = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaChannelGroupHttpRequest: ...

        @typing.type_check_only
        class ConversionEventsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaConversionEvent = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaConversionEventHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaConversionEventHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListConversionEventsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaConversionEvent = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaConversionEventHttpRequest: ...

        @typing.type_check_only
        class CustomDimensionsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaArchiveCustomDimensionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaCustomDimension = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaCustomDimension = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest: ...

        @typing.type_check_only
        class CustomMetricsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaArchiveCustomMetricRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaCustomMetric = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListCustomMetricsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaCustomMetric = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest: ...

        @typing.type_check_only
        class DataStreamsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EventCreateRulesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaEventCreateRule = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaEventCreateRuleHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaEventCreateRuleHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> (
                    GoogleAnalyticsAdminV1alphaListEventCreateRulesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleAnalyticsAdminV1alphaListEventCreateRulesResponseHttpRequest,
                    previous_response: GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse,
                ) -> (
                    GoogleAnalyticsAdminV1alphaListEventCreateRulesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaEventCreateRule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaEventCreateRuleHttpRequest: ...

            @typing.type_check_only
            class MeasurementProtocolSecretsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> (
                    GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest
                ): ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest,
                    previous_response: GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse,
                ) -> (
                    GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> (
                    GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest
                ): ...

            @typing.type_check_only
            class SKAdNetworkConversionValueSchemaResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchemaHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchemaHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponseHttpRequest,
                    previous_response: GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse,
                ) -> (
                    GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchemaHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataStreamHttpRequest: ...
            def getDataRedactionSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataRedactionSettingsHttpRequest: ...
            def getEnhancedMeasurementSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def getGlobalSiteTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListDataStreamsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListDataStreamsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListDataStreamsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListDataStreamsResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataStreamHttpRequest: ...
            def updateDataRedactionSettings(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaDataRedactionSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataRedactionSettingsHttpRequest: ...
            def updateEnhancedMeasurementSettings(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def eventCreateRules(self) -> EventCreateRulesResource: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...
            def sKAdNetworkConversionValueSchema(
                self,
            ) -> SKAdNetworkConversionValueSchemaResource: ...

        @typing.type_check_only
        class DisplayVideo360AdvertiserLinkProposalsResource(
            googleapiclient.discovery.Resource
        ):
            def approve(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponseHttpRequest: ...
            def cancel(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaCancelDisplayVideo360AdvertiserLinkProposalRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposalHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposalHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposalHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class DisplayVideo360AdvertiserLinksResource(
            googleapiclient.discovery.Resource
        ):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest
            ): ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest
            ): ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest
            ): ...

        @typing.type_check_only
        class ExpandedDataSetsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaExpandedDataSet = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaExpandedDataSetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaExpandedDataSetHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaExpandedDataSet = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaExpandedDataSetHttpRequest: ...

        @typing.type_check_only
        class FirebaseLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaFirebaseLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest | None
            ): ...

        @typing.type_check_only
        class GoogleAdsLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...

        @typing.type_check_only
        class RollupPropertySourceLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaRollupPropertySourceLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaRollupPropertySourceLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaRollupPropertySourceLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponseHttpRequest
                | None
            ): ...

        @typing.type_check_only
        class SearchAds360LinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaSearchAds360Link = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSearchAds360LinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSearchAds360LinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> (
                GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest
            ): ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaSearchAds360Link = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSearchAds360LinkHttpRequest: ...

        @typing.type_check_only
        class SubpropertyEventFiltersResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaSubpropertyEventFilter = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSubpropertyEventFilterHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSubpropertyEventFilterHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse,
            ) -> (
                GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponseHttpRequest
                | None
            ): ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaSubpropertyEventFilter = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSubpropertyEventFilterHttpRequest: ...

        def acknowledgeUserDataCollection(
            self,
            *,
            property: str,
            body: GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest = ...,
            **kwargs: typing.Any
        ) -> (
            GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponseHttpRequest
        ): ...
        def create(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def createConnectedSiteTag(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaCreateConnectedSiteTagRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaCreateConnectedSiteTagResponseHttpRequest: ...
        def createRollupProperty(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaCreateRollupPropertyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponseHttpRequest: ...
        def createSubproperty(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaCreateSubpropertyRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaCreateSubpropertyResponseHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def deleteConnectedSiteTag(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaDeleteConnectedSiteTagRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def fetchAutomatedGa4ConfigurationOptOut(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutResponseHttpRequest: ...
        def fetchConnectedGa4Property(
            self, *, property: str = ..., **kwargs: typing.Any
        ) -> (
            GoogleAnalyticsAdminV1alphaFetchConnectedGa4PropertyResponseHttpRequest
        ): ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def getAttributionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAttributionSettingsHttpRequest: ...
        def getDataRetentionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaDataRetentionSettingsHttpRequest: ...
        def getGoogleSignalsSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1alphaListPropertiesResponse,
        ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest | None: ...
        def listConnectedSiteTags(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaListConnectedSiteTagsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListConnectedSiteTagsResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def runAccessReport(
            self,
            *,
            entity: str,
            body: GoogleAnalyticsAdminV1alphaRunAccessReportRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaRunAccessReportResponseHttpRequest: ...
        def setAutomatedGa4ConfigurationOptOut(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutResponseHttpRequest: ...
        def updateAttributionSettings(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaAttributionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAttributionSettingsHttpRequest: ...
        def updateDataRetentionSettings(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaDataRetentionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaDataRetentionSettingsHttpRequest: ...
        def updateGoogleSignalsSettings(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaGoogleSignalsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest: ...
        def accessBindings(self) -> AccessBindingsResource: ...
        def adSenseLinks(self) -> AdSenseLinksResource: ...
        def audiences(self) -> AudiencesResource: ...
        def bigQueryLinks(self) -> BigQueryLinksResource: ...
        def channelGroups(self) -> ChannelGroupsResource: ...
        def conversionEvents(self) -> ConversionEventsResource: ...
        def customDimensions(self) -> CustomDimensionsResource: ...
        def customMetrics(self) -> CustomMetricsResource: ...
        def dataStreams(self) -> DataStreamsResource: ...
        def displayVideo360AdvertiserLinkProposals(
            self,
        ) -> DisplayVideo360AdvertiserLinkProposalsResource: ...
        def displayVideo360AdvertiserLinks(
            self,
        ) -> DisplayVideo360AdvertiserLinksResource: ...
        def expandedDataSets(self) -> ExpandedDataSetsResource: ...
        def firebaseLinks(self) -> FirebaseLinksResource: ...
        def googleAdsLinks(self) -> GoogleAdsLinksResource: ...
        def rollupPropertySourceLinks(self) -> RollupPropertySourceLinksResource: ...
        def searchAds360Links(self) -> SearchAds360LinksResource: ...
        def subpropertyEventFilters(self) -> SubpropertyEventFiltersResource: ...

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
    def accountSummaries(self) -> AccountSummariesResource: ...
    def accounts(self) -> AccountsResource: ...
    def properties(self) -> PropertiesResource: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccessBindingHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAccessBinding: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAccount: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAdSenseLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAdSenseLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> (
        GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse
    ): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAttributionSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAttributionSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaAudienceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAudience: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchCreateAccessBindingsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchGetAccessBindingsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchUpdateAccessBindingsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBigQueryLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBigQueryLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaChannelGroupHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaChannelGroup: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaConversionEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaConversionEvent: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateConnectedSiteTagResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCreateConnectedSiteTagResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCreateRollupPropertyResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCreateSubpropertyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCreateSubpropertyResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomDimensionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCustomDimension: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaCustomMetricHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaCustomMetric: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRedactionSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDataRedactionSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataRetentionSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDataRetentionSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDataSharingSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDataStream: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposalHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkProposal: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaEventCreateRuleHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaEventCreateRule: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaExpandedDataSetHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaExpandedDataSet: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaFetchAutomatedGa4ConfigurationOptOutResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFetchConnectedGa4PropertyResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaFetchConnectedGa4PropertyResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaFirebaseLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTag: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaGoogleSignalsSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaGoogleSignalsSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccessBindingsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAccessBindingsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAccountsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAdSenseLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAdSenseLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAudiencesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListBigQueryLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListBigQueryLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListChannelGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListChannelGroupsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConnectedSiteTagsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListConnectedSiteTagsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListConversionEventsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListCustomDimensionsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListCustomMetricsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListDataStreamsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> (
        GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse
    ): ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListEventCreateRulesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListEventCreateRulesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListExpandedDataSetsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListRollupPropertySourceLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListSKAdNetworkConversionValueSchemasResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListSubpropertyEventFiltersResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaPropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaProperty: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRollupPropertySourceLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaRollupPropertySourceLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaRunAccessReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaRunAccessReportResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchemaHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchAds360LinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSearchAds360Link: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSetAutomatedGa4ConfigurationOptOutResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaSubpropertyEventFilterHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaSubpropertyEventFilter: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
