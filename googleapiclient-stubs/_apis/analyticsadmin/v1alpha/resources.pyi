import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GoogleAnalyticsAdminResource(googleapiclient.discovery.Resource):
    class AccountSummariesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest: ...
    class AccountsResource(googleapiclient.discovery.Resource):
        class UserLinksResource(googleapiclient.discovery.Resource):
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
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
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def provisionAccountTicket(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProvisionAccountTicketRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaAccount = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaAccountHttpRequest: ...
        def getDataSharingSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            showDeleted: bool = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest: ...
        def userLinks(self) -> UserLinksResource: ...
    class PropertiesResource(googleapiclient.discovery.Resource):
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
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaGoogleAdsLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest: ...
        class AndroidAppDataStreamsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAndroidAppDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaAndroidAppDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
        class WebDataStreamsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaWebDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaWebDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListWebDataStreamsResponseHttpRequest: ...
            def getEnhancedMeasurementSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def updateEnhancedMeasurementSettings(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest: ...
            def getGlobalSiteTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest: ...
        class IosAppDataStreamsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaIosAppDataStream = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaIosAppDataStream = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
        class FirebaseLinksResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def list(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaFirebaseLink = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaFirebaseLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest: ...
        class UserLinksResource(googleapiclient.discovery.Resource):
            def batchCreate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchCreateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest: ...
            def batchUpdate(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest: ...
            def batchGet(
                self,
                *,
                parent: str,
                names: typing.Union[str, typing.List[str]] = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest: ...
            def batchDelete(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaBatchDeleteUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
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
            def patch(
                self,
                *,
                name: str,
                body: GoogleAnalyticsAdminV1alphaUserLink = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaUserLinkHttpRequest: ...
            def audit(
                self,
                *,
                parent: str,
                body: GoogleAnalyticsAdminV1alphaAuditUserLinksRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            filter: str = ...,
            showDeleted: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleAnalyticsAdminV1alphaProperty = ...,
            **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleAnalyticsAdminV1alphaPropertyHttpRequest: ...
        def googleAdsLinks(self) -> GoogleAdsLinksResource: ...
        def androidAppDataStreams(self) -> AndroidAppDataStreamsResource: ...
        def webDataStreams(self) -> WebDataStreamsResource: ...
        def iosAppDataStreams(self) -> IosAppDataStreamsResource: ...
        def firebaseLinks(self) -> FirebaseLinksResource: ...
        def userLinks(self) -> UserLinksResource: ...
    def accountSummaries(self) -> AccountSummariesResource: ...
    def accounts(self) -> AccountsResource: ...
    def properties(self) -> PropertiesResource: ...

class GoogleAnalyticsAdminV1alphaListAccountsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListAccountsResponse: ...

class GoogleAnalyticsAdminV1alphaIosAppDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaIosAppDataStream: ...

class GoogleAnalyticsAdminV1alphaGlobalSiteTagHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaGlobalSiteTag: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleAnalyticsAdminV1alphaListPropertiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListPropertiesResponse: ...

class GoogleAnalyticsAdminV1alphaGoogleAdsLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaGoogleAdsLink: ...

class GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaBatchGetUserLinksResponse: ...

class GoogleAnalyticsAdminV1alphaWebDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaWebDataStream: ...

class GoogleAnalyticsAdminV1alphaListFirebaseLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse: ...

class GoogleAnalyticsAdminV1alphaListAccountSummariesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListAccountSummariesResponse: ...

class GoogleAnalyticsAdminV1alphaListUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListUserLinksResponse: ...

class GoogleAnalyticsAdminV1alphaListWebDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListWebDataStreamsResponse: ...

class GoogleAnalyticsAdminV1alphaAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaAccount: ...

class GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaBatchCreateUserLinksResponse: ...

class GoogleAnalyticsAdminV1alphaPropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaProperty: ...

class GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListIosAppDataStreamsResponse: ...

class GoogleAnalyticsAdminV1alphaFirebaseLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaFirebaseLink: ...

class GoogleAnalyticsAdminV1alphaAuditUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaAuditUserLinksResponse: ...

class GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaEnhancedMeasurementSettings: ...

class GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaProvisionAccountTicketResponse: ...

class GoogleAnalyticsAdminV1alphaAndroidAppDataStreamHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaAndroidAppDataStream: ...

class GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListGoogleAdsLinksResponse: ...

class GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaBatchUpdateUserLinksResponse: ...

class GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaListAndroidAppDataStreamsResponse: ...

class GoogleAnalyticsAdminV1alphaUserLinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaUserLink: ...

class GoogleAnalyticsAdminV1alphaDataSharingSettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleAnalyticsAdminV1alphaDataSharingSettings: ...
