import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudAssetResource(googleapiclient.discovery.Resource):
    class ResourcesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            pageSize: int = ...,
            assetTypes: typing.Union[str, typing.List[str]] = ...,
            query: str = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllResourcesResponseHttpRequest: ...
    class IamPoliciesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            pageToken: str = ...,
            pageSize: int = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
    def resources(self) -> ResourcesResource: ...
    def iamPolicies(self) -> IamPoliciesResource: ...

class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllIamPoliciesResponse: ...

class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllResourcesResponse: ...
