import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BigQueryReservationResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            class ReservationGrantsResource(googleapiclient.discovery.Resource):
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
                def create(
                    self,
                    *,
                    parent: str,
                    body: ReservationGrant = ...,
                    **kwargs: typing.Any
                ) -> ReservationGrantHttpRequest: ...
            class ReservationsResource(googleapiclient.discovery.Resource):
                class SlotPoolsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> SlotPoolHttpRequest: ...
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
                    ) -> ListSlotPoolsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Reservation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReservationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def createReservation(
                    self,
                    *,
                    parent: str,
                    body: Reservation = ...,
                    reservationId: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def create(
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
                def slotPools(self) -> SlotPoolsResource: ...
            def searchReservationGrants(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> SearchReservationGrantsResponseHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def reservationGrants(self) -> ReservationGrantsResource: ...
            def reservations(self) -> ReservationsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListSlotPoolsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSlotPoolsResponse: ...

class SlotPoolHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SlotPool: ...

class ReservationGrantHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReservationGrant: ...

class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Reservation: ...

class ListReservationGrantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReservationGrantsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReservationsResponse: ...

class SearchReservationGrantsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchReservationGrantsResponse: ...
