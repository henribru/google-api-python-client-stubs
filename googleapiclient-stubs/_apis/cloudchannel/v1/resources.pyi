import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudchannelResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChannelPartnerLinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1ChannelPartnerLink = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal["UNSPECIFIED", "BASIC", "FULL"] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal["UNSPECIFIED", "BASIC", "FULL"] = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudChannelV1UpdateChannelPartnerLinkRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ChannelPartnerLinkHttpRequest: ...
        @typing.type_check_only
        class CustomersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EntitlementsResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ActivateEntitlementRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1CancelEntitlementRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeOffer(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeOfferRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeParameters(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeParametersRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def changeRenewalSettings(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1ChangeRenewalSettingsRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudChannelV1CreateEntitlementRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudChannelV1EntitlementHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudChannelV1ListEntitlementsResponseHttpRequest: ...
                def startPaidService(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1StartPaidServiceRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def suspend(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudChannelV1SuspendEntitlementRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1Customer = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListCustomersResponseHttpRequest: ...
            def listPurchasableOffers(
                self,
                *,
                customer: str,
                changeOfferPurchase_entitlement: str = ...,
                changeOfferPurchase_newSku: str = ...,
                createEntitlementPurchase_sku: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest: ...
            def listPurchasableSkus(
                self,
                *,
                customer: str,
                changeOfferPurchase_changeType: typing_extensions.Literal[
                    "CHANGE_TYPE_UNSPECIFIED", "UPGRADE", "DOWNGRADE"
                ] = ...,
                changeOfferPurchase_entitlement: str = ...,
                createEntitlementPurchase_product: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudChannelV1Customer = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1CustomerHttpRequest: ...
            def provisionCloudIdentity(
                self,
                *,
                customer: str,
                body: GoogleCloudChannelV1ProvisionCloudIdentityRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def transferEntitlements(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1TransferEntitlementsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def transferEntitlementsToGoogle(
                self,
                *,
                parent: str,
                body: GoogleCloudChannelV1TransferEntitlementsToGoogleRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def entitlements(self) -> EntitlementsResource: ...
        @typing.type_check_only
        class OffersResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListOffersResponseHttpRequest: ...
        def checkCloudIdentityAccountsExist(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1CheckCloudIdentityAccountsExistRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseHttpRequest: ...
        def listSubscribers(
            self,
            *,
            account: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1ListSubscribersResponseHttpRequest: ...
        def listTransferableOffers(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1ListTransferableOffersRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest: ...
        def listTransferableSkus(
            self,
            *,
            parent: str,
            body: GoogleCloudChannelV1ListTransferableSkusRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest: ...
        def register(
            self,
            *,
            account: str,
            body: GoogleCloudChannelV1RegisterSubscriberRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1RegisterSubscriberResponseHttpRequest: ...
        def unregister(
            self,
            *,
            account: str,
            body: GoogleCloudChannelV1UnregisterSubscriberRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1UnregisterSubscriberResponseHttpRequest: ...
        def channelPartnerLinks(self) -> ChannelPartnerLinksResource: ...
        def customers(self) -> CustomersResource: ...
        def offers(self) -> OffersResource: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self,
            *,
            name: str,
            body: GoogleLongrunningCancelOperationRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
    @typing.type_check_only
    class ProductsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SkusResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                account: str = ...,
                languageCode: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudChannelV1ListSkusResponseHttpRequest: ...
        def list(
            self,
            *,
            account: str = ...,
            languageCode: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudChannelV1ListProductsResponseHttpRequest: ...
        def skus(self) -> SkusResource: ...
    def accounts(self) -> AccountsResource: ...
    def operations(self) -> OperationsResource: ...
    def products(self) -> ProductsResource: ...

@typing.type_check_only
class GoogleCloudChannelV1ChannelPartnerLinkHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ChannelPartnerLink: ...

@typing.type_check_only
class GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1CheckCloudIdentityAccountsExistResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1Customer: ...

@typing.type_check_only
class GoogleCloudChannelV1EntitlementHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1Entitlement: ...

@typing.type_check_only
class GoogleCloudChannelV1ListChannelPartnerLinksResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListChannelPartnerLinksResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListCustomersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListCustomersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListEntitlementsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListEntitlementsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListProductsResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListPurchasableOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListPurchasableSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListPurchasableSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSkusResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListSubscribersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListSubscribersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableOffersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListTransferableOffersResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1ListTransferableSkusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1ListTransferableSkusResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1RegisterSubscriberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1RegisterSubscriberResponse: ...

@typing.type_check_only
class GoogleCloudChannelV1UnregisterSubscriberResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudChannelV1UnregisterSubscriberResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
