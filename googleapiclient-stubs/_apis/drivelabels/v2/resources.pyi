import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DriveLabelsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LabelsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            languageCode: str = ...,
            useAdminAccess: bool = ...,
            view: typing_extensions.Literal[
                "LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2LabelHttpRequest: ...
        def list(
            self,
            *,
            languageCode: str = ...,
            minimumRole: typing_extensions.Literal[
                "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            publishedOnly: bool = ...,
            useAdminAccess: bool = ...,
            view: typing_extensions.Literal[
                "LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest,
            previous_response: GoogleAppsDriveLabelsV2ListLabelsResponse,
        ) -> GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest | None: ...

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
    def labels(self) -> LabelsResource: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2Label: ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleAppsDriveLabelsV2ListLabelsResponse: ...
