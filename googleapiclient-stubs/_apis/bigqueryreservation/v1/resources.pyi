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
            class CapacityCommitmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: CapacityCommitment = ...,
                    capacityCommitmentId: str = ...,
                    enforceSingleAdminProjectPerOrg: bool = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def delete(
                    self, *, name: str, force: bool = ..., **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCapacityCommitmentsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCapacityCommitmentsResponseHttpRequest,
                    previous_response: ListCapacityCommitmentsResponse,
                ) -> ListCapacityCommitmentsResponseHttpRequest | None: ...
                def merge(
                    self,
                    *,
                    parent: str,
                    body: MergeCapacityCommitmentsRequest = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CapacityCommitment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def split(
                    self,
                    *,
                    name: str,
                    body: SplitCapacityCommitmentRequest = ...,
                    **kwargs: typing.Any
                ) -> SplitCapacityCommitmentResponseHttpRequest: ...

            @typing.type_check_only
            class ReservationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AssignmentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Assignment = ...,
                        assignmentId: str = ...,
                        **kwargs: typing.Any
                    ) -> AssignmentHttpRequest: ...
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
                    ) -> ListAssignmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAssignmentsResponseHttpRequest,
                        previous_response: ListAssignmentsResponse,
                    ) -> ListAssignmentsResponseHttpRequest | None: ...
                    def move(
                        self,
                        *,
                        name: str,
                        body: MoveAssignmentRequest = ...,
                        **kwargs: typing.Any
                    ) -> AssignmentHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Assignment = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> AssignmentHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Reservation = ...,
                    reservationId: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
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
                def assignments(self) -> AssignmentsResource: ...

            def getBiReservation(
                self, *, name: str, **kwargs: typing.Any
            ) -> BiReservationHttpRequest: ...
            def searchAllAssignments(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> SearchAllAssignmentsResponseHttpRequest: ...
            def searchAllAssignments_next(
                self,
                previous_request: SearchAllAssignmentsResponseHttpRequest,
                previous_response: SearchAllAssignmentsResponse,
            ) -> SearchAllAssignmentsResponseHttpRequest | None: ...
            def searchAssignments(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> SearchAssignmentsResponseHttpRequest: ...
            def searchAssignments_next(
                self,
                previous_request: SearchAssignmentsResponseHttpRequest,
                previous_response: SearchAssignmentsResponse,
            ) -> SearchAssignmentsResponseHttpRequest | None: ...
            def updateBiReservation(
                self,
                *,
                name: str,
                body: BiReservation = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> BiReservationHttpRequest: ...
            def capacityCommitments(self) -> CapacityCommitmentsResource: ...
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
class AssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Assignment: ...

@typing.type_check_only
class BiReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BiReservation: ...

@typing.type_check_only
class CapacityCommitmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CapacityCommitment: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAssignmentsResponse: ...

@typing.type_check_only
class ListCapacityCommitmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListCapacityCommitmentsResponse: ...

@typing.type_check_only
class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReservationsResponse: ...

@typing.type_check_only
class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Reservation: ...

@typing.type_check_only
class SearchAllAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchAllAssignmentsResponse: ...

@typing.type_check_only
class SearchAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchAssignmentsResponse: ...

@typing.type_check_only
class SplitCapacityCommitmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SplitCapacityCommitmentResponse: ...
