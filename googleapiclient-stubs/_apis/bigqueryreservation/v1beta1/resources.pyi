import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BigQueryReservationResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class CapacityCommitmentsResource(googleapiclient.discovery.Resource):
                def patch(
                    self,
                    *,
                    name: str,
                    body: CapacityCommitment = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListCapacityCommitmentsResponseHttpRequest: ...
                def split(
                    self,
                    *,
                    name: str,
                    body: SplitCapacityCommitmentRequest = ...,
                    **kwargs: typing.Any
                ) -> SplitCapacityCommitmentResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CapacityCommitment = ...,
                    enforceSingleAdminProjectPerOrg: bool = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def merge(
                    self,
                    *,
                    parent: str,
                    body: MergeCapacityCommitmentsRequest = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
            class ReservationsResource(googleapiclient.discovery.Resource):
                class AssignmentsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def move(
                        self,
                        *,
                        name: str,
                        body: MoveAssignmentRequest = ...,
                        **kwargs: typing.Any
                    ) -> AssignmentHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Assignment = ...,
                        **kwargs: typing.Any
                    ) -> AssignmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListAssignmentsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Reservation = ...,
                    updateMask: str = ...,
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
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListReservationsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def assignments(self) -> AssignmentsResource: ...
            def getBiReservation(
                self, *, name: str, **kwargs: typing.Any
            ) -> BiReservationHttpRequest: ...
            def searchAssignments(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                query: str = ...,
                **kwargs: typing.Any
            ) -> SearchAssignmentsResponseHttpRequest: ...
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
    def projects(self) -> ProjectsResource: ...

class CapacityCommitmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CapacityCommitment: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class SplitCapacityCommitmentResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SplitCapacityCommitmentResponse: ...

class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Reservation: ...

class ListAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssignmentsResponse: ...

class SearchAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAssignmentsResponse: ...

class AssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Assignment: ...

class ListCapacityCommitmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCapacityCommitmentsResponse: ...

class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReservationsResponse: ...

class BiReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BiReservation: ...
