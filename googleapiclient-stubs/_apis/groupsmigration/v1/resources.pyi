import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class GroupsMigrationResource(googleapiclient.discovery.Resource):
    class ArchiveResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, groupId: str, **kwargs: typing.Any
        ) -> GroupsHttpRequest: ...
    def archive(self) -> ArchiveResource: ...

class GroupsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Groups: ...
