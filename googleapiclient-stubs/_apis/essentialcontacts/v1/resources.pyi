import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
                notificationCategories: typing.Union[
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
                    ],
                    typing.List[
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
                    ],
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
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
                notificationCategories: typing.Union[
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
                    ],
                    typing.List[
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
                    ],
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
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
                notificationCategories: typing.Union[
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
                    ],
                    typing.List[
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
                    ],
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest: ...
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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ComputeContactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1ComputeContactsResponse: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ContactHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1Contact: ...

@typing.type_check_only
class GoogleCloudEssentialcontactsV1ListContactsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudEssentialcontactsV1ListContactsResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...
