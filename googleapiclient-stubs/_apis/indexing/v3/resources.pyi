import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class IndexingResource(googleapiclient.discovery.Resource):
    class UrlNotificationsResource(googleapiclient.discovery.Resource):
        def getMetadata(
            self, *, url: str = ..., **kwargs: typing.Any
        ) -> UrlNotificationMetadataHttpRequest: ...
        def publish(
            self, *, body: UrlNotification = ..., **kwargs: typing.Any
        ) -> PublishUrlNotificationResponseHttpRequest: ...
    def urlNotifications(self) -> UrlNotificationsResource: ...

class PublishUrlNotificationResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishUrlNotificationResponse: ...

class UrlNotificationMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UrlNotificationMetadata: ...
