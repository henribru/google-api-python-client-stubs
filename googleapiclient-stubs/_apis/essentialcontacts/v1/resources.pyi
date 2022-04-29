import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class EssentialcontactsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContactsResource(googleapiclient.discovery.Resource):
            def compute(
                self,
                *,
                parent: str,
                notificationCategories: typing_extensions.Literal[
                    "NOTIFICATION_CATEGORY_UNSPECIFIED",
                    "ALL",
                    "SUSPENSION",
                    "SECURITY",
                    "TECHNICAL",
                    "BILLING",
                    "LEGAL",
                    "PRODUCT_UPDATES",
                    "TECHNICAL_INCIDENTS",
                ]
                | _list[
                    typing_extensions.Literal[
                        "NOTIFICATION_CATEGORY_UNSPECIFIED",
                        "ALL",
                        "SUSPENSION",
                        "SECURITY",
                        "TECHNICAL",
                        "BILLING",
                        "LEGAL",
                        "PRODUCT_UPDATES",
                        "TECHNICAL_INCIDENTS",
                    ]
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
            def compute_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ComputeContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest | None: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ListContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def sendTestMessage(
                self,
                *,
                resource: str,
                body: GoogleCloudEssentialcontactsV1SendTestMessageRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...

        def contacts(self) -> ContactsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContactsResource(googleapiclient.discovery.Resource):
            def compute(
                self,
                *,
                parent: str,
                notificationCategories: typing_extensions.Literal[
                    "NOTIFICATION_CATEGORY_UNSPECIFIED",
                    "ALL",
                    "SUSPENSION",
                    "SECURITY",
                    "TECHNICAL",
                    "BILLING",
                    "LEGAL",
                    "PRODUCT_UPDATES",
                    "TECHNICAL_INCIDENTS",
                ]
                | _list[
                    typing_extensions.Literal[
                        "NOTIFICATION_CATEGORY_UNSPECIFIED",
                        "ALL",
                        "SUSPENSION",
                        "SECURITY",
                        "TECHNICAL",
                        "BILLING",
                        "LEGAL",
                        "PRODUCT_UPDATES",
                        "TECHNICAL_INCIDENTS",
                    ]
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
            def compute_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ComputeContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest | None: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ListContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def sendTestMessage(
                self,
                *,
                resource: str,
                body: GoogleCloudEssentialcontactsV1SendTestMessageRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...

        def contacts(self) -> ContactsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContactsResource(googleapiclient.discovery.Resource):
            def compute(
                self,
                *,
                parent: str,
                notificationCategories: typing_extensions.Literal[
                    "NOTIFICATION_CATEGORY_UNSPECIFIED",
                    "ALL",
                    "SUSPENSION",
                    "SECURITY",
                    "TECHNICAL",
                    "BILLING",
                    "LEGAL",
                    "PRODUCT_UPDATES",
                    "TECHNICAL_INCIDENTS",
                ]
                | _list[
                    typing_extensions.Literal[
                        "NOTIFICATION_CATEGORY_UNSPECIFIED",
                        "ALL",
                        "SUSPENSION",
                        "SECURITY",
                        "TECHNICAL",
                        "BILLING",
                        "LEGAL",
                        "PRODUCT_UPDATES",
                        "TECHNICAL_INCIDENTS",
                    ]
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
            def compute_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ComputeContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest | None: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest,
                previous_response: GoogleCloudEssentialcontactsV1ListContactsResponse,
            ) -> GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudEssentialcontactsV1Contact = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ContactHttpRequest: ...
            def sendTestMessage(
                self,
                *,
                resource: str,
                body: GoogleCloudEssentialcontactsV1SendTestMessageRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...

        def contacts(self) -> ContactsResource: ...

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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponse: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ContactHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1Contact: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1ListContactsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
