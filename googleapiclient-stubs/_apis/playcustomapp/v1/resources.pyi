import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PlaycustomappResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        class CustomAppsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, account: str, body: CustomApp = ..., **kwargs: typing.Any
            ) -> CustomAppHttpRequest: ...
        def customApps(self) -> CustomAppsResource: ...
    def accounts(self) -> AccountsResource: ...

class CustomAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CustomApp: ...
