import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
        self, *, access_token: str = ..., id_token: str = ..., **kwargs: typing.Any
    ) -> TokeninfoHttpRequest: ...
    def userinfo(self) -> UserinfoResource: ...

@typing.type_check_only
class TokeninfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Tokeninfo: ...

@typing.type_check_only
class UserinfoHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Userinfo: ...
