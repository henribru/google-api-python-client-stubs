import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AdvisorynotificationsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class NotificationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudAdvisorynotificationsV1NotificationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "NOTIFICATION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest,
                    previous_response: GoogleCloudAdvisorynotificationsV1ListNotificationsResponse,
                ) -> (
                    GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest
                    | None
                ): ...

            def getSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudAdvisorynotificationsV1SettingsHttpRequest: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: GoogleCloudAdvisorynotificationsV1Settings = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAdvisorynotificationsV1SettingsHttpRequest: ...
            def notifications(self) -> NotificationsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class NotificationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, languageCode: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudAdvisorynotificationsV1NotificationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    languageCode: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    view: typing_extensions.Literal[
                        "NOTIFICATION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest,
                    previous_response: GoogleCloudAdvisorynotificationsV1ListNotificationsResponse,
                ) -> (
                    GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest
                    | None
                ): ...

            def getSettings(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudAdvisorynotificationsV1SettingsHttpRequest: ...
            def updateSettings(
                self,
                *,
                name: str,
                body: GoogleCloudAdvisorynotificationsV1Settings = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudAdvisorynotificationsV1SettingsHttpRequest: ...
            def notifications(self) -> NotificationsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1ListNotificationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAdvisorynotificationsV1ListNotificationsResponse: ...

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1NotificationHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAdvisorynotificationsV1Notification: ...

@typing.type_check_only
class GoogleCloudAdvisorynotificationsV1SettingsHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAdvisorynotificationsV1Settings: ...
