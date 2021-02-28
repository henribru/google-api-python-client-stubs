import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudBuildResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BuildsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                projectId: str,
                id: str,
                body: CancelBuildRequest = ...,
                **kwargs: typing.Any
            ) -> BuildHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: Build = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self, *, projectId: str, id: str, name: str = ..., **kwargs: typing.Any
            ) -> BuildHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> ListBuildsResponseHttpRequest: ...
            def retry(
                self,
                *,
                projectId: str,
                id: str,
                body: RetryBuildRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BuildsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> BuildHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Build = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    id: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> BuildHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    projectId: str = ...,
                    **kwargs: typing.Any
                ) -> ListBuildsResponseHttpRequest: ...
                def retry(
                    self,
                    *,
                    name: str,
                    body: RetryBuildRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            def builds(self) -> BuildsResource: ...
            def operations(self) -> OperationsResource: ...
        @typing.type_check_only
        class TriggersResource(googleapiclient.discovery.Resource):
            def create(
                self, *, projectId: str, body: BuildTrigger = ..., **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def delete(
                self, *, projectId: str, triggerId: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, projectId: str, triggerId: str, **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListBuildTriggersResponseHttpRequest: ...
            def patch(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: BuildTrigger = ...,
                **kwargs: typing.Any
            ) -> BuildTriggerHttpRequest: ...
            def run(
                self,
                *,
                projectId: str,
                triggerId: str,
                body: RepoSource = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def webhook(
                self,
                *,
                projectId: str,
                trigger: str,
                body: HttpBody = ...,
                secret: str = ...,
                **kwargs: typing.Any
            ) -> ReceiveTriggerWebhookResponseHttpRequest: ...
        def builds(self) -> BuildsResource: ...
        def locations(self) -> LocationsResource: ...
        def triggers(self) -> TriggersResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BuildHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Build: ...

@typing.type_check_only
class BuildTriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BuildTrigger: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListBuildTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBuildTriggersResponse: ...

@typing.type_check_only
class ListBuildsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBuildsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ReceiveTriggerWebhookResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReceiveTriggerWebhookResponse: ...
