import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CustomSearchAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CseResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SiterestrictResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                c2coff: str = ...,
                cr: str = ...,
                cx: str = ...,
                dateRestrict: str = ...,
                exactTerms: str = ...,
                excludeTerms: str = ...,
                fileType: str = ...,
                filter: str = ...,
                gl: str = ...,
                googlehost: str = ...,
                highRange: str = ...,
                hl: str = ...,
                hq: str = ...,
                imgColorType: typing_extensions.Literal[
                    "imgColorTypeUndefined", "mono", "gray", "color", "trans"
                ] = ...,
                imgDominantColor: typing_extensions.Literal[
                    "imgDominantColorUndefined",
                    "black",
                    "blue",
                    "brown",
                    "gray",
                    "green",
                    "orange",
                    "pink",
                    "purple",
                    "red",
                    "teal",
                    "white",
                    "yellow",
                ] = ...,
                imgSize: typing_extensions.Literal[
                    "imgSizeUndefined",
                    "HUGE",
                    "ICON",
                    "LARGE",
                    "MEDIUM",
                    "SMALL",
                    "XLARGE",
                    "XXLARGE",
                ] = ...,
                imgType: typing_extensions.Literal[
                    "imgTypeUndefined",
                    "clipart",
                    "face",
                    "lineart",
                    "stock",
                    "photo",
                    "animated",
                ] = ...,
                linkSite: str = ...,
                lowRange: str = ...,
                lr: str = ...,
                num: int = ...,
                orTerms: str = ...,
                q: str = ...,
                relatedSite: str = ...,
                rights: str = ...,
                safe: typing_extensions.Literal[
                    "safeUndefined", "active", "high", "medium", "off"
                ] = ...,
                searchType: typing_extensions.Literal[
                    "searchTypeUndefined", "image"
                ] = ...,
                siteSearch: str = ...,
                siteSearchFilter: typing_extensions.Literal[
                    "siteSearchFilterUndefined", "e", "i"
                ] = ...,
                sort: str = ...,
                start: int = ...,
                **kwargs: typing.Any
            ) -> SearchHttpRequest: ...

        def list(
            self,
            *,
            c2coff: str = ...,
            cr: str = ...,
            cx: str = ...,
            dateRestrict: str = ...,
            exactTerms: str = ...,
            excludeTerms: str = ...,
            fileType: str = ...,
            filter: str = ...,
            gl: str = ...,
            googlehost: str = ...,
            highRange: str = ...,
            hl: str = ...,
            hq: str = ...,
            imgColorType: typing_extensions.Literal[
                "imgColorTypeUndefined", "mono", "gray", "color", "trans"
            ] = ...,
            imgDominantColor: typing_extensions.Literal[
                "imgDominantColorUndefined",
                "black",
                "blue",
                "brown",
                "gray",
                "green",
                "orange",
                "pink",
                "purple",
                "red",
                "teal",
                "white",
                "yellow",
            ] = ...,
            imgSize: typing_extensions.Literal[
                "imgSizeUndefined",
                "HUGE",
                "ICON",
                "LARGE",
                "MEDIUM",
                "SMALL",
                "XLARGE",
                "XXLARGE",
            ] = ...,
            imgType: typing_extensions.Literal[
                "imgTypeUndefined",
                "clipart",
                "face",
                "lineart",
                "stock",
                "photo",
                "animated",
            ] = ...,
            linkSite: str = ...,
            lowRange: str = ...,
            lr: str = ...,
            num: int = ...,
            orTerms: str = ...,
            q: str = ...,
            relatedSite: str = ...,
            rights: str = ...,
            safe: typing_extensions.Literal[
                "safeUndefined", "active", "high", "medium", "off"
            ] = ...,
            searchType: typing_extensions.Literal["searchTypeUndefined", "image"] = ...,
            siteSearch: str = ...,
            siteSearchFilter: typing_extensions.Literal[
                "siteSearchFilterUndefined", "e", "i"
            ] = ...,
            sort: str = ...,
            start: int = ...,
            **kwargs: typing.Any
        ) -> SearchHttpRequest: ...
        def siterestrict(self) -> SiterestrictResource: ...

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
    def cse(self) -> CseResource: ...

@typing.type_check_only
class SearchHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Search: ...
