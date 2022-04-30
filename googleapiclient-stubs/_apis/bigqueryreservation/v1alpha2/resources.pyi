import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BigQueryReservationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ReservationGrantsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: ReservationGrant = ...,
                    **kwargs: typing.Any
                ) -> ReservationGrantHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReservationGrantsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReservationGrantsResponseHttpRequest,
                    previous_response: ListReservationGrantsResponse,
                ) -> ListReservationGrantsResponseHttpRequest | None: ...

            @typing.type_check_only
            class ReservationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SlotPoolsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SlotPoolHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListSlotPoolsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListSlotPoolsResponseHttpRequest,
                        previous_response: ListSlotPoolsResponse,
                    ) -> ListSlotPoolsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Reservation = ...,
                    reservationId: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def createReservation(
                    self,
                    *,
                    parent: str,
                    body: Reservation = ...,
                    reservationId: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReservationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListReservationsResponseHttpRequest,
                    previous_response: ListReservationsResponse,
                ) -> ListReservationsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Reservation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def slotPools(self) -> SlotPoolsResource: ...

            def searchReservationGrants(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> SearchReservationGrantsResponseHttpRequest: ...
            def searchReservationGrants_next(
                self,
                previous_request: SearchReservationGrantsResponseHttpRequest,
                previous_response: SearchReservationGrantsResponse,
            ) -> SearchReservationGrantsResponseHttpRequest | None: ...
            def operations(self) -> OperationsResource: ...
            def reservationGrants(self) -> ReservationGrantsResource: ...
            def reservations(self) -> ReservationsResource: ...

        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListReservationGrantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReservationGrantsResponse: ...

@typing.type_check_only
class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReservationsResponse: ...

@typing.type_check_only
class ListSlotPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSlotPoolsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Reservation: ...

@typing.type_check_only
class ReservationGrantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReservationGrant: ...

@typing.type_check_only
class SearchReservationGrantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchReservationGrantsResponse: ...

@typing.type_check_only
class SlotPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SlotPool: ...
