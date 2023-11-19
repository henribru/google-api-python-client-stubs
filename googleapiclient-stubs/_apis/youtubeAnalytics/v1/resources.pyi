import collections.abc
import typing

import httplib2  # type: ignore[import-untyped]
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore[import-untyped]

from .schemas import *

_list = list

@typing.type_check_only
class YouTubeAnalyticsResource(googleapiclient.discovery.Resource):
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
    ...
