import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FcmdataResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AndroidAppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeliveryDataResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseHttpRequest,
                    previous_response: GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse,
                ) -> GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseHttpRequest | None: ...

            def deliveryData(self) -> DeliveryDataResource: ...

        def androidApps(self) -> AndroidAppsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse: ...
