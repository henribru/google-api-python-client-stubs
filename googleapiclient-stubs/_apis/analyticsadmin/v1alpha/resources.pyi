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
        ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest | None: ...

    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class UserLinksResource(googleapiclient.discovery.Resource):
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
            def audit_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaAuditUserLinksResponse,
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest | None: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: str | _list[str] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                notifyNewUser: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListUserLinksResponse,
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...

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
        def searchChangeHistoryEvents(
            self,
            *,
            account: str,
            body: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest: ...
        def searchChangeHistoryEvents_next(
            self,
            previous_request: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponse,
        ) -> GoogleAnalyticsAdminV1alphaSearchChangeHistoryEventsResponseHttpRequest | None: ...
        def userLinks(self) -> UserLinksResource: ...

    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
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
            ) -> GoogleAnalyticsAdminV1alphaListConversionEventsResponseHttpRequest | None: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListCustomDimensionsResponseHttpRequest | None: ...
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
            ) -> GoogleAnalyticsAdminV1alphaListCustomMetricsResponseHttpRequest | None: ...
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
            class MeasurementProtocolSecretsResource(
                googleapiclient.discovery.Resource
            ):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...
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
                ) -> GoogleAnalyticsAdminV1alphaListMeasurementProtocolSecretsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1alphaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1alphaMeasurementProtocolSecretHttpRequest: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListDataStreamsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDataStreamHttpRequest: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponseHttpRequest | None: ...

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
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest: ...
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
            ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaDisplayVideo360AdvertiserLinkHttpRequest: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest | None: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...

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
            ) -> GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse,
            ) -> GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaSearchAds360Link = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaSearchAds360LinkHttpRequest: ...

        @typing.type_check_only
        class UserLinksResource(googleapiclient.discovery.Resource):
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
            def audit_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaAuditUserLinksResponse,
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest | None: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: str | _list[str] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                notifyNewUser: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1alphaListUserLinksResponse,
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...

        def acknowledgeUserDataCollection(
            self,
            *,
            property: str,
            body: GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAcknowledgeUserDataCollectionResponseHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
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
        def audiences(self) -> AudiencesResource: ...
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
        def firebaseLinks(self) -> FirebaseLinksResource: ...
        def googleAdsLinks(self) -> GoogleAdsLinksResource: ...
        def searchAds360Links(self) -> SearchAds360LinksResource: ...
        def userLinks(self) -> UserLinksResource: ...

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
class GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaApproveDisplayVideo360AdvertiserLinkProposalResponse: ...

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
class GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse: ...

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
class GoogleAnalyticsAdminV1alphaListAudiencesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListAudiencesResponse: ...

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
    ) -> GoogleAnalyticsAdminV1alphaListDisplayVideo360AdvertiserLinkProposalsResponse: ...

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
class GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListSearchAds360LinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponse: ...

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
class GoogleAnalyticsAdminV1alphaRunAccessReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaRunAccessReportResponse: ...

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
class GoogleAnalyticsAdminV1alphaUserLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1alphaUserLink: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
