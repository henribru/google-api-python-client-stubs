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
        ) -> GoogleAnalyticsAdminV1betaListAccountSummariesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1betaListAccountSummariesResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1betaListAccountSummariesResponse,
        ) -> GoogleAnalyticsAdminV1betaListAccountSummariesResponseHttpRequest | None: ...

    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaAccountHttpRequest: ...
        def getDataSharingSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaDataSharingSettingsHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaListAccountsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1betaListAccountsResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1betaListAccountsResponse,
        ) -> GoogleAnalyticsAdminV1betaListAccountsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1betaAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaAccountHttpRequest: ...
        def provisionAccountTicket(
            self,
            *,
            body: GoogleAnalyticsAdminV1betaProvisionAccountTicketRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseHttpRequest: ...
        def searchChangeHistoryEvents(
            self,
            *,
            account: str,
            body: GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseHttpRequest: ...
        def searchChangeHistoryEvents_next(
            self,
            previous_request: GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse,
        ) -> GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseHttpRequest | None: ...

    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConversionEventsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaConversionEvent = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaConversionEventHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaConversionEventHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaListConversionEventsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListConversionEventsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListConversionEventsResponse,
            ) -> GoogleAnalyticsAdminV1betaListConversionEventsResponseHttpRequest | None: ...

        @typing.type_check_only
        class CustomDimensionsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaArchiveCustomDimensionRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaCustomDimension = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomDimensionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomDimensionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaListCustomDimensionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListCustomDimensionsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListCustomDimensionsResponse,
            ) -> GoogleAnalyticsAdminV1betaListCustomDimensionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaCustomDimension = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomDimensionHttpRequest: ...

        @typing.type_check_only
        class CustomMetricsResource(googleapiclient.discovery.Resource):
            def archive(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaArchiveCustomMetricRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaCustomMetric = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomMetricHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaListCustomMetricsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListCustomMetricsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListCustomMetricsResponse,
            ) -> GoogleAnalyticsAdminV1betaListCustomMetricsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaCustomMetric = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaCustomMetricHttpRequest: ...

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
                    body: GoogleAnalyticsAdminV1betaMeasurementProtocolSecret = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1betaMeasurementProtocolSecretHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1betaMeasurementProtocolSecretHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseHttpRequest,
                    previous_response: GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse,
                ) -> GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleAnalyticsAdminV1betaMeasurementProtocolSecret = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleAnalyticsAdminV1betaMeasurementProtocolSecretHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaListDataStreamsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListDataStreamsResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListDataStreamsResponse,
            ) -> GoogleAnalyticsAdminV1betaListDataStreamsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaDataStreamHttpRequest: ...
            def measurementProtocolSecrets(
                self,
            ) -> MeasurementProtocolSecretsResource: ...

        @typing.type_check_only
        class FirebaseLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaFirebaseLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaFirebaseLinkHttpRequest: ...
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
            ) -> GoogleAnalyticsAdminV1betaListFirebaseLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListFirebaseLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListFirebaseLinksResponse,
            ) -> GoogleAnalyticsAdminV1betaListFirebaseLinksResponseHttpRequest | None: ...

        @typing.type_check_only
        class GoogleAdsLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1betaGoogleAdsLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaGoogleAdsLinkHttpRequest: ...
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
            ) -> GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseHttpRequest,
                previous_response: GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse,
            ) -> GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1betaGoogleAdsLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1betaGoogleAdsLinkHttpRequest: ...

        def acknowledgeUserDataCollection(
            self,
            *,
            property: str,
            body: GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleAnalyticsAdminV1betaProperty = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaPropertyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaPropertyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaPropertyHttpRequest: ...
        def getDataRetentionSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaDataRetentionSettingsHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaListPropertiesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAnalyticsAdminV1betaListPropertiesResponseHttpRequest,
            previous_response: GoogleAnalyticsAdminV1betaListPropertiesResponse,
        ) -> GoogleAnalyticsAdminV1betaListPropertiesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1betaProperty = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaPropertyHttpRequest: ...
        def updateDataRetentionSettings(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1betaDataRetentionSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1betaDataRetentionSettingsHttpRequest: ...
        def conversionEvents(self) -> ConversionEventsResource: ...
        def customDimensions(self) -> CustomDimensionsResource: ...
        def customMetrics(self) -> CustomMetricsResource: ...
        def dataStreams(self) -> DataStreamsResource: ...
        def firebaseLinks(self) -> FirebaseLinksResource: ...
        def googleAdsLinks(self) -> GoogleAdsLinksResource: ...

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
class GoogleAnalyticsAdminV1betaAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaAccount: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaAcknowledgeUserDataCollectionResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaConversionEventHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaConversionEvent: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomDimensionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaCustomDimension: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaCustomMetricHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaCustomMetric: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataRetentionSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaDataRetentionSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataSharingSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaDataSharingSettings: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaDataStreamHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaDataStream: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaFirebaseLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaFirebaseLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaGoogleAdsLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaGoogleAdsLink: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListAccountSummariesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListAccountsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListConversionEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListConversionEventsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomDimensionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListCustomDimensionsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListCustomMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListCustomMetricsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListDataStreamsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListFirebaseLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListFirebaseLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListGoogleAdsLinksResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListMeasurementProtocolSecretsResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaListPropertiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaListPropertiesResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaMeasurementProtocolSecretHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaMeasurementProtocolSecret: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaPropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaProperty: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaProvisionAccountTicketResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaProvisionAccountTicketResponse: ...

@typing.type_check_only
class GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAnalyticsAdminV1betaSearchChangeHistoryEventsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
