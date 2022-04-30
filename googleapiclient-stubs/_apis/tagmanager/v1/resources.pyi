import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class TagManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ContainersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EnvironmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Environment = ...,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    environmentId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    environmentId: str,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListEnvironmentsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    environmentId: str,
                    body: Environment = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...

            @typing.type_check_only
            class FoldersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class EntitiesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        accountId: str,
                        containerId: str,
                        folderId: str,
                        **kwargs: typing.Any
                    ) -> FolderEntitiesHttpRequest: ...

                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Folder = ...,
                    **kwargs: typing.Any
                ) -> FolderHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    folderId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    folderId: str,
                    **kwargs: typing.Any
                ) -> FolderHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListFoldersResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    folderId: str,
                    body: Folder = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> FolderHttpRequest: ...
                def entities(self) -> EntitiesResource: ...

            @typing.type_check_only
            class Move_foldersResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    folderId: str,
                    body: Folder = ...,
                    tagId: str | _list[str] = ...,
                    triggerId: str | _list[str] = ...,
                    variableId: str | _list[str] = ...,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...

            @typing.type_check_only
            class Reauthorize_environmentsResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    environmentId: str,
                    body: Environment = ...,
                    **kwargs: typing.Any
                ) -> EnvironmentHttpRequest: ...

            @typing.type_check_only
            class TagsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Tag = ...,
                    **kwargs: typing.Any
                ) -> TagHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    tagId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    tagId: str,
                    **kwargs: typing.Any
                ) -> TagHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListTagsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    tagId: str,
                    body: Tag = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> TagHttpRequest: ...

            @typing.type_check_only
            class TriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Trigger = ...,
                    **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    triggerId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    triggerId: str,
                    **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListTriggersResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    triggerId: str,
                    body: Trigger = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...

            @typing.type_check_only
            class VariablesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Variable = ...,
                    **kwargs: typing.Any
                ) -> VariableHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    variableId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    variableId: str,
                    **kwargs: typing.Any
                ) -> VariableHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListVariablesResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    variableId: str,
                    body: Variable = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> VariableHttpRequest: ...

            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: CreateContainerVersionRequestVersionOptions = ...,
                    **kwargs: typing.Any
                ) -> CreateContainerVersionResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def list(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    headers: bool = ...,
                    includeDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> ListContainerVersionsResponseHttpRequest: ...
                def publish(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> PublishContainerVersionResponseHttpRequest: ...
                def restore(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def undelete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    body: ContainerVersion = ...,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...

            def create(
                self, *, accountId: str, body: Container = ..., **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def delete(
                self, *, accountId: str, containerId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, accountId: str, containerId: str, **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def list(
                self, *, accountId: str, **kwargs: typing.Any
            ) -> ListContainersResponseHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                containerId: str,
                body: Container = ...,
                fingerprint: str = ...,
                **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
            def environments(self) -> EnvironmentsResource: ...
            def folders(self) -> FoldersResource: ...
            def move_folders(self) -> Move_foldersResource: ...
            def reauthorize_environments(self) -> Reauthorize_environmentsResource: ...
            def tags(self) -> TagsResource: ...
            def triggers(self) -> TriggersResource: ...
            def variables(self) -> VariablesResource: ...
            def versions(self) -> VersionsResource: ...

        @typing.type_check_only
        class PermissionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, accountId: str, body: UserAccess = ..., **kwargs: typing.Any
            ) -> UserAccessHttpRequest: ...
            def delete(
                self, *, accountId: str, permissionId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self, *, accountId: str, permissionId: str, **kwargs: typing.Any
            ) -> UserAccessHttpRequest: ...
            def list(
                self, *, accountId: str, **kwargs: typing.Any
            ) -> ListAccountUsersResponseHttpRequest: ...
            def update(
                self,
                *,
                accountId: str,
                permissionId: str,
                body: UserAccess = ...,
                **kwargs: typing.Any
            ) -> UserAccessHttpRequest: ...

        def get(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> ListAccountsResponseHttpRequest: ...
        def update(
            self,
            *,
            accountId: str,
            body: Account = ...,
            fingerprint: str = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def containers(self) -> ContainersResource: ...
        def permissions(self) -> PermissionsResource: ...

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
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Account: ...

@typing.type_check_only
class ContainerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Container: ...

@typing.type_check_only
class ContainerVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ContainerVersion: ...

@typing.type_check_only
class CreateContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CreateContainerVersionResponse: ...

@typing.type_check_only
class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Environment: ...

@typing.type_check_only
class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Folder: ...

@typing.type_check_only
class FolderEntitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FolderEntities: ...

@typing.type_check_only
class ListAccountUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountUsersResponse: ...

@typing.type_check_only
class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAccountsResponse: ...

@typing.type_check_only
class ListContainerVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListContainerVersionsResponse: ...

@typing.type_check_only
class ListContainersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListContainersResponse: ...

@typing.type_check_only
class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListEnvironmentsResponse: ...

@typing.type_check_only
class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFoldersResponse: ...

@typing.type_check_only
class ListTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTagsResponse: ...

@typing.type_check_only
class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTriggersResponse: ...

@typing.type_check_only
class ListVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVariablesResponse: ...

@typing.type_check_only
class PublishContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PublishContainerVersionResponse: ...

@typing.type_check_only
class TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Tag: ...

@typing.type_check_only
class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Trigger: ...

@typing.type_check_only
class UserAccessHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserAccess: ...

@typing.type_check_only
class VariableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Variable: ...
