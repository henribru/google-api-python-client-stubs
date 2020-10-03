import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TagManagerResource(googleapiclient.discovery.Resource):
    class AccountsResource(googleapiclient.discovery.Resource):
        class PermissionsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, accountId: str, permissionId: str, **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
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
                self, *, accountId: str, permissionId: str, **kwargs: typing.Any
            ) -> UserAccessHttpRequest: ...
            def create(
                self, *, accountId: str, body: UserAccess = ..., **kwargs: typing.Any
            ) -> UserAccessHttpRequest: ...
        class ContainersResource(googleapiclient.discovery.Resource):
            class EnvironmentsResource(googleapiclient.discovery.Resource):
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
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListEnvironmentsResponseHttpRequest: ...
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
            class Move_foldersResource(googleapiclient.discovery.Resource):
                def update(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    folderId: str,
                    body: Folder = ...,
                    tagId: typing.Union[str, typing.List[str]] = ...,
                    variableId: typing.Union[str, typing.List[str]] = ...,
                    triggerId: typing.Union[str, typing.List[str]] = ...,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
            class VersionsResource(googleapiclient.discovery.Resource):
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
                def list(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    headers: bool = ...,
                    includeDeleted: bool = ...,
                    **kwargs: typing.Any
                ) -> ListContainerVersionsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
                def restore(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: CreateContainerVersionRequestVersionOptions = ...,
                    **kwargs: typing.Any
                ) -> CreateContainerVersionResponseHttpRequest: ...
                def undelete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    **kwargs: typing.Any
                ) -> ContainerVersionHttpRequest: ...
                def publish(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    containerVersionId: str,
                    fingerprint: str = ...,
                    **kwargs: typing.Any
                ) -> PublishContainerVersionResponseHttpRequest: ...
            class TriggersResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Trigger = ...,
                    **kwargs: typing.Any
                ) -> TriggerHttpRequest: ...
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
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    triggerId: str,
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
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListTriggersResponseHttpRequest: ...
            class VariablesResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    variableId: str,
                    **kwargs: typing.Any
                ) -> VariableHttpRequest: ...
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Variable = ...,
                    **kwargs: typing.Any
                ) -> VariableHttpRequest: ...
                def list(
                    self, *, accountId: str, containerId: str, **kwargs: typing.Any
                ) -> ListVariablesResponseHttpRequest: ...
                def delete(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    variableId: str,
                    **kwargs: typing.Any
                ) -> googleapiclient.http.HttpRequest: ...
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
            class TagsResource(googleapiclient.discovery.Resource):
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
                def create(
                    self,
                    *,
                    accountId: str,
                    containerId: str,
                    body: Tag = ...,
                    **kwargs: typing.Any
                ) -> TagHttpRequest: ...
            class FoldersResource(googleapiclient.discovery.Resource):
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
                def entities(self) -> EntitiesResource: ...
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
            def update(
                self,
                *,
                accountId: str,
                containerId: str,
                body: Container = ...,
                fingerprint: str = ...,
                **kwargs: typing.Any
            ) -> ContainerHttpRequest: ...
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
            def environments(self) -> EnvironmentsResource: ...
            def move_folders(self) -> Move_foldersResource: ...
            def versions(self) -> VersionsResource: ...
            def triggers(self) -> TriggersResource: ...
            def variables(self) -> VariablesResource: ...
            def tags(self) -> TagsResource: ...
            def folders(self) -> FoldersResource: ...
            def reauthorize_environments(self) -> Reauthorize_environmentsResource: ...
        def update(
            self,
            *,
            accountId: str,
            body: Account = ...,
            fingerprint: str = ...,
            **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def get(
            self, *, accountId: str, **kwargs: typing.Any
        ) -> AccountHttpRequest: ...
        def list(self, **kwargs: typing.Any) -> ListAccountsResponseHttpRequest: ...
        def permissions(self) -> PermissionsResource: ...
        def containers(self) -> ContainersResource: ...
    def accounts(self) -> AccountsResource: ...

class TriggerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Trigger: ...

class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFoldersResponse: ...

class ListEnvironmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListEnvironmentsResponse: ...

class ContainerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Container: ...

class AccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Account: ...

class ListAccountUsersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAccountUsersResponse: ...

class FolderEntitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FolderEntities: ...

class PublishContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PublishContainerVersionResponse: ...

class ListAccountsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAccountsResponse: ...

class TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Tag: ...

class VariableHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Variable: ...

class EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Environment: ...

class ListVariablesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVariablesResponse: ...

class ListContainersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListContainersResponse: ...

class ListTriggersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTriggersResponse: ...

class ListContainerVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListContainerVersionsResponse: ...

class UserAccessHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserAccess: ...

class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Folder: ...

class ListTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTagsResponse: ...

class CreateContainerVersionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateContainerVersionResponse: ...

class ContainerVersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ContainerVersion: ...
