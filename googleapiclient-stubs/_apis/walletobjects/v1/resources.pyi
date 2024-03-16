import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class WalletobjectsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EventticketclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> EventTicketClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> EventTicketClassHttpRequest: ...
        def insert(
            self, *, body: EventTicketClass = ..., **kwargs: typing.Any
        ) -> EventTicketClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> EventTicketClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: EventTicketClass = ..., **kwargs: typing.Any
        ) -> EventTicketClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: EventTicketClass = ..., **kwargs: typing.Any
        ) -> EventTicketClassHttpRequest: ...

    @typing.type_check_only
    class EventticketobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> EventTicketObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> EventTicketObjectHttpRequest: ...
        def insert(
            self, *, body: EventTicketObject = ..., **kwargs: typing.Any
        ) -> EventTicketObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> EventTicketObjectListResponseHttpRequest: ...
        def modifylinkedofferobjects(
            self,
            *,
            resourceId: str,
            body: ModifyLinkedOfferObjectsRequest = ...,
            **kwargs: typing.Any,
        ) -> EventTicketObjectHttpRequest: ...
        def patch(
            self,
            *,
            resourceId: str,
            body: EventTicketObject = ...,
            **kwargs: typing.Any,
        ) -> EventTicketObjectHttpRequest: ...
        def update(
            self,
            *,
            resourceId: str,
            body: EventTicketObject = ...,
            **kwargs: typing.Any,
        ) -> EventTicketObjectHttpRequest: ...

    @typing.type_check_only
    class FlightclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> FlightClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> FlightClassHttpRequest: ...
        def insert(
            self, *, body: FlightClass = ..., **kwargs: typing.Any
        ) -> FlightClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> FlightClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: FlightClass = ..., **kwargs: typing.Any
        ) -> FlightClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: FlightClass = ..., **kwargs: typing.Any
        ) -> FlightClassHttpRequest: ...

    @typing.type_check_only
    class FlightobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> FlightObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> FlightObjectHttpRequest: ...
        def insert(
            self, *, body: FlightObject = ..., **kwargs: typing.Any
        ) -> FlightObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> FlightObjectListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: FlightObject = ..., **kwargs: typing.Any
        ) -> FlightObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: FlightObject = ..., **kwargs: typing.Any
        ) -> FlightObjectHttpRequest: ...

    @typing.type_check_only
    class GenericclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> GenericClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> GenericClassHttpRequest: ...
        def insert(
            self, *, body: GenericClass = ..., **kwargs: typing.Any
        ) -> GenericClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> GenericClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: GenericClass = ..., **kwargs: typing.Any
        ) -> GenericClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: GenericClass = ..., **kwargs: typing.Any
        ) -> GenericClassHttpRequest: ...

    @typing.type_check_only
    class GenericobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> GenericObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> GenericObjectHttpRequest: ...
        def insert(
            self, *, body: GenericObject = ..., **kwargs: typing.Any
        ) -> GenericObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> GenericObjectListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: GenericObject = ..., **kwargs: typing.Any
        ) -> GenericObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: GenericObject = ..., **kwargs: typing.Any
        ) -> GenericObjectHttpRequest: ...

    @typing.type_check_only
    class GiftcardclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> GiftCardClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> GiftCardClassHttpRequest: ...
        def insert(
            self, *, body: GiftCardClass = ..., **kwargs: typing.Any
        ) -> GiftCardClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> GiftCardClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: GiftCardClass = ..., **kwargs: typing.Any
        ) -> GiftCardClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: GiftCardClass = ..., **kwargs: typing.Any
        ) -> GiftCardClassHttpRequest: ...

    @typing.type_check_only
    class GiftcardobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> GiftCardObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> GiftCardObjectHttpRequest: ...
        def insert(
            self, *, body: GiftCardObject = ..., **kwargs: typing.Any
        ) -> GiftCardObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> GiftCardObjectListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: GiftCardObject = ..., **kwargs: typing.Any
        ) -> GiftCardObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: GiftCardObject = ..., **kwargs: typing.Any
        ) -> GiftCardObjectHttpRequest: ...

    @typing.type_check_only
    class IssuerResource(googleapiclient.discovery.Resource):
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> IssuerHttpRequest: ...
        def insert(
            self, *, body: Issuer = ..., **kwargs: typing.Any
        ) -> IssuerHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> IssuerListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: Issuer = ..., **kwargs: typing.Any
        ) -> IssuerHttpRequest: ...
        def update(
            self, *, resourceId: str, body: Issuer = ..., **kwargs: typing.Any
        ) -> IssuerHttpRequest: ...

    @typing.type_check_only
    class JwtResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, body: JwtResource = ..., **kwargs: typing.Any
        ) -> JwtInsertResponseHttpRequest: ...

    @typing.type_check_only
    class LoyaltyclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> LoyaltyClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> LoyaltyClassHttpRequest: ...
        def insert(
            self, *, body: LoyaltyClass = ..., **kwargs: typing.Any
        ) -> LoyaltyClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> LoyaltyClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: LoyaltyClass = ..., **kwargs: typing.Any
        ) -> LoyaltyClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: LoyaltyClass = ..., **kwargs: typing.Any
        ) -> LoyaltyClassHttpRequest: ...

    @typing.type_check_only
    class LoyaltyobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> LoyaltyObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> LoyaltyObjectHttpRequest: ...
        def insert(
            self, *, body: LoyaltyObject = ..., **kwargs: typing.Any
        ) -> LoyaltyObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> LoyaltyObjectListResponseHttpRequest: ...
        def modifylinkedofferobjects(
            self,
            *,
            resourceId: str,
            body: ModifyLinkedOfferObjectsRequest = ...,
            **kwargs: typing.Any,
        ) -> LoyaltyObjectHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: LoyaltyObject = ..., **kwargs: typing.Any
        ) -> LoyaltyObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: LoyaltyObject = ..., **kwargs: typing.Any
        ) -> LoyaltyObjectHttpRequest: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> MediaHttpRequest: ...
        def download_media(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def upload(
            self,
            *,
            resourceId: str,
            body: TransitObjectUploadRotatingBarcodeValuesRequest = ...,
            **kwargs: typing.Any,
        ) -> TransitObjectUploadRotatingBarcodeValuesResponseHttpRequest: ...

    @typing.type_check_only
    class OfferclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> OfferClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> OfferClassHttpRequest: ...
        def insert(
            self, *, body: OfferClass = ..., **kwargs: typing.Any
        ) -> OfferClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> OfferClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: OfferClass = ..., **kwargs: typing.Any
        ) -> OfferClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: OfferClass = ..., **kwargs: typing.Any
        ) -> OfferClassHttpRequest: ...

    @typing.type_check_only
    class OfferobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> OfferObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> OfferObjectHttpRequest: ...
        def insert(
            self, *, body: OfferObject = ..., **kwargs: typing.Any
        ) -> OfferObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> OfferObjectListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: OfferObject = ..., **kwargs: typing.Any
        ) -> OfferObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: OfferObject = ..., **kwargs: typing.Any
        ) -> OfferObjectHttpRequest: ...

    @typing.type_check_only
    class PermissionsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> PermissionsHttpRequest: ...
        def update(
            self, *, resourceId: str, body: Permissions = ..., **kwargs: typing.Any
        ) -> PermissionsHttpRequest: ...

    @typing.type_check_only
    class SmarttapResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, body: SmartTap = ..., **kwargs: typing.Any
        ) -> SmartTapHttpRequest: ...

    @typing.type_check_only
    class TransitclassResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> TransitClassAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> TransitClassHttpRequest: ...
        def insert(
            self, *, body: TransitClass = ..., **kwargs: typing.Any
        ) -> TransitClassHttpRequest: ...
        def list(
            self,
            *,
            issuerId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> TransitClassListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: TransitClass = ..., **kwargs: typing.Any
        ) -> TransitClassHttpRequest: ...
        def update(
            self, *, resourceId: str, body: TransitClass = ..., **kwargs: typing.Any
        ) -> TransitClassHttpRequest: ...

    @typing.type_check_only
    class TransitobjectResource(googleapiclient.discovery.Resource):
        def addmessage(
            self,
            *,
            resourceId: str,
            body: AddMessageRequest = ...,
            **kwargs: typing.Any,
        ) -> TransitObjectAddMessageResponseHttpRequest: ...
        def get(
            self, *, resourceId: str, **kwargs: typing.Any
        ) -> TransitObjectHttpRequest: ...
        def insert(
            self, *, body: TransitObject = ..., **kwargs: typing.Any
        ) -> TransitObjectHttpRequest: ...
        def list(
            self,
            *,
            classId: str = ...,
            maxResults: int = ...,
            token: str = ...,
            **kwargs: typing.Any,
        ) -> TransitObjectListResponseHttpRequest: ...
        def patch(
            self, *, resourceId: str, body: TransitObject = ..., **kwargs: typing.Any
        ) -> TransitObjectHttpRequest: ...
        def update(
            self, *, resourceId: str, body: TransitObject = ..., **kwargs: typing.Any
        ) -> TransitObjectHttpRequest: ...

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
    def eventticketclass(self) -> EventticketclassResource: ...
    def eventticketobject(self) -> EventticketobjectResource: ...
    def flightclass(self) -> FlightclassResource: ...
    def flightobject(self) -> FlightobjectResource: ...
    def genericclass(self) -> GenericclassResource: ...
    def genericobject(self) -> GenericobjectResource: ...
    def giftcardclass(self) -> GiftcardclassResource: ...
    def giftcardobject(self) -> GiftcardobjectResource: ...
    def issuer(self) -> IssuerResource: ...
    def jwt(self) -> JwtResource: ...
    def loyaltyclass(self) -> LoyaltyclassResource: ...
    def loyaltyobject(self) -> LoyaltyobjectResource: ...
    def media(self) -> MediaResource: ...
    def offerclass(self) -> OfferclassResource: ...
    def offerobject(self) -> OfferobjectResource: ...
    def permissions(self) -> PermissionsResource: ...
    def smarttap(self) -> SmarttapResource: ...
    def transitclass(self) -> TransitclassResource: ...
    def transitobject(self) -> TransitobjectResource: ...

