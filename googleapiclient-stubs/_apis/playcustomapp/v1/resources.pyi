import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class PlaycustomappResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CustomAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, account: str, body: CustomApp = ..., **kwargs: typing.Any
            ) -> CustomAppHttpRequest: ...
        def customApps(self) -> CustomAppsResource: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class CustomAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CustomApp: ...
