import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class GroupssettingsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class GroupsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, groupUniqueId: str, **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def patch(
            self, *, groupUniqueId: str, body: Groups = ..., **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def update(
            self, *, groupUniqueId: str, body: Groups = ..., **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
    def groups(self) -> GroupsResource: ...

@typing.type_check_only
class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Groups: ...
