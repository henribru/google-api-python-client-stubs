import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class IndexingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UrlNotificationsResource(googleapiclient.discovery.Resource):
        def getMetadata(
            self, *, url: str = ..., **kwargs: typing.Any
        ) -> UrlNotificationMetadataHttpRequest: ...
        def publish(
            self, *, body: UrlNotification = ..., **kwargs: typing.Any
        ) -> PublishUrlNotificationResponseHttpRequest: ...
    def urlNotifications(self) -> UrlNotificationsResource: ...

@typing.type_check_only
class PublishUrlNotificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PublishUrlNotificationResponse: ...

@typing.type_check_only
class UrlNotificationMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UrlNotificationMetadata: ...
