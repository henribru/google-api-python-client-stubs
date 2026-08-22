import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class Oauth2Resource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UserinfoResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class V2Resource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class MeResource(googleapiclient.discovery.Resource):
                def get(self, **kwargs: typing.Any) -> UserinfoHttpRequest: ...

            def me(self) -> MeResource: ...

        def get(self, **kwargs: typing.Any) -> UserinfoHttpRequest: ...
        def v2(self) -> V2Resource: ...

    def tokeninfo(
        self,
        *,
        access_token: str | None = ...,
        alt: typing.Literal["json"] | None = ...,
        fields: str | None = ...,
        id_token: str | None = ...,
        key: str | None = ...,
        oauth_token: str | None = ...,
        pp: str | None = ...,
        prettyPrint: bool | None = ...,
        quotaUser: str | None = ...,
        strict: str | None = ...,
        trace: str | None = ...,
        userIp: str | None = ...,
        userip: str | None = ...,
        **kwargs: typing.Any,
    ) -> TokeninfoHttpRequest: ...
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
    def userinfo(self) -> UserinfoResource: ...

@typing.type_check_only
class TokeninfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Tokeninfo: ...

@typing.type_check_only
class UserinfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Userinfo: ...
