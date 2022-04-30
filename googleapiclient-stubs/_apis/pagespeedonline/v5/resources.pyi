import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PagespeedInsightsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PagespeedapiResource(googleapiclient.discovery.Resource):
        def runpagespeed(
            self,
            *,
            url: str,
            captchaToken: str = ...,
            category: typing_extensions.Literal[
                "CATEGORY_UNSPECIFIED",
                "ACCESSIBILITY",
                "BEST_PRACTICES",
                "PERFORMANCE",
                "PWA",
                "SEO",
            ]
            | _list[
                typing_extensions.Literal[
                    "CATEGORY_UNSPECIFIED",
                    "ACCESSIBILITY",
                    "BEST_PRACTICES",
                    "PERFORMANCE",
                    "PWA",
                    "SEO",
                ]
            ] = ...,
            locale: str = ...,
            strategy: typing_extensions.Literal[
                "STRATEGY_UNSPECIFIED", "DESKTOP", "MOBILE"
            ] = ...,
            utm_campaign: str = ...,
            utm_source: str = ...,
            **kwargs: typing.Any
        ) -> PagespeedApiPagespeedResponseV5HttpRequest: ...

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
    def pagespeedapi(self) -> PagespeedapiResource: ...

@typing.type_check_only
class PagespeedApiPagespeedResponseV5HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PagespeedApiPagespeedResponseV5: ...
