import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ChromewebstoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ItemsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            itemId: str,
            projection: typing_extensions.Literal["DRAFT", "PUBLISHED"] = ...,
            **kwargs: typing.Any,
        ) -> ItemHttpRequest: ...
        def insert(
            self, *, publisherEmail: str = ..., **kwargs: typing.Any
        ) -> ItemHttpRequest: ...
        def publish(
            self,
            *,
            itemId: str,
            body: PublishRequest = ...,
            deployPercentage: int = ...,
            publishTarget: str = ...,
            reviewExemption: bool = ...,
            **kwargs: typing.Any,
        ) -> Item2HttpRequest: ...
        def update(
            self, *, itemId: str, body: Item = ..., **kwargs: typing.Any
        ) -> ItemHttpRequest: ...

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
    def items(self) -> ItemsResource: ...

@typing.type_check_only
class ItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Item: ...

@typing.type_check_only
class Item2HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Item2: ...
