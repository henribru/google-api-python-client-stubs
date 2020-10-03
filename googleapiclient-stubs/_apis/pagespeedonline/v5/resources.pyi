import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class PagespeedInsightsResource(googleapiclient.discovery.Resource):
    class PagespeedapiResource(googleapiclient.discovery.Resource):
        def runpagespeed(
            self,
            *,
            utm_source: str = ...,
            locale: str = ...,
            strategy: typing_extensions.Literal[
                "STRATEGY_UNSPECIFIED", "DESKTOP", "MOBILE"
            ] = ...,
            utm_campaign: str = ...,
            url: str = ...,
            captchaToken: str = ...,
            category: typing.Union[
                typing_extensions.Literal[
                    "CATEGORY_UNSPECIFIED",
                    "ACCESSIBILITY",
                    "BEST_PRACTICES",
                    "PERFORMANCE",
                    "PWA",
                    "SEO",
                ],
                typing.List[
                    typing_extensions.Literal[
                        "CATEGORY_UNSPECIFIED",
                        "ACCESSIBILITY",
                        "BEST_PRACTICES",
                        "PERFORMANCE",
                        "PWA",
                        "SEO",
                    ]
                ],
            ] = ...,
            **kwargs: typing.Any
        ) -> PagespeedApiPagespeedResponseV5HttpRequest: ...
    def pagespeedapi(self) -> PagespeedapiResource: ...

class PagespeedApiPagespeedResponseV5HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PagespeedApiPagespeedResponseV5: ...
