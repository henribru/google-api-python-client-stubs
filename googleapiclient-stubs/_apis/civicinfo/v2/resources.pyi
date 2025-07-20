import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CivicInfoResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DivisionsResource(googleapiclient.discovery.Resource):
        def queryDivisionByAddress(
            self, *, address: str = ..., **kwargs: typing.Any
        ) -> CivicinfoApiprotosV2DivisionByAddressResponseHttpRequest: ...
        def search(
            self, *, query: str = ..., **kwargs: typing.Any
        ) -> CivicinfoApiprotosV2DivisionSearchResponseHttpRequest: ...

    @typing.type_check_only
    class ElectionsResource(googleapiclient.discovery.Resource):
        def electionQuery(
            self, *, productionDataOnly: bool = ..., **kwargs: typing.Any
        ) -> CivicinfoApiprotosV2ElectionsQueryResponseHttpRequest: ...
        def voterInfoQuery(
            self,
            *,
            address: str = ...,
            electionId: str = ...,
            officialOnly: bool = ...,
            productionDataOnly: bool = ...,
            returnAllAvailableData: bool = ...,
            **kwargs: typing.Any,
        ) -> CivicinfoApiprotosV2VoterInfoResponseHttpRequest: ...

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
    def divisions(self) -> DivisionsResource: ...
    def elections(self) -> ElectionsResource: ...

@typing.type_check_only
class CivicinfoApiprotosV2DivisionByAddressResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CivicinfoApiprotosV2DivisionByAddressResponse: ...

@typing.type_check_only
class CivicinfoApiprotosV2DivisionSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CivicinfoApiprotosV2DivisionSearchResponse: ...

@typing.type_check_only
class CivicinfoApiprotosV2ElectionsQueryResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CivicinfoApiprotosV2ElectionsQueryResponse: ...

@typing.type_check_only
class CivicinfoApiprotosV2VoterInfoResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CivicinfoApiprotosV2VoterInfoResponse: ...
