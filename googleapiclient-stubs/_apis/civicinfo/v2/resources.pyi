import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CivicInfoResource(googleapiclient.discovery.Resource):
    class ElectionsResource(googleapiclient.discovery.Resource):
        def electionQuery(
            self, **kwargs: typing.Any
        ) -> ElectionsQueryResponseHttpRequest: ...
        def voterInfoQuery(
            self,
            *,
            address: str,
            electionId: str = ...,
            returnAllAvailableData: bool = ...,
            officialOnly: bool = ...,
            **kwargs: typing.Any
        ) -> VoterInfoResponseHttpRequest: ...
    class DivisionsResource(googleapiclient.discovery.Resource):
        def search(
            self, *, query: str = ..., **kwargs: typing.Any
        ) -> DivisionSearchResponseHttpRequest: ...
    class RepresentativesResource(googleapiclient.discovery.Resource):
        def representativeInfoByDivision(
            self,
            *,
            ocdId: str,
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
            recursive: bool = ...,
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
            **kwargs: typing.Any
        ) -> RepresentativeInfoDataHttpRequest: ...
        def representativeInfoByAddress(
            self,
            *,
            includeOffices: bool = ...,
            address: str = ...,
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
            **kwargs: typing.Any
        ) -> RepresentativeInfoResponseHttpRequest: ...
    def elections(self) -> ElectionsResource: ...
    def divisions(self) -> DivisionsResource: ...
    def representatives(self) -> RepresentativesResource: ...

class RepresentativeInfoDataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RepresentativeInfoData: ...

class ElectionsQueryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ElectionsQueryResponse: ...

class RepresentativeInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RepresentativeInfoResponse: ...

class VoterInfoResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VoterInfoResponse: ...

class DivisionSearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DivisionSearchResponse: ...
