import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class PolicyAnalyzerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ActivityTypesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ActivitiesResource(googleapiclient.discovery.Resource):
                    def query(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudPolicyanalyzerV1QueryActivityResponseHttpRequest: ...
                    def query_next(
                        self,
                        previous_request: GoogleCloudPolicyanalyzerV1QueryActivityResponseHttpRequest,
                        previous_response: GoogleCloudPolicyanalyzerV1QueryActivityResponse,
                    ) -> GoogleCloudPolicyanalyzerV1QueryActivityResponseHttpRequest | None: ...

                def activities(self) -> ActivitiesResource: ...

            def activityTypes(self) -> ActivityTypesResource: ...

        def locations(self) -> LocationsResource: ...

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
class GoogleCloudPolicyanalyzerV1QueryActivityResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudPolicyanalyzerV1QueryActivityResponse: ...
