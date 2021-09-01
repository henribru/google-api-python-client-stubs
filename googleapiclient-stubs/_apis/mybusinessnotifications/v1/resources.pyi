import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class MyBusinessNotificationSettingsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        def getNotificationSetting(
            self, *, name: str, **kwargs: typing.Any
        ) -> NotificationSettingHttpRequest: ...
        def updateNotificationSetting(
            self,
            *,
            name: str,
            body: NotificationSetting = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> NotificationSettingHttpRequest: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class NotificationSettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> NotificationSetting: ...
