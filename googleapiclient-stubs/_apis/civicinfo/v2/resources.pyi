import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
            levels: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            roles: typing.Union[
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
                ],
                typing.List[
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
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> RepresentativeInfoResponseHttpRequest: ...
        def representativeInfoByDivision(
            self,
            *,
            ocdId: str,
            levels: typing.Union[
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
                ],
                typing.List[
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
                ],
            ] = ...,
            recursive: bool = ...,
            roles: typing.Union[
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
                ],
                typing.List[
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
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> RepresentativeInfoDataHttpRequest: ...
    def divisions(self) -> DivisionsResource: ...
    def elections(self) -> ElectionsResource: ...
    def representatives(self) -> RepresentativesResource: ...

@typing.type_check_only
class DivisionSearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DivisionSearchResponse: ...

@typing.type_check_only
class ElectionsQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ElectionsQueryResponse: ...

@typing.type_check_only
class RepresentativeInfoDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RepresentativeInfoData: ...

@typing.type_check_only
class RepresentativeInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RepresentativeInfoResponse: ...

@typing.type_check_only
class VoterInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> VoterInfoResponse: ...
