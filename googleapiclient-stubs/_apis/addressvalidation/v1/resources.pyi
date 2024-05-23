import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AddressValidationResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def provideValidationFeedback(
            self,
            *,
            body: GoogleMapsAddressvalidationV1ProvideValidationFeedbackRequest = ...,
            **kwargs: typing.Any,
        ) -> (
            GoogleMapsAddressvalidationV1ProvideValidationFeedbackResponseHttpRequest
        ): ...
        def validateAddress(
            self,
            *,
            body: GoogleMapsAddressvalidationV1ValidateAddressRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleMapsAddressvalidationV1ValidateAddressResponseHttpRequest: ...

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
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class GoogleMapsAddressvalidationV1ProvideValidationFeedbackResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsAddressvalidationV1ProvideValidationFeedbackResponse: ...

@typing.type_check_only
class GoogleMapsAddressvalidationV1ValidateAddressResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleMapsAddressvalidationV1ValidateAddressResponse: ...
