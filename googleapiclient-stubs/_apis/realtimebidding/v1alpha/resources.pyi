import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class RealTimeBiddingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BiddersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BiddingFunctionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: BiddingFunction = ..., **kwargs: typing.Any
            ) -> BiddingFunctionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListBiddingFunctionsResponseHttpRequest: ...
        def biddingFunctions(self) -> BiddingFunctionsResource: ...
    def bidders(self) -> BiddersResource: ...

@typing.type_check_only
class BiddingFunctionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BiddingFunction: ...

@typing.type_check_only
class ListBiddingFunctionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBiddingFunctionsResponse: ...
