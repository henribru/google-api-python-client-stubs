import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class PagespeedInsightsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PagespeedapiResource(googleapiclient.discovery.Resource):
        def runpagespeed(
            self,
            *,
            url: str,
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
            locale: str = ...,
            strategy: typing_extensions.Literal[
                "STRATEGY_UNSPECIFIED", "DESKTOP", "MOBILE"
            ] = ...,
            utm_campaign: str = ...,
            utm_source: str = ...,
            **kwargs: typing.Any
        ) -> PagespeedApiPagespeedResponseV5HttpRequest: ...
    def pagespeedapi(self) -> PagespeedapiResource: ...

@typing.type_check_only
class PagespeedApiPagespeedResponseV5HttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PagespeedApiPagespeedResponseV5: ...
