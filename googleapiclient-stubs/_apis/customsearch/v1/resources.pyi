import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CustomSearchAPIResource(googleapiclient.discovery.Resource):
    class CseResource(googleapiclient.discovery.Resource):
        class SiterestrictResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                cr: str = ...,
                c2coff: str = ...,
                filter: str = ...,
                googlehost: str = ...,
                exactTerms: str = ...,
                highRange: str = ...,
                safe: typing_extensions.Literal[
                    "safeUndefined", "active", "high", "medium", "off"
                ] = ...,
                num: int = ...,
                rights: str = ...,
                cx: str = ...,
                q: str = ...,
                gl: str = ...,
                imgType: typing_extensions.Literal[
                    "imgTypeUndefined",
                    "clipart",
                    "face",
                    "lineart",
                    "stock",
                    "photo",
                    "animated",
                ] = ...,
                lowRange: str = ...,
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
                searchType: typing_extensions.Literal[
                    "searchTypeUndefined", "image"
                ] = ...,
                siteSearch: str = ...,
                hl: str = ...,
                relatedSite: str = ...,
                excludeTerms: str = ...,
                siteSearchFilter: typing_extensions.Literal[
                    "siteSearchFilterUndefined", "e", "i"
                ] = ...,
                lr: str = ...,
                linkSite: str = ...,
                hq: str = ...,
                start: int = ...,
                sort: str = ...,
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
                orTerms: str = ...,
                fileType: str = ...,
                dateRestrict: str = ...,
                imgColorType: typing_extensions.Literal[
                    "imgColorTypeUndefined", "mono", "gray", "color", "trans"
                ] = ...,
                **kwargs: typing.Any
            ) -> SearchHttpRequest: ...
        def list(
            self,
            *,
            rights: str = ...,
            imgType: typing_extensions.Literal[
                "imgTypeUndefined",
                "clipart",
                "face",
                "lineart",
                "stock",
                "photo",
                "animated",
            ] = ...,
            imgColorType: typing_extensions.Literal[
                "imgColorTypeUndefined", "mono", "gray", "color", "trans"
            ] = ...,
            gl: str = ...,
            linkSite: str = ...,
            highRange: str = ...,
            filter: str = ...,
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
            siteSearchFilter: typing_extensions.Literal[
                "siteSearchFilterUndefined", "e", "i"
            ] = ...,
            exactTerms: str = ...,
            lr: str = ...,
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
            fileType: str = ...,
            dateRestrict: str = ...,
            num: int = ...,
            hl: str = ...,
            excludeTerms: str = ...,
            q: str = ...,
            searchType: typing_extensions.Literal["searchTypeUndefined", "image"] = ...,
            start: int = ...,
            orTerms: str = ...,
            cr: str = ...,
            siteSearch: str = ...,
            safe: typing_extensions.Literal[
                "safeUndefined", "active", "high", "medium", "off"
            ] = ...,
            relatedSite: str = ...,
            googlehost: str = ...,
            c2coff: str = ...,
            sort: str = ...,
            lowRange: str = ...,
            cx: str = ...,
            hq: str = ...,
            **kwargs: typing.Any
        ) -> SearchHttpRequest: ...
        def siterestrict(self) -> SiterestrictResource: ...
    def cse(self) -> CseResource: ...

class SearchHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Search: ...
