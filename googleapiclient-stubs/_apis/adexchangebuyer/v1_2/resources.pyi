import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdExchangeBuyerResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        def get(self, *, id: int, **kwargs: typing.Any) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> AccountsListHttpRequest: ...
        def patch(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def update(
            self, *, id: int, body: Account = ..., **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
    class CreativesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, accountId: int, buyerCreativeId: str, **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def insert(
            self, *, body: Creative = ..., **kwargs: typing.Any
        ) -> CreativeHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            statusFilter: typing_extensions.Literal[
                "approved", "disapproved", "not_checked"
            ] = ...,
            **kwargs: typing.Any
        ) -> CreativesListHttpRequest: ...
    def accounts(self) -> AccountsResource: ...
    def creatives(self) -> CreativesResource: ...

class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Creative: ...

class CreativesListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreativesList: ...

class AccountsListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AccountsList: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...
