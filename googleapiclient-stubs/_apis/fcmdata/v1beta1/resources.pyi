import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

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
            def deliveryData(self) -> DeliveryDataResource: ...
        def androidApps(self) -> AndroidAppsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFirebaseFcmDataV1beta1ListAndroidDeliveryDataResponse: ...
