import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GroupssettingsResource(googleapiclient.discovery.Resource):
    class GroupsResource(googleapiclient.discovery.Resource):
        def patch(
            self, *, groupUniqueId: str, body: Groups = ..., **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def get(
            self, *, groupUniqueId: str, **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
        def update(
            self, *, groupUniqueId: str, body: Groups = ..., **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
    def groups(self) -> GroupsResource: ...

class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Groups: ...