@typing.type_check_only
class EventTicketClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketClass: ...

@typing.type_check_only
class EventTicketClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketClassAddMessageResponse: ...

@typing.type_check_only
class EventTicketClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketClassListResponse: ...

@typing.type_check_only
class EventTicketObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketObject: ...

@typing.type_check_only
class EventTicketObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketObjectAddMessageResponse: ...

@typing.type_check_only
class EventTicketObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EventTicketObjectListResponse: ...

@typing.type_check_only
class FlightClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightClass: ...

@typing.type_check_only
class FlightClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightClassAddMessageResponse: ...

@typing.type_check_only
class FlightClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightClassListResponse: ...

@typing.type_check_only
class FlightObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightObject: ...

@typing.type_check_only
class FlightObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightObjectAddMessageResponse: ...

@typing.type_check_only
class FlightObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FlightObjectListResponse: ...

@typing.type_check_only
class GenericClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericClass: ...

@typing.type_check_only
class GenericClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericClassAddMessageResponse: ...

@typing.type_check_only
class GenericClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericClassListResponse: ...

@typing.type_check_only
class GenericObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericObject: ...

@typing.type_check_only
class GenericObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericObjectAddMessageResponse: ...

