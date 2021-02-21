import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IamPoliciesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
    @typing.type_check_only
    class ResourcesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            assetTypes: typing.Union[str, typing.List[str]] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllResourcesResponseHttpRequest: ...
    def iamPolicies(self) -> IamPoliciesResource: ...
    def resources(self) -> ResourcesResource: ...

@typing.type_check_only
class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchAllIamPoliciesResponse: ...

@typing.type_check_only
class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SearchAllResourcesResponse: ...
