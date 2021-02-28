import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class RealTimeBiddingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BiddersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def watch(
                self,
                *,
                parent: str,
                body: WatchCreativesRequest = ...,
                **kwargs: typing.Any
            ) -> WatchCreativesResponseHttpRequest: ...
        @typing.type_check_only
        class PretargetingConfigsResource(googleapiclient.discovery.Resource):
            def activate(
                self,
                *,
                name: str,
                body: ActivatePretargetingConfigRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedApps(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedAppsRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedPublishers(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedPublishersRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def addTargetedSites(
                self,
                *,
                pretargetingConfig: str,
                body: AddTargetedSitesRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: PretargetingConfig = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListPretargetingConfigsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: PretargetingConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedApps(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedAppsRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedPublishers(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedPublishersRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def removeTargetedSites(
                self,
                *,
                pretargetingConfig: str,
                body: RemoveTargetedSitesRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
            def suspend(
                self,
                *,
                name: str,
                body: SuspendPretargetingConfigRequest = ...,
                **kwargs: typing.Any
            ) -> PretargetingConfigHttpRequest: ...
        def creatives(self) -> CreativesResource: ...
        def pretargetingConfigs(self) -> PretargetingConfigsResource: ...
    @typing.type_check_only
    class BuyersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CreativesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Creative = ..., **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "CREATIVE_VIEW_UNSPECIFIED", "SERVING_DECISION_ONLY", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ListCreativesResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Creative = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> CreativeHttpRequest: ...
        @typing.type_check_only
        class UserListsResource(googleapiclient.discovery.Resource):
            def close(self, *, name: str, body: CloseUserListRequest = ..., **kwargs: typing.Any) -> UserListHttpRequest: ...  # type: ignore
            def create(
                self, *, parent: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def getRemarketingTag(
                self, *, name: str, **kwargs: typing.Any
            ) -> GetRemarketingTagResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListUserListsResponseHttpRequest: ...
            def open(
                self,
                *,
                name: str,
                body: OpenUserListRequest = ...,
                **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
            def update(
                self, *, name: str, body: UserList = ..., **kwargs: typing.Any
            ) -> UserListHttpRequest: ...
        def getRemarketingTag(
            self, *, name: str, **kwargs: typing.Any
        ) -> GetRemarketingTagResponseHttpRequest: ...
        def creatives(self) -> CreativesResource: ...
        def userLists(self) -> UserListsResource: ...
    def bidders(self) -> BiddersResource: ...
    def buyers(self) -> BuyersResource: ...

@typing.type_check_only
class CreativeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Creative: ...

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
class GetRemarketingTagResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetRemarketingTagResponse: ...

@typing.type_check_only
class ListCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListCreativesResponse: ...

@typing.type_check_only
class ListPretargetingConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListPretargetingConfigsResponse: ...

@typing.type_check_only
class ListUserListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListUserListsResponse: ...

@typing.type_check_only
class PretargetingConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PretargetingConfig: ...

@typing.type_check_only
class UserListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UserList: ...

@typing.type_check_only
class WatchCreativesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> WatchCreativesResponse: ...