@typing.type_check_only
class GenericObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenericObjectListResponse: ...

@typing.type_check_only
class GiftCardClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardClass: ...

@typing.type_check_only
class GiftCardClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardClassAddMessageResponse: ...

@typing.type_check_only
class GiftCardClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardClassListResponse: ...

@typing.type_check_only
class GiftCardObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardObject: ...

@typing.type_check_only
class GiftCardObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardObjectAddMessageResponse: ...

@typing.type_check_only
class GiftCardObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GiftCardObjectListResponse: ...

@typing.type_check_only
class IssuerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Issuer: ...

@typing.type_check_only
class IssuerListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> IssuerListResponse: ...

@typing.type_check_only
class JwtInsertResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> JwtInsertResponse: ...

@typing.type_check_only
class LoyaltyClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyClass: ...

@typing.type_check_only
class LoyaltyClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyClassAddMessageResponse: ...

@typing.type_check_only
class LoyaltyClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyClassListResponse: ...

@typing.type_check_only
class LoyaltyObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyObject: ...

@typing.type_check_only
class LoyaltyObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyObjectAddMessageResponse: ...

@typing.type_check_only
class LoyaltyObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LoyaltyObjectListResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Media: ...

@typing.type_check_only
class OfferClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferClass: ...

@typing.type_check_only
class OfferClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferClassAddMessageResponse: ...

@typing.type_check_only
class OfferClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferClassListResponse: ...

@typing.type_check_only
class OfferObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferObject: ...

@typing.type_check_only
class OfferObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferObjectAddMessageResponse: ...

@typing.type_check_only
class OfferObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> OfferObjectListResponse: ...

@typing.type_check_only
class PermissionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Permissions: ...

@typing.type_check_only
class SmartTapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SmartTap: ...

@typing.type_check_only
class TransitClassHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitClass: ...

@typing.type_check_only
class TransitClassAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitClassAddMessageResponse: ...

@typing.type_check_only
class TransitClassListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitClassListResponse: ...

@typing.type_check_only
class TransitObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitObject: ...

@typing.type_check_only
class TransitObjectAddMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitObjectAddMessageResponse: ...

@typing.type_check_only
class TransitObjectListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitObjectListResponse: ...

@typing.type_check_only
class TransitObjectUploadRotatingBarcodeValuesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TransitObjectUploadRotatingBarcodeValuesResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...
