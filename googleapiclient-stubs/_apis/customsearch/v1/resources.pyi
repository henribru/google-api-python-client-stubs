import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                c2coff: str | None = ...,
                cr: str | None = ...,
                cx: str | None = ...,
                dateRestrict: str | None = ...,
                enableAlternateSearchHandler: bool | None = ...,
                exactTerms: str | None = ...,
                excludeTerms: str | None = ...,
                fileType: str | None = ...,
                filter: str | None = ...,
                gl: str | None = ...,
                googlehost: str | None = ...,
                highRange: str | None = ...,
                hl: str | None = ...,
                hq: str | None = ...,
                imgColorType: typing_extensions.Literal[
                    "imgColorTypeUndefined", "mono", "gray", "color", "trans"
                ]
                | None = ...,
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
                ]
                | None = ...,
                imgSize: typing_extensions.Literal[
                    "imgSizeUndefined",
                    "HUGE",
                    "ICON",
                    "LARGE",
                    "MEDIUM",
                    "SMALL",
                    "XLARGE",
                    "XXLARGE",
                ]
                | None = ...,
                imgType: typing_extensions.Literal[
                    "imgTypeUndefined",
                    "clipart",
                    "face",
                    "lineart",
                    "stock",
                    "photo",
                    "animated",
                ]
                | None = ...,
                linkSite: str | None = ...,
                lowRange: str | None = ...,
                lr: str | None = ...,
                num: int | None = ...,
                orTerms: str | None = ...,
                q: str | None = ...,
                relatedSite: str | None = ...,
                rights: str | None = ...,
                safe: typing_extensions.Literal[
                    "safeUndefined", "active", "high", "medium", "off"
                ]
                | None = ...,
                searchType: typing_extensions.Literal["searchTypeUndefined", "image"]
                | None = ...,
                siteSearch: str | None = ...,
                siteSearchFilter: typing_extensions.Literal[
                    "siteSearchFilterUndefined", "e", "i"
                ]
                | None = ...,
                snippetLength: int | None = ...,
                sort: str | None = ...,
                start: int | None = ...,
                **kwargs: typing.Any,
            ) -> SearchHttpRequest: ...

        def list(
            self,
            *,
            c2coff: str | None = ...,
            cr: str | None = ...,
            cx: str | None = ...,
            dateRestrict: str | None = ...,
            enableAlternateSearchHandler: bool | None = ...,
            exactTerms: str | None = ...,
            excludeTerms: str | None = ...,
            fileType: str | None = ...,
            filter: str | None = ...,
            gl: str | None = ...,
            googlehost: str | None = ...,
            highRange: str | None = ...,
            hl: str | None = ...,
            hq: str | None = ...,
            imgColorType: typing_extensions.Literal[
                "imgColorTypeUndefined", "mono", "gray", "color", "trans"
            ]
            | None = ...,
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
            ]
            | None = ...,
            imgSize: typing_extensions.Literal[
                "imgSizeUndefined",
                "HUGE",
                "ICON",
                "LARGE",
                "MEDIUM",
                "SMALL",
                "XLARGE",
                "XXLARGE",
            ]
            | None = ...,
            imgType: typing_extensions.Literal[
                "imgTypeUndefined",
                "clipart",
                "face",
                "lineart",
                "stock",
                "photo",
                "animated",
            ]
            | None = ...,
            linkSite: str | None = ...,
            lowRange: str | None = ...,
            lr: str | None = ...,
            num: int | None = ...,
            orTerms: str | None = ...,
            q: str | None = ...,
            relatedSite: str | None = ...,
            rights: str | None = ...,
            safe: typing_extensions.Literal[
                "safeUndefined", "active", "high", "medium", "off"
            ]
            | None = ...,
            searchType: typing_extensions.Literal["searchTypeUndefined", "image"]
            | None = ...,
            siteSearch: str | None = ...,
            siteSearchFilter: typing_extensions.Literal[
                "siteSearchFilterUndefined", "e", "i"
            ]
            | None = ...,
            snippetLength: int | None = ...,
            sort: str | None = ...,
            start: int | None = ...,
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def cse(self) -> CseResource: ...

@typing.type_check_only
class SearchHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Search: ...
