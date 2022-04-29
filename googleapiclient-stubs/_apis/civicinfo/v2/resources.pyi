import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CivicInfoResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DivisionsResource(googleapiclient.discovery.Resource):
        def search(
            self, *, query: str = ..., **kwargs: typing.Any
        ) -> DivisionSearchResponseHttpRequest: ...

    @typing.type_check_only
    class ElectionsResource(googleapiclient.discovery.Resource):
        def electionQuery(
            self, **kwargs: typing.Any
        ) -> ElectionsQueryResponseHttpRequest: ...
        def voterInfoQuery(
            self,
            *,
            address: str,
            electionId: str = ...,
            officialOnly: bool = ...,
            returnAllAvailableData: bool = ...,
            **kwargs: typing.Any
        ) -> VoterInfoResponseHttpRequest: ...

    @typing.type_check_only
    class RepresentativesResource(googleapiclient.discovery.Resource):
        def representativeInfoByAddress(
            self,
            *,
            address: str = ...,
            includeOffices: bool = ...,
            levels: typing_extensions.Literal[
                "international",
                "country",
                "administrativeArea1",
                "regional",
                "administrativeArea2",
                "locality",
                "subLocality1",
                "subLocality2",
                "special",
            ]
            | _list[
                typing_extensions.Literal[
                    "international",
                    "country",
                    "administrativeArea1",
                    "regional",
                    "administrativeArea2",
                    "locality",
                    "subLocality1",
                    "subLocality2",
                    "special",
                ]
            ] = ...,
            roles: typing_extensions.Literal[
                "headOfState",
                "headOfGovernment",
                "deputyHeadOfGovernment",
                "governmentOfficer",
                "executiveCouncil",
                "legislatorUpperBody",
                "legislatorLowerBody",
                "highestCourtJudge",
                "judge",
                "schoolBoard",
                "specialPurposeOfficer",
                "otherRole",
            ]
            | _list[
                typing_extensions.Literal[
                    "headOfState",
                    "headOfGovernment",
                    "deputyHeadOfGovernment",
                    "governmentOfficer",
                    "executiveCouncil",
                    "legislatorUpperBody",
                    "legislatorLowerBody",
                    "highestCourtJudge",
                    "judge",
                    "schoolBoard",
                    "specialPurposeOfficer",
                    "otherRole",
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> RepresentativeInfoResponseHttpRequest: ...
        def representativeInfoByDivision(
            self,
            *,
            ocdId: str,
            levels: typing_extensions.Literal[
                "international",
                "country",
                "administrativeArea1",
                "regional",
                "administrativeArea2",
                "locality",
                "subLocality1",
                "subLocality2",
                "special",
            ]
            | _list[
                typing_extensions.Literal[
                    "international",
                    "country",
                    "administrativeArea1",
                    "regional",
                    "administrativeArea2",
                    "locality",
                    "subLocality1",
                    "subLocality2",
                    "special",
                ]
            ] = ...,
            recursive: bool = ...,
            roles: typing_extensions.Literal[
                "headOfState",
                "headOfGovernment",
                "deputyHeadOfGovernment",
                "governmentOfficer",
                "executiveCouncil",
                "legislatorUpperBody",
                "legislatorLowerBody",
                "highestCourtJudge",
                "judge",
                "schoolBoard",
                "specialPurposeOfficer",
                "otherRole",
            ]
            | _list[
                typing_extensions.Literal[
                    "headOfState",
                    "headOfGovernment",
                    "deputyHeadOfGovernment",
                    "governmentOfficer",
                    "executiveCouncil",
                    "legislatorUpperBody",
                    "legislatorLowerBody",
                    "highestCourtJudge",
                    "judge",
                    "schoolBoard",
                    "specialPurposeOfficer",
                    "otherRole",
                ]
            ] = ...,
            **kwargs: typing.Any
        ) -> RepresentativeInfoDataHttpRequest: ...

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
    def divisions(self) -> DivisionsResource: ...
    def elections(self) -> ElectionsResource: ...
    def representatives(self) -> RepresentativesResource: ...

@typing.type_check_only
class DivisionSearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DivisionSearchResponse: ...

@typing.type_check_only
class ElectionsQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ElectionsQueryResponse: ...

@typing.type_check_only
class RepresentativeInfoDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RepresentativeInfoData: ...

@typing.type_check_only
class RepresentativeInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RepresentativeInfoResponse: ...

@typing.type_check_only
class VoterInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> VoterInfoResponse: ...
