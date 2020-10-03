import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BigQueryReservationResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class ReservationsResource(googleapiclient.discovery.Resource):
                class AssignmentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListAssignmentsResponseHttpRequest: ...
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
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReservationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Reservation = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ReservationHttpRequest: ...
                def assignments(self) -> AssignmentsResource: ...
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
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListCapacityCommitmentsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def split(
                    self,
                    *,
                    name: str,
                    body: SplitCapacityCommitmentRequest = ...,
                    **kwargs: typing.Any
                ) -> SplitCapacityCommitmentResponseHttpRequest: ...
                def merge(
                    self,
                    *,
                    parent: str,
                    body: MergeCapacityCommitmentsRequest = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: CapacityCommitment = ...,
                    enforceSingleAdminProjectPerOrg: bool = ...,
                    **kwargs: typing.Any
                ) -> CapacityCommitmentHttpRequest: ...
            def getBiReservation(
                self, *, name: str, **kwargs: typing.Any
            ) -> BiReservationHttpRequest: ...
            def searchAllAssignments(
                self,
                *,
                parent: str,
                query: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> SearchAllAssignmentsResponseHttpRequest: ...
            def updateBiReservation(
                self,
                *,
                name: str,
                body: BiReservation = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
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
            def reservations(self) -> ReservationsResource: ...
            def capacityCommitments(self) -> CapacityCommitmentsResource: ...
        def locations(self) -> LocationsResource: ...
    def operations(self) -> OperationsResource: ...
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

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Reservation: ...

class SearchAllAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllAssignmentsResponse: ...

class ListAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssignmentsResponse: ...

class AssignmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Assignment: ...

class BiReservationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BiReservation: ...

class ListCapacityCommitmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListCapacityCommitmentsResponse: ...

class ListReservationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReservationsResponse: ...

class SearchAssignmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAssignmentsResponse: ...
