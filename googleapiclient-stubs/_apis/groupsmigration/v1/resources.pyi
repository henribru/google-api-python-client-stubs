import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class GroupsMigrationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ArchiveResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, groupId: str, **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
    def archive(self) -> ArchiveResource: ...

@typing.type_check_only
class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Groups: ...
