import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

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
        access_token: str = ...,
        alt: typing_extensions.Literal["json"] = ...,
        fields: str = ...,
        id_token: str = ...,
        key: str = ...,
        oauth_token: str = ...,
        pp: str = ...,
        prettyPrint: bool = ...,
        quotaUser: str = ...,
        strict: str = ...,
        trace: str = ...,
        userIp: str = ...,
        userip: str = ...,
        **kwargs: typing.Any
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def userinfo(self) -> UserinfoResource: ...

@typing.type_check_only
class TokeninfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Tokeninfo: ...

@typing.type_check_only
class UserinfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Userinfo: ...
